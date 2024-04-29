Template="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice
questions from the given text of {tone} level.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format you response like RESPONSE_JSON below and use it as a guide. 
Ensure to make {number} questions.
### RESPONSE_JSON
{response_json}
"""


Template_2="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""