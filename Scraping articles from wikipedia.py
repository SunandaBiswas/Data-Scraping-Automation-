##  **Scraping Articles from Wikipedia**

## To scrape a Wikipedia page,the page method has been used from the wikipedia module. The name of the page that is for scrapping purpose is passed as a parameter to the page method.
## The method returns WikipediaPage object, that is used to retrieve the page contents via the content attribute.



artificial_intelligence = wikipedia.page("Artificial Intelligence").content
deep_learning = wikipedia.page("Deep Learning").content
neural_network = wikipedia.page("Neural Network").content

### tokenized scraped text data into sentences using the sent_tokenize method.
artificial_intelligence = sent_tokenize(artificial_intelligence)
deep_learning = sent_tokenize(deep_learning)
neural_network = sent_tokenize(neural_network)

### sentences from the three articles are being joined here together via the extend method.
artificial_intelligence.extend(deep_learning)
artificial_intelligence.extend(neural_network)
