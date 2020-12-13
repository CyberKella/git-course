import random

guessTaken = 0

print('Привет! Как тебя зовут?')
name = input()

number = random.randint(1, 20)
print('Что ж, ' + name + ', я загадываю число от 1 до 20')

for guessTaken in range(6):
    print('Попробуй угадать.')
    guess = input()
    guess = int(guess)


    if guess < number:
        print('Твое число слишком маленькое')
    elif guess > number:
        print('Твое число слшком большое')
    elif guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print('Отлично, ' + name + ', ты справился за ' + guessTaken + ' попыток!')
elif guess != number:
    number = str(number)
    print('Увы! ' + 'Я загадала число ' + number + '.' )