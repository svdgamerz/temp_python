def greet():
    print("NUB")
    
def decideperson():
    age_of_person = input("Enter age of Person")
    if age_of_person < 18:
        print("teenager")
    elif age_of_person < 60 and age_of_person >=18:
        print("adult")
    else:
        print("Senior Citizen")
    
    def main():
        greet()
        
if __name__ == "__main__":
    main()
