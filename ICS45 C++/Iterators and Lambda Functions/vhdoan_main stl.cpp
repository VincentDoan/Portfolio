#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <vector>
using namespace std;





// DUY this is updated after hearing that we were to do every bit in STL
// the example file does not have the file extension attached



int main()
{

  string line = "TEST";
  map<string, int> mapper, bannedmap;
  vector<string> v;
  set<string> setter = {"a", "an", "or", "the", "and", "but"};
  ifstream myfile ("example");
 
  for_each(istream_iterator<string>(myfile), // start of source
      istream_iterator<string>(), // end of source, EOF
      [&v] (string s) {v.push_back(s);} );

  for_each(begin(v), end(v), // start of source // end of source, EOF
      [&mapper] (string s) {++mapper[s];} );

 cout << "Prior to the set of banned words: " << endl;
 for (auto E : mapper)
     cout << E.first <<  ": " << E.second << endl;

 for_each(begin(v), end(v), // start of source // end of source, EOF
      [&] (string s) 
      {
          for (auto F : setter)
          {
             auto it = find(begin(v), end(v), F);
             if (it != end(v))
                v.erase(it);
          };
        
      } );

for_each(begin(v), end(v), 
      [&bannedmap] (string s) {++bannedmap[s];} );

cout << "After the set of banned words:\n";
for (auto E : bannedmap)
     cout << E.first <<  ": " << E.second << endl;


  // PART TWO
  ifstream intList ("IntList");
  ofstream odd ("odd");
  ofstream even ("even");
  set<int> s;
  set<int> s2;
  copy(istream_iterator<int>(intList), istream_iterator<int>(), inserter(s, begin(s)));
  copy_if(begin(s), end(s), ostream_iterator<int>(odd, "\n"), [&] (int i) {return (i % 2 != 0);});
  copy_if(begin(s), end(s), ostream_iterator<int>(even, "\n"), [&] (int i) {return (i % 2 == 0);});

  return 0;
}
