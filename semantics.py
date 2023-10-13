import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Write a note about what you found interesting about the similarities between cat, monkey and banana?
# Cat and monkey: What is interesting is that the score is 0.59 meaning there is a simililarity due to the fact they are both animals regardless of the fact they are not of the same species.
# Banana and monkey: What is interesting is that the score is 0.40 meaning there is some kind of similarity since monkeys are known to eat bananas.
# Banana and cat: What is interesting is that the score is 0.22 meaning there is hardly any similarity due to  the fact that cats do not eat bananas and if they did that would be very strange.

# My own example: 
my_word1 = nlp('shark')
my_word2 = nlp('tomato')
my_word3 = nlp('tomatoe')

print(my_word1.text + " - " + my_word2.text, my_word1.similarity(my_word2) )
print(my_word1.text + " - " + my_word3.text, my_word1.similarity(my_word3) )
print(my_word2.text + " - " + my_word3.text, my_word2.similarity(my_word3) )

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

