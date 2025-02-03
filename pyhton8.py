 # control statements-- controls flow of exceution of a code.
#control statements-- conditional statements, loops, and jump statements.


#conditional statements-- if or else

print("good_morning")
print("good_evening")
num1 = 0
if num1 == 1:
  print("good_morning")
else:
  print("good_evening")
  print("code excutes successfully")
  print("code ended")

#if num2>0 then print positive else print negative
num2 = 0
if num2>0:
  print("positive")
else:
  if num2==0:
    print("zero")
  else:
    print("negative")


num1= 6
if num1>10:
  print("greater than")
else:
  if num1==0:
    print("zero")
  else:
    print("six")   


#else if --- elif--- nested statements
num1= -2
if num1>0:
  print("positive")
elif num1==0:
  print("zero")
elif num1==-1:
  print("-1")
else:
  print("negative")

num1= 10
if num1==0:
  print("zero")
elif num1 == -10:
  print("-10")
elif num1 == 20:
  print("20")
else:
  print("10")

#for loop and while loop
for y in range(0,21):
  print(y)
  print(y+5)
  print("else")
  print("hello world")
for i in range (5, 25):
  print(i)
for z in range(0, 15):
  if z % 2 == 0:
    print(z, 'even')
  else:
    print(z, 'odd')
for a in range(0, 21, 2):
  print(a)
for b in range(0,21,3):
  print(b)
for c in range(0,21):
  if c % 3 == 0:
    print(c)
for d in range(0, 10):
  print(d*d)#squares
  print(d*d*d)#cubes
  print(d ** 2)
  print(d ** 3)

#nested loops:
for i in range (1, 21):
  print(i)
for j in range(1,11):
  if j != 5 and j != 7:
    for i in range(1, 31):
      print(j, i)



#while loop

num1= 10
while num1<12:
  print("hello")
  print("my world")
  num1 += 1 

start = 10
while start<26:
  if start % 2 == 0:
    print(start, 'even')
  else: 
    print(start, 'odd')
  start  += 1 


#jump statements -- break, continue and pass
 # break and continue -- we use in loops

for i in range(0,21):
  if i % 2 == 0:
    print(i)

    if i == 0:
      break

for i in range (0, 31):
  if i == 2 or i == 5:
    break

#continue
for i in range(0, 10):
  if i == 5:
    continue
  print(i)

for i in range(0, 10):
  print(i)
  if i == 5:
    break
print("loop ended")

#break and continue for nested loops

for cls1 in range (1,11):
  for roll in range(1,30):
    print(cls1,roll)
  if cls1 == 5:
    continue
  print(cls1, roll)

for cls1 in range(1, 12):
  for roll in range(1,30):
    if cls1==3 and roll>14:
      continue
    print(cls1, roll)
  


#pass
num1= 15
if num1 % 7 ==0: 
  pass
else:
  print("something something")

