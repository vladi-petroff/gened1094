## Overview

This is the final project for GENED 1091: Classical Chinese Ethical and Political Theory by Vladimir Petrov and Zad Chin. 
Brief overview:

## Data

1) 'data/analects_src.txt' and 'data/mozi_long.txt' are original texts (in English)
'data/mozi_short.txt' is the text we extracted from readings (quite messy) and it's shorter 

2) 'data/analects_frmt.txt' and 'data/mozi_frmt.txt' are texts obtained by function clean_text() in main.py
I deleted all '\n', leaving only letters and punctuation


3) Function count_analysis counts frequencies of "essential" words:  
   - we first delete "common" words such as "with", "and", "no"
   - we then gather words in group accordint to common roots (e.g. friend and friendship)
   - finally we output the most frequent groups
   
   We call this function in the main on both text for Mozi and Confucius
   
  
 4) In main you can also find pdf parser in case you would like to apply clusterization to other authors or some specific selected sections of Confucius/Mozi.
 That's implemented with extract_text_from_pdf function, where you pass the range of pages being used. 
 You can use readings.pdf as a source file (this is the book we read during the class).


## Code

1) main.py is a codefile we use to clean out source text we found online.

2) text analysis.ipynb is a Python Notebook that details the language analysis of Confucius and Mozi texts.

3) quote_generation.ipynb is a Python notebook that generates quotes based on training from the texts on GPT-2.