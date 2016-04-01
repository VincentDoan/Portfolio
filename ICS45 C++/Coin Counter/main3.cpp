// CoinMain.cpp  /// The name of this file
#include "Coins.h"
#include <iostream>
using namespace std;

int main()
{
///  The first line creates a Coins object called 'pocket.'
  Coins myChange(0, 0, 0, 0);
  char answer = 'y';
  char command = ' ';
  cout << "Welcome to your bank account!\n"
	   << "You account balance is: " << myChange << endl;
	   while (answer == 'y')
	   {
		   cout << "You can (d)eposit change, (e)xtract change, or (p)rint your balance.\n";
		   cout << "What would you like to do? ";
		   cin >> command;
		   
		   switch(command)
		   {
			   case 'd':
			   {
				    int change = 0;
				   
					cout << "How much change would you like to deposit? ";
					cin >> change;
					Coins newChange(0, 0, 0, change);
					myChange.depositChange(newChange);
					cout << endl;
			   }
			   break;
			   
			   case 'e':
			   {
					int change = 0;
					
					cout << "How much change would you like to extract? ";
					cin >> change;
					myChange.extractChange(change);
					cout << endl;
			   }
			   break;
			   
			   case 'p':
			   {
				   Coins myCoins = myChange;
				   cout << "Your total balance is: " << myCoins << endl << endl;
			   }
			   break;
			   
			   default: 
					cout << "ERROR ERROR!\n";
		   
		 
	   }
	     cout << "If you like to continue enter y: ";
		 cin >> answer;
		 cout << endl;
   }
   
  return 0;
}
