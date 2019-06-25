import unicodedata

def dict_from(olddict):
    newdict = {}
    for item in olddict.keys():
        newdict[item] = unicodedata.normalize("NFKD", olddict[item]).encode('ascii','ignore')
    return newdict