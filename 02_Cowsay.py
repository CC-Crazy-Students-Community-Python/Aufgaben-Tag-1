# Schreiben Sie ein Programm, welches als Ergebnis ein kleines Bild (als ASCII-Art) auf der Konsole, 
# welches den Text in der Sprechblase der Kuh enthält, ausgibt.

def cow_say():
    output = "  _______________\n"
    output += "< Python rocks! >\n"
    output += "  _______________\n"
    output += "       \   ^__^\n"
    output += "        \  (oo)\_______\n"
    output += "         \_(__)\       )\/\\\n"
    output += "               ||----w |\n"
    output += "               ||     ||\n"
    output += "===============__=====__===\n"
    return output

print( cow_say() )