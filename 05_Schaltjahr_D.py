# Fügen Sie eine Abbruchbedingung hinzu, so dass der Benutzer das Programm mit einem Wort (z.B. exit) beenden kann.

def schaltjahr( y ):
    if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
        return True

while True:
    y = input( "\n\nBitte geben Sie eine Jahreszahl ein:" )

    if y == "exit" or y == "stop" or y == "aus" or y == "halt":
        print( "Danke, Das Tool wird beendet" )
        break
    else:
        y = int( y )
        print( "\n" + str( y ) + " ist " + ("ein" if schaltjahr( y ) else "kein") + " Schaltjahr" )
        continue

