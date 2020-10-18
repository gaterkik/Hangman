import random
WORDS = ['python', 'java', 'kotlin', 'javascript']
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
LIVES = 8
user_action = 'play'


def redraw_prompt(letter, string):
    prompt_list = list(prompt)
    for i in range(len(string)):
        if string[i] == letter:
            prompt_list[i] = letter
    return ''.join(prompt_list)


while user_action == 'play':
    user_action = input('Type "play" to play the game, "exit" to quit:')
    if user_action != 'play':
        break
    word = random.choice(WORDS)
    prompt = '-' * len(word)
    print('H A N G M A N')
    tries_set = set()
    while LIVES > 0:
        print('')
        print(prompt)
        if '-' not in prompt:
            break
        user_letter = input('Input a letter:')
        if len(user_letter) != 1:
            print("You should input a single letter")
            continue
        if user_letter in tries_set:
            print("You already typed this letter")
            continue
        if user_letter not in ALPHABET:
            print('It is not an ASCII lowercase letter" message, but should be')
            continue

        if user_letter in word:
            prompt = redraw_prompt(user_letter, word)
        else:
            print("No such letter in the word")
            LIVES -= 1
        if user_letter in tries_set and user_letter in word:
            print("No improvements")
            LIVES -= 1
        tries_set.add(user_letter)
    else:
        print("You lost!")
    if '-' not in prompt:
        print("You guessed the word!")
        print("You survived!")

