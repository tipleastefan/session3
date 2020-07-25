# split string

string = "abcdefghi"


def SplitString(string):
    list = []
    for i in range(1, len(string), 2):
        var = string[i - 1] + string[i]
        list.append(var)
    if len(string) % 2 != 0:
        var = string[len(string) - 1] + " "
        list.append(var)
    return list


print(SplitString(string))

# reverse word

string = "acesta este un exemplu"


def ReverseWord(string):
    list = []
    word = ""
    for i in range(len(string)):
        if string[i] != " ":
            word += string[i]
        elif string[i] == " ":
            list.append(word)
            word = ""
    if string[len(string) - 1] != "":
        list.append(word)
    reverse = []
    for i in list:
        reverse.append(i[::-1])
    return reverse


print(ReverseWord(string))


# Man woman class

class Human:
    def __init__(self, name="unnamed"):
        self.name = name

    def setName(self, name):
        self.name = name


class Man(Human):
    def __init__(self):
        Human.__init__(self)
        self.gender = "Male"

    def __str__(self):
        return self.name + " is a " + self.gender


class Woman(Human):
    def __init__(self):
        Human.__init__(self)
        self.gender = "Female"

    def __str__(self):
        return self.name + " is a " + self.gender


def Creation(array):
    p1 = Man()
    p1.setName("Adam")
    array.append(p1)
    p2 = Woman()
    p2.setName("Eva")
    array.append(p2)
    for i in array:
        print(i)
    return array


array = []
print(Creation(array))
