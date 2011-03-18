#ifndef __BOARD_H__
#define __BOARD_H__

#include "piece.h"
#include "square.h"

class Board {
public:
	Square squares[11][11];
	bool move(Square oldSquare, Square newSquare);

private:
	bool emptyRow(int row, int colStart, int colEnd);  
	bool emptyCol(int col, int rowStart, int rowEnd);
};

#endif // __BOARD_H__
