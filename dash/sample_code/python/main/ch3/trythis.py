import spacy

nlp = spacy.load('en')
doc = nlp(u'A noun chunk is a phrase that has a noun as its head.')
for token in doc:
    if token.pos_ == 'NOUN':
        chunk = ''
        for w in token.lefts:
            chunk = chunk + w.text + ' '
        chunk = chunk + token.text
        print(chunk)
