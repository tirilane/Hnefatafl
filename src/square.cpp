#include <iostream>
#include "square.h"

using namespace std;

bool Square::empty() {
	if (getPiece() != NULL)
		return true;
	return false;
}

SquareType Square::getType() {
	return type;
}
Piece Square::getPiece() {
	return piece;
}
Piece Square::getDefaultPiece() {
	return defaultPiece;
}
int Square::getRow() {
	return row; 
}
int Square::getCol() { 
	return col; 
}