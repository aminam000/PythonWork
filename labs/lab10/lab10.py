class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den

    def __str__(self):
        if self.numerator%self.denominator == 0:
            return self.numerator/self.denominator
        else:
            return str(self.numerator) + '/' + str(self.denominator)
    def scale(self,scaler):
        self.numerator*=3
        self.denominator*=3




class Sentence:
    def __init__(self, sentence):
        self.sentence=sentence
        self.words=sentence.split(" ")
        self.numWords=len(self.words)
        self.Length=len(self.sentence)

    def getsentence(self):
        return self.sentence
    def getWords(self):
        return self.numWords
    def getLength(self):
        return self.Length
    def getnumWords(self):
        return self.numWords
