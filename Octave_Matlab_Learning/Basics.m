%Created by Guru Sarath
%20 April 2019
% This is a single line comment

disp('Matlab / Octave ----------------------------')

disp('Creating scalar ----------------------------')
s1 = 2

disp('Creating vectors ----------------------------')
a = [1,2,3] #Row matrix / Vector
b = [5 6 7] #Row matrix / Vector
c = [4;7;8] #Column matrix / Vector

disp('Creating 2D matrix ----------------------------')
x = [1 2 3; 4 5 6; 7 8 9] #2D Matrix
y = [1,1,1; 2,3,3; 4,6,6] #2D Matrix

disp('Matrix operations ----------------------------')
x + y
ans * 2 #Elementwise multiplication with 2 (scalar)
x .* y #Elementwise multiplication
x *y #Matrix multiplication
a * c #Matrix multiplication / Vector inner product
x' #Transpose of a matrix
x^2 #Square a matrix (Matrix square)
x.^2 #Square individual terms

#Default is 4 decimal places (short format)
#For 8 decimal places - format long
sqrt(2)

format long
sqrt(2)

disp('Indexing ----------------------------')
a(1)
x(1) #Get first element
x(1,:) #Get first row
x(:,1) #Get first column
MatA = [1 2 3 4 5; 6 7 8 9 10; 11 12 13 14 15; 16 17 18 19 20; 21 22 23 24 25]
image(MatA)
MatA(2,2) = 99999
MatA(3,:) = [19 19 19 19 19]
MatA(2:4,3:5)

disp('Data Types and conversions----------------------------')
disp('String ----------------------------')
strX = 'Guru Sarath'
strX(3)
NewStr = strX + 1
char(NewStr)
int2str(NewStr)
strAry = ['guru'; 'sarath'; 'Priyanka']
strAry = ['guru' 'sarath' 'Priyanka']


disp('Commonly used commands ----------------------------')
who #Lists all variables in scope
whos #Lists all variables and memory allocated
clear a #Remove variable a from memory
clear #Remove all the variables 
format short
#clc #Clear screen



