# Python 3
#Install on Linux/macOS: pip3 install pyperclip
#On Linux, this module makes use of the xclip or xsel commands, which should come with the os. Otherwise run "sudo apt-get install xclip"
import pyperclip
def removeline(text):
    new = ""
    for i in text:
        if i != "\n":
            new = new+i
        else:
            new = new+" "
    return new

text= pyperclip.paste()
noline= removeline(text)
print (noline)
pyperclip.copy(noline)

