import json

# Classe para definir padrão de mensagens enviadas


class Message:
    def __init__(self, type, data):
        self.type = type
        self.data = data

    def getData(self):
        try:
            return self.data.decode()
        except:
            return self.data

    def getType(self):
        try:
            return self.type.decode()
        except:
            return self.type

    def toJSON(self):
        return json.dumps(self.__dict__)
