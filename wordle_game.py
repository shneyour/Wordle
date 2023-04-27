import tkinter as tk
from tkinter import messagebox
import random

daily_word_data = 'About, Above, Abuse, Actor, Acute, Admit, Adopt, Adult, After, Again, Agent, Agree, Ahead, Alarm, Album, Boost, Booth, Bound, Brain, Brand, Bread, Break, Breed, Brief, Bring, Broad, Broke, Brown, Build, Built, Debut, Delay, Depth, Doing, Doubt, Dozen, Draft, Drama, Drawn, Dream, Dress, Drill, Drink, Drive, Drove, Dying, Eager, Early, Earth, Eight, Elite, Empty, Enemy, Enjoy, Enter, Judge, Known, Label, Large, Laser, Later, Laugh, Layer, Learn, Lease, Least, Leave, Legal, Level, Light, Limit, Peace, Panel, Phase, Phone, Photo, Piece, Pilot, Pitch, Place, Plain, Plane, Plant, Plate, Point, Pound, Sheet, Shelf, Shell, Shift, Shirt, Shock, Shoot, Short, Shown, Sight, Since, Sixty, Sized, Skill, Sleep, Slide, Small, Smart, Smile, Smith, Smoke, Solid, Solve, Sorry, Sound, South, Space, Upset, Urban, Usage, Usual, Valid, Value, Video, Virus, Visit, Cheap, Check, Chest, Chief, Child, Entry, Equal, Error, Event, Every, Exact, Exist, Extra, Faith, FALSE, Fault, Fiber, Field, Fifth, Fifty, Fight, Final, First, Fixed, Flash, Fleet, Floor, Fluid, Focus, Force, Metal, Local, Logic, Loose, Lower, Lucky, Lunch, Lying, Magic, Major, Maker, March, Music, Match, Mayor, Meant, Power, Press, Price, Pride, Prime, Print, Prior, Prize, Proof, Proud, Prove, Queen, Sixth, Quiet, Quite, Spare, Speak, Speed, Spend, Spent, Split, Spoke, Sport, Staff, Stage, Stake, Start, State, Steam, Steel, Stick, Still, Stock, Stone, Stood, Store, Storm, Story, Strip, Stuck, Study, Stuff, Whole, Whose, Woman, Train, World, Worry, Worse, Worst, Would, Coach, Coast, Could, Count, Court, Forth, Forty, Forum, Found, Frame, Frank, Fraud, Fresh, Front, Fruit, Fully, Funny, Giant, Given, Glass, Globe, Going, Grace, Grade, Grand, Grant, Grass, Great, Green, Gross, Media, Might, Minor, Minus, Mixed, Model, Money, Month, Moral, Motor, Mount, Mouse, Mouth, Movie, Needs, Never, Radio, Raise, Range, Rapid, Ratio, Reach, Ready, Refer, Right, Rival, River, Quick, Stand, Roman, Rough, Style, Sugar, Suite, Super, Sweet, Table, Taken, Taste, Taxes, Teach, Teeth, Texas, Thank, Theft, Their, Theme, There, These, Thick, Thing, Think, Third, Those, Three, Threw, Throw, Tight, Waste, Watch, Water, Wheel, Where, Which, While, White, Vital, Beach, Began, Begin, Begun, Being, Below, Bench, Billy, Birth, Black, Blame, Blind, Block, Blood, Board, Cover, Craft, Crash, Cream, Crime, Cross, Crowd, Crown, Curve, Cycle, Daily, Dance, Dated, Dealt, Death, Group, Grown, Guard, Guess, Guest, Guide, Happy, Harry, Heart, Heavy, Hence, Night, Horse, Hotel, House, Human'
daily_word_list = daily_word_data.split(sep=', ')
daily_word = random.choice(daily_word_list)
daily_word = daily_word.upper()
try_number = 0

def reset():
    [widget.delete(0, tk.END) for widget in root.winfo_children() if isinstance(widget, tk.Entry)]


