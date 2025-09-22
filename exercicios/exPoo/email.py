
class Email:
    def enviar(self, mensagem):
        print("Caixa de entrada:")
        print(f"Novo email: '{mensagem}'")
        print("-------------------------------")

class SMS:
    def enviar(self, mensagem):
        print("SMSs:")
        print(f"SMS: '{mensagem}'")
        print("-------------------------------")

class Notificacao:
    def enviar(self, mensagem):
        print(f"Nova notificação: '{mensagem}'")
        print("-------------------------------")

def notificar_usuario(comunicador, mensagem):
    comunicador.enviar(mensagem)

email = Email()
sms = SMS()
notification = Notificacao()

notificar_usuario(email, "Sua fatura chegou...")
notificar_usuario(email, "Estamos em promoção, venha conferir...")
notificar_usuario(sms, "Seu código de verificacção é: 43746736")
notificar_usuario(sms, "Você tem uma ligação perdida de (11) 99999-3333")
notificar_usuario(notification, "Você tem uma nova mensagem!")
notificar_usuario(notification, "@fulano curtiu sua publicação")