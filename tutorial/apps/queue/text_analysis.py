import spacy
from spacy.symbols import ORTH, LEMMA

# Load the English NLP model once
nlp = spacy.load("en_core_web_sm")

# Add the custom lemmatizer to the pipeline after the 'ner' component
nlp.add_pipe(custom_lemmatizer, after='ner')


def custom_lemmatizer(doc):
    for token in doc:
        if token.text == 'Frisco':
            token.lemma_ = 'San Francisco'
    return doc


def print_tokens(text):
    """Prints individual tokens in the provided text."""
    doc = nlp(text)
    print([w.text for w in doc])


def print_verbs(text):
    """Prints verbs and gerunds from the provided text."""
    doc = nlp(text)
    print([w.text for w in doc if w.tag_ == 'VBG' or w.tag_ == 'VB'])


def update_lemmas():
    """Updates the lemma for 'Frisco' to 'San Francisco'."""
    special_case = [{ORTH: u'Frisco', LEMMA: u'San Francisco'}]
    nlp.tokenizer.add_special_case(u'Frisco', special_case)


def print_lemmas(text):
    """Prints tokens and their lemmas from the provided text."""
    doc = nlp(text)
    for token in doc:
        print(token.text, token.lemma_)


def print_named_entities(text):
    """Prints tokens that are recognized as named entities."""
    doc = nlp(text)
    for token in doc:
        if token.ent_type_:
            print(token.text, token.ent_type_)


def print_pos_and_dependencies(text):
    """Prints tokens, their part-of-speech tags, and dependencies."""
    doc = nlp(text)
    for token in doc:
        print(token.text, token.pos_, token.dep_)


def print_root_and_pobj(text):
    """Prints root and object of preposition from each sentence."""
    doc = nlp(text)
    for sent in doc.sents:
        print([w.text for w in sent if w.dep_ == 'ROOT' or w.dep_ == 'pobj'])


# Sample usage
text_sample = "I have flown to LA. Now I am flying to Frisco."
print_tokens(text_sample)
print_verbs(text_sample)
update_lemmas()
print_lemmas("I am flying to Frisco")
print_named_entities(text_sample)
print_pos_and_dependencies(text_sample)
print_root_and_pobj(text_sample)
