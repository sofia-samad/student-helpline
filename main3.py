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
        print()
        print("========== CLASS 12 ENGLISH ==========")
        print("1. Textbook Lessons")
        print("2. Grammar")
        print("3. Essays")
        print("4. Poems")

        english_choice = input("What do you want to study? (1-4): ")

        if english_choice == "1":
            lesson = input("Enter the textbook lesson name: ")

            search_text = (
                f"Class 12 Punjab Board English "
                f"textbook lesson {lesson}"
            )

        elif english_choice == "2":
            grammar_topic = input(
                "Enter the grammar topic "
                "(for example, Participles or Forms of Verbs): "
            )

            search_text = (
                f"Class 12 Punjab Board English "
                f"grammar {grammar_topic}"
            )

        elif english_choice == "3":
            essay_topic = input("Enter the essay topic: ")

            search_text = (
                f"Class 12 Punjab Board English "
                f"essay {essay_topic}"
            )

        elif english_choice == "4":
            poem_name = input("Enter the poem name: ")
            poet_name = input("Enter the poet/writer name: ")

            search_text = (
                f"Class 12 Punjab Board English "
                f"poem {poem_name} "
                f"{poet_name} explanation theme"
            )

        else:
            print("Please choose a number from 1 to 4.")
            search_text = None

        if search_text:
            encoded_search = quote(search_text)

            youtube_url = (
                "https://www.youtube.com/results?search_query="
                + encoded_search
            )

            google_url = (
                "https://www.google.com/search?q="
                + encoded_search
            )

            print()
            print("========== SEARCHING ==========")
            print(f"Search: {search_text}")
            print()
            print("Opening YouTube...")
            webbrowser.open(youtube_url)

            print("Opening Google...")
            webbrowser.open(google_url)

    elif subject == "3":
        print()
        print("========== CLASS 12 COMPUTER SCIENCE ==========")
        print("1. Computer Networks")
        print("2. Computational Thinking and Algorithms")
        print("3. Object-Oriented Programming")
        print("4. GUI Development using Python")
        print("5. Database Management")
        print("6. Data and Analysis")
        print("7. Hypothesis Testing")
        print("8. Application of Computer Science")
        print("9. Cybersecurity and Safe Digital Collaboration")

        cs_unit = input("Choose a unit (1-9): ")

        if cs_unit == "1":
            unit_name = "Computer Networks"

        elif cs_unit == "2":
            unit_name = "Computational Thinking and Algorithms"

        elif cs_unit == "3":
            unit_name = "Object-Oriented Programming"

        elif cs_unit == "4":
            unit_name = "GUI Development using Python"

        elif cs_unit == "5":
            unit_name = "Database Management"

        elif cs_unit == "6":
            unit_name = "Data and Analysis"

        elif cs_unit == "7":
            unit_name = "Hypothesis Testing"

        elif cs_unit == "8":
            unit_name = "Application of Computer Science"

        elif cs_unit == "9":
            unit_name = "Cybersecurity and Safe Digital Collaboration"

        else:
            print("Please choose a unit from 1 to 9.")
            unit_name = None

        if unit_name:
            print()
            print(f"========== UNIT {cs_unit}: {unit_name} ==========")

            topic = input("Enter the topic you want to study: ")

            duration = input(
                "Enter the duration you want "
                "(for example, 30 minutes, 1 hour, or 2 hours): "
            )

            search_text = (
                f"Class 12 Punjab Board Computer Science "
                f"Unit {cs_unit} {unit_name} "
                f"topic {topic} "
                f"duration {duration}"
            )

            encoded_search = quote(search_text)

            youtube_url = (
                "https://www.youtube.com/results?search_query="
                + encoded_search
            )

            google_url = (
                "https://www.google.com/search?q="
                + encoded_search
            )

            print()
            print("========== SEARCHING ==========")
            print(f"Unit: {unit_name}")
            print(f"Topic: {topic}")
            print(f"Duration: {duration}")
            print()
            print("Opening YouTube...")
            webbrowser.open(youtube_url)

            print("Opening Google...")
            webbrowser.open(google_url)

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
