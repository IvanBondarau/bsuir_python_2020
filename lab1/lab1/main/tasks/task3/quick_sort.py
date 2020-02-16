class QuickSort:

    def __init__(self, array):
        self.__array = array

    def sort(self):
        if len(self.__array) == 0:
            return self.__array

        self.__sort(0, len(self.__array) - 1)
        return self.__array

    def __sort(self, left_border, right_border):
        median = self.__array[(left_border + right_border) // 2]
        i = left_border
        j = right_border
        while i < j:
            while self.__array[i] < median:
                i += 1
            while self.__array[j] > median:
                j -= 1

            if i <= j:
                x = self.__array[i]
                self.__array[i] = self.__array[j]
                self.__array[j] = x
                i += 1
                j -= 1

        if i < right_border:
            self.__sort(i, right_border)
        if left_border < j:
            self.__sort(left_border, j)

