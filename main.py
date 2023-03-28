import random


def main():
    answer = input("Hello! Do you want to play? YES/NO\n> ")

    if answer.lower() != "yes":
        print("Good bye!")
    else:
        start_game()


def start_game():
    top_of_range = input("Type a number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Please type a number larger than 0!")
            quit()

    else:
        print("Please type a number next time!")
        quit()
    random_number = random.randint(0, top_of_range)
    guesses = 0
    while True:
        guesses += 1
        user_guess = input("Make a guess: ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time!")
            continue

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
    print("You got it in", guesses, "guesses")

if __name__ == '__main__':
    main()
