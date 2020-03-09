import numpy as np
from numpy import dot
from numpy.linalg import norm
import os
from numpy import dot
from sqlitedict import SqliteDict


class FTOOC:
    """FastText Out Of Core class"""

    __modelPath = ""
    vectorDatabase = dict()
    __savedVectors = dict()
    saveGeneratedVectors = False

    def __init__(self, path):
        self.__modelPath = path
        databasePath = os.path.join(
            os.path.dirname(self.__modelPath), "blanksort.database"
        )
        print("Database path: " + databasePath)
        self.vectorDatabase = SqliteDict(databasePath, autocommit=True)
        if not os.path.exists(databasePath):
            self.preloadVectors()

    def __cos_sim(self, a, b):
        return (1 + (dot(a, b) / (norm(a) * norm(b)))) / 2.0

    def inVocab(self, searchToken):
        return searchToken in self.vectorDatabase

    def loadVector(self, word):
        try:
            if word not in self.__savedVectors:
                self.__savedVectors[word] = self.vectorDatabase[word]
        except Exception:
            pass

    def preloadVectors(self):
        print("Vectors are being loaded into memory.")
        print("Loading may take a while.")
        count = 0
        for key in self.vectorDatabase.keys():
            self.__savedVectors[key] = self.vectorDatabase[key]
            count += 1
        print("Loaded " + str(count) + " vectors.")

    def __generateNgrams(self, searchToken, minN, maxN):
        ngrams = []
        for ngram_length in range(minN, min(len(searchToken), maxN) + 1):
            for i in range(0, len(searchToken) - ngram_length + 1):
                ngrams.append(searchToken[i : i + ngram_length])
        return ngrams

    def __generateVector(self, searchToken):
        ngrams = self.__generateNgrams(searchToken, 3, 6)
        wordVector = np.zeros(300, dtype=np.float32)
        ngramsFound = 0
        for ngram in ngrams:
            if self.inVocab(ngram):
                ngramsFound += 1
                wordVector += self.getVector(ngram)
        if wordVector.any():
            return wordVector / max(1, ngramsFound)
        else:
            return np.random.rand(300) * 2 - 1
            # raise KeyError("all ngrams for word " + searchToken + " absent from model")

    def getVector(self, searchToken):
        if searchToken in self.__savedVectors or self.inVocab(searchToken):
            if searchToken not in self.__savedVectors:
                self.__savedVectors[searchToken] = self.vectorDatabase[searchToken]
        else:
            self.__savedVectors[searchToken] = self.__generateVector(searchToken)
            if self.saveGeneratedVectors:
                self.vectorDatabase[searchToken] = self.__savedVectors[searchToken]
        return self.__savedVectors[searchToken]

    def similarity(self, a, b):
        return self.__cos_sim(self.getVector(a), self.getVector(b))
