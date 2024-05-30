/*
 * flysky_ibus.h
 *
 *  Created on: Feb 4, 2021
 *      Author: mokhwasomssi
 */


 // From INAV sources
 // The protocol is driven by the iBus receiver, currently either an IA6B or
 // IA10. All iBus traffic is little endian. It begins with the iBus rx
 // querying for a sensor on the iBus:
 //
 //
 //  /---------\
 //  | IBUS RX | > Hello sensor at address 1, are you there?
 //  \---------/     [ 0x04, 0x81, 0x7A, 0xFF ]
 //
 //     0x04       - Packet Length
 //     0x81       - bits 7-4 Command (1000 = discover sensor)
 //                  bits 3-0 Address (0001 = address 1)
 //     0x7A, 0xFF - Checksum, 0xFFFF - (0x04 + 0x81)


#ifndef __IBUS_H__
#define __IBUS_H__


//#include "usart.h"              // header from stm32cubemx code generate
#include <stdbool.h>
#include <stdint.h>

/* User configuration */
//#define IBUS_UART				(&huart1) // CHANGES ON ---->
//                   <-----------------------------------------------
#define UART1_TX 104
#define UART1_RX 103
#define UART2_TX 14
#define UART2_RX 102
//--------------------
#define IBUS_USER_CHANNELS		6		// Use 6 channels


/* Defines */
#define IBUS_LENGTH				0x20	// 32 bytes
#define IBUS_COMMAND40			0x40	// Command to set servo or motor speed is always 0x40
#define IBUS_MAX_CHANNLES		14


 

/* Main Functions */
void ibus_init();
bool ibus_read(uint16_t* ibus_data);


/* Sub Functions */
bool ibus_is_valid();
bool ibus_checksum();
void ibus_update(uint16_t* ibus_data);
void ibus_soft_failsafe(uint16_t* ibus_data, uint8_t fail_safe_max);
void ibus_reset_failsafe();

#endif /* __IBUS_H__ */