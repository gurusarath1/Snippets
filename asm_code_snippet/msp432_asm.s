	area testing, code, readonly
	export __main


__main    proc



			; Move instruction ----------------------------------------------------
			mov r1, #0x10  ; r1 = 0x10
			mov r1, #0x20
			mov r2, #0x30
			mov r3, #0x40
			mov r3, r1   ; r3 = r1
			mov r2, r1
			; ---------------------------------------------------------------------
			
			
			
			
			
			
			; load/store instructions ----------------------------------------------
			
			ldr r1, =0x20002000   ; r1 = 0x20002000
			
			mov r2, #0xA0B0
			str r2, [r1]     ; Register to memory ; [r1] = r2
			str r2, [r1, #0x6]     ; Register to memory ; [r1 + 0x6] = r2
			
			ldr r8, [r1, #0x6]  ; Memory to register ; r8 = [r1 + 0x6]
			ldrb r9, [r1, #0x6]  ; Memory to register ; r8 = [r1 + 0x6] only one byte copy
			
			; ----------------------------------------------------------------------
			
			
			
			
			
			
			
			
			
			
			
			
			mov r1, #0x22
			; if statement ----------------------------------------------
			cmp r1, #0x22
			beq if_part     ; if(r1 == 0x20)

else_part	
			; else case  ; Do something
			mov r1, #0xABCD
			mov r2,r1
			orr r3, r1  ; OR operation ; r3 = r1 | r3
			
			b end_of_if

if_part		
			; if case ; Do something
			mov r1, #0xFFFF
			mov r2,r1
			and r3, r1   ; AND operation ; r3 = r1 | r3
			

end_of_if
			; -----------------------------------------------------------
			
			
			
			
			
			
			
			
			
			
		
			
			mov r1, #0
			; do while -----------------------------------------------------

do			
			; Do something
			add r1, #5
			eor r5, r1   ; XOR operation ; r5 = r1 xor r5
			
			
			cmp r1, #20 
			ble do     		; while(r1 <= 20)
			
			; -----------------------------------------------------------
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			; Turn on/off LED in deug mode ------------------------------------------
			
			
			ldr r0, =0x40004C00
			add r0, #0x21
			
			mov r1, #0x02
			strb r1, [r0, #0x04]  ; Direction register
			
			mov r3, #02
			strb r3, [r0, #0x02]  ; output register
			
			mov r3, #00
			strb r3, [r0, #0x02]			
			
			mov r3, #02
			strb r3, [r0, #0x02]

			mov r3, #00
			strb r3, [r0, #0x02]

			; -----------------------------------------------------------------------
			
			
			
			
			
			
			
			
			
			
			
			
			
			; Infinite loop -----------------------------------------------------
			
loopX		
			add r1, #0x01  ; Do something
			add r2, #0x03  ; Do something
			
			b loopX
			
			; -----------------------------------------------------------
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			; Some dummy instructions
			mov r1, #0x00
			mov r2, #0x00
			mov r3, #0x00
			
			

	endp

	end
