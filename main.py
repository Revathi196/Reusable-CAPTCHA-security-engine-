from captcha_engine import CAPTCHA

def main():
    print("Welcome to the CAPTCHA Generator and Validator!")
    
    captcha = CAPTCHA()

    # Generate CAPTCHA and save image
    print("Generating CAPTCHA...")
    captcha.create_image()
    captcha.save_image("captcha_image.png")
    print("CAPTCHA image saved as 'captcha_image.png'.")

    # Ask user to solve the CAPTCHA
    print("\nPlease solve the CAPTCHA by entering the text shown in the image.")
    user_input = input("Enter the CAPTCHA: ")

    # Validate the user's answer
    if captcha.validate_answer(user_input):
        print("CAPTCHA validated successfully!")
    else:
        print("Invalid CAPTCHA. Please try again.")

if __name__ == "__main__":
    main()
