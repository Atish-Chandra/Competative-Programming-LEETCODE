''' VALID ANAGRAM
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false  */

/* APPROACH
If the lengths of the two strings s and t are different, they cannot be anagrams, so we return false immediately.
If the lengths are the same, we can count the frequency of each character in both strings. If the frequency of each character matches in both strings, 
they are anagrams; otherwise, they are not.

Step 1: We check if the lengths of s and t are the same. If they are different, the two strings can't be anagrams, so we return False.

Step 2: We create two dictionaries count_s and count_t to store the frequency of each character in s and t, respectively. The get(char, 0) method allows us to handle characters that are not yet in the dictionary, initializing their count to 0.

Step 3: Finally, we compare the two dictionaries. If they are the same, the strings are anagrams, so we return True. Otherwise, we return False.
 '''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
        return False
    
    count_s = {}
    count_t = {}
    
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1
    
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
        return count_s == count_t

'''
Example Walkthrough:

Suppose the string s = "anagram":

1) Initially, the dictionary count_s is empty: {}.
2) When we encounter the first character 'a', the dictionary becomes:
count_s.get('a', 0) returns 0 (since 'a' is not in the dictionary yet), and then 0 + 1 = 1. So we add 'a': 1 to count_s.
count_s now is: {'a': 1}.
3) The next character 'n' is new, so:
count_s.get('n', 0) returns 0, and then 0 + 1 = 1. We add 'n': 1.
count_s is now: {'a': 1, 'n': 1}.
4) When we encounter 'a' again, we increment its count:
count_s.get('a', 0) returns 1 (since 'a' is already in the dictionary), and then 1 + 1 = 2. We update 'a': 2.
count_s becomes: {'a': 2, 'n': 1}.

Example 1:
s = "anagram", t = "nagaram"
Character frequencies:
s: {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}
t: {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
The frequencies match, so we return True.  
'''

