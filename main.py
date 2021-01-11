weight = float(input('what is your weight : '))
metric = input('Pounds or Kilogram : ')


if metric.upper() == 'K':
    print(f'Weight in Pounds :  {str(weight * 2.205)} Pounds')
if metric.upper() == 'L':
    print(f'Weight in Pounds :  {str(weight / 2.205)} Kilograms')
else:
    print('Error in metric input')

