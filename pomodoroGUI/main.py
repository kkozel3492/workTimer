from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
CHECK_TEXT = '✓'
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    global reps
    checkMarks.config(text='')
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text='00:00')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countDown(longBreakSec)
        topLabel.config(fg=RED, text='Long Break', font=(FONT_NAME, 36, 'bold'), bg=YELLOW)
    elif reps % 2 == 0:
        countDown(shortBreakSec)
        topLabel.config(fg=PINK, text='Short Break', font=(FONT_NAME, 36, 'bold'), bg=YELLOW)
    else:
        countDown(workSec)
        topLabel.config(fg=GREEN, text='Work', font=(FONT_NAME, 36, 'bold'), bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    workSession = math.floor(reps / 2)

    # Format Clock
    countMin = math.floor(count / 60)
    countSec = count % 60
    if countSec < 10:
        countSec = f'0{countSec}'
    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        checks = ''
        for work in range(workSession):
            checks += CHECK_TEXT
            checkMarks.config(text=checks)
        startTimer()


# ---------------------------- UI SETUP ------------------------------- #
# Create Window
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Create Label
topLabel = Label(fg=GREEN, text='Timer', font=(FONT_NAME, 36, 'bold'), bg=YELLOW)
topLabel.grid(column=1, row=0)

# Create Button
startButton = Button(text='start', font=(FONT_NAME, 10, 'bold'), command=startTimer)
startButton.grid(column=0, row=2)

resetButton = Button(text='reset', font=(FONT_NAME, 10, 'bold'), command=resetTimer)
resetButton.grid(column=2, row=2)

# Create tomato graphic
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image((100, 112), image=tomato)
timerText = canvas.create_text((100, 130), text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Create Checkmarks
checkMarks = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, 'bold'))
checkMarks.grid(column=1, row=3)

window.mainloop()
