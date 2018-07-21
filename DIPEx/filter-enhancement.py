# import image module
from PIL import Image
from PIL import ImageFilter
# Open an already existing image
imageObject = Image.open("sand.jpg")
# Apply edge enhancement filter
edgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE)
# Apply increased edge enhancement filter
moreEdgeEnahnced = imageObject.filter(ImageFilter.EDGE_ENHANCE_MORE)
# Show original image - before applying edge enhancement filters
imageObject.show() 
# Show image - after applying edge enhancement filter
edgeEnahnced.show()
# Show image - after applying increased edge enhancement filter
moreEdgeEnahnced.show()
