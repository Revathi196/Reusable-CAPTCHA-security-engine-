# Reusable CAPTCHA Security Engine

This project provides a simple, reusable **CAPTCHA security engine** that can generate CAPTCHA images and validate user inputs. The CAPTCHA system is designed to protect forms or login systems from automated bots by generating random alphanumeric text in an image with added noise.

## Features

- **CAPTCHA Generation**: Generate random alphanumeric CAPTCHA text and display it as an image.
- **Image with Noise**: The CAPTCHA image includes random lines and points for added complexity, making it harder for bots to read.
- **Answer Validation**: Users are asked to input the text displayed in the CAPTCHA image, and their input is validated against the generated text.
- **Customizable**: Modify parameters such as CAPTCHA text length, image dimensions, font size, and noise level.

## Files in the Repository

### 1. `captcha_engine.py`

This file contains the core logic for generating and validating CAPTCHA images:

- **`CAPTCHA` class**: 
  - **`generate_random_text()`**: Generates random text made of letters (uppercase and lowercase) and digits.
  - **`create_image()`**: Creates a CAPTCHA image using the generated text with added noise.
  - **`save_image(filename)`**: Saves the generated CAPTCHA image to a file.
  - **`validate_answer(user_input)`**: Validates the user’s input against the generated CAPTCHA text.

### 2. `main.py`

This is the main script where the user interacts with the system:
- **Generate CAPTCHA**: Creates a CAPTCHA image and saves it to a file.
- **Validate Input**: Prompts the user to input the CAPTCHA text and validates the input against the generated text.
- **User Interaction**: Provides a simple command-line interface to generate and validate CAPTCHA.

## Installation

### Step 1: Install Dependencies
The CAPTCHA engine uses the **Pillow** library for image manipulation. Install the required dependencies using `pip`:

```bash
pip install pillow
