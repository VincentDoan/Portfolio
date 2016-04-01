#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
using namespace std;





// DUY since I was using Linux to code this the file name does not have a .txt extension just wanted to give you a heads up if you're checking. THANKS.
















int main()
{

  string line;
  map<string, int> mapper;
  set<string> setter = {"a", "an", "or", "the", "and", "but"};
  ifstream myfile ("example");
 
  if (myfile.is_open())
  {
     
    while(myfile >> line)
    {
      for (auto E : setter)
      {
         if (line == E)
         {
         }
         else
         {
            if(mapper.find(line) == mapper.end())
            {
               cout << "Added: |" << line << "| to map!\n";
               mapper[line] = 1;
            }
            else
            {
               cout << "INCREMENTED |" << line << "| the duplicate!\n";
               mapper[line] += 1;
            }
            break;
         }
      }
    }
    myfile.close();
  }

  else 
    cout << "The file has failed to open!\n"; 

  
   for (auto E : mapper)
   {
     for (auto F : setter)
     {
        if (E.first == F)
           mapper.erase(E.first);
     }
   }

   for (auto E : mapper)
   {
     for (auto F : setter)
     {
        if (E.first == F)
           mapper.erase(E.first);
     }
   }
  for (auto E : mapper)
     cout << E.first <<  ": " << E.second << endl;

  // PART TWO
  //int number;
  ifstream intList ("IntList");
  ofstream odd ("odd");
  ofstream even ("even");
  set<int> s;
  set<int> s2;
  copy(istream_iterator<int>(intList), istream_iterator<int>(), inserter(s, begin(s)));
  copy_if(begin(s), end(s), ostream_iterator<int>(odd, "\n"), [&] (int i) {return (i % 2 != 0);});
  copy_if(begin(s), end(s), ostream_iterator<int>(even, "\n"), [&] (int i) {return (i % 2 == 0);});
 // for_each(begin(s), end(s), [&] (string s) );
  /*for (auto e : s)
     cout << e << endl;*/

  return 0;
}
