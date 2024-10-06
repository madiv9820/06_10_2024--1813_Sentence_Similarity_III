class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        This function checks if two sentences are similar. A sentence is considered similar to another
        if it can be obtained by inserting some words into the other sentence. The function returns True
        if the sentences are similar, and False otherwise.
        """

        # Ensure sentence1 is the shorter one
        if len(sentence2) < len(sentence1):
            sentence1, sentence2 = sentence2, sentence1

        # Initialize variables to count inserted sentences and to build the generated string
        no_of_Sentences_Inserted = 0
        string_Generated = ''

        # Split sentences into lists of words
        words_In_Sentence1 = sentence1.split()
        words_In_Sentence2 = sentence2.split()
        
        # Get the number of words in each sentence
        no_of_Words_In_Sentence1 = len(words_In_Sentence1)
        no_of_Words_In_Sentence2 = len(words_In_Sentence2)

        # Initialize pointers for both word lists
        ptr1, ptr2 = 0, 0

        # Loop through both sentences as long as there are words in both
        while ptr1 < no_of_Words_In_Sentence1 and ptr2 < no_of_Words_In_Sentence2:
            # If the words match, add to the generated string and move both pointers
            if words_In_Sentence1[ptr1] == words_In_Sentence2[ptr2]:
                string_Generated += (words_In_Sentence1[ptr1] + ' ')
                ptr1 += 1
                ptr2 += 1
            else:
                # If words don't match, add words from sentence2 until we find a match
                while ptr2 < no_of_Words_In_Sentence2 and words_In_Sentence2[ptr2] != words_In_Sentence1[ptr1]:
                    string_Generated += (words_In_Sentence2[ptr2] + ' ')
                    ptr2 += 1

                # Increment the count of inserted sentences
                no_of_Sentences_Inserted += 1

        # Add remaining unmatched words from sentence1 to the generated string
        while ptr1 < no_of_Words_In_Sentence1:
            string_Generated += (words_In_Sentence1[ptr1] + ' ')
            ptr1 += 1

        # If there are still unmatched words in sentence2, add them to the generated string
        if ptr2 < no_of_Words_In_Sentence2:
            while ptr2 < no_of_Words_In_Sentence2:
                string_Generated += (words_In_Sentence2[ptr2] + ' ')
                ptr2 += 1
            
            # Increment the count of inserted sentences
            no_of_Sentences_Inserted += 1

        # Remove trailing space from the generated string
        string_Generated = string_Generated[:-1]
        
        # Check if the number of inserted sentences is less than 2 and the generated string matches sentence2
        if no_of_Sentences_Inserted < 2 and string_Generated == sentence2:
            return True
        
        return False

# Test Case: This will fail
sentence1 = "A"
sentence2 = "a A b A"
solution = Solution()
print(solution.areSentencesSimilar(sentence1, sentence2))  # Expected output: True, but will return False

# Time Complexity: O(n + m)
# The algorithm iterates through both sentences, where n and m are the number of words in each sentence.

# Space Complexity: O(n + m)
# The space used is mainly for storing the split words from both sentences, which requires O(n + m) space.