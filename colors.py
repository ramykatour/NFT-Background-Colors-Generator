from PIL import Image, ImageDraw
import random
import os

# Create a directory to save the images
os.makedirs("generated_images", exist_ok=True)

# Number of images to generate
num_images = 1000

# Image size
width, height = 800, 600

for i in range(num_images):
    # Generate a random background color
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Create a new image with the specified background color
    image = Image.new("RGB", (width, height), background_color)

    # Draw something on the image (optional)
    draw = ImageDraw.Draw(image)
    # You can add text, shapes, or any other content here

    # Save the image as a JPG file
    file_name = f"generated_images/image_{i + 1}.jpg"
    image.save(file_name, "JPEG")

print(f"{num_images} images generated and saved without color effects.")
