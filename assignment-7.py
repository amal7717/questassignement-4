# Assignment 7 - Logging Decorator

# Build a Python program using a custom login_required decorator to control access to different functions based onuser authentication.
#     Requirements:
# Create a login_required decorator that checks whether the user is logged in before allowing access to a function.
# Use the username “quest” and password “quest123” as the valid login credentials.
# Create a login function that accepts the username and password from the user.
# If the credentials are correct, display a login successful message and allow access to protected functions.
# Create functions such as Home, About, and Profile.
# Apply the login_required decorator only to functions that require authentication.
# A function without the login_required decorator should work normally without login.
# A function with the login_required decorator should not execute unless the user has successfully logged in.
# If an unauthenticated user tries to access a protected function, display an appropriate access denied/login required message.
# Demonstrate the difference between normal functions and decorator-protected functions.
# Use a menu-driven program to allow the user to access the available functions.

# username="quest"
# password="quest123"
# logged_in=False
# def login():
#     global logged_in
#     entname=input("enter username: ")
#     entpass=input("enter your password: ")
#     if username==entname and password==entpass:
#         logged_in=True
#         print("login success")
#     else:
#         print("invalid username and password")
# def login_requried(fun):
#     def wrapper():
#         if logged_in:
#             fun()
#         else:
#             print("acces denied,login first")
#     return wrapper
# def home():
#     print("welcome to home page")
# @login_requried
# def about():
#     print("welcome to about page")
# @login_requried
# def profile():
#     print("welcome to profile page")
# while True:
#     print("1.login")
#     print("2.home")
#     print("3.about")
#     print("4.profile")
#     print("5.exit")
#     choice=input("enter your choice: ")
#     if choice=="1":
#         login()
#     elif choice=="2":
#         home()
#     elif choice=="3":
#         about()
#     elif choice=="4":
#         profile()
#     elif choice=="5":
#         print("thank you")
#         break
#     else:
#         print("invalid choice")
