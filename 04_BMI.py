# Berechnen Sie den Bodymass-Index bmi nach folgender einfacher Formel:
# Bodymassindex: bmi=gewicht[kg]/groesse[m]²

x = float( input( "Bitte geben Sie Ihr Gewicht ein in kg ( komma=punkt ):" ) )
y = float( input( "Bitte geben Sie Ihre Größe ein in m ( komma=punkt ):" ) )
bmi = round ( ( x / ( y ** 2 ) ),  2 )

print( "\nIhr BMI ist: "  +  str( bmi ) )

# Werten Sie den errechneten bmi anhand der folgenden Kriterien aus:
#     bmi < 10 => Überprüfen Sie ihre Eingabe
#     10 <= bmi < 15 => Magersucht
#     15 <= bmi < 20 => Untergewicht
#     20 <= bmi < 25 => Normalgewicht
#     25 <= bmi < 30 => Übergewicht
#     30 <= bmi < 40 => Fettsucht
#     40 <= bmi < 50 => morbide Fettsucht
#     bmi >= 50 => Überprüfen Sie ihre Eingabe

diag = "Ihre Diagnose ist: "

if bmi < 10 or bmi > 50:
    diag ="Überprüfen Sie Ihre Eingabe"
    nose = " !!!"
elif bmi < 15:
    nose = "Ihre DiagMagersucht"
elif bmi < 20:
    nose = "Untergewicht"
elif bmi < 25:
    nose = "Normalgewicht"
elif bmi < 30:
    nose = "Übergewicht"
elif bmi < 40:
    nose = "Fettsucht"
else:
    nose = "morbide Fettsucht"

print( diag + nose)