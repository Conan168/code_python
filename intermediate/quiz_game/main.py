"""quiz game"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    """main function"""

    question_bank = []

    for question in question_data:
        question_bank.append(
            Question(q_text=question["question"], q_answer=question["correct_answer"]))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You have completed the quiz")
    print("==================================")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


if __name__ == '__main__':
    main()
