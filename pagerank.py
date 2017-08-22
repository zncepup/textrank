import wmd
import time
import getgraph
class textrank:
    def __init__(self,filename):
        # a=time.time()
        # print(a)
        self.damping_factor=0.85
        self.maxx_iteration=100
        self.min_delta=0.00001
        a=wmd.a()
        self.s,self.w=getgraph.filecut(filename,a)
        # print(time.time())
    def getaroundnode(self,n):
        nodes=[]
        sumweights=.0
        for x in range(len(self.s)):
            if self.w[n][x]>0.001:
                sumweights+=self.w[n][x]
                nodes.append(x)
        return nodes,sumweights
    def pagerank(self):
        graph_size=len(self.s)
        key=[i for i in range(graph_size)]
        pagerank=dict.fromkeys(key,1./graph_size)
        flag=False
        for i in range(self.maxx_iteration):
            change=0
            for node in range(len(self.s)):
                rank=0
                nodes,_=self.getaroundnode(node)
                rank_right=0.0
                for aroundnode in nodes:
                    _,sum=self.getaroundnode(aroundnode)
                    rank_from_j=self.w[node][aroundnode]/sum*pagerank[aroundnode]
                    rank_right+=rank_from_j
                rank=1.0-self.damping_factor+self.damping_factor*rank_right
                change+=abs(pagerank[node]-rank)
                pagerank[node]=rank
            print("this is No.%s iteration"%(i+1))
            print(pagerank)

            if change<self.min_delta:
                flag=True
                break
        if flag:
            print("finished in %s iteration"%(i+1))
        else:
            print("out of 100")
        return pagerank




a=textrank("test.txt")
pangerank=a.pagerank()
max=sorted(pangerank.items(),key=lambda item:item[1])[-1]
print(max[0])
print(a.s[max[0]])