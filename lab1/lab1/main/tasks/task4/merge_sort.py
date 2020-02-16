class MergeSort:
    def __init__(self, array):
        self.__array = array
        self.__INFINITY = 2e9

    def sort(self):
        if len(self.__array) == 0:
            return self.__array

        self.__merge_sort(0, len(self.__array))
        return self.__array

    def __merge_sort(self, left_border, right_border):
        if right_border - left_border <= 1:
            return
        else:
            m = left_border + (right_border - left_border) // 2
            self.__merge_sort(left_border, m)
            self.__merge_sort(m, right_border)
            self.__merge(left_border, m, right_border)

    def __merge(self, left_border, second_array_start, right_border):

        left_array = list(self.__array[left_border:second_array_start])
        right_array = list(self.__array[second_array_start:right_border])
        left_array.append(self.__INFINITY)
        right_array.append(self.__INFINITY)

        left_array_pointer = 0
        right_array_pointer = 0
        array_position = left_border

        for _ in range(right_border - left_border):
            if left_array[left_array_pointer] < right_array[right_array_pointer]:
                self.__array[array_position] = left_array[left_array_pointer]
                array_position += 1
                left_array_pointer += 1
            else:
                self.__array[array_position] = right_array[right_array_pointer]
                array_position += 1
                right_array_pointer += 1

        return

