
import json,os
print('''
1.create
2.update
3.delete
''')


def create():
    if (os.path.exists('crud.json')):
        a= open('crud.json','r')
        b=json.load(a)
        c={}
        c['name']=input('enter name')
        c['e-mail']=input('enter e-mail')
        c['password']=input('enter password')
        b.append(c)
        f=open('crud.json','w')
        json.dump(b,f,indent=4)
        print("create data")

    else:
        b=[]
        c={}
        c['name']=input('enter name :')
        c['e-mail']=input('enter e-mail :')
        c['password']=input('enter password :')
        b.append(c)
        f=open('crud.json','w')
        json.dump(b,f,indent=4)
        print("create data")


def update():
    s=open('crud.json','r')
    d=json.load(s)
    q=input('enter your e-mail :')
    g=0
    for i in d:
        if i['e-mail']==q:
            h={}
            h['name']=input('enter name :')
            h['e-mail']=q
            h['password']=input('enter password :')
            d[g]=h

            e=open ('crud.json','w')
            json.dump(d,e,indent=4)
            print('data update')
        else:
            print('invalid e-mail')
            break


def delete():
    a=input('enter your e- mail :')
    b=input('enter your paasword :')
    c=open('crud.json','r')
    d=json.load(c)
    for i in d:
        if i['e-mail']==a and i['password']==b:
            d.remove(i)
            print('remove succesfull')
            e=open('crud.json','w')
            json.dump(d,e,indent=4)
            return
            print('data not find')

w=int(input('your choice :'))
if w==1:
    create()
elif w==2:
    update()
else:
    delete()



# print(
#     """ 1.log in 
#     2. sign up
#     """
# )


##############INSTA###############

# from turtle import* 
# bgcolor('black')
# color('cyan')
# speed(11)
# right(45)
# for i in range(150):
#     circle(30)
#     if 7 < i < 62:
#         left(5)
#     if 80 < i < 133:
#         right(5)
#     if i<80:
#         forward(10)
#     else:
#         forward(5)


####################discurd que


# def multi(a):
#     for i in range(1,11):
#         if i%a:
#             print(a,'*',i,'=',a*i)
# a=eval(input('num'))
# multi(a)
	
	