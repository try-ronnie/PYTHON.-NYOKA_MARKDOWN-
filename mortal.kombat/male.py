from character import Character


class Male(Character):
    def __init__(self, first_name, last_name, health, fighting_style):
        super().__init__(first_name, last_name, health)
        self.fighting_style = fighting_style
    
    def take_damage(self , damage):
        self.health -= damage
         
# Exactly! ✅
# self.attribute is only for attributes that belong to the instance.
# Parameters passed to the method (like damage) are just local variables, so you use them directly, not self.damage.
# # Using self.damage only works if you did something like self.damage = damage earlier in the instance.
# # 3 remember that to refer to the instance 
# and note you dont have super().method if its just returnong a value ..... if its a public attribute the child can also work on it directly since its just like the parent but now modifies it 
# >>>>>>super() use
# Only needed if you want to call a parent method (e.g., to reuse or extend its behavior).
# If you just access or modify a public attribute, you can do it directly (self.health -= damage).
