from PyPDF2 import PdfFileReader, PdfFileWriter
import re

from nltk.stem import WordNetLemmatizer, PorterStemmer, SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

####################################
#WORKING WITH PDF
def extract_text_from_pdf(file_path, pages = (0, 10), file_out = "result"):
    """
    Takes PDF file as input and extract all possible text (into txt format)
    Example (extracting Mozi): mozi_range = (77, 128), mozi_path = 'reading_src.pdf'
    result = extract_text_from_pdf(mozi_path, mozi_range, 'mozi_res.txt')
    """
    pdf = PdfFileReader(file_path)
    with open(file_out, 'w') as f:
        for page_num in range(pages[0], pages[1]):
            pageObj = pdf.getPage(page_num)
            try:
                txt = pageObj.extractText()
                print(''.center(100, '-'))
            except:
                pass
            else:
                f.write('Page {0}\n'.format(page_num+1))
                f.write(''.center(100, '-'))
                f.write(txt)
        f.close()


####################################
# CLEANING TXT FILE
def clean_text(file_path, out_path):
    """
    :param file_path: source file
    :param out_path: output file
    :return: deletes all '\n', remains only letters and punctuation
    """

    data = open(file_path).read()
    lines = data.lower().split('\n')

    with open(out_path, 'w') as out:
        for l in lines:
            letters_only_text = re.sub("[^a-zA-Z,.?!]", " ", l)
            if len(letters_only_text) > 2:
                out.write(letters_only_text + '\n')
                
            

####################################
#TRIVIAL TEXT ANALYSIS (WORD COUNT):

stop_words_file = 'data/stoplist_long.txt'
stop_words = []
with open(stop_words_file, "r") as f:
    for line in f:
        stop_words.extend(line.split()) 


def preprocess(raw_text):
    #regular expression keeping only letters 
    letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

    # convert to lower case and split into words -> convert string into list ( 'hello world' -> ['hello', 'world'])
    words = letters_only_text.lower().split()
    cleaned_words = []
    lemmatizer = PorterStemmer() #plug in here any other stemmer or lemmatiser you want to try out
    
    # remove stopwords
    for word in words:
        if word not in stop_words:
            cleaned_words.append(word)
    
    # stemm or lemmatise words
    stemmed_words = []
    for word in cleaned_words:
        word = lemmatizer.stem(word)   #dont forget to change stem to lemmatize if you are using a lemmatizer
        stemmed_words.append(word)
    
    # converting list back to string
    return " ".join(stemmed_words)


def count_analysis(file_path, limit = 20):

    with open(file_path, 'r') as file:
        text = file.read().replace('\n', '')
    
    cleaned = preprocess(text)
    ans = [(word, val) for word, val in Counter(cleaned.split()).most_common(limit)]
    return ans



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_conf, file_mozi = 'data/conf_frmt.txt', 'data/mozi_frmt.txt'
    
    conf_dic, mozi_dic = count_analysis(file_conf), count_analysis(file_mozi)
    print(conf_dic)
    print(mozi_dic)
