class ConnectionException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Não foi possivel se conectar com o banco de dados')


class InvalidJSON(Exception):
    def __init__(self):
        Exception.__init__(self, 'JSON Invalido')
