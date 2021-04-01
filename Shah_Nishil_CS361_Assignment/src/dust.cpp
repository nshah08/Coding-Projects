#include "dust.h"

dust::dust()
{

}

dust::~dust()
{

}

dust::dust(int id1)
{
     id=id1;

}
void dust::display()
{
    cout<<"Dust ID: " << id << " ("<<x<<", "<<y<<") "<< "Type of Signal: " << tsignal << endl;
}

void dust::randomx(default_random_engine * genptr)
{

    uniform_real_distribution<double> xdist(0,200);
    x=xdist(*genptr);
}

void dust::randomy(default_random_engine * genptr)
{
    normal_distribution<double> ydist(100,30);
    y=ydist(*genptr);
}

void dust::rtsignal(default_random_engine * genptr)
{
    uniform_int_distribution<int> tsig(1,4);
    tsignal=tsig(*genptr);
}
void dust::sigcalc(int sig1, int x1, int y1, int type)
{
    if(y1+100>=y && y>=y1-100)
    {
        if(x1+25>=x && x>=x1-25)
        {
            if((sig1==tsignal)==true)
            {
                double dist=sqrt(((pow((x-x1),2.0))+(pow((y-y1),2.0))));
                strength=((type*163)/pow(dist,2.0));
            }
            else
            {
                strength=0;
            }
        }
        else
        {
            strength =0;
        }

    }
    else
    {
        strength=0;
    }
}
