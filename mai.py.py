from pyscript import document, display

def signup(e):
    document.getElementById("result").innerHTML = "" #clears the output
    username = len(document.getElementById("username").value)
    password = document.getElementById("password").value
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    password_ch= len(document.getElementById("password").value)

    if username >=7: #checks if the username has enough characters
        if has_letter and has_number and password_ch >= 10: #checks if the password has all the requirments
           display("Account Created!", target="result")
        elif password_ch <10: #if the password doesnt have sufficient letters
            display("Please enter a 10 character password.", target="result")
        else: #if theres a digit or letter missing
            display("Please try again!", target="result")
    else:
        display("Make sure that your username contains atleast 7 characters.", target="result")