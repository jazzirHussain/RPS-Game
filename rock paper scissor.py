from tkinter import *
from random import *

w = Tk()
z = Random()
w.title("Roc Paper Scissor")
w.geometry('500x500')

b = 0
score = 0
score_plyr = 0
score_comp = 0
choices = ['Rock', 'Paper', 'Scissor']


def player_score(n):
    global score_plyr
    score_plyr += n
    output_box.insert(INSERT, 'Player score: %d\n' % score_plyr)


def comp_score(n):
    global score_comp
    score_comp += n
    output_box.insert(INSERT, 'Computer score: %d\n' % score_comp)


def btns(n):
    global b
    global score
    b += 1
    output_box.insert (INSERT, '%d.' %b)
    output_box.insert(INSERT, 'Player chose %s\n' %n)
    choices_random = Random.choice(z,choices)
    output_box.insert (INSERT, '  Computer chose %s \n' % choices_random)
    if choices_random == n:
        player_score(score)
        comp_score(score)
    if (choices_random == 'Rock') & (n == 'Scissor'):
        player_score (score)
        comp_score(score+1)
    elif (choices_random == 'Rock') & (n == 'Paper'):
        player_score(score+1)
        comp_score (score)
    elif (choices_random == 'Paper') & (n == 'Rock'):
        player_score (score)
        comp_score(score+1)
    elif (choices_random == 'Paper') & (n == 'Scissor'):
        player_score(score+1)
        comp_score (score)
    elif (choices_random == 'Scissor') & (n == 'Rock'):
        player_score(score+1)
        comp_score (score)
    elif (choices_random == 'Scissor') & (n == 'Paper'):
        player_score (score)
        comp_score (score + 1)



rock_btn = Button(w, text='Rock', width=20, height=2, bd=4, relief=GROOVE, padx=2, pady=2, command=lambda: btns('Rock'))
paper_btn = Button(w, text='Paper', width=20, height=2, bd=4, relief=GROOVE, padx=2, pady=2, command=lambda: btns('Paper'))
scissor_btn = Button(w, text='Scissor', width=20, height=2, bd=4, relief=GROOVE, padx=2, pady=2, command=lambda: btns('Scissor'))
output_box= Text(w, bd=4, relief=GROOVE, width=61, height=22, bg='light yellow')


rock_btn.grid(row=0, column=0)
paper_btn.grid(row=1, column=0)
scissor_btn.grid(row=2, column=0)
output_box.grid(row=3, column=0)



w.mainloop()