#!/usr/bin/python3

def conv_length(value_in, unit_in, unit_out):

    # Dictionary Umrechnungsfaktoren fuer das metrische System
    conv_facts_m = {
        "mum": 1000000,
        "mm": 1000,
        "cm": 100,
        "dm": 10,
        "m": 1,
        "km": 1/1000,
    }
    # Dictionary Umrechnungsfaktoren fuer das angloamerikanischen Maßsystem
    conv_facts_us = {
        "in": 1,
        "ft": 1/12,
        "yd": 1/36,
        "mi": 1/63360,
    }

    # Konstanten Umrechnungsfaktoren Meter in inch
    CONVERSION_FACTOR_METER_INCH = 39.37

    # exception: handelt es sich um positiven Zahlenwert?
    # (um negative Längen und ungültige String-Eingaben zu verhindern).
    # der cast in float der variable value_in ermoeglicht, dass auch zahlen
    # in anfuerhungszeichen verarbeitet werden können
    try:
        value_in = float(value_in)

        if value_in <= 0:
            raise ValueError

    except ValueError:
        print(value_in, "is not a (positive) number.., program exited")
        exit()

    # hier wird auf existierende Schlüsselwerte in den
    # jeweiligen Umrechnungsfaktoren überprüft
    # Existiert nur eine der beiden Übergabeparameter
    # (unit_in und unit_out) bzw. Längeneinheit oder keiner von beiden?

    if unit_in not in conv_facts_m.keys() and\
            unit_in not in conv_facts_us.keys():
        print(unit_in, "is no valid (input) unit of measurement")

        if unit_out not in conv_facts_m.keys()\
                and unit_out not in conv_facts_us.keys():
            print(unit_out, "is no valid  (output) unit of measurement")

        exit()

    if unit_out not in conv_facts_m.keys() and\
            unit_out not in conv_facts_us.keys():
        print(unit_out, "is no valid (output) unit of measurement")
        exit()

    # Berechnung innerhalb des metrischen Systems:
    # notwendigen Umrechnungsfaktoren mittels
    # der Schlüsselwerte aus dem entsprechenden
    # Dictionary (conv_facts_m) entnommen
    # ergebnis wird in variable result gespeichert
    if unit_in in conv_facts_m.keys() and\
            unit_out in conv_facts_m.keys():
        result = value_in * (conv_facts_m[unit_out] / conv_facts_m[unit_in])

    # Berechnung innerhalb des angloamerikanischen Systems:
    # notwendigen Umrechnungsfaktoren mittels
    # der Schlüsselwerte aus dem entsprechenden
    # Dictionary (conv_facts_us) entnommen
    # ergebnis wird in variable result gespeichert
    if unit_in in conv_facts_us.keys() and\
            unit_out in conv_facts_us.keys():
        result = value_in * (conv_facts_us[unit_out] / conv_facts_us[unit_in])

    # Berechnung vom metischen System in das angloamerikanische
    # notwendigen Umrechnungsfaktoren mittels
    # der Schlüsselwerte aus dem entsprechenden
    # Dictionaries (conv_facts_m und conv_facts_us)
    # (value_in) in wird in Basiswert Meter umgerechnet (var: tmp_m)
    # danach wird der Wert in Inch umgewandelt (var: tmp_in)
    # das ergebnis wird in die Zieleinheit berechnet (var: result)

    if unit_in in conv_facts_m.keys() and\
            unit_out in conv_facts_us.keys():
        tmp_m = value_in * (conv_facts_m["m"] / conv_facts_m[unit_in])
        tmp_in = tmp_m * CONVERSION_FACTOR_METER_INCH
        result = tmp_in * (conv_facts_us[unit_out] / conv_facts_us["in"])

    # Berechnung vom angloamerikanische System ins metrische
    # notwendigen Umrechnungsfaktoren mittels
    # der Schlüsselwerte aus dem entsprechenden
    # Dictionaries (conv_facts_us und conv_facts_m)
    # (value_in) in wird in Basiswert Inch umgerechnet (var: tmp_us)
    # danach wird der Wert in meter umgewandelt (var: tmp_m)
    # das ergebnis wird in die Zieleinheit berechnet (var: result)
    if unit_in in conv_facts_us.keys() and\
            unit_out in conv_facts_m.keys():
        tmp_us = value_in * (conv_facts_us["in"] / conv_facts_us[unit_in])
        tmp_m = tmp_us / CONVERSION_FACTOR_METER_INCH
        result = tmp_m * (conv_facts_m[unit_out] / conv_facts_m["m"])

    print("converted:", value_in, unit_in, "to", result, unit_out)

    # Rueckgabewert der funktion
    return (result)
