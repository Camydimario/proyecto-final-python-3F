import tkinter as tk
from view.vista import Frame
from controller.menu import menu_bar

def main():
    ventana = tk.Tk()
    ventana.title("Class Tracker")
    ventana.iconbitmap("img/class_tracker2.ico")
    ventana.resizable(0,0)
    
    app = Frame(root = ventana)
    
    menu_bar(ventana)
   
    ventana.mainloop()
    
if __name__ == '__main__':
    main()
        
    
    
    