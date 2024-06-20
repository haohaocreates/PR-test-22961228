import os
from PIL import Image
import numpy as np
import io

class ChessPieceSelector:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "chess_piece": (["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"],)
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("Output Image", "Prompt")

    FUNCTION = "run"
    CATEGORY = "ChessNodes"

    def run(self, chess_piece):
        # Define prompts for each chess piece
        prompts = {
            "King": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a king, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (holding a sword:1.3)",
            "Queen": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a queen, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Rook": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a rook, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Bishop": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a bishop, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Knight": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a knight, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (riding a horse:1.3)",

            "Pawn": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a pawn, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }

        # Load the corresponding chess piece image
        image_path = os.path.join(os.path.dirname(__file__), "images", f"{chess_piece.lower()}.png")
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        image = Image.open(image_path)
        
        # Convert the image to bytes for output
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')

        img_byte_arr = img_byte_arr.getvalue()

        prompt = prompts.get(chess_piece, "")

        return (img_byte_arr, prompt)

NODE_CLASS_MAPPINGS = {
    "ChessPieceSelector": ChessPieceSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPieceSelector": "Chess Piece Selector"
}