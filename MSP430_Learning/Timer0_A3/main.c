/*
BASIC TIMER0_A3 OPERATION
 */

#include <msp430g2553.h>
void main(void) {
	WDTCTL = WDTPW | WDTHOLD;

	P1OUT = 0X00;
	P1DIR = 0X41;
	_bis_SR_register(GIE);


	BCSCTL3 = LFXT1S_2; /* SOURCE ACLK FROM VLO */
	P2SEL = 0; //use port 2 pins as basic input output
	P2DIR = 0; //port 2 as input
	P2REN = BIT6|BIT7; // pull up resistors for unused pins (XIN and XOUT)

	TA0CTL = TASSEL_1|ID_0|MC_1|TAIE; //timer a clocked from aclk
	TA0CCR0 = 0X0F00; // maximum count

	while(1){P1OUT |= 0X40;}
	
}

#pragma vector = TIMER0_A1_VECTOR
__interrupt void TIMER_ISR(void)
{
	switch(TA0IV)
	{

	case 0x000A:

			P1OUT ^= 0X41;

	default: break;

	}


}
