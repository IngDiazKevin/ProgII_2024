def is_year(year):
    if year < 1582:
        print("No esta dentro del rango de años bisiestos")
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
test_data = [1900 , 2000, 2016, 1477]
test_resul = [True, True, True, False]

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, '->', end ='')
    resultado = is_year(yr)
    
    if resultado == test_resul[i]:
        print('OK')
    else:
        print('Fallido')