/*
 * WATCH DOG TIMER
 *
 */
#include <msp430g2553.h>

void main(void) {
	int i;
	//WDTCTL = WDTPW | WDTHOLD ; //stop WDT
	WDTCTL = WDTPW | WDTSSEL | WDTCNTCL;

	P1OUT = 0x40; // green LED will indicates that the program is getting reset
	P1DIR = 0x41;
	for(i=0;i<1000;i++);

	while(1){
	P1OUT = 0X01; // red LED ON
	for(i=0;i<10000;i++);

	P1OUT = 0X00; // red LED OFF

	for(i=0;i<10000;i++);

	/* if the watch dog timer was stopped, the program will get stuck in this loop
		and the red led will blink
				but if it is ON(running)
				the green led will blink fast (because of reset(PUC)) */
			}
}
