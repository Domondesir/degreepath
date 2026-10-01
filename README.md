# degreepath
Python prototype that checks course eligibility based on prerequisites and lists what courses can be taken.

DegreePath is a Python command-line prototype that assists UCF CS students with selecting the classes they should take next. How it works right now is the user enters the courses that they have completed and the program checks it to see which courses they are eligible to take now and shows missing prerequisites for classes they cannot take yet.

 To run the program, download the repository and open a terminal in the folder containing `main.py`. Run `python3 main.py` and when prompted enter the completed course codes separated by commas such as COP2500, MAC1105C, COP3223C. Python 3 is the only thing needed.  
 
Note: Currently this prototype has six of the starting classes for the major. I plan for this to eventually account for placement tests, transfer credits, and semester planning.
