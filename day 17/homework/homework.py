input_numbers = input("შეიყვანეთ რიცხვები, მძიმით გამოყოფილი ფორმატით (მაგალითად: 1, 2, 3, 4): ")

# შეყვანილი რიცხვების დამუშავება
try:
    numbers = [float(num.strip()) for num in input_numbers.split(",")]
    
    # სიის რიცხვების ჯამის გამოთვლა
    total_sum = sum(numbers)

    print("რიცხვების ჯამი არის:", total_sum)
except ValueError:
    print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვები, მძიმით გამოყოფილი ფორმატით.")
