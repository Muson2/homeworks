import argparse
import hw6month3

parser = argparse.ArgumentParser(description="User CLI")
subparsers = parser.add_subparsers(dest='command')


parser_add = subparsers.add_parser('add')
parser_add.add_argument('--name', required=True)
parser_add.add_argument('--age', required=True)
parser_add.add_argument('--email')
parser_add.add_argument('--phone')
parser_add.add_argument('--job')



parser_update = subparsers.add_parser('update')
parser_update.add_argument('--id', required=True, type=int)
parser_update.add_argument('--name')
parser_update.add_argument('--age')
parser_update.add_argument('--email')
parser_update.add_argument('--phone')
parser_update.add_argument('--job')


parser_list = subparsers.add_parser('list')

args = parser.parse_args()

if args.command == 'add':
    conn = hw6month3.connect_db()
    conn.execute("INSERT INTO users (name, age, email, phone, job) VALUES (?, ?, ?, ?, ?)",
                 (args.name, args.age, args.email, args.phone, args.job))
    conn.commit()
    conn.close()
    print(f"Пользователь {args.name} добавлен.")

elif args.command == 'update':
    updated = hw6month3.update_user(args.id, args.name, args.age, args.email, args.phone, args.job)
    if updated:
        print(f"Пользователь ID={args.id} обновлён.")
    else:
        print("Пользователь не найден или не указаны поля для обновления.")

elif args.command == 'list':
    conn = hw6month3.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, email, job FROM users")
    rows = cursor.fetchall()

    print(f"{'ID':<4} | {'Name':<15} | {'Age':<5} | {'Email':<25} | {'Job'}")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]:<4} | {row[1]:<15} | {row[2]:<5} | {row[3]:<25} | {row[4] or '-'}")
    conn.close()
