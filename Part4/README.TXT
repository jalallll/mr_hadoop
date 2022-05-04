###############################################
Important: INPUT FILES MUST BE STORED IN DIRECTORY:    /.../Part4/inputDirectory
###############################################

- The directory "inputDirectory" (located in the same level as this README.TXT file 
~/Part4/inputDirectory) is where you must store the .txt files for testing. 

- If you would like to use another directory, 
change the input_path variable in mapper1.py file.


#######################
How To Run Using Pipes:
########################

1) Give each file permission to execute using the command
" chmod +x fileName.py " 

Example:

chmod +x ./mapper1.py
chmod +x ./mapper2.py 
chmod +x ./mapper3.py 

chmod +x ./reducer1.py 
chmod +x ./reducer2.py 
chmod +x ./reducer3.py 

If the above does not work then type "pwd" into terminal and 
append the full path to each mapper and reducer file above.


2) 
Navigate to the directory: /.../Part4/ 
& execute the below command 

python mapper1.py |sort | ./reducer1.py |sort| ./mapper2.py |sort| ./reducer2.py |sort| ./mapper3.py |sort| ./reducer3.py


