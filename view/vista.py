import tkinter as tk
from tkinter import ttk
import model.consultas_dao as consulta
from model.consultas_dao import Cursos, guardar_cursos

class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_curso = None
        self.backg = '#F0F8FF'
        self.foreg = '#1E3A8A'
        self.config(bg=self.backg)

        self.label_form()
        self.input_form()
        self.btn_principales()
        self.mostrar_tabla()

    # ETIQUETAS
    def label_form(self):
        self.label_curso = tk.Label(self, text='Nombre del curso', font=('Helvetica', 11, 'bold'), bg=self.backg, fg=self.foreg)
        self.label_curso.grid(row=0, column=0, padx=10, pady=10)

        self.label_profesor = tk.Label(self, text='Profesor o institución', font=('Helvetica', 11, 'bold'), bg=self.backg, fg=self.foreg)
        self.label_profesor.grid(row=1, column=0, padx=10, pady=10)

        self.label_fecha = tk.Label(self, text='Fecha de inscripción', font=('Helvetica', 11, 'bold'), bg=self.backg, fg=self.foreg)
        self.label_fecha.grid(row=2, column=0, padx=10, pady=10)

        self.label_modalidad = tk.Label(self, text='Modalidad', font=('Helvetica', 11, 'bold'), bg=self.backg, fg=self.foreg)
        self.label_modalidad.grid(row=3, column=0, padx=10, pady=10)

        self.label_estado = tk.Label(self, font=('Helvetica', 11, 'bold'), bg=self.backg, fg=self.foreg)
        self.label_estado.grid(row=4, column=0, padx=10, pady=10)

    # ENTRADAS
    def input_form(self):
        
        #ENTRY
        self.curso = tk.StringVar()
        self.entry_curso = tk.Entry(self, textvariable=self.curso, width=50, state='disabled')
        self.entry_curso.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.profesor = tk.StringVar()
        self.entry_profesor = tk.Entry(self, textvariable=self.profesor, width=50, state='disabled')
        self.entry_profesor.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.fecha = tk.StringVar()
        self.entry_fecha = tk.Entry(self, textvariable=self.fecha, width=50, state='disabled')
        self.entry_fecha.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        # COMBOBOX
        self.modalidad = tk.StringVar()
        self.combo_modalidad = ttk.Combobox(self, textvariable=self.modalidad, values=["Presencial", "Virtual",  "Híbrido"], state='disabled')
        self.combo_modalidad.config(width=47)
        self.combo_modalidad.set("Seleccione una opción...")  # Simula placeholder
        self.combo_modalidad.grid(row=3, column=1, padx=10, pady=10, columnspan=2)

        # CHECKBUTTON
        self.estado = tk.BooleanVar()
        self.check_estado = tk.Checkbutton(self, variable=self.estado, text='¿Finalizado?', font=("Helvetica", 10), bg=self.backg)
        self.check_estado.config(state='disabled')
        self.check_estado.grid(row=4, column=1, padx=10, pady=10, sticky="e", columnspan=2)


    # BOTONES
    def btn_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg="#3ACD66", cursor='hand2', activebackground='#1E7F56', activeforeground='#000000', relief='ridge', bd=3)
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1CA9C9', cursor='hand2', activebackground='#0D7583', activeforeground='#000000', relief='ridge', bd=3, state='disabled')
        self.btn_guardar.grid(row=5, column=1, padx=10, pady=10)

        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg="#FF7300", cursor='hand2', activebackground="#CC3D00", activeforeground='#000000', relief='ridge', bd=3, state='disabled')
        self.btn_cancelar.grid(row=5, column=2, padx=10, pady=10)

    # TABLA
    def mostrar_tabla(self):
        self.tabla = ttk.Treeview(self, columns=('Curso', 'Profesor', 'Fecha', 'Modalidad', 'Finalizado'))
        self.tabla.grid(row=6, column=0, columnspan=4)
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Curso')
        self.tabla.heading('#2', text='Profesor')
        self.tabla.heading('#3', text='Fecha')
        self.tabla.heading('#4', text='Modalidad')
        self.tabla.heading('#5', text='Finalizado')

        self.btn_editar = tk.Button(self, text='Editar')
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1CA9C9', cursor='hand2', activebackground='#0D7583', activeforeground='#000000', relief='ridge')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text='Borrar')
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#FF7300', cursor='hand2', activebackground='#CC3D00', activeforeground='#000000', relief='ridge')
        self.btn_delete.grid(row=7, column=1, padx=10, pady=10)
        
    def guardar_campos(self):
        cursos = Cursos(
            self.curso.get(),
            self.profesor.get(),
            self.fecha.get(),
            self.modalidad.get(),
            self.estado.get()
        )
        
        if self.id_curso == None:
            consulta.guardar_cursos(cursos)
        # else:
        #     consulta.editar_cursos(cursos, int(self.id_curso)) #Falta hacer función en consultas_dao y vista
        self.mostrar_tabla()
        self.bloquear_campos()
        

    # HABILITAR
    def habilitar_campos(self):
        self.entry_curso.config(state='normal')
        self.entry_profesor.config(state='normal')
        self.entry_fecha.config(state='normal')
        self.combo_modalidad.config(state='readonly')
        self.check_estado.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_alta.config(state='disabled')

    # BLOQUEAR
    def bloquear_campos(self):
        self.entry_curso.config(state='disabled')
        self.entry_profesor.config(state='disabled')
        self.entry_fecha.config(state='disabled')
        self.combo_modalidad.config(state='disabled')
        self.check_estado.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.btn_alta.config(state='normal')

        self.curso.set('')
        self.profesor.set('')
        self.fecha.set('')
        self.combo_modalidad.set("Seleccione una opción...")
        self.estado.set(False)
