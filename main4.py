    elif subject == "4":
        print()
        print("========== SCIENCE ==========")
        print("1. Physics")
        print("2. Chemistry")
        print("3. Biology")

        science_subject = input("Choose a subject (1-3): ")

        if science_subject == "1":
            print()
            print("========== CLASS 12 PHYSICS ==========")
            print("13. Thermal Physics")
            print("14. Simple Harmonic Motion")
            print("15. Physical Optics")
            print("16. Electrostatics")
            print("17. Alternating Current")
            print("18. Quantum Physics")
            print("19. Nuclear and Particle Physics")
            print("20. Medical Physics")
            print("21. Space Environment")

            physics_chapter = input("Choose a chapter (13-21): ")

            if physics_chapter == "13":
                chapter_name = "Thermal Physics"

            elif physics_chapter == "14":
                chapter_name = "Simple Harmonic Motion"

            elif physics_chapter == "15":
                chapter_name = "Physical Optics"

            elif physics_chapter == "16":
                chapter_name = "Electrostatics"

            elif physics_chapter == "17":
                chapter_name = "Alternating Current"

            elif physics_chapter == "18":
                chapter_name = "Quantum Physics"

            elif physics_chapter == "19":
                chapter_name = "Nuclear and Particle Physics"

            elif physics_chapter == "20":
                chapter_name = "Medical Physics"

            elif physics_chapter == "21":
                chapter_name = "Space Environment"

            else:
                print("Please choose a chapter from 13 to 21.")
                chapter_name = None

            if chapter_name:
                print()
                print(
                    f"========== CHAPTER {physics_chapter}: "
                    f"{chapter_name} =========="
                )

                topic = input("Enter the topic you want to study: ")

                duration = input(
                    "Enter the duration you want "
                    "(for example, 30 minutes, 1 hour, or 2 hours): "
                )

                search_text = (
                    f"Class 12 Punjab Board Physics "
                    f"Chapter {physics_chapter} {chapter_name} "
                    f"topic {topic} duration {duration}"
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
                print(f"Chapter: {chapter_name}")
                print(f"Topic: {topic}")
                print(f"Duration: {duration}")
                print()
                print("Opening YouTube...")
                webbrowser.open(youtube_url)

                print("Opening Google...")
                webbrowser.open(google_url)

        elif science_subject == "2":
            print()
            print("========== CLASS 12 CHEMISTRY ==========")
            print("17. Group 2 Elements")
            print("18. Transition Metals")
            print("19. Basics of Organic Chemistry")
            print("20. Aromatic Hydrocarbons")
            print("21. Halogenoalkanes")
            print("22. Hydroxy Compounds")
            print("23. Carbonyl Compounds and Carboxylic Acids")
            print("24. Organic Nitrogen Compounds")
            print("25. Organic Synthesis")
            print("26. Polymers")
            print("27. Biochemistry")
            print("28. Chromatography")
            print("29. Spectrography")
            print("30. Spectroscopy to NMR")
            print("31. Material and Energy")
            print("32. Medical, Agriculture and Industry")
            print("33. Water")

            chemistry_chapter = input("Choose a chapter (17-33): ")

            if chemistry_chapter == "17":
                chapter_name = "Group 2 Elements"

            elif chemistry_chapter == "18":
                chapter_name = "Transition Metals"

            elif chemistry_chapter == "19":
                chapter_name = "Basics of Organic Chemistry"

            elif chemistry_chapter == "20":
                chapter_name = "Aromatic Hydrocarbons"

            elif chemistry_chapter == "21":
                chapter_name = "Halogenoalkanes"

            elif chemistry_chapter == "22":
                chapter_name = "Hydroxy Compounds"

            elif chemistry_chapter == "23":
                chapter_name = (
                    "Carbonyl Compounds and Carboxylic Acids"
                )

            elif chemistry_chapter == "24":
                chapter_name = "Organic Nitrogen Compounds"

            elif chemistry_chapter == "25":
                chapter_name = "Organic Synthesis"

            elif chemistry_chapter == "26":
                chapter_name = "Polymers"

            elif chemistry_chapter == "27":
                chapter_name = "Biochemistry"

            elif chemistry_chapter == "28":
                chapter_name = "Chromatography"

            elif chemistry_chapter == "29":
                chapter_name = "Spectrography"

            elif chemistry_chapter == "30":
                chapter_name = "Spectroscopy to NMR"

            elif chemistry_chapter == "31":
                chapter_name = "Material and Energy"

            elif chemistry_chapter == "32":
                chapter_name = "Medical, Agriculture and Industry"

            elif chemistry_chapter == "33":
                chapter_name = "Water"

            else:
                print("Please choose a chapter from 17 to 33.")
                chapter_name = None

            if chapter_name:
                print()
                print(
                    f"========== CHAPTER {chemistry_chapter}: "
                    f"{chapter_name} =========="
                )

                topic = input("Enter the topic you want to study: ")

                duration = input(
                    "Enter the duration you want "
                    "(for example, 30 minutes, 1 hour, or 2 hours): "
                )

                search_text = (
                    f"Class 12 Punjab Board Chemistry "
                    f"Chapter {chemistry_chapter} {chapter_name} "
                    f"topic {topic} duration {duration}"
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
                print(f"Chapter: {chapter_name}")
                print(f"Topic: {topic}")
                print(f"Duration: {duration}")
                print()
                print("Opening YouTube...")
                webbrowser.open(youtube_url)

                print("Opening Google...")
                webbrowser.open(google_url)

        elif science_subject == "3":
            print()
            print("========== CLASS 12 BIOLOGY ==========")
            print("13. Thermoregulation and Osmoregulation")
            print("14. Human Excretory System")
            print("15. Human Nervous System")
            print("16. Human Endocrine System")
            print("17. Human Reproductive System")
            print("18. Inheritance")
            print("19. Chromosomes and DNA")
            print("20. Biotechnology")
            print("21. Immunity")
            print("22. Biostatistics")
            print("23. Pharmacology")
            print("24. Evolution")
            print("25. Ecology")

            biology_chapter = input("Choose a chapter (13-25): ")

            if biology_chapter == "13":
                chapter_name = "Thermoregulation and Osmoregulation"

            elif biology_chapter == "14":
                chapter_name = "Human Excretory System"

            elif biology_chapter == "15":
                chapter_name = "Human Nervous System"

            elif biology_chapter == "16":
                chapter_name = "Human Endocrine System"

            elif biology_chapter == "17":
                chapter_name = "Human Reproductive System"

            elif biology_chapter == "18":
                chapter_name = "Inheritance"

            elif biology_chapter == "19":
                chapter_name = "Chromosomes and DNA"

            elif biology_chapter == "20":
                chapter_name = "Biotechnology"

            elif biology_chapter == "21":
                chapter_name = "Immunity"

            elif biology_chapter == "22":
                chapter_name = "Biostatistics"

            elif biology_chapter == "23":
                chapter_name = "Pharmacology"

            elif biology_chapter == "24":
                chapter_name = "Evolution"

            elif biology_chapter == "25":
                chapter_name = "Ecology"

            else:
                print("Please choose a chapter from 13 to 25.")
                chapter_name = None

            if chapter_name:
                print()
                print(
                    f"========== CHAPTER {biology_chapter}: "
                    f"{chapter_name} =========="
                )

                topic = input("Enter the topic you want to study: ")

                duration = input(
                    "Enter the duration you want "
                    "(for example, 30 minutes, 1 hour, or 2 hours): "
                )

                search_text = (
                    f"Class 12 Punjab Board Biology "
                    f"Chapter {biology_chapter} {chapter_name} "
                    f"topic {topic} duration {duration}"
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
                print(f"Chapter: {chapter_name}")
                print(f"Topic: {topic}")
                print(f"Duration: {duration}")
                print()
                print("Opening YouTube...")
                webbrowser.open(youtube_url)

                print("Opening Google...")
                webbrowser.open(google_url)

        else:
            print("Please choose a subject from 1 to 3.")
