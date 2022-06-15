from stanfordcorenlp.corenlp import StanfordCoreNLP

# The sentence you want to parse
nlp=stanfordcorenlp()
sentence = 'I eat a big and red apple.'

# POS
print('POS：', nlp.pos_tag(sentence))

# Tokenize
print('Tokenize：', nlp.word_tokenize(sentence))

# NER
print('NER：', nlp.ner(sentence))

# Parser
print('Parser：')
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))

# Close Stanford Parser
nlp.close()