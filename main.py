from newspaper import Article

url = 'http://mitsui-mall.com/mit/event/event.seam?cid=4394&flashId=4277'
article = Article(url)
article.download()
print (article.summary)


