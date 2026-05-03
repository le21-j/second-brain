/**
  ******************************************************************************
  * @file    waveplayer.c
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

/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/

/* Private function prototypes -----------------------------------------------*/
/* Private functions ---------------------------------------------------------*/

/*--------------------------------
Callbacks implementation:
The callbacks prototypes are defined in the stm32f4_discovery_audio_codec.h file
and their implementation should be done in the user code if they are needed.
Below some examples of callback implementations.
--------------------------------------------------------*/

/**
  * @brief  Manages the DMA Half Transfer complete interrupt.
  * @param  None
  * @retval None
  */
void BSP_AUDIO_OUT_HalfTransfer_CallBack(void)
{ 

}

/**
* @brief  Calculates the remaining file size and new position of the pointer.
* @param  None
* @retval None
*/
void BSP_AUDIO_OUT_TransferComplete_CallBack(void)
{

}

/**
* @brief  Manages the DMA FIFO error interrupt.
* @param  None
* @retval None
*/
void BSP_AUDIO_OUT_Error_CallBack(void)
{
  /* Stop the program with an infinite loop */
  while (1)
  {}
  
  /* Could also generate a system reset to recover from the error */
  /* .... */
}


