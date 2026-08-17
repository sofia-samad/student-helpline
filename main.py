import webbrowser
from urllib.parse import quote

print("===================================")
print("        WELCOME TO STUDENT HUB")
print("===================================")
print()
print("A simple place to help students")
print("stay organized, learn, and discover")
print("useful educational opportunities.")
print()

name = input("What's your name? ")

print()
print(f"Welcome, {name}! 👋")
print("Let's make your student life a little easier.")
print()
print("What would you like help with?")
print("1. Study Resources")
print("2. Assignment Tracker")
print("3. Scholarships & Opportunities")
print("4. Study Planner")

choice = input("Choose an option (1-4): ")

print()
print(f"You selected option {choice}.")

if choice == "1":
    print()
    print("========== STUDY RESOURCES ==========")
    print("1. Mathematics")
    print("2. English")
    print("3. Computer Science")
    print("4. Science")

    subject = input("Choose a subject (1-4): ")

    if subject == "1":
        print()
        print("========== MATHEMATICS ==========")

        chapter = input("Choose a chapter (1-11): ")

        if chapter in [str(i) for i in range(1, 12)]:
            print()
            print(f"========== CHAPTER {chapter} ==========")
            print(f"Chapter {chapter} selected.")

            exercise = input(
                f"Enter the exercise you want (for example, {chapter}.1, {chapter}.2): "
            )

            if exercise.startswith(chapter + "."):
                print()
                print("========== CHOOSE YOUR TEACHER ==========")
                print("1. Sir Shahzad Sair")
                print("2. Knowledge Zone")

                teacher = input("Choose a teacher (1-2): ")

                if teacher == "1":
                    teacher_name = "Sir Shahzad Sair"
                elif teacher == "2":
                    teacher_name = "Knowledge Zone"
                else:
                    print("Please choose 1 or 2.")
                    teacher_name = None

                if teacher_name:
                    search_text = (
                        f"Class 12 Mathematics Chapter {chapter} "
                        f"Exercise {exercise} {teacher_name}"
                    )

                    youtube_url = (
                        "https://www.youtube.com/results?search_query="
                        + quote(search_text)
                    )

                    print()
                    print(f"Searching YouTube for Exercise {exercise}...")
                    print(f"Teacher: {teacher_name}")

                    webbrowser.open(youtube_url)

            else:
                print(f"Please enter an exercise from Chapter {chapter}.")

        else:
            print("Please choose a chapter from 1 to 11.")

    elif subject == "2":
        print("English resources coming soon!")

    elif subject == "3":
        print("Computer Science resources coming soon!")

    elif subject == "4":
        print("Science resources coming soon!")

    else:
        print("Please choose a number from 1 to 4.")

elif choice == "2":
    print("Assignment Tracker coming soon!")

elif choice == "3":
    print("Scholarships & Opportunities coming soon!")

elif choice == "4":
    print("Study Planner coming soon!")

else:
    print("Please choose an option from 1 to 4.")
