# qrcode_generator
CS633 week 2 Assignment
A simple Python application that generates QR codes from user-provided URLs and displays them.

# Author 
Fuyuki Kobayashi

## Features
- Generates QR codes from any valid URL
- Visual display of the generated QR code
- User-friendly command-line interface

## Requirements
- Python 3.6 or higher
- qrcode
- matplotlib
- Pillow (dependency of qrcode)

## Installation
Clone the repository or download the script

Install the required packages:
```pip install qrcode matplotlib```

## Usage
Run the script from the command line:
```python qr_code_generator.py```
Follow the prompts to enter your URL. The program will generate a QR code and display it in a new window.

## Example
```
###############################
##### QR code generator #######
Please enter the URL to generate a QR code => bioxsystems.com
```
After entering the URL, a matplotlib window will open displaying your QR code.

![QR Code Generator](https://github.com/sakufuyu/qrcode_generator/blob/main/pics/qrcode.png?raw=true)

## Customization
You can modify the QR code parameters in the generate_qrcode function:
- version: Controls the size of the QR code (1-40)
- error_correction: Error correction level (L, M, Q, H)
- box_size: Size of each box in the QR code
- border: Size of the border around the QR code
- fill_color: Color of the QR code elements
- back_color: Background color