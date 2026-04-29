% /**
%  ******************************************************************************
%   * @file    gen_sin_f.m
%   * @author  Dr. Chao Wang, Arizona State University, chao.wang.6@asu.edu
%   * @version V1.0.0
%   * @date    07/31/2024
%  ******************************************************************************
%   * @attention
%   *
%   * Lab 7: Fast Fourier Transform
%   *
%   * All course materials for this class are protected by copyright and
%   * may not be shared, reproduced, or uploaded to any website
%   * without the written permission of the instructor.
%   ******************************************************************************
%  */


fs=8192;
fin = 256; 
duration=1/60;
sec = 60*duration;
n=0:1/fs:sec;
x=sin(2*pi*fin*n);

% write to file
fid = fopen('sine_table.h','w');

fprintf(fid,'float sin_f[128] = {\n');
fprintf(fid,'%f,\n',x(1:128));
fprintf(fid,'};\n');

fclose(fid);

% compute and plot fft
close all;
N = 128;
y = fft(x(1:N), N);
spectrum = abs(y).^2
plot(1:N, spectrum)
