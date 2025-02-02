import random
import string
from PIL import Image, ImageDraw, ImageFont
import os

class CAPTCHA:
    def __init__(self, width=200, height=80, length=5, font_size=30):
        """Initialize CAPTCHA configuration"""
        self.width = width
        self.height = height
        self.length = length
        self.font_size = font_size
        self.text = self.generate_random_text()
        self.image = None

    def generate_random_text(self):
        """Generate a random string of letters and digits"""
        characters = string.ascii_letters + string.digits
        random_text = ''.join(random.choice(characters) for _ in range(self.length))
        return random_text

    def create_image(self):
        """Create an image with the random text"""
        # Create a blank white image
        image = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))
        draw = ImageDraw.Draw(image)
        
        try:
            # You can specify a font file here if you want a custom font
            font = ImageFont.truetype("arial.ttf", self.font_size)
        except IOError:
            # Default font if arial is not available
            font = ImageFont.load_default()
        
        # Calculate the position of the text in the center
        text_width, text_height = draw.textsize(self.text, font=font)
        position = ((self.width - text_width) // 2, (self.height - text_height) // 2)
        
        # Add the text to the image
        draw.text(position, self.text, fill=(0, 0, 0), font=font)
        
        # Add some noise: random lines
        for _ in range(5):
            x1, y1 = random.randint(0, self.width), random.randint(0, self.height)
            x2, y2 = random.randint(0, self.width), random.randint(0, self.height)
            draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=2)
        
        # Add random points (noise)
        for _ in range(30):
            x, y = random.randint(0, self.width), random.randint(0, self.height)
            draw.point((x, y), fill=(0, 0, 0))

        self.image = image
        return image

    def save_image(self, filename):
        """Save the generated CAPTCHA image to a file"""
        if self.image:
            self.image.save(filename)

    def validate_answer(self, user_input):
        """Validate the user's CAPTCHA input"""
        return user_input == self.text
