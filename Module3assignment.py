# Module 3 Assignment
# Carlos Barona

myfile = open('question.txt', 'r+')

myquestion = myfile.read()

myresponce = input(myquestion)

myfile.write(myresponce)

myfile.close()
