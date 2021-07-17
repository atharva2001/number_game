#8 labels needed in total
import random
from tkinter import *
from threading import *
import winsound
import time
import re


#variable declaration

wrong = 0
lives = 3
score = 0
diff = 0
file = open("score.txt", "r+")
file.write("Highest Score is ")
count = file.read()
res = int(re.search(r'\d+', count).group())

#ui starts

root = Tk()
root.iconbitmap('path to the .ico file("absolute path")')
root.geometry("700x500")
root.title("Number Game")
root['bg']='black'
root.resizable(0,0)


font_tuple=("Comic Sans MS",15,"bold")
norms=("Helvetica",11,"bold")
lvls1=("Helvetica",13,"italic")
lvls2=("Helvetica",15,"bold")
font_tuple2=("Comic Sans MS",12,"bold")

Label(root,text="NUMBER GAME           \n\n\n",font=font_tuple,bg="black",fg="red").grid(row=0,column=0)
#labels just created
l1 = Label(root,fg="pink",bg="black",font=norms)
l1.grid(row=0,column=5000)
l2 = Label(root,fg="white",bg="black")
l2.grid(row=1,column=5000)
l3 = Label(root,fg="brown",bg="black",font=norms)
l3.grid(row=2,column=5000)
l4 = Label(root,fg="white",bg="black",font=lvls1)
l4.grid(row=4, column=5000)
l5 = Label(root,fg="white",bg="black")
l5.grid(row=95, column=5000)
l6 = Label(root,fg="white",bg="black")
l6.grid(row=55, column=5000)
l8 = Label(root,fg="pink",bg="black",font=font_tuple)
l8.grid(row=25, column=5000)
l8.config(text="Guess the next number?")
l9 = Label(root,fg="blue",bg="black",font=lvls1)
l9.grid(row=75, column=5000)

def logiccommon():
    global t,z,wrong, lives, score, file, count, res, diff,q
    l1.config(text="*** Highest Score is {} ***".format(res))
    l9.config(text="*** Your Score is {} ***".format(score))

    if (score == 0 or score <= 15):
        diff = 1
        a = random.randint(0, 1)
        l2.config(text="!!! EASY LEVEL!!!",fg="green",font=lvls1)
    elif (score >= 21 or score <= 55):
        diff = 2
        a = random.randint(5, 6)
        l2.config(text="!!! MEDIUM LEVEL!!!",fg="yellow",font=lvls1)
    if (score >= 61):
        diff = 3
        a = random.randint(2, 4)
        l2.config(text="!!! HARD LEVEL!!!",fg="red",font=lvls1)

    l3.config(text="Your lives are {}".format(lives))
    c = random.randint(1, 101)
    v = 5
    u = 5000

    if (a == 0 and diff == 1):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=c + x,fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z = (c + x)
    if (a == 1 and diff == 1):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=c - x,fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z = (c - x)
    if (a == 5 and diff == 2):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text= (c + (2 * x)),fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z =(c + (2 * x))
    if (a == 6 and diff == 2):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=(c + (x ** 2)),fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z = (c + (x ** 2))
    if (a == 3 and diff == 3):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=(c + (x ** 3)),fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z = (c + (x ** 3))
    if (a == 2 and diff == 3):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=((c*2) * x),fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z = ((c*2) * x)
    if (a == 4 and diff == 3):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=(c + (x ** 3)),fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z = (c + (x ** 3))
    if (a == 4 and diff == 3):
        for x in range(0, 4):
            # Label(root, text=str(c+x)).pack()

            Label(root, text=(c * (c + x)),fg="white",bg="black",font=lvls2).grid(row=v,column=u)
            v+=1


            if (x == 3):
                x += 1
                z =(c * (c + x))
def check():
    global score,lives,res

    a = int(t.get())
    var = random.randint(1, 5)
    if lives != 1:
        if a == z:

            l6.config(text="Correct the answer is {}".format(z),font=lvls1,fg="green")
            winsound.PlaySound('Sound/win.wav', winsound.SND_FILENAME)
            if var == 1:
                l4.config(text="Nice One")

            if var == 2:
                l4.config(text="Well Done")
            if var == 3:
                l4.config(text="You got that!")
            if var == 4:
                l4.config(text="Nice Brain")
            if var == 5:
                l4.config(text="Appreciate it")
            score += 5
            file.seek(0)
            file.truncate()
            file.write("Highest Score is ")
            file.write(str(score))

        if a != z:

            l6.config(text="Wrong the answer was {}".format(z),font=lvls1,fg="red")
            winsound.PlaySound('Sound/aww.wav', winsound.SND_FILENAME)
            if var == 1:
                l4.config(text="Wrong One")
            if var == 2:
                l4.config(text="Go Learn Math!!")
            if var == 3:
                l4.config(text="LOL!!!")
            if var == 4:
                l4.config(text="Dont give up!!!")
            if var == 5:
                l4.config(text="Lets try again")
            lives -= 1

        buttoncall()
    else:
        l3.config(text="Your lives are 0")
        file.close()
        if (res <= score):

            l5.config(text="You created a new record!!",font=font_tuple,fg="yellow")



        else:
            l5.config(text="You Looooooooooser!!!!!!!!",font=font_tuple,fg="orange")




def buttoncall():
    global t
    logiccommon()

    t = Entry(root)
    t.grid(row=30,column=5000)
    b = Button(root, text="Check!",command=check)
    b.grid(row=89,column=5000)



class Sound(Thread):
    def run(self):
        time.sleep(0.5)
        frequency = 2000  # Set Frequency To 2500 Hertz
        duration = 500  # Set Duration To 1000 ms == 1 second
        winsound.PlaySound('Sound/intro.wav', winsound.SND_FILENAME)



y = Sound()
y.start()
buttoncall()

#logic

root.mainloop()
