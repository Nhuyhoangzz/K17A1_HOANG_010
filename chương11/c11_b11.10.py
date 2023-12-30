#menu_is_boring(meals)
meals_1=['Redneck Ribs','Prawn Star','San Qeantin Squid',
         'Fist Full of Pizza','Honky Tonk Chicken']
meals_2=['Redneck Ribs','Prawn Star','Running Bear Salmon',
         'Running Bear Salmon','Honky Tonk Chicken']
def meal(ls):
    for i in range(len(ls)):
        for j in range(i +1 ,len(ls)):
            if ls[i]==ls[j]:
                return True
    return False


# Kiểm tra xem có phần tử trùng nhau trong list không
a = meal(meals_1)
b = meal(meals_2)

print(f'Bữa ăn 1 có phần tử trùng nhau không?',a)
print(f'Bữa ăn 2 có phần tử trùng nhau không?',b)