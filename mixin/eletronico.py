from log import LogFileMixin, LogPrintMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        if self._ligado:
            msg = f'{self._nome} ja esta ligado'
            self.log_error(msg)
        else:
            msg = f'{self._nome} ligou'
            self.log_success(msg)
        return super().ligar()


    def desligar(self):
        if not self._ligado:
            msg = f'{self._nome} ja esta desligado'
            self.log_error(msg)
        else:
            msg = f'{self._nome} desligou'
            self.log_success(msg)
        return super().desligar()

iPhone = Smartphone('Iphone')

iPhone.ligar()
iPhone.ligar()
iPhone.desligar()
iPhone.desligar()
