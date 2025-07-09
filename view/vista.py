import tkinter as tk
from tkinter import ttk

class Frame(tk.Frame):
    
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()
        self.backg = "#ECDFC7"
        self.config(bg= self.backg)
        
        self.label_form()
        self.input_form()
        self.btn_principales()
    
    #ETIQUETAS
        
    def label_form(self):
        self.label_fecha = tk.Label(self, text='Fecha', font=('Helvetica', 11, 'bold'), bg=self.backg)
        self.label_fecha.grid(row=0, column=0, padx=10, pady=10)

        self.label_nombre = tk.Label(self, text='Nombre', font=('Helvetica', 11, 'bold'), bg=self.backg)
        self.label_nombre.grid(row=1, column=0, padx=10, pady=10)

        self.label_habito = tk.Label(self, text='Hábito', font=('Helvetica', 11, 'bold'), bg=self.backg)
        self.label_habito.grid(row=2, column=0, padx=10, pady=10)

        self.label_otro = tk.Label(self, text='Otro dato', font=('Helvetica', 11, 'bold'), bg=self.backg)
        self.label_otro.grid(row=3, column=0, padx=10, pady=10)

        self.label_cumplido = tk.Label(self, font=('Helvetica', 11, 'bold'), bg=self.backg)
        self.label_cumplido.grid(row=4, column=0, padx=10, pady=10)
        
    #ENTRADAS
    
    def input_form(self):
        self.fecha = tk.StringVar()
        self.entry_fecha = tk.Entry(self, textvariable=self.fecha)
        self.entry_fecha.config(width= 50, state= 'disabled')
        self.entry_fecha.grid(row= 0, column= 1, padx= 10, pady=10, columnspan=2)
        
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width= 50, state= 'disabled')
        self.entry_nombre.grid(row= 1, column= 1, padx= 10, pady=10, columnspan=2)
        
        self.habito = tk.StringVar()
        self.entry_habito = tk.Entry(self, textvariable=self.habito)
        self.entry_habito.config(width= 50, state= 'disabled')
        self.entry_habito.grid(row= 2, column= 1, padx= 10, pady=10, columnspan=2)
        
        self.otrodato = tk.StringVar()
        self.entry_otrodato = tk.Entry(self, textvariable=self.otrodato)
        self.entry_otrodato.config(width= 50, state= 'disabled')
        self.entry_otrodato.grid(row= 3, column= 1, padx= 10, pady=10, columnspan=2)
        
        #self.cumplido = tk.BooleanVar()
        self.check_cumplido = tk.Checkbutton(self, text="¿Cumplido?", font=("Arial", 10), bg= self.backg)
        self.check_cumplido.config(state= 'disabled')
        self.check_cumplido.grid(row= 4, column= 1, padx= 10, pady=10, sticky="e", columnspan=2)
        
    #BOTONES
    
    def btn_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.btn_alta.config(width=20,font=('Arial', 12, 'bold'), fg='#FFFFFF', bg="#3ACD66", cursor='hand2',activebackground='#1E7F56',activeforeground='#000000', relief='ridge', bd=3)
        self.btn_alta.grid(row=5, column=0, padx=10,pady=10)
        
        self.btn_Guardar = tk.Button(self, text='Guardar')
        self.btn_Guardar.config(width=20,font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1CA9C9', cursor='hand2',activebackground='#0D7583',activeforeground='#000000', relief='ridge', bd=3, state='disabled')
        self.btn_Guardar.grid(row=5, column=1, padx=10,pady=10)
        
        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cancelar.config(width=20,font=('Arial', 12, 'bold'), fg='#FFFFFF', bg="#FF7300", cursor='hand2',activebackground="#CC3D00",activeforeground='#000000', relief='ridge', bd=3, state='disabled')
        self.btn_cancelar.grid(row=5, column=2, padx=10,pady=10)
        
    #Tabla de datos
    def mostrar_tabla(self):
        self.tabla = ttk.Treeview(self, columns=('Fecha', 'Nombre', 'Habito', 'OtroDato', 'Cumplido'))
        self.tabla.grid(row=6, column=0, columnspan=4)
        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'Fecha')
        self.tabla.heading('#2', text = 'Nombre')
        self.tabla.heading('#3', text = 'Hábito')
        self.tabla.heading('#4', text = 'OtroDato')
        self.tabla.heading('#5', text = 'Cumplido')
        
     #Botones Editar y eliminar de la tabla
     
        self.btn_editar = tk.Button(self, text='Editar')
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1CA9C9', cursor='hand2', activebackground='#0D7583', activeforeground='#000000', relief='ridge')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10)
        
        self.btn_delete = tk.Button(self, text='Borrar')
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#FF7300', cursor='hand2', activebackground='#CC3D00', activeforeground='#000000', relief='ridge')
        self.btn_delete.grid(row=7, column=1, padx=10, pady=10)
    #Habilitar campos
    
    def habilitar_campos(self):
        self.entry_fecha.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_habito.config(state='normal')
        self.entry_otrodato.config(state='normal')
        self.check_cumplido.config(state='normal')
        self.btn_Guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_alta.config(state='disabled')
        
    #Deshabilitar campos
    
    def bloquear_campos(self):
        self.entry_fecha.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_habito.config(state='disabled')
        self.entry_otrodato.config(state='disabled')
        self.check_cumplido.config(state='disabled')
        self.btn_Guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.fecha.set('')
        self.nombre.set('')
        self.habito.set('')
        self.otrodato.set('')