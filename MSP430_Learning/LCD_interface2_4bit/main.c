/*
Standard LCD module interfaced (in 4bit mode) with the launchpad
P1.0 - P1.3 {d4 - 7}
P2.0 - register select
P2.1 - read/write
P2.2 - enable
 */
#include <msp430g2553.h>
#define delay __delay_cycles(800)
#define delay1ms __delay_cycles(1100);
#define delay10ms __delay_cycles(2200);
#define lcd_matrix 0x38
#define lcd_off 0x08 //lcd off cursor off
#define lcd_on 0x0c //lcd on cursor off
#define lcd_clear 0x01
#define cursor_home 0x02
#define cursor_left 0x10
#define cursor_right 0x14
#define cursor_blink1 0x0e
#define cursor_blink2 0x0f
#define cursor_off 0x0c //lcd on cursor off
#define cursor_line1 0x80
#define cursor_line2 0xc0
#define display_left 0x18

void data_in(unsigned char);
void command_in(unsigned char);
void reset_4bit(void);
void flash(void);

void main(void) {
	int i;
	char text_stream1 [] = "T.GURU SARATH";
	char text_stream2 [] = "MSP430G2553";

	/*initialize the microcontroller */
	WDTCTL = WDTPW|WDTHOLD;

	P1OUT = 0X00;
	P1DIR = 0X0f;
	P2OUT = 0X00;
	P2DIR |= BIT0|BIT1|BIT2;
	delay;

	reset_4bit();

	for(i = 0 ;i<13;i++)
	data_in(text_stream1 [i]);

	command_in(0xc0);

	for(i = 0 ;i<11;i++)
	data_in(text_stream2 [i]);

	/* put the MCU in low power mode */
	while(1)__bis_SR_register(LPM4);

}

void data_in(unsigned char data)
{
	P2OUT |= BIT0; //data register
	P2OUT &= ~BIT1; //write mode

	P1OUT = (0xf0 & data)>>4;
	flash();


	P1OUT = 0x0f & data;
	flash();
	P1OUT = 0X00; //clear the data lines
}

void command_in(unsigned char command)
{
	P2OUT &= ~BIT0; //command register
	P2OUT &= ~BIT1; //write mode

	P1OUT = (0xf0 & command)>>4;
	flash();


	P1OUT = 0x0f & command;
	flash();

	P1OUT = 0X00;//clear the data lines
}



void reset_4bit(void)
{
	P2OUT &= ~BIT0; //command register
	P2OUT &= ~BIT1; //write mode

	delay10ms;
	delay10ms;
	delay10ms;
	delay10ms;
	delay10ms;
	delay10ms;

	P1OUT = 0X03;
	flash();

	delay10ms;
	P1OUT = 0X03;
	flash();

	delay1ms;
	P1OUT = 0X03;
	flash();

	delay1ms;
	P1OUT = 0X02;
	flash();

	delay10ms;


	///
	P1OUT = 0x02;   //function set
	flash();
	P1OUT = 0x08;
	flash();

	P1OUT = 0x00;   // on off
	flash();
	P1OUT = 0x0f;
	flash();

	P1OUT = 0x00;  //clear
	flash();
	P1OUT = 0x01;
	flash();

	P1OUT = 0x00;   //entry
	flash();
	P1OUT = 0x06;
	flash();

	P1OUT = 0x00;   //entry
	flash();
	P1OUT = 0x02;
	flash();

}

void flash(void)
{

	/*flash the enable pin */
	P2OUT |= BIT2;
	delay1ms;
	P2OUT &= ~BIT2;
	delay1ms;
}
