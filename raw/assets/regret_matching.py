import sys
import numpy as np
import matplotlib.pyplot as plt
from channel_gain import *


def compute_f_h(
    h: np.float64,
) -> np.float64:
    return 1/(np.power(np.abs(np.log(h)), 0.1))


def action_choice(action_set: np.ndarray, probabilities: np.ndarray) -> tuple[np.float64, int]:
    probabilities = probabilities / np.sum(probabilities)
    power = np.random.choice(action_set, p=probabilities)
    # Index of chosen power in action_set and return as integer
    index = int(np.where(action_set == power)[0][0])
    return power, index


def mse(num_devices: int, power: np.ndarray, channel_gain: np.ndarray, eta: np.float64, noise_power: np.float64) -> np.float64:
    mse = noise_power / eta
    for n in range(num_devices):
        error_value = np.sqrt(power[n]) * channel_gain[n] / np.sqrt(eta)
        mse += np.power(error_value - np.float64(1), 2)
    return mse / np.power(num_devices, 2, dtype=np.float64)


def error_function(power: np.ndarray, channel_gain: np.ndarray, n: int, eta: np.float64) -> np.float64:
	f_h = compute_f_h(channel_gain[n])
	return np.sqrt(power[n]) * f_h / np.sqrt(eta)


def device_utility(num_devices: int, power: np.ndarray, channel_gain: np.ndarray, known: int, eta: np.float64, util_const_1: np.float64, util_const_2: np.float64) -> tuple[np.float64, np.float64, np.float64]:
	known_device = error_function(power, channel_gain, known, eta)
	other_sum = np.float64(0.0)
	other_sq_sum = np.float64(0.0)

	for n in range(num_devices):
		if n != known:
			x = error_function(power, channel_gain, n, eta)
			other_sum += x
			other_sq_sum += np.power(x, 2)

	A = known_device * other_sum
	B =  (np.power(known_device, 2) * other_sq_sum)
	return (A - B), A, B


