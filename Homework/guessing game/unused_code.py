
    #dictionary to store the different game modes
    d_games = {1: f_user_guesses_number, 2: f_computer_guesses_number, 3: f_global_thermonuclear_war}

    #calls the function, like a switch statement, based on the selection from the user
    v_selection = f_prompt_user()

    #test user input for proper input