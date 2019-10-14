from tkinter import *

class NeuralNetwork:

    def __init__(self, master):
        self.inputs = []
        self.weights = []

        f = Frame(master, width=700, height=700)
        f.pack()

        # inputs label and spinbox
        self.labelInputs = Label(f, text="Inputs")
        self.labelInputs.grid(row=0, column=0)
        self.spinboxInputs = Spinbox(f, from_=0, to=10, width=5)
        self.spinboxInputs.grid(row=1, column=0)

        self.createSpinboxList = Button(
            f, text="Generate Neural Network", 
            command=self.generateInputs
            )
        self.createSpinboxList.grid(row=2, column=0)


    def generateInputs(self):
        xSi = 10
        ySi = 80

        xWs = 120
        yWs = 80
        
        nrOfInputs = int(self.spinboxInputs.get())
        for i in range(nrOfInputs):
            curSb = 'inputSpinbox' + str(i) 
            curWb = 'weightSpinbox'+ str(i)
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
                width=10)
            curSb.place(x=xSi, y=ySi)
            curWb.place(x=xWs, y=yWs)
            ySi+=40
            yWs+=40

            self.inputs.append(curSb)
            self.weights.append(curWb)


        


root = Tk()
root.geometry('500x500')
nn = NeuralNetwork(root)
root.mainloop()