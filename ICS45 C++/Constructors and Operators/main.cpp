 #include <iostream>
 #include "45C Homework #3.h"
 using namespace std;
 
   
int main() {
	String string("Yo Bro"); //constructor test

	cout << string << endl; //print test

	String string2(string); //copy constructor test
	cout << string2 << endl;

	String string3("What the @%#%!"); //assignment operator test
	cout << string3 << " " << string3.size() << endl;
	string3 = string;
	cout << string3 << endl;
	
	cout << string3[0] << endl; //operator[] test
	
	cout << string3.size() << endl; //size test
	
	cout << string3.reverse() << endl; //reverse test
	
	cout << string3.indexOf('B') << endl << string3.indexOf('r') << endl << string3.indexOf('C') << endl; //indexOf(char c) test of original string3 before reverse
	cout << string3.reverse().indexOf('B') << endl; //indexOf(char c) after reverse
	
	cout << string3.indexOf("Bro") << endl << string3.indexOf("r") << endl << string3.indexOf("lolwut") << endl << string3.indexOf("BYAAHHHHAHHHHHHH") << endl; //indexOf(String pattern) test
	
	cout << (string3 == string) << endl << (string == string3) << endl << (string3 == "ayyy") << endl; //operator== tests
	String string4(string3.reverse());
	cout << string4 << " " << string4[0] << " " << (string3 == string4) << endl;
	cout << (string3 == "orB oY") << " " << (string3 == "Yo Bro") << endl; 
	
	cout << (string3 != "orB oY") << " " << (string3 != "Yo Bro") << endl; //operator != test
	
	cout << (string3 > string3) << " " << (string3 > string3.reverse()) << " " << (string3 > "ORB YO") << " " << (string3 > "aaaa") << " " << (string3 > "Aa Aaa") << endl; //operator > test
	
	cout << (string3 < string3) << " " << (string3 < string3.reverse()) << " " << (string3 < "ORB YO") << " " << (string3 < "aaaa") << " " << (string3 < "Aa Aaa") << endl; //operator < test
	
	cout << (string3 >= string3) << " " << (string3 >= string3.reverse()) << " " << (string3 >= "ORB YO") << " " << (string3 >= "aaaa") << " " << (string3 >= "Aa Aaa") << endl; //operator >= test
	
	cout << (string3 <= string3) << " " << (string3 <= string3.reverse()) << " " << (string3 <= "ORB YO") << " " << (string3 <= "aaaa") << " " << (string3 <= "Aa Aaa") << endl; //operator <= test
	
	String something;
	something = string3 + string4;
	cout << something << endl; //operation + test
	
	string3 += " ";
	string3 += string3;
	cout << string3 << " " << string3.size() << endl; //operation += test
	
	cout << "Enter a string in for the read test: ";
	cin >> string3; //read test
	cout << endl << string3 << " " << string3.size() << endl;
	
	String big("123456789");
	cout << "big size: " << big.size() << " big maxSize: " << big.maxSize() << endl;
	char huge[1000];
	cin >> huge;
	String fat(huge); //Copy Constructor size check
	cout << "Fat: " << fat.size() << " Max Size: " << fat.maxSize() << endl;

	big += huge; //+= operator size check
	cout << big << endl << "Big len: " << big.size() << " maxSize: " << big.maxSize() << endl;
	
	String oneK("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
	cout << "oneK len: " << oneK.size() << " oneK maxSize: " << oneK.maxSize() << endl; //Constructor size check
	
	String read; //read size check
	cin >> read;
	cout << "read len: " << read.size() << " read maxSize: " << read.maxSize() << endl;
	cout << read << endl;
	cout << "read len: " << read.size() << " maxSize: " << read.maxSize();
	return 0;
}