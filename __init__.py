from .chessPicker import ChessPiecePrompt

# Ensure the module is registered with ComfyUI
NODE_CLASS_MAPPINGS = {
    "ChessPiecePrompt": ChessPiecePrompt
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ChessPiecePrompt": "Chess Piece Prompt"
}