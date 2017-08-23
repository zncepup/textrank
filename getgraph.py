import wmd
def filecut(fname,wmd):
    with open(fname) as f:
        s=f.read()
        s=s.split("。")
    w=[[0 for x in range(len(s))] for x in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s)):
            if j != i:
                if wmd.compute(s[i],s[j])<999:
                    w[i][j]=1.0/wmd.compute(s[i],s[j])
                else:
                    w[i][j]=0.0
            else:
                w[i][j]=0.0
    return s,w

wmd=wmd.a()
s,w=filecut("test.txt",wmd)
print(w)

print("只是一个尝试")