from SatFileReader import Reader

class Lexer:
    def __init__(self, *contents):
        self.contents = contents
        self.commands = []

    def read(self):
        for string in self.contents:
            for el in string:
                self._parseString(el)
        

    #чекает всю строчку
    def _parseString(self, command):
        ## Исправить хрень с тем, что парсер работает криво
        print(command)
        if (command[0] == 'use'):
            if (len(command) != 2):
                return self._error('command use have only one fuckin argument!', 102)
            
            if (command[1] == 'chromium' or command[1] == 'firefox'):
                return self._error(f'unknown argument >> {command[1]} <<', 101)

            # Логика слениума
        return self._error(f'unkown command >> {command[0]} << please read the fucking documentation before doing anything', 101)

    def _error(self, msg, code):
        print('lexer error: ' + msg)
        return code

reader = Reader('test.sat')
lexer = Lexer(reader.readFile())
lexer.read()