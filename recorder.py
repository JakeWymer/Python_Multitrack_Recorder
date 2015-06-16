#!usr/bin python

__author__ = 'Jake Wymer'

from tkinter import *
from tkSnack import *

root = Tk()
initializeSnack(root)
root.geometry('1920x800')

print(root.tk.call('snack::audio', 'inputDevices'))

F = Frame(root)
G = Frame(root)
H = Frame(root)
I = Frame(root)
top = Frame(root)

snd1 = Sound()
snd2 = Sound()
snd3 = Sound()
snd4 = Sound()


def start(this_sound):
    this_sound.record()
    if snd1.length() > 0:
        play(snd1)

    if snd2.length() > 0:
        play(snd1)

    if snd3.length() > 0:
        play(snd1)

    if snd4.length() > 0:
        play(snd1)



def play(this_sound):
    this_sound.play()


def stop(this_sound):
    this_sound.stop()


def load(this_sound):
    file = root.tk.call('eval', 'snack::getOpenFile')
    this_sound.load(file)


def save(this_sound):
    file = root.tk.call('eval', 'snack::getSaveFile')
    this_sound.save(file)


def play_all():
    snd1.play()
    snd2.play()
    snd3.play()
    snd4.play()


def stop_all():
    snd1.stop()
    snd2.stop()
    snd3.stop()
    snd4.stop()


def mix():
    snd1.mix(snd2)
    snd1.mix(snd3)
    snd1.mix(snd4)
    snd2.flush()
    snd3.flush()
    snd4.flush()


def clear(sound_name):
    sound_name.flush()


def clear_all():
    snd1.flush()
    snd2.flush()
    snd3.flush()
    snd4.flush()


def track(sound_name):
    c = SnackCanvas(height=100, width=1920, bg='white')
    c.pack()
    c.create_waveform(0, 0, sound=sound_name, width=1920, height=100, pixelspersec=500)


def buttons(sound_name, frame):

    start_button = Button(frame, text='Record', command=lambda: start(sound_name))
    start_button.pack(side='left')

    play_button = Button(frame, text='Play', command=lambda: play(sound_name))
    play_button.pack(side='left')

    save_button = Button(frame, text='Save', command=lambda: save(sound_name))
    save_button.pack(side='left')

    stop_button = Button(frame, text='Stop', command=lambda: stop(sound_name))
    stop_button.pack(side='left')

    load_button = Button(frame, text='Load', command=lambda: load(sound_name))
    load_button.pack(side='left')

    clear_button = Button(frame, text='Clear Track', command=lambda: clear(sound_name))
    clear_button.pack(side='left')

top.pack(side='top')

play_all_button = Button(top, text='Play All', command=play_all)
play_all_button.pack(side='left')

stop_all_button = Button(top, text='Stop All', command=stop_all)
stop_all_button.pack(side='left')

mix_button = Button(top, text='Mix', command=mix)
mix_button.pack(side='left')

clear_all_button = Button(top, text='Clear All', command=clear_all())
clear_all_button.pack(side='left')

track(snd1)
buttons(snd1, F)
F.pack(anchor=W)

track(snd2)
buttons(snd2, G)
G.pack(anchor=W)

track(snd3)
buttons(snd3, H)
H.pack(anchor=W)

track(snd4)
buttons(snd4, I)
I.pack(anchor=W)


root.mainloop()