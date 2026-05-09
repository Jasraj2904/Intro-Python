import random
from colorama import init, Fore, Style

init(autoreset=True)

def display_choices():
    print(Fore.CYAN + "\nChoose:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors\n" + Style.RESET_ALL)

def player_choice():
    choice = 0

    while choice not in [1, 2, 3]:
        try:
            choice = int(input(Fore.GREEN + "Enter your choice (1-3): " + Style.RESET_ALL))

            if choice not in [1, 2, 3]:
                print(Fore.RED + "Invalid choice! Please try again." + Style.RESET_ALL)

        except ValueError:
            print(Fore.RED + "Please enter a number between 1 and 3." + Style.RESET_ALL)

    return choice

def get_choice_name(choice):

    if choice == 1:
        return "Rock"

    elif choice == 2:
        return "Paper"

    else:
        return "Scissors"

def ai_choice(player_history):

    if len(player_history) == 0:
        return random.randint(1, 3)

    most_common = max(set(player_history), key=player_history.count)

    if most_common == 1:
        return 2

    elif most_common == 2:
        return 3

    else:
        return 1

def check_winner(player, ai):

    if player == ai:
        return "Tie"

    elif (player == 1 and ai == 3) or \
         (player == 2 and ai == 1) or \
         (player == 3 and ai == 2):
        return "Player"

    else:
        return "AI"

def rock_paper_scissors():

    print(Fore.YELLOW + "Welcome to Rock Paper Scissors Game!" + Style.RESET_ALL)

    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    player_score = 0
    ai_score = 0
    player_history = []

    while True:

        display_choices()

        player = player_choice()

        player_history.append(player)

        ai = ai_choice(player_history)

        print(Fore.BLUE + "\n" + player_name + " chose: " + get_choice_name(player))
        print("AI chose: " + get_choice_name(ai) + Style.RESET_ALL)

        result = check_winner(player, ai)

        if result == "Player":
            print(Fore.GREEN + "\nCongratulations! You won this round!" + Style.RESET_ALL)
            player_score += 1

        elif result == "AI":
            print(Fore.RED + "\nAI won this round!" + Style.RESET_ALL)
            ai_score += 1

        else:
            print(Fore.YELLOW + "\nIt's a tie!" + Style.RESET_ALL)

        print(Fore.CYAN + "\nScoreboard")
        print(player_name + " :", player_score)
        print("AI :", ai_score)
        print(Style.RESET_ALL)

        play_again = input(Fore.MAGENTA + "\nDo you want to play again? (yes/no): " + Style.RESET_ALL).lower()

        if play_again != "yes":
            print(Fore.YELLOW + "\nFinal Scores")
            print(player_name + " :", player_score)
            print("AI :", ai_score)

            if player_score > ai_score:
                print(Fore.GREEN + "\nGreat job! You defeated the AI!" + Style.RESET_ALL)

            elif ai_score > player_score:
                print(Fore.RED + "\nAI wins the game!" + Style.RESET_ALL)

            else:
                print(Fore.YELLOW + "\nThe game ended in a tie!" + Style.RESET_ALL)

            print(Fore.CYAN + "\nThank you for playing!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    rock_paper_scissors()