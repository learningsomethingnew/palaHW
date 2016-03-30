import sys
import os
from time import sleep, time
from webbrowser import open_new

# min max for random generator
v_min_range = 1
v_max_range = 100

# list of numbers for binary search
ls_potential_numbers = [x for x in range(101)]


##################################################################################
# Graphics #
##################################################################################

# clears the screen for easier player tracking
def f_clear_console():
    # f_print_text("\n"* 20, True)
    os.system('cls' if os.name == 'nt' else 'clear')


# displays text as if someone is typing
def f_print_text(a_string, a_is_slow):
    if a_is_slow:
        for words in a_string + "\n":
            sys.stdout.write(words)
            sys.stdout.flush()
            sleep(.03)
    else:
        print(a_string)


# print banners for visuals
def f_banner(a_type_of_banner):
    # la denotes line art string
    la_main_menu_banner = "^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^*^"
    # banner used between guesses
    la_game_banner = "^------------------------------------------------------------^"

    # decides which banner to be used
    if a_type_of_banner == 1:
        # printing of graphics
        f_print_text(la_main_menu_banner, False)
    elif a_type_of_banner == 2:
        f_print_text(la_game_banner, False)


##################################################################################
# Game 1: Player Guesses Computer's Number #
#################################################################################

def f_user_guesses_number():
    # clear the console
    f_clear_console()

    f_print_text("    Can you guess the number that I'm thinking of?", True)
    f_print_text("    The number is between 1 - 100", True)
    f_print_text("    You can type 'Quit' or 'quit' to go back to the main menu", True)

    # banner
    f_banner(2)

    # start the game loop
    f_user_guess_game_loop()


# Loop that manages the game state
def f_user_guess_game_loop(a_list_coming_in):
    # variable for player guesses
    v_player_attempts = 0
    v_previous_player_guess = -1

    # the random number for the player to guess
    v_ran_number = f_random_number_generator()
    # print("RANDOM NUNBER IS " + str(v_ran_number))

    # while loop manages the number of guesses. Allows player to quit
    while v_player_attempts < 5:
        v_player_guess = f_prompt_user()
        v_player_attempts += 1

        # allows player to escape to menu
        if v_player_guess == 'quit':
            f_print_text("    Until next time player.", True)
            f_print_text("    Returning to main menu", True)
            f_main()
        # if player entered something other than a number
        elif v_player_guess == False:
            continue

        # catches players duplicate answer
        elif v_player_guess == v_previous_player_guess:
            f_print_text("    Hello? Player, are you still ok?", True)
            f_print_text("    You guessed the same number as before", True)
            f_print_text("    You have " + str(5 - v_player_attempts) + " chance(s) left", True)
            f_banner(2)

        # players guess within 10 places of the number
        elif abs(v_player_guess - v_ran_number) > 1 and abs(v_player_guess - v_ran_number) < 10:
            v_previous_player_guess = v_player_guess
            f_print_text("    Player, you're super close!", True)
            f_print_text("    You have " + str(5 - v_player_attempts) + " chance(s) left", True)
            f_banner(2)

        # notifies the player their guess is being wasted high
        # probably need to store the player's guess as a list and then
        # compare their guesses to see if they are throwing away answers
        # ran out of time

        # player guess is too high
        elif v_player_guess > v_ran_number:
            v_previous_player_guess = v_player_guess
            f_print_text("    Your guess is too high player", True)
            f_print_text("    You have " + str(5 - v_player_attempts) + " chance(s) left", True)
            f_banner(2)

        # player guess is too low
        elif v_player_guess < v_ran_number:
            v_previous_player_guess = v_player_guess
            f_print_text("    Your guess is too low player", True)
            f_print_text("    You have " + str(5 - v_player_attempts) + " chance(s) left", True)
            f_banner(2)

        # player guessed correctly
        elif v_player_guess == v_ran_number:
            f_print_text("    Congrats player, you guessed my number", True)
            f_print_text("    Returning back to the main menu\n\n", True)
            f_banner(2)
            sleep(3)
            f_main()

    # player ran out of guesses
    f_print_text(" Better luck next time player", True)
    f_print_text(" My number was " + str(v_ran_number), True)
    sleep(3)
    f_main()


##################################################################################
# Computer guesses player's number #
##################################################################################
def f_computer_guesses_number():
    # start with a clean screen
    f_clear_console()

    # Game instructions
    f_print_text("Check back again player, this feature is in development", True)
    f_print_text("Now being returned back to the main menu", True)
    f_clear_console()
    f_greeting()

    # f_print_text("    Player, please think of a number between 1 & 100", True)
    # f_print_text("    Don't change that number on me now", True)
    # f_print_text("    You can type 'Quit' or 'quit' to go back to the main menu", True)

    # banner for breaking up the display
    # f_banner(2)

    # starts the game loop
    # f_computer_guess_game_loop()


