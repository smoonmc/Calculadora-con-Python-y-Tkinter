"""
CALCULADORA:
-Dos campos de texto
-4 botones para las operaciones
-Mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def cFloat(self, numero):
        try:
           result = float(numero)
        except:
           result = 0
           messagebox.showerror("Error", "Introduce bien los datos")
    
        return result

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado de la operación es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")


ventana = Tk()
ventana.title("Ejercicio Calculadora")
ventana.geometry("400x250")
ventana.config(
    bd=10,
    bg="lightblue"
)

calculadora = Calculadora(messagebox)


marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief="ridge", # "sunken"
    bg="CadetBlue"
    
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)



Label(marco, text="Primer número:", bg="CadetBlue").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()


Label(marco, text="Segundo número:", bg="CadetBlue").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="",bg="CadetBlue").pack()

Button(marco, text="Sumar", command=calculadora.sumar, bg="steel blue", cursor="spider").pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar",command=calculadora.restar,bg="steel blue", cursor="spider").pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar",command=calculadora.multiplicar,bg="steel blue", cursor="spider").pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir",command=calculadora.dividir,bg="steel blue", cursor="spider").pack(side="left", fill=X, expand=YES)



ventana.mainloop()
