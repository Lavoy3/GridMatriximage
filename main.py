# Import the required modules
import cv2 as cv
import numpy as np

# Read the image from a file
img = cv.imread('image.jpg')

# Resize the image to fit the display
img = cv.resize(img, (2880, 1800))

# Define the grid shape (rows, columns)
grid_shape = (10, 10)

# Draw the grid and use the original color
def draw_grid_and_use_original_color(img, grid_shape):
  # Get the image height, width and channels
  h, w, c = img.shape

  # Get the grid rows and columns
  rows, cols = grid_shape

  # Get the grid cell height and width
  dy, dx = h // rows, w // cols

  # Loop over the grid cells
  for i in range(rows):
    for j in range(cols):
      # Get the cell coordinates
      x1, y1 = j * dx, i * dy
      x2, y2 = (j + 1) * dx, (i + 1) * dy

      # Get the cell color
      color = img[y1:y2, x1:x2].mean(axis=(0, 1))

      # Fill the cell with the original color
      img[y1:y2, x1:x2] = color

      # Draw the cell border
      cv.rectangle(img, (x1, y1), (x2, y2), (128, 128, 128), 1)

  # Return the modified image
  return img

# Apply the function to the image
img = draw_grid_and_use_original_color(img, grid_shape)

# Show the image
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
