import os

class ChessPiecePrompt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "piece": (["King", "Queen", "Bishop", "Knight", "Rook", "Pawn"],),
            }
        }

    RETURN_TYPES = ("STRING", "IMAGE")
    RETURN_NAMES = ("prompt", "image")

    FUNCTION = "generate_prompt"

    CATEGORY = "Chess"

    def generate_prompt(self, piece):
        prompt_map = {
            "King": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a king, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (holding a sword:1.3)",
            "Queen": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a queen, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Rook": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a rook, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Bishop": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a bishop, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Knight": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a knight, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (riding a horse:1.3)",
            "Pawn": "(solo) chess piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a chess costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a pawn, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }
        image_path = os.path.join(os.path.dirname(__file__), "images", f"{piece.lower()}.png")
        return (prompt_map[piece], image_path)

NODE_CLASS_MAPPINGS = {
    "ChessPiecePrompt": ChessPiecePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePrompt": "Chess Piece Prompt"
}