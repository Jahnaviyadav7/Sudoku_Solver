import tkinter
import customtkinter as ctk
import random

#Setting up the startup pages geometry and background
startup_tk = tkinter.Tk()
startup_tk.geometry("360x360")
startup_tk.title("Sudoku Solver")
ctk.set_appearance_mode("Light")
startup_tk.configure(bg='#F5F9E9')

def helpPage ():
  helpPage_tk = tkinter.Tk()
  helpPage_tk.geometry("600x600")
  helpPage_tk.title("Help Page")
  helpPage_tk.configure(bg='#F5F9E9')

  mainlabel = ctk.CTkLabel(master=helpPage_tk,
                        text="Help Page",
                        font=("Times New Roman", (45), 'bold'),
                        fg_color="#F5F9E9")
  mainlabel.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)

  label1 = ctk.CTkLabel(master=helpPage_tk,
                           text="Welcome to my program",
                           font=("Georgia", (20)),
                           fg_color="#F5F9E9")
  label1.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)

  label2 = ctk.CTkLabel(master=helpPage_tk,
                        text="There are 2 types of Sudokus available: 4x4 (easy) and 9x9 (hard)",
                        font=("Georgia", (18)),
                        fg_color="#F5F9E9")
  label2.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

  label3 = ctk.CTkLabel(master=helpPage_tk,
                        text="Click on enter key to submit values",
                        font=("Garamond", (20)),
                        fg_color="#F5F9E9")
  label3.place(relx=0.65, rely=0.37, anchor=tkinter.CENTER)

  label4 = ctk.CTkLabel(master=helpPage_tk,
                        text="Partially solves to provide few values",
                        font=("Garamond", (20)),
                        fg_color="#F5F9E9")
  label4.place(relx=0.65, rely=0.49, anchor=tkinter.CENTER)

  label5 = ctk.CTkLabel(master=helpPage_tk,
                        text="If no changes even after multiple tries,",
                        font=("Garamond", (20)),
                        fg_color="#F5F9E9")
  label5.place(relx=0.65, rely=0.545, anchor=tkinter.CENTER)

  label6 = ctk.CTkLabel(master=helpPage_tk,
                        text="=> no more hints available",
                        font=("Garamond", (20)),
                        fg_color="#F5F9E9")
  label6.place(relx=0.65, rely=0.59, anchor=tkinter.CENTER)

  label7 = ctk.CTkLabel(master=helpPage_tk,
                        text="Completely solves the grid",
                        font=("Garamond", (20)),
                        fg_color="#F5F9E9")
  label7.place(relx=0.65, rely=0.71, anchor=tkinter.CENTER)

  label8 = ctk.CTkLabel(master=helpPage_tk,
                        text="Saves grid values on external txt file",
                        font=("Garamond", (20)),
                        fg_color="#F5F9E9")
  label8.place(relx=0.65, rely=0.84, anchor=tkinter.CENTER)

  enterKey = ctk.CTkButton(master=helpPage_tk,
                             fg_color="#292929",
                             width=105,
                             height=50,
                             text="← Enter",
                             state = "disabled",
                             font=("Verdana", (15)))
  enterKey.place(relx=0.23, rely=0.37, anchor=tkinter.CENTER)

  hintButton = ctk.CTkButton(master=helpPage_tk,
                             fg_color="#E79B00",
                             width=70,
                             height=45,
                             text="Hint",
                             text_color="Black",
                             state="disabled",
                             font=("Georgia", (25)))
  hintButton.place(relx=0.23, rely=0.545, anchor=tkinter.CENTER)

  solveButton = ctk.CTkButton(master=helpPage_tk,
                             fg_color="#E79B00",
                             width=70,
                             height=45,
                             text="Solve",
                             text_color="Black",
                             state="disabled",
                             font=("Georgia", (25)))
  solveButton.place(relx=0.23, rely=0.7, anchor=tkinter.CENTER)

  saveButton = ctk.CTkButton(master=helpPage_tk,
                             fg_color="#E79B00",
                             width=70,
                             height=45,
                             text="Hint",
                             text_color="Black",
                             state="disabled",
                             font=("Georgia", (25)))
  saveButton.place(relx=0.23, rely=0.84, anchor=tkinter.CENTER)

'''
This part of the code contains everything for the Shidoku page.
This is a function which is called when the shidoku button is pressed.
The function loads up the page and is independent of the main code
'''
def openShidoku(): # function to open shidoku page

  # geometry for shidoku page
   shidoku_tk = tkinter.Tk()
   shidoku_tk.geometry("520x345")
   shidoku_tk.title("Shidoku")
   shidoku_tk.configure(bg='#F5F9E9')

   # storing the updated grid values and checks if in range
   grid = []#grid with all values which will be used throughout the program
   gridSize = 4
   for x in range (4):#turning the list into a 4x4 list
      row = [0 for x in range(4)]
      grid.append(row)

   def updateGrid(event):
       #hides(blends) the error messages before running
       valueErrorMessage ("#F5F9E9")
       repeatErrorMessage("#F5F9E9")
