
#pip install Rich
from rich.console import Console
from rich.text import Text

msg = Text("Happy Friendship Day!", style="bold rainbow")
Console().print(msg)

msg = "Happy Birthday"
import time
for i in range(6):
    print(msg)
    time.sleep(0.5)
    print("\r" + " " * len(msg), end="")
    time.sleep(0.5)


#pip install qrcode
import qrcode
qr = qrcode.make("Happy Friendship Day from Oscar")
qr.save("friendship_day_qr.png")



#pip install pyfiglet
from pyfiglet import figlet_format
print(figlet_format("Happy friendship Day!", font="slant"))



#pip install termcolor
from termcolor import colored
msg = "Happy friendship Day!"
colors = ['red','yellow','green','cyan','blue','magenta']
print(''.join([colored(c, colors[i%6]) for i, c in enumerate(msg)]))


print('\n'.join([''.join([('Friendship'[(x-y)%8] if((x*0.05)**2+(y*0.1)**2-1)**3 -
     (x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,30)])
     for y in range(15,-15,-1)]))

print("Happy Friendship Day")

import tkinter as tk
root = tk.Tk()
tk.Label(root, text="Happy friendship Day!", font=('Helvetica',18), fg="green").pack()
root.mainloop()


#pip install pyttsx3
import  pyttsx3
e = pyttsx3.init()
e.say("Happy friendship Day, dear Friend!")
e.runAndWait()

with open("friendship.txt","w") as f:
    f.write("Happy friendship Day to my dear friend")

from datetime import datetime
print(f"Happy friendship Day - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")