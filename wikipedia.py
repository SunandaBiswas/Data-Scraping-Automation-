
!pip install wikipedia


import wikipedia

print("Welcome to wikipedia")

while True:
    ques = input("Ask a question please?")
    wikipedia.set_lang("en") #change "en" to convenient language for example wikipedia.set_lang("es") will set the language to spanish
    print (wikipedia.summary(ques, sentences=3))