#checks each value in the gridEntry list
       for i in range(gridSize):
           for j in range(gridSize):
               if (gridEntry[i][j].get()!=""):#checks if the entry box has a value and only runs the rest if it does
                   try: 
                      value = int(gridEntry[i][j].get())#gets the input value for each cell entry box
                      if value >= 1 and value <= gridSize:#checks if the value entered is within the acceptable value range
                          grid[i][j] = value#stores the input value for the cell entry box in the list grid
                      else:#prints a incorrect value message if value out of range
                          valueErrorMessage("Red")
                   except:#prints a incorrect value message if error occurs
                       valueErrorMessage("Red")
       checkButtonFunction()

   # updates the grid values on the screen
   def updateGridVal():
      for i in range (gridSize):
          for j in range (gridSize):
              if grid[i][j] != 0: #if the cell has a value (0 = no value)
                  gridEntry[i][j].configure(placeholder_text = int(grid[i][j])) #set the value as the placeholder text
                  gridEntry[i][j].configure(state="disabled")#and disable the cell

   #error message for out of range values
   def valueErrorMessage (colour):
      label = ctk.CTkLabel(master=shidoku_tk,
          text = "Value needs to be between 1 and 4",
          font = ("Times New Roman", (25)),
          text_color = colour,
          fg_color = "#F5F9E9")
      label.place(relx=0.45, rely=0.75, anchor=tkinter.CENTER)

   #error message for invalid values
   def repeatErrorMessage (colour):
      label = ctk.CTkLabel(master=shidoku_tk,
          text = "No number repeats in row, column or box",
          font = ("Times New Roman", (25)),
          text_color = colour,
          fg_color = "#F5F9E9")
      label.place(relx=0.45, rely=0.75, anchor=tkinter.CENTER)

   # returns if the input is valid or not
   def validityCheck ():
      #check rows and columns
      flag = True #flag represent if the inputs are valid, assumes true to start
      #check row and columns
      for i in range (gridSize):
          for j in range (gridSize):
              valueI = i + 1 #gets the next value’s index for the row
              valueJ = j + 1 #gets the next value’s index for the column
              while valueI < gridSize and flag == True and grid[i][j] != 0: #checks if the next index value is still a valid grid index, no repeats have already been found and the grid value is not 0
                  if grid[i][j] == grid[valueI][j]:#checks if the value are same
                      flag = False #inputs are invalid, flag is set to False
                  else:
                      valueI += 1 #no repeats so gets the next unchecked value’s index
              while valueJ < gridSize and flag == True and grid[i][j] != 0: #checks if the next index value is still a valid grid index, no repeats have already been foundand the grid value is not 0
                  if grid[i][j] == grid[i][valueJ]:#checks if the value are same
                      flag = False #inputs are invalid, flag is set to False
                  else:
                      valueJ += 1 #no repeats so gets the next unchecked value’s index
      #check boxes
      #index values to check inputs using
      a = 0
      b = 1
      x = a
      y = b
      if grid[x][x]==grid[y][y]!=0 or grid[x][y]==grid[y][x]!=0: #Box 1
          #checks 00==11 or 01==10 (index values)
          flag = False #inputs are invalid, flag is set to False
      #changes x and y to 2 and 3 to use it for second half of the grid
      x = a+2
      y = b+2
      if grid[x][x]==grid[y][y]!=0 or grid[x][y]==grid[y][x]!=0: #Box 4
          #checks 22==33 or 23==32 (index values)
          flag = False #inputs are invalid, flag is set to False
      if grid[a][x]==grid[b][y]!=0 or grid[a][y]==grid[b][x]!=0: #Box 2
          #checks 02==13 or 03==12 (index values)
          flag = False #inputs are invalid, flag is set to False
      if grid[x][a]==grid[y][b]!=0 or grid[y][a]==grid[x][b]!=0:#Box 3
          #checks 20==31 or 30==21 (index values)
          flag = False #inputs are invalid, flag is set to False
      return flag #returns if the inputs are valid or not

   def removeItem (a,b, posVal):
       try:
           posVal.remove(grid[a][b])
       except:
           pass

   #does the last remaining cell method
   def lastRemainingCell():
      for digit in range (gridSize):#digit is the possible values of the puzzle
          count = 0 #counts how many instances of a number are in the grid
          found = False #shows if the number is found in the row or not
          for j in range (gridSize):
              if found == False: #if no instances were found
                  rowNum = j-1 #rowNum is the previous row
              found = False #resets to not found at the start of each row
              for i in range (gridSize):
                  if found == False: #if number has not been found yet
                      if grid[i][j] == digit: #check if value is digit
                          count += 1 #if found, instances is incremented
                          found = True
          if count == 3: #if 3 instances found (only 1 instance & location left)
              for i in range (gridSize):
                  if found == False: #if no instances found
                          colNum = i-1 #colNum is the previous column
                  found = False #resets to not found at the start of each column
                  for j in range (gridSize):
                      if found == False: #if number has not been found yet
                          if grid[i][j] == digit: #check if value is digit
                              found = True #if found, found = True
              grid[colNum][rowNum] = digit #store digit in grid

   #does last free cell method
   def lastFreeCell ():
      posVal = [1, 2, 3, 4]
      #Row
      for i in range (gridSize):
          if len(posVal) == 1: #if there is only 1 possible value left
              grid[a][b] = posVal[0]#set the empty cell it
          posVal = [1,2,3,4]#reset the possible values list for each row
          for j in range (gridSize): #for each value in the row
              if grid[i][j] != 0: #if the cell has a value
                  removeItem(i,j,posVal) #remove it from the possible values
              if grid[i][j] == 0:#if the cell is empty, store its coordinates
                  a = i
                  b = j
      #Column
      for j in range(gridSize):
          if len(posVal) == 1: #if there is only 1 possible value left
              grid[a][b] = posVal[0]#set the empty cell it
          posVal = [1, 2, 3, 4]#reset the possible values list for each row
          for i in range(gridSize): #for each value in the column
              if grid[i][j] != 0: #if the cell has a value
                  removeItem(i,j,posVal) #remove it from the possible values
              if grid[i][j] == 0:#if the cell is empty, store its coordinates
                  a = i
                  b = j

   # does last possible number method
   def possibleValues(i,j):
       posVal = [1, 2, 3, 4]#resets possible values before checking
       for x in range(gridSize):
           if grid[x][j] != 0:#if the cell (row) has a value
               removeItem(x,j,posVal)#remove it from the possible values
           if grid[i][x] != 0:#if the cell (column) has a value
               removeItem(i,x,posVal)#remove it from the possible values
       # box
       if len(posVal) == 2:#if there is only 2 possible values left
           iVal = i % 2
           jVal = j % 2
           if iVal == 0 and jVal == 0:  # EE
               if grid[i + 1][j + 1] != 0:#if the cell has a value
                   removeItem(i+1, j+1, posVal)#remove from the possible values
           if iVal == 1 and jVal == 1:  # OO
               if grid[i - 1][j - 1] != 0:#if the cell has a value
                   removeItem(i-1, j-1, posVal)#remove from the possible values
           if iVal == 0 and jVal == 1:  # EO
               if grid[i + 1][j - 1] != 0:#if the cell has a value
                   removeItem(i+1, j-1, posVal)#remove from the possible values
           if iVal == 1 and jVal == 0:  # OE:
               if grid[i - 1][j + 1] != 0:#if the cell has a value
                   removeItem(i-1, j+1, posVal)#remove from the possible values
       return(posVal)
   def lastPossibleNumber ():
      #row and column
      for i in range (gridSize):
          for j in range(gridSize):#for each value in the cell
              if grid[i][j] == 0:#if a cell is empty
                  posVal = possibleValues(i,j)#checks and return possible values
                  if len(posVal) == 1:#if there is only 1 possible value left
                      grid[i][j] = posVal[0]#set the empty cell it

   # does brute force
   startgrid = grid#to see what changes have been made
   def performCheck(i, j, posVal):
      check = validityCheck()
      while check == False and len(posVal) >= 1:#while invalid and possible values available
          grid[i][j] = posVal[0]#set to first possible value
      if len(posVal) < 1:#when no more possible values left
          for x in range(i, 0, -1):
              for y in range(j, 0, -1):#go backwards
                 if startgrid[x][y] == 0:#find first 0 value
                     posVal = possibleValues(x, y)#get possible values
                     performCheck(x, y, posVal)#repeat function
   def bruteForce():
      for i in range(gridSize):
          for j in range(gridSize):#for each cell
              if grid[i][j] == 0:#if empty
                  posVal = possibleValues(i,j)#get possible values
                  grid[i][j] = posVal[0]#set to first possible value
                  performCheck(i, j, posVal)

   # solve button function
   def solveButtonFunction ():
      count = 0 #counts how many times there are no changes made
      while count < 4 : #does the loop until there are no more solutions available even after 4 runs
          startGrid = grid
          lastRemainingCell()
          lastFreeCell()
          lastPossibleNumber()
          if startGrid == grid:
              count = count + 1 #updates count
          print(grid)
          updateGridVal()
      try: #tries to run brute force
          bruteForce()
          updateGridVal()
      except: #prints error message if it fails
          slabel = ctk.CTkLabel(master=shidoku_tk,
                                text="Not enough values to fully solve",
                                font=("Georgia", (20)),
                                text_color="Red",
                                fg_color="#F5F9E9")
          slabel.place(relx=0.4, rely=0.75, anchor=tkinter.CENTER)

   # save button function
   def saveButtonFunction():
      f = open('Shidoku_Values.txt', 'a')
      f.write("Grid")
      gridVal = str(grid) #converts the list into a string
      f.write(gridVal)
      f.close()

   # hint button function
   def hintButtonFunction ():
      num = random.randint(1,3) #generates a random number to choose a method at random
      if num == 1:
          lastRemainingCell()
      elif num == 2:
          lastFreeCell()
      else:
          lastPossibleNumber()
      updateGridVal()

   # check button function
   def checkButtonFunction(): 
       if validityCheck() == False: #calls validity check
           repeatErrorMessage("Red") #error message displayed if inputs are invalid

  # Main label
   slabel = ctk.CTkLabel(master=shidoku_tk,
         text = "4x4 Shidoku",
         font = ("Times New Roman", (40), 'bold'),
         fg_color = "#F5F9E9")
   slabel.place(relx=0.73, rely=0.15, anchor=tkinter.CENTER)

   # Help button
   helpButton = ctk.CTkButton (master= shidoku_tk,
         fg_color= "#0080FE",
         width = 70,
         height = 40,
         text= "Help",
         text_color = "Black",
         hover_color = "#4CC9F0",
         font = ("Georgia", (23)),
         command=helpPage)
   helpButton.place(relx=0.87, rely=0.85, anchor=tkinter.CENTER)

   # Hint button
   hintButton = ctk.CTkButton (master= shidoku_tk,
         fg_color= "#E79B00",
         width = 70,
         height = 45,
         text= "Hint",
         text_color = "Black",
         hover_color = "#EEDD82",
         font = ("Georgia", (25)),
         command=hintButtonFunction)
   hintButton.place(relx=0.65, rely=0.35, anchor=tkinter.CENTER)

   # Solve button
   solveButton = ctk.CTkButton (master= shidoku_tk,
         fg_color= "#E79B00",
         width = 70,
         height = 45,
         text= "Solve",
         text_color = "Black",
         hover_color = "#EEDD82",
         font = ("Georgia", (25)),
         command=solveButtonFunction)
   solveButton.place(relx=0.85, rely=0.35, anchor=tkinter.CENTER)

   # Save button
   saveButton = ctk.CTkButton (master= shidoku_tk,
         fg_color= "#E79B00",
         width = 70,
         height = 45,
         text= "Save",
         text_color = "Black",
         hover_color = "#EEDD82",
         font = ("Georgia", (25)),
         command=saveButtonFunction)
   saveButton.place(relx=0.65, rely=0.55, anchor=tkinter.CENTER)

   # Check button
   checkButton = ctk.CTkButton (master= shidoku_tk,
         fg_color= "#E79B00",
         width = 70,
         height = 45,
         text= "Check",
         text_color = "Black",
         hover_color = "#EEDD82",
         font = ("Georgia", (25)),
         command=checkButtonFunction)
   checkButton.place(relx=0.85, rely=0.55, anchor=tkinter.CENTER)

   # Creating the grid for entry
   x = 0.18 #x Position of the first cell
   y = 0.3 #y Position of the first cell
   gridEntry =[] #2D list to store all the input values
   for i in range (4):
       row_entry = []#list to store the input boxes for each row (resets each row)
       for j in range (4):
           CellEntry = ctk.CTkEntry(master=shidoku_tk,
                placeholder_text= "",
                placeholder_text_color= "Blue",
                width=40,
                height=40,
                border_width=2,
                corner_radius=5)
           CellEntry.place(relx=x, rely=y, anchor=tkinter.CENTER)
           CellEntry.bind("<Return>", updateGrid) #calls the updateGrid function every time the return/enter key is pressed
           row_entry.append(CellEntry)#adds entry box in the row into the list
           x+=0.075 #increments in the x position to add all cells in the row
       gridEntry.append(row_entry)#adds the row to the 2D list gridEntry
       y+=0.111 #increments in the y position to add all rows
       x= 0.18 #resets the initial x position for each row

   #Creating the top grid label
   text = "A"
