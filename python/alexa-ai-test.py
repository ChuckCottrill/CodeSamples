
'''
Prompt:
A circular definition is one that uses the term being defined as part of the definition.
For example, define 

“oak” : “a tree that grows from an acorn” 
“acorn” : “the nut produced by an oak tree”. 
acorn = nut, produced, oak-tree

acorn -> nut -> oak -> acorn
acorn -> tree -> nut -> oak -> acorn

Task: Given a dictionary, identify all of the circular definitions.
'''

non_important = [ 'the', 'a', 'an' ] #etc

def extract_important_words(definition):
    # define function...
    words = definition.split('')
    words = remove_articles(words)
    words = remove_unimportant(ewords)
    return words # ['nut', 'produce', 'oak', 'tree']

# (word, defintion)\
# definition = list(words)
# dictionary = list(words)
# for every word in dictionary:
def find_path(dictionary,root,path):
    frontier = extract_important_words(dicgtionary[word]) #firest level
    for element in frontier:
        if element == root:
            return path # match
        nextpath = copy(path)
        path.append(find_path(dictionary,root,nextpath))
    return []

def find_circular(dictionary,word):
    frontier = extract_important_words(dicgtionary[word]) #firest level
    for element in frontier:
        path = []
        if element == root:
            return [word]
        found = find_path(dictionary,root,path)
        if len(found) > 0:
            print("found", found.join('->'))

def find_all_circular(dictionary):
    for word,_ in dictionary:
        found = find_circular(dictionary,word)
        if len(found) > 0:
            circular[word] = found

# 1. ['oak -> acorn -> oak']
# 2. number of circular definitions



