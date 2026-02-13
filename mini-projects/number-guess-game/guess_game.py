import random

random_number = random.randint(1, 100)
remaining_attempts = 4
score = 100
attempt_count = 0

print("1 ile 100 arasında bir sayı tahmin et")
print(f"Şu anki skorun: {score}")

while remaining_attempts > 0:
    try:
        guess = int(input("Tahmininiz: "))
    except ValueError:
        print("Lütfen sadece sayı giriniz")
        continue

    if guess < 1 or guess > 100:
        print("Lütfen 1 ile 100 arasında bir sayı giriniz")
        continue

    attempt_count += 1

    if guess == random_number:
        print(f"Tebrikler! Tutulan sayıyı {attempt_count}. denemenizde bildiniz")
        print(f"Skorunuz: {score}")
        break

    remaining_attempts -= 1
    score -= 25

    if remaining_attempts == 0:
        print("Hakkınız kalmamıştır")
        print(f"Doğru sayı: {random_number}")
        print(f"Skorunuz: {score}")
        break

    if guess < random_number:
        print("Lütfen daha büyük bir sayı giriniz")
    else:
        print("Lütfen daha küçük bir sayı giriniz")

    print(f"Kalan deneme sayınız: {remaining_attempts}")
    print(f"Kalan puanınız: {score}")
