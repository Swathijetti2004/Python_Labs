from breezypythongui import EasyFrame
class Itgui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.setTitle("Age Calculator")
        self.addLabel(text="Date", row=0, column=0)
        self.addLabel(text="Month", row=1, column=0)
        self.addLabel(text="Year", row=2, column=0)
        self.t1 = self.addIntegerField(value="", row=0, column=1)
        self.t2 = self.addIntegerField(value="", row=1, column=1)
        self.t3 = self.addIntegerField(value="", row=2, column=1)
        self.addButton(text="Calculate Age!", row=4, column=0, command=self.check)
        self.addLabel(text="The Calculate Age", row=5, column=0)
        self.t4 = self.addIntegerField(value="", row=5, column=1)

    def check(self):
        Date = self.t1.getNumber()
        Month = self.t2.getNumber()
        Year = self.t3.getNumber()
        y=2022
        result=y-int(Year)
        self.t4.setNumber(result)
def main():
    Itgui().mainloop()
if (__name__ == "__main__"):
    main()