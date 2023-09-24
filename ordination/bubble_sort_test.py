import unittest
from bubble_sort import BubbleSort

class BubbleSortTest(unittest.TestCase):
    def setUp(self) -> None:
        self.bubbleSort = BubbleSort()

    def test_execute(self) -> None:
        aleatoryNumbers = [5, 18, 10, 16, 49, 82, 43, 12 ]
        orderedNumbers = [ 5, 10, 12, 16, 18, 43, 49, 82 ]
        resultArray = self.bubbleSort.execute(aleatoryNumbers)
        self.assertListEqual(orderedNumbers, resultArray, "Should return the ordered numbers")

    def test_execute_with_repeated_elements(self) -> None:
        aleatoryNumbers = [5, 18, 10, 49, 16, 49, 10, 82, 43, 12 ]
        orderedNumbers = [ 5, 10, 10, 12, 16, 18, 43, 49, 49, 82 ]
        resultArray = self.bubbleSort.execute(aleatoryNumbers)
        self.assertListEqual(orderedNumbers, resultArray, "Should return the ordered numbers")

if __name__ == "__main__":
    unittest.main()