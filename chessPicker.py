class ChessPieceNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "piece_type": (["King", "Queen", "Rook", "Bishop", "Knight", "Pawn"],)
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"

    def execute(self, piece_type):
        prompts = {
            "King": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a king, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (holding a sword:1.3)",
            "Queen": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a queen, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Rook": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a rook, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Bishop": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a bishop, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)",
            "Knight": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a knight, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0), (riding a horse:1.3)",
            "Pawn": "(solo) piece (realistic:1.5), (detailed:1.3), (human-like:1.4), (wearing a costume:1.3), (metallic sheen:0.9), (polished:1.2), (intricate engravings:1.1), maintaining the shape and features of a pawn, (full body:1.2), (high resolution:1.0), (sharp focus:1.0), (realistic textures:1.3), (dramatic lighting:1.0)"
        }

        return (prompts[piece_type],)

NODE_CLASS_MAPPINGS = {
    "ChessPieceNode": ChessPieceNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPieceNode": "Chess Piece Node"
}