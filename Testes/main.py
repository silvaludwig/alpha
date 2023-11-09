import tkinter as tk
from janela1 import Window1
from janela2 import Window2

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        self.label = tk.Label(root, text='Welcome!')
        self.label.pack()
        
        self.button1 = tk.Button(root, text="New Income", command=self.open_window1)
        self.button1.pack()

        self.button2 = tk.Button(root, text="New Expense", command=self.open_window2)
        self.button2.pack()

    def open_window1(self):
        window1_root = tk.Toplevel(self.root)
        window1 = Window1(window1_root)

    def open_window2(self):
        window2_root = tk.Toplevel(self.root)
        window2 = Window2(window2_root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


