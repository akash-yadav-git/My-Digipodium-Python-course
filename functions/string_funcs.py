from string import punctuation

from wcwidth import wcswidth

def remove_punc(text):
    print()
    '''
    removes punctuation from a text and return cleaned text

    '''
    for punc in punctuation:
        text =text.replace(punc,'')
    return text
def word_count(text):
    wordlist=text.lower().split()
    wc={}
    for word in wc:
        wc[word]+=1
    else:
        wc[word]=1
    return wc

def sort(word_dict):
    ans=sorted(word_dict.items(),key=lambda val: val[1], reverse=True)
    return dict(ans) # convert list to dict


if __name__=='__main__':
    long_text='''
    the quick brown fox jumps over the lazy dog,
    and attaks the chicken with a flying kick.
    this is real time story about a fox , that could
    kick and jump
    '''
    cl_text=remove_punc(long_text)
    counted_word =word_count(cl_text)
    print(counted_word)