# We used the time, tkinter, and pillow module for the project! Here's the code to load the imports:
import time
import tkinter as tk
import PIL
from tkinter import *
from PIL import ImageTk, Image

# These are our global variables. Start holds the key to keeping the game running and Rock checks if the player has Uranium-235.
start = False
rock = "no_choice_yet"


### DISPLAY SECTION ###

# Takes text and an output name in string form and returns text with fancy lettering printed out in the window.
# Referenced from this website: https://jams.hackclub.com/jam/story-game
def typewriter(text, text_widget):
   for letter in text:
       text_widget.config(state=tk.NORMAL)
       if letter == "\n":
           text_widget.insert(tk.END, "\n")
       else:
           text_widget.insert(tk.END, letter)
           text_widget.see(tk.END)
       text_widget.config(state=tk.DISABLED)
       text_widget.update()
       time.sleep(0.035)

# Code to generate the main window!
window = tk.Tk()
window.title("TRY NOT TO DIE: The Life of Hank")
window.geometry("600x400")
window.resizable(False, False)

# Code for all our frames, which represent the new scenes into the adventure game.
death_frame = tk.Frame(window)
welcome_frame = tk.Frame(window)
plot_frame = tk.Frame(window)
rock_frame = tk.Frame(window)
radioactive_frame = tk.Frame(window)
job_frame = tk.Frame(window)
rizz_frame = tk.Frame(window)
gift_frame = tk.Frame(window)
marry_frame = tk.Frame(window)
final_frame = tk.Frame(window)
win_frame = tk.Frame(window)

# Code for where the typewriter will print the text!
output_text = tk.Text(window, height=10, width=50, wrap=tk.WORD)
output_text.config(state=tk.DISABLED)
output_text.pack()

# When prompted, begins the game by moving to the first frame of the game. This is activated by the start button.
# Made by Ting Ting!
def begin():
     global start
     welcome_frame.pack_forget()
     plot_frame.pack()
     job_text()
     start = True

# When prompted, stops the code and game. This is activated by the exit button.
# Made by Ting Ting!
def end():
    quit()

# When prompted, moves the player from the game over or win screen back to the start. This is activated by the replay button.
# Made by Ting Ting!
def replay(yes):
     if yes == "yes": 
         death_frame.pack_forget()
         welcome_frame.pack()
     elif yes == "yeah":
         win_frame.pack_forget()
         welcome_frame.pack()

# Code to import all our images! We did this by opening and resizing them to the appropriate aspect ratio.
derp = Image.open('project/derp.png')
derp = derp.resize((100,100))
derp = ImageTk.PhotoImage(derp)

babyhank =Image.open('project/hank.png')
babyhank = babyhank.resize((100,100))
babyhank=ImageTk.PhotoImage(babyhank)

hank =Image.open('project/adult.png')
hank = hank.resize((100,100))
hank =ImageTk.PhotoImage(hank)

hank_job = Image.open('project/spelunker.png')
hank_job = hank_job.resize((100,100))
hank_job = ImageTk.PhotoImage(hank_job)

hank235 = Image.open('project/has_uranium.png')
hank235 = hank235.resize((100,100))
hank235 = ImageTk.PhotoImage(hank235)

hankradioheart = Image.open('project/has_uranium_love.png')
hankradioheart = hankradioheart.resize((100,100))
hankradioheart = ImageTk.PhotoImage(hankradioheart)

hanklove = Image.open('project/love.png')
hanklove = hanklove.resize((100,100))
hanklove = ImageTk.PhotoImage(hanklove)

dedge = Image.open('project/dead.png')
dedge = dedge.resize((100,100))
dedge = ImageTk.PhotoImage(dedge)

win = Image.open('project/win.png')
win = win.resize((100,100))
win = ImageTk.PhotoImage(win)


## CODE FOR WELCOME DISPLAY:
# Sets up all the display for the start screen.
welcome_label = tk.Label(welcome_frame, text="Press play to start!", image=derp)
welcome_label.pack()
start_button = tk.Button(welcome_frame, text="Play", command=begin, bg="gray")
start_button.pack()
end_button = tk.Button(welcome_frame, text = "Exit", command=end, bg="gray")
end_button.pack()
typewriter("WELCOME TO HANK'S LIFE! HAVE FUN!!!", output_text)
typewriter("\n\nMade By: Kanchanok Zhang and Sofia Lawrence", output_text)


