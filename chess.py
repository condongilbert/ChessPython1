class Piece:
    def __init__(self, color):
        self.color = color
    
    def valid_moves(self, position, board):
        # To be implemented in individual pieces
        pass

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def valid_moves(self, position, board):
        # Logic for pawn moves
        pass

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        # Logic for king moves
        pass

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def valid_moves(self, position, board):
        # Logic for queen moves
        pass

# Define other pieces similarly (Rook, Bishop, Knight)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    def valid_moves(self, position, board):
        # Logic for bishop moves
        pass

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    def valid_moves(self, position, board):
        # Logic for bishop moves
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    def valid_moves(self, position, board):
        # Logic for bishop moves
        pass

class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # 8x8 grid with None in empty spaces and Piece objects in the correct places
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Initialize pawns, rooks, knights, etc.
        # For example, initialize white pawns at row 1
        for i in range(8):
            board[1][i] = Pawn('white')
            board[6][i] = Pawn('black')
        
        # Other pieces
        board[0][0], board[0][7] = Rook('white'), Rook('white')  # Rooks
        board[7][0], board[7][7] = Rook('black'), Rook('black')

        board[0][1], board[0][6] = Knight('white'), Knight('white')  # Knights
        board[7][1], board[7][6] = Knight('black'), Knight('black')

        board[0][2], board[0][5] = Bishop('white'), Bishop('white')  # Bishops
        board[7][2], board[7][5] = Bishop('black'), Bishop('black')

        board[0][3], board[7][3] = Queen('white'), Queen('black')  # Queens
        board[0][4], board[7][4] = King('white'), King('black')  # Kings

        return board

    def print_board(self):
        for row in self.board:
            print([self.get_piece_symbol(piece) if piece else '.' for piece in row])
    def get_piece_symbol(self, piece):
    # Return specific symbols for each piece type
        if isinstance(piece, King):
            return 'K'
        elif isinstance(piece, Queen):
            return 'Q'
        elif isinstance(piece, Rook):
            return 'R'
        elif isinstance(piece, Bishop):
            return 'B'
        elif isinstance(piece, Knight):
            return 'N'  # 'N' for Knight to avoid conflict with 'K' for King
        elif isinstance(piece, Pawn):
            return 'P'
        return '?'  # Default fallback (in case something goes wrong)
    
class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def play_turn(self):
        print(f"{self.current_turn}'s turn")
        self.board.print_board()

        # Ask the user to input their move
        start = input("Enter the position of the piece to move (e.g., 'e2'): ")
        end = input("Enter the position to move to (e.g., 'e4'): ")
        
        # Convert input into board positions (e.g., 'e2' -> (6, 4), 'e4' -> (4, 4))
        start_pos = self.algebraic_to_index(start)
        end_pos = self.algebraic_to_index(end)

        # Perform move validation and move the piece
        piece = self.board.board[start_pos[0]][start_pos[1]]
        if piece and piece.color == self.current_turn:
            if self.is_valid_move(piece, start_pos, end_pos):
                self.move_piece(start_pos, end_pos)
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            else:
                print("Invalid move!")
        else:
            print("No valid piece at this position or not your turn!")

    def algebraic_to_index(self, pos):
        column = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return (row, column)

    def is_valid_move(self, piece, start, end):
        # Check if the move is valid according to the piece's rules
        return True  # Placeholder for move validation logic

    def move_piece(self, start, end):
        self.board.board[end[0]][end[1]] = self.board.board[start[0]][start[1]]
        self.board.board[start[0]][start[1]] = None

if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    while True:
        game.play_turn()

    
        