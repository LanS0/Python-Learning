data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

class Enigma:

    def __init__(self, data, string, state):
        self.data1 = data
        self.data2 = []
        self.strings = string
        self.state = state
        self.list2 = []
        self.enigma_code = []

    def splitter_strings(self):
        list1 = list(self.strings.split())
        listed2 = []
        for x in range(len(list1)):
            for j in list1[x]:
                listed2.append(j)

        self.list2 = listed2

    def enigma_strings(self):
        dummy1 = self.data1
        dummy2 = []
        the_real_state = 0
        for x in self.state:
            the_real_state += x

        dummy3 = dummy1[0:x]
        dummy4 = dummy1[x:]
        for i in dummy4:
            dummy2.append(i)
        for i in dummy3:
            dummy2.append(i)

        self.data2 = dummy2

    def enigma_breaker(self):
        # UPPER CASE
        self.splitter_strings()

        for x in range(len(self.list2)):
            for y in range(len(self.data1)):
                if self.list2[x].upper() == self.data1[y].upper():
                    print(self.list2[x].upper(), self.data1[y].upper())
                    print(y)

    def enigma_maker(self):
        # UPPER CASE
        self.splitter_strings()
        self.enigma_strings()

        for x in range(len(self.list2)):
            for y in range(len(self.data1)):
                if self.list2[x].upper() == self.data1[y].upper():
                    # print(self.list2[x].upper(), self.data1[y].upper())
                    self.enigma_code.append(self.data2[y].upper())
     
        print(''.join(self.enigma_code))

random_state = [13,5]

to_enigma = "HAI AKU MICHAEL"

enigma = Enigma(data, to_enigma, random_state)
enigma.enigma_maker()