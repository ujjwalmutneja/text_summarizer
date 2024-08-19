import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
from string import punctuation



Text="""Artificial Intelligence (AI) is revolutionizing various industries by enhancing efficiency and productivity. AI technologies, such as machine learning and deep learning, enable machines to learn from data and make decisions with minimal human intervention. This capability is transforming sectors like healthcare, finance, retail, and transportation.
In healthcare, AI is being used to predict disease outbreaks, assist in diagnosis, and personalize treatment plans. Financial institutions utilize AI to detect fraudulent activities, automate trading, and provide customer service through chatbots. Retailers leverage AI for inventory management, personalized marketing, and improving customer experiences. The transportation industry benefits from AI through autonomous vehicles, traffic management systems, and predictive maintenance of infrastructure.
Despite its advantages, AI also raises ethical concerns, including job displacement, privacy issues, and biases in decision-making. As AI continues to evolve, it is crucial to address these challenges to ensure the technology is used responsibly and equitably."""

def summarizer(rawdocs):
    stopwords=list(STOP_WORDS)
    #print(stopwords)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    #print(doc)
    tokens=[token.text for token in doc]
    #print(tokens)
    #word frequency
    word_freq={}
    for word in doc:
       if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
            word_freq[word.text]=1
        else:

            word_freq[word.text]+=1

    #print(word_freq)
    max_freq=max(word_freq.values())
    #print(max_freq)
    #normalised frequency
    for word in word_freq.keys():
     word_freq[word]=word_freq[word]/max_freq

    #print(word_freq)
    sent_tokens=[sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores={}
    for sent in sent_tokens:  
     for word in sent:

        if word.text in word_freq.keys():
            if sent not in sent_scores.keys():
                sent_scores[sent]=word_freq[word.text]
            else:
                sent_scores[sent]+=word_freq[word.text]
                
    #kitna precent  length chheya
    select_len=int(len(sent_tokens)*0.3)
    #print(select_len)
    #jonsa 2 senetences ki higher frequency unko put karo as select_len ka ans 2 ha
    summary = nlargest(select_len , sent_scores, key = sent_scores.get)
    #print(summary)
    #it is a list comprehension. It iterates over each element (word) in the summary iterable and extracts the text attribute from each word. The resulting list of text strings is stored in final_summary.
    final_summary=[word.text for word in summary]
    #akes the list of text strings (final_summary) and joins them into a single string, with each word separated by a space (' '). The resulting single string is stored back in the variable summary.
    summary=' '.join(final_summary)
    #print(Text)
    #print("length of orignal text" ,len(Text.split(' ')))
    #print(summary)
    #print("length of summary text" ,len(summary.split(' ')))
    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))
  


# Import libraries: Necessary tools for NLP and data handling.
# Define the function: summarizer to process and summarize text.
# Convert stop words: Prepare stop words for filtering.
# Load model and process text: Tokenize and analyze the text with spaCy.
# Tokenize text: Extract individual words.
# Calculate word frequencies: Count how often each word appears.
# Normalize frequencies: Adjust word frequencies to a 0-1 range.
# Score sentences: Calculate a score for each sentence based on word frequencies.
# Select top sentences: Choose the most relevant sentences for the summary.
# Finalize summary: Create a string from the selected sentences.
# Return results: Provide the summary and other details.

