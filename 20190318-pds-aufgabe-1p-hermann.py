#!/usr/bin/python3

def conv_length (value_in, unit_in, unit_out):

    conversion_factors_metric = {
        "mum": 1000000,
        "mm": 1000,
        "cm": 100,
        "dm": 10,
        "m" : 1,
        "km" : 1/1000,
    }

    conversion_factors_english_units = {
        "in": 1,
        "ft": 1/12,
        "yd": 1/36,
        "mi": 1/63360,
    }

    CONVERSION_FACTORS_METER_INCH = 39.37

    #exception to make sure value_in contains an postive int or float number
    try:
        value_in = float(value_in)
        if value_in <= 0:
            raise ValueError

    except ValueError:
        print (value_in, "is not a (positive) number.., program exited")
        exit()

    # check if the unit_in varaibles are existing in the conversion_factors
    if unit_in not in conversion_factors_metric.keys() and unit_in not in conversion_factors_english_units.keys():
        print (unit_in, "is no valid (input) unit of measurement (at least not in this program)")

        if unit_out not in conversion_factors_metric.keys() and unit_out not in conversion_factors_english_units.keys():
            print (unit_out, "is no valid  (output) unit of measurement (at least not in this program)")

        exit()

    if unit_out not in conversion_factors_metric.keys() and unit_out not in conversion_factors_english_units.keys():
        print (unit_out, "is no valid (output) unit of measurement (at least not in this program)")
        exit()

    #wenn der ein- und ausgabewert metrisch ist
    if unit_in in conversion_factors_metric.keys() and unit_out in conversion_factors_metric.keys():
        result = value_in * (conversion_factors_metric[unit_out] / conversion_factors_metric[unit_in])

    #wenn der ein- und ausgabewert nicht metrisch ist
    if unit_in in conversion_factors_english_units.keys() and unit_out in conversion_factors_english_units.keys():
        result = value_in * (conversion_factors_english_units[unit_out] / conversion_factors_english_units[unit_in])

    #wenn der eingabewert metrisch ist und in ein 'anderes' format umgewandelt werden soll
    if unit_in in conversion_factors_metric.keys() and unit_out in conversion_factors_english_units.keys():
        result_metric = value_in * (conversion_factors_metric["m"] / conversion_factors_metric[unit_in])
        result_in_inch = result_metric * CONVERSION_FACTORS_METER_INCH
        result = result_in_inch * (conversion_factors_english_units[unit_out] / conversion_factors_english_units["in"])

    #wenn der eingabewert nicht metrisch ist und in ein metrisches format umgewandelt werden soll
    if unit_in in conversion_factors_english_units.keys() and unit_out in conversion_factors_metric.keys():
        result_anders = value_in * (conversion_factors_english_units["in"] / conversion_factors_english_units[unit_in])
        result_in_meter = result_anders / CONVERSION_FACTORS_METER_INCH
        result = result_in_meter * (conversion_factors_metric[unit_out] / conversion_factors_metric["m"])

    print("converted:", value_in,unit_in,"to", result,unit_out)


def main():
    value_in = 6
    unit_in = "km"
    unit_out = "m"
    conv_length(value_in, unit_in, unit_out)


if  __name__ =='__main__':
    main()
