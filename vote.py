def check_voting_eligibility():
    print("=== Voter Eligibility Check ===")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    citizenship = input("Are you an Indian citizen? (yes/no): ").strip().lower()

    if age >= 18 and citizenship == "yes":
        print(f"{name}, you are eligible to vote in India.")
    else:
        print(f"{name}, you are NOT eligible to vote in India.")

check_voting_eligibility()
