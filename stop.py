def loadstop(filename):
    f=open(filename,"r",encoding="gbk")
    l=[]
    s=f.readlines()
    for x in s:
        l.append(x.strip())
    return l

def stop(old,stopword):
    new=[]
    for x in old:
        if x in stopword:
            pass
        elif str(x).isdigit():
            pass
        else:
            new.append(x)
    return  new
#
# old=["hh","啊","的","hh"]
# w=loadstop("stopword.txt")
# new=stop(old,w)
# print(new)
# print(w)