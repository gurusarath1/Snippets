/*
 * INPUT TESTING
 *
 *  Created on: 09-Jul-2014
 *      Author: Guru Sarath
 */
#include <msp430x11x1.h>
#define BUTTON BIT3
#define LED1 BIT0
#define LED2 BIT1

void main(void)
{
	int i;
WDTCTL = WDTPW|WDTHOLD;
P1OUT = ~(LED1+LED2) ;
P1DIR |= LED1;
P1DIR |= LED2;

while(1){
if((P1IN & 0x08) == 0x08 )
{P1OUT = LED1;
break;
}else {;}

}

for(i=0;i<30000;i++);

while(1){

if((P1IN & 0x08) == 0x08 )
{
P1OUT |= LED2;
break;
}

}

while (1)
{

	if((P1IN & 0x08) == 0x08 )
	{for(i=0;i<20000;i++);
		P1OUT = ~P1OUT;
	}

}

}

