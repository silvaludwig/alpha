from pathlib import Path


LOG_FILE = Path(__file__).parent/'log.txt'


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o metodo Log')
    
    def log_error(self, msg):
        return self._log(f'Log Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Log Success: {msg}')

class LogFileMixin(Log):    
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as file:
            file.write(msg_format)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':    
    log_print = LogPrintMixin()
    log_print.log_error('Qualquer coisa')
    log_print.log_success('Bom demais')

    log_file_ = LogFileMixin()
    log_file_.log_error('Qualquer coisa')
    log_file_.log_success('Bom demais')

    # print(log_file)
