/*
COMPARATOR A+ INTERRUPT
+ve input - CA2
-ve input - 0.5Vcc
output - P1.7 (CAOUT)

on falling edge of the comparator output both the on board LEDs blink once
 */
#include <msp430g2553.h>
void main(void) {

	WDTCTL = WDTPW | WDTHOLD;
	P1OUT =  0x00;
	P1DIR = BIT0|BIT6; //on board LEDs as output

//  CACTL1 = reference given to -ve i/p| 0.5Vcc | ON |falling edge |enable interrupt
	CACTL1 = CARSEL | CAREF_2 | CAON | CAIES | CAIE;
//	CACTL2 = select CA2 as +ve input | enable output filter
	CACTL2 = P2CA0 | P2CA4 | CAF ;
	CAPD = CAPD2; //disable pin's (P1.2(CA2)) input buffer


	P1SEL = BIT2|BIT7; //select alternative function
	P1DIR |= BIT7; //output of comparator
	_bis_SR_register(GIE); // enable interrupts
	
	while(1);
}

#pragma vector = COMPARATORA_VECTOR
__interrupt void compAISR(void)
{

	//blink the on board red and yellow LED once
	P1OUT ^=  BIT0|BIT6;
	__delay_cycles(100000); // delay
	P1OUT ^=  BIT0|BIT6;

	// interrupt flag is automatically cleared
}
