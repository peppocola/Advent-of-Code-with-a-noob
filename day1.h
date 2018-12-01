#ifndef DAY1_H
#define DAY1_H

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <map>

using namespace std;

int day1_part1(){

  vector<int> vet;
  int n;
  ifstream OpenFile("/home/peppocola/Scrivania/file");

    while(!OpenFile.eof())
    {
      OpenFile>>n;
      vet.push_back(n);
    }
    OpenFile.close();

//here we have a vector filled with all numbers that where on the file

  int i=0;
  int checksum=0;
  while(i<vet.size()-1){
    checksum+=vet[i];
    i++;
  }

//gg ez

  cout<<"checksum is="<<checksum<<endl;

}

int day1_part2(){

  map<int,bool> dict;
  vector<int> vet;
  int n;
  ifstream OpenFile("/home/peppocola/Scrivania/file");

  while(!OpenFile.eof()){
      OpenFile>>n;
      vet.push_back(n);
    }

  OpenFile.close();

  int freq=0;
  int i=0;
  dict.insert(pair<int,bool>(0,1));
  while(true){
    freq=freq+vet[i%(vet.size()-1)];
    i++;
    if(dict.insert(pair<int, bool>(freq, true)).second==false){
      cout<<freq;
      break;
    }

  }

}

#endif
