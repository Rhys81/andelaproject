#Welcome User
#Get User Name
import os.path
def write_user_to_users_file(username):
    if os.path.isfile(str('usernames.txt')):
        print 'File Exists'
        write_to_usernames=open('usernames.txt','r')
        available_users=[]
        #print "Checking q"
        for user in write_to_usernames:
            available_users.append(user)
            #print "Checking"
        if username in available_users:
            #Do Noth
            write_to_usernames.close()
        else:
            write_to_usernames=open('usernames.txt','a')
            write_to_usernames.write("\n")
            write_to_usernames.write(username)
    else:
        write_to_usernames=open('usernames.txt','a')
        #print 'File Created'
        write_to_usernames.write("\n")
        write_to_usernames.write(username)
        #print username

def user_day(username,tasks,D,task_done):
    tas=open(username+str(D)+'.txt','a')
    #[OOP,Growth Mindset,Agile] 1
    #2
    #3
    #4
    for i in tasks:
         tas.write(i+"\n")
    done=[]
    if task_done>0:
        done.append(tasks[task_done-1])
    done_tas=open(username+str(D)+"done"+'.txt','a')
    for i in done:
         done_tas.write(i+",")
    print 'Done'
def out_put(username,D):
    f=open(username+str(D)+"done"+'.txt','r')
    done=[]
    for dtasks in f:
        done.append(dtasks)
    return done
        
#write_user_to_users_file("esir")
#user_day("esir",['OOP','Agile','Data'],1,3)
#print out_put('esir',1)

username=input('Enter Username')
day1=['OOP','Version Control']
day2=['Check Growth ','Blog']
day3=['Agile','Data Types']
day4=['Unit Testing','Repository']

all=day1+day2+day3+day4
for a in all:
    print a

day=input("Day To Track")
taskDone=input("Task Done")
write_user_to_users_file(username)
user_day(username,day1,day,taskDone)
print out_put(username,day)
