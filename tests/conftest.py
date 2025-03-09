from pytest import fixture
from os import remove


@fixture
def delete_valid_emails_file():
    """Фикстура для очистки 'valid_emails.txt' перед тестами и удаления после тестов.

    Returns:
        str: Путь к созданному файлу.
    """
    file_path = 'valid_emails.txt'

    # Создаём пустой файл или очищаем, если уже существует
    with open(file_path, 'w', encoding='utf-8') as file:
        pass

    yield file_path  # Передаём путь к файлу в тест

    # Удаляем файл после завершения теста
    try:
        remove(file_path)
    except FileNotFoundError:
        pass
