#This Code was written by Parker Thurston, with help from code that was done in class
import BookSuggestionParkerThurston 
from breezypythongui import EasyFrame

class BookRecsGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Book Recommendations", 
                                width = 220, 
                                height= 100, 
                                background="powder blue",
                                resizable= True)

        self.btnFriends = self.addButton(text="Friends", row = 0, column = 0, command = self.getFriends)
        self.btnRecomm = self.addButton(text="Recommend", row = 0, column = 1, command = self.recommendations)
        self.btnReport = self.addButton(text="Report", row = 0, column = 2, command = self.Report)


    def getFriends(self):
        name = self.prompterBox("Friends", "Enter Reader Name:")
        if name in BookSuggestionParkerThurston.ratings.keys():
            friends = BookSuggestionParkerThurston.friends(name)
            self.messageBox("Friends of " + name, friends[0] +'\n'+friends[1])
        else:
            self.messageBox("Error", "No such reader.")
        

    def recommendations(self):
        name = self.prompterBox("Recommendations", "Enter Reader Name:")
        if name in BookSuggestionParkerThurston.ratings.keys():
            top2 = BookSuggestionParkerThurston.friends(name)
            recommends = BookSuggestionParkerThurston.recommend(name,top2)
            brStr = ""
            for book in recommends:
                brStr += book[0] +", " + book[1] +"\n"
            self.messageBox("Recommendations for " + name, brStr, width = 100, height= 50)
        else:
           self.messageBox("Error", "No such reader.") 
    def Report(self):
        
        self.messageBox("Report", BookSuggestionParkerThurston.report(), width = 100, height= 50)
    
    

def main():
    BookRecsGui().mainloop()

if __name__ == "__main__":
    main()

