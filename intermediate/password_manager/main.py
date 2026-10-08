from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

BLUE = "#31A1F0"
WHITE = "#ffffff"
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'Q', 'R', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '%', '&', '*', '(', ')', '+']
website_entry = None
email_username_entry = None
password_entry = None


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """generate a new password"""
    global password_entry

    letters_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    symbols_list = [choice(SYMBOLS) for _ in range(randint(2, 4))]
    numbers_list = [choice(NUMBERS) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    password_entry.clipboard_clear()
    password_entry.clipboard_append(password)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    """find password in file"""
    website = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showinfo(message="No data file")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=f"Website: {website}",
                message=f"Email: {email}\n "
                f"password: {password}\n "
            )
        else:
            messagebox.showinfo(message="No detail for the wedsite exists")
    finally:
        website_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """save password to file"""

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            message=f"Please confirm:\n "
            f"Website: {website}\n "
            f"Email: {email}\n "
            f"password: {password}\n "
            f"Is theses ok to save!"
        )

        if is_ok:
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{website} | {email} | {password}\n")
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}

            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


def main():
    """main function"""
    global website_entry, email_username_entry, password_entry

    window = Tk()
    window.title("Password manager")
    window.config(padx=30, pady=30)

    canvas = Canvas(width=200, height=200)
    lock_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=lock_img)
    canvas.grid(row=0, column=1)

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0)
    website_entry = Entry(window, width=24)
    website_entry.grid(row=1, column=1)
    website_entry.focus()
    search_button = Button(window, text="Search",
                           width=14, command=find_password)
    search_button.grid(row=1, column=2)

    email_username_label = Label(text="Email/Username:")
    email_username_label.grid(row=2, column=0)
    email_username_entry = Entry(window, width=42)
    email_username_entry.grid(row=2, column=1, columnspan=2)
    email_username_entry.insert(0, "conan@gmail.com")

    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)
    password_entry = Entry(window, width=24)
    password_entry.grid(row=3, column=1)
    password_button = Button(
        window, text="Generate Password", command=generate_password)
    password_button.grid(row=3, column=2)

    add_button = Button(window, text="add", width=20,
                        bg=BLUE, highlightthickness=0, fg=WHITE,
                        font=("Helvetica", 12, "bold",  "italic"),
                        command=save)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()
