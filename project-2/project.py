def number_guessing_game():
    target_num = generate_target_number()
    user_guess = get_user_guess()
    while user_guess != target_num:
        print_feedback_message(user_guess, target_num)
        user_guess = get_user_guess()
    print_success_message()


"""
Define a function generate_target_number():
    Parameters: N/A
    Returns: A random target number from 1 (inclusive) to 100 (inclusive).
"""


"""
Define a function get_user_guess():
    Parameters: N/A
    Side Effect: Asks user for number guess
    Returns: user's guess
"""


"""
Define a function print_feedback_message():
    Parameters: two ints user_guess, target_num
    Side Effect: Prints out feedback message of "too low" if user_guess is less than
        target_num, prints out feedback message of "too high" otherwise
    Returns: N/A
"""


"""
Define a function print_success_message():
    Parameters: N/A
    Side Effect: Prints out success message
    Returns: N/A
"""


# Play the game
number_guessing_game()
