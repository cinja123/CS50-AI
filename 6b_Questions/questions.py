import math
import nltk
import sys
import os
import string

from numpy import char

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)
    
    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)
    
    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = {}
    for filename in os.listdir(directory):
        if not filename.endswith(".txt"): 
            continue
        with open(os.path.join(directory, filename), encoding="utf8") as f:
            files[filename] = f.read()
    return files



def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    punctuation = set(string.punctuation)
    stop_words = nltk.corpus.stopwords.words("english")
    
    words = nltk.word_tokenize(document.lower())
    return [word for word in words if not all(char in punctuation for char in word) and word not in stop_words]


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = dict()
    for filename in documents:
        words_seen_in_doc = set()
        for word in documents[filename]:
            if word not in words_seen_in_doc:
                words_seen_in_doc.add(word)
                if word in idfs.keys():
                    idfs[word] += 1
                else:
                    idfs[word] = 1

    return {word: math.log(len(documents) / idfs[word]) for word in idfs}


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    scores = dict()
    for filename, words in files.items():
        tf_idf = 0
        for word in query:
            tf_idf += words.count(word) * idfs[word]
        scores[filename] = tf_idf  
    sorted_filenames = [filename for filename,score in sorted(scores.items(), key=lambda x: x[1], reverse=True)][:n]

    return sorted_filenames


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    ranked_sentences = list()
    for sentence in sentences:
        # sentence, matching word measure, query term desnity
        sentence_rank = [sentence, 0, 0]
        for word in query:
            if word in sentences[sentence]:
                sentence_rank[1] += idfs[word]
                sentence_rank[2] += sentences[sentence].count(word) / len(sentences[sentence])
        ranked_sentences.append(sentence_rank)
    return [sentence for sentence, mwm, qtd in sorted(ranked_sentences, key=lambda x: (x[1], x[2]), reverse=True)][:n]


if __name__ == "__main__":
    main()
