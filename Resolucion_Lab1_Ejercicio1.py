def is_year_leap(year):
    if year < 1582:
        print("No dentro del período del calendario Gregoriano.")
    elif year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    monthDays = [31, 28 ,31, 30 ,31, 30 ,31,31,30,31,30,31]

    if is_year_leap(year) and month == 2:
        return 29
    return monthDays[month -1 ] #Devuelve el valor de dias que tiene el mes
                                #Marzo se mando como 3 pero si se pone tres es incorrecto
                                #Ya que la posicion 3 es ABril (empieza contando desde cero)
                                #Por tal razon menos 1

test_years = [1998, 2000, 2016, 1987]
test_months = [4, 2, 1, 11]
test_results = [27, 29, 25, 30]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")