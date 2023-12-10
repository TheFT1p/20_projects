import random
import os
# dict import capitals
# os.chdir(r"C:\Users\DusanS\20 projects\20-python-project\generate-random-quiz-files")
# print(os.getcwd())
capitals = {'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois':'Springfield',
'Indiana': 'Indianapolis',
'Iowa': 'Des Moines',
'Kansas':'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine':'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan':'Lansing',
'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson',
'Missouri':'Jefferson City',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada':'Carson City',
'New Hampshire': 'Concord',
'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe',
'New York': 'Albany',
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee':'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont':'Montpelier',
'Virginia': 'Richmond',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}

# question_with_choices = dict()
# for question in capitals:
#     correct_answer = capitals[question]
#     values_list = list(capitals.values())
#     incorrect_questions = random.sample(values_list, 3)
#     choices = [correct_answer] + incorrect_questions
#     random.shuffle(choices)
#     question_with_choices[question] = choices
# question_list = list(question_with_choices.items())
# shuffled_list = dict(question_list)

def make_quiz():
    global capitals
    for question in capitals:
        correct_answer = capitals[question]
        values_list = list(capitals.values())
        incorrect_questions = random.sample(values_list, 3)
        choices = [correct_answer] + incorrect_questions
        random.shuffle(choices)
        question_with_choices[question] = choices
    question_list = list(question_with_choices.items())
    random.shuffle(question_list)
    shuffled_list = dict(question_list)
    return shuffled_list
def make_keys(quiz):
    answers = dict()
    global capitals
    for key in quiz:
        answers[key] = capitals[key]
    return  answers


def generate_random_quiz_files():
    # Create a directory to store quiz and answer key files
    if not os.path.exists('quizzes'):
        os.mkdir('quizzes/')
    if not os.path.exists('quizzes/questions'):
        os.makedirs('quizzes/questions')
    if not os.path.exists('quizzes/answers'):
        os.makedirs('quizzes/answers')
        
    # Generate 35 quiz files.
    for quizNum in range(35):
        # Create the quiz and answer key files.
        # add other comments
        nameTest = r'C:\Users\DusanS\20 projects\20-python-project\generate-random-quiz-files\quizzes\questions\Test_'+str(quizNum)+'.csv'
        nameAnswer = r'C:\Users\DusanS\20 projects\20-python-project\generate-random-quiz-files\quizzes\answers\Key_'+str(quizNum)+'.csv'
        with open(nameTest, 'w+', encoding="utf-8") as testFajl:
            quiz = make_quiz()
            keys = make_keys(quiz)
            testFajl.write(str(quiz))
            with open(nameAnswer, 'w+', encoding='utf-8') as keyFajl:
                keyFajl.write(str(keys))













if __name__ == '__main__':
    generate_random_quiz_files()
    
