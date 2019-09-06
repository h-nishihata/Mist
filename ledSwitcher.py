import RPi.GPIO as GPIO
import tkinter as tk
import time


relayPins = [26, 6, 22, 4]

GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPins, GPIO.OUT)

def turnOffAll():
    GPIO.output(relayPins, GPIO.LOW)

def ledOn(num):
    GPIO.output(relayPins[num], GPIO.HIGH)
    print(str(num) + ': ON')

def ledOff(num):
    GPIO.output(relayPins[num], GPIO.LOW)
    print(str(num) + ': OFF')
    
def delayStart(num0, num1, delay):
    GPIO.output(relayPins[num0], GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(relayPins[num1], GPIO.HIGH)

def quitApp(event):
    GPIO.cleanup()
    import sys; sys.exit()


turnOffAll() 

root = tk.Tk()
root.title('Switcher')
root.geometry('{}x{}'.format(360,360))
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 0)

main = tk.Frame(root, bg='pink', width = 600, height = 150)
bottom = tk.Frame(root, bg='white', width = 600, height = 150, padx = 50, pady = 20)
main.grid(row = 0)
bottom.grid(row = 1)

pane00 = tk.Frame(main, bg='pink', width = 200, height = 150, padx = 20, pady = 20)
pane01 = tk.Frame(main, bg='gray', width = 200, height = 150, padx = 20, pady = 20)
pane02 = tk.Frame(main, bg='lavender', width = 200, height = 150, padx = 20, pady = 20)

pane00.grid(row = 0, column = 0)
pane01.grid(row = 0, column = 1)
pane02.grid(row = 0, column = 2)

on_00 = tk.Button(pane00, text = '00_ON', command = lambda: ledOn(0))
off_00 = tk.Button(pane00, text = '00_OFF', command = lambda: ledOff(0))
on_00.grid(row = 0, column = 0)
off_00.grid(row = 1, column = 0, pady = 12)

on_01 = tk.Button(pane01, text = '01_ON', command = lambda: ledOn(1))
off_01 = tk.Button(pane01, text = '01_OFF', command = lambda: ledOff(1))
on_01.grid(row = 0, column = 0)
off_01.grid(row = 1, column = 0, pady = 12)

on_02 = tk.Button(pane02, text = '02_ON', command = lambda: ledOn(2))
off_02 = tk.Button(pane02, text = '02_OFF', command = lambda: ledOff(2))
on_02.grid(row = 0, column = 0)
off_02.grid(row = 1, column = 0, pady = 12)

firstLabel = tk.Label(bottom, text = '1st')
secondLabel = tk.Label(bottom, text = '2nd')
delayLabel = tk.Label(bottom, text = 'delay')
firstNum = tk.Entry(bottom)
secondNum = tk.Entry(bottom)
delaySec = tk.Entry(bottom)
delay_00 = tk.Button(bottom, text = 'Delay Start',
                     command = lambda: delayStart(int(firstNum.get()), int(secondNum.get()), float(delaySec.get())))
firstLabel.grid(row = 0, column = 0)
secondLabel.grid(row = 1, column = 0)
delayLabel.grid(row = 2, column = 0)
firstNum.grid(row = 0, column = 1)
secondNum.grid(row = 1, column = 1)
delaySec.grid(row = 2, column = 1)
delay_00.grid(row = 3, column = 0)


root.mainloop()
GPIO.cleanup()
