
#1 print 'hello' 5 times using an arithmetic operator
print("hi"*5)


#2 print 'hello' 5 times using a loop
cnt = 0
while cnt < 5: 
    print('hello')
    cnt += 1

#3 print 'hello' 5 times on the same line using a loop
count=0
while count < 5:
  print('hello', end= ' ')
  count += 1
  print ( )




#4  using nested loops print the following:
'''
00 01 02
10 11 12
20 21 22

'''
for row in range(3):        # outer loop for rows
    for col in range(3):    # inner loop for columns
        print(str(row)+str(col), end=" ")
    print()  # moves to the next line after each row
print()

#5 define txt and input some text from the keyboard into it

txt= 'enter name'
choice= (input(txt))



#6 print each letter in txt 

txt= 'enter name'
choice=(input(txt))
print(choice)

#7 assign the variable letter to the first letter in txt

choice_txt='enter name'
name=(input(choice_txt))
print(txt)
letter = txt[0]

#8 print out all the letters in txt that are equal to the first letter

'''
say txt = 'the cat in the hat was read today'
't' is the first letter

result: tttt
'''
choice_txt= 'enter name'
txt = (input(txt))
letter= txt[0]
if txt == letter:
    print(letter)


'''
#9 suppose we had a list of n elements. create a new list that
  shifts the elements by 3

    myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
      shifted_list = ['pear', 'blueberry', 'peach', 'apple', 'orange']

        Hints:
             1) use len(), %, enumerate
             2) also assign shifted_list = [None] * length  (you'll need to determine 
                the length variable)
             3) shift inside the for loop
             4) print out the printed list outside the for loop
'''

myList = ['apple', 'orange', 'pear', 'blueberry', 'peach']
length= len(myList)
shifted_list=[None]* length

shift = 3

for idx in range(length):
  new_idx = (idx + 3) % length
  shifted_list[new_idx] = myList[idx]
print(shifted_list)                                 
                                    

for idx,item in enumerate(myList):
   print(idx, item)