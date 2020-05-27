from tkinter import *
from playsound import playsound
import random
import os

root = Tk()
root.title("Rock Paper Scissors Game")
width = 700
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#050231")
player_score = 0
comp_score = 0
count = 0

#================================IMAGES========================================
blank_img=PhotoImage(file="images/blank.png")
player_rock=PhotoImage(file="images/player_rock.png")
sm_player_rock=player_rock.subsample(3, 3)
player_paper=PhotoImage(file="images/player_paper.png")
sm_player_paper=player_paper.subsample(3, 3)
player_scissor=PhotoImage(file="images/player_scissor.png")
sm_player_scissor= player_scissor.subsample(3, 3)
com_rock=PhotoImage(file="images/com_rock.png")
com_paper=PhotoImage(file="images/com_paper.png")
com_scissor=PhotoImage(file="images/com_scissor.png")
exit1=PhotoImage(file="exit1.PNG")

#===============================METHODS========================================
def Rock():
    playsound("Sound.mp3")
    global count
    global player_score
    global comp_score
    global player_choice
    player_choice = 1
    player_img.configure(image=player_rock)
    MatchProcess()
 
def Paper():
    playsound("Sound.mp3")
    global count
    global player_score
    global comp_score
    global player_choice
    player_choice = 2
    player_img.configure(image=player_paper)
    MatchProcess()
    
def Scissor():
    playsound("Sound.mp3")
    global count
    global player_score
    global comp_score
    global player_choice
    player_choice = 3
    player_img.configure(image=player_scissor)
    MatchProcess()

def MatchProcess():
    global player_score
    global comp_score
    global count
    count += 1
    if count == 10:
        if player_score > comp_score:
            playsound("Sound1.mp3")
            os.system('python won_tkinter.py')            
        elif player_score < comp_score:
            playsound("Sound1.mp3")
            os.system('python lost_tkinter.py')
        else:
            playsound("Sound1.mp3")
            os.system('python tie_tkinter.py')            
        root.destroy()
        #print(player_score," ",comp_score)
    else:
        com_choice = random.randint(1,3)
        if com_choice == 1:
            comp_img.configure(image=com_rock)
            ComputerRock()
        elif com_choice == 2:
            comp_img.configure(image=com_paper)
            ComputerPaper()
        elif com_choice == 3:
            comp_img.configure(image=com_scissor)
            CompututerScissor()

def ComputerRock():
    global player_score
    global comp_score
    if player_choice == 1:
        lbl_status.config(text="IT'S A TIE !!")
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    elif player_choice == 2:
        lbl_status.config(text="PLAYER WINS !!")
        player_score += 1
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    elif player_choice == 3:
        lbl_status.config(text="COMPUTER WINS !!")
        comp_score += 1
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
           
def ComputerPaper():
    global player_score
    global comp_score
    if player_choice == 1:
        lbl_status.config(text="COMPUTER WINS !!")
        comp_score += 1
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    elif player_choice == 2:
        lbl_status.config(text="IT'S A TIE !!")
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    elif player_choice == 3:
        lbl_status.config(text="PLAYER WINS !!")
        player_score += 1
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    
def CompututerScissor():
    global player_score
    global comp_score
    if player_choice == 1:
        lbl_status.config(text="PLAYER WINS !!")
        player_score += 1
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    elif player_choice == 2:
        lbl_status.config(text="COMPUTER WINS !!")
        comp_score += 1
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)
    elif player_choice == 3:
        lbl_status.config(text="IT'S A TIE !!")
        lbl_player_score1.config(text=player_score)
        lbl_comp_score1.config(text=comp_score)

def ExitApp():
    playsound("Sound.mp3")
    root.destroy()
    exit()

#===============================LABEL WIDGET=========================================
player_img = Label(root,image=blank_img)
comp_img = Label(root,image=blank_img)
lbl_player = Label(root,text="PLAYER",fg="#b0cbf7",font=('HoboStd', 17))
lbl_player.place(x=198,y=25,anchor=CENTER)
lbl_player.config(bg="#050231")
lbl_computer = Label(root,text="COMPUTER",fg="#b0cbf7",font=('HoboStd', 17))
lbl_computer.place(x=502,y=25,anchor=CENTER)
lbl_computer.config(bg="#050231")
lbl_player_score=Label(root,text="SCORE :",fg="#b0cbf7",font=('HoboStd', 14))
lbl_player_score.place(x=187,y=307,anchor=CENTER)
lbl_player_score.config(bg="#050231")
lbl_player_score1=Label(root,text="0",fg="#b0cbf7",font=('HoboStd', 14))
lbl_player_score1.place(x=235,y=307,anchor=CENTER)
lbl_player_score1.config(bg="#050231")
lbl_comp_score=Label(root,text="SCORE :",fg="#b0cbf7",font=('HoboStd', 14))
lbl_comp_score.place(x=491,y=307,anchor=CENTER)
lbl_comp_score.config(bg="#050231")
lbl_comp_score1=Label(root,text="0",fg="#b0cbf7",font=('HoboStd', 14))
lbl_comp_score1.place(x=539,y=307,anchor=CENTER)
lbl_comp_score1.config(bg="#050231")
lbl_status=Label(root, text="WELCOME !!", font=('HoboStd', 17),fg="#b0cbf7")
lbl_status.config(bg="#050231")
player_img.place(x=90,y=50)
comp_img.place(x=394,y=50)
lbl_status.place(x=350,y=340,anchor=CENTER)



#===============================BUTTON WIDGET===================================
rock = Button(root, image=sm_player_rock, command=Rock,height=80,width=80)
paper = Button(root, image=sm_player_paper, command=Paper,height=80,width=80)
scissor = Button(root, image=sm_player_scissor, command=Scissor,height=80,width=80)
btn_quit = Button(root, image=exit1,command=ExitApp)
rock.place(x=115,y=370)
paper.place(x=310,y=370)
scissor.place(x=505,y=370)
btn_quit.place(x=350,y=490,anchor=CENTER)


#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
