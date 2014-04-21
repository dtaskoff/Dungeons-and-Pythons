# the script that runs the whole game
import gameplay
import ui


# briefly: gets input from the keyboard to manipulate
# the whole action in a cycle that runs
# until we win or we get eaten
def main():
    ui.welcome_screen()
    
    game = gameplay.Gameplay(ui.pick_difficulty())
    hero_name = ui.pick_a_hero(game)

    while game.in_game():
        ui.visualise_map(game)
        ui.execute_command()


if __name__ == '__main__':
    main()