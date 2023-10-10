%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 1.2 Forward and inverse 2D DFT                                          %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% part 1                                                                  % 
% Recreate the example of 2D DFT in page 5 of the lecture handouts.       %
% First generate an image of a small white rectangle in black background  %
% with the code given. Display the image. Then perform 2D DFT and display %
% the magnitude spectrum.                                                 %
% Centre the spectrum, and display in logarithm scale.                    %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear;
close all;
clc;
x=zeros(512,512);
for i=1:20
   for j=1:40
      x(256-10+i,256-20+j)=255;
   end 
end
% display the image
figure; imshow(x);
% simple 2D DFT
figure; y=fft2(x);
% display the DFT magnitude image
imshow(abs(y)/max(max(abs(y))));
% display shifted DFT magnitude image
figure; y=fftshift(fft2(x));
imshow(abs(y)/max(max(abs(y))));
% display log magnitude (shifted) DFT magnitude iamge
figure; imshow(log(abs(y)),[]); colormap(gray);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% part 2                                                                  %
% Load a real image (e.g. [I,map]=imread('lena_gray.png');)               %
% Then display the image (e.g. imshow(I, map);).                          %
% Perform 2D DFT on the grey level image (e.g. after, X=ind2gray(I,map))  %
% and display the magnitude spectrum.                                     %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
close all;
clear;
clc;
% Load the grayscale image
[I, map] = imread('image/lena_gray.png');

% Convert indexed image to grayscale
X = ind2gray(I, map);

% Display the original grayscale image
figure;
imshow(X);
title('Original Grayscale Image');

% Perform 2D DFT
F = fft2(X);

% Compute the magnitude spectrum
magnitude_spectrum = abs(F);

% Display the magnitude spectrum
figure;
imshow(log(1 + magnitude_spectrum), []);
title('Magnitude Spectrum (log scale)');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% part 3                                                                  %
% Now apply the inverse 2D DFT (Matlab: ifft2) on the raw spectrum        %
% and display the result.                                                 %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Apply inverse 2D DFT
restored_image = ifft2(F);

% Display the restored image
figure;
imshow(abs(restored_image), []);
title('Restored Image from Inverse DFT');

% Check if the restored image is the same as the original image
if isequal(round(abs(restored_image)), X)
    disp('Restored image is the same as the original image.');
else
    disp('Restored image is different from the original image.');
end
