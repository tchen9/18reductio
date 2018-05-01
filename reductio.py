file = open("text.txt","r")
words = file.read()

wlist = words.split()

def singlefreq(word):
    freq = [i for i in wlist if i.lower() == word.lower()]
    return len(freq)

print "Frequency of nonsense: ", singlefreq("nonsense")
print "Frequency of women: ", singlefreq("women")
print "Frequency of brooklyn: ",singlefreq("brooklyn")

def totalfreq(words):
    return reduce(lambda x,y: x+y, [singlefreq(w) for w in words])

print "Frequency of nonsense and women: ", totalfreq(["nonsense", "women"])

