%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 1.1 Spatial frequencies                                                 %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear;
close all;
clc;
n=1:128;
x=sin(2*pi*n./16); % i.e. f=fs/16; format: 2*pi*f*n/fs figure();plot(x);
% Apply (1D) DFT (Matlab function: fft) to the signal and display the magnitude spectrum:
y=fft(x); %do a 128-point DFT
figure(); plot(abs(y)); % magnitude spectrum, uncentred, 0(DC) to fs % You can centre the spectrum, so spectrum is from -fs/2 to fs/2, with dc at the middle point:
figure();plot(abs(fftshift(fft(x))));
for i=1:128
          X(i,:)=x;
end
figure();
imshow(X);
Y = fft2(X);
figure(); plot(abs(Y));
figure();plot(abs(fftshift(Y)));

