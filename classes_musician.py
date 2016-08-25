class Musician(object):
    def __init__(self, sounds):
        """
        Creates sounds the musician makes.
        """
        self.sounds = sounds

    def solo(self, length):
        """
        Creates the counts of how long the musician plays its solo.
        """
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        """
        Call the __init__ method of the parent class.
        """
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        """
        Call the __init__ method of the parent class.
        """
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        """
        States what the guitarist says and the noises made when tuning.
        """
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        """
        Call the __init__ method of the parent class
        """
        super().__init__(["Tss", "Chick", "Chucka", "Doom", "Daa", "Ba-Da"])

    def count(self):
        """
        States what the drummer says before the band rocks out
        """
        print("Here we go...")
        print("1 - 2 - 3 - 4")

    def combustion(self):
        """
        Call the solo method of the parent class to create a special long solo for the drummer
        """
        super().solo(18)

class Band():
    def __init__(self):
        """
        Creates a dictionary to add band members to.
        """
        self.group = {}

    def hire(self, musician, name):
        """
        Adds a new musician to the the band dictionary with their name and the instrument played.
        """
        self.group[name] = musician

    def fire(self, name):
        """
        Deletes a member from the band.
        """
        del self.group[name]

    def play(self, drummer_name):
        """
        Has the drummer start off performance with the count function.
        Then each musician in the band plays a quick solo.
        Lastly, the drummer has an extra long solo.

        If the drummer_name doesn't correspond with the name given, an error message will appear.
        """
        try:
            rockers.group[drummer_name].count()
            for name, musician in self.group.items():
                musician.solo(6)
            rockers.group[drummer_name].combustion()
        except KeyError:
            print("We have a different drummer adjusting to the band. Give us a moment.")

drummer = Drummer()
guitarist = Guitarist()
bassist = Bassist()

rockers = Band()
rockers.hire(drummer, "mike")
rockers.hire(guitarist, "nigel")
rockers.hire(bassist, "david")
print(rockers.group)

rockers.play("mike")

rockers.fire("nigel")
print(rockers.group)