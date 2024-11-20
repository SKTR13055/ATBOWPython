#PRROGRAM ON COLLATZ SQUENCE AKA SIMPLEST IMPOSSIBLE MATH PROBLEM
def collatz(number):
        if(number % 2 == 0):
            return number // 2
        else:
            return 3 * number + 1
        
while True:
    try:
        number = int(input("Enter a number: "))
        if(number == 0):
            print('Exiting the program')
            break
        if(number < 0):
            print('Enter a positive integer')
            continue
        while number != 1:
                print(number)
                number = collatz(number)
        print(number)

    except ValueError:
        print('Error:Please enter a valid integer')


