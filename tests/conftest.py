import pytest
import os


@pytest.fixture
def delete_vaild_emails_file():
    file_path = 'valid_emails.txt'
    open(file_path, 'w').close()
    yield file_path
    
    if os.path.exists(file_path):
        os.remove(file_path)