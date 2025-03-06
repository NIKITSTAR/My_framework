

def email_exists_in_file(email, file_path='valid_emails.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return email + '\n' in lines
    except FileNotFoundError:
       return False 
   
