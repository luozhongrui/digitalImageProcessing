# EEEN4/60161 Digital Image Processing LABORATORY 3 (2022/23)

**Objectives:** 

• Understand and practise frequency-domain image processing 

• Understand block-based image processing and DCT-based image coding 


## Introduction

Spatial frequency is an important concept in image processing and vision. Frequency-domain image processing involves 2D Discrete Fourier Transforms (DFT) and filtering images in the frequency domain. In first part of this laboratory you will first practise 2D DFT (forward and inverse) and appreciate the meaning of spatial frequencies, before practise lowpass and highpass filtering in the frequency-domain.

Block-based coding may not be the best way to code image data but it is simple, relatively easy to implement. For these reasons it is widely used in existing and commercial image codecs. In the second part of this laboratory you will explore the properties of block-based processing, especially the Discrete Cosine Transformation (DCT) that is widely used in image coding. The DCT is a reversible transformation, that is, the transformed can be reversed to provide an exact replica of the input image. For efficient coding we abandon the requirement that the input be transmitted exactly and seek only a good approximation to the input. This process is known as lossy coding. In this lab the image quality will be evaluated for representations using different numbers of DCT coefficients.
