from levenshtein import percent_dif
from itertools import islice
from numpy import std, mean

def get_repeating_lines(start, increment, lines, maxPercentDif=.34):
    "Returns either None or a tuple for an xrange of the repeating line numbers."
    head = lines[start]
    count = 0
    for line in islice(lines,start+increment,None,increment):
        if percent_dif(head, line) < maxPercentDif:
            count+=1
        else:
            break
    if count <= 1:
        return None
    else:
        return (start, start+increment*(count+1), increment)

def find_repeating_line_groups(lines, maxPercentDif=.34, maxIncrement=3):
    "Returns a list of all xrange-tuples that represent repeating line numbers."
    in_group_flags = [False]*len(lines)
    groups = []
    for start in xrange(len(lines)):
        for increment in xrange(1, maxIncrement):
            if not in_group_flags[start]:
                group = get_repeating_lines(start, increment, lines, maxPercentDif=maxPercentDif)
                if group:
                    groups.append(group)
                    for i in xrange(*group):
                        in_group_flags[i] = True
    return groups

def is_probable_lle(group, lines, outlierFactor=1):
    "Returns true if the group is a probable error in a repetative group."
    start, end, inc = group
    percent_difs = []
    for i in xrange(start, end, inc):
        for j in xrange(i+inc, end, inc):
            percent_difs.append(percent_dif(lines[i], lines[j]))
    avg = mean(percent_difs)
    sigma = std(percent_difs)
    for dif in percent_difs:
        if abs(dif-avg)>outlierFactor*sigma:
            return True
    return False

if __name__=="__main__":
    import sys
    def print_usage_and_die():
        print """
    Usage:
        python repeat_test.py <fileName> [outlierFactor=1]
        
    The outlier factor is the number of sigmas away from the mean the repeating lines
    difference must be to trigger a positive result.

"""
        exit()
    if len(sys.argv)>3:
        print_usage_and_die()
    try:
        file_name = sys.argv[1]
        if len(sys.argv)>2:
            outlierFactor = float(sys.argv[2])
        else:
            outlierFactor = 1
        with open(file_name, 'r') as f:
            lines = f.read().split("\n")
        lines = [l.strip() for l in lines if l.strip()]
        groups = find_repeating_line_groups(lines)
        for group in groups:
            if is_probable_lle(group, lines, outlierFactor):
                print "Length:", (group[1]-group[0])/group[2]
                for i in xrange(*group):
                    print "%d)\t%s"%(i,lines[i])
                print
    except Exception as e:
        print e
        print_usage_and_die()
