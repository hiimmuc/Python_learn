import random


def input_mat(rows, cols):
    print("Enter the matrix: ")
    matrix = [[0 for j in range(cols)] for i in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input(f"pos[{i + 1}][{j + 1}]: "))
    return matrix


def print_mat(mat, rows, cols):
    print("The matrix is : ")
    for i in range(rows):
        result = ""
        for j in range(cols):
            result += "{:4d}".format(mat[i][j])
        print(result)


def input_vector():
    print("input vector coordinates below: ")
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    z = int(input("enter z: "))
    coordinates = (x, y, z)
    return coordinates


def dot_product(vector1, vector2):
    result = [0 for i in range(len(vector1))]
    for i in range(len(vector1)):
        result[i] = vector1[i] * vector2[i]
    return result


def power_(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result = result * base_num
    return result


def max_number(list_of_number):
    return max(list_of_number)


def removing_duplicators(list_num):
    result = [list_num[0]]
    for i in list_num:
        if i not in result:
            result.append(i)
    return result
