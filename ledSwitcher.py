import RPi.GPIO as GPIO
import tkinter as tk


relayPins = [26, 6, 22, 4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPins, GPIO.OUT)

def turnOffAll():
    GPIO.output(relayPins, GPIO.LOW)

def ledOn(num):
    GPIO.output(relayPins[num], GPIO.HIGH)

def ledOff(num):
    GPIO.output(relayPins[num], GPIO.LOW)

def quitApp(event):
    GPIO.cleanup()
    import sys; sys.exit()


turnOffAll()

root = tk.Tk()
root.title('Switcher')
root.geometry('{}x{}'.format(360, 180))
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

left = tk.Frame(root, bg = 'pink', width = 120, height = 180, padx = 30, pady = 60)
center = tk.Frame(root, bg = 'gray', width = 120, height = 180)
right = tk.Frame(root, bg = 'lavender', width = 120, height = 180)
left.grid(row = 0, column = 0)
center.grid(row = 0, column = 1)
right.grid(row = 0, column = 2)

on_00 = tk.Button(left, text = '00_ON', command = lambda: ledOn(0))
off_00 = tk.Button(left, text = '00_OFF', command = lambda: ledOff(0))
on_00.grid(row = 0, column = 0)
off_00.grid(row = 1, column = 0, pady = 24)

root.mainloop()
GPIO.cleanup()
