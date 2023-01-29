import random
import turtle
from words import word_list
wz = turtle.Screen()
wz.bgcolor("white")
bob = turtle.Turtle()
x,y = 0,0
bob.speed(1)

def turtle_map(p):
    if p == 0:
        bob.speed(10)
        bob.hideturtle()
        bob.goto(50,0)
        bob.goto(40,0)
        bob.goto(40,20)
        bob.goto(10,20)
        bob.goto(10,0)
        bob.penup()
        bob.goto(25,20)
        bob.pendown()
        bob.goto(25,100)
        bob.goto(75,100)
        bob.goto(75,90)
    if p == 1:
        #head
        bob.penup()
        bob.goto(75,76)
        bob.pendown()
        bob.circle(7,360)
        bob.speed(1)
    elif p == 2:
        #body
        bob.goto(75,50)
    elif p == 3:
        #left leg
        bob.goto(60,35)
    elif p == 4:
        #right leg
        bob.penup()
        bob.goto(75,50)
        bob.pendown()
        bob.goto(90,35)
    elif p == 5:
        #left arm
        bob.penup()
        bob.goto(75,70)
        bob.pendown()
        bob.goto(60,60)
    elif p == 6:
        #right arm
        bob.penup()
        bob.goto(75,70)
        bob.pendown()
        bob.goto(90,60)
    
def choose_word():
    global word
    word = random.choice(word_list).lower()
    print('_ ' * len(word))

#pick the word before the guesses



def check_letter(letter, num_guessed):
    global num_wrong
    global count
    global sf
    if num_guessed == 1:
        parts = list(enumerate(word))
        for v in parts:
            if letter == v[1]:
                sf.append(letter)
            else:
                sf.append(' _ ')
        sf_word = ''.join(sf)
        print(sf_word)
    elif num_guessed >= 2:
        parts = list(enumerate(word))
        for k,v in parts:
            if letter == v:
                sf[k] = letter
            else:
                continue
        sf_word = ''.join(sf)
        print(sf_word)
                
    if letter not in word:
        print('Incorrect Guess')
        num_wrong += 1
        turtle_map(num_wrong)
        
    if sf_word == word:
        print("You guessed the word!")
        count += 1
        return True

def check_guess(guess):
    global num_wrong
    global count
    global sf
    letter_count = 0
    num_wrong = 0
    count = 1
    gcatalog = list()   #guessed words
    sf = list()   #guess so far in list form


    turtle_map(0) #draw the hangman block

    while True:
        guess = input("Guess a letter or word: ").lower()
        if guess in gcatalog or len(guess) < 1:
            print('You\'ve already guessed that')
            continue
        gcatalog.append(guess)
        print('You have guessed: ', end='')
        for letter in sorted(gcatalog):
            print(f'{letter}, ', end='')
    
        print(f'\nYou have guessed {count} time(s)')


        if len(guess) == 1:     #is letter
            letter_count += 1
            if check_letter(guess,letter_count) == True:
                break
            
        else:
            if guess.lower() == word:
                print("You guessed the word!")
                break
            else:
                print('Sorry, incorrect guess')
                num_wrong += 1
                turtle_map(num_wrong)

        count += 1
        print('\n')

        if num_wrong == 6:
            print(f'Game Over\nThe word was {word}')
            break


            

while True:
    choose_word()
    check_guess(0)
    x = input('Would you like to play again? ')
    ylist = ['yes', 'y']
    if x.lower() in ylist:
        bob.reset()
        continue
    else:
        print("Thanks for Playing!")
        break



