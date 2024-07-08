from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem):
        self._mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: # "->" é uma convensando que determina o retorno do metodo
        ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool: # "->" é uma convensando que determina o retorno do metodo
        print(f'Email enviado: {self._mensagem}')
        return True

class NotificacaoSms(Notificacao):
    def enviar(self) -> bool: # "->" é uma convensando que determina o retorno do metodo
        print(f'SMS enviado: {self._mensagem}')
        return True

def notificar(notificacao: Notificacao): # "notificacao: Notificacao" é uma convenção que define o tipo do paramentro
    ...

    notificar_enviada = notificacao.enviar()

    if notificar_enviada:
        print('Notificação enviada')
        return
    print('Notificação não enviada')

