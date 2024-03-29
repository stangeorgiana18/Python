# interactive program short lectures exercises

# displaying information
# combine a custom using a def call with the print function

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

example_row = [1, 2, 3]
display(example_row, example_row, example_row)

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

display(row1, row2, row3)
row2[1] = 'X'
display(row1, row2, row3)


# accepting user input

result = input("enter a value: ")
print(result)
print(type(result))


position_index = int(input('choose an index pos: '))
print(type(position_index))
print('\n')


# validating user input 

# python can convert "two" into an integer directly

def user_choice():

    choice = 'wrong'

    while choice.isdigit() == False:
        choice = input("enter a number (0-10): ")

        if choice.isdigit() == False:
            print('this is not a digit!')
    
    return int(choice)

some_value = '100'
print(some_value.isdigit())
print(int(some_value))

print(user_choice(), '\n')
result = 'wrong value'

acceptable_values = [0, 1, 2]
print(result in acceptable_values, '\n')


print('user_choice function:')

def user_choice():
    
    # variables

    # inital
    choice = 'wrong'
    acceptable_range = range(0, 10) 
    within_range = False

    # two conditions to check
    # digit or within_range == False

    # isdigit() returns True if all characters in the string are digits
    while not choice.isdigit() or not within_range:
        
        choice = input("enter a number (0-10): ")

        # digit check
        if not choice.isdigit() or (choice.startswith('0') and len(choice) > 1): # not accept 001 for eg
            print('this is not a digit!')
            continue

        # range check
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = True
            else: 
                print('you are out of the acceptable range')
                pass # within_range = False

    return int(choice)

user_choice()