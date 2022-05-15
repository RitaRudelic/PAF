#include <iostream>
#include <HarmonicOscillator.h>


int main(){
    
    HarmonicOscillator h1(15, 0.2, 0.4, 0);
    h1.move(0.02,10);
    

    ofstream myfile;
    myfile.open ("e.txt");
    for(int i=0;i < h1.xl.size();i++){
        myfile<<h1.xl[i];
        myfile<<" ";
    };
    myfile<< "\n";

    for(int i=0;i < h1.vl.size();i++){
        myfile<<h1.vl[i];
        myfile<<" ";
    };
    myfile<< "\n";

    for(int i=0;i < h1.al.size();i++){
        myfile<<h1.al[i];
        myfile<<" ";
    };
    myfile<< "\n";
    for(int i=0;i < h1.tl.size();i++){
        myfile<<h1.tl[i];
        myfile<<" ";
    };
    myfile.close();

    return 0;

}