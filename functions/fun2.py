
def vowel_counter(sentence):
    
    result={} # creat a dictionary

    for vowel in "aeiou":
        result[vowel]=sentence.lower().count(vowel)
    return result

if _name_=="_main_":
    msg="this is a test"
    print(vowel_counter(msg))