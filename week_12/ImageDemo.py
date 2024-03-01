from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
class ImageDemo(EasyFrame):
    """Displays an image and a caption."""
    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Image Demo")
        self.setSize(500,500)
        imageLabel = self.addLabel(text = "",row = 0, column = 0,sticky = "NSEW")
        textLabel = self.addLabel(text = "Home",row = 1, column = 0,sticky = "NSEW")
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "lappy.gif")
        imageLabel["image"] = self.image
        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 20,slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"
def main():
    """Instantiates and pops up the window."""
    ImageDemo().mainloop()
if __name__ == "__main__":
    main()
