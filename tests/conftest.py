import pytest
import os


@pytest.fixture
def delete_vaild_emails_file():
    """Фикстура для создания пустого файла 'valid_emails.txt' перед выполнением теста и его удаления после теста. yield: Путь к созданному файлу."""
    file_path = 'valid_emails.txt'
    open(file_path, 'w').close()
    yield file_path
    
    if os.path.exists(file_path):
        os.remove(file_path)