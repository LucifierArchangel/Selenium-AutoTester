from SatFileReader import Reader


class Lexer:
    def __init__(self, seleniumController, *contents):
        self.contents = contents
        self.seleniumController = seleniumController
        self.commands = []

    def read(self):
        for string in self.contents:
            for el in string:
                errorCode = self._parseString(el)
                if self._parseString(el) < 1:
                    self.commands.append(el)
                else: 
                    return errorCode
        
    def _parseString(self, command):
        if command[0] == 'use':
            if len(command) != 2:
                return self._error('command use have only one fuckin argument!', 102)
            
            if command[1] != 'chromium' and command[1] != 'firefox':
                return self._error(f'unknown argument >> {command[1]} <<', 101)

            self.seleniumController.execute(command[0], command[1])

            return 000

        if command[0] == 'open':
            if len(command) != 2:
                return self._error('command open have only one fuckin argument!', 102)

            return 000

            # Логика слениума
        return self._error(f'unkown command >> {command[0]} << please read the fucking documentation before doing anything', 101)

    def _error(self, msg, code):
        print('lexer error: ' + msg)
        return code

if __name__ == '__main__':
    reader = Reader('test.sat')
    lexer = Lexer(reader.readFile())
    lexer.read()