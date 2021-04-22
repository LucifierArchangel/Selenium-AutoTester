import sys as s

class Lexer:
    def __init__(self, contents):
        self.contents = contents

        self.commands = []
    
    def read(self):
        for string in self.contents:
            self._parseString(string)
        pass

    def _error(self, msg, code):
        print('lexer error: ' + msg)
        return code
        
    #чекает всю строчку
    def _parseString(self, string):
        ## Исправить хрень с тем, что парсер работает криво
        if (command_list[0] == 'use'):
            if (len(command_list) != 2):
                self._error('command use have only one fuckin argument!', 102)
                pass
            
            if (command_list[1] != 'chromium' or command_list[1] != 'firefox'):
                self._error('unknown argument!', 101)
                pass

        errMsg = 'unkown command >> ' + string[0] + ' << please read the fucking documentation before doing anything'
        self._error(errMsg, 101)
        pass

lol = Lexer((['use chromium'], ['use firefox']))
lol.read()
