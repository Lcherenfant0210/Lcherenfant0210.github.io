"""COP 1500 Integration Project - Text-based game."""
__author__ = "Leo Cherenfant"
import time


def main():
    """The opening sequence of the game, asks for name, choice to start, and
    then loads the choices."""
    # Leo Cherenfant
    # This is a simple text based adventure game
    # asks for players name and print introduction
    player_name = input("Name: ")
    print("Your name is", player_name)

    # added time for effect, and so I can use more operators
    time.sleep(2)
    print("Hello", player_name, "and welcome to this adventure game!")
    time.sleep(2)

    # establishes player's health pool

    health = 10

    start = input("Do you wish to embark on this adventure? ")

    if start == "yes":
        print("Then lets begin!")
        time.sleep(1)
# prints the word loading with three periods
        load = "." * 3
        print("loading" + load)
        time.sleep(1)
# prints three dots in three sec, 0.40 second delay between each print
        count = 0
        while count != 3:
            print(".", end="")
            time.sleep(.40)
            count += 1
        print("\nHealth: ", health, sep='')
        print("It begins...")
        time.sleep(1)

# skipping dialogue and just putting in the choices for now

        choice_direction = input("enter left door or right door? ")
        if choice_direction == "left" or "right":
            print("You enter the door and find a box with potions")
        else:
            print("Error: Please choose left or right")

        potion = ["red", "blue", "green", "orange", "pink", "white", "black"]

        def potion_func(potion):
            """This asks the player for which potion they want and then
            sets the parameters for what each potion does."""
            for x in range(1):
                print(potion)

        potion_func(potion)

        player_potion = input("Choose a potion.. ")

        if player_potion == "red":
            print("You drank the red potion and it healed you!")
            time.sleep(1)

        # assigning potion value using basic ops to modify the players health

            red_potion = 2
            health = (health + red_potion)
            print("Health: ", health)

        elif player_potion == "blue":
            print("You drank the blue potion and it harmed you!")
            time.sleep(1)
            blue_potion = 2
            health = (health - blue_potion)
            print("Health: ", health)

        elif player_potion == "green":
            print("You drank the green potion and it healed you!")
            time.sleep(1)
            green_potion = 2
            health = (health * green_potion)
            print("Health: ", health)

        elif player_potion == "orange":
            print("You drank the orange potion and it harmed you!")
            time.sleep(1)
            orange_potion = 2
            health = (health / orange_potion)
            print("Health: ", health)

        elif player_potion == "pink":
            print("You drank the pink potion and it harmed you!")
            time.sleep(1)
            pink_potion = 2
            health = (health % pink_potion)
            print("Health: ", health)

        elif player_potion == "white":
            print("You drank the white potion and it healed you!")
            time.sleep(1)
            white_potion = 2
            health = (health ** white_potion)
            print("Health: ", health)

        elif player_potion == "black":
            print("You drank the black potion and it harmed you!")
            time.sleep(1)
            black_potion = 2
            health = (health // black_potion)
            print("Health: ", health)
    while health < 10:
        if health == 5:
            print("you are at half health")
        # here is my usage of "and"
        if 1 < health <= 3:
            print("you are at critical health")

        if not (health > 0):
            print("you have died")
            print("Health: ", health)
        break

    print("That's all so far.")


main()
# So far the game is only a potion simulator.
# also need to add a functional game over system and more choices
# reference:
# https://cppsecrets.com/users/5617971101051071011161151049711410997484852494964103109971051084699111109/Text-based-Adventure-Game-using-Python.php
# reference:
# https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
# reference:
# https://stackoverflow.com/questions/50473861/tracking-player-health-text-based-game-python
