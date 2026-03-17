import sys
import re

def word_frequency(file_name,top_N):
    try:
        with open(file_name,'r',encoding='utf-8') as file:
            text=file.read()
        
        words=text.split()
        word_freq={}
        for word in words:
            word=re.sub(r'[^\w\s]','',word).lower()


            if word in word_freq:
                word_freq[word]+=1
            else:
                word_freq[word]=1
        sorted_words=sorted(word_freq.items(),key=lambda x:x[1],reverse=True)

        for i,(word,freq) in enumerate(sorted_words[:top_N],1):
            print(f"{i}. {word}--{freq}")
    except Exception as e:
        print("error")

if __name__ == "__main__":
        if len(sys.argv)!=3:
            print("Useage:pyton script.py<filr_name><top_N>")
        else:
            file_name=sys.argv[1]
            try:
                top_N=int(sys.argv[2])
                if top_N<1:
                    print("Top_N must be a positive number")
                else:
                    word_frequency(file_name,top_N)
            except ValueError:
                print("top_N must be an integeer")