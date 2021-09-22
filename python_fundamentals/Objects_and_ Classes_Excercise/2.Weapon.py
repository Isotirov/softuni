class Weapon:
    def __init__(self, number_bullets):
        self.num_bullets = number_bullets

    def shoot(self):
        if self.num_bullets <= 0:
            return "no bullets left"
        self.num_bullets -= 1
        return "shooting…"

    def __repr__(self):
        return f"Remaining bullets: {self.num_bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
