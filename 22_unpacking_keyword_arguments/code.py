def named(**kwargs):
    print(kwargs) # {"name": "Bob", "age": 25}

named(name="Bob", age=25)

def named_separated(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named_separated(**details)

named(**details)

def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)