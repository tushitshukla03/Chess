import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('./Chess/images/' + piece + '.png'), (SQ_SIZE, SQ_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []
    promotion = False
    promotionMove = None

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if promotion:
                    choice = getPromotionChoice(location)
                    if choice:
                        promotionMove = choice
                        gs.makeMove(promotionMove)
                        moveMade = True
                        promotion = False
                        promotionMove = None
                else:
                    if sqSelected == (row, col):
                        sqSelected = ()
                        playerClicks = []
                    else:
                        sqSelected = (row, col)
                        playerClicks.append(sqSelected)
                    if len(playerClicks) == 2:
                        startSq, endSq = playerClicks
                        move = ChessEngine.Move(startSq, endSq, gs.board)
                        for i in range(len(validMoves)):
                            if move == validMoves[i]:
                                if move.isPawnPromotion:
                                    promotion = True
                                    promotionMove = move
                                else:
                                    gs.makeMove(validMoves[i])
                                    moveMade = True
                                sqSelected = ()
                                playerClicks = []
                        if not moveMade:
                            playerClicks = [sqSelected]
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs, promotion)
        clock.tick(MAX_FPS)
        p.display.flip()
        
def getPromotionChoice(location):
    x, y = location
    if y < SQ_SIZE:
        col = x // SQ_SIZE
        if col == 0:
            return 'Q'
        elif col == 1:
            return 'R'
        elif col == 2:
            return 'B'
        elif col == 3:
            return 'N'
    return None

def drawGameState(screen, gs, promotion):
    drawBoard(screen)
    drawPieces(screen, gs.board)
    if promotion:
        drawPromotionChoices(screen)
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("pink")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
def drawPromotionChoices(screen):
    choices = ['wQ', 'wR', 'wB', 'wN']
    for i in range(4):
        p.draw.rect(screen, p.Color("gray"), p.Rect(i * SQ_SIZE, 0, SQ_SIZE, SQ_SIZE))
        screen.blit(IMAGES[choices[i]], p.Rect(i * SQ_SIZE, 0, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
