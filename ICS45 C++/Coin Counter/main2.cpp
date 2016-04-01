// CoinMain.cpp  /// The name of this file
#include "Coins.h"
#include <iostream>
using namespace std;

const int CENTS_FOR_CHIPS = 68;
int main()
{
///  The first line creates a Coins object called 'pocket.'
  Coins pocket(5, 3, 6, 8);
  Coins piggyBank(50, 50, 50, 50);
  Coins piggyBankChange(0, 0, 0, 0);
  Coins sofaChange(1, 1, 1, 1);
  cout << "I started with " << pocket << " in my pocket" << endl;
///  This line creates a Coins object called payForCandy and initializes it.
  Coins payForChips = pocket.extractChange( CENTS_FOR_CHIPS);
  //Coins payForCandy(10, 10, 10, 10);
  cout << "I bought a bag of chips for " << CENTS_FOR_CHIPS
     << " cents using " << payForChips << endl;
  cout << "I have " << pocket << " left in my pocket" << endl;
  piggyBankChange = piggyBank.extractChange(100);
  pocket.depositChange(piggyBankChange);
  cout << "PiggyBank change/deposit: " << piggyBankChange << "\nPiggyBank total is: " << piggyBank << "\nI now have " << pocket << " now in my pocket\n";
  cout << "I found " << sofaChange << " in the sofa and have deposited it in my PiggyBank\n";
  piggyBank.depositChange(sofaChange);
  cout << "My PiggyBank now has: " << piggyBank << endl;
  return 0;
}
