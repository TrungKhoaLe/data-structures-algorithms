from typing import List


class QuickSort:
    def quick_sort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        # choosing a pivot element
        pivot = arr[len(arr) // 2]

        smaller_elements = [x for x in arr if x < pivot]
        equal_elements = [x for x in arr if x == pivot]
        greater_elements = [x for x in arr if x > pivot]

        return self.quick_sort(smaller_elements) + \
               equal_elements + self.quick_sort(greater_elements)


if __name__ == "__main__":
    nums = [5, 2, 8, 12, 3]
    sorter = QuickSort()
    print(sorter.quick_sort(nums))