## CODE FOR DEATH DISPLAY:
# Sets up all the display for the end screen. Connects to replay as well!
death_label = tk.Label(death_frame, text = "Want to replay?", image = dedge)
death_label.pack()
restart_button = tk.Button(death_frame, text="Replay", command=lambda: replay("yes"), bg="gray")
restart_button.pack()
end2_button = tk.Button(death_frame, text = "Exit", command=end, bg="gray")
end2_button.pack()

## CODE FOR CHOOSING JOB DISPLAY:
# Frame:
plot_label = tk.Label(plot_frame, text="Choose a job!", image=babyhank)
plot_label.pack()
# Buttons:
geologist_button = tk.Button(plot_frame, text="Geologist", command=lambda: choose_job("geologist"), bg="gray")
geologist_button.pack()
jeweler_button = tk.Button(plot_frame, text="Jeweler", command=lambda: choose_job("jeweler"), bg="gray")
jeweler_button.pack()

## CODE FOR MISSION ACCEPTANCE DISPLAY:
# Frame:
job_label = tk.Label(job_frame, text="Will you go on the mission?", image=hank_job)
job_label.pack()
# Buttons:
yes_button = tk.Button(job_frame, text="Yes", command=lambda: job_accept("yes"), bg="gray")
yes_button.pack()
no_button = tk.Button(job_frame, text="No", command=lambda: job_accept("no"), bg="gray")
no_button.pack()

## CODE FOR CHOOSING ROCKS DISPLAY:
# Frame:
rock_label = tk.Label(rock_frame, text="Choose a rock!", image=hank_job)
rock_label.pack()
# Buttons:
marble_button = tk.Button(rock_frame, text="Marbly White", command=lambda: choose_rock("marble"), bg="gray")
marble_button.pack()
uranium_button = tk.Button(rock_frame, text="Suspicious", command=lambda: choose_rock("uranium"), bg="gray")
uranium_button.pack()

## CODE FOR URANIUM TASTE TEST DISPLAY:
# Frame:
radioactive_label = tk.Label(radioactive_frame, text="Do you keep it or do a little taste test?", image=hank_job)
radioactive_label.pack()
# Buttons:
keep_button = tk.Button(radioactive_frame, text="Keep", command=lambda: slurp("keep"), bg="gray")
keep_button.pack()
drink_button = tk.Button(radioactive_frame, text="Drink", command=lambda: slurp("drink"), bg="gray")
drink_button.pack()

## CODE FOR FLIRTING SCENE DISPLAY:
# Frame:
rizz_label = tk.Label(rizz_frame, text="Do you flirt with her?", image=hanklove)
rizz_label.pack()
# Buttons:
rizzler_button = tk.Button(rizz_frame, text="Yes", command=lambda: flirt("yes"), bg="gray")
rizzler_button.pack()
unrizzler_button = tk.Button(rizz_frame, text="No", command=lambda: flirt("no"), bg="gray")
unrizzler_button.pack()

## CODE FOR GIFT DISPLAY:
# Frame:
gift_label = tk.Label(gift_frame, text="Do you buy her a gourmet selection of krill or her favorite ice perfume?", image=hanklove)
gift_label.pack()
# Buttons:
shrimp_button = tk.Button(gift_frame, text="Krill", command=lambda: gift("shrimp"), bg="gray")
shrimp_button.pack()
perfume_button = tk.Button(gift_frame, text="Perfume", command=lambda: gift("perfume"), bg="gray")
perfume_button.pack()

## CODE FOR PROPOSAL DISPLAY:
# Frame:
marry_label = tk.Label(marry_frame, text = "Will you go through with it?", image=hanklove)
marry_label.pack()
# Buttons:
accept_button = tk.Button(marry_frame, text="Yes", command=lambda: proposal("yes"), bg="gray")
accept_button.pack()
reject_button = tk.Button(marry_frame, text="No", command=lambda: proposal("no"), bg="gray")
reject_button.pack()

