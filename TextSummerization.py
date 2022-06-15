from gatenlp import Document, Annotation
from gatenlp.processing.tokenizer import NLTKTokenizer
from nltk.tokenize import TreebankWordTokenizer

# Create the document
from gatenlp.features import Features

doc1 = Document("This is the text of the document.")

# set a document feature
doc1.features["purpose"] = "simple illustration of gatenlp basics"

# get the default annotation set
defset = doc1.annset()

# add an annotation that spans the whole document, no features
defset.add(0, len(doc1), "Document", {})

# save the document in bdocjson format, this can be read into Java GATE
# using the format-bdoc plugin.
doc1.save("testdoc.bdocjs")
# Read back the document
doc2 = Document.load("testdoc.bdocjs")

# print the json representation of the loaded document
print(doc2.save_mem(fmt="json"))



nltk_tok = TreebankWordTokenizer()
ann_tok = NLTKTokenizer(nltk_tokenizer=nltk_tok)
doc1 = ann_tok(doc1)

# get the annotation set with the name "NLTK" and print the number of annotations
set_nltk = doc1.annset("NLTK")
print(len(set_nltk))

# get only annotations of annotation type "Token" from the set and print the number of annotations
# since there are no other annotations in the original set, the number should be the same
set_tokens = set_nltk.with_type("Token")
print(len(set_tokens))

# print all the annotations in order
for ann in set_tokens:
    print(ann)
#check if the set_nltk is detached
print("set_nltk is detached: ", set_nltk.isdetached())  # no it is attached!
print("set_nltk is immutable: ", set_nltk.immutable)  # no
# add an annotation to the set
set_nltk.add(3, 5, "New1")

# check if the set_tokens is detached
print("set_tokens is detached: ", set_tokens.isdetached())  # yes!
# check if it is immutable as well
print("set_tokens is immutable: ", set_tokens.immutable)  # yes
try:
    set_tokens.add(5, 7, "New2")
except Exception as ex:
    print("Error:", ex)

# ok, let's make the set mutable and add the annotation
set_tokens.immutable = False
set_tokens.add(5, 7, "New2")

print("set_nltk: size=", len(set_nltk), ", annotation:", set_nltk)
print("set_tokens: size=", len(set_tokens), ", annotations: ", set_tokens)

# check if the set_nltk is detached
print("set_nltk is detached: ", set_nltk.isdetached())  # no it is attached!
print("set_nltk is immutable: ", set_nltk.immutable)  # no
# add an annotation to the set
set_nltk.add(3, 5, "New1")

# check if the set_tokens is detached
print("set_tokens is detached: ", set_tokens.isdetached())  # yes!
# check if it is immutable as well
print("set_tokens is immutable: ", set_tokens.immutable)  # yes
try:
    set_tokens.add(5, 7, "New2")
except Exception as ex:
    print("Error:", ex)

# ok, let's make the set mutable and add the annotation
set_tokens.immutable = False
set_tokens.add(5, 7, "New2")

print("set_nltk: size=", len(set_nltk), ", annotation:", set_nltk)
print("set_tokens: size=", len(set_tokens), ", annotations: ", set_tokens)