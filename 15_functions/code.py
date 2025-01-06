def hello():
    print("Hello!")

hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_in_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is: {age_in_seconds}")

print("Welcome to the age in seconds program!")

user_age_in_seconds()

print("Goodbye!")

# don't do that!
# this overrides a python's native function
# def print():
#     print("Hello, world!")

# friends = ["Rolf", "Bob"]

# def add_friend():
#     friend_name = input("Enter you friend name: ")
#     # friends = friends + [friend_name] # error: python can't redefine 'friends' global variable in that way

# add_friend()