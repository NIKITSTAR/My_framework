from faker import Faker

fake = Faker()


class Request_count:
    URL = 'http://любойадресзаглушка'

    @staticmethod
    def post(count_email, url=URL):
        """Проверяем, что count_email - целое число"""
        if not isinstance(count_email, int):
            return 404

        """Проверяем, что количество находится в допустимом диапазоне (от 2 до 11)"""
        if count_email <= 2 or count_email >= 11:
            return 404

        """Генерируем список email'ов нужной длины"""
        emails = [fake.email() for _ in range(count_email)]
        return emails


