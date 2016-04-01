#include "ICS45C HW4.h"

int main() 
{
    String string1("YO BRO"); //Constructor tests
    cout << string1;
    String string2(string1);
    cout << string2;
     
    cout << string2.length() << endl; //Length test
     
    String string3("Wut"); //operator = test
    string2 = string3;
    cout << string2;
     
    cout << string2[0] << " " << string2[1] << endl; //operator[] test
     
    cout << (string2 == string3) << " " << (string1 == string2) << endl; //operator == test
     
    String string4("Wuu");
    cout << (string2 < string3) << " " << (string1 < string2) << " " << (string2 < string1) << " " << (string2 < string4) << endl; //operator < test
     
    cout << string2.indexOf('W') << " " << string2.indexOf('u') << " " << string2.indexOf('t') << " " << string2.indexOf('Z') << endl; //indexOf test
     
    cout << (string2 += string3); //operator += test
     
    string1 = string3 + string4;
    cout << string1; //operator + test
     
    cin >> string1;   //read test
    cout << string1;
    return 0;
}
