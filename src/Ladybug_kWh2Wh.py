# By Daniel Nielsen
# ark.daniel.nielsen@gmail.com
# Ladybug started by Mostapha Sadeghipour Roudsari is licensed
# under a Creative Commons Attribution-ShareAlike 3.0 Unported License.

#kWh to Wh
"""
Use this component to convert energy values in kWh to Wh or kWh/m2 to Wh/m2.
-
Provided by Ladybug 0.0.59
    
    Args:
        _kWh: An energy value or list of energy values in kWh or kWh/m2.  Note that, for the component to recognize flux or floor normalization, the input must have a Ladybug header.
    Returns:
        Wh: The input energy values converted to Wh.
"""

ghenv.Component.Name = "Ladybug_kWh2Wh"
ghenv.Component.NickName = 'kWh2Wh'
ghenv.Component.Message = 'VER 0.0.59\nMAR_01_2015'
ghenv.Component.Category = "Ladybug"
ghenv.Component.SubCategory = "4 | Extra"
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "7"
except: pass

floorNorm = False
Wh = []
for num in _kWh:
    if num == 'kWh/m2':
        Wh.append('Wh/m2')
        floorNorm = True
    elif num == 'kWh':
        Wh.append('Wh')
        floorNorm = False
    elif num == 'kWh':
        Wh.append('Wh')
        floorNorm = False
    elif num == 'kWh/m2':
        Wh.append('Wh/m2')
        floorNorm = True
    else:
        if floorNorm == True:
            try: Wh.append(float(num)*1000)
            except: Wh.append(num)
        else:
            try: Wh.append(float(num)*1000)
            except: Wh.append(num)
