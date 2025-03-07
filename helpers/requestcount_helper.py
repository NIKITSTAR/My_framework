import random

class RequestDataHelper:
    @staticmethod
    def valid_payload():
        """Возвращает валидный payload с корректным значением 'count_email' в диапазоне от 3 до 10 и валидным URL. return: Словарь с ключами count_email и url"""
        return {"count_email": random.randint(3, 10), "url": "http://любойадресзаглушка"}

    @staticmethod
    def invalid_payload():
        """Возвращает случайный невалидный payload, где значение count_email может быть числом вне допустимого диапазона, строкой или None. return: Словарь с ключами count_email и url"""
        opts = [
            {"count_email": random.choice([1, 2, 11, 12]), "url": "http://любойадресзаглушка"},
            {"count_email": "not an int", "url": "http://любойадресзаглушка"},
            {"count_email": None, "url": "http://любойадресзаглушка"}
        ]
        return random.choice(opts)
