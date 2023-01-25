# Erweitern Sie Ihr Jahreszahl-Programm aus Aufgabenteil 2 um Schleifen.
# Hat der Benutzer eine erfolgreiche Schaltjahresabfrage durchgeführt, so soll das Programm wieder „von vorne“ beginnen.
# Der Benutzer soll als nach der nächsten Zahl gefragt werden.

def schaltjahr( y ):
    if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
        return True

while True:
    y = int( input( "\n\nBitte geben Sie eine Jahreszahl ein:" ) )

    print( "\n" + str( y ) + " ist " + ("ein" if schaltjahr( y ) else "kein") + " Schaltjahr" )
    continue