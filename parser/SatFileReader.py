class Reader: 
    def __init__(self, path):
        self.path = path

    def readFile(self):
        commands = []

        file = open(self.path, 'r')

        if (file.name.split('.')[1] != 'sat'):
            return self._error('unknown file extension, the script must have the .sat extension!', 103)

        for string in file:
            el = string.replace('\n', ' ')
            el = el.split(' ')
            
            _command = []
            for lex in el: 
                if (lex != ''):
                    _command.append(lex)
            if (len(_command) > 0):
                commands.append(_command)

        if (len(commands) <= 0):
            return self._error('file empety', 104)

        file.close()
        return commands

    def _error(self, msg, code):
        print('file reader error: ' + msg)
        return code