/*
 * TIMER0_A3 EXTERNAL CLOCK
timer0_A3 clocked with an external clock (on pin P1.0)(using a 555 timer in astable mode)
timer0 is configured in mode 1(UP)
red LED indicates the state of the external clock (HIGH or LOW)
toggling of the yellow LED indicates an interrupt due to capture compare register 0
 */

#include <msp430g2553.h>

void main(void) {
	WDTCTL = WDTPW|WDTHOLD;

	P1OUT =  0X00;
	P1DIR = 0X40; // output on yellow LED
	P1SEL = 0X01; // select the alternate function of pin P1.0

	_bis_SR_register(GIE);
	TA0CTL = TASSEL_0|ID_0|MC_1|TACLR; //external source |no internal divider | UP mode | clear timer
	TACCTL0 |= CCIE; // enable capture compare register 0 interrupt
	TACCR0 = 0X000f; // maximum count 15


	while(1);
	
}

#pragma vector = TIMER0_A0_VECTOR

__interrupt void timerc0(void)
{

	P1OUT ^= 0X40; // toggle yellow LED
	// interrupt flag is cleared automatically
}

//code below is not needed (because timer overflow interrupt is not enabled in the program)

#pragma vector = TIMER0_A1_VECTOR

__interrupt void timer(void)
{
	switch (TA0IV)  // interrupt flag is cleared as soon as ta0iv register is read
	{

	case 0x0A :P1OUT ^= 0X40;

	default : break;

	}
}






