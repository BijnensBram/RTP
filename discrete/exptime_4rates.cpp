#include <iostream>
#include <cmath>
#include <random>
#include <stdio.h>
#include "move.h"

using namespace std;

/* printing metadata */ 
#define PRINTER(name) std::cout << "#" << #name << " = " << name << std::endl;

/* test whether and what way the particle moves */ 
int movetest(double dt, double *k, double rand){
	if (rand < k[0]*dt){
		return 0;
	} else if (rand < (k[0]+k[1])*dt){
		return 1;
	} else if (rand < (k[0]+k[1]+k[2])*dt ){
		return 2;
	} else if (rand < (k[0]+k[1]+k[2]+k[3])*dt ){
		return 3;
	} else {
		return 5;
	}
}

/* test whether sigma flips or not */ 
int fliptest(double mu,int sigma, double rand,int rand2){
	if (rand < 1-mu){
		return sigma;
	} else {
		return sigma = (sigma + rand2) % 4;
	}
}

/* function to test if particles do not have a change to move greater than one */ 
int testerror (double dt, double p[],double m[],double u[],double d[]){
	if ( (p[1]+p[2]+p[3]+p[0])*dt > 1 | (m[1]+m[2]+m[3]+m[0])*dt > 1 | (u[1]+u[2]+u[3]+u[0])*dt > 1 | (d[1]+d[2]+d[3]+d[0])*dt > 1){
		cerr << "Error: rates to high for dt" << endl;
		exit(1);
	}
	return 1;
}

/* function to calculate the time the sigma stays the same */
double waitingtime(double a,double rand){
	return -(1/a)*log(1-rand);
}

int main(int argc, char *argv[]){
	/* setting the program constants */ 
    const double pi2 = 6.28318530718;
	const double dx = 0.1;
	const double dy = 0.1;
	const int nx = 10;
	const int ny = 10;
	const int nx1 = 3;
	const int nx2 = 8;
	const int nxh = 5;
	const int nyh =	5;
    const int N = 10000; 

    /* init */
	/* random number generators */ 
	std::random_device dev;
	std::mt19937 rng(dev());
	std::uniform_real_distribution<double> dist(0,1);
	std::uniform_int_distribution<int> distsigma(0,3);
	std::uniform_int_distribution<int> distx(0,nx);
	/* std::uniform_int_distribution<int> disty(nyh,ny); */
	std::uniform_int_distribution<int> disty(0,nyh);
	
	/* defining variables */ 
	double rand;
	int rand2;
	int x;
    int y;
	int move;
	int sigma;
	int count;
	int count_dummy;
	void (*movefunc)(int move, int &x, int &y, int &count, int nx, int nxh, int nx1, int nx2, int ny, int nyh);

	/* taking user input */ 
	double c = stod(argv[1]);
	double a = stod(argv[2]);
	double dt = stod(argv[3]);
	double tmax = stod(argv[4]);
	int obstacle = stod(argv[5]);
	double emax = stod(argv[6]);
	double de = stod(argv[7]);
	double emin;

	/* setting the obstacle */ 
	if (obstacle == 1){
		movefunc=&lefthook;
		emin = emax;
		emax = 0;
	} else if (obstacle == 2) {
		movefunc=&righthook;
		emin = 0;
	} else if (obstacle == 3) {
		movefunc=&symhook;
		emin = -emax;
	} else {
		movefunc=&no_obstacle;
		emin = -emax;
	}
	
	/* printing out the parameters */ 
	PRINTER(dt);
	PRINTER(a);
	PRINTER(c);
	PRINTER(N);
	PRINTER(tmax);

	/* simulation */ 
	for (double e = emin; e <= emax; e+=de){

		double bp = 0.5*(c+e);
		double bm = 0.5*(-c+e);
		double bu = 0.5*(c);
		double bd = 0.5*(-c);
		double be = 0.5*(e);
		
		double p[4] = {(bp+sqrt(bp*bp+1))/dx,1/((bp+sqrt(bp*bp+1))*dx),(bd+sqrt(bd*bd+1))/dx,(bd+sqrt(bd*bd+1))/dx};
		double m[4] = {(bm+sqrt(bm*bm+1))/dx,1/((bm+sqrt(bm*bm+1))*dx),(bd+sqrt(bd*bd+1))/dx,(bd+sqrt(bd*bd+1))/dx};
		double u[4] = {(bm+sqrt(bm*bm+1))/dx,1/((bp+sqrt(bp*bp+1))*dx),(bu+sqrt(bu*bu+1))/dx,((bd+sqrt(bd*bd+1))/dx)};
		double d[4] = {(bm+sqrt(bm*bm+1))/dx,1/((bp+sqrt(bp*bp+1))*dx),(bd+sqrt(bd*bd+1))/dx,((bu+sqrt(bu*bu+1))/dx)};

		/* double p[4] = {(bp+sqrt(bp*bp+1))/dx,1/((bp+sqrt(bp*bp+1))*dx),(bd+sqrt(bd*bd+1))/dx,(bd+sqrt(bd*bd+1))/dx}; */
		/* double m[4] = {(bm+sqrt(bm*bm+1))/dx,1/((bm+sqrt(bm*bm+1))*dx),(bd+sqrt(bd*bd+1))/dx,(bd+sqrt(bd*bd+1))/dx}; */
		/* double u[4] = {(bm+sqrt(bm*bm+1))/dx,1/((bp+sqrt(bp*bp+1))*dx),(bu+sqrt(bu*bu+1))/dx,((bd+sqrt(bd*bd+1))/dx)}; */
		/* double d[4] = {(be+sqrt(be*be+1))/dx,1/((be+sqrt(be*be+1))*dx),(bd+sqrt(bd*bd+1))/dx,((bu+sqrt(bu*bu+1))/dx)}; */

		double *list_of_rates[4] = {p, m, u, d};
		double *rates;
		testerror(dt,p,m,u,d);
		count = 0;
		count_dummy =0;
		double t;
		double tau;
		for (int i=1; i <= N; i++){
			x = distx(rng);
			y = disty(rng);
			/* equilibration period */ 
			t=0;
			while (t < 50){
				rand = dist(rng);
				sigma = distsigma(rng);
				tau = waitingtime(a,rand);

				rates = list_of_rates[sigma];
				
				for (double tt=0 ; tt < tau ; tt+=dt){
					rand = dist(rng);
					move = movetest(dt,rates,rand);
					movefunc(move,x,y,count_dummy,nx,nxh,nx1,nx2,ny,nyh);
				}
				t += tau;
			}
			/* measuring period */ 
			t=0;
			while (t < tmax){
				rand = dist(rng);
				sigma = distsigma(rng);
				tau = waitingtime(a,rand);

				rates = list_of_rates[sigma];

				for (double tt=0 ; tt<tau ; tt+=dt){
					rand = dist(rng);
					move = movetest(dt,rates,rand);
					movefunc(move,x,y,count,nx,nxh,nx1,nx2,ny,nyh);
				}
				t+=tau;
			}
		}
		cout << e << ";" << count/(tmax*N) << endl;
	}
	return 0;
}
