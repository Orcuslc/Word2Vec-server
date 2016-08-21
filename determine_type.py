import word2vec as wv
import numpy as np
import sys

model_path = '/home/chuanlu/Downloads/text8.bin'
attr = ['fruit', 'sport', 'weather', 'human', 'animal', 'nature', 'universe']
model = wv.load(model_path)

def cosine_similarity(vec1, vec2):
	return np.dot(vec1, vec2)/(np.sqrt(np.dot(vec1, vec1)*np.dot(vec2, vec2)))

def judge_type(word):
	word = model[word]
	attr_vec = [model[i] for i in attr]
	type_vec = np.asarray([cosine_similarity(word, attri) for attri in attr_vec])
	argmax = type_vec.argmax(0)
	print(attr[argmax])


if __name__ == '__main__':
	word = sys.argv[1]
	judge_type(word)
