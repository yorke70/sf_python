class APIException(Exception):
    pass


class ValPairDoesNotExist(APIException):
    def __str__(self):
        return "Валютная пара недоступна, попробуйте другую"


class InvalidRequestTemplate(APIException):
    def __str__(self):
        return "Неверный запрос, воспользуйтесь примером в справке /help"


class WrongAmount(APIException):
    def __str__(self):
        return "Указано неверное количество для обмена"
