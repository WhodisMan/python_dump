class animal:
    def perform(self):
        print(" Animals performing ")


class human:
    def perform(self):
        print(" Humans performing ")


class circus:
    def play(self, test):
        test.perform()


tiger = animal()
anu = human()
c = circus()

c.play(tiger)
c.play(anu)

print("-------------")
