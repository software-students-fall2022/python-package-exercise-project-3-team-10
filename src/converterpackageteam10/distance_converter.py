

def convert_distance(num, unit1, unit2):
    units = {"in", "ft", "mi", "mm", "cm", "m", "km"}
    alias_units = {
        "inches": "in", 
        "feet": "ft", 
        "mile": "mi", 
        "milimeter": "mm", 
        "centimeter": "cm", 
        "meter": "m", 
        "kilometer": "km"
    }
    conversions = {"in": {"ft": 1/12, "mi": 1/63360, "mm": 25.4, "cm": 2.54, "m": 0.0254, "km": 2.54e-5}, 
                   "ft": {"in": 12, "mi": 1/5280, "mm": 304.8, "cm": 30.48, "m": 0.3048, "km": 3.048e-4},
                   "mi": {"in": 63360, "ft": 5280, "mm": 1609340, "cm": 160934, "m": 1609.34, "km": 1.60934},
                   "mm": {"in": 1/25.4, "ft": 1/304.8, "mi": 1/1609340, "cm": 1/10, "m": 1/1000, "km": 1e-6},
                   "cm": {"in": 1/2.54, "ft": 1/30.48, "mi": 1/160934, "mm": 10, "m": 1/100, "km": 1e-5},
                   "m": {"in": 39.3701, "ft": 3.28084, "mi": 1/1609.34, "mm": 1000, "cm": 100, "km": 1e-3},
                   "km": {"in": 39370.1, "ft": 3280.84, "mi": 1/1.60934, "mm": 1e6, "cm": 1e5, "m": 1000}}
    if unit1 in alias_units:
        unit1 = alias_units[unit1]
    if unit2 in alias_units:
        unit2 = alias_units[unit2]
    
    if unit1 in units:
        if unit2 in units:
            return str(float(num) * conversions[unit1][unit2])
        else:
            raise UnitNotFound(unit2)
    else:
        raise UnitNotFound(unit1)

class UnitNotFound(Exception):
    def __init__(self, unit):
        super().__init__("The unit " + unit + " is not listed as a valid convertible.")
