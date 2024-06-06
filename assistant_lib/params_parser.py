import spacy

nlp = spacy.load("uk_core_news_sm")

def find_phrase(text_doc, start_words):
    phrase = []
    for token in text_doc:
        if token.head in start_words or token in start_words:
            phrase.append(token)

    if sorted(phrase) == sorted(start_words):
        return " ".join([token.text for token in text_doc if token in start_words])
    else:
        return find_phrase(text_doc, phrase)
    
def extract_params(text: str, keywords: list[str], ban_words: list[str]):
    delete_words = []

    text = " ".join(word for word in text.split() if word.lower() not in delete_words)

    keywords_doc_lemmas = [token.lemma_ for token in nlp(" ".join(keywords))]
    ban_words_doc_lemmas = [token.lemma_ for token in nlp(" ".join(ban_words))]
    doc = nlp(text)

    # пошук ключового слова
    index = -1
    for i, token in enumerate(doc):
        if token.lemma_ in keywords_doc_lemmas:
            index = i
            break

    # пошук залежних слів
    start_words = []

    for token in doc:
        if (
            token.lemma_ not in ban_words_doc_lemmas
            and token.head == doc[index]
            and token != doc[index]
        ):
            start_words.append(token)
            
    if len(start_words) < 1:
        return None

    return find_phrase(doc, start_words)

def normilaze_city(city):
    city = ' '.join(word for word in city.split() if word not in ['у', 'в'])
    cities = {
        'Києві' : 'Київ'
    }
    
    if city in cities.keys():
        return cities[city]
    
    doc = nlp(city)
    
    return doc[0].lemma_
