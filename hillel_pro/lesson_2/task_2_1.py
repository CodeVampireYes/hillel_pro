def my_sum(*args):
    def sum():
        print('This is my custom sum function!')
    return sum()


numbers = [1, 2, 3, 4, 5]
print(sum(numbers))
my_sum(numbers)
print(sum(numbers))
