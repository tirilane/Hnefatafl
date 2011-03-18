#ifndef __PIECE_H__
#define __PIECE_H__

#include "pieceimg.h"

class Piece {
public:
	bool empty();
	bool getAlive();
	void setAlive(bool a);
private:
	bool alive;
};

class DefendantPiece : public Piece {
	static PieceImg defRep;
};

class AttackerPiece : public Piece {
	static PieceImg attRep;
};

class KingPiece : public DefendantPiece {
	static PieceImg kingRep;
};

#endif // __PIECE_H__