# Loop that manages the game state
def f_computer_guess_game_loop():
    # variable for player guesses
    v_computer_attempts = 0

    # the random number for the player to guess
    v_ran_number = f_random_number_generator()

    # while loop manages the number of guesses. Allows player to quit
    while v_computer_attempts < 5:
        v_computer_attempts += 1

        # starting point of guessing
        v_computer_guess = f_random_number_generator()

        # asks the player what their number is
        f_print_text("Is your number " + str(v_computer_guess) + "?", True)
        f_print_text("Enter '1' for high, '2' for low, or '3' if I got it correct", True)

        # Asks the player if the computer is close to the number
        v_player_response = f_prompt_user()
        # allows player to escape to menu
        if v_player_response == 'quit':
            f_print_text("    Until next time player.", True)
            f_print_text("    Returning to main menu", True)
            f_main()
        # if player entered something other than a number
        elif v_player_response == False:
            continue
        elif v_player_response == 1:
            f_remove_numbers_higher_than(v_computer_guess)

            # catches players duplicate answer


##################################################################################
# List Manipulation #
##################################################################################

# removes numbers great than the initial guess
def f_remove_numbers_higher_than(a_computer_guess):
    for number in ls_potential_numbers:
        if a_computer_guess <= number:
            ls_potential_numbers.remove(number)
    print(ls_potential_numbers)


# removes numbers less than initial guess
def f_remove_numbers_less_than(a_computer_guess):
    for number in ls_potential_numbers:
        if a_computer_guess >= number:
            ls_potential_numbers.remove(number)
    print(ls_potential_numbers)


# check to see if the player has lied
def f_number_outside_of_list():
    return


##################################################################################
# Global Thermonuclear War #
##################################################################################
def f_global_thermonuclear_war():
    f_print_text("GREETINGS PROFESSOR FALKEN", True)
    f_print_text("HOW ARE YOU FEELING TODAY?", True)
    sleep(2)
    open_new('https://www.youtube.com/embed/m4wk6jSNZU8?rel=0&autoplay=1')
    sleep(1)

    f_clear_console()
    f_print_text("Now being returned back to the main menu", True)
    f_greeting()


def f_user_entered_non_number():
    f_print_text("Player, please only use whole numbers. No characters", True)


##################################################################################
# Random Number Generator #
##################################################################################

# inspired by SO
def f_random_number_generator():
    v_current_time = time()
    v_time_difference = v_current_time - float(str(v_current_time).split('.')[0])
    v_random_number = int(v_time_difference * (v_max_range - v_min_range) + v_min_range)
    return v_random_number


##################################################################################
# Controls #
##################################################################################

# Takes input from the user
def f_prompt_user():
    # catches the user's input for testing
    v_user_input = input(">>>")
    if v_user_input == "quit" or v_user_input == "Quit":
        return "quit"
    try:
        int(v_user_input)
        return int(v_user_input)
    except ValueError:
        f_print_text("Player please enter in only whole numbers.", True)
        return False


##################################################################################
# Main Functions Before Games#
##################################################################################

# user selects which game and the selection will start that game
def f_main():
    f_clear_console()
    f_greeting()

    # variable that controls the run state
    v_run = True

    # run loop
    while v_run == True:
        v_user_input = f_prompt_user()
        if v_user_input == False:
            continue
        elif v_user_input == "quit":
            sys.exit(0)
        else:
            f_game_selection(v_user_input)


# Greeting for the player
def f_greeting():
    # banners
    f_banner(1)
    f_banner(1)

    # printing of welcome message text
    f_print_text("                   SHALL WE PLAY A GAME?" + "\n" + "\n", True)
    f_print_text("1. You Guess My Number", True)
    f_print_text("2. I Guess Your Number", True)
    f_print_text("3. Global Thermonuclear War", True)
    f_print_text("Type 'Quit' or 'quit' to quit", True)


# game selection
def f_game_selection(a_game_mode):
    # dictionary to store the different game modes
    d_games = {1: f_user_guesses_number, 2: f_computer_guesses_number, 3: f_global_thermonuclear_war}

    # calls the function, like a switch statement, based on the selection from the user
    d_games[a_game_mode]()
    # test user input for proper input


f_main()
# f_print_text("this is a test string", True)
# f_print_text("this is a slow string", False)
