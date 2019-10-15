from tkinter import *
import numpy as np


class NeuralNetwork:

    def __init__(self, master):
        self.inputs = []
        self.weights = []
        self.neurons = []
        self.inputsSb = []
        self.weightsSp = []
        self.neuronsLabel = []

        self.f = Frame(master, width=700, height=700)
        self.f.pack()

        # inputs label and spinbox
        self.labelInputs = Label(self.f, text="Inputs")
        self.labelInputs.grid(row=0, column=0)
        self.spinboxInputs = Spinbox(self.f, from_=0, to=10, width=5)
        self.spinboxInputs.grid(row=1, column=0)

        # self.labelHl = Label(self.f, text="Hidden Layers")
        # self.labelHl.grid(row=0, column=1)
        # self.spinboxHl = Spinbox(self.f, from_=0, to=10, width=5)
        # self.spinboxHl.grid(row=1, column=1)

        # self.labelNeurons = Label(self.f, text="Neurons")
        # self.labelNeurons.grid(row=0, column=2)
        # self.spinboxNeurons = Spinbox(self.f, from_=0, to=10, width=5)
        # self.spinboxNeurons.grid(row=1, column=2)


        self.createSpinboxList = Button(
            self.f, text="Generate Neural Network", 
            command=self.generateInputs
            )
        self.createSpinboxList.grid(row=2, column=0)

    
    def sum(self):
        self.updateSpinBoxes()
        for idx, element in enumerate(self.weights):
            self.neurons[idx] += (self.inputs[idx] * self.weights[idx])
        for idx, element in enumerate(self.neuronsLabel):
            element.text(self.neurons[idx])

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
        self.neurons = [0.000] * nrOfInputs

        print(self.neurons)
        # nrOfHl = int(self.spinboxHl.get())
        # nrOfNeurons = int(self.spinboxNeurons.get())

        for i in range(nrOfInputs):
            curSb = 'inputSpinbox' + str(i) 
            curWb = 'weightSpinbox'+ str(i)
            labelWb = 'labelNeuron' + str(i)

            curSb = Spinbox(
                from_=0.001, 
                to=10.000, 
                increment=0.001,
                width=10,
                )

            curWb = Spinbox(
                from_=0.001, 
                to=10.000, 
                increment=0.001,
                width=10,
            )
            labelWb = Label(
                text = "{}".format(self.neurons[i])
            )

            curSb.place(x=xSi, y=ySi)
            curWb.place(x=xWs, y=yWs)
            labelWb.place(x=xLw, y=yLw)

            ySi+=40
            yWs+=40
            yLw+=40

            self.inputsSb.append(curSb)
            self.weightsSp.append(curWb)
            self.neuronsLabel.append(labelWb)
        
        self.createCalculateInputsButton = Button(
            self.f, 
            text="Calculate",
            command=self.sum
            )            
        self.createCalculateInputsButton.grid(row=2, column=2)


        # self.neurons = np.zeros(nrOfNeurons)
        # for i in range(nrOfNeurons):
            # curWb = 'weightSpinbox'+ str(i)
            # labelWb = 'labelNeuron' + str(i)
            # curWb = Spinbox(
            #     from_=0.001, 
            #     to=10.000, 
            #     increment=0.001,
            #     width=10,
            # )
            # labelWb = Label(
            #     self.f,
            #     text="neuron"
            # )
            # curWb.place(x=xWs, y=yWs)
            # labelWb.place(x=180, y=yWs)

            # yWs+=40
            # self.weights.append(curWb)
            # self.labelNeurons.append(labelWb)




        


root = Tk()
root.geometry('500x500')
nn = NeuralNetwork(root)
root.mainloop()