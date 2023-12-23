import random
import math
from statistics import NormalDist
from copy import copy


WordMap = {
    "EE": ["Talkative", "Extraverted", "Aggressive"],
    "EA": ["Sociable", "Enthusiastic", "Communicative"],
    "EC": ["Active", "Competitive", "Persistenc"],
    "ES": ["Confident", "Bold", "Assured"],
    "EO": ["Expressive", "Adventurous", "Dramatic"],
    "AE": ["Sympathetic", "Kind", "Warm"],
    "AA": ["Merry", "Cheerful", "Happy"],
    "AC": ["Helpful", "Cooperative", "Considerate"],
    "AS": ["Trustful", "Pleasant", "Tolerant"],
    "AO": ["Genial", "Tactful"],
    "CE": ["Alert", "Ambitious", "Firm"],
    "CA": ["Responsible", "Dependable", "Reliable"],
    "CC": ["Organized", "Neat", "Orderly"],
    "CS": ["Unenvious"],
    "CO": ["Industrious", "Perfectionist", "Sophisticated"],
    "SE": ["Unselfconscious", "Weariless", "Indefatigable"],
    "SA": ["Patient", "Relaxed", "Undemanding"],
    "SC": ["Determined", "Unswerving"],
    "SS": ["Unenvious"],
    "SO": ["Adaptable", "Multitalented"],
    "OE": ["Theatrical", "Worldly", "Eloquent"],
    "OA": ["Deep", "Diplomatic", "Idealistic"],
    "OC": ["Analytical", "Perceptive", "Informative"],
    "OS": ["Intellectual", "Inventive", "Intelligent"],
    "OO": ["Creative", "Philisophical", "Imaginative"],

    "E-E": [],
    "E-A": ["Dominant", "Forceful", "Domineering"],
    "E-C": ["Boistrous", "Exhibitionist", "Mischievous"],
    "E-S": ["Flirtatious", "Wordy", "Explosive"],
    "E-O": ["Verbose"],
    "A-E": ["Soft-Hearted", "Agreeable", "Obliging"],
    "A-A": [],
    "A-C": ["Lenient", "Compassionate", "Sheepish"],
    "A-S": ["Affectionate", "Sentimental", "Sensitive"],
    "A-O": ["Conforming"],
    "C-E": ["Careful", "Cautious", "Punctual"],
    "C-A": ["Stern", "Strict", "Deliberate"],
    "C-C": [],
    "C-S": ["Exacting", "Arduous"],
    "C-O": ["Conventional", "Traditional"],
    "S-E": ["Unexcitable", "Unassuming"],
    "S-A": ["Unemotional", "Masculine"],
    "S-C": ["Informal", "Casual"],
    "S-S": [],
    "S-O": ["Imperturbable", "Unconcerned"],
    "O-E": ["Introspective", "Meditative", "Contemplative"],
    "O-A": ["Individualistic", "Eccentric"],
    "O-C": ["Improvisational", "Versatile"],
    "O-S": ["Sensual"],
    "O-O": [],

    "-EE": [],
    "-EA": ["Timid", "Submissive", "Unaggressive"],
    "-EC": ["Reserved", "Serious", "Restrained"],
    "-ES": ["Tranquil", "Placid", "Sedate"],
    "-EO": ["Inner-Directed"],
    "-AE": ["Rough", "Abrupt", "Crude"],
    "-AA": [],
    "-AC": ["Rigid", "Hard"],
    "-AS": ["Insensitive", "Passionless", "Unaffectionate"],
    "-AO": ["Shrewd", "Sharp-Witted"],
    "-CE": ["Reckless", "Unruly", "Devil-May-Care"],
    "-CA": ["Permissive", "Enabling"],
    "-CC": [],
    "-CS": ["Complacent", "Unbothered"],
    "-CO": ["Unconventional", "Slapdash"],
    "-SE": ["High-Strung"],
    "-SA": ["Emotional", "Gullible"],
    "-SC": ["Particular", "Intrusive"],
    "-SS": [],
    "-SO": ["Paranoid", "Weird", "Histrionic"],
    "-OE": ["Unscrupulous", "Pompous"],
    "-OA": ["Simple", "Servile", "Dependent"],
    "-OC": ["Muleheaded", "Obstinate", "Infuriating"],
    "-OS": ["Unreflective", "Imperceptible", "Unsophisticated"],
    "-OO": [],

    "-E-E": ["Shy", "Quiet", "Introverted"],
    "-E-A": ["Unsociable", "Seclusive", "Uncommunicative"],
    "-E-C": ["Unenergetic", "Sluggish", "Uncompetitive"],
    "-E-S": ["Lonely", "Weak-Willed", "Cowardly"],
    "-E-O": ["Passive", "Meek", "Dull"],
    "-A-E": ["Cold", "Unfriendly", "Impersonal"],
    "-A-A": ["Unsympathetic", "Unkind", "Harsh"],
    "-A-C": ["Impolite", "Rude", "Inconsiderate"],
    "-A-S": ["Demanding", "Selfish", "Ill-Tempered"],
    "-A-O": ["Ruthless", "Coarse", "Uncharitable"],
    "-C-E": ["Inefficient", "Lazy", "Indecisive"],
    "-C-A": ["Unreliable", "Negligent", "Undependable"],
    "-C-C": ["Disorderly", "Careless", "Disorganized"],
    "-C-S": ["Inconsistant", "Unstable", "Scatterbrained"],
    "-C-O": ["Illogical", "Immature", "Haphazard"],
    "-S-E": ["Self-Pitying", "Insecure","Fretful"],
    "-S-A": ["Irritable", "Defensive", "Tempermental"],
    "-S-C": ["Hypocritical", "Nosey", "Compulsive"],
    "-S-S": ["Moody", "Jealous", "Possessive"],
    "-S-O": ["Contemptuous"],
    "-O-E": ["Unimaginative", "Inarticulate", "Uninquisitive"],
    "-O-A": ["Shallow", "Terse"],
    "-O-C": ["Unobservant", "Ignorant", "Short-Sighted"],
    "-O-S": ["Controlling"],
    "-O-O": ["Uncreative", "Unintellectual", "Unintelligent"],
}




