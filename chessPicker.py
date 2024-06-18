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
            "King": "An ultra-realistic king, transformed into a medieval king, wearing an ornate crown and luxurious royal robes, holding a scepter, standing in a regal pose, set against a grand throne room backdrop, photorealistic, high resolution, sharp focus, dramatic lighting, realistic textures and reflections",
            "Queen": "An ultra-realistic queen, transformed into a medieval queen, wearing an elegant crown and detailed royal gown, holding a scepter, standing in a majestic pose, set against a lavish castle garden backdrop, photorealistic, high resolution, sharp focus, dramatic lighting, realistic textures and reflections",
            "Rook": "An ultra-realistic rook, transformed into a fortified medieval tower, with intricate stonework, battlements, and archers' slots, standing strong and imposing, set against a castle courtyard backdrop, photorealistic, high resolution, sharp focus, dramatic lighting, realistic textures and reflections",
            "Bishop": "An ultra-realistic bishop, transformed into a medieval cleric, wearing detailed robes and a mitre, holding a staff with intricate carvings, standing in a serene and wise pose, set against a grand cathedral interior backdrop, photorealistic, high resolution, sharp focus, dramatic lighting, realistic textures and reflections",
            "Knight": "An ultra-realistic knight, transformed into a medieval knight riding a majestic horse, wearing detailed armor with intricate engravings, holding a shining sword, set against a castle backdrop, photorealistic, high resolution, sharp focus, dramatic lighting, realistic textures and reflections",
            "Pawn": "An ultra-realistic pawn, transformed into a medieval foot soldier, wearing basic but sturdy armor and a helmet, holding a spear, standing in a vigilant pose, set against a battlefield backdrop, photorealistic, high resolution, sharp focus, dramatic lighting, realistic textures and reflections"
        }
        return (prompts[chess_piece],)
    
NODE_CLASS_MAPPINGS = {
    "ChessPiecePromptNode": ChessPiecePromptNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePromptNode": "Chess Piece Prompt"
}