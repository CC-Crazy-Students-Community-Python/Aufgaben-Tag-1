# Schreiben Sie eine Methode, die als Rückgabewert ein boolean hat und auswertet, 
# ob es sich bei dem übergebenen Jahr (als int-Wert) um ein Schaltjahr handelt oder nicht.

y = 2020

def schaltjahr( y ):
    if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
        return True

if schaltjahr( y ):
    print( "\n" + str( y ) + " ist ein Schaltjahr" )
else:
    print( "\n" + str( y ) + " ist kein Schaltjahr" )