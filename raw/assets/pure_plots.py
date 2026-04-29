import numpy as np
import matplotlib.pyplot as plt
import time
import os
import pandas as pd

from channel_gain import get_channel_gain
from regret_matching import regret_matching
import constants as const


# Create a timestamp directory
time_stamp_str = str(time.strftime("%Y%m%d-%H%M%S"))
current_directory = os.getcwd()
timestamp_dir = os.path.join(current_directory, "results/pure", time_stamp_str)
os.makedirs(timestamp_dir, exist_ok=True)


num_devices = const.num_devices
num_actions = const.num_actions
epsilon =const.epsilon
eta=const.eta
mu=np.float64(500)
noise_power=const.noise_power
power_max = const.power_max
util_const_1 = const.util_const_1
util_const_2 = const.util_const_2
max_epochs = const.max_epochs

action_set = np.linspace(power_max/num_actions, power_max, num_actions, dtype=np.float64)


# Constructing network architecture
bs_position = const.bs_position
f_c = const.f_c
d_max = const.d_max
x_pos = np.linspace(d_max / num_devices, d_max, num_devices, dtype=np.float64)
user_positions = [(x, 0.0, 0.0) for x in x_pos]
channel_gain = np.array([get_channel_gain(user_pos, bs_position, f_c) for user_pos in user_positions])


# Running regret matching
start_time = time.time()
psi_list, mse_list, avg_power_list, avg_utility_list, util_diff_lut, regret_lut, power_vector, conv_ctr, utility_per_device_history = regret_matching(
    action_set, channel_gain, num_devices, num_actions, epsilon, eta, mu, noise_power, util_const_1, util_const_2, max_epochs
)
stop_time = time.time()

computation_time_per_device = (stop_time - start_time) / num_devices
regret_tensor = np.stack(regret_lut)
total_regret_per_device = regret_tensor.sum(axis=(2, 3))


# Plot MSE vs t
plt.figure()
plt.plot(mse_list)
plt.xlabel('Epoch')
plt.ylabel('MSE')
plt.title('MSE vs Epoch')
plt.savefig(os.path.join(timestamp_dir, f'mse_{num_devices}.png'))
# plt.show()
plt.close()

# Plot Utility per device vs t
utility_per_device_history = np.vstack(utility_per_device_history)
power_vector = np.vstack(power_vector)
plt.figure()
for device_idx in range(num_devices):
    plt.plot(utility_per_device_history[:, device_idx], label=f'Device {device_idx}')
plt.xlabel('Epoch')
plt.ylabel('Utility per device')
plt.title('Utility per device vs Epoch')
plt.legend()
plt.savefig(os.path.join(timestamp_dir, f'utility_per_device_{num_devices}.png'))
# plt.show()
plt.close()

# Plot average utility vs t
plt.figure()
plt.plot(avg_utility_list)
plt.xlabel('Epoch')
plt.ylabel('Average Utility')
plt.title('Average Utility vs Epoch')
plt.savefig(os.path.join(timestamp_dir, f'avg_utility_{num_devices}.png'))
# plt.show()
plt.close()

# Plot total regret per device vs t
plt.figure()
for device_idx in range(num_devices):
    plt.plot(total_regret_per_device[:, device_idx], label=f'Device {device_idx}')
plt.xlabel('Epoch')
plt.ylabel('Total Regret per device')
plt.title('Per-Device Total Regret vs Epoch')
plt.legend()
plt.savefig(os.path.join(timestamp_dir, f'total_regret_per_device_{num_devices}.png'))
# plt.show()
plt.close()

# Plot average regret vs t
plt.figure()
plt.plot(np.mean(total_regret_per_device, axis=1))
plt.xlabel('Epoch')
plt.ylabel('Average Regret')
plt.title('Average Regret vs Epoch')
plt.savefig(os.path.join(timestamp_dir, f'avg_regret_{num_devices}.png'))
# plt.show()
plt.close()

# Plot Power per device vs t
plt.figure()
for device_idx in range(num_devices):
    plt.plot(power_vector[:, device_idx], label=f'Device {device_idx}')
plt.xlabel('Epoch')
plt.ylabel('Power per device')
plt.title('Power vs Epoch')
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(timestamp_dir, f'power_per_device_{num_devices}.png'))
# plt.show()
plt.close()

# Plot average power vs t
plt.figure()
plt.plot(np.mean(power_vector, axis=1))
plt.xlabel('Epoch')
plt.ylabel('Average Power')
plt.title('Average Power vs Epoch')
plt.savefig(os.path.join(timestamp_dir, f'avg_power_{num_devices}.png'))
# plt.show()
plt.close()

# Save results to CSV
data_dict = {'mse_list': mse_list}
# Add columns for each device
for device_idx in range(num_devices):
    data_dict[f'total_regret_device_{device_idx}'] = total_regret_per_device[:, device_idx]
    data_dict[f'power_device_{device_idx}'] = power_vector[:, device_idx]
    data_dict[f'utility_device_{device_idx}'] = utility_per_device_history[:, device_idx]

df = pd.DataFrame(data_dict)
df.to_csv(os.path.join(timestamp_dir, f"{time_stamp_str}_{num_devices}_devices.csv"), index=False)


