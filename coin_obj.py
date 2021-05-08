# Data Type - Coin
class Coin():
    # Constructor - This will initialize a new coin object
    def __init__(self, row, col, colour):
        self.r = row
        self.c = col
        self.clr = colour

    # This method will allow you to see the attributes associated with the coin object
    def __str__(self):
        row = "Row: " + str(self.r)
        col = "Col: " + str(self.c)
        colour = "Colour: " + str(self.clr)

        return row + "\t" + col + "\t" + colour