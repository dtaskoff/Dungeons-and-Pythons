import gameplay


def welcome_screen():
    print("welcome to dungeons and pythons v0.00!")
    print("-" * 40)

def pick_difficulty():
    picked_difficulty = int(input("choose a difficulty(1-3): "))

    if picked_difficulty > 3 or picked_difficulty < 1:
        picked_difficulty = 0
        print("you chose an invalid difficulty! demo mode started")

    return gameplay.Gameplay(picked_difficulty)

def pick_a_hero(game):
    print(game.list_heroes())
    picked_hero = input("choose a hero: ")

    while not game.hero_exists(picked_hero):
        print("you entered incorrect name")
        picked_hero = input("choose a hero: ")

    game.add_hero(picked_hero)

def stepped_on_an_anaconda():
    print('\n'.join(["you dared to wake up the anaconda!",
            "now you're in trouble..\n"]))

def stepped_on_a_python():
    print("you stepped on a python!\n")

def init_fight(hero, enemy):
    print("{} vs {}\n".format(hero, enemy))

def status(hero, enemy):
    print("{}\n\n{}\n".format(hero, enemy))

def game_over():
    print("game over..")

def beaten_the(enemy):
    print("good job\nyou've beaten the {}\n\n".format(enemy))

def damage_dealt(hitter, damage):
    print("{} dealt {} damage\n".format(hitter, damage))

def hero_bonuses(health_bonus, damage_bonus):
    print("you got bonus for beating the anaconda:")
    print("your max health is now {}".format(health_bonus))
    print("your damage is now {}".format(damage_bonus))

def weapon_bonuses(damage_bonus, crit_bonus):
    print("your weapon damage is now {}".format(damage_bonus))
    print("your critical strike chance is now {}%".format(crit_bonus * 100))

def eaten_by_a_snake():
    print("you have been eaten by a snake..")