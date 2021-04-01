#ifndef DUST_H
#define DUST_H
#include <iostream>
#include <list>
#include <random>
#include <cstdlib>
#include <ctime>
#include <cmath>



using namespace std;

class dust
{
    public:
        dust();
        dust(int id1);
        virtual ~dust();

        int Getid() { return id; }
        void Setid(int val) { id = val; }
        int Getx() { return x; }
        void Setx(int val) { x = val; }
        int Gety() { return y; }
        void Sety(int val) { y = val; }
        int Getstrength() { return strength; }
        void Setstrength(int val) { strength = val; }
        int Gettsignal() { return tsignal; }
        void Settsignal(int val) { tsignal = val; }
        void display();
        void randomx(default_random_engine * genptr);
        void randomy(default_random_engine * genptr);
        void rtsignal(default_random_engine * genptr);
        void sigcalc(int sig1, int x1, int y1, int type);

    protected:

    private:
        int id;
        int x;
        int y;
        int tsignal;
        int strength;

};

#endif // DUST_H
