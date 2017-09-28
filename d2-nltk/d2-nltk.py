from nltk.book import *
import nltk

# Data already downloaded
# nltk.download()

# Searching for text
print("Concordiance functon - look for a word")
print(text1.concordance("monstrous"))

# Similar range of context (of a word)
print("Similar function - looking for context of a word")
print(text1.similar("monstrous"))

# Common context for a given word
print("Common context function - common context for a given word")
print(text2.common_contexts(["monstrous", "very"]))

# Frequence distribution
print("Frequence distribution - ")
fdist1 = FreqDist(text1)
print(fdist1)
print(fdist1.most_common(50))