## CODE FOR FINAL SCENE DISPLAY:
# Frame:
final_label = tk.Label(final_frame, text="How do you get out of this situation?", image=hank)
final_label.pack()
# Buttons:
defend_button = tk.Button(final_frame, text="Fight Back", command=lambda: final("fight_back"), bg ="gray")
defend_button.pack()
flee_button = tk.Button(final_frame, text="Flee", command=lambda: final("run"), bg ="gray")
flee_button.pack()

## CODE FOR WIN DISPLAY:
win_label = tk.Label(win_frame, text="You have reached the end!", image=win)
win_label.pack()
win_again_button = tk.Button(win_frame, text="Continue", command=lambda: replay("yeah"), bg="gray")
win_again_button.pack()

### LOGIC SECTION ###

# When prompted by the start of the game, prints the first text and keeps the button disabled until the text finishes.
# Made by Ting Ting
def job_text():
     geologist_button.config(state=tk.DISABLED)
     jeweler_button.config(state=tk.DISABLED)
     typewriter("\n\n\n\n\n\n\n\n\n\n\n\n\nHank is hatched. It's a boy! \nYou are Hank by the way.", output_text)
     typewriter("\nHank grows up to the age of 10 (late bloomer) and must decide his future career.", output_text)
     typewriter("\nGeologist or Jeweler?", output_text)
     geologist_button.config(state=tk.NORMAL)
     jeweler_button.config(state=tk.NORMAL)

## FOR ALL THE FUNCTIONS BELOW: They all accept string responses and return text responses based on the specific event. 
# Buttons are disabled once pressed and are reset after the event changes. These functions progress the game and are prompted by 
# buttons from the display section.
# Made by Ting Ting and Sofia (Did both the logic and reformatting together)
def choose_job(job):
     if job == "geologist":
         geologist_button.config(state=tk.DISABLED)
         jeweler_button.config(state=tk.DISABLED)
         plot_frame.pack_forget() 
         job_frame.pack()
         geologist_button.config(state=tk.NORMAL)
         jeweler_button.config(state=tk.NORMAL)
         typewriter("\nYour big boss Boris alpha carbon shows you his collection of rocks.", output_text)
     elif job == "jeweler":
         geologist_button.config(state=tk.DISABLED)
         jeweler_button.config(state=tk.DISABLED)
         plot_frame.pack_forget() 
         job_frame.pack()
         geologist_button.config(state=tk.NORMAL)
         jeweler_button.config(state=tk.NORMAL)
         typewriter("\nYour big boss Boris alpha carbon shows you his collection of jewels.", output_text)

def job_accept(response):
     if response == "yes":
         yes_button.config(state=tk.DISABLED)
         no_button.config(state=tk.DISABLED)
         typewriter("\nHe then sends you to get more stones.", output_text)
         typewriter("\nYou must decide between the marbley white one or the suspicious one that is scattered over the water.", output_text)
         job_frame.pack_forget() 
         yes_button.config(state=tk.NORMAL)
         no_button.config(state=tk.NORMAL)
         rock_frame.pack()
     elif response == "no":
         yes_button.config(state=tk.DISABLED)
         no_button.config(state=tk.DISABLED)
         typewriter("\n\n\n\n\n\n\n\n\n\n\nYou get fired, go bankrupt, and spontaneously combust out of grief.", output_text)
         job_frame.pack_forget() 
         yes_button.config(state=tk.NORMAL)
         no_button.config(state=tk.NORMAL)
         death_frame.pack()


def choose_rock(gem):
     if gem == "marble":
         marble_button.config(state=tk.DISABLED)
         uranium_button.config(state=tk.DISABLED)
         typewriter("\nYou return to Boris and he is pleased.", output_text)
         rock_frame.pack_forget()
         marble_button.config(state=tk.NORMAL)
         uranium_button.config(state=tk.NORMAL)
         rizz_frame.pack()
         typewriter("\nYou walk home that day, and bump into a pretty, female penguin, Hilda.",output_text)
         typewriter("\nWill you flirt with her?", output_text)
     elif gem == "uranium":
         marble_button.config(state=tk.DISABLED)
         uranium_button.config(state=tk.DISABLED)
         typewriter("\nYou encounter a neon green ore in a buzzing puddle of something.", output_text)
         typewriter("\nDo you keep it or drink it?", output_text)
         rock_frame.pack_forget()
         marble_button.config(state=tk.NORMAL)
         uranium_button.config(state=tk.NORMAL)
         radioactive_frame.pack()

