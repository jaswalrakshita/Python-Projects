questions = [
    {
        "prompt" : "What is capital of India?",
        "options" : ["A. Delhi, B. Shimla, C. Chandigarh, D. Mumbai"],
        "answer" : "A"
    },

     {
        "prompt" : "Which language is majorly spken in India?",
        "options" : ["A. Punjabi, B. Hindi, C. English, D. Tamil"],
        "answer" : "B"
    },

     {
        "prompt" : "Which is national bird of India?",
        "options" : ["A. Owl, B. Kingfisher, C. Sparrow, D. Peacock"],
        "answer" : "D"
    },

     {
        "prompt" : "How many states are there in India?",
        "options" : ["A.25 , B. 26, C. 28, D. 29"],
        "answer" : "C"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)

        user_ans = input("Enter your answer(A, B, C, or D): ").upper()
        if user_ans == question["answer"]:
           print("Correct!!!!\n")
           score += 1
        else:
            print("Not Correct!!. The correct answer is", question["answer"], "\n")
   
    print(f"Your score is {score} out of {len(questions)} questions correct.")

run_quiz(questions)