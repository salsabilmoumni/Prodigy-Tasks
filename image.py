
from tkinter import * # imports all the classes and functions from the tkinter library, which is used to create graphical user interfaces (GUIs) in Python
from tkinter import filedialog #imports the filedialog module from tkinter, which provides dialogs for opening and saving files

root = Tk()
root.geometry("200x160")

def encrypt_image():
    # opens a file dialog for the user to select a JPG or PNG file.
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg'), ('png file', '*.png')]) 
    if file1 is not None:  #checks if a file was selected
        file_name = file1.name # gets the name of the selected file
        key = Entry1.get(1.0, END).strip() # retrieves the key entered by the user in the Entry1 widget, removing any extra newline characters
        print(file_name, key)
        with open(file_name, 'rb') as fi: #opens the selected file in binary read mode 
            image = fi.read()
        
        image = bytearray(image) # converts the image data to a mutable bytearray.
        for index, value in enumerate(image): #iterates over each byte in the image
            image[index] = value ^ int(key) # performs a bitwise XOR operation on each byte with the key (converted to an integer) to encrypt the image
        
        with open(file_name, 'wb') as fi:
            fi.write(image)

b1 = Button(root, text='Encrypt', command=encrypt_image) # creates a button widget. The root parameter specifies that this button is part of the main window
b1.place(x=70, y=10)

Entry1 = Text(root, height=1, width=10)
Entry1.place(x=50, y=50)

root.mainloop()
