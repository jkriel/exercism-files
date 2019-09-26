def convert(number):
    droplets = ''

    if number%3 == 0:
        droplets += 'Pling'
        if number%5 == 0:
            droplets += 'Plang'
            if number%7 == 0:
                droplets += 'Plong'
        elif number%7 == 0:
            droplets += 'Plong'    
    
    elif number%5 == 0:
        droplets += 'Plang'
        if number%7 == 0:
            droplets += 'Plong'
    elif number%7 == 0:
        droplets += 'Plong'
    
    else:
        return str(number)

    return droplets

print(convert(42))