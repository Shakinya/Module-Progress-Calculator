
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

while True:

    while True:

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

    if pass_credits == 120:
        result = 'Progress'
    elif pass_credits == 100:
        result = 'Progress(Module trailer)'
    elif pass_credits == 80 or pass_credits == 60:
        result = 'Module retriever'
    elif fail_credits >= 80:
        result = 'Exclude'
    else:
        result = 'Module retriever'

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
                   
        
