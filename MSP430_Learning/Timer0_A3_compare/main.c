/*
 * TIMER0_A3 COMPARE
when the value of count in the timer register is equal to the value in TA0CCR1
the program toggles the on board yellow LED
(capture compare channel 1 is programmed in conmpare mode)
(the output signal of channel 1 is in PIN P1.6)
(the output signal of channel 0 is in PIN p1.5)
 */

#include <msp430g2553.h>

void main(void) {
	WDTCTL = WDTPW|WDTHOLD;

	P1OUT = 0X00;
	P1DIR = BIT6; //P1.6 as output (on board yellow LED)
	P1SEL = BIT6; //select the alternate function of the pin P1.6 (output of compare channel 1)

	BCSCTL3 = LFXT1S_2; /* SOURCE ACLK FROM VLO */
	P2SEL = 0; //use port 2 pins as basic input output
	P2DIR = 0; //port 2 as input
	P2REN = BIT6|BIT7; // pull up resistors for unused pins (XIN and XOUT)

	TA0CCTL1 |= OUTMOD_4; //toggle mode
	TA0CTL |= TASSEL_1|ID_0|MC_1|TACLR; // ACLK|no divider|up mode|clear
	TA0CCR0 = 0X0FFF; // maximum count in up mode
	TA0CCR1 = 0X0FFF; // compare value (toggle the yellow LED when TA0R == 0x0fff)

	while(1);

}