#x position not reset as it is already at the value required before this runs
   y = 0.18 #y Position of the first label(above the first row of entry cells so y value is lower than the entry cell’s initial y position)
   for i in range (4):
         labelgrid4 = ctk.CTkLabel(master=shidoku_tk,
             text = text,
             width = 40,
             height = 40,
             font = ("Times New Roman", (30)),
             fg_color = "#F5F9E9")
         labelgrid4.place(relx=x, rely=y, anchor=tkinter.CENTER)
         text = chr(ord(text) + 1)#get the next letter in the alphabet
         x += 0.075 #increments in x position to add all labels in the row

   #Creating the side grid label
   text = "A"
   x = 0.1  #x Position of the first label(left of the first column of entry cells so x value is lower than the entry cell’s initial x position)
   y = 0.3 #y Position of the first label(same as initial cell entry y position)
   for i in range (4):
         labelgrid4 = ctk.CTkLabel(master=shidoku_tk,
             text = text,
             width = 40,
             height = 40,
             font = ("Times New Roman", (30)),
             fg_color = "#F5F9E9")
         labelgrid4.place(relx=x, rely=y, anchor=tkinter.CENTER)
         text = chr(ord(text) + 1)#get the next letter in the alphabet
         y += 0.111 #increments in y position to add all labels in the column

   shidoku_tk.mainloop()

