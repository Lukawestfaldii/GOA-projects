
sum_even = 0
count_even = 0
number = 1

# while ციკლი
while number <= 100:
    if number % 2 == 0:  # ლუწი რიცხვის შემოწმება
        sum_even += number
        count_even += 1
    number += 1

# საშუალო არითმეტიკული
average = sum_even / count_even

print("1-დან 100-მდე ლუწი რიცხვების საშუალო არითმეტიკულია:",)

# მომხმარებლისთვის რიცხვის შეყვანა
try:
    number = float(input("შეიყვანეთ რიცხვი: "))

    # რიცხვის შემოწმება
    if number > 0:
        print("ეს რიცხვი დადებითია.")
    elif number < 0:
        print("ეს რიცხვი უარყოფითია.")
    else:
        print("რიცხვი არის 0.")

except ValueError:
    print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვი.")



