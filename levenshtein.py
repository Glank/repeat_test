def levenshtein(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    d = [[0 for j in xrange(len(str2)+1)] for i in xrange(len(str1)+1)]
    for i in xrange(1, len(str1)+1):
        d[i][0] = i
    for j in xrange(1, len(str2)+1):
        d[0][j] = j
    for j in xrange(1, len(str2)+1):
        for i in xrange(1, len(str1)+1):
            if str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1
    return d[-1][-1]

def percent_dif(str1, str2):
    lev = levenshtein(str1, str2)
    length = max(len(str1), len(str2), 1)
    return float(lev)/length

def levenshtein_min(str1, str2, mini):
    str1 = list(str1)
    str2 = list(str2)
    d = [[0 for j in xrange(len(str2)+1)] for i in xrange(len(str1)+1)]
    for i in xrange(1, len(str1)+1):
        d[i][0] = i
    for j in xrange(1, len(str2)+1):
        d[0][j] = j
    for j in xrange(1, len(str2)+1):
        for i in xrange(1, len(str1)+1):
            if str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1
            if len(str1)-i==len(str2)-j and d[i][j]>mini:
                return d[i][j]
    return d[-1][-1]

def percent_dif_min(str1, str2, min_per):
    length = max(len(str1), len(str2))
    if length == 0:
        length=0.001
    min_dif = min_per*length
    lev = levenshtein_min(str1, str2, min_dif)
    return float(lev)/length
