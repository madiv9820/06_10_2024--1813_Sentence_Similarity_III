class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        This function checks if two sentences are similar. A sentence is considered similar to another
        if it can be obtained by inserting some words into the other sentence.
        """

        # Split sentences into lists of words
        words_In_Sentence1 = sentence1.split()
        words_In_Sentence2 = sentence2.split()

        # Ensure words_In_Sentence1 is the shorter one
        if len(words_In_Sentence2) < len(words_In_Sentence1):
            words_In_Sentence1, words_In_Sentence2 = words_In_Sentence2, words_In_Sentence1

        # Remove matching words from the beginning of both sentences
        while words_In_Sentence1 and words_In_Sentence1[0] == words_In_Sentence2[0]:
            words_In_Sentence1.pop(0)
            words_In_Sentence2.pop(0)

        # Remove matching words from the end of both sentences
        while words_In_Sentence2 and words_In_Sentence1 and words_In_Sentence1[-1] == words_In_Sentence2[-1]:
            words_In_Sentence1.pop()
            words_In_Sentence2.pop()

        # Return True if all words in words_In_Sentence1 have been matched
        return not words_In_Sentence1

# Time Complexity: O(n + m)
# The algorithm iterates through both sentences, where n and m are the number of words in each sentence.

# Space Complexity: O(n + m)
# The space used is mainly for storing the split words from both sentences, which requires O(n + m) space.