def new_game():
    global daily_word, try_number
    try_number = 0
    [widget.destroy() for widget in root.winfo_children() if isinstance(widget, tk.Label)]
    tk.Label(root, text="First Try").place(x=5, y=5)
    tk.Label(root, text="Second Try").place(x=5, y=30)
    tk.Label(root, text="Third Try").place(x=5, y=55)
    tk.Label(root, text="Fourth Try").place(x=5, y=80)
    tk.Label(root, text="Fifth Try").place(x=5, y=105)
    tk.Label(root, text="Sixth Try").place(x=5, y=130)
    tk.Label(root, text="Your Guess:").place(x=5, y=170)
    daily_word = random.choice(daily_word_list)
    daily_word = daily_word.upper()


def word_check():
    global try_number, ariel, pop
    check_list = []
    user_try = guess_entry.get()
    user_try = user_try.upper()
    user_try_list = list(user_try)
    if len(user_try) != 5:
        messagebox.showinfo(title="Ariel's Wordle", message='Please enter a 5 letter word in English')

    else:
        for i in range(0, 5):
            if user_try_list[i] in daily_word:
                if user_try_list[i] == daily_word[i]:
                    tk.Label(root, text=user_try_list[i], bg='green', width=1).place(x=(i * 20)+90, y=(try_number + 0.11) * 25)
                    check_list.append(user_try_list[i])

                elif (2 <= len(set(user_try_list)) <= 4) and (user_try_list.count(user_try_list[i]) > daily_word.count(user_try_list[i])):
                    if user_try_list[i] not in check_list and i > user_try_list.index(user_try_list[i]):
                        tk.Label(root, text=user_try_list[i], bg='yellow', width=1).place(x=(i * 20) + 90, y=(try_number + 0.11) * 25)
                        check_list.append(user_try_list[i])
                    else:
                        tk.Label(root, text=user_try_list[i], bg='grey', width=1).place(x=(i * 20) + 90, y=(try_number + 0.11) * 25)
                else:
                    tk.Label(root, text=user_try_list[i], bg='yellow', width=1).place(x=(i * 20)+90, y=(try_number + 0.11) * 25)
                    check_list.append(user_try_list[i])

            else:
                tk.Label(root, text=user_try_list[i], bg='grey', width=1).place(x=(i * 20)+90, y=(try_number + 0.11) * 25)
                check_list.append(user_try_list[i])

        try_number += 1

        if list(user_try) == list(daily_word):
            # messagebox.showinfo(title="Ariel's Wordle", message=f'Good job! Your guess {user_try} is correct')
            ariel = tk.PhotoImage(file='/Users/arielshneyour/Desktop/פרויקט/IMG_9009.png')
            pop = tk.Toplevel(root)
            pop.title("Ariel's Wordle")
            pop.geometry('250x250')
            pop_label = tk.Label(pop, text=f'Good job! Your guess {user_try} is correct')
            pop_label.pack(pady=10)
            my_frame = tk.Frame(pop)
            my_frame.pack(pady=5)
            me_pic = tk.Label(my_frame, image=ariel)
            me_pic.grid(row=0, column=0, padx=10)

        if try_number == 6 and list(user_try) != list(daily_word):
            messagebox.showinfo(title="Ariel's Wordle", message=f'You lose, the word was {daily_word}')


root = tk.Tk()
root.title("Ariel's Wordle")
root.geometry('273x230')

tk.Label(root, text="First Try").place(x=5, y=5)

tk.Label(root, text="Second Try").place(x=5, y=30)

tk.Label(root, text="Third Try").place(x=5, y=55)

tk.Label(root, text="Fourth Try").place(x=5, y=80)

tk.Label(root, text="Fifth Try").place(x=5, y=105)

tk.Label(root, text="Sixth Try").place(x=5, y=130)

tk.Label(root, text="Your Guess:").place(x=5, y=170)

guess_entry = tk.Entry(root)
guess_entry.place(x=100, y=170, width=80)

btn_submit = tk.Button(root, text='Submit', bd='5', command=lambda: [word_check(), reset()])
btn_submit.place(x=180, y=165)

btn_game = tk.Button(root, text='New Game', bd='5', command=new_game)
btn_game.place(x=167, y=197)

tk.mainloop()