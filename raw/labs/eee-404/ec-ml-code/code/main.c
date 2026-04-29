/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "embeddedML.h"
#include <stdlib.h>
/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
#define N_EPOCH   2000
#define N_REPORT  200
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
float net_error_epoch;
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void generate_xorand(float *x, float *y, int i) {
	int k;

	k = rand() % 8;

	switch (k) {
	case 0:
		x[0] = 0.0;
		x[1] = 0.0;
		x[2] = 0.0;
		y[0] = 0.0;
		y[1] = 0.0;
		break;
	case 1:
		x[0] = 0.0;
		x[1] = 0.0;
		x[2] = 1.0;
		y[0] = 0.0;
		y[1] = 0.0;
		break;
	case 2:
		x[0] = 0.0;
		x[1] = 1.0;
		x[2] = 0.0;
		y[0] = 1.0;
		y[1] = 0.0;
		break;
	case 3:
		x[0] = 0.0;
		x[1] = 1.0;
		x[2] = 1.0;
		y[0] = 1.0;
		y[1] = 1.0;
		break;
	case 4:
		x[0] = 1.0;
		x[1] = 0.0;
		x[2] = 0.0;
		y[0] = 1.0;
		y[1] = 0.0;
		break;
	case 5:
		x[0] = 1.0;
		x[1] = 0.0;
		x[2] = 1.0;
		y[0] = 1.0;
		y[1] = 0.0;
		break;
	case 6:
		x[0] = 1.0;
		x[1] = 1.0;
		x[2] = 0.0;
		y[0] = 0.0;
		y[1] = 0.0;
		break;
	case 7:
		x[0] = 1.0;
		x[1] = 1.0;
		x[2] = 1.0;
		y[0] = 0.0;
		y[1] = 1.0;
		break;
	default:
		x[0] = 0.0;
		x[1] = 0.0;
		x[2] = 0.0;
		y[0] = 0.0;
		y[1] = 0.0;
		break;
	}

	/*
	 * The XOR-AND system supplies three input values and
	 * two Ground Truth output values.
	 *
	 * Since the neural network has 6 neurons in the output layer, the
	 * remaining four Ground Truth values are set to zero.
	 *
	 */

	y[2] = 0.0;
	y[3] = 0.0;
	y[4] = 0.0;
	y[5] = 0.0;
}



