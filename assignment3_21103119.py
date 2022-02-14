print('Q U E S T I O N  1')
#Initializing null lists
list1=[]
list2=[]
list3=[]
#counting character of a single word
def count_character(str):
    list1=list(str)
#list of characters of input word
    for item in list1:
        if item not in list2:
            list2.append(item)
#Printing occurance of characters in the input word
    for i in range(0,len(list2)):
        print("Number of occurance of ",list2[i],": ",str.count(list2[i]))
#counting words in the input string
def count_word(str):
    word=lower_str.split()
#Making list of unique characters
    for item in word:

        if item not in list3:
            list3.append(item)
#Printing occurance of words in input string
    for q in range(0,len(list3)):
        print("Number of occurance of",list3[q],": ",str.count(list3[q]))
#Taking string as input from user
input_str=str(input("Enter your string:"))
lower_str=input_str.lower()

words_count=len(lower_str.split())
#Using different function for a single word or string
if words_count==1:
    count_character(lower_str)
else:
    count_word(lower_str)


print('Q U E S T I O N  2')
#taking input value of year from user
input_year=int(input('enter a year:'))
#checking if the entered year is a leap year
if (input_year%4==0):               
 leap=True
else:
 leap=False
#taking input value of month from user
input_month=int(input('enter month number:'))
#for months with 31 days
if input_month in (1,3,5,7,8,10,12):
  month_length=31
#for february month
elif input_month==2:
    if leap:
        month_length=29
    else:
         month_length=28
#for months with 30 days                 
else:
    month_length=30
#taking input value of date from user    
input_date=int(input('enter date:'))
#pointing out invalid input date
if(input_date>month_length):
    print('invalid date')
elif(input_month>12):
    print('invalid date')
#printing the next date
elif (input_date<month_length):
    input_date=input_date+1
    print('the next date is:',input_date,'/',input_month,'/',input_year)
elif (input_month==12 and input_date==31):
    input_date=1
    input_month=1
    input_year=input_year+1
    print('the next date is:',input_date,'/',input_month,'/',input_year)
else:
     input_month+=1
     print('the next date is:',input_date,'/',input_month,'/',input_year)
if(input_date>month_length):
    print('invalid date')

print('Q U E S T I O N  3')
#initializing lists
list1=[]
list2=[]
#making a list of the input values 
list1=list(map(int,input('enter numbers separated by space:').split()))
#printing the input values
print('list of numbers entered by the user:',list1)
#sqauring each number and adding them to list2
for k in range (0,len(list1)):
    pairr=(list1[k],list1[k]**2)
    list2.append(pairr)
#printing the required list    
print('required list:',list2)  

print('Q U E S T I O N  4')
#taking input grade from user
grade=int(input('enter a grade from 4 and 10:'))
#creating list for remarks
list1=['Outstanding','Excellent','Very Good','Good','Average','Below Average','Poor']
#creating list for grades
list2=['A+','A','B+','B','C+','C','D']
#linking input grade value with respective remarks and grade
a=list1[10-grade]
b=list2[10-grade]
#printing error message if input grade is invalid
if grade<4 or grade>10:
 print('error')
#printing the required statement
else:
 print('Your Grade is',b,'and',a,'Performance')

print('Q U E S T I O N  5')
rows = 6
#loop for number of rows
for k in range(rows):
#loop for printing spaces
    for j in range(k):
        print(" ", end="")
#loop for printing alphabet
    for j in range(2*(rows-k)-1):
        print(chr(65 + j), end="")
    print()


print('Q U E S T I O N  6')
#initialising dictionaries
dict1=dict()
dict2=dict()
dict3=dict()
dict4=dict()
#creating an infinite while loop to perform looping behaviour
while(1):
#taking input from user to run or end the loop
 choice=str(input('do you want to enter the student details? Y for yes, N for no:'))
 if choice=='Y':
#taking input details of the student from the user     
  name=str(input('enter name of student:'))
  sid=int(input('enter SID of student:'))
#creating dictionary with SID as key value  
  dict1.update({sid:name})
#creating dictionary with name as key value  
  dict2.update({name:sid})
 elif choice=='N':
  break
 else:
  print('invalid input')
#printing student details
print('student details:',dict1)
#sorting dictionary with respect to student name
list1=sorted(dict2)
for a in list1:
    dict3.update({dict2.get(a):a})
print('dictionary sorted by name of the student:',dict3)
#sorting dictionary with respect to student SID
list2=sorted(dict1)
for b in list2:
    dict4.update({dict1.get(b):b})
print('dictionary sorted by SID of the student:',dict4)
#searching student details for the input SID
input_sid=int(input('enter the SID of the student to find their detail:'))
print('name of the student with SID:',input_sid,'is:',dict1[input_sid])

print('Q U E S T I O N  7')
#initialising list of fibonacci series
list1=list()
#fixing first two terms of the fibonacci series
list2=[0,1]
num1=0
num2=1
sum=1
#taking input of the number of terms to be print
count=int(input('enter the number of fibonacci terms you want to print:'))
count1=count
#reducing the first two already fixed terms ie.0,1 from the series count
count1=count1-2
while count1>0:
    num3=num1+num2
#adding new terms to the list2    
    list2.append(num3)
    num1=num2
    num2=num3
#decrementation to end the loop after specified number of loops    
    count1=count1-1
#calculating the sum of series    
    sum=sum+num3
print('the resultant fibonacci series is:',list2)
avg=sum/count
#printing the average of the given fibonacci series
print('average of the resultant fibonacci series is:',avg)

print('Q U E S T I O N  8')
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
list1=list()
#printing the given information
print('set 1:',set1)
print('set 2:',set2)
print('set 3:',set3)
print('part a')
#intersection-union of set 1 and set 2
print('set of elements present in set 1 and set 2 but not in both:',((set1|set2)-(set1&set2)))
print('part b')
set4=set1-set2-set3
set5=set2-set1-set3
set6=set3-set2-set1
print('set of elements present in only set 1:',set4)
print('set of elements present in only set 2:',set5)
print('set of elements present in only set 3:',set6)
set7=set4.union(set5).union(set6)
print('set of elements present in only one of the three sets:',set7)
print('part c')
print('set of elements present in exactly set 1 and set 2:',(set1&set2))
print('set of elements present in exactly set 2 and set 3:',(set2&set3))
print('set of elements present in exactly set 1 and set 3:', (set1&set3))
print('set of elements present in exactly two of the three sets:',(set1&set2).union(set2&set3).union(set1&set3))
print('part d')
#creating a set with integers 1 to 10
for i in range(1,11):
    list1.append(i)
    i+=1
set8=set(list1)    
print('set of integers from 1-10 not in set 1:',(set8-set1))
print('part e')
set9=set8-set1-set2-set3
print('set of integers from 1-10 not in set 1,set 2 and set 3:',set9)
