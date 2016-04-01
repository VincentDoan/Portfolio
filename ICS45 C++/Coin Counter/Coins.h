// Coins.h		///  The name of this file.
#include <iostream>
using namespace std;

const int CENTS_PER_QUARTER = 25, CENTS_PER_DIME = 10, CENTS_PER_NICKEL = 5;
class Coins
{
public:
  Coins( int q, int d, int n, int p );
  void depositChange( Coins c );
  bool hasSufficientAmount( int amount );
  Coins extractChange( int amount );
  void print( ostream & out );
private:
  int quarters, dimes, nickels, pennies;
};
ostream & operator << ( ostream & out, Coins & c );

Coins::Coins(int q, int d, int n, int p)
{
	quarters = q;
	dimes = d;
	nickels = n;
	pennies = p;
}

void Coins::depositChange(Coins c)
{
	quarters += c.quarters;
	dimes += c.dimes;
	nickels += c.nickels;
	pennies += c.pennies;
}

bool Coins::hasSufficientAmount( int amount )
{
	int total = quarters * 25 + dimes * 10 + nickels * 5 + pennies;
	
	if (total < amount)
	return false;
	else
	return true;
}

Coins Coins::extractChange( int amount )
{
	int q = 0;
	int d = 0;
	int n = 0;
	int p = 0;
	
	if (hasSufficientAmount(amount))
	{
		while (quarters > 0 && amount >= 25)
		{
			amount -= 25;
			q = q+1;
			--quarters;
		}
		
		while (dimes > 0 && amount >= 10)
		{
			amount -= 10;
			d = d+1;
			--dimes;
		}
		
		while (nickels > 0 && amount >= 5)
		{
			amount -= 5;
			n = n+1;
			--nickels;
		}
		
		while (pennies > 0 && amount >= 1)
		{
			amount -= 1;
			p = p+1;
			--pennies;
		}	
	}
	
	Coins coins(q, d, n, p);
	//Coins coins(1, 1, 1, 1);
	return coins;
}

void Coins::print( ostream & out )
{
	int amount;
	amount = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1;
	out << amount << " cents";
}


ostream & operator << ( ostream & out, Coins & c)
{
	c.print(out);
	return out;
}
