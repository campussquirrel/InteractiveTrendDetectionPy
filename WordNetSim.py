from nltk.corpus import wordnet as wn
import math

def get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
        hyponyms |= set(get_hyponyms(hyponym))
    return hyponyms | set(synset.hyponyms())

"""
It takes a set of terms and return the set of their direct/immidiate hyponyms

    :param: termsSet
    :return: immidiateHyponyms 
"""
def directHyponyms(termsSet):
    immidiateHyponyms=set()
    for termSyn in termsSet:
        termHyponyms=set()
        termHyponyms = termSyn.hyponyms()
        immidiateHyponyms.update(termHyponyms)
    return immidiateHyponyms

"""taking the Similarity Degree (SD) and the Key term (d1)"""
keyTerm = wn.synset('material.n.01')
SD = 0.8
maxd1=0

"""finding the depth of the keyTerm (d1)
There are many paths (and tehrefore depths) to the ROOT, here we take the longest path as :var: maxPath"""
for path in keyTerm.hypernym_paths():
    d1=len(path)
    if d1>maxd1:
        maxd1=d1
        maxPath=path

hyponymsSet=set()
print(d1, maxPath)
"""LCS floor"""
LCS_lower = math.ceil(SD/(2-SD)*d1)
"""LCS ceiling"""
LCS_upper = d1
"""calculating d2 position"""
for LCS in range(LCS_lower,LCS_upper+1):
    """d2 floor"""
    d2_lower = LCS
    """d2 ceiling"""
    d2_upper = math.floor(2*(LCS/SD) - d1)

    for d2 in range(d2_lower,d2_upper+1):
        if d2 == LCS:
            start = LCS-1
            hyponymsSet.add(maxPath[start])
        else:
            hyponymsSet.update(directHyponyms(hyponymsSet))
        print ("for the LCS {}, the d2 locates at position {} in the HypernymTree".format(LCS, d2))

print("HypernymTree is:\n {}".format(hyponymsSet))