def regret_matching(
	action_set: np.ndarray,
	channel_gain: np.ndarray,
	num_devices: int,
	num_actions: int,
	epsilon: np.float64,
	eta: np.float64,
	mu: np.float64,
	noise_power: np.float64,
	util_const_1: np.float64,	
	util_const_2: np.float64,
	max_epochs: int = 10000,
	adaptive_mu_flag: bool = False,
	power_vector_init: np.ndarray = None,
	action_index_init: np.ndarray = None
):
	t = np.float64(1)
	convergence = False

	mse_list, avg_power_list, avg_utility_list = [], [], []
	utility_per_device_history: list[np.ndarray] = []
	action_index: list[np.ndarray] = []
	power_vector: list[np.ndarray] = []
	conv_ctr: dict[np.ndarray, np.float64] = dict()
	utility_lut: list[np.ndarray] = []
	util_diff_lut: list[np.ndarray] = []
	regret_lut: list[np.ndarray] = []

	psi_curr = np.zeros((num_devices, num_actions), dtype=np.float64)
	for n in range(num_devices):
		psi_curr[n,:] = np.float64(1)/np.float64(num_actions)
	psi_list: list[np.ndarray] = [psi_curr]
	if adaptive_mu_flag:
		mu_per_device = np.full((num_devices), mu, dtype=np.float64)
		mu_list = [mu_per_device.copy()]
	while not convergence:
		if power_vector_init is not None and t == 1:
			power_vector_t = power_vector_init.copy()
			action_index_t = action_index_init.copy()
		else:
			action_index_t = np.zeros((num_devices), dtype=np.int32)
			power_vector_t = np.zeros((num_devices), dtype=np.float64)
			for n in range(num_devices):
				power_vector_t[n], action_index_t[n] = action_choice(action_set, psi_curr[n,:])

		# Keep count of actions taken
		key = tuple(action_index_t.tolist())
		if key not in conv_ctr:
			conv_ctr[key] = 0.0
		conv_ctr[key] += 1.0

		temp_power_t = power_vector_t.copy()
		curr_utility = np.zeros((num_devices), dtype=np.float64)
		utility_lut_t = np.zeros((num_devices, num_actions), dtype=np.float64)
		A_list = np.zeros((num_devices), dtype=np.float64) # for deducing utility const + mu
		B_list = np.zeros((num_devices), dtype=np.float64)
		for n in range(num_devices):
			curr_utility[n], A_list[n], B_list[n] = device_utility(num_devices, power_vector_t, channel_gain, n, eta, util_const_1, util_const_2)
			for l, action in enumerate(action_set):
				temp_power_t[n] = action
				utility_lut_t[n,l], _, _ = device_utility(num_devices, temp_power_t, channel_gain, n, eta, util_const_1, util_const_2)
				temp_power_t[n] = power_vector_t[n]
		
		# print("curr_utility: ", curr_utility)
		# print("A_list: ", A_list)
		# print("B_list: ", B_list)

		psi_list_t = np.zeros((num_devices, num_actions), dtype=np.float64)
		util_diff_lut_t = np.zeros((num_devices, num_actions, num_actions), dtype=np.float64)
		regret_lut_t = np.zeros((num_devices, num_actions, num_actions), dtype=np.float64)
		if t > 1:
			util_diff_lut_t = util_diff_lut[-1].copy() * (t-np.float64(1))/t
			regret_lut_t = regret_lut[-1].copy() * (t-np.float64(1))/t
		for n in range(num_devices):
			if adaptive_mu_flag:
				mu = mu_per_device[n]
			for l in range(num_actions):
				if l != action_index_t[n]:
					if t > 1:
						prev_util = util_diff_lut[-1][n,action_index_t[n],l]
					else:
						prev_util = 0.0

					util_diff_lut_t[n,action_index_t[n],l] = ((t-np.float64(1))/t) * prev_util + (np.float64(1)/t) * (utility_lut_t[n,l] - curr_utility[n])
					regret_lut_t[n,action_index_t[n],l] = np.maximum(np.float64(0), util_diff_lut_t[n,action_index_t[n],l])
					psi_list_t[n,l] = regret_lut_t[n,action_index_t[n],l]/mu
					if psi_list_t[n,l] <= 0:
						psi_list_t[n,l] = np.float64(1e-6) # we still have a chance to explore this in the future

			chosen_action_l = action_index_t[n]
			sum_of_other_probs = np.sum(psi_list_t[n, :])
			fine_tune_mu = False
			if sum_of_other_probs > 1 and adaptive_mu_flag:
				fine_tune_mu = True
				sum_of_other_probs_fine_tune_list = []
    
			while fine_tune_mu and adaptive_mu_flag:
				sum_of_other_probs_fine_tune_list.append(sum_of_other_probs)
				mu = mu * np.float64(2.0)
				for l in range(num_actions):
					if l != action_index_t[n]:
						psi_list_t[n,l] = regret_lut_t[n,action_index_t[n],l]/mu
						if psi_list_t[n,l] <= 0:
							psi_list_t[n,l] = np.float64(1e-6) # we still have a chance to explore this in the future
				sum_of_other_probs = np.sum(psi_list_t[n, :])
				if sum_of_other_probs <= 1:
					fine_tune_mu = False
					# Plot sum_of_other_probs_fine_tune_list and mu values
			if sum_of_other_probs < 1:
				psi_list_t[n, chosen_action_l] = np.float64(1.0) - sum_of_other_probs
			if sum_of_other_probs > 1:
				print("error: sum_of_other_probs not in [0, 1]")
				print("Try to tune mu")
				print("sum_of_other: ", sum_of_other_probs)
				print("psi_list_t: ", psi_list_t[n, :])
				sys.exit()
			
			if adaptive_mu_flag:
				sum_regret = np.sum(regret_lut_t[n,action_index_t[n],:])
				if sum_regret == 0:
					mu_new = np.float64(3000) # to avoid division by zero
				else:
					mu_new = np.float64(0.01)/sum_regret

				# print("mu_new: ", mu_new)
				if mu_new > 0:
					mu = mu_new
					# if mu_new > 30000:
					# 	mu = np.float64(30000)
					# else:
					# 	mu = mu_new
				mu_per_device[n] = mu
				mu_list.append(mu_per_device.copy())
        # Calculate
		avg_power_list.append(np.mean(power_vector_t))
		mse_list.append(mse(num_devices, power_vector_t, channel_gain, eta, noise_power))
		avg_utility_list.append(np.mean(curr_utility))
		utility_per_device_history.append(curr_utility.copy())
	
		# Append the results to the lists
		power_vector.append(power_vector_t)
		action_index.append(action_index_t)
		utility_lut.append(utility_lut_t)
		util_diff_lut.append(util_diff_lut_t)
		regret_lut.append(regret_lut_t)
		psi_list.append(psi_list_t)

		# Update psi_curr
		psi_curr = psi_list_t.copy()

		if t > 1:
			conv_diff = [np.absolute((conv_ctr[p]/t) - (conv_ctr[p]/(t-1))) for p in conv_ctr.keys()]
			if t == max_epochs or np.all(conv_diff < epsilon):
				convergence = True

		t=t+1
  
	# # Plot mu evolution if adaptive_mu_flag is True for each device as list
	# if adaptive_mu_flag:
	# 	plt.figure()
	# 	for n in range(num_devices):
	# 		mu_values = [mu_list[i][n] for i in range(len(mu_list))]
	# 		plt.plot(range(len(mu_values)), mu_values, label=f'Device {n+1}')
	# 	plt.legend()
	# 	plt.xlabel('Iterations')
	# 	plt.ylabel('Mu Value')
	# 	plt.title('Evolution of Mu over Iterations')
	# 	plt.grid()
	# 	plt.savefig('mu_evolution_per_device.png')
	# 	plt.show()
	# 	plt.close()


	
	return psi_list, mse_list, avg_power_list, avg_utility_list, util_diff_lut, regret_lut, power_vector, conv_ctr, utility_per_device_history
