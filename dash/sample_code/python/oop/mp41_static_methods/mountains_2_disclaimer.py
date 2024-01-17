class Mountain:

    def __init__(self, name="", elev_meters=0):
        self.name = name
        self.elev_meters = elev_meters

    def describe_mountain(self):
        msg = f"{self.name} is {self.elev_meters:,} meters tall."
        print(msg)

    def show_disclaimer(self):
        msg = "\nClimbing steep mountains can be dangerous."
        msg += " If you are new to climbing,"
        msg += " please seek out instruction from"
        msg += " a qualified guide or an"
        msg += " experienced mentor."
        print(msg)


my_mountain = Mountain("Mt. Verstovia", 1022)
my_mountain.describe_mountain()

my_mountain.show_disclaimer()
