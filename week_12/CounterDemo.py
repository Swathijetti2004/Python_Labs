"""4.	Write a Python GUI program using breezypythongui library, to demonstrate instance variable. Implement a counter increment program on
a button event, and reset the counter to 0 when the user presses the reset button."""
from breezypythongui import EasyFrame
class CounterDemo(EasyFrame): 
	def __init__(self): 
		EasyFrame.__init__(self, title = "Counter Demo") 
		self.setSize(200, 200)
		self.count = 0 
		self.label = self.addLabel(text = "0", row = 0, column = 0, sticky = "NSEW", columnspan= 2)
		self.addButton(text = "Next", row = 1, column = 0, command = self.next) 
		self.addButton(text = "Reset", row = 1, column = 1, command = self.reset) 
	def next(self): 
		self.count += 1 
		self.label["text"] = str(self.count) 
	def reset(self): 
		self.count = 0 
		self.label["text"] = str(self.count)
def main():
    CounterDemo().mainloop()
if __name__ == "__main__":
    main()
