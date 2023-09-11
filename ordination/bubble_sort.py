class BubbleSort:
    def execute(self, numbers: list) -> list:
        swapped = True
        while (swapped):
            swapped = False
            for firstIndex in range(0, len(numbers) - 1):
                secondIndex = firstIndex + 1
                if numbers[firstIndex] >= numbers[secondIndex]:
                    swapping = numbers[firstIndex]
                    numbers[firstIndex] = numbers[secondIndex]
                    numbers[secondIndex] = swapping
                    swapped = True
        return numbers