def openSudoku(): # function to open sudoku page

  # geometry for sudoku page
  sudoku_tk = tkinter.Tk()
  sudoku_tk.geometry("545x370")
  sudoku_tk.title("Sudoku")
  sudoku_tk.configure(bg='#F5F9E9')

  # storing the updated grid values and checks if in range
  grid = []#grid with all values which will be used throughout the program
  gridSize = 9
  for x in range (gridSize):#turning the list into a 9x9 list
      row = [0 for x in range(gridSize)]
      grid.append(row)
  def updateGrid(event):
      #hides(blends) the error messages before running
      valueErrorMessage ("#F5F9E9")
      repeatErrorMessage("#F5F9E9")
	#checks each value in the gridEntry list
      for i in range(gridSize):
          for j in range(gridSize):
              if (gridEntry[i][j].get()!=""):
                  try:
                      value = int(gridEntry[i][j].get())#gets the input value for each cell entry box
                      if value >= 1 and value <= gridSize:#checks if the value entered is within the acceptable value range
                          grid[i][j] = value#stores the input value for the cell entry box in the list grid
                      else:#prints a incorrect value message if value out of range
                          valueErrorMessage("Red")
                  except:#prints a incorrect value message if value out of range
                      valueErrorMessage("Red")
      checkButtonFunction()

  # updates the grid values on the screen
  def updateGridVal():
      for i in range (gridSize):
          for j in range (gridSize):
              if grid[i][j] != 0: #if the cell has a value (0 = no value)
                  gridEntry[i][j].configure(placeholder_text = int(grid[i][j])) #set the value as the placeholder text
                  gridEntry[i][j].configure(state="disabled")#and disable the cell

   #error message for out of range values
  def valueErrorMessage (colour):
      label = ctk.CTkLabel(master=sudoku_tk,
          text = "Value needs to be between 1 and 9",
          font = ("Times New Roman", (25)),
          text_color = colour,
          fg_color = "#F5F9E9")
      label.place(relx=0.43, rely=0.85, anchor=tkinter.CENTER)

   #error message for invalid values
  def repeatErrorMessage (colour):
      label = ctk.CTkLabel(master=sudoku_tk,
          text = "No number repeats in row, column or box",
          font = ("Times New Roman", (25)),
          text_color = colour,
          fg_color = "#F5F9E9")
      label.place(relx=0.43, rely=0.85, anchor=tkinter.CENTER)

   # returns if the input is valid or not
  def validityCheck ():
      #check rows and columns
      flag = True #flag represent if the inputs are valid, assumes true to start
      for i in range (gridSize):
          for j in range (gridSize):
              valueI = i + 1 #gets the next value’s index for the row
              valueJ = j + 1 #gets the next value’s index for the column
              while valueI < gridSize and flag == True and grid[i][j] != 0: #checks if the next index value is still a valid grid index, no repeats have already been found and the grid value is not 0
                  if grid[i][j] != grid[valueI][j]:#checks if the value are same
                      valueI += 1 #no repeats so gets the next unchecked value’s index
                  else:
                      flag = False #inputs are invalid, flag is set to False
              while valueJ < gridSize and flag == True and grid[i][j] != 0: #checks if the next index value is still a valid grid index, no repeats have already been foundand the grid value is not 0
                  if grid[i][j] != grid[i][valueJ]:#checks if the value are same
                      valueJ += 1 #no repeats so gets the next unchecked value’s index
                  else:
                      flag = False #inputs are invalid, flag is set to False
      #check boxes
      for i in range (0, 9, 3):
          for j in range (0, 9, 3):#for each box, store the 5 diagonal values
              a = grid[i][j]
              b = grid[i+1][j+1]
              c = grid[i+2][j+2]
              d = grid[i][j+2]
              e = grid[i+2][j]
              values = [a,b,c,d,e]#add the values in a values list
              for num in values:#for each value in the list
                  if num != 0:#if cell has a value
                      numbers = []#reset the numbers list as empty
                      if num in numbers:#if the value already exists
                          flag = False#inputs are invalid
                      else:
                          numbers.append(num)#else add it to the list
      return flag

   #does the last remaining cell method
  def lastRemainingCell():
      for digit in range (gridSize):#digit is the possible values of the puzzle
          count = 0 #counts how many instances of a number are in the grid
          found = False #shows if the number is found in the row or not
          for j in range (gridSize):
              if found == False: #if no instances were found
                  rowNum = j-1 #rowNum is the previous row
              found = False #resets to not found at the start of each row
              for i in range (gridSize):
                  if found == False: #if number has not been found yet
                      if grid[i][j] == digit : #check if value is digit
                          count += 1 #if found, instances is incremented
                          found = True
          if count == 8: #if 8 instances found (only 1 instance & location left)
              for i in range (gridSize):
                  if found == False: #if no instances found
                          colNum = i-1 #colNum is the previous column
                  found = False #resets to not found at the start of each column
                  for j in range (gridSize):
                      if found == False: #if number has not been found yet
                          if grid[i][j] == digit: #check if value is digit
                              found = True #if found, found = True
              grid[colNum][rowNum] = digit #store digit in grid

   #does last free cell method
  def lastFreeCell ():
      posVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      #Row
      for i in range (gridSize):
          if len(posVal) == 1:#if there is only 1 possible value left
              grid[a][b] = posVal[0]#set the empty cell it
          posVal = [1,2,3,4,5,6,7,8,9]#reset the possible values for each row
          for j in range (gridSize):#for each value in the row
              if grid[i][j] != 0:#if the cell has a value
                  removeItem(i,j,posVal)#remove it from the possible values
              if grid[i][j] == 0:#if the cell is empty, store its coordinates
                  a = i
                  b = j

      #Column
      for j in range(gridSize):#for each value in the column
          if len(posVal) == 1:#if there is only 1 possible value left
              grid[a][b] = posVal[0]#set the empty cell it
          posVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]#reset possible values list for each column
          for i in range(gridSize):#for each value in the column
              if grid[i][j] != 0:#if the cell has a value
                  removeItem(i,j,posVal)#remove it from the possible values
              if grid[i][j] == 0:#if the cell is empty, store its coordinates
                  a = i
                  b = j

   # does last possible number method
  posVal = []
  def possibleValues(i,j):
      posVal = [1, 2, 3, 4, 5, 6, 7, 8, 9]#resets possible values 
      for x in range(gridSize):
          if grid[x][j] != 0:#if the cell (row) has a value
              removeItem(x, j,posVal)#remove from the possible values
          if grid[i][x] != 0:#if the cell (column) has a value
              removeItem(i, x, posVal)#remove from the possible values
      # box
      if len(posVal) > 1: #if there is more than 1 possible values left
          iVal = i % 3
          jVal = j % 3
          if iVal == 0 and jVal == 0:  # 00
              if grid[i + 1][j + 1] != 0:#if the cell has a value
                  removeItem(i + 1, j + 1, posVal)#remove from possible values
              if grid[i + 2][j + 2] != 0:#if the cell has a value
                  removeItem(i + 2, j + 2, posVal)#remove from possible values
          if iVal == 1 and jVal == 1:  # 11
              if grid[i - 1][j - 1] != 0:#if the cell has a value
                  removeItem(i - 1, j - 1, posVal)#remove from possible values
              if grid[i + 1][j + 1] != 0:#if the cell has a value
                  removeItem(i + 1, j + 1, posVal)#remove from possible values
              if grid[i - 1][j + 1] != 0:#if the cell has a value
                  removeItem(i - 1, j + 1, posVal)#remove from possible values
              if grid[i + 1][j - 1] != 0:#if the cell has a value
                  removeItem(i + 1, j - 1, posVal)#remove from possible values
          if iVal == 2 and jVal == 2:  # 22
              if grid[i - 2][j - 2] != 0:#if the cell has a value
                  removeItem(i - 2, j - 2, posVal)#remove from possible values
              if grid[i - 1][j - 1] != 0:#if the cell has a value
                  removeItem(i - 1, j - 1, posVal)#remove from possible values
          if iVal == 0 and jVal == 2:  # 02
              if grid[i + 1][j - 1] != 0:#if the cell has a value
                  removeItem(i + 1, j - 1, posVal)#remove from possible values
              if grid[i + 2][j - 2] != 0:#if the cell has a value
                  removeItem(i + 2, j - 2, posVal)#remove from possible values
          if iVal == 2 and jVal == 0:  # 20
              if grid[i - 1][j + 1] != 0:#if the cell has a value
                  removeItem(i - 1, j + 1, posVal)#remove from possible values
              if grid[i - 2][j + 2] != 0:#if the cell has a value
                  removeItem(i - 2, j + 2, posVal)#remove from possible values
          if iVal == 1 and jVal == 0:  # 10
              if grid[i - 1][j + 1] != 0:#if the cell has a value
                  removeItem(i - 1, j + 1, posVal)#remove from possible values
              if grid[i - 1][j + 2] != 0:#if the cell has a value
                  removeItem(i - 1, j + 2, posVal)#remove from possible values
              if grid[i + 1][j + 1] != 0:#if the cell has a value
                  removeItem(i + 1, j + 1, posVal)#remove from possible values
              if grid[i + 1][j + 2] != 0:#if the cell has a value
                  removeItem(i + 1, j + 2, posVal)#remove from possible values
          if iVal == 0 and jVal == 1:  # 01
              if grid[i + 1][j - 1] != 0:#if the cell has a value
                  removeItem(i + 1, j - 1, posVal)#remove from possible values
              if grid[i + 1][j + 1] != 0:#if the cell has a value
                  removeItem(i + 1, j + 1, posVal)#remove from possible values
              if grid[i + 2][j - 1] != 0:#if the cell has a value
                  removeItem(i + 2, j - 1, posVal)#remove from possible values
              if grid[i + 2][j - 1] != 0:#if the cell has a value
                  removeItem(i + 2, j - 1, posVal)#remove from possible values
          if iVal == 2 and jVal == 1:  # 01
              if grid[i - 1][j - 1] != 0:#if the cell has a value
                  removeItem(i - 1, j - 1, posVal)#remove from possible values
              if grid[i - 1][j + 1] != 0:#if the cell has a value
                  removeItem(i - 1, j + 1, posVal)#remove from possible values
              if grid[i - 2][j + 1] != 0:#if the cell has a value
                  removeItem(i - 2, j + 1, posVal)#remove from possible values
              if grid[i - 2][j - 1] != 0:#if the cell has a value
                  removeItem(i - 2, j - 1, posVal)#remove from possible values
          if iVal == 1 and jVal == 2:  # 01
              if grid[i - 1][j - 1] != 0:#if the cell has a value
                  removeItem(i - 1, j - 1, posVal)#remove from possible values
              if grid[i - 1][j - 2] != 0:#if the cell has a value
                  removeItem(i - 1, j - 2, posVal)#remove from possible values
              if grid[i + 1][j - 1] != 0:#if the cell has a value
                  removeItem(i + 1, j - 1, posVal)#remove from possible values
              if grid[i + 1][j - 2] != 0:#if the cell has a value
                  removeItem(i + 1, j - 2, posVal)#remove from possible values
      return posVal
  def removeItem(a, b, posVal):
      try:
          posVal.remove(grid[a][b])
      except:
          pass
  def lastPossibleNumber ():
      #row and column
      for i in range (gridSize):
          for j in range(gridSize):#for each value in the cell
              if grid[i][j] == 0:#if a cell is empty
                  posVal = possibleValues(i,j)#checks and return possible values
                  if len(posVal) == 1:#if there is only 1 possible value left
                     grid[i][j] = posVal[0]#set the empty cell it

   #does brute force
  startgrid = grid#to see what changes have been made
  def performCheck(i, j, posVal):
      check = validityCheck()
      while check == False and len(posVal) >= 1:#while invalid and possible values available
          grid[i][j] = posVal[0]#set to first possible value
      if len(posVal) < 1:#when no more possible values left
          for x in range(i, 0, -1):
              for y in range(j, 0, -1):#go backwards
                  if startgrid[x][y] == 0:#find first 0 value
                      posVal = possibleValues(x, y)#get possible values
                      performCheck(x, y, posVal)#repeat function
  def bruteForce():
      for i in range(gridSize):
          for j in range(gridSize):#for each cell
              if grid[i][j] == 0:#if empty
                  posVal = possibleValues(i, j)#get possible values
                  grid[i][j] = posVal[0]#set to first possible value
                  performCheck(i, j, posVal)

  # solve button function
  def solveButtonFunction ():
      count = 0 #counts how many times there are no changes made
      while count < 5: #does the loop until there are no more solutions available even after 5 runs
          startGrid = grid
          lastRemainingCell()
          lastFreeCell()
          lastPossibleNumber()
          if startGrid == grid:
              count = count + 1 #updates count
          updateGridVal()
      print (grid)
      try: #tries to run brute force
          bruteForce()
          updateGridVal()
      except: #prints error message if it fails
          slabel = ctk.CTkLabel(master=sudoku_tk,
                                text="Not enough values to fully solve",
                                font=("Georgia", (20)),
                                text_color="Red",
                                fg_color="#F5F9E9")
          slabel.place(relx=0.4, rely=0.85, anchor=tkinter.CENTER)

   # save button function
  def saveButtonFunction():
      f = open('Sudoku_Values.txt', 'a')
      f.write("Grid")
      gridVal = str(grid) #converts the list into a string
      f.write(gridVal)
      f.close()

   # hint button function
  def hintButtonFunction ():
      num = random.randint(1,3)#generates a random number to choose a method at random
      if num == 1:
          lastRemainingCell()
      elif num == 2:
          lastFreeCell()
      else:
          lastPossibleNumber()
      updateGridVal()

  # check button function
  def checkButtonFunction():
      if validityCheck() == False: #calls validity check
          repeatErrorMessage("Red") #error message displayed if inputs are invalid

  # Main label
  slabel2 = ctk.CTkLabel(master=sudoku_tk,
      text = "9x9 Sudoku",
      width = 100,
      height = 25,
      font = ("Times New Roman", (40),'bold'),
      fg_color = "#F5F9E9")
  slabel2.place(relx=0.76, rely=0.15, anchor=tkinter.CENTER)

   # Help button
  helpButton = ctk.CTkButton (master= sudoku_tk,
      fg_color= "#0080FE",
      width = 50,
      height = 40,
      text= "Help",
      text_color = "Black",
      hover_color = "#4CC9F0",
      font = ("Georgia", (23)),
      command=helpPage)
  helpButton.place(relx=0.90, rely=0.85, anchor=tkinter.CENTER)

   # Hint button'
  hintButton = ctk.CTkButton (master= sudoku_tk,
      fg_color= "#E79B00",
      width = 70,
      height = 45,
      text= "Hint",
      text_color = "Black",
      hover_color = "#EEDD82",
      font = ("Georgia", (25)),
      command=hintButtonFunction)
  hintButton.place(relx=0.68, rely=0.35, anchor=tkinter.CENTER)

   # Solve button
  solveButton = ctk.CTkButton (master= sudoku_tk,
      fg_color= "#E79B00",
      width = 70,
      height = 45,
      text= "Solve",
      text_color = "Black",
      hover_color = "#EEDD82",
      font = ("Georgia", (25)),
      command=solveButtonFunction)
  solveButton.place(relx=0.88, rely=0.35, anchor=tkinter.CENTER)

   # save button
  saveButton = ctk.CTkButton (master= sudoku_tk,
      fg_color= "#E79B00",
      width = 70,
      height = 45,
      text= "Save",
      text_color = "Black",
      hover_color = "#EEDD82",
      font = ("Georgia", (25)),
      command=saveButtonFunction)
  saveButton.place(relx=0.68, rely=0.55, anchor=tkinter.CENTER)

   # Check button
  checkButton = ctk.CTkButton (master= sudoku_tk,
      fg_color= "#E79B00",
      width = 70,
      height = 45,
      text= "Check",
      text_color = "Black",
      hover_color = "#EEDD82",
      font = ("Georgia", (25)),
      command=checkButtonFunction)
  checkButton.place(relx=0.88, rely=0.55, anchor=tkinter.CENTER)

   # Creating entry grid
  x = 0.12 #x Position of the first cell
  y = 0.2 #y Position of the first cell
  gridEntry =[]#2D list to store all the input values
  for i in range (9):
      row_entry = []#list to store the input boxes for each row (resets each row)
      for j in range (9):
          CellEntry = ctk.CTkEntry(master=sudoku_tk,
              placeholder_text= "",
              placeholder_text_color="Blue",
              width=27,
              height=27,
              border_width=2,
              corner_radius=5)
          CellEntry.place(relx=x, rely=y, anchor=tkinter.CENTER)
          CellEntry.place(relx=x, rely=y, anchor=tkinter.CENTER)
          CellEntry.bind("<Return>", updateGrid)#calls the updateGrid function every time the return/enter key is pressed
          row_entry.append(CellEntry)#adds entry box in the row into the list
          x+=0.0475 #increments in the x position to add all cells in the row
      gridEntry.append(row_entry)#adds the row to the 2D list gridEntry
      y+=0.067 #increments in the y position to add all rows
      x= 0.12 #resets the initial x position for each row

   # Creating the top grid label
  text = "A"
