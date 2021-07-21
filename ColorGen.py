import colorama
from colorama import Back, Fore

colorama.init(autoreset = True) 

text = input("Please enter any word or phrase you desire: ")

print(Fore.RED + text)
print(Fore.BLUE + text)
print(Fore.GREEN + text)
print(Fore.YELLOW + text)