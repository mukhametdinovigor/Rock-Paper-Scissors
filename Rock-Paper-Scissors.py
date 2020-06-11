import random

combinations = dict()
user_name = input('Enter your name: ')
print(f'Hello, {user_name}')

user_options = input().split(',')
if len(user_options) == 1:
    combinations = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}
else:
    ln = int((len(user_options) - 1) / 2)
    tmp_user_options = user_options + user_options[:ln]
    for ind, it in enumerate(user_options):
        tmp = []
        for i in range(1, ln + 1):
            tmp.append(tmp_user_options[ind + i])
        combinations[it] = tmp

user_input = input("Okay, let's start \n")
rating_file = open('rating.txt', 'r', encoding='utf-8')
user_rating = 0
for line in rating_file:
    if line.split()[0] == user_name:
        user_rating = int(line.split()[1])

while user_input != '!exit':
    if user_input == '!rating':
        print(f'Your rating: {user_rating}')
    elif user_input not in list(combinations.keys()):
        print('Invalid input')
    else:
        computer_input = random.choice(list(combinations.keys()))
        if computer_input == user_input:
            user_rating += 50
            print(f'There is a draw ({user_input})')
        elif user_input in combinations[computer_input]:
            user_rating += 100
            print(f'Well done. Computer chose {computer_input} and failed')
        elif computer_input in combinations[user_input]:
            print(f'Sorry, but computer chose {computer_input}')
    user_input = input()
rating_file.close()
print('Bye!')
