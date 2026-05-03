%   *****************************************************************************
%   * @file    vowel_analysis.m 
%   * @author  Dr. Chao Wang, Arizona State University, chao.wang.6@asu.edu
%   * @version V1.0.0
%   * @date    07/31/2024
%  ******************************************************************************
%   * @attention
%   *
%   * Project 2: Applications of Fast Fourier Transform 
%   *
%   * All course materials for this class are protected by copyright and
%   * may not be shared, reproduced, or uploaded to any website
%   * without the written permission of the instructor.
%   ******************************************************************************

% This script analyzes vowel sounds by plotting spectrogram/STFT, 
% time domain signal, FFT and autocorrelation function.
% It implements the algorithm to identify pitch/fundamental frequency.
% It also generates the C header files for MCU analysis.

clear all; close all;

N = 512;

% audio file name
file_name = 'a.wav';
[s0,fs0] = audioread(file_name); % stereo sound, two columns
fs0
fs = 8000;
s0 = resample(s0, fs, fs0); % resample the audio file to 8000Hz
s = (s0(:,1)+s0(:,2))/2; % average the two channels

% plot spectrogram with 50% overlap
subplot(2,2,1)
% parameters: vector to apply spectrogram on, window size (apply hamming
% window by default), num_overlap, num_fft, sampling frequency
spectrogram(s, N, 0.5*N, N, fs, 'yaxis'); % plot frequency on y axis
title('Spectrogram');

% extract N samples in the middle of the file (where the sound is likely to be stable)
mid = floor(length(s)/2); 
start_index = mid-N/2;
x = s(start_index:start_index+N-1)';

% save data to header file for use in c program, note you need to change 
% the file and variable names for a different vowel
fid = fopen('vowel_a.h','w');
fprintf(fid,'float vowel_a[512] = {\n');
fprintf(fid,'%f,\n',x);
fprintf(fid,'};\n');
fclose(fid);

% display time domain voice samples
subplot(2,2,2)
plot(x)
xlabel('Samples')
ylabel('Amplitude')
title('Samples for the Vowel')

% take FFT on the samples
y = fft(x,N);
f = fs*linspace(0,1, N) - fs/2; % generate frequency vector
spectrum = abs(y).^2 % magnitude^2 of fft

% plot double-sided spectrum
subplot(2,2,3)
plot(f,fftshift(spectrum)); 
xlabel('Frequency (Hz)')
ylabel('Amplitude Squared')
title('FFT')

% calculate auto-correlation function, which is inverse transform of power spectrum
auto_corr = ifft(spectrum,N)
auto_corr = auto_corr(1:N/2); % real and symmetric, only keep the 1st half
subplot(2,2,4)
plot(auto_corr)
xlabel('Samples')
ylabel('Amplitude')
title('Autocorrelation Function')

% find all peaks of the autocorrelation function
peaks = zeros(N/2, 1);
peaks_index = zeros(N/2, 1);
num_peaks = 0;
direction = 0; % 0 is going up, 1 is going down
for i = 2 : length(auto_corr)
    % going up before, but now going down, then it is a peak
    if auto_corr(i) < auto_corr(i-1) && direction == 0
        num_peaks = num_peaks + 1;
        peaks(num_peaks) = auto_corr(i-1);
        peaks_index(num_peaks) = i-1;
        direction = 1; 
    elseif auto_corr(i) > auto_corr(i-1) && direction == 1
        direction = 0;
    end
end

if direction == 0
    % count last element in the array as a peak
    num_peaks = num_peaks + 1;
    peaks(num_peaks) = auto_corr(length(auto_corr));
    peaks_index(num_peaks) = length(auto_corr);  
end

% % for debugging 
% peaks(1:num_peaks)
% peaks_index(1:num_peaks)
% num_peaks

% search for the highest peak of the auto correlation function
% ignore self correlation, which is the first element auto_corr(1), 
% if it is a peak
if peaks_index(1) == 1
    % search max peak from index 2 of peaks array, ignore self correlation peak (index 1)
    index_offset = 1;
else
    % search max peak from index 1 of peaks array
    index_offset = 0;
end

% max_index function, find max value and its index in an array
max_num = peaks(1+index_offset); % keep track of max value in the array
max_peak_index = 1 + index_offset; % keep track of max value index in the array
start_index = 2 + index_offset;
for i = start_index : num_peaks
    if peaks(i) > max_num
        max_num = peaks(i);
        max_peak_index = i;
    end
end

max_index = peaks_index(max_peak_index)

pitch = 1/((max_index-1)/fs); % convert to Hz
str = sprintf('Estimated pitch is at index %d (starting from 0) with frequency at %f Hz.', max_index-1, pitch);
disp(str)





