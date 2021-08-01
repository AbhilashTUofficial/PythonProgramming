# Python            ->      Json   #
# ---------------------------------#
# dict              ->      object #
# list, tuple       ->      array  #
# str               ->      String #
# int, long, float  ->      number #
# True              ->      true   #
# False             ->      false  #
# None              ->      null   #
#----------------------------------#

import json


q1= {
            "category": "Entertainment: Japanese Anime & Manga",
            "type": "multiple","difficulty": "easy",
            "question": "What is the name of the stuffed lion in Bleach?",
            "correct_answer": "Kon",
            "incorrect_answers": [
                "Jo",
                "Urdiu",
                "Chad"
            ]
        }
q2= {
            "category": "Entertainment: Japanese Anime & Manga",
            "type": "multiple",
            "difficulty": "easy",
            "question": "What is the age of Ash Ketchum in Pokemon when he starts his journey?",
            "correct_answer": "10",
            "incorrect_answers": [
                "11",
                "12",
                "9"
            ]
        }
q3= {
            "category": "Entertainment: Japanese Anime & Manga",
            "type": "multiple",
            "difficulty": "easy",
            "question": "In &quot;Future Diary&quot;, what is the name of Yuno Gasai's Phone Diary?",
            "correct_answer": "Yukiteru Diary",
            "incorrect_answers": [
                "Murder Diary",
                "Escape Diary ",
                "Justice Diary "
            ]
        }
q4= {
            "category": "Entertainment: Japanese Anime & Manga",
            "type": "multiple",
            "difficulty": "easy",
            "question": "Satella in 'Re:Zero' is the witch of what?",
            "correct_answer": "Envy",
            "incorrect_answers": [
                "Pride",
                "Sloth",
                "Wrath"
            ]
        }
q5= {
            "category": "Entertainment: Japanese Anime & Manga",
            "type": "multiple",
            "difficulty": "easy",
            "question": "In the anime 'My Hero Academia', which character is shown with the ability to manipulate gravity?",
            "correct_answer": "Uraraka",
            "incorrect_answers": [
                "Bakugo",
                "Deku",
                "Asui "
            ]
        }

q_array1={'results':[q1,q2,q3,q4,q5]}

class question:
    def __init__(self,category,type,difficulty,question,correct_answer,incorrect_answers):
        self.category=category
        self.type=type
        self.difficulty=difficulty
        self.question=question
        self.correct_answer=correct_answer
        self.incorrect_answers=incorrect_answers

q6=question("Entertainment: Japanese Anime & Manga",
            "multiple",
            "easy",
            "In the anime 'My Hero Academia', which character is shown with the ability to manipulate gravity?",
            "Uraraka",
            [
                "Bakugo",
                "Deku",
                "Asui "
            ]
            )

def encodePyClass(x):
    if isinstance(x,question):
        return {'category':x.category,'type':x.type,'difficulty':x.difficulty,'question':x.question,'correct_answer':x.correct_answer,'incorrect_answers':x.incorrect_answers}
    else:
        print("Encoding failed!");

#---------------or-----------------#

from json import JSONEncoder
class overrideJEncoder(JSONEncoder):
    def default(self, x):
        if isinstance(x,question):
            return {'category':x.category,'type':x.type,'difficulty':x.difficulty,'question':x.question,'correct_answer':x.correct_answer,'incorrect_answers':x.incorrect_answers}
        else:
            print("Encoding failed!");

def encodePyDict(x):
    if question.__name__ in x:
        return(question(category=x['category'],type=x['type'],difficulty=x['difficulty'],question=x['question'],correct_answer=x['correct_answer'],incorrect_answers=x['incorrect_answers']))
    print("Encoding failed!");


# Convert Python dict to JSON format
def pyDict2JString(q):
    q=json.dumps(q,indent=4);
    # separators('<current separators>','<new separators>')
    # sort_keys=True -> sort the keys in alphabetical order, default : False
    print(q);

# Convert Python dict and write to a json file
def pyDict2JFile():
    with open('Learning/Intermediate/Json/data.json','w') as file:
        json.dump(q_array1,file,indent=4);

# Convert JSON string (dumps) to Python dict
def jString2PyDict(q):
    q=json.loads(q);
    print(q);

# Convert json file, Convert to Python dict
def jFile2PyDict():
    with open('Learning/Intermediate/Json/data.json','r') as file:
        print(json.load(file));

# Convert Python class to JSON string
def pyClass2Jstring(q):
    q=json.dumps(q,default=encodePyClass)
    print(overrideJEncoder().encode(q))
    print(q)

pyClass2Jstring(q6)
# Convert Python class to Json file
def pyClass2JFile(q):
    with open('Learning/Intermediate/Json/data.json','w') as file:
        json.dump(q,file,indent=4,default=overrideJEncoder);

# Convert Json string to Python string
def jString2PyString(q):
    print(json.loads(overrideJEncoder().encode(q)));
