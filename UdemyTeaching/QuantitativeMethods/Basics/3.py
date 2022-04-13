'''
Multiplication_Table_For_a_Range.py
Multiplication table printer for elementary school
'''
def multi_table(a, b):
    for k in range(a, b+1):
        print('----------------------------------------')
        for i in range(1, 11):
            print('{0} x {1} = {2}'.format(k, i, k*i))

if __name__ == '__main__':
    print(__doc__)
    while True:
        try:
            a = int(input('Enter a Range Start: For Example 4 '))
            b = int(input('Enter a Range End: For Example 14 '))
            multi_table(a, b)
            answer = input('Do you want to exit? (y) for yes ')
            if answer == 'y':
                    break
        except ValueError:
                print('Incorrect value entered')