def acronym(*words):
    for words in words:
        
        yield ''.join([i[0].upper() for i in word.split()])

    for item in acronym('Project Manager','Software Engineer','Data Analyst'):
        print(item)

print(list(acronym('Progect Manager','Software Engineer','Dta Analyst')))
