#ifndef FUNCTIONS
#define FUNCTIONS 
	/* move function with hook at the left side of the unit cell */ 
	void lefthook(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh);

	/* move function with hook at the right side of the unit cell */ 
	void righthook(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh);

	/* move function with symmetric hook */ 
	void symhook(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh);

	/* move function without obstacle */ 
	void no_obstacle(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh);
#endif //FUNCTIONS
