from tkinter import *
from tkinter import ttk

_heightBtn= 50
_widthBtn = 68

#definimos frames dentro de frames para controlar el diseño

#Frame para el recuadro donde va el resultado de la calculadora
class CalcDisplay(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height =_heightBtn, width=_widthBtn*4)

        #hace que se propage para rellenar el espacio
        self.pack_propagate(0)

        s = ttk.Style()
        #configuracion que se aplicara a ttk lable
        s.configure('my.TLabel', font='Helvetica 40')

        self.lblDisplay = ttk.Label(self, text='0', style='my.TLabel', anchor=E)
        self.lblDisplay.pack(fill=BOTH, expand=True)

#frame para los botones de la calculadora (caixes per cada boto)
class CalcButton(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn)
        self.pack_propagate(0)

        self.button = ttk.Button(self, text=kwargs['text'], command=kwargs['command'])
        self.button.pack(fill = BOTH, expand=True)



class Calculator(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height= kwargs['height'],width = kwargs['width'])
        self.display = CalcDisplay(self)
#        self.display.place(x=0, y=0)
        self.display.grid(column=0, row = 0, columnspan=4)

        #creamos los botones
        CalcButton(self, text='C', command=None).grid(column=0, row=1)
        CalcButton(self, text='+/-', command=None).grid(column=1, row=1)
        CalcButton(self, text='%', command=None).grid(column=2, row=1)
        CalcButton(self, text='/', command=None).grid(column=3, row=1)
        CalcButton(self, text='7', command=None).grid(column=0, row=2)
        CalcButton(self, text='8', command=None).grid(column=1, row=2)
        CalcButton(self, text='9', command=None).grid(column=2, row=2)
        CalcButton(self, text='X', command=None).grid(column=3, row=2)
        CalcButton(self, text='4', command=None).grid(column=0, row=3)
        CalcButton(self, text='5', command=None).grid(column=1, row=3)
        CalcButton(self, text='6', command=None).grid(column=2, row=3)
        CalcButton(self, text='-', command=None).grid(column=3, row=3)
        CalcButton(self, text='1', command=None).grid(column=0, row=4)
        CalcButton(self, text='2', command=None).grid(column=1, row=4)
        CalcButton(self, text='3', command=None).grid(column=2, row=4)
        CalcButton(self, text='+', command=None).grid(column=3, row=4)
        CalcButton(self, text='0', command=None).grid(column=0, row=5, columnspan=2)
        CalcButton(self, text=',', command=None).grid(column=2, row=5)
        CalcButton(self, text='=', command=None).grid(column=3, row=5)

    

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Calculator')
        self.geometry('{}x{}'.format(_widthBtn*4, _heightBtn*6))

        self.calculator = Calculator(self, height=_heightBtn*6, width=_widthBtn*4)
        self.calculator.place(x=0, y=0)

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.start()