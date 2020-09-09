from typing import List, Tuple
from gensim.models.doc2vec import Doc2Vec
import re
import spacy

class Doc2VecRec:
    model = None

    def __init__(self, filename: str=None):
        self.nlp = spacy.load("en_core_web_sm")
        self.exception_regex = re.compile(r".+Exception[^\n].*\s+at", re.MULTILINE | re.IGNORECASE)
        self.greater_regex = re.compile(r"^> .*$", re.MULTILINE | re.IGNORECASE)
        self.gerrit_created_regex = re.compile(r"New Gerrit change created: [^\ ]+", re.MULTILINE | re.IGNORECASE)
        self.gerrit_merge_regex = re.compile(r"Gerrit change [^\s]+ was merged to [^\.]+\.", re.MULTILINE | re.IGNORECASE)
        self.gerrit_commit_regex = re.compile(r"Commit: [^\ ]+", re.MULTILINE | re.IGNORECASE)
        self.filter = ['VERB', 'NOUN', 'PROPN']
        if filename != None:
            self.load(filename)

    def load(self, filename: str):
        self.model = Doc2Vec.load(filename)

    def recommendClosest(self, text: str) -> List[Tuple[float, float]]:
        """Recomends the 'closest' bugs to the text string passed in."""

        tokens = self.tokenize(text)
        vector = self.model.infer_vector(tokens)

        similar = self.model.docvecs.most_similar([vector])
        print(self.model.trainables)
        return similar


    def tokenize(self, text: str) -> List[str]:
        """Returns a list of tokens created from the text."""

        text = self.greater_regex.sub("", text)
        text = self.exception_regex.sub("", text)
        text = self.gerrit_created_regex.sub("", text)
        text = self.gerrit_merge_regex.sub("", text)
        text = self.gerrit_commit_regex.sub("", text)
        filtered_tokens = []
        
        doc = self.nlp(text)
        for sent in doc.sents:
            for token in sent:
    #            if re.fullmatch('[a-zA-Z]+', token.text) and not token.is_stop:
    #            if token.pos_ in filter and re.fullmatch('[a-zA-Z]+', token.text):
                if re.fullmatch('[a-zA-Z]+', token.text):
    #                 filtered_tokens.append(token.lemma_)
                    filtered_tokens.append(token.text)
        return filtered_tokens