def slurp(choice):
     global rock
     if choice == "keep":
         keep_button.config(state=tk.DISABLED)
         drink_button.config(state=tk.DISABLED)
         typewriter("\nYou keep the suspicious green rock in your bag. Hopefully this can be useful later?", output_text)
         rock = "yes"
         radioactive_frame.pack_forget()
         keep_button.config(state=tk.NORMAL)
         drink_button.config(state=tk.NORMAL)
         rizz_frame.pack()
         typewriter("\nYou return to Boris empty handed. You are lucky that he is in a good mood and not upset.", output_text)
         typewriter("\nYou walk home that day, and bump into a pretty, female penguin, Hilda.",output_text)
         typewriter("\nWill you flirt with her?", output_text)
     elif choice == "drink":
         keep_button.config(state=tk.DISABLED)
         drink_button.config(state=tk.DISABLED)
         typewriter("\n\n\n\n\n\n\n\n\n\n\nYou die from stupidity and poison.",output_text)
         radioactive_frame.pack_forget()
         keep_button.config(state=tk.NORMAL)
         drink_button.config(state=tk.NORMAL)
         death_frame.pack()

def flirt(choice):
     if choice == "yes":
         rizzler_button.config(state=tk.DISABLED)
         unrizzler_button.config(state=tk.DISABLED)
         typewriter("\nYou say “Do you believe in love at first sight or should I waddle by again?” Hilda blushes.",output_text)
         rizz_frame.pack_forget()
         rizzler_button.config(state=tk.NORMAL)
         unrizzler_button.config(state=tk.NORMAL)
         gift_frame.pack()
         typewriter("\nYou are entranced by Hilda and enter a relationship with her.",output_text)
     elif choice == "no":
         rizzler_button.config(state=tk.DISABLED)
         unrizzler_button.config(state=tk.DISABLED)
         typewriter("\nYou and Hilda exchange smiles and she gives you a wink.",output_text)
         time.sleep(0.1)
         typewriter("\nHilda looks at you and says “Are you an iceberg? Cuz you just melted my heart”. You blush.", output_text)
         rizz_frame.pack_forget()
         rizzler_button.config(state=tk.NORMAL)
         unrizzler_button.config(state=tk.NORMAL)
         gift_frame.pack()
         typewriter("\nYou are entranced by Hilda and enter a relationship with her.", output_text)
         typewriter("Do you buy her a gourmet selection of krill or her favorite ice perfume?",output_text)

def gift(choice):
     if choice == "shrimp":
         shrimp_button.config(state=tk.DISABLED)
         perfume_button.config(state=tk.DISABLED)
         typewriter("\nShe loves your gourmet selection!",output_text)
         gift_frame.pack_forget()
         shrimp_button.config(state=tk.NORMAL)
         perfume_button.config(state=tk.NORMAL)
         marry_frame.pack()
         typewriter("\nYou spend three years with your new beloved. Over time, the two of you grow very close.",output_text)
         typewriter("\nA few months later, you propose to Hilda with a stone you stole from your job.",output_text)
         typewriter("\nWill you follow through?", output_text)
     elif choice == "perfume":
         shrimp_button.config(state=tk.DISABLED)
         perfume_button.config(state=tk.DISABLED)
         typewriter("\nShe is offended by your offering of ice perfume and smacks you on the spot for thinking she smells.",output_text)
         typewriter("\n\n\n\n\n\n\n\n\n\n\nYou end up as the fastest flying object to leave the Earth's orbit and succumb to the vacuum of space.",output_text)
         gift_frame.pack_forget()
         shrimp_button.config(state=tk.NORMAL)
         perfume_button.config(state=tk.NORMAL)
         death_frame.pack()

