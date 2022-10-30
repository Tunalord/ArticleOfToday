import random #imports random

print("the article of today is")
#the random article is selected
articleSelected = random.randint(0,2)
#the articles in an array
article = ["https://en.wikipedia.org/wiki/Python_(programming_language)","https://en.wikipedia.org/wiki/High-level_programming_language","https://en.wikipedia.org/wiki/Computer_science"]
#print the article at the position of the int selected randomly
print(article[articleSelected])