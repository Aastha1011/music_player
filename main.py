def resumemusic():
    root.resumebutton.grid_remove()
    root.pausebutton.grid()
    mixer.music.unpause()

def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)

def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.1)

def stopmusic():
    mixer.music.stop()

def pausemusic():
    mixer.music.pause()
    root.pausebutton.grid_remove()
    root.resumebutton.grid()

def playmusic():
    ad= audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()

def musicurl():
    dd= filedialog.askopenfilename()
    audiotrack.set(dd)

def createWidgets():

    tracklabel = Label(root, text='Select Audio Track:', background = 'bisque', font = ('arial', 15, 'bold'))
    tracklabel.grid(row=0, column=0, padx=20, pady=22)

    tracklabelentry= Entry(root, font = ('arial', 16, 'bold'), width= 35, textvariable=audiotrack)
    tracklabelentry.grid(row=0, column =1, padx=20, pady=20)

    browsebutton = Button(root, text='Search', bg='gainsboro', font = ('arial', 13, 'bold'), width=20, bd=3,
                          activebackground='papaya whip', command = musicurl )
    browsebutton.grid(row=0, column =3, padx=20, pady=20)

    playbutton = Button(root, text='Play', bg='pale violet red', font=('arial', 13, 'bold'), width=20, bd=3,
                        activebackground='ivory2', command=playmusic)
    playbutton.grid(row=1, column=0, padx=20, pady=20)

    root.pausebutton = Button(root, text='Pause', bg='pale violet red', font=('arial', 13, 'bold'), width=20,
                         bd=3, activebackground='ivory2', command=pausemusic)
    root.pausebutton.grid(row=1, column=1, padx=20, pady=20)

    root.resumebutton = Button(root, text='Resume', bg='pale violet red', font=('arial', 13, 'bold'), width=20,
                         bd=3, activebackground='ivory2', command=resumemusic)
    root.resumebutton.grid(row=1, column=1, padx=20, pady=20)
    root.resumebutton.grid_remove()

    volumeupbutton = Button(root, text='Volume Up', bg='pale violet red', font=('arial', 13, 'bold'), width=20, bd=3,
                            activebackground='ivory2', command = volumeup)
    volumeupbutton.grid(row=1, column=3, padx=20, pady=20)

    volumedownbutton = Button(root, text='Volume Down', bg='pale violet red', font=('arial', 13, 'bold'), width=20, bd=3,
                              activebackground='ivory2', command = volumedown)
    volumedownbutton.grid(row=2, column=3, padx=20, pady=20)

    stopbutton = Button(root, text='Stop', bg='red', font=('arial', 13, 'bold'), width=20, bd=3,
                        command = stopmusic)
    stopbutton.grid(row=2, column=0, padx=20, pady=20)


from tkinter import *
from tkinter import filedialog
from pygame import mixer


root = Tk()
root.geometry('1100x500+200+50')
root.title("Music Player!!")
root.iconbitmap('music.ico')
root.resizable(False, False)
root.configure(bg='bisque')

audiotrack = StringVar()

ss = 'Play your Music!!!'
count = 0
text = ''

sliderlabel = Label(root, text=ss, bg='tomato2', font = ('arial', 40, 'bold'))
sliderlabel.grid(row=4, column=0, padx=30, pady=20, columnspan=3)

def IntroLabelTrick():
    global count, text
    if(count >= len(ss)):
        count = -1
        text = ''
        sliderlabel.configure(text=text)

    else:
        text = text + ss[count]
        sliderlabel.configure(text = text)
    count += 1
    sliderlabel.after(200, IntroLabelTrick)

IntroLabelTrick()
mixer.init()
createWidgets()
root.mainloop()

