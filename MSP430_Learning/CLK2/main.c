/*
 * main.c
 */
#include <msp430g2553.h>
#include <TI_USCI_I2C_master.h>
void main(void) {
	unsigned char tx = { 0x00 , 0x01 ,0x11 };
	unsigned char rx = 0x00;
	TI_USCI_I2C_transmitinit(104,0x15);
	TI_USCI_I2C_transmit(1,tx);

	TI_USCI_I2C_receiveinit(104,0x15);
	TI_USCI_I2C_receive(1,rx);
	
	while(1);
}
