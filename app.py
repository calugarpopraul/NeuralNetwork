from tkinter import *
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NeuralNetwork:

    def __init__(self, master):
        self.inputs = []
        self.weights = []
        self.neuron = 0.000
        # self.neurons = []
        self.inputsSb = []
        self.weightsSp = []
        self.neuronsLabel = []
        self.operationsMenu = [
            'sum',
            'product',
        ]
        self.operationNeuron = StringVar()
        self.activationFunctions = [
            'Binary Step',
            'Linear',
            'Sigmoid',
            'Tanh',
            'Softmax'
        ]
        self.functionsMenu = StringVar()
        self.selectedFunction = StringVar()
        self.neuronValue = StringVar()

        self.f = Frame(master, width=700, height=700)
        self.f.pack()

        # inputs label and spinbox
        self.labelInputs = Label(self.f, text="Inputs")
        self.labelInputs.grid(row=0, column=0)
        self.spinboxInputs = Spinbox(self.f, from_=1, to=10, width=5)
        self.spinboxInputs.grid(row=1, column=0)

        self.createSpinboxList = Button(
            self.f, text="Generate Neural Network", 
            command=self.generateInputs
            )
        self.createSpinboxList.grid(row=2, column=0)

        self.selectedFunction.set(self.activationFunctions[0])
        self.functionsMenu = OptionMenu(
            self.f,
            self.selectedFunction,
            *self.activationFunctions
        )
        self.functionsMenu.grid(row=1, column=2)

        self.operationNeuron.set(self.operationsMenu[0])
        self.operationsMenu = OptionMenu(
            self.f,
            self.operationNeuron,
            *self.operationsMenu
        )
        self.operationsMenu.grid(row=1, column=4)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))
    
    def binarystep(self, x):
        return 1 if x > 0.5 else 0

    def sigma(self, x):
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        return np.sinh(x)/np.cosh(x)

    def showgraph(self, functions):
        X = np.linspace(-5, 5, 100)
        plt.plot(X, self.sigma(X),'b')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        plt.title('Sigmoid Function')
        plt.grid()
        plt.text(4, 0.8, r'$\sigma(x)=\frac{1}{1+e^{-x}}$', fontsize=16)
        plt.show()
    
    def sum(self):
        self.updateSpinBoxes()
        function = str(self.selectedFunction.get()).lower().replace(' ', '')
        operation = str(self.operationNeuron.get())
        print("operation: {}".format(operation))

        if function == "sigmoid":
            print("in {}".format(function))
            for idx, element in enumerate(self.weights):
                x = 0
                x += (self.inputs[idx] * self.weights[idx])
                self.neuron = self.sigmoid(x)
            for idx, element in enumerate(self.neuronsLabel):
                    element["text"] = str(self.neuron)


        if function == 'binarystep':
            print("in {}".format(function))
            for idx, element in enumerate(self.weights):
                x = 0
                x += (self.inputs[idx] * self.weights[idx])
                self.neuron = self.binarystep(x)
            for idx, element in enumerate(self.neuronsLabel):
                element["text"] = str(self.neuron)
            
        if function == 'tanh':
            print("in {}".format(function))
            for idx, element in enumerate(self.weights):
                x = 0
                x += (self.inputs[idx] * self.weights[idx])
                self.neuron = self.tanh(x)
            for idx, element in enumerate(self.neuronsLabel):
                element["text"] = str(self.neuron)
            
    def updateSpinBoxes(self):

        for idx, element in enumerate(self.inputsSb):
            self.inputs[idx] = float(element.get())
        print(self.inputs)
        for idx, element in enumerate(self.weightsSp):
            self.weights[idx] = float(element.get())
        print(self.weights)

    def generateInputs(self):
        xSi = 20
        ySi = 80

        xWs = 140
        yWs = 80

        xLw = 280
        yLw = 85
        
        nrOfInputs = int(self.spinboxInputs.get())
        self.inputs = [0.000] * nrOfInputs
        self.weights = [0.000] * nrOfInputs
        # self.neurons = [0.000] * nrOfInputs

        labelWb = 'labelNeuron'
        labelWb = Label(
                text = "{}".format(self.neuron),
            )
        labelWb.place(x=xLw, y=yLw)
        self.neuronsLabel.append(labelWb)

        for i in range(nrOfInputs):
            curSb = 'inputSpinbox' + str(i) 
            curWb = 'weightSpinbox'+ str(i)

            curSb = Spinbox(
                from_=0.000, 
                to=1.0, 
                increment=0.001,
                width=10,
                )

            curWb = Spinbox(
                from_=0.000, 
                to=1.0, 
                increment=0.001,
                width=10,
            )

            curSb.place(x=xSi, y=ySi)
            curWb.place(x=xWs, y=yWs)

            ySi+=40
            yWs+=40
            # yLw+=40

            self.inputsSb.append(curSb)
            self.weightsSp.append(curWb)
        
        self.createCalculateInputsButton = Button(
            self.f, 
            text="Calculate",
            command=self.sum
            )            
        self.createCalculateInputsButton.grid(row=2, column=2)


root = Tk()
root.geometry('600x600')
nn = NeuralNetwork(root)
root.mainloop()