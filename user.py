
class user:
    def __init__(self, user_number):
        # initial 36's cards
        self.user_number = user_number
        self.user_names = []
        self.user = {}
    def get_user_names(self):
        user_name = ["A", "B", "C", "D", "E", "F"]
        self.user_names = user_name[:self.user_number]
    def initial_user(self):
        user_full = {"A":[0,0,0], "B":[0,0,0], "C":[0,0,0], "D":[0,0,0], "E":[0,0,0], "F":[0,0,0]}
        self.get_user_names()
        for key in self.user_names:
            self.user[key] = user_full[key]