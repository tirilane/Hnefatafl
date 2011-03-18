#ifndef __PLAYER_H__
#define __PLAYER_H__

#include <string>
#include "piece.h"

class Player {
public:
	
private:
	std::string name;
};

class Defendant : public Player {
public:
	
private:
	DefendantPiece pieces[12];
	KingPiece king;
};

class Attacker : public Player {
public:
	
private:
	AttackerPiece pieces[24];
};

#endif // __PLAYER_H__
