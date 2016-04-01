#include <iostream>
using namespace std;
 
class String
  {
  public:
    /// Both constructors should construct
    /// from the parameter s
    String( const char * s = "");
    String( const String & s );
    String operator = ( const String & s );
    char & operator [] ( const int index );
    int length();
    int indexOf( char c ) const;
    bool operator == ( const String & s ) const;
    bool operator < ( const String & s ) const;
    /// concatenates this and s
    String operator + ( const String & s ) const;
    /// concatenates s onto end of this
    String operator += ( const String & s );
    void print( ostream & out );
    void read( istream & in );
    ~String();
  private:
    bool inBounds( int i )
    {
      return i >= 0 && i < length();
    }
    struct ListNode
    {
      char info;
      ListNode * next;
      ListNode(char newInfo, ListNode * newNext)
        : info( newInfo ), next( newNext )
      {
      }// HINT: some primitives you *must* write and use, recursion?
      static ListNode * stringToList(char *s);//Yes, I just fixed this
      static ListNode * copy(ListNode * L);
      static bool equal(ListNode * L1, ListNode * L2);
      static ListNode * concat(ListNode * L1, ListNode * L2);
      static int compare(ListNode * L1, ListNode * L2); // just fixed
      static int length(ListNode * L); // just added, O(N) so call rarely
       
    };
    ListNode * head; // no other data members!! - especially no len!
     
  static ListNode * stringToList(char *s)
  {
    int i = 0;
    int next = 1;
    char * temp = &s[next];
     
    if (s[i] == '\0')
        return nullptr;
    else
    {
        return new ListNode(s[i], stringToList(temp));
        ++i;
        ++next;
    }
    delete[] s;
    delete s;
    delete temp;
    temp = nullptr;
  }
   
  static ListNode * copy(ListNode * L)
  {
    return !L ? 0
              : new ListNode(L->info, copy(L->next));
  }
   
  static int length(ListNode * L)
  {
    int i = 0;
    for (ListNode * p = L; p != nullptr; p = p->next)
    {
        ++i;
    }
    return i;
  }
   
  static int compare(ListNode * L1, ListNode * L2)
  {
    if (length(L1) < length(L2))
    {
        return -1;
    }
    else if (length(L1) > length(L2))
    {
        return 1;
    }
    else
    {
        ListNode * one = L1;
        ListNode * two = L2;
         
        for (int i = 0; i < length(L1); ++i)
        {
            if (one->info < two->info)
            {
                return -1;
            }
            if (one->info > two->info)
            {
                return 1;
            }
            one = one->next;
            two = two->next;
        }
        return 0;
    }
  }
     
    static bool equal(ListNode * L1, ListNode * L2)
    {
        if (compare(L1, L2) == 0)
            return true;
        else
            return false;
    }
     
    static ListNode * concat(ListNode * L1, ListNode * L2)
    {
        return !L1 ? copy(L2)
                   : new ListNode(L1->info, concat(L1->next, L2));
    }
  };
  ostream & operator << ( ostream & out, String str );
  istream & operator >> ( istream & in, String & str );
  
 String::String( const char * s)
 {
    head = stringToList(const_cast<char*>(s));
 }
  
 String::String( const String & s )
 {
    head = copy(s.head);
 }
  
int String::length()
{
    return length(head);
}
 
 String String::operator = ( const String & s )
 {
	ListNode * temp;
	for (ListNode * p = head; p != nullptr;)
	{
	    temp = p;
            p = p->next;
	    delete temp;
        }
    	head = nullptr;
	temp = nullptr;
    head = copy(s.head);
    return *this;
 }
  
 char & String::operator [] ( const int index )
 {
    ListNode * temp;
    temp = head;
    for (int i = 0; i < index; ++i)
    {
        temp = head->next;
    }
    return temp->info;
 }
  
 bool String::operator == ( const String & s ) const
 {
    return equal(head, s.head);
 }
  
 bool String::operator < ( const String & s ) const
 {
    if (compare(head, s.head) == -1)
        return true;
    else
        return false;
 }
 int String::indexOf( char c ) const
 {
    int i = 0;
    ListNode * temp = head;
    for (; i < length(head); ++i)
    {
        if (c == temp->info)
        {
            return i;
        }
        temp = temp->next;
    }
    return -1;
 }
  
   /// concatenates s onto end of this
 String String::operator += ( const String & s )
 {	
	ListNode * temp;
	for (ListNode * p = head; p != nullptr;)
	{
	    temp = p;
            p = p->next;
	    delete temp;
        }
    	head = nullptr;
	temp = nullptr;
        head = concat(head, s.head);
        return *this;
 }
  
 String String::operator + ( const String & s ) const
 {
    String string(*this);
    return string += s;
 }
 
String:: ~String()
{
	
	ListNode * temp;
	for (ListNode * p = head; p != nullptr;)
	{
	    temp = p;
            p = p->next;
	    delete temp;
        }
    	head = nullptr;
	temp = nullptr;
}
  
 istream & operator >> ( istream & in, String & str )
 {
    str.read(in);
    return in;
 }
 void String::read( istream & in )
 {
    char buf[1000];
     
    in.getline(buf,1000); 
    String string(buf);
     
     
    	ListNode * temp;
	for (ListNode * r = head; r != nullptr;)
	{
	    temp = r;
            r = r->next;
	    delete temp;
        }
    temp = nullptr;
    head = nullptr;
    head = copy(string.head);
 }
  
 void String::print( ostream & out )
 {
    for (ListNode * p = head; p != nullptr; p = p->next )
      out << p->info;
       
      out << endl;
 }
  
  ostream & operator << ( ostream & out, String str )
  {
    str.print(out);
    return out;
  }
/*
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
}*/
