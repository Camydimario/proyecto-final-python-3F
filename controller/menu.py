import tkinter as tk

def menu_bar(root):
    bar = tk.Menu(root)
    root.config(menu = bar, width = 300, height = 300)
    menu_inicio = tk.Menu(bar, tearoff = 0)
    menu_consultas = tk.Menu(bar, tearoff = 0)
    menu_acerca_de = tk.Menu(bar, tearoff = 0)
    menu_ayuda = tk.Menu(bar, tearoff = 0)
    
#Principal

    bar.add_cascade(label= 'Inicio', menu = menu_inicio)
    bar.add_cascade(label= 'Consultas', menu = menu_consultas)
    bar.add_cascade(label= 'Acerca de Healthy Plus...', menu = menu_acerca_de)
    bar.add_cascade(label= 'Ayuda', menu = menu_ayuda)
    
#submenu inicio
    menu_inicio.add_command(label= 'Conectar BD')
    menu_inicio.add_command(label= 'Desconectar DB')
    menu_inicio.add_command(label= 'Salir', command= root.destroy)

#submenu consultas
    menu_consultas.add_command(label='Agregar')
    menu_consultas.add_command(label='Modificar')
    menu_consultas.add_command(label='Elminar')
#submenu acerca de...
    menu_acerca_de.add_command(label='Sobre nosotros')

#submenu ayuda
    menu_ayuda.add_command(label='info')
    menu_ayuda.add_command(label='Preguntas frecuentes')
