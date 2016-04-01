#include "Matrix.h"

template
  < class T >
void fillMatrix(Matrix <T> & m )
{
  int i, j;
  for ( i = 0; i < m.numRows(); i++ )
    m[i][0] = T();
  for ( j = 0; j < m.numCols(); j++ )
    m[0][j] = T();
  for ( i = 1; i < m.numRows(); i++ )
    for ( j = 1; j < m.numCols(); j++ )
    {
      m[i][j] = T(i * j);
    }
}
int main()
{
  try
  {
     Matrix < int > m(5,5);
     fillMatrix( m );
     cout << m;
     Matrix < double > M(8,10);
     fillMatrix( M );
     cout << M;
    
    
     Matrix<int> m2(-1,-1);  // IndexOutOfBounds Tests
     //Array<int> a1(-1);
     //Array<int> a2(10);
     //cout << a2[-1];
  }
  catch (IndexOutOfBoundsException &e)
  {
     cout << "\nIndex is out of bounds!\n";
  }
}
