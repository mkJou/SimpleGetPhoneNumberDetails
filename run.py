"""
    # Developed as test code by mkJou (github.com/mkJou)
    # Version 1.0.0
"""
import phonenumbers
from tkinter import *
from tkinter import messagebox
from phonenumbers import carrier, geocoder,  timezone

window = Tk()
window.title("List")
window.geometry("256x256")

lbl1 = Label(window, text="Get Phone Number\n Details\n", font="none 16 bold")
lbl1.config(anchor=CENTER)
lbl1.pack()
  
lbl2 = Label (window, text="Enter phone number (including to prefix)\nFor example: +584241234567:", font="none 6 bold")
lbl2.config(anchor=CENTER)
lbl2.pack()
 
form1 = StringVar()
form1_entry = Entry(window, textvariable=form1)
form1_entry.pack()

def searchNumberDetails():
    try:
        MobileNumber = phonenumbers.parse(form1.get())
        tmZone = timezone.time_zones_for_number(MobileNumber)
        tcarrier = carrier.name_for_number(MobileNumber, "es")
        tGeocoder = geocoder.description_for_number(MobileNumber, "es")
        tValidNumber = phonenumbers.is_valid_number(MobileNumber)
        tCheckNumber = phonenumbers.is_possible_number(MobileNumber)
        title = 'Number found: ' + str(form1.get())
        message = 'Region: ' + str(tmZone[0]) + '\nCountry: ' + str(tGeocoder) + '\n\nCarrier: ' + str(tcarrier).capitalize() + '\nValid number: (' + str(tValidNumber) + '/' + str(tCheckNumber) + ')'
        messagebox.showinfo(message=message, title=title)
        
    except Exception as error:
        message = 'An error has occurred, verify the cell phone is valid.'
        messagebox.showerror(message=message, title='Oops, an error.')

btn1 = Button(window, text="Search", command=searchNumberDetails)
btn1.config(anchor=CENTER)
btn1.pack()

lbl2 = Label (window, text="\nDeveloped as test code by mkJou\nwww.github.com/mkJou", font="none 6")
lbl2.config(anchor=CENTER)
lbl2.pack()

window.mainloop()