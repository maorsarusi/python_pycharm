from db import my_table_utils


class my_Table:
    def __init__(self, R, Demolitions):
        list_of_column_values = []
        list_of_row_values = []
        self.__R = R
        self.__Demolitions = Demolitions
        for i in R:
            list_of_column_values += [[]]
        self.__column_values = list_of_column_values
        for i in Demolitions:
            list_of_row_values += [[]]
        self.__row_values = list_of_row_values

    def get_column_values(self):
        return self.__column_values

    def get_row_values(self):
        return self.__row_values

    def get_R_list(self):
        list_of_R = []
        for letter in self.__R:
            list_of_R += letter
        return list_of_R

    def get_demolitions(self):
        return self.__Demolitions

    def set_columns_values(self, column_values):
        self.__column_values = column_values

    def set_one_column(self, col, num):
        col_values = self.get_column_values()
        col_values[num] = col
        self.set_columns_values(col_values)

    def set_row_values(self, row_values):
        self.__row_values = row_values

    def check_losses(self):
        rows = self.get_row_values()
        for line in rows:
            if my_table_utils.check_a(line):
                return "There are'nt any losses"
        return "There are a losses"

    def insert_values(self):
        R = self.get_R_list()
        demolition = self.get_demolitions()
        column_values = self.get_column_values()
        row_values = self.get_row_values()

        for i in range(len(R)):
            for j in range(len(demolition)):
                if R[i] in demolition[j]:
                    column_values[i] += ["a{}".format(i + 1)]
                else:
                    column_values[i] += ["b{},{}".format(j + 1, i + 1)]
        self.set_columns_values(column_values)

        row_values = my_table_utils.from_column_to_row(column_values, row_values)
        self.set_row_values(row_values)

    def chase_table(self, dependencies):
        list_of_num = [[], []]
        for i in range(len(dependencies)):
            for j in range(len(dependencies[i])):
                list_of_num[i] += [my_table_utils.find_places(dependencies[i][j], self.get_R_list())]
        incerments = my_table_utils.create_incerments(self.get_column_values(), list_of_num)
        for j in list_of_num[0]:
            for i in range(len(incerments[0])):
                my_table_utils.insert_new_values(self, incerments[0][i], incerments[1][i], list_of_num[1][i])
                incerments = my_table_utils.create_incerments(self.get_column_values(), list_of_num)
        print("Table after chase table")
        self.print_table()
        return self.check_losses()

    def print_table(self):
        demolitions = self.get_demolitions()
        print("    {}".format(self.get_R_list()))
        for i in range(len(demolitions)):
            print("{}  {}".format(demolitions[i], self.get_row_values()[i]))


def main():
    T = my_Table("abcd", ["ad", "bd", "ac"])
    T.insert_values()
    print("Table after initialize values:")
    T.print_table()
    print(T.check_losses())
    print()
    demolitions = [["c", "d", "a", "ad"], ["b", "c", "c", "c"]]
    print(T.chase_table(demolitions))


if __name__ == "__main__":
    main()
