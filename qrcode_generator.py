"""
QR code generator

This script generates a QR code from a user-provided URL 
and displays it using matplotlib.
"""

import qrcode
import matplotlib.pyplot as plt


def generate_qrcode(url: str) -> "Image":
    """
    Generate a QR code image from a given URL.

    Args:
        url (str): The URL to encode in the QR code.

    Returns:
        Image: The generated QR code image object.
    """

    # Generate QR code with specified parameters
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generate image of QR code
    img = qr.make_image(fill_color="black", back_color="white")

    return img


def display_qrcode(img: "Image") -> None:
    """
    Display the generated QR code image using matplotlib.

    Args:
        img (Image): The QR code image to display.
    """

    plt.imshow(img)
    plt.axis("off")
    # plt.title(f"QR code for: {url}")
    plt.show()


def get_user_input() -> str:
    """
    Prompt the user for a URL and validate the input.

    Returns:
        str: The validated URL provided by the user.
    """

    is_valid_url = False
    print("###############################")
    print("##### QR code generator #######")

    while (not is_valid_url):
        url = input("Please enter the URL to generate a QR code => ")

        if (url is None or url.strip() == ""):
            print("Error: URL cannot be empty. Please try again.")
            continue
        else:
            is_valid_url = True

    return url


def main() -> None:
    """
    Main function to orchestrate the QR code generation process.
    """

    url = get_user_input()
    img = generate_qrcode(url)
    display_qrcode(img)


if __name__ == "__main__":
    main()
