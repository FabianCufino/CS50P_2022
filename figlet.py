import sys
from pyfiglet import Figlet

figlet = Figlet()
list_fonts = figlet.getFonts()

if len(sys.argv) == 1:
    #print("no commands")
    in_1 = input("text:")
    print(figlet.renderText(in_1))
elif len(sys.argv) == 2:
    #print("no commands")
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f','--font']:
        if sys.argv[2] in list_fonts:
            #print("2 commands")
            in_1 = input("text:")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(in_1))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

