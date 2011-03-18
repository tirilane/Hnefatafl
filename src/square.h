#ifndef __SQUARE_H__
#define __SQUARE_H__

#include "piece.h"

enum SquareType {
	DEFENDANT_SQUARE, ATTACKER_SQUARE, NEUTRAL_SQUARE
};

class Square {
public:
	bool empty();

	SquareType getType();
	Piece getPiece();
	Piece getDefaultPiece();
	int getRow();
	int getCol();
	
private:
	SquareType type;
	Piece piece;
	Piece defaultPiece;
	int row, col;
};


#endif // __SQUARE_H__
