import base64

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Paths to your images
image_paths = {
    "King": "images/king.png",
    "Queen": "images/queen.png",
    "Bishop": "images/bishop.png",
    "Knight": "images/knight.png",
    "Rook": "images/rook.png",
    "Pawn": "images/pawn.png"
}

# Convert images to base64 strings
base64_images = {name: encode_image_to_base64(path) for name, path in image_paths.items()}

# Print the base64 strings (or save them to a file)
for name, base64_string in base64_images.items():
    print(f'{name}_image_base64 = "{base64_string}"')