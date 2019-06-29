from tkinter import *
from tkinter import ttk

_heightBtn= 50
_widthBtn = 68

#definimos frames dentro de frames para controlar el diseño

#Frame para el recuadro donde va el resultado de la calculadora
class CalcDisplay(ttk.Frame):
    #creamos una variable dentro de una clase se llama atributo i define el estado de la instancia
    #self._value nos sirve para saber lo que hay en pantalla
    _value='0'
    _espositivo = True

    def __init__(self, parent, **kwargs):
       
        ttk.Frame.__init__(self, parent, height =_heightBtn, width=_widthBtn*4)

        #hace que se propage para rellenar el espacio
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        #configuracion que se aplicara a ttk lable
        s.configure('my.TLabel', font='Helvetica 30')

        self.lblDisplay = ttk.Label(self, text=self._value, style='my.TLabel', anchor=E, foreground='white', background='black')
        self.lblDisplay.pack(fill=BOTH, expand=True)

    def addDigit(self, digito):
       


        #para controlar el maximo de caracteres que entran en la calculadora a un maximo de 10
        if self._value[0] != '-' and len(self._value) >= 10 or len(self._value)>= 11:
            return
        '''
         if self._value[0] == '-':
            longmax = 11
        esle:
            longmax = 10

        if len(self._value) == 10:
            return
        '''
        if self._value == '0':
            self._value = digito
        else:
            self._value += digito

        self.pintar()

    def pintar(self):
        
        #para pintar los valores de los botones en el Label display
        self.lblDisplay.configure(text=self._value)
    
    def reset(self):
        self._value = '0'
        #reseteamos la opcion del signo para que siga haciendolo correctamente
        self._espositivo = True
        self.pintar()

    def signo(self):
        if self._value == '0':
            return

        if self._espositivo:
            self._value = '-'+self._value
            
        else:
            self._value = self._value[1:]
        
        #si esta en true lo niega a false, si esta en false lo niega a true
        self._espositivo = not self._espositivo
        self.pintar()
            



#frame para los botones de la calculadora (caixes per cada boto)
class CalcButton(ttk.Frame):
    def __init__(self, parent, **kwargs):

        #si no se informa bw valdrá 1
        '''
        if 'bw' in kwargs:
                    bw = kwargs['bw']
        else:
            bw = 1
        '''
        #equivale al if de arriba en una línea
        bw = kwargs['bw'] if 'bw' in kwargs else 1 

        ttk.Frame.__init__(self, parent, height=_heightBtn, width=_widthBtn * bw)
        self.pack_propagate(0) #(los componentes hijos no controlan su tamaño1)

        self.button = ttk.Button(self, text=kwargs['text'], command=kwargs['command'])
        self.button.pack(fill = BOTH, expand=True)



class Calculator(ttk.Frame):
    _op1 = None
    _op2 = None
    _operador = None

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height= kwargs['height'],width = kwargs['width'])
        self.display = CalcDisplay(self)
#        self.display.place(x=0, y=0)
        self.display.grid(column=0, row = 0, columnspan=4)

        #creamos los botones
        #para el comand definimos una funcion en CalcDisplay
        CalcButton(self, text='C', command=self.display.reset).grid(column=0, row=1)
        CalcButton(self, text='+/-', command=self.display.signo).grid(column=1, row=1)
        CalcButton(self, text='%', command=None).grid(column=2, row=1)
        CalcButton(self, text='/', command=None).grid(column=3, row=1)
        CalcButton(self, text='7', command=lambda: self.display.addDigit('7')).grid(column=0, row=2)
        CalcButton(self, text='8', command=lambda: self.display.addDigit('8')).grid(column=1, row=2)
        CalcButton(self, text='9', command=lambda: self.display.addDigit('9')).grid(column=2, row=2)
        CalcButton(self, text='X', command=None).grid(column=3, row=2)
        CalcButton(self, text='4', command=lambda: self.display.addDigit('4')).grid(column=0, row=3)
        CalcButton(self, text='5', command=lambda: self.display.addDigit('5')).grid(column=1, row=3)
        CalcButton(self, text='6', command=lambda: self.display.addDigit('6')).grid(column=2, row=3)
        CalcButton(self, text='-', command=None).grid(column=3, row=3)
        CalcButton(self, text='1', command=lambda: self.display.addDigit('1')).grid(column=0, row=4)
        CalcButton(self, text='2', command=lambda: self.display.addDigit('2')).grid(column=1, row=4)
        #utilizamos las funciones anónimas lambda para poder pasar un parametro por comand así no tenemos que definir la funcion i podemos pasarle el valor
        CalcButton(self, text='3', command=lambda: self.display.addDigit('3')).grid(column=2, row=4)
        CalcButton(self, text='+', command=lambda: self.opera('+')).grid(column=3, row=4)
        CalcButton(self, text='0', command=lambda: self.display.addDigit('0'), bw=2).grid(column=0, row=5, columnspan=2) #informamos a kwargs de clave7valor bw=2 para que ocupe dos botones
        CalcButton(self, text=',', command=None).grid(column=2, row=5)
        CalcButton(self, text='=', command=None).grid(column=3, row=5)

        #ponemos aqui las operaciones aritméticas por que son de calculadora

    def opera(self, operador):
        if self._op1 is None:
            self._op1 = float(self.display._value)
            self._operador = operador
            self.display.reset()
        else:
            self._op2 = float(self.display._value)
            if self._operador == '+':
                resultado = self._op1 + self._op2
            elif self._operador == '-':
                resultado = self._op1 - self._op2
            elif self._operador == '*':
                resultado = self._op1 * self._op2
            else:
                resultado = self._op1 * self._op2
            
            self._op1 = resultado
            self._operador = operador
            resultador = str(resultado)
            self.display._value = resultado
            self.display.pintar()

    def enviar(self, value):
        self.display.pintar(value)
    

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