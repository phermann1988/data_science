#!/usr/bin/python3

#conversion_factors beziehen sich immer in die umrechung in die zielmaßeinheit meter
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

conversion_factors_meter_inch = 39.37

def conv_length (value_in, unit_in, unit_out):

    #exception to make sure value_in contains a int or float number
    try:
        float(value_in)

        if value_in <= 0:
            raise ValueError

    except ValueError:
        print (value_in, "is not a (positive) number.., program exited")
        exit()

    # hier wird ueberprueft ob die eingangswerte existieren oder nicht
    if unit_in not in conversion_factors_metric.keys() and unit_in not in conversion_factors_english_units.keys():
        print ("unit_in is not available")

        if unit_out not in conversion_factors_metric.keys() and unit_out not in conversion_factors_english_units.keys():
            print ("unit_out is not available")

        print("exiting...")
        exit()

    # hier wird ueberprueft ob die eingangswerte existieren oder nicht
    if unit_out not in conversion_factors_metric.keys() and unit_out not in conversion_factors_english_units.keys():
        print ("unit_out not available, program exited")
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
        result_in_inch = result_metric * conversion_factors_meter_inch
        result = result_in_inch * (conversion_factors_english_units[unit_out] / conversion_factors_english_units["in"])

    #wenn der eingabewert nicht metrisch ist und in ein metrisches format umgewandelt werden soll
    if unit_in in conversion_factors_english_units.keys() and unit_out in conversion_factors_metric.keys():
        result_anders = value_in * (conversion_factors_english_units["in"] / conversion_factors_english_units[unit_in])
        result_in_meter = result_anders / conversion_factors_meter_inch
        result = result_in_meter * (conversion_factors_metric[unit_out] / conversion_factors_metric["m"])


    print("converted:", value_in,unit_in,"to", result,unit_out)


def main():
    value_in = 5
    unit_in = "in"
    unit_out = "mi"
    conv_length(value_in, unit_in, unit_out)


if  __name__ =='__main__':
    main()
