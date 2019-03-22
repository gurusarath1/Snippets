/*
TIMER0_A3 CAPTURE
 */

#include <msp430g2553.h>

unsigned int start_time = 0x00;
unsigned int end_time = 0x00;
unsigned int capture = 0;

void main(void) {
	int i;
	WDTCTL = WDTPW|WDTHOLD;
	P1OUT = 0X00;
	P1DIR = ~(BIT1) | 0x41; //P1.1 configured as input
	P1SEL = BIT1; //CAPTURE INPUT (select alternate function of the input)
	_bis_SR_register(GIE);
	TA0CCTL0 = CM_3 | CCIS_0 | SCS | CAP | CCIE;
	TA0CTL = TASSEL_1 | ID_0 | MC_2 |TACLR;

	while(1)
	{
		P1OUT ^= 0X40; //blink yellow led
		for(i=0;i<10000;i++); //yellow blink indicates waiting for capture
	}

}

#pragma vector = TIMER0_A0_VECTOR

__interrupt void TIMER_CAP(void)
{

	if (capture == 0)
	{
		start_time = TA0CCR0;
		P1OUT |= 0x01; //red led turns ON - rising edge was capture
		capture = 1;
	}else{
		end_time  = TA0CCR0;
		P1OUT &= ~(0x01); //red led goes OFF - indicates falling edge was captured
		capture = 0;
	}

}
