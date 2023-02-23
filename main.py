# print('Hello, world!')
### variables pracitce
import math

# for string we can use single quote or double quote
string = "This is a variable named string"
# for printing we have to write print(whatever you want to print)
print("This string is in the print condition and second as using the variable string "+string)
# for printing the data type of the variable you can use print(type(variable name))
print(type(string))
# you can combine the two variables under the third variable if it is of same data type by using the firstvariablename+secondvariablename


#int data type
intr = 21
# we cant use the int in semico as it will be registered as string not int and it will throw error
# for increament we use += sign
intr+=1
print(intr)
print(type(intr))
print("the number is "+str(intr))
# we had to use the str(int) becoz the int is of diff data type and we cant connect it with string so we do the typecasting
# float data
# for declarring float we have to give normal name like int but put .00 or a digit after point
floatt = 15.0
print(floatt)
print(type(floatt))
print("the floating point is "+str(floatt))
# for boolean you can basically write true or false not in the "" as it will become the string data type
boolean = False
print(boolean)
print(type(boolean))
#for typing the string with the boolean we can use the  typecasting to change it to the desired type
print("the boolean variable is "+str(boolean))


###Multipe assignment means giving same value to diff variables using var1=var2=var3 and we can use var1 var2 var3 seperately
var1=var2=var3=25
print(var1, var2, var3)
print(var1+3,var2+5,var3+15)


### string methords use len to print the length of the string
string1= "hello Bro "
print(string1)
print(len(string1))
# the length also counts the spaces as in length
# for finding an specific character in the string you can use the varname.find("character")
# for capitalizing the first letter of the string we can use the varname.capitalize()
print(string1.capitalize())
# for all uppercase or lowercase letters you can use varname.upper() or varname.lower()
print(string1.upper() + string1.lower())
# varname.isdigit() is used to check if the var is the digit or not and varname.isalpha() for checking if its alphaet or not (show false if sapce is in bw)
print(string1.isdigit())
# for counting the freq of a character we use the varname.count("character") ad for replacing the char in string we use the varname.replace("chartobereplaced","chartobereplacedwith")
print(string1.replace("o","a"))
#for displaing a string multiple time we can use the varname*nooftimes
print(string1*3)


###typecasting
# for typecasting we can delcare any var and then convert it into other by typeyouwanttoconvertinto(varname)
xxx= 1
yyy=59.90
zzz="996"
yyy=int(yyy)
print(xxx+yyy)



### User Input
# for user input we use the input near the declared variable
name=input("Enter the name ")
age= input("Enter the age ")
print("Hello"+name+"\nYour age is "+str(age))


###math function
# we can use the round function to round off the int and we can use th emath.floor for the lower value of th enumber and math.ceil to get the higher round of value
pi=3.14
print(str(pi)+" The value before operation \n")
print(round(pi))
print(math.floor(pi))
print(math.ceil(pi))
#how far a no is away from zero is abs function
pi=-3.14
print(abs(pi))
#pow function gives the power to the number that is entered first
print(pow(pi,2))
# math.sqrt is used to make the sq root of the number
print(math.sqrt(599))
q=5
w=6
e=2
# for max or min value of the given set we use max or min function
print(max(q,w,e,pi))
print(min(q,w,e,pi))


### Slicing =create a substring by extracting elements from other string
# indexing[] or slice()
#[start:stop:step]
egindexing="Hello Motherfuckers How are you"
first_letter=egindexing[0:5]
second_letter=egindexing[5:19]
# for putting a starting element to ending elemnt skipping 1 value we can write stringname[::1]
funky_string=egindexing[1:99:3]
print(" The main string "+egindexing+"\n The first indexing "+first_letter+"\n The second letter " +second_letter+"\n Funky string "+funky_string)
reversed=egindexing[::-1]
print("The reversed string is :"+reversed)
# the slice does the same thing as the indexing[] but instead of : it uses ,
web1="https://google.com"
web2="https://facebook.com"
slice=slice(8,-4)
print(web1[slice])
print(web2[slice])


### conditional statement
# if statement the code should follow the indentation of the if block
#in python the indentation makes the block instead of {..}.{indentation means spaces before writing the code}
ageif=int(input("enter the age for if block "))
if ageif >= 18:
    print("You are a adult"+"\nThe age of the person is "+str(ageif))
    # the order of if statement matters a lot and you cant use the elif after else as u have exitted the ifelse block
elif ageif < 0:
    print("Enter the valid age")
else:
    print("You are a child"+"\nThe age is "+str(ageif))

##logical operator (and or)
temp=int(input("Enter the temperature: \n"))
if temp>0 and temp<30:
    print("The temp is good go outside\n.")
elif temp<0 or temp>30:
    print("The temp is not goo. sit back and relax")
else:
    print("Go fk urself")
## While loop = a blockk of code which runs until condition is true.
# while 1==1:
#     print("This is a infinite loop")
namewhle = ""
# another way of writing while len(namewhle) == 0 is
while len(namewhle) == 0:
    namewhle = input("Enter the name: ")
print("Hello " + namewhle )
