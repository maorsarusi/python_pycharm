__author__ = "Maor"

# two strings to save the file names
# הערה:הקובץ המועתק אינו קיים בתיקייה והוא נולד רק עם הרצת התכנית
EXISTSFILE = "origin_file.txt"
COPYFILE = "copy_file.txt"


def copy_files(file):
    """
    function copy_files gets a file and copy it to another file
    :param file: string with all the things in the file
    :return: if the copy succeed
    """
    with open(COPYFILE, 'w') as f:
        f.write(file)
    return "copied"


def get_file():
    """
    function get_file open the origin file
    :return: string with the text in the origin file
    """
    file_list = ""
    with open(EXISTSFILE, 'r') as file:
        for i in file:
            file_list += i
    return file_list


def check_copy(string1, string2):
    """
    function check copy gets two strings and checks if they equals
    :param string1: first string
    :param string2: second string
    :return: True if they equals and False if they didn't
    """
    if string1 == string2:
        return True
    return False


def main():
    # asserts for check_copy function
    assert check_copy("abcd", "abcd") is True
    assert check_copy("", "") is True
    assert check_copy("", "a") is False

    file_list = get_file()
    print(copy_files(file_list))

    # checks if the file are equals
    file1_string = ""
    with open(EXISTSFILE, 'r') as file1:
        for i in file1:
            file1_string += i

    file2_string = ""
    with open(COPYFILE, 'r') as file2:
        for i in file2:
            file2_string += i

    if check_copy(file1_string, file2_string):
        print("succcess\n")
    else:
        print("fail\n")


if __name__ == '__main__':
    main()
