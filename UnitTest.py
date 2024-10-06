from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {'sentence1': "My name is Haley", 'sentence2': "My Haley", 'output': True},
            2: {'sentence1': "of", 'sentence2': "A lot of words", 'output': False},
            3: {'sentence1': "Eating right now", 'sentence2': "Eating", 'output': True}
        }

        self.__obj = Solution()

        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        sentence1, sentence2, output = self.__testCases[1].values()
        result = self.__obj.areSentencesSimilar(sentence1, sentence2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        sentence1, sentence2, output = self.__testCases[2].values()
        result = self.__obj.areSentencesSimilar(sentence1, sentence2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        sentence1, sentence2, output = self.__testCases[3].values()
        result = self.__obj.areSentencesSimilar(sentence1, sentence2)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()