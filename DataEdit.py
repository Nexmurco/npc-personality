from copy import copy

class Facet:
    def __init__(self, name):
        self.name = name
    
    value = 0

class Trait:
    def __init__(self, name):
        self.name = name
    name = ""
    value = 0
    facets = []

class Personality:
    def __init__(self):
        pass

    traits = [Trait("Neuroticism"), Trait("Extraversion"),  Trait("Openness"), Trait("Acceptance"), Trait("Concientiousness")]

    traits[2].facets = [Facet("Imagination"), Facet("Artistic-Interest"), Facet("Emotionality"), Facet("Adventurousness"), Facet("Intellect"), Facet("Liberalism")]

    traits[3].facets = [Facet("Trust"),Facet("Morality"),Facet("Altruism"),Facet("Cooperation"),Facet("Modesty"),Facet("Sympathy")]

    traits[0].facets = [Facet("Anxiety"), Facet("Anger"), Facet("Depression"), Facet("Self-Conciousness"), Facet("Immoderation"), Facet("Vulneability")]

    traits[1].facets = [Facet("Friendliness"), Facet("Gregariousness"), Facet("Assertiveness"), Facet("Activity-Level"), Facet("Excitement-Seeking"), Facet("Cheerfulness")]

    traits[4].facets = [Facet("Self-Efficacy"), Facet("Orderliness"), Facet("Dutifulness"), Facet("Achievement-Striving"), Facet("Self-Discipline"), Facet("Cautiousness")]

    def clear(self):
        for t in self.traits:
            t.value = 0
            for f in t.facets:
                f.value = 0


def isReversedWeight(id):
    if id>=148 and id <= 152:
        return True
    if id>=156 and id <= 160:
        return True
    if id>=162 and id <= 165:
        return True
    if id>=167 and id <= 169:
        return True
    if id>=173 and id <= 176:
        return True
    if id>=178 and id <= 190:
        return True
    if id>=192 and id <= 199:
        return True
    if id>=203 and id <= 206:
        return True
    if id>=208 and id <= 231:
        return True
    if id>=233 and id <= 236:
        return True
    if id>=238 and id <= 300:
        return True

    if id==69:
        return True
    if id==99:
        return True
    if id==109:
        return True
    if id==118:
        return True
    if id==120:
        return True
    if id==129:
        return True
    if id==138:
        return True
    if id==139:
        return True
    if id==144:
        return True
    if id==171:
        return True
    if id==201:
        return True
    

    return False


def addScore(scores, id, value):
    value = int(value)
    if isReversedWeight(id):
        value = 6-value


    traitValue = int(id%5)

    facetValue = int(id/5)
    facetValue = int(facetValue%6)

    scores.traits[traitValue].facets[facetValue].value += value
    scores.traits[traitValue].value += value




with open('IPIP300.txt', 'r') as file:
    data = file.readlines()

scoreData = copy(data)
scoreMainData = copy(data)
#make changes
counter = 0
percentCounter = 0
scores = Personality()
for line in data:

    scores.clear()

    #ID
    dataString = line[:6] + ","
    scoreString = line[:6] + ","
    scoreMainString = line[:6] + ","
    #SEX
    dataString += line[6] + ","
    scoreString += line[6] + ","
    scoreMainString += line[6] + ","
    #AGE
    dataString += line[7:9]  + ","
    scoreString += line[7:9] + ","
    scoreMainString += line[7:9] + ","
    #COUNTRY
    dataString += line[22:33]
    scoreString += line[22:33]
    scoreMainString += line[22:33]

    #ANSWERS
    for i in range(34,333):
        question = i - 33

        value = line[i:i+1]
        addScore(scores, question, value)
        dataString += "," + value


    #neoac
    for trait in scores.traits:
        scoreString += "," + str(trait.value)
        scoreMainString += "," + str(trait.value)

    
    for trait in scores.traits: 
        for facet in trait.facets:
            scoreString += "," + str(facet.value)

    scoreString += "\n"
    dataString += "\n"
    scoreMainString += "\n"

    data[counter] = dataString
    scoreData[counter] = scoreString
    scoreMainData[counter] = scoreMainString


    counter += 1
    if counter % 3073 == 0:

        percentCounter += 1
        print(str(percentCounter) + "%")

with open('scoresMain.txt', 'w') as file:
    file.writelines(scoreMainData)

with open('scores.txt', 'w') as file:
    file.writelines(scoreData)

with open('test.txt', 'w') as file:
    file.writelines(data)
