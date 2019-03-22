/*
Standard LCD module interfaced (in 4bit mode) with the launchpad
P1.0 - P1.7 {8 bit data input to the LCD}
P2.0 - register select
P2.1 - read/write
P2.2 - enable
 */
#include <msp430g2553.h>
#define delay __delay_cycles(800)
#define delay1ms __delay_cycles(1100);
#define delay10ms __delay_cycles(2200);
#define delay_large __delay_cycles(50000);
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
#define SLAVE_ADDRESS 0x68

void data_in(unsigned char);
void command_in(unsigned char);
void reset_4bit(void);
void flash(void);

void i2c_transmit(char);

void init_i2c(void);
void clock_set(char,char,char,char,char,char,char,char);
void clock_receive(char);

void disp(char);
void day_disp(char);


void main(void) {
	int i;
	char first = 1;
	/*initialize the microcontroller */
	WDTCTL = WDTPW|WDTHOLD;
	init_i2c();

	P1OUT = 0X00;
	P1DIR = 0X0f;
	P2OUT = 0X00;
//           rs    rw   e	BUZ
	P2DIR |= BIT0|BIT1|BIT2|BIT3;


	/*initialize the LCD in 4 bit mode*/
	reset_4bit();
	command_in(0x0c);

//	clock_set(sec,  min,hour,day,date,month,year,set)
	clock_set(0x00,0x35,0x12,0x02,0x06,0x10,0x14,0x80);

	clock_receive(first);


	while(1){

		clock_receive(0x00);


		for(i=0;i<100;i++)delay10ms;
	}


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



void clock_receive(char first)
{
	char sec,min,hour,day,year,date,month;

	init_i2c();
	i2c_transmit(0x00);
	//command_in(lcd_clear);

    UCB0CTL1 &= ~UCTR ;  // Clear I2C TX flag for receive
    UCB0I2CSA = 0x68;
    UCB0CTL1 |= UCTXSTT;    // I2C start condition with NACK for single byte reading
    while((IFG2 & UCB0RXIFG) == 0);// Start condition sent? RXBuffer full?
    sec = UCB0RXBUF;
    while((IFG2 & UCB0RXIFG) == 0);
    min = UCB0RXBUF;
    while((IFG2 & UCB0RXIFG) == 0);
    hour = UCB0RXBUF;
    if(first ||  min == 0x00){
    while((IFG2 & UCB0RXIFG) == 0);
    day = UCB0RXBUF;
    while((IFG2 & UCB0RXIFG) == 0);
    date = UCB0RXBUF;
    while((IFG2 & UCB0RXIFG) == 0);
    month = UCB0RXBUF;
    while((IFG2 & UCB0RXIFG) == 0);
    year = UCB0RXBUF;
    }
    UCB0CTL1 |= UCTXSTP;


    command_in(cursor_line1);
    disp(hour);
    data_in(':');
    disp(min);
    data_in(':');
    disp(sec);

    if(first)
    {
    	command_in(cursor_right);
    	command_in(cursor_right);
    	command_in(cursor_right);

    	data_in('G');
    	data_in('U');
    	data_in('R');
    	data_in('U');

    }

    if(first || min == 0x00){
    command_in(cursor_line2);
    disp(date);
    data_in('/');
    disp(month);
    data_in('/');
    data_in('2');
    data_in('0');
    disp(year);

    day_disp(day);
    }

    if(min == 0x00 && sec == 0x00)
    {P2OUT |= BIT3;
    delay_large;}else{
    P2OUT &= ~BIT3;}




}

void clock_set(char sec,char min,char hour,char day,char date,char month,char year,char set)
{
	while (UCB0CTL1 & UCTXSTP);
	UCB0CTL1 |= UCTR;
	UCB0I2CSA = 0x68;
	UCB0CTL1 |= UCTXSTT;
	while((IFG2 & UCB0TXIFG) == 0);  //set when stt con
	UCB0TXBUF = 0x00; //starting address

	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = sec;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = min;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = hour;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = day;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = date;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = month;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = year;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0TXBUF = set;
	while((IFG2 & UCB0TXIFG) == 0);


	UCB0CTL1 |= UCTXSTP;

}



void init_i2c(void) {
	P1SEL |= BIT6|BIT7;
	P1SEL2 |= BIT6|BIT7;

          UCB0CTL1 |= UCSWRST;                      // Enable SW reset
          UCB0CTL0 = UCMST + UCMODE_3 + UCSYNC;     // I2C Master, synchronous mode
          UCB0CTL1 = UCSSEL_2 + UCSWRST;            // Use SMCLK, keep SW reset
          UCB0BR0 = 13;                             // fSCL = 1Mhz/10 = ~100kHz
          UCB0BR1 = 0;
          UCB0I2CSA = 0x68;                   // Slave Address is 069h
          UCB0CTL1 &= ~UCSWRST;                     // **Initialize USCI state machine**
}

void disp(char dat)
{
data_in(((0xf0 & dat)>>4) | 0x30);
data_in((0x0f & dat) | 0x30);
}

void day_disp(char day)
{
	command_in(cursor_right);
	command_in(cursor_right);
	command_in(cursor_right);
	if(day == 1) {data_in(0x30|day); data_in('S');}
	if(day == 2) {data_in(0x30|day);data_in('M');}
	if(day == 3) {data_in(0x30|day);data_in('T');}
	if(day == 4) {data_in(0x30|day);data_in('W');}
	if(day == 5) {data_in(0x30|day);data_in('T');}
	if(day == 6) {data_in(0x30|day);data_in('F');}
	if(day == 7) {data_in(0x30|day);data_in('S');}
}

void i2c_transmit(char reg)
{
	while (UCB0CTL1 & UCTXSTP);
	UCB0CTL1 |= UCTR;
	UCB0I2CSA = 0x68;
	UCB0CTL1 |= UCTXSTT;
	while((IFG2 & UCB0TXIFG) == 0);  //set when stt con
	UCB0TXBUF = reg;
	while((IFG2 & UCB0TXIFG) == 0);
	UCB0CTL1 |= UCTXSTP;

}
