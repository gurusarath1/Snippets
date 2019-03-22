/*
PIR SENSOR INTERFACE USING COMPARATOR
 */
#include <msp430g2553.h>
void main(void) {
	WDTCTL = WDTPW | WDTHOLD;
	P1OUT = 0X00;
	P1DIR = BIT6|BIT1;
	P1SEL = BIT0;

	CACTL1 = CAON | CAREF_1 | CAIE;
	CACTL2 = P2CA0|CAF;

	_bis_SR_register(GIE);

	while(1)_bis_SR_register(GIE|LPM4);
	
}

#pragma vector =  COMPARATORA_VECTOR
__interrupt void port (void)
{
	int i;


	for(i=0;i<20;i++)
	{
	P1OUT ^= BIT6|BIT1;
	__delay_cycles(200000);
	}

	for(i=0;i<100;i++)
	{
	P1OUT ^= BIT6|BIT1;
	__delay_cycles(50000);
	}

	for(i=0;i<100;i++)
	{
	P1OUT ^= BIT6|BIT1;
	__delay_cycles(70000);
	}


	P1OUT = BIT6|BIT1;

	__delay_cycles(10000000);

	P1OUT &= ~(BIT6|BIT1);

	CACTL1 &= ~CAIFG;
}
