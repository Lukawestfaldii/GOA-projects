def check_drivers_license_eligibility():
    age = int(input("შეიყვანეთ ასაკი: "))
    experience = int(input("შეიყვანეთ მართვის გამოცდილება (წლები): "))

    if age >= 18 and experience >= 1:
        print("თქვენ გაქვთ მართვის მოწმობის აღების უფლება.")
    else:
        print("თქვენ არ გაქვთ მართვის მოწმობის აღების უფლება.")

check_drivers_license_eligibility()