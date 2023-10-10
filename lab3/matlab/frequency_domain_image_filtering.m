%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%1.3 Frequency-domain image filtering                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% part 1                                                                  %
% Based on the definitions (formulae) on the lecture notes (section 8.4), %
% generate the ideal and Butterworth or Gaussian filters,                 %
% respectively, with the cut-off frequency D0 set to 40.                  %
% Plot the generated filters (i.e. their frequency response).             %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[X, map] = imread('image/lena_gray.png');
X = ind2gray(X, map);
figure;
imshow(X);
title('orignal image');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generating an ideal low-pass filter                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Define the size of the filter (should be same as the size of the image)
[M, N] = size(X);

% Set the cut-off frequency D0
D0 = 40;

% Create a meshgrid for the frequency domain
[u, v] = meshgrid(1:N, 1:M);

% Compute the distance from the center of the frequency domain
D = sqrt((u - N/2).^2 + (v - M/2).^2);

% Create the ideal lowpass filter
H_ideal = double(D <= D0);

% Display the ideal lowpass filter
figure;
imshow(H_ideal, []);
title('Ideal Lowpass Filter');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generating a Butterworth low-pass filter                                %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Define the order of the Butterworth filter
n = 2; % You can adjust the order as needed

% Create the Butterworth lowpass filter
H_butterworth = 1 ./ (1 + (D ./ D0).^(2*n));

% Display the Butterworth lowpass filter
figure;
imshow(H_butterworth, []);
title('Butterworth Lowpass Filter');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate Gaussian low-pass filter                                       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Create the Gaussian lowpass filter
H_gaussian = exp(-(D.^2) / (2 * (D0^2)));

% Display the Gaussian lowpass filter
figure;
imshow(H_gaussian, []);
title('Gaussian Lowpass Filter');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% part 2                                                                  %
% Apply these filters to the Lena image in the frequency domain,          %
% respectively. That is, multiply the spectrum of the image with          %
% the filter s frequency esponses (element by element) and apply          %
% inverse 2D DFT. Display these filtered images (inverse of the           %
% multiplied spectrum), respectively.                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute the FFT of the Lena image
F = fft2(X);

% Apply frequency domain filters element-wise multiplication

% Ideal Lowpass Filter
F_ideal_filtered = F .* H_ideal;

% Butterworth Lowpass Filter
F_butterworth_filtered = F .* H_butterworth;

% Gaussian Lowpass Filter
F_gaussian_filtered = F .* H_gaussian;

% Apply inverse 2D DFT to obtain filtered images

% Ideal Lowpass Filtered Image
restored_ideal = ifft2(F_ideal_filtered);

% Butterworth Lowpass Filtered Image
restored_butterworth = ifft2(F_butterworth_filtered);

% Gaussian Lowpass Filtered Image
restored_gaussian = ifft2(F_gaussian_filtered);

% Display the filtered images

% Display Ideal Lowpass Filtered Image
figure;
imshow(abs(restored_ideal), []);
title('Image Filtered with Ideal Lowpass Filter');

% Display Butterworth Lowpass Filtered Image
figure;
imshow(abs(restored_butterworth), []);
title('Image Filtered with Butterworth Lowpass Filter');

% Display Gaussian Lowpass Filtered Image
figure;
imshow(abs(restored_gaussian), []);
title('Image Filtered with Gaussian Lowpass Filter');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% part 3                                                                  %
% Convert these filters to high-pass filters (using the same D0).         %
% Refer to page 20 for the definitions of these filters.                  %
% Then apply them to the Lena image (in the frequency domain).            %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Compute the inverse of low-pass filters to get high-pass filters

% Ideal Highpass Filter
H_ideal_highpass = 1 - H_ideal;

% Butterworth Highpass Filter
H_butterworth_highpass = 1 - H_butterworth;

% Gaussian Highpass Filter
H_gaussian_highpass = 1 - H_gaussian;

% Apply high-pass filters in the frequency domain

% Ideal Highpass Filtered Image
F_ideal_highpass_filtered = F .* H_ideal_highpass;
restored_ideal_highpass = ifft2(F_ideal_highpass_filtered);

% Butterworth Highpass Filtered Image
F_butterworth_highpass_filtered = F .* H_butterworth_highpass;
restored_butterworth_highpass = ifft2(F_butterworth_highpass_filtered);

% Gaussian Highpass Filtered Image
F_gaussian_highpass_filtered = F .* H_gaussian_highpass;
restored_gaussian_highpass = ifft2(F_gaussian_highpass_filtered);

% Display the high-pass filtered images

% Display Ideal Highpass Filtered Image
figure;
imshow(abs(restored_ideal_highpass), []);
title('Image Filtered with Ideal Highpass Filter');

% Display Butterworth Highpass Filtered Image
figure;
imshow(abs(restored_butterworth_highpass), []);
title('Image Filtered with Butterworth Highpass Filter');

% Display Gaussian Highpass Filtered Image
figure;
imshow(abs(restored_gaussian_highpass), []);
title('Image Filtered with Gaussian Highpass Filter');

