class User:
    user_id: int
    name: str
    email: str
    signup_date:str

    def __init__(self, user_id, name, email, signup_date):
        self.user_id = int(user_id)
        self.name = name.strip()
        self.email = email.strip()
        self.signup_date = signup_date.strip()