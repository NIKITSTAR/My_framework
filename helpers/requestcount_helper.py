from random import choice, randint

class RequestDataHelper:
    """Класс для генерации валидных и невалидных payload'ов."""
    @staticmethod
    def valid_payload():
        """Возвращает валидный payload с корректным значением 'count_email' в диапазоне от 3 до 10 и валидным URL.

        Returns:
            dict: Словарь с ключами `count_email` и `url`.
        """
        return {"count_email": randint(3, 10), "url": "http://любойадресзаглушка"}

    @staticmethod
    def invalid_payload():
        """Возвращает случайный невалидный payload, где значение count_email может быть числом вне допустимого диапазона, строкой или None.

        Returns:
            dict: Словарь с ключами `count_email` и `url`."""
        opts = [
            {"count_email": choice([1, 2, 11, 12]), "url": "http://любойадресзаглушка"},
            {"count_email": "not an int", "url": "http://любойадресзаглушка"},
            {"count_email": None, "url": "http://любойадресзаглушка"}
        ]
        return choice(opts)