mean = 0
dev = 1

traits = {"E": 0, "A": 0, "C": 0, "S" : 0, "O": 0}

for key in traits:
    value =random.normalvariate(mean, dev)
    perc = NormalDist().cdf(value)
    traits[key] = int((perc * 2 - 1) * 100)


#print (traits)

traits = dict(sorted(traits.items(), key=lambda item: -abs(item[1])))

print(traits)

traitNames = []
traitPairs = {}

for key in traits:
    name = key
    if traits[key] < 0:
        name = "-" + key
    traitNames.append(name)

total = 0

for i in range(len(traitNames)):
    trait1 = traitNames[i]
    t1 = trait1
    if len(t1) == 2:
            t1 = t1[1]

    for j in range(i, len(traitNames)):
        trait2 = traitNames[j]
        t2 = trait2
        if len(t2) == 2:
            t2 = t2[1]

        val1 = traits[t1]
        val2 = traits[t2]
        weight = abs(val1*val1*val1) + abs(val2*val2*val2)
        total += weight
        traitPairs[trait1 + trait2] = weight

traitPairs = dict(sorted(traitPairs.items(), key=lambda item: -item[1]))

traitPairPercentages = copy(traitPairs)

sum = 0
for t in traitPairPercentages:
    value = round(traitPairPercentages[t] * 100 / total, 1)
    traitPairPercentages[t] = value
    sum += value

#print(traitPairs)
print(traitPairPercentages)

rangeAdjust = 0

primary = random.randrange(0,100)
primaryTrait = ""
primaryCount = 0
for k in traitPairPercentages:
    #print(k + ": " + str(WordMap[k]))
    pass

for key in traitPairPercentages:
    primaryCount += 1
    primary -= traitPairPercentages[key]
    primaryTrait = key
    if primary <= 0:
        break

rangeAdjust += int(traitPairPercentages[primaryTrait])
traitPairPercentages.pop(primaryTrait)
primaryDesc = random.choice(WordMap[primaryTrait])

secondary = random.randrange(0,100-rangeAdjust)
secondaryTrait = ""
secondaryCount = 0
for key in traitPairPercentages:
    secondaryCount += 1
    secondary -= traitPairPercentages[key]
    secondaryTrait = key
    if secondary <= 0:
        break
rangeAdjust += int(traitPairPercentages[secondaryTrait])
traitPairPercentages.pop(secondaryTrait)
secondaryDesc = random.choice(WordMap[secondaryTrait])

tertiary = random.randrange(0,100-rangeAdjust)
tertiaryTrait = ""
tertiaryCount = 0
for key in traitPairPercentages:
    tertiaryCount += 1
    tertiary -= traitPairPercentages[key]
    tertiaryTrait = key
    if tertiary <= 0:
        break
rangeAdjust += traitPairPercentages[tertiaryTrait]
tertiaryDesc = random.choice(WordMap[tertiaryTrait])


print(str(primaryCount) + ") " + primaryTrait + ": " + primaryDesc)
print(str(secondaryCount) + ") " + secondaryTrait + ": " + secondaryDesc)
print(str(tertiaryCount) + ") " + tertiaryTrait + ": " + tertiaryDesc)
#generate 5 values


#enneagram correlation

'''
type1 .e, .a, ++c, +s, -o
type2 ++e, _h, .c, .s, -o
type3 ++e, -a, ++c, .s, .o
type4 -e, .a, -c, --s, +o
type5 --e, --a, .c, .s, .o
type6 --e, +a, .c, --s, -o
'''