#x position not reset as it is already at the value required before this runs
  y = 0.13 #y Position of the first label(above the first row of entry cells so y value is lower than the entry cell’s initial y position)
  for i in range(9):
      labelgrid9 = ctk.CTkLabel(master=sudoku_tk,
               text=text,
               width=27,
               height=27,
               font=("Times New Roman", (23)),
               fg_color="#F5F9E9")
      labelgrid9.place(relx=x, rely=y, anchor=tkinter.CENTER)
      text = chr(ord(text) + 1)#get the next letter in the alphabet
      x += 0.0475 #increments in x position to add all labels in the row

   # Creating the side label
  text = "A"
  x = 0.07#x Position of the first label(left of the first column of entry cells so x value is lower than the entry cell’s initial x position)
  y = 0.2#y Position of the first label(same as initial cell entry y position)
  for i in range(9):
      labelgrid9 = ctk.CTkLabel(master=sudoku_tk,
           text=text,
           width=27,
           height=27,
           font=("Times New Roman", (22)),
           fg_color="#F5F9E9")
      labelgrid9.place(relx=x, rely=y, anchor=tkinter.CENTER)
      text = chr(ord(text) + 1)#get the next letter in the alphabet
      y += 0.067 #increments in y position to add all labels in the column

  sudoku_tk.mainloop()

