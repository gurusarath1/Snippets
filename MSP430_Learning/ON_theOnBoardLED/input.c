/*
 * main.c
 */
#include <msp430g2553.h>

void main(void) {

unsigned int i,delay_int=6000;

WDTCTL = WDTPW | WDTHOLD;
P1DIR = 0Xff;

while(1)
{
	P1OUT = 0X40;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X41;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X01;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X00;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X01;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X41;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X40;
	for(i=0;i<delay_int;i++);
	P1OUT = 0X00;
	for(i=0;i<delay_int;i++);

}
}
