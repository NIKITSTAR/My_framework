
class request:
    URL = 'http://new_learn_url'
    
    def post(email, url=URL):
        if ' ' in email:
            return 404
        
        if len(email) <= 4:
            return 404
        
        if '..' in email:
            return 404
        
        at_index = email.find('@')
        if at_index <= 0 or at_index >= len(email) - 1:
            return 404
        
        dot_index = email.rfind('.', at_index)
        if dot_index <= at_index or dot_index >= len(email) - 1:
            return 404
        
        if dot_index - at_index <= 1:
            return 404
        
        if dot_index == len(email) - 1:
            return 404
        
        if email is None:
            return 404
        
        with open('valid_emails.txt', 'a') as file:
            file.write(email + "\n")
        
        return 200
    