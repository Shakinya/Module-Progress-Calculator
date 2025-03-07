
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID : w1985734
# IIT No : 20222163
# Date : 21/04/2023

'''
References
 1.https://www.guru99.com/python-tutorials.html
 2.https://www.w3schools.com/python/python_intro.asp
 3.Lecture materials & Tutorial materials
 
'''

progress = 0
trailer = 0
retriever = 0
exclude = 0
no_of_outcomes = 0

pass_list = []
defer_list = []
fail_list = []
result_list = []
student_list = []

student_dict = {}


while True:

    while True:
        student_ID = str(input('Please enter your Student ID : '))

        while True:
            pass_credits = input('Please enter your credits at pass: ')
            try:
                pass_credits = int(pass_credits)
                if pass_credits not in range(0,121,20):
                    print(' \nOut of range! ')
                    print('Please try again!! \n')
                else:
                    break
            except ValueError:
                print(' \nInteger required! ')
                print('Please try again!! \n')

        while True:   
            defer_credits = input('Please enter your credits at defer: ')
            try:
                defer_credits = int(defer_credits)
                if defer_credits not in range(0,121,20):
                    print(' \nOut of range! ')
                    print('Please try again!! \n')
                else:
                    break
            except ValueError:
                print(' \nInteger required! ')
                print('Please try again!! \n')

        while True:
            fail_credits = input('Please enter your credits at fail: ')
            try:
                fail_credits = int(fail_credits)
                if fail_credits not in range(0,121,20):
                    print(' \nOut of range! ')
                    print('Please try again!! \n')
                else:
                    break
            except ValueError:
                print(' \nInteger required! ')
                print('Please try again!! \n')

        total_credits = pass_credits + defer_credits + fail_credits
        if total_credits == 120:
            break
        else:
            print(' \nTotal incorrect! ')
            print('Please try again!! \n')

            
    student_list.append(student_ID)       
    if pass_credits == 120:
        result = 'Progress'
        result_list.append('Progress')
        
    elif pass_credits == 100:
        result = 'Progress(Module trailer)'
        result_list.append('Progress(Module trailer)')
        
    elif pass_credits == 80 or pass_credits == 60:
        result = 'Module retriever'
        result_list.append('Module retriever')
        
    elif fail_credits >= 80:
        result = 'Exclude'
        result_list.append('Exclude')
    else:
        result = 'Module retriever'
        result_list.append('Module retriever')

    print(result, '\n')

    if result == 'Progress':
        progress += 1
    elif result == 'Progress(Module trailer)':
        trailer += 1
    elif result == 'Module retriever':
        retriever += 1
    else:
        exclude += 1

    no_of_outcomes += 1

    pass_list.append(pass_credits)
    defer_list.append(defer_credits)
    fail_list.append(fail_credits)

    Repeat = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results : ")
    Repeat = Repeat.lower()
    print('')
    if Repeat == 'q':
        break
    elif Repeat == 'y':
        continue
    

print('-' * 50)
print('Histogram ')
print(f'Progress   {progress} :', progress * '*')
print(f'Trailer    {trailer} :', trailer * '*')
print(f'Retriever  {retriever} :', retriever * '*')
print(f'Exclude    {exclude} :', exclude * '*', '\n')
print(no_of_outcomes, 'Total of outcomes.')
print('-' * 50)

for i in range(no_of_outcomes):
    print(f'{result_list[i]} - {pass_list[i]},{defer_list[i]},{fail_list[i]}')
    results = ' %s - %d, %d, %d' % (result_list[i],pass_list[i],defer_list[i],fail_list[i])
    student_dict.update({student_list[i] : results})
    

file = open('20222163_shakinya.txt', 'w')
for i in range (no_of_outcomes):
    file.write(f'{result_list[i]} - {pass_list[i]}, {defer_list[i]}, {fail_list[i]} \n')
file.close()

print('')
for key,value in student_dict.items():
    print (key, ':', value)
        

