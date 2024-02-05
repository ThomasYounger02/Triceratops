# Cleaning

网页标签提取

```python
summaries = soup.find_all("div", {"class":"course-summary-card"})
```

网页整理

```python
print(summaries[0].prettify())
```

内容提取

```python
summaries[0].select_one("h3").get_text().strip()
```

# Normalization

## Case Normalization

```python
# Convert to lowercase
text = text.lower()
```

## Punctuation Normalization

```python
import re
# Remove punctuation characters
text = re.sub(r"[^a-zA-Z0-9]", " ", text)
```

# Tokenization

下载

```python
import nltk
nltk.download('punkt')
#nltk.download() 全部
```

拆分成句子或者单词

```python
# import statements
from nltk.tokenize import word_tokenize, sent_tokenize

# Split text into words using NLTK
words = word_tokenize(text)

# Split text into sentences
sentences = sent_tokenize(text)
```

# Stop Words

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

print(stopwords.words("english"))
```

过滤

```python
from nltk.corpus import stopwords

# Remove stop words
words = [w for w in words if w not in stopwords.words('english')]
print(words)
```

# POS & NER

```python
import nltk
from nltk.tokenize import word_tokenize
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
```

## pos tagging

```python
# import statements
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from nltk import ne_chunk
```

```python
# tokenize text
sentence = word_tokenize(text)

# tag each word with part of speech
pos_tag(sentence)
```

## ner

```python
# tokenize, pos tag, then recognize named entities in text
tree = ne_chunk(pos_tag(word_tokenize(text)))
print(tree)
```

## Sentence Parsing

```python
# Define a custom grammar
my_grammar = nltk.CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")
parser = nltk.ChartParser(my_grammar)
```

```python
# Parse a sentence
sentence = word_tokenize("I shot an elephant in my pajamas")
for tree in parser.parse(sentence):
    print(tree)
```

# Stemming and Lemmatizing

```python
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet') # download for lemmatization
```

## Stemming

```python
from nltk.stem.porter import PorterStemmer

# Reduce words to their stems
stemmed = [PorterStemmer().stem(w) for w in words]
print(stemmed)
```

## Lemmatization

```python
from nltk.stem.wordnet import WordNetLemmatizer

# Reduce words to their root form
lemmed = [WordNetLemmatizer().lemmatize(w) for w in words]
print(lemmed)
```

```python
# Lemmatize verbs by specifying pos
lemmed = [WordNetLemmatizer().lemmatize(w, pos='v') for w in lemmed]
print(lemmed)
```

# Feature Extraction

Below, we'll look at three useful methods of vectorizing text.

- `CountVectorizer` - Bag of Words
- `TfidfTransformer` - TF-IDF values
- `TfidfVectorizer` - Bag of Words AND TF-IDF values

Let's first use an example from earlier and apply the text processing steps we saw in this lesson.

```python
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

```python
corpus = ["The first time you see The Second Renaissance it may look boring.",
        "Look at it at least twice and definitely watch part 2.",
        "It will change your view of the matrix.",
        "Are the human people the ones who started the war?",
        "Is AI a bad thing ?"]

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()
```

```python
def tokenize(text):
    # normalize case and remove punctuation
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # tokenize text
    tokens = word_tokenize(text)
    
    # lemmatize andremove stop words
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    return tokens
```

## CountVectorizer (Bag of Words)

```python
from sklearn.feature_extraction.text import CountVectorizer

# initialize count vectorizer object
vect = CountVectorizer(tokenizer=tokenize)

# get counts of each token (word) in text data
X = vect.fit_transform(corpus)

# convert sparse matrix to numpy array to view
X.toarray()

# view token vocabulary and counts
vect.vocabulary_
```

## TfidfTransformer

```python
from sklearn.feature_extraction.text import TfidfTransformer

# initialize tf-idf transformer object
transformer = TfidfTransformer(smooth_idf=False)

# use counts from count vectorizer results to compute tf-idf values
tfidf = transformer.fit_transform(X)

# convert sparse matrix to numpy array to view
tfidf.toarray()
```

## TfidfVectorizer

TfidfVectorizer = CountVectorizer + TfidfTransformer



from sklearn.feature_extraction.text import TfidfVectorizer

# initialize tf-idf vectorizer object
vectorizer = TfidfVectorizer()


# compute bag of word counts and tf-idf values
X = vectorizer.fit_transform(corpus)

# convert sparse matrix to numpy array to view
X.toarray()