#include <iostream>
#include <cmath>
#include <random>
#include "move.h"
using namespace std;

double flip(double a,double dt, double angle,double randangle,double rand){
	if (rand < a*dt){
		return randangle; 
	}
	else {
		return angle;
	}
}

double waitingtime(double a,double rand){
	return -(1/a)*log(1-rand);
}

int main(int argc,char *argv[]){
	/*	constants*/
	int N = 10000;
	double xmax = 1;
	double xh = 0.5;
	double ymax = 1;
	double yh = 0.5;
	double epsilon = 0.001;
	int count = 0;
	double rand = 0;
	double randangle = 0;
	
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_real_distribution<double> dist(0,1);
    std::uniform_real_distribution<double> distangle(0,360);
    std::uniform_real_distribution<double> distx(0,xmax);
    std::uniform_real_distribution<double> disty(0,ymax);
	
	/* taking user input */ 
	double c = stod(argv[1]);
	double a = stod(argv[2]);
	double dt = stod(argv[3]);
	double tmax = stod(argv[4]);
	int obstacle = stod(argv[5]);
	
	
	int (*movefunc)(double &x, double &y, double dt, double epsilon, double xmax, double ymax,double xh,double yh, double x1,double x2, double dx, double dy,double &tt,double tau);
	/* setting the obstacle */ 
	if (obstacle == 1){
		movefunc=&righthook;
	} else {
		movefunc=&symhook;
	}
	
	/*	init*/
	double x;
	double y;
	double dx;
	double dy;
	double angle = distangle(rng);
	double tau;
	double t;
	double tt;
	
	for (double e=0; e <=0.1 ; e += 0.005){
		count = 0;
		for (int i =0 ; i <= N ; i++){
			x = distx(rng);
			y = disty(rng);
			t = 0;
			while (t < 50){
				rand = dist(rng);
				angle = distangle(rng);
				tau = waitingtime(a,rand);
				dx = cos(angle)*c + e;
				dy = sin(angle)*c;
				tt=0;
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
				t+=tt;
			}
			t = 0;
			while (t < tmax){
				rand = dist(rng);
				angle = distangle(rng);
				tau = waitingtime(a,rand);
				dx = cos(angle)*c + e;
				dy = sin(angle)*c;
				tt=0;
				while (tt < tau){
					x += dx*dt;
					if (((xmax-x) <= epsilon | x <= epsilon) && y < yh){
						x -= dx*dt;
					} else if (x > xmax){
						x-=xmax;
						count++;
					} else if (x < 0){
						x+=xmax;
						count--;
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
				t+=tt;
			}
		}
		cout << e << ";" << count/(tmax) << endl;
	}
} 
