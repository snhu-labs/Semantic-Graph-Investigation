from stanfordcorenlp.corenlp import StanfordCoreNLP

nlp= StanfordCoreNLP('C:\\Users\\Student\\PycharmProjects\\pythonProject1\\stanford-corenlp-4.4.0',lang='en',memory='8g')

sentence1='The strongest rain ever recorded in India shut down the financial hub of Mumbai, snapped communication lines, closed airports and forced thousands of people to sleep in their offices or walk home during the night, officials said today.'
sentence = 'The quick brown fox jumped over the lazy dog.'
sentence2='Southern New Hampshire University is a 4-year college based in Manchester, New Hampshire (N.H). Michael is a student who studies computer science at SNHU. Michael Works with Deepu on a team with Jordan and Seth. Seth and Jordan both work for SNHU. During todays meeting, Michael and Deepu had the pleasure of meeting Anthony today. Anthony works for a company called Riiid. Southern New Hampshire University currently employees Jordan and Seth as full time workers as Michael and Deepu are employed part time as a student job. Anthony attends the University of Toroto, which is located in Toronto,Canada. Deepu and Michael are working together with Jordan and Seth and have now included Jordan in part of their research team. They are trying to figure out what NLP happens to be better suited for the job. Whether it is the Stanford NLP or the Spacy NLP.'

print('POS：', nlp.pos_tag(sentence1))

print('Tokenize：', nlp.word_tokenize(sentence1))

print('NER：', nlp.ner(sentence1))

print('Parser：')
print(nlp.parse(sentence1))
print(nlp.dependency_parse(sentence1))
print(nlp.coref(sentence1))

nlp.close()