# When prompted, prints extra dialogue for the final scene.
# Made by Sofia
def final_dialogue():
    typewriter("\nHilda grows to hate you for giving her a son and not a daughter. She plans on how to kill you.", output_text)
    time.sleep(0.1)
    typewriter("\nShe buys a glock from the store and hides in under her pillow.", output_text)
    time.sleep(0.1)
    typewriter("\nThe glock falls off the pillow one night when you two go to sleep.", output_text)
    time.sleep(0.1)
    typewriter("\nThis is the final moment. Hilda grabs her glock and stuffs it with bullets.", output_text)
    time.sleep(0.1)
    typewriter("\nShe's trying to get back at you for giving her a son and not a daughter.", output_text)
    time.sleep(0.1)
    typewriter("\nDo you defend yourself or try to escape?", output_text)

def proposal(choice):
    if choice == "yes":
         accept_button.config(state=tk.DISABLED)
         reject_button.config(state=tk.DISABLED)
         typewriter("\nYou and Hilda become happily married and Hilda gives birth to a son, Hankiton Jimmy John Joe II Jr. middle name hilda.",output_text)
         marry_frame.pack_forget()
         accept_button.config(state=tk.NORMAL)
         reject_button.config(state=tk.NORMAL)
         final_frame.pack()
         final_dialogue()
    elif choice == "no":
         accept_button.config(state=tk.DISABLED)
         reject_button.config(state=tk.DISABLED)
         typewriter("\n\n\n\n\n\n\n\n\n\n\nHOW DARE YOU BACK OUT! Hilda kills you with a wooden spoon for your cowardice.",output_text)
         marry_frame.pack_forget()
         accept_button.config(state=tk.NORMAL)
         reject_button.config(state=tk.NORMAL)
         death_frame.pack()

def final(choice):
     global rock
     if choice == "fight_back":
         if rock == "yes":
             defend_button.config(state=tk.DISABLED)
             flee_button.config(state=tk.DISABLED)
             typewriter("\nIn the heat of the moment, you throw the radioactive substance at Hilda.", output_text)
             typewriter("\nThe force of throwing the Uranium-235 causes it to undergo fission and blows up Hilda. From your sheer determination, you survive.", output_text)
             final_frame.pack_forget()
             defend_button.config(state=tk.NORMAL)
             flee_button.config(state=tk.NORMAL)
             win_frame.pack()
         else:
             defend_button.config(state=tk.DISABLED)
             flee_button.config(state=tk.DISABLED)
             typewriter("\nUnfortunately, you do not have anything to fight back with.", output_text)
             typewriter("\n\n\n\n\n\n\n\n\n\n\nHilda shoots you 55 times and you die from bleeding out.", output_text)
             final_frame.pack_forget()
             defend_button.config(state=tk.NORMAL)
             flee_button.config(state=tk.NORMAL)
             death_frame.pack()
     elif choice == "flee":
         defend_button.config(state=tk.DISABLED)
         flee_button.config(state=tk.DISABLED)
         typewriter("\n\n\n\n\n\n\n\n\n\n\nHilda shoots you 55 times and you die from bleeding out.", output_text)
         final_frame.pack_forget()
         defend_button.config(state=tk.NORMAL)
         flee_button.config(state=tk.NORMAL)
         death_frame.pack()

### RUN THE GAME ###
# Starts the game loop!
welcome_frame.pack()
window.mainloop()
      

### OLD CODE: TEXT-BASED ON PYTHON ONLY (MVP) ###

# def start_game():
#     global start
#     x= input("do you wanna start the game now: ")
#     if x == "yes" or x == "y":
#        start = True
#     elif x == "no" or x == "n":
#        start = False
#     else:
#         print("Why are you here if u cant spell normally")
#         return start_game()


# def run():
#     global start
#     while start == True:
#         time.sleep(1)
#         typewriter("pls try to print everything in lower case", output_text)
#         time.sleep(1)
#         typewriter("\n" + "Hank is hatched. It's a boy! You are Hank BTW.", output_text)
#         time.sleep(1)
#         job = input("\n" + "Hank grows up to the age of 10 (late bloomer) and must decide his future career. Geologist or Jeweler?")
#         if job == "geologist" or job == "Geologist":
#             print("Your big boss Boris carbon alpha shows you his collection of rocks.")
#             boris()
#         elif job == "jeweler" or job == "Jeweler":
#             print("Your big boss Boris carbon alpha shows you his collection of jewels.")
#             boris()
#         else:
#             print("stop making spelling errors")
#             run()

