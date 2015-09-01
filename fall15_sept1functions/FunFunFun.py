def inch2centi(inches):
    return 2.54*inches

def pluralize(word):
    return word + "es"

xh = inch2centi(72)
pf = pluralize("fish")

print xh, pf
