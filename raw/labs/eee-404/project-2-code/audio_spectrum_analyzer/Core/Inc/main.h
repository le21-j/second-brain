/**
  ******************************************************************************
  * @file    main.h
  * @author  Dr. Chao Wang, Arizona State University, chao.wang.6@asu.edu
  * @version V1.0.0
  * @date    07/31/2024
 ******************************************************************************
  * @attention
  *
  * Project 2: Applications of Fast Fourier Transform
  *
  * All course materials for this class are protected by copyright and
  * may not be shared, reproduced, or uploaded to any website
  * without the written permission of the instructor.
  *
  * This software is developed based on the example provided by STMicroelectronics
  * at https://www.st.com/en/embedded-software/stsw-stm32068.html
  * Specifically, the "Audio playback and recording using the STM32F4DISCOVERY"
  * Application note AN3997.
  *
  ******************************************************************************
*/
  
/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

/* Includes ------------------------------------------------------------------*/
#include <stdio.h>
#include "stm32f4xx_hal.h"
#include "stm32f4_discovery.h"
#include "stm32f4_discovery_audio.h"
#include "stm32f4xx_it.h"
#include "waveplayer.h"
#include "waverecorder.h"

#define MICROPHONE_IN_FRAME_SIZE 16 // 16 x 16-bit data
#define FFT_SIZE 1024
#define AUDIO_STORAGE_BUFFER_SIZE 1024
#define ARM_MATH_CM4
#include "arm_math.h"



/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/

/* Defines for the Audio used commands */
#define CMD_PLAY           ((uint32_t)0x00)
#define CMD_RECORD         ((uint32_t)0x01)
#define CMD_STOP           ((uint32_t)0x02)

/* Defines for LEDs lighting */
#define LED3_TOGGLE      0x03  /* Toggle LED3 */
#define LED4_TOGGLE      0x04  /* Toggle LED4 */
#define LED6_TOGGLE      0x06  /* Toggle LED6 */
#define LEDS_OFF         0x07  /* Turn OFF all LEDs */
#define STOP_TOGGLE      0x00  /* Stop LED Toggling */

/* Defines for the Audio playing process */
#define PAUSE_STATUS     ((uint32_t)0x00) /* Audio Player in Pause Status */
#define RESUME_STATUS    ((uint32_t)0x01) /* Audio Player in Resume Status */
#define IDLE_STATUS      ((uint32_t)0x02) /* Audio Player in Idle Status */

#define REPEAT_ON        ((uint32_t)0x00) /* Replay Status in ON */
#define REPEAT_OFF       ((uint32_t)0x01) /* Replay Status in OFF */


#define USARTx                           USART2
#define USARTx_CLK_ENABLE()              __USART2_CLK_ENABLE();
#define DMAx_CLK_ENABLE()                __DMA1_CLK_ENABLE()
#define USARTx_RX_GPIO_CLK_ENABLE()      __GPIOA_CLK_ENABLE()
#define USARTx_TX_GPIO_CLK_ENABLE()      __GPIOA_CLK_ENABLE() 

#define USARTx_FORCE_RESET()             __USART2_FORCE_RESET()
#define USARTx_RELEASE_RESET()           __USART2_RELEASE_RESET()

/* Definition for USARTx Pins */
#define USARTx_TX_PIN                    GPIO_PIN_2
#define USARTx_TX_GPIO_PORT              GPIOA
#define USARTx_TX_AF                     GPIO_AF7_USART2
#define USARTx_RX_PIN                    GPIO_PIN_3
#define USARTx_RX_GPIO_PORT              GPIOA
#define USARTx_RX_AF                     GPIO_AF7_USART2

/* Definition for USARTx's DMA */
#define USARTx_TX_DMA_CHANNEL             DMA_CHANNEL_4
#define USARTx_TX_DMA_STREAM              DMA1_Stream6
#define USARTx_RX_DMA_CHANNEL             DMA_CHANNEL_4
#define USARTx_RX_DMA_STREAM              DMA1_Stream5

/* Definition for USARTx's NVIC */
#define USARTx_DMA_TX_IRQn                DMA1_Stream6_IRQn
#define USARTx_DMA_RX_IRQn                DMA1_Stream5_IRQn
#define USARTx_DMA_TX_IRQHandler          DMA1_Stream6_IRQHandler
#define USARTx_DMA_RX_IRQHandler          DMA1_Stream5_IRQHandler
                                                                                    
/* Exported macro ------------------------------------------------------------*/
/* Exported functions ------------------------------------------------------- */
void Error_Handler(void);

#define TIMx                           TIM3
#define TIMx_CLK_ENABLE                __TIM3_CLK_ENABLE

/* Definition for TIMx's NVIC */
#define TIMx_IRQn                      TIM3_IRQn
#define TIMx_IRQHandler                TIM3_IRQHandler

#endif /* __MAIN_H */
