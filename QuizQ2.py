def main():
    num = 5
    numList = [1,2,3,4,5,6,7,8,9,10]

    print('Number:', num)
    print('List of numbers: ', numList, sep='')
    print('List of numbers that are larger than'," ",\
    num, ':', sep='')

    display_larger_than_n_list(num, numList)

def display_larger_than_n_list(n, n_list):
    larger_than_n_list = []
    for value in n_list:
        if value > n:
            print(value)
main()
