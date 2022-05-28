# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

word_count = {}
word_list = ()

def read_file_content(file):
    # [assignment] Add your code here 
        text = open(file) 
        for word in text:
           word_list.append(word)
           return word_list


def count_words():
    #text = read_file_content("../Read me/story.txt")
    # [assignment] Add your code here
    text = '''Once upon a time a psychology professor walked around on a stage while teaching stress management principles to an auditorium filled with students.  
As she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question.  
Instead, with a smile on her face, the professor asked, How heavy is this glass of water I am holding?'''
    text = text.split()
    for word in text:
        if word not in word_count:
            word_count[word] = 1

        else:
            word_count[word]+=1
    return word_count

print(count_words())