def react(unit1, unit2):
    # Check if the letter is the same
    if unit1.lower() == unit2.lower():
        # Check if they react
        if (unit1.islower() and unit2.isupper()) or \
        (unit1.isupper() and unit2.islower()):
            return True
    else:
        return False

def react_polymers(raw_data):
    # Start with empty string
    polymers = ""
    for unit in raw_data:
        # Handle initial unit
        if not polymers:
            polymers += unit
        # Check if they react
        elif react(unit, polymers[-1]):
            polymers = polymers[:-1]
        # Otherwise add the unit
        else:
            polymers += unit
    return polymers
