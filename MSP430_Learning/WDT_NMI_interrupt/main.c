/*
 * NMI INTERRUPT
 */

#include <msp430g2553.h>
void main(void) {
	WDTCTL = WDTPW | WDTCNTCL | WDTHOLD | WDTNMI |WDTNMIES;
	P1DIR = 0x41;
	IE1 |= NMIIE;
	//IFG1 |= NMIIFG; //software can also call an interrupt
	while(1)P1OUT = 0x01;
}

#pragma vector = NMI_VECTOR

__interrupt void NMI_ISR(void)
{
	int i,j;
	IFG1 &= ~NMIIFG; //clear int NMI interrupt flag
	for(j=0;j<10;j++){
	P1OUT = 0X40; // GREEN LED ON
	for(i=0;i<30000;i++);

	P1OUT = 0X00; // GREEN LED OFF

	for(i=0;i<30000;i++);
	}

	IE1 |= NMIIE; //u hav to re enable the nmi interrupt

}
