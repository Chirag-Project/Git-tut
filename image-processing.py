import cv2
import asyncio


# Read the image
img = cv2.imread('E:\Projects\ziaskinandwellness\image\contact-lady2.jpg')

# Define the crop size
crop_size = (10, 10)

# Loop through the image and create cropped images
cropped_images = []
for i in range(0, img.shape[0], crop_size[0]):
    for j in range(0, img.shape[1], crop_size[1]):
        cropped_image = img[i:i+crop_size[0], j:j+crop_size[1]]
        cropped_images.append(cropped_image)

# Define a coroutine to send the cropped images asynchronously
async def send_cropped_images(cropped_images):
    # Code to send the images asynchronously goes here

# Create a new event loop and run the coroutine
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_cropped_images(cropped_images))
    loop.close()

# Save the cropped images
for i, cropped_image in enumerate(cropped_images):
    cv2.imwrite(f'path/to/cropped_image_{i}.jpg', cropped_image)
