import math
import numpy as np
import os
from PIL import Image

class ImageSizer:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                
            "King": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a king, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (holding a sword:1.3)",
            "Queen": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a queen, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Rook": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a rook, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Bishop": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a bishop, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Knight": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a knight, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (riding a horse:1.3)",
            "Pawn": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a pawn, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("Output Image",)
    FUNCTION = "run"
    CATEGORY = "CodyCustom"

    def run(self, model_type, aspect_ratio_width, aspect_ratio_height, chess_piece):
        # Define the total pixel counts for SD and SDXL
        total_pixels = {
            'SD': 512 * 512,
            'SDXL': 1024 * 1024
        }

        # Calculate the number of total pixels based on model type
        pixels = total_pixels.get(model_type, 0)

        # Calculate the aspect ratio decimal
        aspect_ratio_decimal = aspect_ratio_width / aspect_ratio_height

        # Calculate width and height
        width = math.sqrt(pixels * aspect_ratio_decimal)
        height = pixels / width

        # Generate prompts based on chess piece
        prompts = {
            "king": "(full body, human wearing a costume of king, crown, sword:1.0), (medieval attire, standing tall:1.0), (detailed face, realistic features, natural lighting:1.0), (metallic sheen:0.9), (detailed costume, intricate design)",
            "queen": "(full body, human wearing a costume of queen, crown, regal attire:1.0), (medieval attire, graceful stance:1.0), (detailed face, realistic features, natural lighting:1.0), (metallic sheen:0.9), (detailed costume, intricate design)",
            "bishop": "(full body, human wearing a costume of bishop, religious attire:1.0), (medieval attire, holding a staff:1.0), (detailed face, realistic features, natural lighting:1.0), (metallic sheen:0.9), (detailed costume, intricate design)",
            "knight": "(full body, human wearing a costume of knight, armor, on horseback:1.0), (medieval attire, holding a sword:1.0), (detailed face, realistic features, natural lighting:1.0), (metallic sheen:0.9), (detailed costume, intricate design)",
            "rook": "(full body, human wearing a costume of rook, castle-like attire:1.0), (medieval attire, standing firm:1.0), (detailed face, realistic features, natural lighting:1.0), (metallic sheen:0.9), (detailed costume, intricate design)",
            "pawn": "(full body, human wearing a costume of pawn, simple attire:1.0), (medieval attire, determined stance:1.0), (detailed face, realistic features, natural lighting:1.0), (metallic sheen:0.9), (detailed costume, intricate design)"
        }

        # Get the prompt for the selected chess piece
        prompt = prompts.get(chess_piece, "")

        # Load the corresponding chess piece image
        image_path = os.path.join("custom_nodes/ChessJawn/images", f"{chess_piece}.png")
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        image = Image.open(image_path)
        image = image.resize((int(round(width)), int(round(height))), Image.ANTIALIAS)
        image_array = np.array(image)

        return (image_array,)

NODE_CLASS_MAPPINGS = {
    "ImageSizer": ImageSizer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageSizer": "Image Sizer"
}