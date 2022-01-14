#include <bits/stdc++.h>

using namespace std;

int randomNumberGenerator(){
    int temp=99;
    time_t theTime = time(NULL);
    struct tm *aTime = localtime(&theTime);
    int hour=aTime->tm_hour;
    int min=aTime->tm_min;
    int second=aTime->tm_sec;
    int monthDay=aTime->tm_mday;
    int randomNumber=((hour+1)*(second+1)*(monthDay+1))%temp;
    return randomNumber+1;
}

int main()
{
   int randomNumber=randomNumberGenerator();
   cout<<randomNumber;
   
   return 0;
}
