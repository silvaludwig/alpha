from tkinter import *

window = Tk()
window.title('teste com entry')
window.geometry("950x200")



name = Label(text='Name: ', font='Times 35 bold').grid(row=1, column=0)

exit_button = Button(window, text='Exit', command=window.destroy).grid()

window.mainloop()