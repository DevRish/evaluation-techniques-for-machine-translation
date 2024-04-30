# Recursive Tree N-Gram Method

Download all the 3 python files in the same folder and run "main.py". <br/>
"POS.py" is used for parts-of-speech tagging and weight assignment to each word. <br/>
"Stemmer.py" is used for lemmatization of the words. The corresponding partial score assigned to matching lemmas is given in "main.py". <br/>
Since RTN is a recursion based algorithm it might take some time to finish execution if the given corpus is too long. <br/>
Some of the sentences on which the scoring was tested are already provided in the "main.py". To test scoring on manually given input, comment out all those sentences and print statements and uncomment lines 305, 306 and 338.
