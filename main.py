# coding:utf-8
import numpy
import pyemd
import stop
import jieba
import gensim
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.metrics import euclidean_distances



def readfile(filename):
    doc=[]
    f=open(filename)
    s=f.readlines()
    for x in s:
        stence=jieba.cut(x.strip())
        doc.extend(stence)
    return doc
def drop(d,model):
  new=[x for x in d if x in model.wv.vocab]
  return new
def listtostr(d):
    s=""
    for x in d:
        s=s+str(x)+" "
    s=s.strip()
    return s
def emd_d(v1,v2,d):
    v1=v1.astype(numpy.double)
    v2=v2.astype(numpy.double)
    v1/=v1.sum()
    v2/=v2.sum()
    distances=float(pyemd.emd(v1,v2,d))
    return distances

d1= readfile("test2.txt")
# print(d1)
d2 = readfile("test3.txt")
stopword = stop.loadstop("stopword.txt")
d1 = stop.stop(d1, stopword)
d2 = stop.stop(d2, stopword)
# print(d1)
model = gensim.models.KeyedVectors.load_word2vec_format("model.txt", fvocab="vocab.vocab", binary=False)

d1 = drop(d1, model)
d2 = drop(d2, model)
print("d1长度", len(d1))
print("d2长度", len(d2))
d1 = listtostr(d1)
d2 = listtostr(d2)
print(d1)
print(d2)
vect = CountVectorizer(token_pattern='(?u)\\b\\w+\\b').fit([d1, d2])
v1, v2 = vect.transform([d1, d2])
print(type(v1))
# print('v1:',v1)
# print('v2:',v1.toarray())
print("-----d1-----", v1.toarray().ravel())
print("-----d2-----", v2.toarray().ravel())
v1 = v1.toarray().ravel()
v2 = v2.toarray().ravel()
# print(v1, "\n", v2)

w = numpy.array([model[w] for w in vect.get_feature_names()])
print(numpy.shape(vect.get_feature_names()))
print(vect.get_feature_names())
d = euclidean_distances(w)
d = d.astype(numpy.double)
d /= d.max()
# print(d)

dis = emd_d(v1, v2, d)
# print(numpy.shape(v1),numpy.shape(v2),numpy.shape(d))
print('距离:', dis)


