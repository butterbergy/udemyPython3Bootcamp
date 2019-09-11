from pyfiglet import figlet_format
from termcolor import colored

msg = input("What do you want to print?")
color = input("What color do you want to use?")

ascii_art = figlet_format(msg)
colored_ascii = colored(ascii_art, color)
print(colored_ascii)
