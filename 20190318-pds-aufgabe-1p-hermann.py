#!/usr/bin/python3

#die umrechnungsfaktoren beziehen sich immer in die umrechung in die zielmaßeinheit meter
umrechnungsfaktoren_metrisch = {
    "mum": 1000000,
    "mm": 1000,
    "cm": 100,
    "dm": 10,
    "m" : 1,
    "km" : 1/1000,
}

umrechnungsfaktoren_andere = {
    "in": 1,
    "ft": 1/12,
    "yd": 1/36,
    "mi": 1/63360, #->stimmt nicht!
}

umrechnungsfaktor_meter_inch = 39.37

def conv_length (value_in, unit_in, unit_out):

    #hier die execption zum werte pruefen!!

    # hier wird ueberprueft ob die eingangswerte existieren oder nicht

    if unit_in in umrechnungsfaktoren_metrisch.keys() and unit_out in umrechnungsfaktoren_metrisch.keys():
        print("ok im metrischen bereich!")
        ergebnis = value_in * (umrechnungsfaktoren_metrisch[unit_out] / umrechnungsfaktoren_metrisch[unit_in])

    if unit_in in umrechnungsfaktoren_andere.keys() and unit_out in umrechnungsfaktoren_andere.keys():
        print("ok im NICHT-metrischen bereich!")
        ergebnis = value_in * (umrechnungsfaktoren_andere[unit_out] / umrechnungsfaktoren_andere[unit_in])

    #wenn der eingabewert metrisch ist und in ein 'anderes' format umgewandelt werden soll
    if unit_in in umrechnungsfaktoren_metrisch.keys() and unit_out in umrechnungsfaktoren_andere.keys():
        ergebnis_metrisch = value_in * (umrechnungsfaktoren_metrisch["m"] / umrechnungsfaktoren_metrisch[unit_in])
        ergebnis_in_zoll = ergebnis_metrisch * umrechnungsfaktor_meter_inch
        ergebnis = ergebnis_in_zoll * (umrechnungsfaktoren_andere[unit_out] / umrechnungsfaktoren_andere["in"])

    #wenn der eingabewert nicht metrisch ist und in ein metrisches format umgewandelt werden soll
    if unit_in in umrechnungsfaktoren_andere.keys() and unit_out in umrechnungsfaktoren_metrisch.keys():
        ergebnis_anders = value_in * (umrechnungsfaktoren_andere["in"] / umrechnungsfaktoren_andere[unit_in])
        ergebnis_in_meter = ergebnis_anders / umrechnungsfaktor_meter_inch
        ergebnis = ergebnis_in_meter * (umrechnungsfaktoren_metrisch[unit_out] / umrechnungsfaktoren_metrisch["m"])



    print("Eingangswert:", value_in, unit_in )
    print("---> Zielmaßeinheit:", unit_out)
    print("\n",ergebnis, unit_out)




def main():
    value_in = 500
    unit_in = "mm"
    unit_out = "ft"
    conv_length(value_in, unit_in, unit_out)


if  __name__ =='__main__':
    main()