# Button to open the shidoku page
shidokupageButton = ctk.CTkButton (master =startup_tk,
      fg_color= "#F1AD00",
      width = 230,
      height = 40,
      text= "→ Shidoku (4 x 4)",
      text_color = "Black",
      hover_color = "#FFC5B0",
      font = ("Georgia", (25)),
      command=openShidoku)
shidokupageButton.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)

#Button to open the sudoku page
sudokupageButton = ctk.CTkButton (master =startup_tk,
      fg_color= "#F1AD00",
      width = 230,
      height = 40,
      text= "→ Sudoku (9 x 9)",
      text_color = "Black",
      hover_color = "#FFC5B0",
      font = ("Georgia", (25)),
      command=openSudoku)
sudokupageButton.place(relx=0.5, rely=0.70, anchor=tkinter.CENTER)

#choose sudoku type label
label1 = ctk.CTkLabel(master=startup_tk,
      text = "Choose Sudoku Type",
      width = 120,
      font = ("Georgia", (35)),
      fg_color = "#F5F9E9")
label1.place(relx=0.5, rely=0.38, anchor=tkinter.CENTER)

#welcome label
label2 = ctk.CTkLabel(master=startup_tk,
      text = "Welcome",
      width = 120,
      font = ("Georgia", (60),'bold'),
      fg_color = "#F5F9E9")
label2.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

# help button
helpButton = ctk.CTkButton (master=startup_tk,
      fg_color= "#0080FE",
      width = 50,
      height = 40,
      text= "Help",
      text_color = "Black",
      hover_color = "#4CC9F0",
      font = ("Georgia", (25)),
      command=helpPage)
helpButton.place(relx=0.87, rely=0.9, anchor=tkinter.CENTER)

startup_tk.mainloop()