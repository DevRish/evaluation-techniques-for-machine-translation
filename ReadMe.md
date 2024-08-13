## Study Of Evaluation Techniques For Machine Translation
In today's globally interconnected communication landscape, machine translation systems play an increasingly crucial role, facilitating cross-lingual interactions and overcoming language barriers. The efficacy of these automated translation systems hinges on the use of rigorous evaluation techniques capable of accurately assessing their quality and precision. This study explores the intricate realm of evaluating machine translation, focusing on critically examining established metrics.

Although these metrics have propelled the field forward, their application presents challenges. Given the rising need for effective cross-lingual communication and the limitations of current evaluation methods, there's a clear necessity to refine and broaden our approach. The crux of the issue lies in the inability of existing metrics to fully encapsulate the nuances and complexities of human language.

This study aims to advance machine translation evaluation by meticulously analyzing the BLEU, METEOR, and BLEURT metrics. We closely examine their shortcomings in addressing linguistic complexities and propose two innovative evaluation techniques – the RTN-Method and SAA-Method – to address their limitations and provide a more comprehensive assessment of machine translation systems. 
## Review of pre-existing works
Previous studies have extensively explored the efficacy and limitations of machine translation evaluation metrics such as BLEU, METEOR, and BLEURT.
## RTN-Method
The RTN-Method or Recursive Tree-based N-gram method, recursively calculates the weighted precision and recall scores from lower-grams to the higher-grams in a bottom-up approach. It also implements lemmatization for fairer evaluation.
## SAA-Method
The SAA Model or Semantic Assignment and Alignment Model solves the classic assignment problem between the words from the reference sentence and the candidate sentence and finds an optimal pairing of words such that the difference in their meanings is minimized, while also minimizing the positional differences and information disparity.
## References
[1] Satanjeev Banerjee and Alon Lavie. METEOR: An automatic metric for MT evaluation with improved correlation with human judgments. In Jade Goldstein, Alon Lavie, Chin-Yew Lin, and Clare Voss, editors, Proceedings of the ACL Workshop on Intrinsic and Extrinsic Evaluation Measures for Machine Translation and/or Summarization, pages 65–72, Ann Arbor, Michigan, June 2005. Association for Computational Linguistics.
[2] Matthew Honnibal, Ines Montani, Sofie Van Landeghem, and Adriane Boyd.spaCy: Industrial-strength Natural Language Processing in Python. 2020.
[3] Armand Joulin, Edouard Grave, Piotr Bojanowski, and Tomas Mikolov. Bag of tricks for efficient text classification. arXiv preprint arXiv:1607.01759, 2016.
[4] Edward Loper and Steven Bird. Nltk: The natural language toolkit, 2002.
[5] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781, 2013.
[6] Tomas Mikolov, Quoc V Le, and Ilya Sutskever. Exploiting similarities among languages for machine translation. arXiv preprint arXiv:1309.4168, 2013.
[7] Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic evaluation of machine translation. In Pierre Isabelle, Eugene Charniak, and Dekang Lin, editors,
Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics pages 311–318, Philadelphia, Pennsylvania, USA, July 2002. Association for Computational Linguistics.
[8] Jeffrey Pennington, Richard Socher, and Christopher D Manning. Glove: Global vectors for word representation. In Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pages 1532–1543, 2014.
[9] Neha Rai and A.J. Khan. A brief review on classic assignment problem and its applications. IOSR Journal of Engineering, 9, 2019.
[10] Thibault Sellam, Dipanjan Das, and Ankur Parikh. BLEURT: Learning robust metrics for text generation. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 7881–7892, Online, July 2020. Association for Computational Linguistics.
