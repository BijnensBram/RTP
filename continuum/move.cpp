#include <iostream>
#include <cmath>
#include <random>
#include "move.h"
using namespace std;

int righthook(double &x, double &y, double dt, double epsilon, double xmax, double ymax,double xh,double yh, double x1,double x2, double dx, double dy,double &tt,double tau){
	while (tt < tau){
		x += dx*dt;
		if (abs(xh-x) <= epsilon  && y < yh){
			x -= dx*dt;
		} else if (x > xmax){
			x-=xmax;
		} else if (x < 0){
			x+=xmax;
		}
		y += dy*dt;
		if (abs(y-yh) < epsilon && x > x1 && x < x2 ){
			y -= dy*dt;
		} else if (y > ymax){
			y=ymax;
		} else if (y<0){
				y=0;
		}
		tt+=dt;
	}
	return 0;
}

int symhook(double &x, double &y, double dt, double epsilon, double xmax, double ymax,double xh,double yh, double x1,double x2, double dx, double dy,double &tt,double tau){
	while (tt < tau){
		x += dx*dt;
		if (((xmax-x) <= epsilon | x <= epsilon) && y < yh){
			x -= dx*dt;
		} else if (x > xmax){
			x-=xmax;
		} else if (x < 0){
			x+=xmax;
		}
		y += dy*dt;
		if (abs(y-yh) < epsilon && x > xh ){
			y -= dy*dt;
		} else if (y > ymax){
			y=ymax;
		} else if (y<0){
				y=0;
		}
		tt+=dt;
	}
	return 0;
}
