
import base64
import os

class ChessPiecePrompt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "chess_piece": (["King", "Queen", "Bishop", "Knight", "Rook", "Pawn"],),
            }
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("positive_prompt", "chess_image")

    FUNCTION = "generate_prompt"

    CATEGORY = "Custom"

    def generate_prompt(self, chess_piece):
        prompts = {
            "King": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a king, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (holding a sword:1.3)",
            "Queen": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a queen, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Rook": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a rook, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Bishop": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a bishop, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Knight": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a knight, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (riding a horse:1.3)",
            "Pawn": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a pawn, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }\

        # Define the path to the images directory
        images_dir = os.path.join(os.path.dirname(__file__), 'images')

        # Base64 encoded images
        images = {
            "King": os.path.join(images_dir, 'king.png'),
            "Queen": os.path.join(images_dir, 'queen.png'),
            "Bishop": os.path.join(images_dir, 'bishop.png'),
            "Knight": os.path.join(images_dir, 'knight.png'),
            "Rook": os.path.join(images_dir, 'rook.png'),
            "Pawn": os.path.join(images_dir, 'pawn.png')
        }

        # Convert image to base64
        def encode_image_to_base64(image_path):
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

        prompt = prompts[chess_piece]
        image_base64 = encode_image_to_base64(images[chess_piece])

        # Decode the image from base64
        image_data = base64.b64decode(image_base64)

        return (prompt, image_data)

NODE_CLASS_MAPPINGS = {
    "ChessPiecePrompt": ChessPiecePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePrompt": "Chess Piece Prompt"
}