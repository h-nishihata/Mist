import RPi.GPIO as GPIO
import tkinter as tk


relayPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

def ledOn(event):
    GPIO.output(relayPin, GPIO.HIGH)
    print('ON')

def ledOff(event):
    GPIO.output(relayPin, GPIO.LOW)
    print('OFF')

def quitApp(event):
    GPIO.cleanup()
    import sys; sys.exit()


root = tk.Tk()
frame = tk.Frame()
root.title('Switcher')

widget00 = tk.Button(frame, text = 'ON')
widget00.bind('<Button-1>', ledOn)
widget00.pack(padx = 72, pady = 24)

widget01 = tk.Button(frame, text = 'OFF')
widget01.bind('<Button-1>', ledOff)
widget01.pack(padx = 72, pady = 12)

widget02 = tk.Button(frame, text = 'QUIT')
widget02.bind('<Button-1>', quitApp)
widget02.pack(padx = 72, pady = 48)

frame.pack()
root.mainloop()
GPIO.cleanup()