# def boris():
#     time.sleep(1)
#     fate = input("He then sends you on a mission to get more stones. Do you accept?: ")
#     if fate == "yes":
#         print("You start collecting stones.")
#         rock_choice()
#     elif fate == "no":
#         print("You get fired, go bankrupt, and spontaneously combust out of grief. GAME ENDS.")
#         replay()
#     else:
#         print("learn how to type")
#         boris()
#         # end the game here

# def rock_choice():
#     time.sleep(1)
#     fate = input("You must decide between the marbley white one or the uranium 235 that is spilt over the water. [input 1 or 2]")
#     if fate == "1":
#         print("You return to Boris and he is pleased.")
#         rizz()
#     elif fate == "2":
#         uranium()
#     else:
#         print("are you dumb")
#         rock_choice()

# def uranium():
#     global rock
#     time.sleep(1)
#     uranium235 = input("save or drink?")
#     if uranium235 == "save":
#         print("You return to Boris empty handed. You are lucky that he is in a good mood and not upset.")
#         rock = "yes"
#         rizz()
#     elif uranium235 == "drink":
#         print("You die from stupidity and poison. GAME ENDS.")
#         rock = "no"
#         replay()
#     else:
#         print("you suck at typing")
#         uranium()
        
# def rizz():
#     time.sleep(1)
#     fate = input("You walk home that day, and bump into a pretty, female penguin, Hilda. Do you flirt with her?" )
#     if fate == "yes":
#         time.sleep(2)
#         print("You say “Do you believe in love at first sight or should I waddle by again?” Hilda blushes." )
#         gift()
#     elif fate == "no":
#         time.sleep(2)
#         print("You and Hilda exchange smiles and she gives you a wink." )
#         gift()
#     else:
#         print("you really can't type can you")
#         rizz()


# def gift():
#     time.sleep(1.5)
#     print("Hilda looks at you and says “Are you an iceberg? Cuz you just melted my heart”. You blush.")
#     time.sleep(2)
#     gift1 = input("You are entranced by Hilda and enter a relationship with her. Do you buy her a gourmet selection of krill or her favorite ice perfume? [input 1 or 2]")
#     if gift1 == "2":
#         print("She is offended by your offering of ice perfume and shoots you on spot for thinking she smells. GAME ENDS")
#         replay()
#     elif gift1 == "1":
#         print("She loves your gourmet selection!")
#         proposal()
#     else:
#         print("please spell correctly girl")
#         gift()

# def proposal():
#     time.sleep(1.5)
#     fate = input("2 years later, you propose to Hilda with a stone you stole from your job. Does she say yes or no? ")
#     if fate == "yes":
#         print("You and Hilda become happily married and Hilda gives birth to a son, Hankiton Jimmy John Joe II Jr. middle name hilda.")
#         finalbattleforyourlife()
#     elif fate == "no":
#         print("HOW DARE YOU THINK I WOULD SAY NO? Hilda kills you with a wooden spoon.. GAME ENDS.")
#         replay()
#     else:
#         print("get better and type better")
#         proposal()

# def finalbattleforyourlife():
#     global rock
#     time.sleep(1.5)
#     print("Hilda grows to hate you for giving her a son and not a daughter. She plans on how to kill you.")
#     time.sleep(1.5)
#     print("This is the final moment. Hilda grabs her glock and stuffs it with bullets.")
#     if rock != "yes":
#         print("Since you never aquired a weapon to defend yourself with throughout the game, Hilda shoots you 55 times. YOU DIE!")
#         replay()
#     else:
#         final = input("Do you choose to throw the Uranium 235 that you gained at Hilda?: ")
#         if final == "yes":
#             print("In the flash of the moment, you pour the radioactive substance on Hilda and she explodes and her ashes melt. YOU WIN!")
#             replay()
#         elif final == "no":
#             print("Hilda shoots you 55 times. YOU DIE!")
#             replay()
#         else:
#             print("lock in and type right")
#             finalbattleforyourlife()

# def replay():
#     grah = input("Do you want to play again?")
#     if grah == "yes":
#         start_game()
#     elif grah == "no":
#         print("ok dude its over")
#     else:
#         print("ok lil bro im ending the game for you")
# start_game() 
# run()
