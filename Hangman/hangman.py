#import knižnicu na kreslenie
import random
import time
import tkinter

#zakladne funkcie pre kreslenie
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

def draw_gallows(x,y):
    #definujem ako by mala vyzerat sibenica
    gallow = x, y, x, y-40, x-100, y-40, x-100, y+160
    canvas.create_line(gallow, width=5)
    canvas.create_line(x-150, y+160, x-50, y+160, width=15)

def draw_hangman(x,y):
    #vykreslenie hangmana
    #state=tkinter.HIDDEN davam koli tomu že ja to cele vykreslim ale postupne to budem odhalovat
    head = canvas.create_oval(x-20, y, x+20, y+40, width=4 , state=tkinter.HIDDEN)
    torso = canvas.create_line(x, y+40, x, y+90, width=4, state=tkinter.HIDDEN)
    left_arm = canvas.create_line(x-40, y+60, x, y+60, width=4, state=tkinter.HIDDEN)
    right_arm = canvas.create_line(x+40, y+60, x, y+60, width=4, state=tkinter.HIDDEN)
    left_leg = canvas.create_line(x, y+90, x-30, y+130, width=4, state=tkinter.HIDDEN)
    right_leg = canvas.create_line(x, y+90, x+30, y+130, width=4, state=tkinter.HIDDEN)
    return head, torso, left_arm, right_arm, left_leg, right_leg

def draw_letters(letters):
    start = 320 - 40*len(letters)/2
    letter_ids = {letter:[] for letter in letters if letter != " "}
    for letter in letters:
        #ked tu bude medzera aby sme dali moznost
        if letter == " ":
            start+=40
            #bez toho continue by nam to spravilo že sa posunie o medzeru ale vykreslilo by prazdnu ciaru
            continue
        canvas.create_line(start+5, 100, start+35, 100, width=2)
        #definicia stredu pismenka
        idx = canvas.create_text(start+20,85, text=letter.upper(),
                            font="arial 25", state=tkinter.HIDDEN)
        letter_ids[letter].append(idx)
        start += 40
    return letter_ids

#čitaine z textu
def load_word(file_name):
    with open(file_name, "r") as fp:
        word_list = fp.read().splitlines()
    random_word = random.choice(word_list)
    return random_word

def show_letter(letter_ids, already_guessed):
    for letter, ids in letter_ids.items():
        if letter in already_guessed:
            for idx in ids:
                canvas.itemconfig(idx, state=tkinter.NORMAL)

def update_hangman(wrong_guesses, hangman_id):
    for i in range(0, wrong_guesses):
        canvas.itemconfig(hangman_id[i], state=tkinter.NORMAL)

def good_guess(letter):
    already_guessed.append(letter)
    show_letter(letter_ids, already_guessed)

def bad_guess(letter):
    global wrong_guesses
    already_guessed.append(letter)
    wrong_guesses += 1
    update_hangman(wrong_guesses, hangman_id)

def is_winner(letter_ids, already_guessed):
    for letter in letter_ids:
        if letter not in already_guessed:
            return False
    return True

def game_over(game_state):
    if game_state == "WIN":
        canvas.create_text(320, 240, text="yvhral si",
                           font="ariel 60", fill="RED")
    else:
        canvas.create_text(320, 240, text="prehral si",
                           font="ariel 60", fill="RED")
    canvas.update()
    time.sleep(3)
def check_game_state():
    global game_state
    if is_winner(letter_ids, already_guessed):
        game_state = "WIN"
    elif wrong_guesses > 5:
        game_state = "LOSS"
draw_gallows(400, 200)
hangman_id = draw_hangman(400, 200)

the_word = load_word("hangman_world.txt")
print(the_word)
letter_ids = draw_letters(the_word)
print(letter_ids)
print(hangman_id)
game_state = "RUNNING"
#toto si možem inicializovat ako prazdne pole
already_guessed = []
wrong_guesses = 0

while game_state == "RUNNING":
    guess = input("guess letter: ")
    if guess in already_guessed:
        continue
    elif guess in letter_ids:
        #dobre pismenko
        good_guess(guess)
    else:
        #zle pismenko
        bad_guess(guess)

    check_game_state()
    #canvas update aktualizuje a nanov vykreli veci ktore treba
    canvas.update()
game_over(game_state)
canvas.mainloop()