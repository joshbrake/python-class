#!/usr/bin/python

import Tkinter

class tipCalculator(Tkinter.Tk):
  def __init__(self,parent):
    Tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.grid()

    # Meal subtotal label
    self.subtotalLabel = Tkinter.Label(self,text='Subtotal ($)',anchor='c',fg='black')
    self.subtotalLabel.grid(column=0,row=0,sticky='EW')

    # Meal subtotal entry box
    self.subtotalEntryVariable = Tkinter.DoubleVar()
    self.subtotalEntry = Tkinter.Entry(self,textvariable=self.subtotalEntryVariable)
    self.subtotalEntry.grid(column=1,row=0,sticky='EW')
    self.subtotalEntryVariable.set('0.00')
    #self.subtotalEntry.selection_range(0,Tkinter.END)

    # Tip percentage label
    self.tipPercentageLabel = Tkinter.Label(self,text='Tip Percentage',anchor='c',fg='black')
    self.tipPercentageLabel.grid(column=0,row=1,sticky='EW')

    # Tip percentage entry box
    #self.tipEntryVariable = Tkinter.DoubleVar()
    #self.tipEntry = Tkinter.Entry(self,textvariable=self.tipEntryVariable)
    #self.tipEntry.grid(column=1,row=1,sticky='EW')
    #self.tipEntryVariable.set('%')
    #self.tipEntry.selection_range(0,Tkinter.END)

    # Tip dropdown menu
    self.tipDropdownVariable = Tkinter.StringVar()
    self.tipDropdown = Tkinter.OptionMenu(self,self.tipDropdownVariable,'15%','18%','20%')
    self.tipDropdown.grid(column=1,row=1,sticky='EW')    
    self.tipDropdownVariable.set('Select a value')

    # Calculated tip label
    self.tipLabelVariable = Tkinter.StringVar()
    self.tipLabel = Tkinter.Label(self,textvariable=self.tipLabelVariable,anchor='c',fg='black')
    self.tipLabel.grid(column=0,row=2,columnspan=2,sticky='EW')
    self.tipLabelVariable.set('Tip: ?')

    # Calculated total
    self.totalLabelVariable = Tkinter.StringVar()
    self.totalLabel = Tkinter.Label(self,textvariable=self.totalLabelVariable,anchor='c',fg='black')
    self.totalLabel.grid(column=0,row=3,columnspan=2,sticky='EW')
    self.totalLabelVariable.set('Total: ?')

    # Calculate tip button
    self.button = Tkinter.Button(self,text="Calculate",command=self.calculate)
    self.button.grid(column=0,row=4,columnspan=2)
    
    # Set resizing
    self.grid_columnconfigure((0,1),weight=1)

  def calculate(self):
    self.tipPercentage = self.tipDropdownVariable.get()
    self.tipPercentage = float(self.tipPercentage[0:2])   
    self.subtotal = self.subtotalEntryVariable.get()
    self.tipAmount = self.tipPercentage/100*self.subtotal
    self.totalAmount = self.subtotal+self.tipAmount
    self.tipLabelVariable.set('Tip: $%0.2f' % self.tipAmount)
    self.totalLabelVariable.set('Total: $%0.2f' % self.totalAmount)

if __name__=="__main__":
  app = tipCalculator(None)
  app.title('Tip Calculator')
  app.mainloop()