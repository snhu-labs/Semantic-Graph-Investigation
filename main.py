# Michael Colandrea
# Testing

# All labels can be found here
# https://github.com/explosion/spacy-models/blob/master/meta/en_core_web_md-3.0.0.json


from html import entities
from webbrowser import get
import spacy

# Load English token, tag, parser and NER
nlp = spacy.load("en_core_web_sm")

# Read whole document

text = ("Peyton Manning, in full Peyton Williams Manning, born March 24, 1976, New Orleans, Louisiana, U.S.,"
        "American collegiate and professional gridiron football quarterback who is considered one of the greatest players at his position in"
        "National Football League (NFL) history. He won Super Bowls as the quarterback of the Indianapolis Colts (2007) and the Denver Broncos (2016). "
        "C# is great and Michael loves programming and is his greatest position")

doc = nlp(text)

# Analyze Syntax
# print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
# print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# find named entities, phrases and concepts
# https://github.com/explosion/spacy-models/blob/master/meta/en_core_web_md-3.0.0.json


for token in doc:
    print(f"{token.text} => {token.dep_}")

for x in doc.ents:
    print(f"{x.text} => {x.label_}")
