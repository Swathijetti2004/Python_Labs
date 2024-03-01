"""1.	Write a Python GUI program using breezypythongui library, to demonstrate command button events. To clear and restore a message using
two command buttons called clear and restore."""
from breezypythongui import EasyFrame
class ButtonDemo(EasyFrame):
    def __init__(self):
         EasyFrame.__init__(self)
         self.setTitle("Button")
         self.label = self.addLabel(text = "Hello world!",row = 0, column = 0,columnspan = 2,sticky = "NSEW")
         self.clearBtn = self.addButton(text = "Clear",row = 1, column = 0,command = self.clear)
         self.restoreBtn = self.addButton(text = "Restore",row = 1, column = 1,state = "disabled",command = self.restore)
    def clear(self):
         self.label["text"] = ""
         self.clearBtn["state"] = "disabled"
         self.restoreBtn["state"] = "normal"
    def restore(self):
         self.label["text"] = "Hello world!"
         self.clearBtn["state"] = "normal"
         self.restoreBtn["state"] = "disabled"
def main():
         ButtonDemo().mainloop()
if __name__ == "__main__":
    main()