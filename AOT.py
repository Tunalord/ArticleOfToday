import random #imports random
import webbrowser #imports web browser
print("the article of today is")
#the random article is selected
articleSelected = random.randint(0,2)
#the articles in an array
article = ["https://en.wikipedia.org/wiki/Python_(programming_language)","https://en.wikipedia.org/wiki/High-level_programming_language","https://en.wikipedia.org/wiki/Computer_science"]
#print the article at the position of the int selected randomly
print(article[articleSelected])
#opens selected article in new window
webbrowser.open(article[articleSelected], new=2)