# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Ishmael", color='#56638A')
define q = Character("Queequeg", color='#FCB0B3')
define a = Character("Ahab", color="#0060f0")
define s = Character("Starbuck", color="#BF2155")
define b = Character("Stubb", color="#000000")
define f = Character("Flask", color="#82D173")
define t = Character("Tashtego")
define d = Character("Dagoo")
define m = Character("Moby Dick")

default book = False
default ahabCharm = 0
default queequegCharm = 0
default starbuckCharm = 0

# The game starts here.
label start:
    jump scene1_0
    return
