# Erweitern Sie Ihr Programm aus Aufgabenteil 1 um Benutzereingaben.
# Fragen Sie den Benutzer, welches Jahr er überprüfen möchte und geben Sie ihm dann hierauf die korrekte Antwort zurück.

y = int( input( "Bitte geben Sie eine Jahreszahl ein:" ) )

def schaltjahr( y ):
    if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
        return True

print( "\n" + str( y ) + " ist " + ("ein" if schaltjahr( y ) else "kein") + " Schaltjahr" )
