class Notification:
    def send(self):
        pass

class SMSNotification(Notification):
    def send(self):
        print("Вам пришло сообщение")
        return super().send()
    def set_message(self, messe):
        message = input("Введите сообщение: ")
        self.messe = messe
        self.messe = message
    def _message(self):
        print("Сообщение: "+ self.messe)
    
class EmailNotification(Notification):
    def send(self):
        print("Вам пришло письмо на почту")
        return super().send()
    def _message(self):
        print("Сообщение" + self.meese)
    def set_message(self, messe):
        message = input("Введите сообщение")
        self.meese = messe
        self.messe = message

notif = SMSNotification()
notif.send()
notif.set_message("1")
notif._message()