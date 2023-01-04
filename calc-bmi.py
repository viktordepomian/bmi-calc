input_weight = int(input('Enter your weight(kg): '))
input_height = float(input('Enter your height(m): '))

def calcBMI(weight, height):
    
    TOTAL = weight / (height * height)
    return round(TOTAL, 1)

print(calcBMI(input_weight, input_height))