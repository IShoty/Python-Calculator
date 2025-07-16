from customtkinter import *
global numbers
global numbers2
global Num1
global operatorDef
numbers = ''
numbers2 = ''
Num1 = True
resultTrue = False
operatorDef = ''

class CalGUI():
    def __init__(self):
        self.root = CTk()
        self.root.geometry('420x300')
        self.label = CTkLabel(self.root, text=f'{numbers}')
        self.label.grid(row= 0, column=3, padx=5, pady=5)
        self.num = CTkLabel(self.root, text=f'Your first number = {numbers}')
        self.num.grid(row=0 , column= 0, padx=5, pady=5)

        self.button1 = CTkButton(self.root, text='1',command = lambda: self.addNum('1'), height=30, width=50)
        self.button2 = CTkButton(self.root, text='2',command = lambda: self.addNum('2'), height=30, width=50)
        self.button3 = CTkButton(self.root, text='3',command = lambda: self.addNum('3'), height=30, width=50)
        self.button4 = CTkButton(self.root, text='4',command = lambda: self.addNum('4'), height=30, width=50)
        self.button5 = CTkButton(self.root, text='5',command = lambda: self.addNum('5'), height=30, width=50)
        self.button6 = CTkButton(self.root, text='6',command = lambda: self.addNum('6'), height=30, width=50)
        self.button7 = CTkButton(self.root, text='7',command = lambda: self.addNum('7'), height=30, width=50)
        self.button8 = CTkButton(self.root, text='8',command = lambda: self.addNum('8'), height=30, width=50)
        self.button9 = CTkButton(self.root, text='9',command = lambda: self.addNum('9'), height=30, width=50)
        self.button0 = CTkButton(self.root, text='0',command = lambda: self.addNum('0'), height=30, width=50)

        self.button1.grid(row = 2, column=1, padx=5, pady=5)
        self.button2.grid(row = 2, column=2, padx=5, pady=5)
        self.button3.grid(row = 2, column=3, padx=5, pady=5)
        self.button4.grid(row = 3, column=1, padx=5, pady=5)
        self.button5.grid(row = 3, column=2, padx=5, pady=5)
        self.button6.grid(row = 3, column=3, padx=5, pady=5)
        self.button7.grid(row = 4, column=1, padx=5, pady=5)
        self.button8.grid(row = 4, column=2, padx=5, pady=5)
        self.button9.grid(row = 4, column=3, padx=5, pady=5)
        self.button0.grid(row = 5, column=2, padx=5, pady=5)

        self.buttonX = CTkButton(self.root, text='X',command = lambda: self.op('X'), height=30, width=50)
        self.buttonD = CTkButton(self.root, text='/',command = lambda: self.op('/'), height=30, width=50)
        self.buttonpl = CTkButton(self.root, text='+',command = lambda: self.op('+'), height=30, width=50)
        self.buttonmi = CTkButton(self.root, text='-',command = lambda: self.op('-'), height=30, width=50)
        self.buttoneq = CTkButton(self.root, text='=',command = lambda: self.Cal(), height=30, width=50)
        self.buttonac = CTkButton(self.root, text='A/C',command = lambda: self.clear(), height=30, width=50)

        self.buttonX.grid(row = 2, column = 4, padx=5, pady=5)
        self.buttonD.grid(row = 3, column = 4, padx=5, pady=5)
        self.buttonpl.grid(row = 4, column = 4, padx=5, pady=5)
        self.buttonmi.grid(row = 5, column = 4, padx=5, pady=5)
        self.buttoneq.grid(row = 6, column = 4, padx=5, pady=5)
        self.buttonac.grid(row = 7, column = 4, padx=5, pady=5)

        self.error = CTkLabel(self.root, text='')
        self.error.grid(row= 9, column=1)

    def op(self,operator):
        global numbers
        global numbers2
        global Num1
        global resultTrue
        global operatorDef

        if operator == 'X':
            Num1 = False
            self.num.configure(text=f'Your first number = {numbers}')
            operatorDef = 'X'
        elif operator == '/':
            Num1 = False
            self.num.configure(text=f'Your first number = {numbers}')
            operatorDef = '/'
        elif operator == '+':
            Num1 = False
            self.num.configure(text=f'Your first number = {numbers}')
            operatorDef = '+'
        elif operator == '-':
            Num1 = False
            self.num.configure(text=f'Your first number = {numbers}')
            operatorDef = '-'
            

    def addNum(self,number):
        global numbers
        global numbers2
        global Num1
        global operatorDef
        global resultTrue

        if Num1 == True:
            numbers = numbers + number
            self.label.configure(text=f'{numbers}')
        else:
            numbers2 = numbers2 + number
            self.label.configure(text=f'{numbers2}')

    def stackSum(self):
        global numbers2
        global numbers
        global operatorDef
        numbers2 = ''
        operatorDef = ''
        self.label.configure(text=f'{numbers}')
        self.num.configure(text=f'Your first number = {numbers}')

    def clear(self):
        global numbers
        global numbers2
        global operatorDef
        global Num1
        Num1 = True
        numbers = ''
        numbers2 = ''
        operatorDef = ''
        self.label.configure(text='')
        self.error.configure(text='')
        self.num.configure(text=f'Your first number = {numbers}')
        
    def Cal(self):
        global numbers
        global numbers2
        global Num1
        global operatorDef
        global resultTrue
        if operatorDef == 'X':
            try:
                numbers = int(numbers) * int(numbers2)
                resultTrue = True
            except ValueError:
                self.error.configure(text='Value error press A/C')
        elif operatorDef == '/':
            try:
                numbers = int(numbers) / int(numbers2)
                resultTrue = True
            except ValueError:
                self.error.configure(text='Value error press A/C')
        elif operatorDef == '+':
            try:
                numbers = int(numbers) + int(numbers2)
                resultTrue = True
            except ValueError:
                self.error.configure(text='Value error press A/C')
        elif operatorDef == '-':
            try:
                numbers = int(numbers) - int(numbers2)
                resultTrue = True
            except ValueError:
                self.error.configure(text='Value error press A/C')
        self.label.configure(text=f'{numbers}')
        self.stackSum()

if __name__ == '__main__':
    gui = CalGUI()
    gui.root.mainloop()