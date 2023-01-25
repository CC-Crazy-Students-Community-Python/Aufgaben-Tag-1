# Schreiben Sie eine Funktion maximum der zwei int-Werte übergeben werden und die den größten der beiden Werte zurückliefert.
# Sind beide gleich, dann soll der erste zurückgegeben werden.

def maximum( x, y ):
    if x >= y:
        return x
    else:
        return y

x=int( input( "Bitte geben Sie einen Zahl ein:" ) )
y=int( input( "Bitte geben Sie einen Zahl ein:" ) )

print( "\ndie größere Zahl ist: " + str( maximum( x, y ) ) )
