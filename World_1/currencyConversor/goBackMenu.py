import menu
import errorCrt

r = input('| Go back to Menu? [Y]/[N]: ')

if r.upper()[0] == "Y":
    menu
elif r.upper()[0] == "N":
    exit()
else:
    errorCrt.errorCaracter()