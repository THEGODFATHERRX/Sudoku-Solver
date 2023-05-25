import time

input = [                        # INPUT , Enter 0 in empty spaces.
[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,0,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0],
]

import copy
data = [0 for i in range(1000)] # initiates list
data[0] = input   # maintains copy/Stores data

def possibilities(Y,X,mino):  #this programs finds the possible Nos in a particular place
  possible = [1,2,3,4,5,6,7,8,9]   #possibilities, 1 to 9
  
  #checks horizontally
  for i in data[mino][Y]:  
    if i == 0:
      continue
    elif i in possible:
      possible.remove(i)
  
  # checks vertically
  vertical = [data[mino][i][X] for i in range(0,9)] 
  for i in vertical:  
    if i == 0:
      continue
    elif i in possible:
      possible.remove(i)
  
  #checks in the Box 3x3
  box = [data[mino][i][(X//3)*3:((X//3)*3+3)] for i in range((Y//3)*3,(Y//3)*3+3)] #creates 3X3 box by dviding X & Y cordinate by 3 and discarding remainder, this creates partitions which are equal to the one made in sudoku, so 0,1,2(0,1,2 // 3 = 0) on x belongs to one partitions and 3,4,5(3,4,5 // 3 = 1) to another and 6,7,8(6,7,8 //3 = 2) another and similarly on Y   
  for k in range(0,3):  
    for i in box[k]: 
      if i == 0:
        continue
      elif i in possible:
        possible.remove(i) 
  return possible    


a = 1 #implement to check change, this value is set to Input afterwards, if no change is detected after the   


possibles = [0 for i in range(1000)]  #store possibiles for future use

def replacer(mino,k): # k here is the number of possibilities it is going to go through
  global a
  global possibles
  global data
  #checks if sudoku is complete/solved
  if any(0 in subl for subl in data[mino]) == False:
    print(data[mino],'solved')
    return data[mino] #shoots Answer up Recursion
  
  a=data[mino]
  
  #iterate through all cells
  for X in range(0,9):
    for Y in range(0,9):
      
      #checks if space is empty
      if data[mino][Y][X] == 0:   
        
        if len(possibilities(Y,X,mino)) == 0:
          return False
        
        possibles[mino] = possibilities(Y,X,mino) #checkpossibilities
                                        
        if len(possibles[mino])==k:
          for i in possibles[mino]:  #converts list to int
            replacement = int(i)
            data[mino+1] = copy.deepcopy(data[mino])
            data[mino+1][Y][X] = replacement #Replaced!
            replacer(mino+1,1) #starts from begining
          return
            

  
  
  if a == data[mino]:
    if k+1 == 10: #K == 10 means that solution is not valid and take another route/possibility, this is because there are no spaces now which have any possibilites left to take, if this is before all spots(0s gone) are taken this means that there no solution for that particular guess
      print(mino)
      #print(mino,k,'False')
      return False
    #print(mino+1,k+1)
    data[mino+1] = data[mino]
    #print(mino+1,k+1)
    replacer(mino+1,k+1)       

start_time = int(time.time())

### RUN!!
replacer(0,1)
print("--- %s seconds ---" % (time.time() - start_time))


#'''
