/*
 * main.c
 *
 */
#include <msp430g2553.h>

void main(void) {
	int i;
	WDTCTL = WDTPW | WDTSSEL | WDTCNTCL |WDTTMSEL;
	IE1 |= WDTIE;
	IFG1 |= WDTIFG;
	P1DIR = 0x41;

	BCSCTL3 = LFXT1S_2; /* SOURCE ACLK FROM VLO */
	P2SEL = 0; //use port 2 pins as basic input output
	P2DIR = 0; //port 2 as input
	P2REN = BIT6|BIT7; // pull up resistors for unused pins (XIN and XOUT)

	_bis_SR_register(GIE);


	while(1){
	P1OUT = 0X01; // RED LED ON
	for(i=0;i<10000;i++);

	P1OUT = 0X00; // RED LED OFF

	for(i=0;i<10000;i++);

			}
}

#pragma vector = WDT_VECTOR
__interrupt void  WDTISR(void)
{
	int i,j;

	for(j=0;j<10;j++){
	P1OUT = 0X40; // GREEN LED ON
	for(i=0;i<10000;i++);

	P1OUT = 0X00; // GREEN LED OFF

	for(i=0;i<10000;i++);
	}


}
