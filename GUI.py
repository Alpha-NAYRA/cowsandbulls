import rootcode as r
import tkinter as tk


root = tk.Tk()
root.title("Cows And Bulls Game")
canvas1 = tk.Canvas(root, width=400, height=320, relief='raised')
canvas1.pack()


label1 = tk.Label(root, text='Cows And Bulls Game')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)


label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)


entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


tries = 4
num = r.generateNum()
print(num)


def submittheguess():
    global tries
    global num

    tries -= 1
    guess = int(entry1.get())
    bull_cow = r.numOfBullsCows(num, guess)

    if tries == 0:
        if num == guess:
            root1 = tk.Tk()
            root1.title("you won")
            canvas2 = tk.Canvas(root1, width=400, height=100, relief='raised')
            canvas2.pack()
            label5 = tk.Label(root1, text='You guessed right!!')
            label5.config(font=('helvetica', 14))
            canvas2.create_window(200, 25, window=label5)
            root.destroy()
        else:
            root1 = tk.Tk()
            root1.title("you lost")
            canvas2 = tk.Canvas(root1, width=400, height=100, relief='raised')
            canvas2.pack()
            label5 = tk.Label(root1, text='You ran out of tries,the number was '+str(num))
            label5.config(font=('helvetica', 14))
            canvas2.create_window(200, 25, window=label5)
            root.destroy()
    else:
        if not r.noDuplicates(guess) or (guess < 1000 or guess > 9999):
            label3 = tk.Label(root, text="Please enter a unique 4 digit number.", font=('helvetica', 10))
            canvas1.create_window(200, 240, window=label3)
            tries += 1

        else:
            label4 = tk.Label(root, text=f"{bull_cow[1]} bulls, {bull_cow[0]} cows", font=('helvetica', 10))
            canvas1.create_window(200, 260, window=label4)

        t = 'Number of guesses left:' + str(tries)
        label7 = tk.Label(root, text=t, font=('helvetica', 10))
        canvas1.create_window(200, 290, window=label7)

        if num == guess:
            root1 = tk.Tk()
            root1.title("you won")
            canvas2 = tk.Canvas(root1, width=400, height=100, relief='raised')
            canvas2.pack()
            label5 = tk.Label(root1, text='You guessed right!!')
            label5.config(font=('helvetica', 14))
            canvas2.create_window(200, 25, window=label5)
            root.destroy()
            tries=0

def gethints():
    root2 = tk.Tk()
    root2.title("Hints")
    canvas3 = tk.Canvas(root2, width=400, height=100, relief='raised')
    canvas3.pack()

    x = r.hints(num)
    t ="there are "+str(x[0])+" even numbers and there are "+str(x[1])+" odd numbers"
    label8 = tk.Label(root2, text=t)
    label8.config(font=('helvetica', 10))
    canvas3.create_window(200, 25, window=label8)

    t=r.upperrange(num)
    label9 = tk.Label(root2, text=t)
    label9.config(font=('helvetica', 10))
    canvas3.create_window(200, 50, window=label9)

    t=r.lowerrange(num)
    label10 = tk.Label(root2, text=t)
    label10.config(font=('helvetica', 10))
    canvas3.create_window(200, 75, window=label10)

button1 = tk.Button(text='submit my guess', command=submittheguess, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

button2 = tk.Button(text='show some hints', command=gethints, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 210, window=button2)


root.mainloop()
