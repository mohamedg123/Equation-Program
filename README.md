![Image](https://github.com/user-attachments/assets/c7f305a8-37ea-4cbf-a032-4f4bcb90ca32)

The program starts by welcoming the user. The following variables and print functions are at the start so they ran in the beginning. Welcoming the user. I created a variable “name=input()” which will prompt the user to enter their name. The print string below that variable will take the input of the user's name and substituted that into the print string i used a f string used the f-string formatting to do this. Lastly the last print function lets the user know to ‘Solve for x in each line’ and i added \n which will create a new line for the next set of codes. 

![Image](https://github.com/user-attachments/assets/d9524fe1-7cad-4bcf-836b-b078700c710d)

In the next piece of code i imported the Random module which is a library which is used to generate random numbers. I required to import this module to create the two defined function make_a_equation1 and make_a_equation2. As you can see for each letter i have equated it to random.randint(-5,10) so when it creates the equation the numbers can be any number between –5 to 10.  

My first defined function is creating a type of equation in the form of a = y * x and the second function is g = d + x. For each defined function i made sure it returns the equation string which is ‘{y} * x = {g} and return the answer ‘x’. As both return functions are in fstrings for each questions it will generate a different equation with different numbers. 
