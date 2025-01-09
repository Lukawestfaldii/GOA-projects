

def capitalize_first_letter():
    
    text = input("შეიყვანეთ ტექსტი: ")
    
    capitalized_text = text.capitalize()
    
    print("პირველი სიმბოლო დიდი ასოთი, დანარჩენი მცირე ასოებით:", capitalized_text)

capitalize_first_letter()

def find_word_index():
    
    text = input("შეიყვანეთ ტექსტი: ")
    
    search_word = input("შეიყვანეთ საძიებელი სიტყვა: ")
    
    index = text.find(search_word)

    if index != -1:
        print(f"სიტყვა '{search_word}' ტექსტში პირველად გვხვდება ინდექსზე: {index}")
    else:
        print(f"სიტყვა '{search_word}' ტექსტში ვერ მოიძებნა.")

find_word_index()