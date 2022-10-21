# Lesson 3 - Fonctions

1. Local and Global Scope
   1. Local and Global Scope: a variable that exists in a local scope is called a local  variable, while a variable that exists in the global scope is called a global variable. A variable must be one or the other, it can not be both local and global.
      1. Code in the global scope can not use any local variables;
      2. However, a local scope can access global variables; 
      3. Code in a function's local scope can not use variables in any other local scope 
      4. You can use the same name for a different variables if they are in different scopes. That is, there can be a local variable named spam and a global variable also named spam.
2. Exception Handling: errors can be handled with 'try' and 'excepts' statements. So, the code that could potentially have an error is put in a try clause and the program execution moves to the start of a following excepts clause if an error happen.

3. random.randint(): function to generate a number. 
   1. Ex: random.randint(1,10) #one number between 1 and 10;
   