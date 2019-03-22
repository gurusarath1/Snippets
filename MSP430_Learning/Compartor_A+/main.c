/*
Basic operation of comparator A+
P1.0 +ve input (CA0)
P1.1 -ve input (CA1)
P1.7 output (CAOUT)
 */
#include <msp430g2553.h>
void main(void) {
	WDTCTL = WDTPW | WDTHOLD;

	CACTL1 = CAON; //turn ON the comparator
	CACTL2 = P2CA1 | P2CA0 ; //select  inputs
	CAPD = CAPD0|CAPD1; //disable the input buffers of CA0 and CA1 inputs
	
	P1SEL |= BIT0|BIT1|BIT7; //select alternative function of the pins
	P1DIR |= BIT7; //comparator output

	while(1);
}
