"""Inverted Index implementation from ... Lecture"""
import argparse
import ast
import re


class InvertedIndex:
    """A Inverted index class."""
    def __init__(self):
        self.inverted_list: dict = {}

    def read_from_file(self, filename: str):
        """
        Construct Index from given file.

        >>> inverted_index = InvertedIndex()
        >>> inverted_index.read_from_file("text.txt")
        [('document', [1, 2, 3]), ('first', [1]), ('second', [2]), ('third', [3])]
        """
        with open(filename) as f:
            corpus = f.read().strip().split("\n")

        for index, doc in enumerate(corpus):
            index += 1
            doc = doc.lower().strip()
            for token in re.split(r"[^a-zA-Z]", doc):
                if len(token) > 0:
                    if token in self.inverted_list:
                        self.inverted_list[token].append(index)
                    else:
                        self.inverted_list[token] = [index]
        with open("search_index", mode="w") as f:
            out = str(list(sorted(self.inverted_list.items())))
            f.write(out)
    
    @staticmethod
    def search(text: str, index_file="search_index"):
        text = text.lower()
        text_token = re.split(r"[^a-zA-Z]", text)

        with open(index_file, mode="r") as f:
            index = f.read()
            index = ast.literal_eval(index)
        
        for token in text_token:
            token = token.lower().strip()
            print(f"{token}", dict(index).get(token))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Information Retrieval Inverted Indexing")
    parser.add_argument("--search")
    args = parser.parse_args()

    inverted_index = InvertedIndex()
    if args.search:
        inverted_index.search(args.search)
    # inverted_index.read_from_file("../data/train/5FD1A8FB7F6C.txt"
