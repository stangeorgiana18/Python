def func():
    return 1

print(func())

# we can assign functions to other variables and then execute them off that variable

def hello():
    return "hello!"

#greet = hello

#print(greet(), '\n')

# did greet make its own copy of the hello function or just pointed to hello?
# test by deleting hello and see if we can still call greet

del hello

#print(greet())

# passing in a function within another function

def hello(name = "Geo"):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is a greet() function inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello.'
    
    print(greet())
    print(welcome())
    print("This is the end of the hello function!")


hello()

# calling functions within another function