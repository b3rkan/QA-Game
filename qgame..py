questions = [
    {
        "promt": "Who is the rythm guitarist of Metallica? ",
        "options": ["A. Mick Thomson", "B. Jimi Hendrix", "C. James Hetfield", "D. Dave Mustaine"],
        "answer": "C"

    },
    {
        "promt": "In what year was Slipknot founded by Shawn Crahan?",
        "options": ["A. 1998", "B. 1996", "C. 1991", "D. 1995"],
        "answer": "D"


    },
    {
        "promt": "Which album is the mostselled album?",
        "options":["A. Thriller by Michael Jackson", "B. Metallica by Metallica", "C. The Dark Side of The Moon by Pink Floyd", "D. Back in Black by AC/DC"],
        "answer": "A"


    },
    {
        "promt": "Which year Elvis Presley died by heart attack?",
        "options": ["A. 1983", "B. 1978", "C. 1981", "D. 1977"],
        "answer":"D"


    },
    {
        "promt": "Who founded Metallica?",
        "options": ["A. James Hetfield", "B. Lars Ulrich", "C. James Hetfield and Lars Ulrich","D. James Hetfield and Dave Mustaine"],
        "answer": "C"
    }

]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["promt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, D) : \n").upper()
        if answer == question["answer"]:
            print("Correct, Welldone ! 😊 \n")
            score += 1
        else:
            print("Not correct 😥\n")

    print(f"You got {score} out of {len(questions)} questions correct.")




run_quiz(questions)        

