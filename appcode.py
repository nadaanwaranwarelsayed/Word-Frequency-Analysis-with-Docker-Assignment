import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('stopwords')
with open('random_paragraphs.txt', 'r') as file:
    text = file.read()
    

tokens = nltk.word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print(filtered_tokens)
word_counts = Counter(filtered_tokens)

#for word, count in word_counts.items():
#    print(f"{word}: {count}")
