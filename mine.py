import comfy

class ChessPiecePromptNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "chess_piece": (["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"],),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positive_prompt",)

    FUNCTION = "generate_prompt"

    CATEGORY = "CustomNodes"

    def generate_prompt(self, chess_piece):
        prompts = {
            "King": "A majestic and powerful chess King, intricately detailed, set against a grand background, photorealistic, high resolution",
            "Queen": "A regal and elegant chess Queen, with detailed features and royal attire, set against a majestic background, photorealistic, high resolution",
            "Rook": "A solid and sturdy chess Rook, with intricate masonry details, set against a castle background, photorealistic, high resolution",
            "Bishop": "A wise and noble chess Bishop, with detailed robes and staff, set against a cathedral background, photorealistic, high resolution",
            "Knight": "A brave and gallant chess Knight, riding a majestic horse, with detailed armor, set against a medieval background, photorealistic, high resolution",
            "Pawn": "A simple yet determined chess Pawn, with detailed features, set against a battlefield background, photorealistic, high resolution"
        }
        return (prompts[chess_piece],)
    
NODE_CLASS_MAPPINGS = {
    "ChessPiecePromptNode": ChessPiecePromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePromptNode": "Chess Piece Prompt"
}