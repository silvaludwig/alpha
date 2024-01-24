from log import LogFileMixin, LogPrintMixin


class Electronic:
    def __init__(self, name):
        self._name = name
        self._turned_on = False

    def turn_on(self):
        if not self._turned_on:
            self._turned_on = True

    def turn_off(self):
        if not self._turned_on:
            self._turned_on = False


class Smartphone(Electronic, LogPrintMixin):
    
    def turn_on(self):
        super().turn_on()
    
        if self._turned_on:
            msg = f'{self._name} is turned on'
            self.log_success(msg)


    
    def turn_off(self):
        super().turn_off()
        
        if not self._turned_on:
            msg = f'{self._name} is turned off'
            self.log_success(msg)
 

