import random

secret_number = random.randint(1, 100)
remaining_attempts = 4
score = 100
attempt_count = 0

print("Guess a number between 1 and 100")
print(f"Starting score: {score}")

while remaining_attempts > 0:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100")
        continue

    attempt_count += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed it on the {attempt_count}th try")
        print(f"Your score: {score}")
        break

    remaining_attempts -= 1
    score -= 25

    if remaining_attempts == 0:
        print("No attempts left")
        print(f"The correct number was: {secret_number}")
        print(f"Your score: {score}")
        break

    if guess < secret_number:
        print("Enter a higher number")
    else:
        print("Enter a lower number")

    print(f"Remaining attempts: {remaining_attempts}")
    print(f"Remaining score: {score}")
