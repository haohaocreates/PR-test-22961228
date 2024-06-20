
import base64

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
        }
        
        # Base64 encoded images
        images = {
            "King": "king_image_base64_string",
            "Queen": "queen_image_base64_string",
            "Bishop": "bishop_image_base64_string",
            "Knight": "knight_image_base64_string",
            "Rook": "rook_image_base64_string",
            "Pawn": "pawn_image_base64_string"
        }
        
        prompt = prompts[chess_piece]
        image_base64 = images[chess_piece]

        # Decode the image from base64
        image_data = base64.b64decode(image_base64)

        return (prompt, image_data)

NODE_CLASS_MAPPINGS = {
    "ChessPiecePrompt": ChessPiecePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePrompt": "Chess Piece Prompt"
}