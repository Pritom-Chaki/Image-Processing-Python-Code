# import the pillow modules
from PIL import Image
from PIL import ImageFilter
# Create an Image Object
image = Image.open("./lamp.jpg")
# Apply SMOOTH filters
smoothenedImage = image.filter(ImageFilter.SMOOTH)
moreSmoothenedImage = image.filter(ImageFilter.SMOOTH_MORE)
# Display the original image and the smoothened Images
image.show()
smoothenedImage.show()
moreSmoothenedImage.show()