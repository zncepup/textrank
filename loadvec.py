# # coding:utf-8
# import numpy
# from gensim.models import word2vec
# import logging, gensim, os
#
# '''def computedistance(d1,d2):
#     dis=numpy.linalg.norm(d1-d2)
#     return dis
# def loadvec():
#     model = gensim.models.KeyedVectors.load_word2vec_format("model.txt", binary=False)
# '''
# '''s=gensim.models.word2vec.Text8Corpus(u"3.txt")
# model=word2vec.Word2Vec(s)
# model.wv.save_word2vec_format("model-2.txt",fvocab="model-2.vocab",binary=False)
# '''
# model=gensim.models.KeyedVectors.load_word2vec_format("model-2.txt",fvocab="model-2.vocab",binary=False)
# a="的"
# if a not in model.wv.vocab:
#     print("111")
a={0:1,1:2,3:4,4:1}
print(max(a))