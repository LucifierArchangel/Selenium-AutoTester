class Reader: 
    def __init__(self, path):
        self.path = path

    def readFile(self):
        commands = []

        file = open(self.path, 'r')

        if (file.name.split('.')[1] != 'sat'):
            self._error('unknown file extension, the script must have the .sat extension.', 103)
            pass

        for el in file:
            commands.append(el)

        file.close()
        return commands

    def _error(self, msg, code):
        print('file reader error: ' + msg)
        return code
        

reader = Reader('test.sat')
print(reader.readFile())

