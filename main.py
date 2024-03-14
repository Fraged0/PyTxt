import pip # import pip for installing colorama
import os # for clearing terminal
import platform # for getting os name

# and install colorama
if hasattr(pip, "main"):
    pip.main(["install", "colorama"])
else:
    pip._internal.main(["install", "colorama"])
    
if platform.system() == "Linux":
    # if Linux style
    os.system('clear')
elif platform.system == "Windows":
    # if Windows style
    os.system('cls')
    
# import colorama for colors
import colorama

colorama.init(autoreset=True) # init colorama

# variables
lines = {}
isRunning = True
count = -1

# title
print("     " + colorama.Back.WHITE + colorama.Fore.BLACK + "                   ")
print("     " + colorama.Back.WHITE + colorama.Fore.BLACK + "    |  PyTxt  |    ")
print("     " + colorama.Back.WHITE + colorama.Fore.BLACK + "                   \n")

# and main script
while isRunning:
    line = input() # user input
    
    # save function
    if line == "///SAVE///":
        fn = input("Enter filename: ")
        with open(fn, "w") as file:
            for i in range(len(lines)):
                value = lines["line" + str(i)]
                file.write(value)
                i += 1
        #for i in range(len(lines)):
        #        print(i)
        #        i += 1
    # quit function
    elif line == "///QUIT///":
        break;
    else:
        # if function is not writen, then it's just a text'
        count += 1
        name = "line" + str(count)
        lines[name] = line + "\n"
