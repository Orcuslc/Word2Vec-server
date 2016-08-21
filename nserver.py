'''
Forked from https://github.com/3Top/word2vec-api/blob/master/word2vec-api.py
'''
from flask import Flask, request, jsonify
from flask.ext.restful import Resource, Api, reqparse
import numpy as np
import sys
import argparse

parser = reqparse.RequestParser()

def cosine_similarity(vec1, vec2):
	return np.dot(vec1, vec2)/(np.sqrt(np.dot(vec1, vec1)*np.dot(vec2, vec2)))

def filter_words(words):
	if words is None:
		return
	return [word for word in words if word in model.vocab]

class Model(Resource):
	def __init__(self, path):
		with open(path, 'r') as f:
			lines = f.read().split('\n')[:-1]
			# print(lines[-1])
			# print(len(lines))
			lines = [line.split(' ') for line in lines]
			lines = [[line[0]] + [float(i) for i in line[1:]] for line in lines]
			# print(lines[0])
			self.vocab = [line[0] for line in lines]
			nvs = zip([line[0] for line in lines], [line[1:] for line in lines])
			self.vec = dict((name, val) for name, val in nvs)
			# print(self.vec['the'])
	
	def filter_word(self, word):
		if word in self.vocab:
			return True
		else:
			return False
	
	def similarity(self, word1, word2):
		# flag = self.filter_word(word1) && self.filter_word(word2)
		# if flag == True:
		try:
			word1 = self.vec[str(word1)]
			word2 = self.vec[str(word2)]
		# else:
		except BaseException:
			return 0
		return cosine_similarity(word1, word2)

	
	def most_similar_concept(self, word, concept):
		# flag = self.filter_word(word)
		# if flag == True:
		try:
			word = self.vec[str(word)]
		except BaseException:
			return 0
		type_vec = np.asarray([cosine_similarity(word, attr) for attr in concept.vec])
		return(concept.vocab[type_vec.argmax(0)])

	def similarity_concept(self, word, concept):
		try:
			word = self.vec[str(word)]
		except BaseException:
			return 0
		type_vec = np.asarray([cosine_similarity(word, attr) for attr in concept.vec])
		return type_vec.tolist()

class Concept(Resource):
	def __init__(self, path):
		with open(path, 'r') as f:
			lines = f.read().split('\n')[:-1]
			self.vocab = lines
			self.vec = [model.vec[word] for word in self.vocab]

class Most_Similar_Concept(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('word', type=str, required=True, action='append')
		args = parser.parse_args()
		word = args.get('word')[0]
		return model.most_similar_concept(word, concept)

class Similarity_Concept(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('word', type=str, required=True, action='append')
		args = parser.parse_args()
		word = args.get('word')[0]
		return model.similarity_concept(word, concept)

class Similarity(Resource):
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('w1', type=str, required=True, action='append')
		parser.add_argument('w1', type=str, required=True, action='append')
		args = parser.parse_args()
		w1 = args.get('w1')[0]
		w2 = args.get('w2')[0]
		return model.similarity(w1, w2)


class N_Similarity(Resource):
	pass

class Most_Similar(Resource):
	pass



app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
	global model, concept
	p = argparse.ArgumentParser()
	p.add_argument('--model', help='Path to the trained model')
	p.add_argument('--port', help='Server port, default: 5000')
	p.add_argument('--host', help='Server host, default: localhost')
	p.add_argument('--concept', help='Path to concept files')
	p.add_argument('--path', help='Server path, default: /word2vec')
	args = p.parse_args()
	host = args.host if args.host else 'localhost'
	port = int(args.port) if args.port else 5000
	path = args.path if args.path else '/word2vec'
	model = Model(args.model)
	concept = Concept(args.concept)

	api.add_resource(Most_Similar_Concept, path+'/msc')
	api.add_resource(Similarity_Concept, path+'/sc')
	app.run(host=host, port=port)


