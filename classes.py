import os
import cv2 
import matplotlib.pyplot as plt

"""
  0.  Watch images in folder
"""
# Specify the folder containing images
folder_path = "MRI Competitors Labeled_Images"

# list all files in the folder
image_files = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
]

# Loop through each images file and display it
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Unable to load image: {image_file}")
        continue

    cv2.imshow("Image Viewer", image)
    key = cv2.waitKey(0) # Wait for a kay prass to move to the next image

    if key == 27:
        break
cv2.destroyAllWindows()


"""
   1. Resize All Images in a Folder
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = "Resized_images"

# Create output folder if it dosen't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize dimensions
width, height = 1080, 900

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue
        
        resized_image = cv2.resize(image, (width, height))
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, resized_image)
        print(f"Resized and saved: {output_path}")


"""
   2. Convert Images to Grayscale
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'grayscale_images'

# Create output folder if it dosen't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each images
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue
        
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, grayscale_image)
        print(f"Convorted to grayscale and saved: {output_path}")


"""
   3. Display Images with Matplotlib
"""
# Folder containing images
folder_path = 'MRI Competitors Labeled_Images'

# List all images files
image_files = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
]

# Display each image
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Unable to load image: {image_file}")
        continue

    # Convort BGR to RGB for MatPlotLib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.imshow(image_rgb)
    plt.title(image_file)
    plt.axis('off')
    plt.show()


"""
   4. Detect Edges in Images
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'edge_detected_images'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue
        
        edges = cv2.Canny(image, 100, 200)
        output_path = os.path.join(output_folder, f"edges_{image_file}")
        cv2.imwrite(output_path, edges)
        print(f"Edge-detected image saved: {output_path}")


"""
    5. Create a Slideshow of Images
"""
# Folder containing image
folder_path = 'MRI Competitors Labeled_Images'

# List all image files
image_files = [
    f for f in os.listdir(folder_path)
    if f.lower().endswith(('.jpg', '.jpeg', '.png'))
]

# Display each image for 1 seconds
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print(f"Unable to load image: {image_file}")
        continue
    
    cv2.imshow('Slideshow', image)
    key = cv2.waitKey(1000) # Display each image for 1000ms (2 seconds)

    if key == 27: # Press 'ESC' to exit
        break
cv2.destroyAllWindows()


"""
    6. Blur Images
"""

# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'blurred_images'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue

        blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
        output_path = os.path.join(output_folder, f"blurred_{image_file}")
        cv2.imwrite(output_path, blurred_image)
        print(f"Blurred image saved: {output_path}")

"""
    7. Draw Shapes on Images
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'shapes_on_images'

# Create output folder if it dosen't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue
        
        # Draw a rectangle
        cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 3)

        # Draw a circle
        cv2.circle(image, (300, 300), 50, (255, 0, 0), -1) 

        output_path = os.path.join(output_folder, f"shapes_{image_file}")
        cv2.imwrite(output_path, image)
        print(f"Shales deawn and saved: {output_path}")


"""
    8. Add Text to Images
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'text_on_images'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue

        # Add text
        cv2.putText(image, 'Simple Text', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        output_path = os.path.join(output_folder, f"text_{image_file}")
        cv2.imwrite(output_path, image)
        print(f"Text added and saved: {output_path}")


"""
    9. Rotate Images
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'rotated_images'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")
            continue

        # Rotate the image 90 degrees clockwise
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

        output_path = os.path.join(output_folder, f"rotated_{image_file}")
        cv2.imwrite(output_path, rotated_image)
        print(f"Rotated image saved: {output_path}")


"""
    10. Crop Images
"""
# Folder containing images
input_folder = 'MRI Competitors Labeled_Images'
output_folder = 'cropped_images'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image
for image_file in os.listdir(input_folder):
    if image_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(input_folder, image_file)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Unable to load image: {image_file}")

        # Crop the image (e.g., top-left corner 100X1000 pixels)
        cropped_iamge = image[50:150, 50:150]

        output_path = os.path.join(output_folder, f"cropped_{image_file}")
        cv2.imwrite(output_path, cropped_iamge)
        print(f"Cropped image saved: {output_path}")

        