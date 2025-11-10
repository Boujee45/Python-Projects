import tkinter as tk

#Create Main Window
root = tk.Tk()
root.title("Cool GUI")
root.geometry("300x200") #Width x Height


label = tk.Label(root,text = "Hello World!") #Text or Label
label2 = tk.Button(root, text= "Click Me") #Create a button
label.pack()
label2.pack()

root.mainloop() #Run the application