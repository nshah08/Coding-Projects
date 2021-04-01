#ifndef TARGET_H
#define TARGET_H
#include <iostream>
#include <list>
#include <random>
#include <cstdlib>
#include <ctime>

using namespace std;

class Target
{
    public:
        Target();
        virtual ~Target();

        int GetId() { return Id; }
        void SetId(int val) { Id = val; }
        int Getspeed() { return speed; }
        void Setspeed(int val) { speed = val; }
        int Getsignal() { return signal; }
        void Setsignal(int val) { signal = val; }
        int Getx() { return x; }
        void Setx(int val) { x = val; }
        int Gety() { return y; }
        void Sety(int val) { y = val; }
        int Gettype() { return type; }
        void Settype(int val) { type = val; }
        void display();
        void rsig(default_random_engine * genptr);
        void rspeed(default_random_engine * genptr);
        void rtype(default_random_engine * genptr);
        int stype();
        void tmove();

    protected:

    private:
        int Id;
        int speed;
        int signal;
        int x;
        int y;
        int type;
        int profile[4];
};

#endif // TARGET_H
