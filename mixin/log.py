# ABSTRAÇÃO
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'file.txt'

class Log():
    def _log(self, msg):
        raise NotImplementedError('implemente o metodo log') # Isso é um @abstractmethod manual
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formated = f'Error: {msg} {__class__.__name__}'
        with open(LOG_FILE, 'a') as file:
            file.write(msg_formated)
            file.write('\r\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(msg, __class__.__name__)

