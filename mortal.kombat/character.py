class Character:
    def __init__(self , first_name , last_name , health):
        self.first_name = first_name
        self.last_name = last_name
        self.health = health
    def get_health(self):
        return self.health
