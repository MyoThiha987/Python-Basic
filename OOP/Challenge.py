# Challenge
import random
import sys

name = ''
name = input("Enter your name!\t")
print(f"\n{name}, guess which number i am thinking of 1, 2 or 3.\n")


def guess_number():
    game_count = 0
    player_win = 0
    player_win_rate = 0
    again = False

    global name

    def play_game():
        nonlocal again
        if again:
            print(f"\nWelcome Back, {name}")

        my_number = input("\nEnter a number for guess game!\t")
        # print(f"\n{my_number}\n")

        if my_number not in ["1", "2", "3"]:
            print("You must enter 1, 2 or 3.")
            return play_game()

        print(f"\n{name}, you chose {my_number}\n")

        computer_number = random.choice("123")
        player_choice = int(my_number)
        computer_choice = int(computer_number)
        print(f"I was thinking about the number {computer_number}")

        def decide_winner(player_choice, computer_choice):
            nonlocal player_win

            if player_choice == computer_choice:
                player_win += 1
                return f"\n{name}, You Win!🎉"
            else:
                return f"\nSorry, {name}!. Better luck next time.😢"

        game_result = decide_winner(player_choice, computer_choice)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {game_count}")



        nonlocal player_win_rate
        player_win_rate = (player_win / game_count) * 100

        print(f"\nYour winning percentage : {player_win_rate} %")

        print("\nPlay again?\n")

        while True:
            play_again = input("Y for Yes or\n\nQ  for Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
            again = True
            return play_game()
        else:
            again = False
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋🏻")
            else:
                return

    return play_game


play_game = guess_number()
play_game()
