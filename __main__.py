from converterpackageteam10 import age_converter
from converterpackageteam10 import distance_converter
from converterpackageteam10 import number_converter
from converterpackageteam10 import time_zone_converter

def main():
  print("\tCalling age_converter methods...")
  print("\tCalling age_converter.help()...")
  age_converter.help()
  print()
  print("\tCalling age_converter.calc_age(str, str)...")
  print("\t\tDOB of Jan 1 2000 1:33PM: ", age_converter.calc_age('Jan 1 2000 1:33PM', 'actual'))
  print("\t\tDOB of Jan 11 2000 1:33PM: ", age_converter.calc_age('Jan 11 2000 1:33PM', 'years'))
  print("\t\tDOB of Feb 1 2005 1:33PM: ", age_converter.calc_age('Feb 1 2005 1:33PM', 'days'))
  print()

  print()
  print()

  print("\tCalling distance_converter methods...")
  print("\tCalling distance_converter.allowed_distance_conversions()...")
  li = distance_converter.allowed_distance_conversions()
  print("\t\tReturns:", li)
  print()
  print('\tCalling distance_converter.convert_distance(int, str, str)...')
  print("\t\t10 feet =", distance_converter.convert_distance(10, 'ft', 'in'), "inches")
  print("\t\t100 centimeters =", distance_converter.convert_distance(100, 'cm', 'm'), "meters")
  print()

  print()
  print()

  print("\tCalling number_converter methods...")
  print("\tCalling number_converter.convert_number(str, Any)...")
  print("\t\tBinary of 0b1111 =", number_converter.convert_number("decimal", 0b1111), "in decimal")
  print("\t\tOctal of 0o1111 =", number_converter.convert_number("decimal", 0o1111), "in decimal")
  print("\t\tHexadecimal of 0x1111 =", number_converter.convert_number("decimal", 0x1111), "in decimal")
  print("\t\tDecimal of 1000 =", number_converter.convert_number("binary", 1000), "in binary")
  print("\t\tDecimal of 1000 =", number_converter.convert_number("octal", 1000), "in octal")
  print("\t\tDecimal of 1000 =", number_converter.convert_number("hexadecimal", 1000), "in hexadecimal")
  print()

  print()
  print()

  print("\tCalling time_zone_converter methods...")
  print("\tCalling time_zone_converter.convert_timezone(str)...")
  print("\t\tCurrent times in the USA:", time_zone_converter.convert_timezone("US"))
  print()

  print()

if __name__ == '__main__':
    main()