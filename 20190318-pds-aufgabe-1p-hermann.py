#!/usr/bin/python3

def conv_length(value_in, unit_in, unit_out):

    # dict for conversion factors of the metric measurement system
    conv_facts_m = {
        "mum": 1000000,
        "mm": 1000,
        "cm": 100,
        "dm": 10,
        "m": 1,
        "km": 1/1000,
    }
    # dict for conversion factors of the US customary measurement system
    conv_facts_us = {
        "in": 1,
        "ft": 1/12,
        "yd": 1/36,
        "mi": 1/63360,
    }

    CONVERSION_FACTOR_METER_INCH = 39.37

    # exception to make sure value_in contains an postive int or float number
    try:
        value_in = float(value_in)

        if value_in <= 0:
            raise ValueError

    except ValueError:
        print(value_in, "is not a (positive) number.., program exited")
        exit()

    # check if unit_in + unit_out varaibles are existing in conv_facts
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

    # calculate in the metric system
    if unit_in in conv_facts_m.keys() and\
            unit_out in conv_facts_m.keys():
        result = value_in * (conv_facts_m[unit_out] / conv_facts_m[unit_in])

    # calculate in the US customary measurement system
    if unit_in in conv_facts_us.keys() and\
            unit_out in conv_facts_us.keys():
        result = value_in * (conv_facts_us[unit_out] / conv_facts_us[unit_in])

    # calculate from the metric system into the US customary measurement system
    if unit_in in conv_facts_m.keys() and\
            unit_out in conv_facts_us.keys():
        tmp_m = value_in * (conv_facts_m["m"] / conv_facts_m[unit_in])
        tmp_in = tmp_m * CONVERSION_FACTOR_METER_INCH
        result = tmp_in * (conv_facts_us[unit_out] / conv_facts_us["in"])

    # calculate from the US customary measurement system into the metric system
    if unit_in in conv_facts_us.keys() and\
            unit_out in conv_facts_m.keys():
        tmp_us = value_in * (conv_facts_us["in"] / conv_facts_us[unit_in])
        tmp_m = tmp_us / CONVERSION_FACTOR_METER_INCH
        result = tmp_m * (conv_facts_m[unit_out] / conv_facts_m["m"])

    print("converted:", value_in, unit_in, "to", result, unit_out)

    return (result)
