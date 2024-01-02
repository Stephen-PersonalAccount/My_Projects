from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- SEARCH FOR PASSWORD ------------------------------ #


def search_details():
    """This looks through the JSON file to fetch a user detail based on the searched keyword"""
    searched_web = website_text_box.get()
    if len(searched_web) == 0:
        messagebox.showerror(title="Error", message="No data found")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            """This catches the FileNotFoundError if the file doesn't exist or is the first time running this program"""
            messagebox.showerror(title="Error", message="No Data File Found")
        else:
            if searched_web in data:
                user_email = data[searched_web]["email"]
                user_password = data[searched_web]["password"]
                messagebox.showinfo(title=searched_web, message=f"Email: {user_email} "
                                                                f"\nPassword: {user_password}")
            else:
                messagebox.showerror(title="Error", message=f"No details for {searched_web.upper()} found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    """This generates a random password when the generate password is pushed or clicked"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]

    shuffle(password_list)

    new_password = "".join(password_list)
    password_text_box.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """This collates all user data from the input filed and saves them to a JSON file.
    It also confirms that no text filed is left empty when the add button is pushed"""
    website = website_text_box.get()
    email = email_or_username_text_box.get()
    pass_generated = password_text_box.get()
    # Checks if the user have entered data in the input boxes
    if len(website) == 0 or len(email) < 4 or len(pass_generated) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        new_data = {
            website: {
                "email": email,
                "password": pass_generated
            }
        }
        #  The messagebox.askokcancel returns a boolean
        is_ok = messagebox.askokcancel(title="web", message=f"These are the details entered: \nEmail/Username: {email} "
                                                            f"\nPassword: {pass_generated} \nIs it OK to save")
        if is_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # Read the existing data in the file
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    # Creating a data.jason file if it doesn't exist and writing the generated data into the file
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating the existing data to include newly generated data
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Saving the updated data to the JSON file
                    json.dump(data, data_file, indent=4)
            finally:
                website_text_box.delete(0, END)
                email_or_username_text_box.delete(0, END)
                password_text_box.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


"""This initializes the window for our program"""
window = Tk()
window.title("Password Manager")
# window.minsize(width=200, height=300)
window.config(padx=40, pady=40)

"""This is a canvas holding the picture of a padlock on the GUI"""
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

"""These are the labels of each text box on the GUI"""
website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(row=1, column=0)
email_or_username = Label(text="Email/Username:", font=("Arial", 12))
email_or_username.grid(row=2, column=0)
password = Label(text="Password:", font=("Arial", 12))
password.grid(row=3, column=0)

"""These are the text boxes for user inputs"""
website_text_box = Entry(width=32, highlightthickness=0)
website_text_box.grid(row=1, column=1)
website_text_box.focus()
email_or_username_text_box = Entry(width=60, highlightthickness=0)
email_or_username_text_box.grid(row=2, column=1, columnspan=2)
email_or_username_text_box.insert(0, "Email")
password_text_box = Entry(width=32, highlightthickness=0)
password_text_box.grid(row=3, column=1)

"""These are all the buttons on the GUI"""
search_btn = Button(text="Search", width=22, highlightthickness=0, command=search_details)
search_btn.grid(row=1, column=2, padx=1)
gen_password_btn = Button(text="Generate Password", width=22, highlightthickness=0, command=password_generator)
gen_password_btn.grid(row=3, column=2, padx=1)
add_password_btn = Button(text="Add", width=51, highlightthickness=0, command=save)
add_password_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
