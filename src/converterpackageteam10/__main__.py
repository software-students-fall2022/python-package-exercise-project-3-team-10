import age_converter
import distance_converter
import number_converter
import time_zone_converter

def main():
  print("Calling age_converter methods...")
  print("Calling age_converter.help()...")
  age_converter.help()
  print()
  print("Calling age_converter.calc_age(str, str)...")
  print("DOB of Jan 1 2000 1:33PM: ", age_converter.calc_age('Jan 1 2000 1:33PM', 'actual'))
  print("DOB of Jan 1 2000 1:33PM: ", age_converter.calc_age('Jan 1 2000 1:33PM', 'years'))
  print("DOB of Jan 1 2000 1:33PM: ", age_converter.calc_age('Jan 1 2000 1:33PM', 'days'))
  print()

  print()
  print()

  print("Calling distance_converter methods...")
  print("Calling distance_converter.allowed_distance_conversions()...")
  li = distance_converter.allowed_distance_conversions()
  print("Returns:", li)
  print()
  print('Calling distance_converter.convert_distance(int, str, str)...')
  print("10 feet =", distance_converter.convert_distance(10, 'ft', 'in'), "inches")
  print("100 centimeters =", distance_converter.convert_distance(100, 'cm', 'm'), "meters")
  print()

  print()
  print()

  print("Calling number_converter methods...")
  print("Calling number_converter.convert_number(str, Any)...")
  print("Binary of 0b1111 =", number_converter.convert_number("decimal", 0b1111), "in decimal")
  print("Octal of 0o1111 =", number_converter.convert_number("decimal", 0o1111), "in decimal")
  print("Hexadecimal of 0x1111 =", number_converter.convert_number("decimal", 0x1111), "in decimal")
  print("Decimal of 1000 =", number_converter.convert_number("binary", 1000), "in binary")
  print("Decimal of 1000 =", number_converter.convert_number("octal", 1000), "in octal")
  print("Decimal of 1000 =", number_converter.convert_number("hexadecimal", 1000), "in hexadecimal")
  print()

  print()
  print()

  print("Calling time_zone_converter methods...")
  print("Calling time_zone_converter.convert_timezone(str)...")
  print("Current times in the USA:", time_zone_converter.convert_timezone("US"))
  print()

  print()
  print()

if __name__ == '__main__':
    main()

