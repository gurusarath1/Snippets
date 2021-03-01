module firstOne (
  input [3:0] a,
  output [2:0] k);
  
  wire a0_bar, a1_bar, sig1, sig2;
  wire sig3, sig4, sig5;
  wire a2_bar, sig6, sig7;
  
  not N1(a0_bar, a[0]);
  not N2(a1_bar, a[1]);
  and AND1(sig1, a0_bar, a1_bar);
  and AND2(sig2, sig1, a[2]);
  or OR1(k[0], sig2, a[0]); // k[0] = a[0] + a[0]' a[1]' a[2]
  
  and AND3(sig3, a0_bar, a[1]);
  and AND4(sig4, a0_bar, a1_bar);
  and AND5(sig5, sig4, a[2]);
  or OR2(k[1], sig3, sig5); // k[1] = a[1] a[0]' + a[0]' a[1]' a[2]
  
  and AND6(sig6, a0_bar, a1_bar);
  not N3(a2_bar, a[2]);
  and AND7(sig7, sig6, a2_bar);
  and AND8(k[2], sig7, a[3]); // k[2] = a[0]' a[1]' a[2]' a[3]
  
endmodule