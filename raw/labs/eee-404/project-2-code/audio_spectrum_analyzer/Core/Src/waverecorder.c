/**
  ******************************************************************************
  * @file    waverecorder.c
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
#include "waverecorder.h" 
#include "pdm_filter.h" // microphone
#include "arm_math.h" // fft
#include "hamming.h" // window function
#include "hanning.h" // window function

/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
extern uint16_t AudioOutBuffer[]; // circular buffer to store processed audio data which is sent to audio DAC to play
uint16_t Buffer_m_i_pointer =0; // circular buffer pointer, increment when new microphone data becomes available

// microphone related
static uint16_t InternalBuffer[INTERNAL_BUFF_SIZE];  // microphone PDM buffer
uint16_t MicrophoneInBuffer[MICROPHONE_IN_FRAME_SIZE]; // buffer to store microphone PCM data

// fft related
extern arm_rfft_fast_instance_f32 fft_handler; // FFT structure
uint16_t Buffer_fft_pointer =0; // circular buffer pointer, wait for FFT size to process
float FFTInBuffer[FFT_SIZE]; // input FFT array
float FFTOutBuffer[FFT_SIZE]; // store FFT output

// Serial related
extern UART_HandleTypeDef UartHandle; //serial
uint8_t SerialOutBuffer[FFT_SIZE/2+1];

int16_t data_in, ldata_out, rdata_out; // store audio data

/* Private function prototypes -----------------------------------------------*/
void Process_Out(void);
// fft window function
void apply_window(float* signal_segment, float* window_function, uint16_t length);

/* Private functions ---------------------------------------------------------*/
uint8_t WaveRecorderStart(uint16_t* pBuf, uint32_t wSize)
{
  return (BSP_AUDIO_IN_Record(pBuf, wSize));
}

/**
  * @brief  Stop Audio recording.
  * @param  None
  * @retval None
  */
uint32_t WaveRecorderStop(void)
{
  return BSP_AUDIO_IN_Stop();
}

/**
  * @brief  Update the recorded data. 
  * @param  None
  * @retval None
  */
void WaveRecorderProcess(void)
{     
  BSP_AUDIO_IN_Init(DEFAULT_AUDIO_IN_FREQ, DEFAULT_AUDIO_IN_BIT_RESOLUTION, DEFAULT_AUDIO_IN_CHANNEL_NBR);
  BSP_AUDIO_IN_Record((uint16_t*)&InternalBuffer[0], INTERNAL_BUFF_SIZE);
}

/**
  * @brief Calculates the remaining file size and new position of the pointer.
  * @param None
  * @retval None
  */
void BSP_AUDIO_IN_TransferComplete_CallBack(void)
{

  /* PDM to PCM data convert */
  BSP_LED_On(LED4);
  // convert second half of DMA buffer from PDM to PCM and store in MicrophoneInBuffer
  BSP_AUDIO_IN_PDMToPCM((uint16_t*)&InternalBuffer[INTERNAL_BUFF_SIZE/2], (uint16_t*)&MicrophoneInBuffer[0]);
  // process audio data
  Process_Out();
  BSP_LED_Off(LED4);


}

/**
  * @brief  Manages the DMA Half Transfer complete interrupt.
  * @param  None
  * @retval None
  */
void BSP_AUDIO_IN_HalfTransfer_CallBack(void)
{ 
  /* PDM to PCM data convert */

  BSP_LED_On(LED4);
  // convert first half of DMA buffer from PDM to PCM and store in MicrophoneInBuffer
  BSP_AUDIO_IN_PDMToPCM((uint16_t*)&InternalBuffer[0], (uint16_t*)&MicrophoneInBuffer[0]);
  // process audio data
  Process_Out();

  BSP_LED_Off(LED4);
  

}


void Process_Out(void){
static  uint8_t Start_stream=0;

	// spectrum analyzer, loop back audio, compute FFT, transmit FFT through serial
    for(int i=0;i<MICROPHONE_IN_FRAME_SIZE;i++){
    	data_in = MicrophoneInBuffer[i];
    	FFTInBuffer[Buffer_fft_pointer+i] = (float)data_in; // copy data to FFT buffer
    	rdata_out = data_in;
    	ldata_out = data_in;
    	AudioOutBuffer[Buffer_m_i_pointer*2+i*2]=ldata_out; // left channel no processing, to be played by DAC
    	AudioOutBuffer[Buffer_m_i_pointer*2+i*2+1]=rdata_out; // right channel no processing, to be played by DAC
    }

	Buffer_m_i_pointer += MICROPHONE_IN_FRAME_SIZE ;
    if(Buffer_m_i_pointer==AUDIO_STORAGE_BUFFER_SIZE) Buffer_m_i_pointer=0;

    Buffer_fft_pointer += MICROPHONE_IN_FRAME_SIZE;
    if(Buffer_fft_pointer==FFT_SIZE) Buffer_fft_pointer=0;

    if(Start_stream == 1 && Buffer_fft_pointer == 0) { // FFT buffer full
    	// FILL_IN_BLANK: apply window, comment out this line is equivalent to rectangular window


		// FILL_IN_BLANK: FFT forward transform


		// FFT out buffer stores 0 to FFT_SIZE/2-1 of the FFT vector, with real and imaginary parts interleaved
		// i.e., suppose the FFT of X[FFT_SIZE] is Y[FFT_SIZE], stored in FFTOutBuffer[FFT_SIZE] from the function call
	    // FFTOutBuffer[0] = Y[0].re, FFTOutBuffer[1] = Y[N/2].re, FFTOutBuffer[2] = Y[1].re, FFTOutBuffer[3] = Y[1].im, ...
		// FFTOutBuffer[FFT_SIZE-2] = Y[FFT_SIZE/2-1].re, FFTOutBuffer[SIZE_FFT-1] = Y[FFT_SIZE/2-1].im
		// recall for real signal, X[k]=X^*[(-k)_N], so the 2nd half of Y[FFT_SIZE] can be derived from the 1st half


		SerialOutBuffer[0] = 0xff; // prepare serial output buffer: set frame start

		int offset = 60; //variable noise floor offset to mask the noise, can be adjusted
		float spectrum;
		int spectrum_int;

		// extract real and imaginary parts to calculate magnitude values and convert to dB
		for (int i=0; i<FFT_SIZE; i=i+2) {
			// FILL_IN_BLANK: compute spectrum (amplitude squared) = real^2 + imaginary^2


			spectrum_int = (int)(10*log10f(spectrum))-offset; // convert to dB and cast to integer
			if (spectrum_int < 0) {
				spectrum_int = 0; // make all positive
			}
			SerialOutBuffer[i/2+1] = (uint8_t)spectrum_int;
		}

		// correct for FFT[0]
		SerialOutBuffer[1] = (uint8_t)(10*log10f(FFTOutBuffer[0]*FFTOutBuffer[0]))-offset;


		if(HAL_UART_Transmit_DMA(&UartHandle, (uint8_t*)&SerialOutBuffer, FFT_SIZE/2+1)!= HAL_OK) // start serial DMA
	    {
			Error_Handler();
	    }

   }


  
   // only start play once, transmit (to audio DAC) DMA is in circular mode, when reach end of buffer, start playing from the beginning of buffer
   if(Start_stream==0){
      // Enable I2S Out
      BSP_AUDIO_OUT_Play(AudioOutBuffer,AUDIO_STORAGE_BUFFER_SIZE*2);  // left and right channels, size of AudioOutBuffer
      Start_stream=1;
   }

}



// apply window to the data segment
void apply_window(float* signal_segment, float* window_function, uint16_t length)
{

}

