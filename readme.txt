                  Dungeons and Pythons
===================================================================
                          _,..,,,_ 
                     '``````~-~-,_`-,_
        .~-~-.                    `~:. `-.     
   >~~~-.     ;                      `:.  `-,     _.-~-~-~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '.
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `~-~`   .:.  `.       ;    ;
        `-.__,-~                  `-.        ,' ':    '.__.`    :'
                                     `--..--'     ':.         .:'
                                                     ':..___.:'

    My own implementation of the game Dungeons and Pythons, a project
from the course Hack Bulgaria.
The game can be started by running main.py (at least python3.3 needed!).
*edit:
- all tests can be run by entering 'py test.py' (or whatever your python command is)
- test code coverage can be displayed by entering 'py test.py coverage'
**you must have the pypi coverage module in order to do the latter, which
can be downloaded from here: https://pypi.python.org/pypi/coverage/3.7.1

Current version:
* has three heroes with different difficulties. From easiest to hardest:
- Sharik
- Arya
- Silmarillion

* has game difficulty from 1 to 3
- difficulty 'x' means, you have to go through 'x' maps to win

* enemies:
- pythons: these are the easiest enemies. You don't get bonuses for
beating them.
- anacondas: these are the harder (hardest) ones. The 'x' level has
'x' anacondas on it. For every slained anaconda you get critical hit,
health and damage bonuses.

* items:
- weapons
- potions
- by stepping on an item field, the chances for getting weapon and potion
are equal

* weapons:
- dagger (tier 1)
- staff (tier 2)
- bow (tier 2)
- rapier (tier 2)
- elder rod (tier 3)
- snaken bow (tier 3)
- long sword (tier 3)
- you can get tier 'x' weapon on 'x'th level

* maps:
- currently, there are only three maps

The available commands while in the game are:
* instructions - prints some help
* status - prints current champion's stats
* inventory - prints the weapon you own
* move <direction> - moves the champion in these direction
    if it's not outside the map or obstacle.
* exit

Map:
* # - a field you can't step on
* . - a free/path field
* I - an item field
* P - a python field
* A - an anaconda field

If you step on P or A field, the fight starts!