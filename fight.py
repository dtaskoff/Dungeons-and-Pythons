# our fight module
from random import randint
import hero
import python, anaconda
import weapon
import ui


# the bonuses we get for slaining anacondas!
_health_bonus = 0.10
_damage_bonus = 0.10
_weapon_damage_bonus = 0.05
_weapon_critical_hit_chance_bonus = 0.05


class Fight():
    # fight's constructor
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    # returns true if Hero should hit first,
    # else false
    def flip_coin(self):
        chance = randint(1, 100)
        return chance >= 50

    # returns a tuple from fight's hero and enemy in the
    # following form: attacker, attacked
    def pick_order(self):
        if self.flip_coin():
            return self.hero, self.enemy

        return self.enemy, self.hero

    # some informational messages to help us know
    # what's going on during the fight
    def init_fight(self):
        enemy = "python"
        if isinstance(self.enemy, anaconda.Anaconda):
            ui.stepped_on_an_anaconda()
            enemy = "anaconda"
        else:
            ui.stepped_on_a_python()

        ui.init_fight(self.hero.known_as(), enemy)

    def status(self):
        ui.status(self.hero, self.enemy)

    # the sad one :/ (to see when playing)
    def game_over(self):
        ui.game_over()
        exit(0)

    # and the cool one
    def won(self):
        enemy = "python"

        if isinstance(self.enemy, anaconda.Anaconda):
            enemy = "anaconda"

        ui.beaten_the(enemy)

    # information about every hit during the fight
    # (i.e. damage dealt and taken)
    def battle(self, damage, attacker):
        hitter = "enemy"
        if isinstance(attacker, hero.Hero):
            hitter = "you"

        ui.damage_dealt(hitter, damage)

    # calculates the bonuses we get for slaining an anaconda
    # (no bonuses for a python, a python is easy)
    def bonus(self):
        self.hero.max_health += int(self.hero.max_health * _health_bonus)
        self.hero.damage += int(self.hero.damage * _damage_bonus)
        self.hero.health = self.hero.max_health

        ui.hero_bonuses(self.hero.max_health, self.hero.damage)

        if 'weapon' in self.hero.__dict__:
            self.hero.weapon.damage +=\
                int(self.hero.weapon.damage * _weapon_damage_bonus)

            self.hero.weapon.critical_strike_percent +=\
                self.hero.weapon.critical_strike_percent *\
                    _weapon_critical_hit_chance_bonus
            if self.hero.weapon.critical_strike_percent > 1.0:
                self.hero.weapon.critical_strike_percent = 1.0

            ui.weapon_bonuses(self.hero.weapon.damage,
                self.hero.weapon.critical_strike_percent)

    # the whole thing is happening here:
    # (we get the winner as a result from the method,
    # no idea why)
    def simulate_fight(self):
        attacker, attacked = self.pick_order()

        self.init_fight()

        while attacker.is_alive() and attacked.is_alive():
            self.status()
            damage = attacker.attack()
            self.battle(damage, attacker)
            attacked.take_damage(damage)
            attacker, attacked = attacked, attacker

        if attacker == self.hero:
            ui.eaten_by_a_snake()
            self.game_over()
        elif isinstance(attacker, anaconda.Anaconda):
            self.won()
            self.bonus()
        else:
            self.won()

        return attacked