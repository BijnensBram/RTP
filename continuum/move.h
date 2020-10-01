#ifndef FUNCTIONS
#define FUNCTIONS 

	/* move function with hook at the right side of the unit cell */ 
	int righthook(double &x, double &y, double dt, double epsilon, double xmax, double ymax,double xh,double yh, double x1,double x2, double dx, double dy,double &tt,double tau);

	/* move function with symmetric hook */ 
	int symhook(double &x, double &y, double dt, double epsilon, double xmax, double ymax,double xh,double yh, double x1,double x2, double dx, double dy,double &tt,double tau);
#endif //FUNCTIONS
