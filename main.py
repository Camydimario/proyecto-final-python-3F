import tkinter as tk
from view.vista import Frame
from controller.menu import menu_bar

def main():
    ventana = tk.Tk()
    ventana.title("Healthy Plus")
    ventana.iconbitmap("img/healthy_strength.ico")
    ventana.resizable(0,0)
    
    app = Frame(root = ventana)
    
    menu_bar(ventana)
   
    ventana.mainloop()
    
if __name__ == '__main__':
    main()
        
    
    
    