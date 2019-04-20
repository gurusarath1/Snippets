% Created by Guru Sarath
% 10 April 2019

Var_one = 1;
Var_two = 2;
printf("Var_one = %d\n",Var_one)
printf("Var_two = %d\n",Var_two)

%Bit setting and clearing operation
Var_two = bitset(Var_two, 1); %Set bit 1
Var_one = bitset(Var_one, 6); %Set bit 6
printf("Var_one (After setting bit 6) = %d\n",Var_one)
printf("Var_two (After setting bit 1) = %d\n",Var_two)
Var_one = bitset(Var_one, 6, 0); %Clear bit 6
printf("Var_one (After setting bit 6 to 0) = %d\n",Var_one)

bitget(Var_two, 2) %Get the 2nd bit

%Bit shifting 
VarX = bitshift(Var_one, 1) %Left shift
printf('After shifting once (Left) %d\n',VarX); 
VarX = bitshift(VarX, 1)
printf('After shifting twice (Left) %d\n',VarX);
VarX = bitshift(VarX, 1)
printf('After shifting thrice (Left) %d\n',VarX);
VarX = bitshift(VarX, -2) %Right shift
printf('After shifting twice (Right) %d\n',VarX);

%Logical bit operations 
bitand(Var_one, Var_two)
bitor(Var_one, Var_two)
bitxor(Var_one, Var_two)
