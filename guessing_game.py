random = __import__('random')

secret_num = random.randint(1, 50)
lives = 5

while lives > 0:
    guess = int(input("Enter your guess (1-50): "))

    if guess == secret_num:
        print("You win!")
        break
    elif guess < secret_num:
        print("the secret number is higher than your guess.")
    else:
        print("the secret number is lower than your guess.")

    lives -= 1

if lives == 0:
    print("Game over! You've run out of lives.")
    print(f"The secret number was: {secret_num}")