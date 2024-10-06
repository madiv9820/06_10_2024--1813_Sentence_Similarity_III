# 1813. Sentence Similarity III

__Type:__ Medium <br>
__Topics:__ Array, Two Pointers, String <br>
__Companies:__ Google, Amazon <br>
__Leetcode Link:__ [Sentence Similarity III](https://leetcode.com/problems/sentence-similarity-iii/description/)
<hr>

### Question

You are given two strings `sentence1` and `sentence2`, each representing a __sentence__ composed of words. A sentence is a list of __words__ that are separated by a __single__ space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences `s1` and `s2` are considered __similar__ if it is possible to insert an arbitrary sentence _(possibly empty)_ inside one of these sentences such that the two sentences become equal. __Note__ that the inserted sentence must be separated from existing words by spaces.

For example,

- `s1 = "Hello Jane"` and `s2 = "Hello my name is Jane"` can be made equal by inserting "`my name is"` between `"Hello"` and `"Jane"` in `s1`.
- `s1 = "Frog cool"` and `s2 = "Frogs are cool"` are __not__ similar, since although there is a sentence `"s are"` inserted into `s1`, it is not separated from `"Frog"` by a space.

Given two sentences `sentence1` and `sentence2`, return __true__ if `sentence1` and `sentence2` are __similar__. Otherwise, return __false__.
<hr>

### Examples

__Example 1:__

__Input:__ sentence1 = "My name is Haley", sentence2 = "My Haley" <br>
__Output:__ true <br>
__Explanation:__ <br>
sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".

__Example 2:__

__Input:__ sentence1 = "of", sentence2 = "A lot of words" <br>
__Output:__ false <br>
__Explanation:__ <br>
No single sentence can be inserted inside one of the sentences to make it equal to the other.

__Example 3:__

__Input:__ sentence1 = "Eating right now", sentence2 = "Eating" <br>
__Output:__ true <br>
__Explanation:__ <br>
sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
<hr>

### Constraints:

- `1 <= sentence1.length, sentence2.length <= 100`
- `sentence1` and `sentence2` consist of lowercase and uppercase English letters and spaces.
- The words in `sentence1` and `sentence2` are separated by a single space.
<hr>

### Hints:
- One way to look at it is to find one sentence as a concatenation of a prefix and suffix from the other sentence.
- Get the longest common prefix between them and the longest common suffix.