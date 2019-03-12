#!/usr/bin/python3

#die umrechnungsfaktoren beziehen sich immer in die umrechung in die zielmaßeinheit meter
umrechnungsfaktoren = {
    #"nm" : 100000,
    "mum": 1000000,
    "mm": 1000,
    "cm": 100,
    "dm": 10,
    "m" : 1,
    # "da": 10,
    # "": 1,
    # "d": 0.1,
    # "c": 0.01,
    # "m": 0.001
}




def conv_length (value_in, unit_in, unit_out):
    eingangsmaßeinheit = umrechnungsfaktoren[unit_in]
    zielmaßeinheit = umrechnungsfaktoren[unit_out]

    print("Eingangswert:", value_in, unit_in )
    print("---> Zielmaßeinheit:", unit_out)

    ergebnis = value_in * (zielmaßeinheit / eingangsmaßeinheit)
    #ergebnis = value_in * 100
    print("\n",ergebnis, unit_out)


def main():
    value_in = 6.4
    unit_in = "m"
    unit_out = "mum"
    conv_length(value_in, unit_in, unit_out)


if  __name__ =='__main__':
    main()
