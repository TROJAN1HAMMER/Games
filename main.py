import winsound

winsound.PlaySound("whip-110235.wav", winsound.SND_ASYNC)


print("Hi!!")
print("Select the game you want to play: ")
print("------------------------------------")
print("1 - Random number guesser")
print("2 - Rock, Paper and Scissors")
print("3 - Adventure")
print("4 - Tic-Tac-Toe")
print("5 - quit")
print("------------------------------------")
game_choice = int(input("Enter the no. for the game you want to play: "))

if game_choice == 1:
    import random

    secret_number = random.randint(1, 25)


    def main():
        a = int(input("Guess a number between 1 and 25: "))
        count = 0
        while count < 10:
            if a != secret_number:
                print("You lose!")
                count += 1
                main()

            else:
                print("you win")


    main()

elif game_choice == 2:
    # rock, paper, scissors
    import random

    choices = ["rock", "paper", "scissors"]

    computer_input = random.choice(choices)

    count = 0
    no_of_rounds = 5
    user_score = 0
    computer_score = 0
    chances = 5

    while count < no_of_rounds:
        user_input = input("rock, paper or scissors: ")
        print("-------------------------")
        if user_input in choices:
            count += 1
            chances = 5 - count
            if computer_input == "rock":
                if user_input == "rock":
                    print("Draw!!")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                elif user_input == "paper":
                    print("You get a point!!")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                    user_score += 1
                elif user_input == "scissors":
                    print("No points")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                    computer_score += 1

            elif computer_input == "paper":
                if user_input == "paper":
                    print("Draw!!")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                elif user_input == "scissors":
                    print("You get a point!!")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                    user_score += 1
                elif user_input == "rock":
                    print("No points")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                    computer_score += 1

            elif computer_input == "scissors":
                if user_input == "scissors":
                    print("Draw!!")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                elif user_input == "rock":
                    print("You get a point!!")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                    user_score += 1
                elif user_input == "paper":
                    print("No points")
                    print("Number of chances left: ", chances)
                    print("-------------------------")
                    computer_score += 1

        elif user_input not in choices:
            print("Typo!")
            print("-------------------------")
            count += 0

        elif user_input == "quit":
            quit()

    else:
        print("Your score is:", user_score)
        print("-------------------------")
        if user_score > computer_score:
            print("You win!")
        elif user_score == computer_score:
            print("Draw!!")
        elif user_score < computer_score:
            print("You lose, Try again!!")

    print("-------------------------")
    print("Game over!!", "Thank you for playing!")

elif game_choice == 3:
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure!")

    answer = input("You are on a dirt road, "
                   "it has come to an end and you can go left or right. Which way would you like to go? ").lower()

    if answer == "left":
        answer = input("You come to a river, "
                       "you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

        if answer == "swim":
            print("You swam acrross and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
        else:
            print('Not a valid option. You lose.')

    elif answer == "right":
        answer = input(
            "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            answer = input(
                "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

            if answer == "yes":
                print("You talk to the stanger and they give you gold. You WIN!")
            elif answer == "no":
                print("You ignore the stranger and they are offended and you lose.")
            else:
                print('Not a valid option. You lose.')
        else:
            print('Not a valid option. You lose.')

    else:
        print('Not a valid option. You lose.')

    print("Thank you for trying", name)

elif game_choice == 4:
    def sum(a, b, c):
        return a + b + c


    def printBoard(xState, zState):
        zero = 'X' if xState[0] else ('O' if zState[0] else 0)
        one = 'X' if xState[1] else ('O' if zState[1] else 1)
        two = 'X' if xState[2] else ('O' if zState[2] else 2)
        three = 'X' if xState[3] else ('O' if zState[3] else 3)
        four = 'X' if xState[4] else ('O' if zState[4] else 4)
        five = 'X' if xState[5] else ('O' if zState[5] else 5)
        six = 'X' if xState[6] else ('O' if zState[6] else 6)
        seven = 'X' if xState[7] else ('O' if zState[7] else 7)
        eight = 'X' if xState[8] else ('O' if zState[8] else 8)
        print(f"{zero} | {one} | {two} ")
        print(f"--|---|---")
        print(f"{three} | {four} | {five} ")
        print(f"--|---|---")
        print(f"{six} | {seven} | {eight} ")


    def checkWin(xState, zState):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
                print("X Won the match")
                return 1
            if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
                print("O Won the match")
                return 0
        return -1


    if __name__ == "__main__":
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1  # 1 for X and 0 for O
        print("Welcome to Tic Tac Toe")
        while True:
            printBoard(xState, zState)
            if turn == 1:
                print("X's Chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
            else:
                print("O's Chance")
                value = int(input("Please enter a value: "))
                zState[value] = 1
            cwin = checkWin(xState, zState)
            if cwin != -1:
                print("Match over")
                break

            turn -= 1


elif game_choice == 5:
    quit()
