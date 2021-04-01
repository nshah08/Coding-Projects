#ifndef FLECHETTES_H
#define FLECHETTES_H
#include <iostream>
#include <list>
#include <random>
#include <ctime>
#include <cstdlib>
#include "dust.h"

using namespace std;

class Flechettes
{
    public:
        Flechettes(int i);
        virtual ~Flechettes();
        int Getid() { return id; }
        void Setid(int val) { id = val; }
        int Getx() { return x; }
        void Setx(int val) { x = val; }
        int Gety() { return y; }
        void Sety(int val) { y = val; }
        list<dust*> GetDlist() { return Dlist; }
        void SetDlist(list<dust*> val) { Dlist = val; }
        void randomy(default_random_engine * genptr);
        void randomx(default_random_engine * genptr);
        void display();
        void addDust(dust * dptr){Dlist.push_back(dptr);}
        void checkdust();

    protected:

    private:
        int id;
        int x;
        int y;
        list<dust*> Dlist;
        list<dust*>::iterator Ditr;
};

#endif // FLECHETTES_H
