#Word2vec
from gensim.models import word2vec

from bs4 import BeautifulSoup
from nltk.corpus import stopwords # Import the stop word list
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import nltk.data # Download the punkt tokenizer for sentence splitting


def sof_to_wordlist(review, remove_stopwords=False, stemm=False, lemmatize=False):
    # Function to convert a document to a sequence of words,
    # optionally removing stop words.  Returns a list of words.
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(review, "lxml").get_text()
    #
    # 2. Remove non-letters
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    #
    # 3. Convert words to lower case and split them
    words = review_text.lower().split()
    #
    # 4. Optionally remove stop words
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    #
    # 6. English Stemming
    if stemm :
        stemmer = SnowballStemmer("english")
        steammed_words = [stemmer.stem(mots) for mots in words]
    else:
        steammed_words = words
    #
    # 7. Lemmatization
    if lemmatize :
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmatized_words = [wordnet_lemmatizer.lemmatize(mots) for mots in steammed_words]
    else:
        lemmatized_words = steammed_words
    #
    # 5. Return a list of words
    return(steammed_words)

# Define a function to split a ask into parsed sentences
def sof_to_sentences( review, tokenizer, remove_stopwords=False, stemm=False, lemmatize=False):
    # Function to split a ask into parsed sentences. Returns a
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(review.strip())
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            sentences.append( sof_to_wordlist( raw_sentence, \
              remove_stopwords = remove_stopwords, stemm=stemm, lemmatize=lemmatize ))
    #
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences


def tagme(ma_question, nb_tags):
    model_name = "W2V_All_features_250features_100minwords_10context"
    # Load pre-trained Word2Vec model.
    modelw2v = word2vec.Word2Vec.load(model_name)


    # Load the punkt tokenizer (découpage en phrases)
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    mon_doc = []  # Initialize an empty list of sentences
    mon_doc += sof_to_sentences(ma_question, tokenizer, remove_stopwords = True, stemm = True, lemmatize = False)
    mon_doc = sum(mon_doc, [])
    mots_predits = modelw2v.predict_output_word(mon_doc, topn=nb_tags + 1)
    print("mots_predits: ", mots_predits)
    #### Mots_predits est une liste de tuple,
    #### Conversion en liste simple:
    try:
        liste_mots_predits = [x for tu in mots_predits for x in tu ]
    except TypeError:
        print("Planté !")
    #### Suppression des probabilités
    liste_mots_predits = liste_mots_predits[::2]

    return liste_mots_predits, "process via Word2vec / predict_output_word"
