#ifndef HOMEBASE_H
#define HOMEBASE_H
#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include "Flechettes.h"

using namespace std;

class Homebase
{
public:
    Homebase();
    virtual ~Homebase();
    void readFlech(int x1, int y1, int i);


protected:

private:
    int x;
    int y;
    int id;
};

#endif // HOMEBASE_H
