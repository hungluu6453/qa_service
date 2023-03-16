import string
import numpy as np
import re
from gensim.corpora import Dictionary
from gensim.models import TfidfModel, OkapiBM25Model
from gensim.similarities import SparseMatrixSimilarity

# best_document = corpus[np.argmax(similarities)]


class BM25Gensim:
    def __init__(self, data=None):
        if data:
            self.corpus = [text.split() for text in data]

    def create_model(self, output_path):
        dictionary = Dictionary(self.corpus)
        bm25_model = OkapiBM25Model(dictionary=dictionary)
        bm25_corpus = bm25_model[list(map(dictionary.doc2bow, self.corpus))]
        bm25_index = SparseMatrixSimilarity(
            bm25_corpus,
            num_docs=len(self.corpus),
            num_terms=len(dictionary),
            normalize_queries=False,
            normalize_documents=False
            )
        tfidf_model = TfidfModel(dictionary=dictionary, smartirs='bnn')

        dictionary.save(output_path + "/dict")
        tfidf_model.save(output_path + "/tfidf")
        bm25_index.save(output_path + "/bm25_index")

    def load_model(self, checkpoint_path):
        self.dictionary = Dictionary.load(checkpoint_path + "/dict")
        self.tfidf_model = SparseMatrixSimilarity.load(checkpoint_path + "/tfidf")
        self.bm25_index = TfidfModel.load(checkpoint_path + "/bm25_index")

    def preprocess(self, text):
        exclude = set(string.punctuation)
        text = ' '.join(text.split())
        text = ''.join(ch for ch in text if ch not in exclude)
        text = text.lower()
        text = text.replace('\n', ' ')
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def get_top_result(self, query, topk=10):
        query = self.preprocess(query)
        tokenized_query = query.split()
        tfidf_query = self.tfidf_model[self.dictionary.doc2bow(tokenized_query)]
        scores = self.bm25_index[tfidf_query]
        top_n = np.argsort(scores)[::-1][:topk]
        return top_n.tolist()  # , scores[top_n], " ".join(self.corpus[np.argmax(scores)])
