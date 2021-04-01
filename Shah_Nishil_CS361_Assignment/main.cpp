#include <iostream>
#include <list>
#include <random>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include "dust.h"
#include "Flechettes.h"
#include "Target.h"
#include "Homebase.h"

using namespace std;

int main()
{
    default_random_engine * genptr;
    genptr = new default_random_engine(time(NULL));
    list<dust>Mydust;
    list<dust>::iterator ditr;
    dust * dptr;
    list<Flechettes>Myflech;
    list<Flechettes>::iterator fitr;
    list<Homebase>Myhome;
    list<Homebase>::iterator hitr;
    Flechettes * fptr;
    Target * tptr;
    Homebase * hptr;
    int counter=1;
    int counter2=1;
    int input;
    int input2;
    int j=0;
    int type;
    fstream fout;
    fstream fout2;
    fstream fout3;
    string prefix= "tx_ty_data.txt";
    string FileID;
    string PngName;
    fout.open("dx_dy_data.txt",ios::out);
    fout2.open("fx_fy_data.txt",ios::out);
    fout3.open("tx_ty_data.txt", ios::out);
    cout << "How many dust particles do you want to simulate? " ;
    cin >> input;
    cout << "How many Flechettes do you want to simulate? " ;
    cin >> input2;

    hptr= new Homebase();
    tptr= new Target();
    tptr->Setx(0);
    tptr->Sety(100);
    tptr->rsig(genptr);
    tptr->rspeed(genptr);
    tptr->rtype(genptr);
    type=tptr->stype();
    tptr->display();
    fstream command;
    fstream command2;
    fstream command3;
    command.open("command.txt", ios::out);

    command << "set xlabel \" x location \" " << endl;
    command << "set ylabel \" y location \"" << endl;
    command << "set xrange [0:200]" << endl;
    command << "set yrange [0:200]" << endl;
    command << "set view equal xyz" << endl;
    command << "set terminal png" << endl;
        command2.open("command2.txt", ios::out);

    command2 << "set xlabel \" x location \" " << endl;
    command2 << "set ylabel \" y location \"" << endl;
    command2 << "set xrange [0:200]" << endl;
    command2 << "set yrange [0:200]" << endl;
    command2 << "set view equal xyz" << endl;
    command2 << "set terminal png" << endl;
        command3.open("command3.txt", ios::out);

    command3 << "set xlabel \" x location \" " << endl;
    command3 << "set ylabel \" y location \"" << endl;
    command3 << "set xrange [0:200]" << endl;
    command3 << "set yrange [0:200]" << endl;
    command3<< "set view equal xyz" << endl;
    command3 << "set terminal png" << endl;

    for(j=0; j<input; j++)
    {
        dptr= new dust(counter);
        dptr->randomx(genptr);
        dptr->randomy(genptr);
        dptr->rtsignal(genptr);
        Mydust.push_back(*dptr);
        counter++;
    }

    for(int i=0; i<input2; i++)
    {
        fptr= new Flechettes(counter2);
        ditr=Mydust.begin();
        while(ditr!=Mydust.end())
        {
            dptr=&(*ditr);
            fptr->addDust(dptr);
            ditr++;
        }
        fptr->randomx(genptr);
        fptr->randomy(genptr);
        Myflech.push_back(*fptr);
        counter2++;
    }
    ditr= Mydust.begin();
    while(ditr!=Mydust.end())
    {
        ditr->display();
        ditr++;
    }
    fitr=Myflech.begin();
    while(fitr!=Myflech.end())
    {
        fitr->display();
        fitr->checkdust();
        fitr++;
    }

    while((tptr->Getx())<=200)
    {
        counter=0;
        ditr=Mydust.begin();
        while(ditr!=Mydust.end())
        {
            ditr->sigcalc((tptr->Getsignal()),(tptr->Getx()),(tptr->Gety()), type);
            ditr++;
        }
        ditr=Mydust.begin();
        while(ditr!=Mydust.end())
        {
            int x= ditr->Getx();
            int y= ditr->Gety();
            if(ditr!=Mydust.begin()){fout<<endl;}
            fout<<x<<" "<<y;
            ditr++;
        }
        fout.close();
        fitr=Myflech.begin();
        while(fitr!=Myflech.end())
        {
            hptr->readFlech((fitr->Getx()),(fitr->Gety()),(fitr->Getid()));
            int x= fitr->Getx();
            int y= fitr->Gety();
            if(fitr!=Myflech.begin()){fout2<<endl;}
            fout2<<x<<" "<<y;
            fitr++;
        }
        fout2.close();
        int x=tptr->Getx();
        int y=tptr->Gety();
        if((tptr->Getx())!=0){fout3<<endl;}
        fout3<<x<<" " << y;
        FileID= to_string(counter);
        PngName=prefix +"_" +FileID +".png";
        command3<<"set output \""<<PngName.c_str()<<"\"  "<<endl;
        command3<<"plot \"tx_ty_data.txt\" ps var pt 1 with points " << endl;
        counter++;
        tptr->tmove();
       // hptr->makefile();
    }
    fout3.close();
    command<<"set output \"dx_dy_data.png\" "<<endl;
    command<<"plot \"dx_dy_data.txt\"  ps var pt 2  with points "<<endl;
    command2<<"set output \" fx_fy_data.png\" "<<endl;
    command2<<"plot \"fx_fy_data.txt\"  ps var pt 1  with points "<<endl;




    command<<"pause -1"<<endl;
    command.close();
    system("gnuplot command.txt");

    command2<<"pause -1"<<endl;
    command2.close();
    system("gnuplot command2.txt");

    command3<<"pause -1"<<endl;
    command3.close();
    system("gnuplot command3.txt");
    return 0;
}

