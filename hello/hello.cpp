// let's build a simple chess game
// we will have a board of 8x8 - we will use a 2D array
char board[8][8] = {
    {'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'},
    {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
    {'', '', '', '', '', '', '', ''},
    {'', '', '', '', '', '', '', ''},
    {'', '', '', '', '', '', '', ''},
    {'', '', '', '', '', '', '', ''},
    {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
    {'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'}
};

void printBoard() {
    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}
legalMovesPawn = {
    {1, 0},
    {2, 0},
    {1, 1},
    {1, -1}
};

// we will have 2 players
// each player will have 16 pieces
// 8 pawns, 2 rooks, 2 knights, 2 bishops, 1 queen, 1 king
legalMovesRook = {
    {1, 0},
    {2, 0},
    {3, 0},
    {4, 0},
    {5, 0},
    {6, 0},
    {7, 0},
    {8, 0},
    {0, 1},
    {0, 2},
    {0, 3},
    {0, 4},
    {0, 5},
    {0, 6},
    {0, 7},
    {0, 8}
};

// each piece will have a color
// the board will have 2 colors
// the pieces will move according to their rules
// pawns can move 1 or 2 squares forward, 1 square diagonally to capture
// rooks can move any number of squares horizontally or vertically
// knights can move in an L shape (2 squares in one direction, 1 square in the other)
// bishops can move diagonally any number of squares (like the rook)
// queens can move any number of squares in any direction (like the rook and the bishop)
// kings can move 1 square in any direction
// the game will start with the white player

// the game will end when one of the kings is captured
// the game will end when one of the kings is in checkmate
// the game will end when one of the players resigns
// the game will end when there is a stalemate
// the game will end when there is a draw
// the game will end when there is a 3-fold repetition
// the game will end when there is a 50-move rule
// the game will end when there is insufficient material