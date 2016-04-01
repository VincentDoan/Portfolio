#include <iostream>
#include <iomanip>
#include <cassert>
using namespace std;
 
class IndexOutOfBoundsException : public exception
{
};
template
   <class Element>
 
class Array
{
private:
  int len;
  Element * buf;
public:
  Array( int newLen )
    : len( newLen ), buf( new Element[newLen] )
  {
	if (newLen < 0)
	   throw IndexOutOfBoundsException();
  }
  Array( Array & l )
    : len( l.len ), buf( new Element[l.len] )
  {
    for ( int i = 0; i < l.len; i++ )
      buf[i] = l.buf[i];
  }
  int length()
  {
    return len;
  }
  Element & operator [] ( int i )
  {
    //assert( 0 <= i && i < len );
    if (i < 0 || i > len)
       throw IndexOutOfBoundsException();
    return buf[i];
  }
  void print( ostream & out )
  {
    for (int i = 0; i < len; i++)
      out << setw(5) << buf[i];
  }
  friend ostream & operator << ( ostream & out, Array & a )
  {
    a.print( out );
    return out;
  }
  friend ostream & operator << ( ostream & out, Array * ap )
  {
    ap->print( out );
    return out;
  }
  // note the overloading of operator << on a pointer as well
 
  ~Array()
  {
    delete[] buf;
  }
};