#include <iostream>
#include <cmath>
#include <random>
#include <stdio.h>
#include "move.h"

using namespace std;

/* move function with hook at the left side of the unit cell */ 
void lefthook(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		x++;
		if (x == (nx+1) && y <= nyh){
			x--;
		}else if (x == (nx+1)){
			count++;
			x=1;
		}
	} else if (move == 1){
		x--;
		if (x == 0 && y <= nyh){
			x++;
		}else if (x == 0){
			x = nx;
			count--;
		}
	} else if (move == 2){
		y++;
		if (x <= nxh && y == (nyh+1)){
			y--;
		} else if (y == (ny+1)){
			y = ny;
		}
	} else if (move == 3){
		y--;
		if (x <= nxh && y == nyh){
			y++;
		}else if (y == 0){
			y = 1;
		}
	}
}

/* move function with hook at the right side of the unit cell */ 
void righthook(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		x++;
		if (x == (nx+1) && y <= nyh){
			x--;
		}else if (x == (nx+1)){
			count++;
			x=1;
		}
	} else if (move == 1){
		x--;
		if (x == 0 && y <= nyh){
			x++;
		}else if (x == 0){
			x = nx;
			count--;
		}
	} else if (move == 2){
		y++;
		if (x >= (nxh+1) && y == (nyh+1)){
			y--;
		} else if (y == (ny+1)){
			y = ny;
		}
	} else if (move == 3){
		y--;
		if (x >= (nxh+1) && y == nyh){
			y++;
		}else if (y == 0){
			y = 1;
		}
	}
}

/* move function with symmetric hook */ 
void symhook(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		x++;
		if (x == (nxh)+1 && y <= nyh){
			x--;
		}else if (x == (nx+1)){
			count++;
			x=1;
		}
	} else if (move == 1){
		x--;
		if (x == nxh && y <= nyh){
			x++;
		}else if (x == 0){
			x = nx;
			count--;
		}
	} else if (move == 2){
		y++;
		if (x >= nx1 && x <= nx2 && y == (nyh+1)){
			y--;
		} else if (y == (ny+1)){
			y = ny;
		}
	} else if (move == 3){
		y--;
		if (x >= nx1 && x <= nx2 && y == (nyh)){
			y++;
		}else if (y == 0){
			y = 1;
		}
	}
}

/* move function without obstacle */ 
void no_obstacle(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh){
	if (move == 0){
		x++;
		if (x == (nx+1)){
			count++;
			x=1;
		}
	} else if (move == 1){
		x--;
		if (x == 0){
			x = nx;
			count--;
		}
	} else if (move == 2){
		y++;
		if (y == (ny+1)){
			y = ny;
		}
	} else if (move == 3){
		y--;
		if (y == 0){
			y = 1;
		}
	}
}
