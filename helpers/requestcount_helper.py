import random

class RequestDataHelper:
    @staticmethod
    def valid_payload():
        return {"count_email": random.randint(3, 10), "url": "http://любойадресзаглушка"}

    @staticmethod
    def invalid_payload():
        opts = [
            {"count_email": random.choice([1, 2, 11, 12]), "url": "http://любойадресзаглушка"},
            {"count_email": "not an int", "url": "http://любойадресзаглушка"},
            {"count_email": None, "url": "http://любойадресзаглушка"}
        ]
        return random.choice(opts)
