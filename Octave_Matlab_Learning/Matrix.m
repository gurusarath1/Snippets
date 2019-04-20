% Created by Guru Sarath
% 21 April 2019
clear

printf('Matrix------------------------\n')
zeros(2)
zeros(2,3)
ones(5)
ones(5,1)
magic(5)
eye(4)

printf('Any All------------------------\n')
x = [1 2 3; 4 5 6; 7 0 9; 8 8 9]
any(x) %Checks if any element in columns is non zero (true)
all(x) %Checks if all elements in columns is non zero (true)

x2 = [0 2 0; 3 4 0; 5 6 0]
any(x2)
all(x2)
any(any(x2))

printf('Any All 2------------------------\n')

any(x2, 2) %Checks along the row (2nd Dimension)
all(x2, 2) %Checks along the row (2nd Dimension)

printf('Flip------------------------\n')
M = [3 4 1 8; 9 8 7 6; 9 9 9 0; 7 5 4 3; 0 0 6 5; 1 2 3 4]

fliplr(M)
flipud(M)
flip(M, 2) %Flip along dimension 2 %Same as fliplr

printf('Rotate------------------------\n')
M = [3 4 1 8; 9 8 7 6; 9 9 9 0; 7 5 4 3; 0 0 6 5; 1 2 3 4]

rot90(M) %Rotate Anti-Clockwise 
rot90(M,-1) %Rotate Clockwise
rot90(M, 2) %Rotate Anti-Clockwise 2 times

printf('Reshape------------------------\n')
K = [1 2 3 4 5 6 7 8]
reshape(K,4,2) %4 rows 2 columns 
reshape(K,2,4) %2 rows 4 columns 

printf('Resize------------------------\n')
M = [3 4 1 8; 9 8 7 6; 9 9 9 0; 7 5 4 3; 0 0 6 5; 1 2 3 4]
resize(M,4,2) %Resize to 4 rows and 2 cols
resize(M,10,10) %Resize to 10 rows and 10 cols
resize(M,7) %Resize to 7 rows and 7 cols


printf('Circular shift------------------------\n')
M = [3 4 1 8; 9 8 7 6; 9 9 9 0; 7 5 4 3; 0 0 6 5; 1 2 3 4]
circshift(M, 1) %Circular shift once along dimension 1
circshift(M, 2) %Circular shift twice along dimension 1
circshift(M, 1, 2) %Circular shift once along dimension 2














