%Created by Guru Sarath
%20 April 2019
filename = 'DataSample.csv';
delimiterIn = ',';
headerlinesIn = 1;
A = importdata(filename,delimiterIn,headerlinesIn)
A.data
A.textdata
A.colheaders