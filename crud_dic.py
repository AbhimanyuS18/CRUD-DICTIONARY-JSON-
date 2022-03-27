
dic={}
while True:
    print("""
    aap kya chahate ho
    press 1 for create
    press 2 for read
    press 3 for update
    press 4 for delete
    press 5 for exit """
    )

    choice=int(input(' your choice :- '))

    if choice==1:
        a=int(input('enter your number :- '))
        a1={'name':input('enter your name'),
            'email':input('enter your email')}
        dic[a]=a1
    elif choice==2:
        number=int(input('enter your number :- '))
        if number in dic:
            print(dic[number])
        else:
            print('not exist ')
    elif choice==3:
        number=int(input('enter your number :- '))
        if number in dic:
            a=int(input('enter your number :- '))
            a1={'name':input('enter your name'),
                'email':input('enter your email')}
            dic[a]=a1
        else:
            print('not exist ')
    elif choice==4:
        number=int(input('enter your number :- '))
        if number in dic:
            dic.pop(number)
        else:
            print('not exist ')
    elif choice==5:
        break
    




