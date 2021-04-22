import sys as s

class Lexer:
    def __init__(self, *contents):
        self.contents = contents.split(' ')
        self.commands = []

    def read(self):
        for string in self.contents:
            print(string)

    #чекает всю строчку
    def _parseString(self, string):
        ## Исправить хрень с тем, что парсер работает криво
        if (command_list[0] == 'use'):
            if (len(command_list) != 2):
                return self._error('command use have only one fuckin argument!', 102)
            
            if (command_list[1] != 'chromium' or command_list[1] != 'firefox'):
                return self._error('unknown argument!', 101)

        errMsg = 'unkown command >> ' + string[0] + ' << please read the fucking documentation before doing anything'
        return self._error(errMsg, 101)

    def _error(self, msg, code):
        print('lexer error: ' + msg)
        return code

lol = Lexer('use chromium use firefox')
lol.read()
