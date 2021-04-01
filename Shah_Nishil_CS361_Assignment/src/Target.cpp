#include "Target.h"

Target::Target()
{
    //ctor
}

Target::~Target()
{
    //dtor
}

void Target::display()
{
    cout << "X coordinate " << x << endl;
    cout << "Y coordinate " << y << endl;
    cout << "Signal: " << signal << endl;
    cout << "Speed: " << speed << endl;
    cout << "Type: " << type << endl;
}

void Target::rsig(default_random_engine * genptr)
{
    uniform_real_distribution<double> sig(1,4);
    signal=sig(*genptr);
}

void Target::rspeed(default_random_engine * genptr)
{
    uniform_int_distribution<int> sp(8,12);
    speed=sp(*genptr);

}
void Target::rtype(default_random_engine * genptr)
{
    uniform_real_distribution<double> t(0,3);
    type=t(*genptr);
}

int Target::stype()
{
    if(signal==1)
    {
        int profile[4]={120,100,80,60};
        return profile[type];

    }
    else if(signal==2)
    {
        int profile[4]={10,8,6,4};
        return profile[type];
    }
    else if(signal==3)
    {
        int profile[4]={105,85,65,45};
        return profile[type];
    }
    else if(signal==4)
    {
        int profile[4]={90,70,50,30};
        return profile[type];
    }
}

void Target::tmove()
{
    x=x+speed;
}
