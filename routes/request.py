
class Request:
    """
Класс для отправки email-запросов и проверки их валидности.  """

    URL = 'http://new_learn_url'

    @staticmethod
    def post(email: str, url: str = URL) -> int:
        """
        Отправляет email на сервер, проверяя его валидность.

        Args:
            email (str): Электронная почта для проверки.
            url (str, optional): URL сервера. По умолчанию `http://new_learn_url`.

        Returns:
            int: 200 если email валиден и сохранён, иначе 404.
        """
        if not isinstance(email, str) or not email:
            return 404  # Проверка на None и неверный тип

        email = email.strip()  # Убираем лишние пробелы по краям

        invalid_conditions = [
            ' ' in email,             # Пробелы в email
            len(email) <= 4,          # Длина менее 5 символов
            '..' in email,            # Двойная точка
            email.count('@') != 1,    # Должна быть одна '@'
            email.startswith('@'),    # '@' в начале
            email.endswith('@'),      # '@' в конце
            email.rfind('.') <= email.find('@'),  # Точка должна быть после '@'
            email.endswith('.'),      # Не может заканчиваться на точку
            email[email.find('@') + 1] == '.'  # '@.' недопустимо
        ]

        if any(invalid_conditions):
            return 404

        # Сохраняем email в файл, если он прошёл все проверки
        with open('valid_emails.txt', 'a', encoding='utf-8') as file:
            file.write(email + "\n")

        return 200

    