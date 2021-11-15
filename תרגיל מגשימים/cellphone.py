# a dictionary represents the cellphone
cellphone = {'2': "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def combinations(cellphone, numbers):
    """
    a function that returns the conbinations of thr letters in the cellphone buttons
    :param cellphone: s dictionary represents the cellphone
    :param numbers: the numbers we "pressed"
    :return: a list of combinations of the letters
    """

    # calculating the number of combinations
    length = len(cellphone[numbers[0]])
    for num in numbers[1:]:
        length *= len(cellphone[num])
    combinations_list = [""] * length
    place = 0 # represents the place in the string for each button
    jumping_count = 0
    for num in numbers:
        jumping = int(length / len(cellphone[num])) # represents the numbers of times we write the letter in row
        length = jumping
        for i in range(len(combinations_list)):
            combinations_list[i] += cellphone[num][place]
            jumping_count += 1
            if jumping_count == jumping: # checks if we wrote the much we need
                jumping_count = 0
                place += 1
                if place == len(cellphone[num]):# in case that the place is bigger than the number of letters in the button
                    place = 0
        place = 0
    return combinations_list


def main():
    numbers = input("Please insert numbers between 2-9:\n")
    for num in numbers:
        if num not in cellphone.keys():
            print("Invalid input\n")
            return
    print(combinations(cellphone, numbers))



if __name__ == '__main__':
    main()