void Output_Error(int size, ANN *net, float * ground_truth, float *error) {

	int i;
	/*
	 * Compute error as mean squared difference between
	 * output and Ground Truth
	 */

	*error = 0;
	for (i = 0; i < size; i++) {
		*error = *error
				+ (net->output[i] - ground_truth[i]) * (net->output[i] - ground_truth[i]);
	}
	*error = *error / size;

}
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  /* USER CODE BEGIN 2 */

  //---EMBEDDED ANN---
	unsigned int i;

	unsigned int network_topology[3] = { 3, 9, 6 }; // input, hidden and output layer neurons

	float weights_initial[81] = { 0.680700, 0.324900, 0.607300, 0.365800, 0.693000,
			0.527200, 0.754400, 0.287800, 0.592300, 0.570900, 0.644000,
			0.416500, 0.249200, 0.704200, 0.598700, 0.250300, 0.632700,
			0.372900, 0.684000, 0.661200, 0.230300, 0.516900, 0.770900,
			0.315700, 0.756000, 0.293300, 0.509900, 0.627800, 0.781600,
			0.733500, 0.509700, 0.382600, 0.551200, 0.326700, 0.781000,
			0.563300, 0.297900, 0.714900, 0.257900, 0.682100, 0.596700,
			0.467200, 0.339300, 0.533600, 0.548500, 0.374500, 0.722800,
			0.209100, 0.619400, 0.635700, 0.300100, 0.715300, 0.670800,
			0.794400, 0.766800, 0.349000, 0.412400, 0.619600, 0.353000,
			0.690300, 0.772200, 0.666600, 0.254900, 0.402400, 0.780100,
			0.285300, 0.697700, 0.540800, 0.222800, 0.693300, 0.229800,
			0.698100, 0.463500, 0.201300, 0.786500, 0.581400, 0.706300,
			0.653600, 0.542500, 0.766900, 0.411500 };

	float weights[81];
	float dedw[81]; // weight derivatives
	float bias[15];
	float output[6]; // NN output

	/*
	 * Initialize weight, output, and bias values
	 */
	for (i = 0; i < 15; i++){
		bias[i] = 0.5; // initial biases
	}
	for (i = 0; i < 6; i++){
		output[i] = 0.0;
	}
	for (i = 0; i < 81; i++){
		weights[i] = weights_initial[i]; // initial weights
		dedw[i] = 0.0;
	}

	/*
	 * Initialize neural network data structure
	 */
	ANN net;
	net.weights = weights;
	net.dedw = dedw;
	net.bias = bias;
	net.topology = network_topology;
	net.n_layers = 3;
	net.n_weights = 81;
	net.n_bias = 15;
	net.output = output;

	//OPTIONS
	net.eta = 0.05;     //Learning Rate
	net.beta = 0.01;    //Bias Learning Rate
	net.alpha = 0.25;   //Momentum Coefficient
	net.output_activation_function = &relu; // Rectified linear unit
	net.hidden_activation_function = &relu;

	/*
	 * Initialize neural network
	 */

	init_ann(&net);

	//---------------------
	// For training:
	float x[3];  // training input
	float y[6]; // training ground truth output values

	/* For testing:
	 * Input Values corresponding to output Ground Truth values
	 * The neural network includes 3 input neurons
	 *
	 */
									  // x1 XOR x2, x2 AND x3
	float x0[3] = { 0.0, 0.0, 0.0 };  // Corresponds to output 0 0
	float x1[3] = { 0.0, 0.0, 1.0 };  // Corresponds to output 0 0
	float x2[3] = { 0.0, 1.0, 0.0 };  // Corresponds to output 1 0
	float x3[3] = { 0.0, 1.0, 1.0 };  // Corresponds to output 1 1
	float x4[3] = { 1.0, 0.0, 0.0 };  // Corresponds to output 1 0
	float x5[3] = { 1.0, 0.0, 1.0 };  // Corresponds to output 1 0
	float x6[3] = { 1.0, 1.0, 0.0 };  // Corresponds to output 0 0
	float x7[3] = { 1.0, 1.0, 1.0 };  // Corresponds to output 0 1
	float ground_truth[2]; // define ground truth for each input combination
	float error, net_error; // testing errors


		/*
		 * Initiate train and test cycles
		 */

		for (i = 0; i < N_EPOCH; i++) {

			/*
			 * Compute input and output ground truth
			 */

			generate_xorand(x, y, i); // a random input/output combination

			/*
			 * Train network on input and ground truth
			 */

			train_ann(&net, x, y);

			/*
			 * After completion of a number of epochs, N_REPORT
			 * perform neural network test execution, calculate output error
			 */

			if (i % N_REPORT == 0 || i == 0) {

				net_error = 0; // clear error

				/*
				 * Execute trained network and compute Output Error
				 * with Ground Truth supplied in ground_truth array
				 */

				run_ann(&net, x0);
				ground_truth[0] = 0.0;
				ground_truth[1] = 0.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x1);
				ground_truth[0] = 0.0;
				ground_truth[1] = 0.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x2);
				ground_truth[0] = 1.0;
				ground_truth[1] = 0.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x3);
				ground_truth[0] = 1.0;
				ground_truth[1] = 1.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x4);
				ground_truth[0] = 1.0;
				ground_truth[1] = 0.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x5);
				ground_truth[0] = 1.0;
				ground_truth[1] = 0.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x6);
				ground_truth[0] = 0.0;
				ground_truth[1] = 0.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				run_ann(&net, x7);
				ground_truth[0] = 0.0;
				ground_truth[1] = 1.0;
				Output_Error(2, &net, ground_truth, &error);
				net_error = net_error + error;

				net_error_epoch = net_error; // total error for all possible input combinations

			}
		}


  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  while (1)
  {
    /* USER CODE END WHILE */

    /* USER CODE BEGIN 3 */
  }
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};

  /** Configure the main internal regulator output voltage
  */
  __HAL_RCC_PWR_CLK_ENABLE();
  __HAL_PWR_VOLTAGESCALING_CONFIG(PWR_REGULATOR_VOLTAGE_SCALE1);
  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLM = 4;
  RCC_OscInitStruct.PLL.PLLN = 168;
  RCC_OscInitStruct.PLL.PLLP = RCC_PLLP_DIV2;
  RCC_OscInitStruct.PLL.PLLQ = 7;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV4;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV2;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_5) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{
  GPIO_InitTypeDef GPIO_InitStruct = {0};

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOE_CLK_ENABLE();
  __HAL_RCC_GPIOC_CLK_ENABLE();
  __HAL_RCC_GPIOH_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();
  __HAL_RCC_GPIOB_CLK_ENABLE();
  __HAL_RCC_GPIOD_CLK_ENABLE();

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(CS_I2C_SPI_GPIO_Port, CS_I2C_SPI_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(OTG_FS_PowerSwitchOn_GPIO_Port, OTG_FS_PowerSwitchOn_Pin, GPIO_PIN_SET);

  /*Configure GPIO pin Output Level */
  HAL_GPIO_WritePin(GPIOD, LD4_Pin|LD3_Pin|LD5_Pin|LD6_Pin
                          |Audio_RST_Pin, GPIO_PIN_RESET);

  /*Configure GPIO pin : CS_I2C_SPI_Pin */
  GPIO_InitStruct.Pin = CS_I2C_SPI_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(CS_I2C_SPI_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : OTG_FS_PowerSwitchOn_Pin */
  GPIO_InitStruct.Pin = OTG_FS_PowerSwitchOn_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(OTG_FS_PowerSwitchOn_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : PDM_OUT_Pin */
  GPIO_InitStruct.Pin = PDM_OUT_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF5_SPI2;
  HAL_GPIO_Init(PDM_OUT_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : B1_Pin */
  GPIO_InitStruct.Pin = B1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_IT_RISING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(B1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : I2S3_WS_Pin */
  GPIO_InitStruct.Pin = I2S3_WS_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF6_SPI3;
  HAL_GPIO_Init(I2S3_WS_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : SPI1_SCK_Pin SPI1_MISO_Pin SPI1_MOSI_Pin */
  GPIO_InitStruct.Pin = SPI1_SCK_Pin|SPI1_MISO_Pin|SPI1_MOSI_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF5_SPI1;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pin : BOOT1_Pin */
  GPIO_InitStruct.Pin = BOOT1_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(BOOT1_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pin : CLK_IN_Pin */
  GPIO_InitStruct.Pin = CLK_IN_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF5_SPI2;
  HAL_GPIO_Init(CLK_IN_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : LD4_Pin LD3_Pin LD5_Pin LD6_Pin
                           Audio_RST_Pin */
  GPIO_InitStruct.Pin = LD4_Pin|LD3_Pin|LD5_Pin|LD6_Pin
                          |Audio_RST_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  HAL_GPIO_Init(GPIOD, &GPIO_InitStruct);

  /*Configure GPIO pins : I2S3_MCK_Pin I2S3_SCK_Pin I2S3_SD_Pin */
  GPIO_InitStruct.Pin = I2S3_MCK_Pin|I2S3_SCK_Pin|I2S3_SD_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF6_SPI3;
  HAL_GPIO_Init(GPIOC, &GPIO_InitStruct);

  /*Configure GPIO pin : VBUS_FS_Pin */
  GPIO_InitStruct.Pin = VBUS_FS_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(VBUS_FS_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : OTG_FS_ID_Pin OTG_FS_DM_Pin OTG_FS_DP_Pin */
  GPIO_InitStruct.Pin = OTG_FS_ID_Pin|OTG_FS_DM_Pin|OTG_FS_DP_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF10_OTG_FS;
  HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

  /*Configure GPIO pin : OTG_FS_OverCurrent_Pin */
  GPIO_InitStruct.Pin = OTG_FS_OverCurrent_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(OTG_FS_OverCurrent_GPIO_Port, &GPIO_InitStruct);

  /*Configure GPIO pins : Audio_SCL_Pin Audio_SDA_Pin */
  GPIO_InitStruct.Pin = Audio_SCL_Pin|Audio_SDA_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_AF_OD;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
  GPIO_InitStruct.Alternate = GPIO_AF4_I2C1;
  HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

  /*Configure GPIO pin : MEMS_INT2_Pin */
  GPIO_InitStruct.Pin = MEMS_INT2_Pin;
  GPIO_InitStruct.Mode = GPIO_MODE_EVT_RISING;
  GPIO_InitStruct.Pull = GPIO_NOPULL;
  HAL_GPIO_Init(MEMS_INT2_GPIO_Port, &GPIO_InitStruct);

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
