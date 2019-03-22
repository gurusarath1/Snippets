/*
 * main.c
 */
#include <msp430g2553.h>
#include <intrinsics.h>
#ifndef TIMER0_A1_VECTOR
#define TIMER0_A1_VECTOR    TIMERA1_VECTOR
#define TIMER0_A0_VECTOR    TIMERA0_VECTOR
#endif
#define LED1 BIT6
#define LED2 BIT0


void main(void) {


	WDTCTL = WDTPW|WDTHOLD;
	P1OUT = LED1|LED2;
	P1DIR = LED1|LED2;
	_BIS_SR(GIE);
	TA0CTL = MC_2|ID_3|TACLR|TASSEL_2|TAIE;
	

	for(;;);

}

#pragma vector = TIMER0_A0_VECTOR
__interrupt void TA0_ISR(void)
{
			TA0CTL |= TACLR;
			TA0CTL = MC_2|ID_3|TACLR|TASSEL_2|TAIE;
			P1OUT = ~P1OUT;


}
