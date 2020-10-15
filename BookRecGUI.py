import BookSuggestion 
from breezypythongui import EasyFrame

class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Book Recommendations")

        self.btnFriends = self.addButton(text="Friends", row = 0, column = 0, command = self.getFriends())

    def getFriends(self):
        name = self.prompterBox("Friends", "Enter Reader Name")


def main():
    BookRecsGui().mainloop()

if __name__ == "__main__":
    main()

