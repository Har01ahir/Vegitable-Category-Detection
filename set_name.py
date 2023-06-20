import os
from PIL import Image

folder_path = r"C:\Users\hardi\Face_detection\Onion_type_detection\onion" # Replace with the path to your folder
# new_name = "image_" # Replace with the prefix you want to use for your images

i = 822 # Start the counter at 0
for filename in os.listdir(folder_path):
    if filename.endswith(".jpeg"):
        # Convert PNG to JPG
        src = os.path.join(folder_path, filename)
        dst = os.path.join(r"C:\Users\hardi\Face_detection\Onion_type_detection\OnionData\Data", str(i) + ".jpg")
        with Image.open(src) as img:
            img.convert("RGB").save(dst)
    # elif filename.endswith(".jpg"):
    #     # Rename JPG
    #     src = os.path.join(folder_path, filename)
    #     dst = os.path.join(folder_path, new_name + str(i) + ".jpg")
    #     os.rename(src, dst)
    i += 1 # Increment the counter for the next image











# import os

# folder_path = r"C:\Users\hardi\Face_detection\Onion_type_detection\onion" # Replace with the path to your folder
# # new_name = "image_" # Replace with the prefix you want to use for your images

# i = 0 # Start the counter at 0
# for filename in os.listdir(folder_path):
#     if filename.endswith(".jpg"): # Change the extension to match your image format
#         src = os.path.join(folder_path, filename)
#         dst = os.path.join(r"C:\Users\hardi\Face_detection\Onion_type_detection\OnionData", str(i) + ".jpg") # Change the extension to match your image format
#         os.rename(src, dst)
#         i += 1 # Increment the counter for the next image
