from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

df = pd.read_csv(r"dataMeizu.csv", encoding ="latin-1") 

my_list = ["hey","you","suck","why","don't","you","fuck","off"]

comment_words = ' '
stopwords = set(STOPWORDS) 

for val in df.review_text: 
	val = str(val) 
	tokens = val.split() 
	
	for i in range(len(tokens)): 
		tokens[i] = tokens[i].lower() 
		
	for words in tokens:
		comment_words = comment_words + words + ' '

unique_string=(" ").join(my_list)
wordcloud = WordCloud(width = 800, height = 800, 
				background_color ='white', 
				stopwords = stopwords, 
				min_font_size = 10).generate(unique_string) 

plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 
