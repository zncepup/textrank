# # import numpy
# # import libwmdrelax
# #
# # embeddings = numpy.array([[0.1, 1], [1, 0.1]], dtype=numpy.float32)
# # nbow = {"first":  ("#1", [0, 1], numpy.array([1.5, 0.5], dtype=numpy.float32)),
# #         "second": ("#2", [0, 1], numpy.array([0.75, 0.15], dtype=numpy.float32))}
# # calc = libwmdrelax.emd_relaxed()
# import jieba.posseg as psg
# import jieba
# def tt():
#     jieba.add_word("小型客车")
# jieba.add_word("藏宝阁")
# tt()
# jieba.suggest_freq(("太","贵"),True)
# s=jieba.cut("藏宝阁太贵",HMM=False)
# print(" ".join(s))
import time

import gensim
import jieba
import pyemd
import numpy
import stop
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.metrics import euclidean_distances
class a:
    def __init__(self):
        # self.start=time.time()
        self.model=gensim.models.KeyedVectors.load_word2vec_format("model.txt", fvocab="vocab.vocab", binary=False)
        # self.stopword=stop.loadstop("stopword.txt")
    def cutsentence(self,s1,s2):
        s1=jieba.cut(s1)
        s2=jieba.cut(s2)
        return list(s1),list(s2)
    def drop(self,s1,s2):
        new1=[x for x in s1 if x in self.model.wv.vocab]
        new2=[x for x in s2 if x in self.model.wv.vocab]
        return new1,new2
    def listtostr(self,s1,s2):
        ss1=""
        ss2=""
        for x in s1:
            ss1=ss1+str(x)+" "
        for x in s2:
            ss2=ss2+str(x)+" "
        return ss1.strip(),ss2.strip()
    def emd_d(self,v1, v2, d):
        v1 = v1.astype(numpy.double)
        v2 = v2.astype(numpy.double)
        v1 /= v1.sum()
        v2 /= v2.sum()
        distances = float(pyemd.emd(v1, v2, d))
        return distances
    def getvec(self,s1,s2):
        vect = CountVectorizer(token_pattern='(?u)\\b\\w+\\b').fit([s1, s2])
        v1, v2 = vect.transform([s1, s2])
        v1 = v1.toarray().ravel()
        v2 = v2.toarray().ravel()
        w = numpy.array([self.model[w] for w in vect.get_feature_names()])
        d = euclidean_distances(w)
        d = d.astype(numpy.double)
        d /= d.max()
        return v1,v2,d
    def compute(self,s1,s2):
        s1,s2=self.cutsentence(s1,s2)
        s1,s2=self.drop(s1,s2)
        if len(s1)!=0 and len(s2)!=0:
            s1,s2=self.listtostr(s1,s2)

            v1,v2,d=self.getvec(s1,s2)
            distance=self.emd_d(v1,v2,d)
            # print(time.time()-self.start)
            return distance
        else :
            return 100
# a1=a()
# b=a1.compute("中华人民共和国今天成立了","你妈妈喊你回家吃饭")
# c=a1.compute("","")
# print(b,c)

