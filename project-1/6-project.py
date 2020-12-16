def main():
    print_welcome_message()
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print_ending_message(user_choice, computer_choice)


"""
Define a function print_welcome_message():
    Parameters: N/A
    Side Effect: Prints welcome message
    Returns: N/A
"""


"""
Define a function get_user_choice():
    Parameters: N/A
    Side Effect: Asks user for choice of 'r'/'p'/'s'
    Returns: user input
"""


"""
Define a function get_computer_choice():
    Parameters: N/A
    Returns: random choice of 'r'/'p'/'s'
"""


"""
Define a function print_ending_message():
    Parameters: two strings user_choice, computer_choice
    Side Effect:
        prints out message displaying:
            - what choice user made
            - what choice computer made
            - who won
    Returns: N/A
"""


# Play the game
main()
