#include "board.h"

bool Board::move(Square from, Square to) {
	// Break if there is no piece to move
	if (from.empty())
		return false;
	// Break if there already is a piece on the square to be moved to
	if (!to.empty())
		return false;
		
	int row, col;
	if (from.getRow() == to.getRow()) {
		row = from.getRow();
	} else if (from.getCol() == to.getCol()) {
		col = from.getCol();
	} 
	
}

bool Board::emptyRow(int row, int colStart, int colEnd) {
	int colMin, colMax;
	if (colStart < colEnd) {
		colMin = colStart;
		colMax = colEnd;
	} else {
		colMin = colEnd;
		colMax = colStart;
	}
	
	int c;
	for (c = colMin; c <= colMax; c++) {
		
	}
}

bool Board::emptyCol(int col, int rowStart, int rowEnd) {
	
}
