import BookSuggestion 
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
        if name in BookSuggestion.ratings.keys():
            friends = BookSuggestion.friends(name)
            self.messageBox("Friends of " + name, friends[0] +'\n'+friends[1])
        else:
            self.messageBox("Error", "No such reader.")
        

    def recommendations(self):
        name = self.prompterBox("Recommendations", "Enter Reader Name:")
        if name in BookSuggestion.ratings.keys():
            top2 = BookSuggestion.friends(name)
            recommends = BookSuggestion.recommend(name,top2)
            brStr = ""
            for book in recommends:
                brStr += book[0] +", " + book[1] +"\n"
            self.messageBox("Recommendations for " + name, brStr, width = 100, height= 50)
        else:
           self.messageBox("Error", "No such reader.") 
    def Report(self):
        
        self.messageBox("Report", BookSuggestion.report(), width = 100, height= 50)
    
    

def main():
    BookRecsGui().mainloop()

if __name__ == "__main__":
    main()

