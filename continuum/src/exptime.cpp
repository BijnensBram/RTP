#include <iostream>
#include <cmath>
#include <random>
#include <fstream>
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
	double x1 = 0.25;
	double x2 = 0.75;
	double ymax = 1;
	double yh = 0.5;
	double epsilon = 0.001;
	int count = 0;
	int dummycount = 0;
	double rand = 0;
	
	std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_real_distribution<double> dist(0,1);
    std::uniform_real_distribution<double> distangle(0,360);
    std::uniform_real_distribution<double> distx(0,xmax);
    std::uniform_real_distribution<double> disty(0,ymax);
	
	/* taking user input */ 
	double c		= stod(argv[1]);
	double a		= stod(argv[2]);
	double dt		= stod(argv[3]);
	double tmax		= stod(argv[4]);
	int    obstacle = stod(argv[5]);
	double emax		= stod(argv[6]);
	double de		= stod(argv[7]);
    string filename = argv[8];
    ofstream Outfile;
	double emin;
	
	int (*movefunc)(double &x, double &y, double dt, double epsilon, double xmax, double ymax,double xh,double yh, double x1,double x2, double dx, double dy,double &tt,double tau,int &count);
	/* setting the obstacle */ 
	if (obstacle == 1){
		movefunc=&righthook;
		emin = 0;
	} else {
		movefunc=&symhook;
		emin = -emax;
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
	
    Outfile.open(filename,ios::trunc);
	for (double e=emin; e <= emax ; e += de){
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
				movefunc(x,y,dt,epsilon,xmax,ymax,xh,yh,x1,x2,dx,dy,tt,tau,dummycount);
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
				movefunc(x,y,dt,epsilon,xmax,ymax,xh,yh,x1,x2,dx,dy,tt,tau,count);
				t+=tt;
			}
		}
		Outfile << e << ";" << count/(N*tmax) << "\n";
	}
    Outfile.close();
} 
