/**
  ******************************************************************************
  * @file    waverecorder.h
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
#ifndef __WAVERECORDER_H
#define __WAVERECORDER_H

/* Includes ------------------------------------------------------------------*/
/* Exported types ------------------------------------------------------------*/
/* Exported Defines ----------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported macro ------------------------------------------------------------*/
/* Exported functions ------------------------------------------------------- */
uint8_t   WaveRecorderStart(uint16_t* pBuf, uint32_t wSize);
uint32_t  WaveRecorderStop(void);
void      WaveRecorderProcess(void);

#endif /* __WAVERECORDER_H */


