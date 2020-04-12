from collections import Counter
from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
  

        groupedWords = defaultdict(list) 

        # Put all anagram words together in a dictionary  
        # where key is sorted word 
        for word in strs: 
            groupedWords["".join(sorted(word))].append(word) 

        # Print all anagrams together 
        return(list(groupedWords.values())) 
              
