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
            "King": "A majestic king with a golden crown, royal robes, holding a sword, standing tall.",
            "Queen": "A regal queen with a jeweled crown, elegant robes, holding a scepter, standing with grace.",
            "Bishop": "A wise bishop with a mitre, holding a staff, standing in a contemplative pose.",
            "Knight": "A brave knight in shining armor, riding a horse, holding a lance, ready for battle.",
            "Rook": "A sturdy tower with battlements, standing firm and imposing.",
            "Pawn": "A determined pawn with simple armor, holding a spear, ready for duty."
        }
        image_path = os.path.join(os.path.dirname(__file__), "images", f"{piece.lower()}.png")
        return (prompt_map[piece], image_path)

NODE_CLASS_MAPPINGS = {
    "ChessPiecePrompt": ChessPiecePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePrompt": "Chess Piece Prompt"
}