# Pixelator-View
Program code (Python) for Pixelator View as explained in the paper, "[SoCodeCNN: Program Source Code for Visual CNN Classification Using Computer Vision Methodology](https://ieeexplore.ieee.org/document/8882216)", published in IEEE Access (2019).

This program (**Pixelator View**) finds the differences between two images, where the minute differences are not being able to be picked up by classic image difference monitoring approaches such as SSIM map, MSE, Quality of Image, etc.

## Requirements

The Pixelator View requires ***matplotlib*** and ***sklearn*** libraries in Python programmaing language.

## Usage

Let's assume you have two image files to compare using Pixelator View and the names of the files are as follows: MySmallImg.png and MyBigImg.png, where MySmallImg.png represents the image file with smaller dimensions and MyBigImg.png represents the image file with larger dimensions compared between the two.

Then, copy the program named ***pixelator.py*** from this repository and in your command prompt use the following command:

      $python pixelator.py MySmallImg.png MyBigImg.png

## Example

![image](https://user-images.githubusercontent.com/8515608/67832082-6b349980-fad8-11e9-86da-868e6e05e8e0.jpg)

**Lena standard image (lena_std.jpg)**

![image](https://user-images.githubusercontent.com/8515608/67832086-6e2f8a00-fad8-11e9-9e2b-f3177bf31121.jpg)

**Lena blurred image (lena_blurred.jpg)**

      $python pixelator.py lena_std.jpg lena_blurred.jpg

#### Output

![image](https://user-images.githubusercontent.com/8515608/67832094-71c31100-fad8-11e9-9434-aed69c4e25a8.png)

----------------------------------------------------------------------------

## Citation
***
***Dey, Somdip, Amit Kumar Singh, Dilip Kumar Prasad, and Klaus McDonald-Maier. "[SoCodeCNN: Program Source Code for Visual CNN Classification Using Computer Vision Methodology](https://ieeexplore.ieee.org/document/8882216)." IEEE Access (2019).***
***

