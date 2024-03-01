"""2.	Write a Python GUI program using breezypythongui library, to demonstrate text fields. Convert the given text to upper case."""
from breezypythongui import EasyFrame
class TextFieldDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Text Field Demo",resizable=False)
        self.addLabel(text = "Enter a string", row = 0, column = 0)
        self.inputField = self.addTextField(text = "",row = 0,column = 1)
 # Label and field for the output
        self.addLabel(text = "String in uppercase", row = 1, column = 0)
        self.outputField = self.addTextField(text = "",row =  1,column = 1,state = "readonly")
 # The command button
        self.addButton(text = "Convert", row = 2, column = 0, rowspan = 2,columnspan=2, command = self.convert)
 # The event handling method for the button
    def convert(self):
        textdata = self.inputField.getText()
        result = textdata.upper()
        self.outputField.setText(result)
def main():
    """Instantiates and pops up the window."""
    TextFieldDemo().mainloop()
if __name__ == "__main__":
    main()
