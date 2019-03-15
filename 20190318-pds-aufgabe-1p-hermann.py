#!/usr/bin/python3

def conv_length (value_in, unit_in, unit_out):

    #dict for conversion factors of the metric measurement system
    conversion_factors_metric = {
        "mum": 1000000,
        "mm": 1000,
        "cm": 100,
        "dm": 10,
        "m" : 1,
        "km" : 1/1000,
    }
    #dict for conversion factors of the US customary measurement system
    conversion_factors_us = {
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


    # check if the unit_in and unit_out varaibles are existing in the conversion_factors
    if unit_in not in conversion_factors_metric.keys() and unit_in not in conversion_factors_us.keys():
        print (unit_in, "is no valid (input) unit of measurement (at least not in this program)")

        if unit_out not in conversion_factors_metric.keys() and unit_out not in conversion_factors_us.keys():
            print (unit_out, "is no valid  (output) unit of measurement (at least not in this program)")

        exit()

    if unit_out not in conversion_factors_metric.keys() and unit_out not in conversion_factors_us.keys():
        print (unit_out, "is no valid (output) unit of measurement (at least not in this program)")
        exit()


    #calculate in the metric system
    if unit_in in conversion_factors_metric.keys() and unit_out in conversion_factors_metric.keys():
        result = value_in * (conversion_factors_metric[unit_out] / conversion_factors_metric[unit_in])

    #calculate in the US customary measurement system
    if unit_in in conversion_factors_us.keys() and unit_out in conversion_factors_us.keys():
        result = value_in * (conversion_factors_us[unit_out] / conversion_factors_us[unit_in])

    #calculate from the metric system into the US customary measurement system
    if unit_in in conversion_factors_metric.keys() and unit_out in conversion_factors_us.keys():
        result_metric = value_in * (conversion_factors_metric["m"] / conversion_factors_metric[unit_in])
        result_in_inch = result_metric * CONVERSION_FACTORS_METER_INCH
        result = result_in_inch * (conversion_factors_us[unit_out] / conversion_factors_us["in"])

    #calculate from the US customary measurement system into the metric system
    if unit_in in conversion_factors_us.keys() and unit_out in conversion_factors_metric.keys():
        result_us = value_in * (conversion_factors_us["in"] / conversion_factors_us[unit_in])
        result_in_meter = result_us / CONVERSION_FACTORS_METER_INCH
        result = result_in_meter * (conversion_factors_metric[unit_out] / conversion_factors_metric["m"])

    print("converted:", value_in,unit_in,"to", result,unit_out)

    return (result)

def main():
    value_in = 6
    unit_in = "km"
    unit_out = "m"
    conv_length(value_in, unit_in, unit_out)


if  __name__ =='__main__':
    main()
