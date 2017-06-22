__author__ = 'Musimire'


def lone_sum(a,b,c):
    numbers = [a,b,c]
    sum_list = []

    for value in numbers:
        if numbers.count(value) == 1:
            sum_list.append(value)

    return sum(sum_list)








#
# if __name__ == "__main__":
#     print lone_sum(2,6,6)