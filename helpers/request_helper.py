def email_exists_in_file(email: str, file_path: str = 'valid_emails.txt') -> bool:
    """Проверяет, существует ли указанный email в файле. email: Электронная почта для проверки. file_path: Путь к файлу. return: True, если email найден в файле, иначе False."""
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return email + '\n' in lines
    except FileNotFoundError:
        return False

   
