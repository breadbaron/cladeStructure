import sys
from math import log, exp

def unique(inList):
    out = []
    for item in inList:
        if not item in out:
            out.append(item)
    return out
def isUnique(inList):
    return len(unique(inList)) == 1
def within(a,(b,c),leftInclude=1, rightInclude=1):
    '''returns whether a is within (b,c)'''
    if leftInclude and rightInclude:
        return a>=b and a<=c
    elif leftInclude and not rightInclude:
        return a>=b and a<c
    elif not leftInclude and not rightInclude:
        return a>b and a<c
    elif not leftInclude and rightInclude:
        return a>b and a<=c

def add_logs(x,y):
    "A fast way to add logarithms"
    if not x==0 and not y==0:
        return x+log(1+exp(y-x))
    elif x==0 and y==0:
        sys.stderr.write('problem with log values\n')
        sys.exit(1)
    elif x==0:
        return y
    elif y==0:
        return x
def get_cmd_args():
    import sys
    argDict = {}
    argDict['options'] = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith('-'):
            # a new argument
            arg = arg[1:]
            i+=1
            while i < len(sys.argv):
                if not sys.argv[i].startswith('-'):
                    if argDict.has_key(arg):
                        if type(argDict[arg]) == list:
                            argDict[arg].append(sys.argv[i])
                        else:
                            argDict[arg] = [argDict[arg]]
                            argDict[arg].append(sys.argv[i])
                    else:
                        argDict[arg] = sys.argv[i]
                    i += 1
                else:
                    i -= 1
                    break

        else:
            argDict['options'].append(arg)
        i += 1
    return argDict

def check_nonoverlap(gffDict):
    return True
