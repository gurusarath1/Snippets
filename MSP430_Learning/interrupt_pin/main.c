/*
IO PIN INTERRUPT
 */

#include <msp430g2553.h>

void main(void) {
	WDTCTL = WDTPW | WDTHOLD;
	P1OUT = 0X41;
	P1DIR = 0X41;
	P1IE = 0X02;
	//P1REN = 0X02;
	P1IES = 0X00; // low to high interrupt

	do
	{
		P1IFG = 0X00;

	}while(P1IFG != 0X00); // THIS LOOP PREVENTS UNWANTED INTERRUPTS

	_bis_SR_register(GIE);
	while(1){;}

}

#pragma vector = PORT1_VECTOR
__interrupt void PORT1_ISR (void)
{
	do
	{
		P1IFG = 0X00;

	}while(P1IFG != 0X00);

	P1OUT ^= 0X41;
	
	do
	{
		P1IFG = 0X00;

	}while(P1IFG != 0X00);

}
