import random
#Rule
class Rule:
    ruleSet = []
    ruleFile = None
    
    def __init__(self):
        self.readRulesFromFile()

    def createDefaultList(self):
        w, h = 6, 6
        result = [[0 for x in range(w)] for y in range (h)]

        result[0][0] = "self;ex"
        result[1][0] = "self;2"
        result[2][0] = "self;3"
        result[3][0] = "self;4"
        result[4][0] = "self;5"
        result[5][0] = "self;6"

        result[0][1] = "self;1"
        result[1][1] = "other;2"
        result[2][1] = "self;3"
        result[3][1] = "self;4"
        result[4][1] = "self;5"
        result[5][1] = "self;6"

        result[0][2] = "self;1"
        result[1][2] = "self;2"
        result[2][2] = "other;3"
        result[3][2] = "self;4"
        result[4][2] = "self;5"
        result[5][2] = "self;6"

        result[0][3] = "self;1"
        result[1][3] = "self;2"
        result[2][3] = "self;3"
        result[3][3] = "other;4"
        result[4][3] = "self;5"
        result[5][3] = "self;6"

        result[0][4] = "self;1"
        result[1][4] = "self;2"
        result[2][4] = "self;3"
        result[3][4] = "self;4"
        result[4][4] = "other;5"
        result[5][4] = "self;6"

        result[0][5] = "self;1"
        result[1][5] = "self;2"
        result[2][5] = "self;3"
        result[3][5] = "self;4"
        result[4][5] = "self;5"
        result[5][5] = "other;ex"

        return result

    def stringToList(self, text):
        index = len(text)
        w, h = index, index
        result = [[0 for x in range(w)] for y in range (h)]
        for rule in text:
            result[rule[0]-1][rule[2]-1] = text[text.index(" "):]
        return result 

    def readRulesFromFile(self):
        self.ruleFile = open("rule.conf","a+")
        textInput = self.ruleFile.readlines()
        if not textInput:
            self.ruleSet = self.createDefaultList()
        else:
            self.ruleSet = self.stringToList(textInput)
        self.ruleFile.close()

    def ruleSetToString(self):
        textInput = ""
        index1 = 0
        index2 = 0
        for x in self.ruleSet:
            for y in x:
                textInput += str(index1) + ":" + str(index2) + " " + y + "\n"
                index2 += 1
            index2 = 0
            index1 += 1
        return textInput

    def saveRulesAsFile(self):
        self.ruleFile = open("rule.conf","w+")
        if self.ruleSet:
            textInput = self.ruleSetToString()
            self.ruleFile.write(textInput)
        self.ruleFile.close()

    def getRuleSet(self):
        return self.ruleSet