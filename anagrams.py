# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
def find_anagrams(s1, s2):
    #the sorted strings are checked
    if(sorted(s1)== sorted(s2)):
        print("True")
    else:
        print("False")
find_anagrams("brainy", "binary")
