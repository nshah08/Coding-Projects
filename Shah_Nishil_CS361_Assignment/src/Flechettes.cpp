#include "Flechettes.h"

Flechettes::Flechettes(int i)
{
    id=i;
}

Flechettes::~Flechettes()
{
    //dtor
}

void Flechettes::randomy(default_random_engine * genptr)
{
    normal_distribution<double> ydist(100,15);
    y=ydist(*genptr);
}

void Flechettes::display()
{
    cout << "Flechettes ID: " << id <<  " ("<<x<<", "<<y<<") " << endl;
}

void Flechettes::randomx(default_random_engine * genptr)
{
    uniform_real_distribution<double> xdist(0,200);
    x=xdist(*genptr);
}

void Flechettes::checkdust()
{
    Ditr=Dlist.begin();
    while(Ditr!=Dlist.end())
    {
        int x1= (*Ditr)->Getx();
        int y1= (*Ditr)->Gety();
        if(x+20>=x1 && x1>=x-20)
        {
            if(y+20>=y1 && y1>=y-20)
            {
                cout << "In Range " << ((*Ditr)->Getid()) << endl;
            }
            else
            {
                cout<< "Not in Range" << endl;
            }
        }
        else
        {
            cout << "Not in Range" << endl;
        }
        Ditr++;
    }
}
