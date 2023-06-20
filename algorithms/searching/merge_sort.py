from typing import List, Callable


class MergeSort:
    def merge_sort(self, arr: List[int]) -> Callable:
        if len(arr) <= 1:
            return arr

        # divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print("[INFO] Merge sort function's operations")
        print(f"Left half: {left_half}")
        print(f"Right half: {right_half}")

        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        return self.merge(left_half, right_half)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged = []
        left_index = 0
        right_index = 0
        
        print("[INFO] Merge function's operations")
        print(f"Left: {left}")
        print(f"Right: {right}")

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # append any remaining elements from the left half
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        # append any remaining elements from the right half
        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1
        print(f"Left after: {left}")
        print(f"Right after: {right}")
        print(f"Merge: {merged}")
        return merged


if __name__ == '__main__':
    nums = [70, 50, 30, 10, 20, 40, 60]
    merge_sorter = MergeSort()
    print(merge_sorter.merge_sort(nums))
