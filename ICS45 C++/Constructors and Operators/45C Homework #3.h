 #include <iostream>
 using namespace std;
 
 class String
  {
  public:
    /// Both constructors should construct
    /// this String from the parameter s
    String( const char * s = "");
    String( const String & s );
    String operator = ( const String & s );
    char & operator [] ( int index );
    int size();
    int maxSize();
    String reverse(); // does not modify this String
    int indexOf( char c );
    int indexOf( String pattern );
    bool operator == ( String s );
    bool operator != ( String s );
    bool operator > ( String s );
    bool operator < ( String s );
    bool operator <= ( String s );
    bool operator >= ( String s );
    /// concatenates this and s to return result
    String operator + ( String s );
    /// concatenates s onto end of this
    String operator += ( String s ); 
    void print( ostream & out );
    void read( istream & in );
    ~String();
  private:
    bool inBounds( int i )
    {
      return i >= 0 && i < maxLength;
    }
    char * buf;
    int len = 0;
    int maxLength = 1000;
  };
  ostream & operator << ( ostream & out, String str );
  istream & operator >> ( istream & in, String & str );

	String::String( const char * s)
	{
		int size = 0;
		for (int i = 0; s[i] != '\0'; ++i)
		{
			size++;
		}
		//cout << "Constructor: " << size << endl;
		if (inBounds(size))
		{
			buf = new char[1000];
			for (int i = 0; s[i] != '\0'; ++i)
			{
				buf[i] = s[i];
				len++;
				if (s[i+1] == '\0')
				{
					buf[i+1] = '\0';
				}
			}
		}
		else
		{
			cout << "Constructor: TOO BIG!\n";
			buf = new char[size * 2];
			maxLength = size * 2;
			
			for (int i = 0; s[i] != '\0'; ++i)
			{
				buf[i] = s[i];
				len++;
				
				if (s[i+1] == '\0')
				{
					buf[i+1] = '\0';
				}
			}
		}
	
	}
    String::String( const String & s )
	{
		//cout << "Copy Constructor: " << s.len << endl;
		if (inBounds(s.len))
		{
			buf = new char[maxLength];
			for (int i = 0; s.buf[i] != '\0'; ++i)
			{
				buf[i] = s.buf[i];
				len++;
				if (s.buf[i+1] == '\0')
				{
					buf[i+1] = '\0';
				}
			}
		}
		else
		{
			cout << "Copy Constructor: TOO BIG!\n";
			buf = new char[s.maxLength * 2];
			maxLength = s.maxLength * 2;
			
			for (int i = 0; s.buf[i] != '\0'; ++i)
			{
				buf[i] = s.buf[i];
				len++;
				if (s.buf[i+1] == '\0')
				{
					buf[i+1] = '\0';
				}
			}
		}
	}
   String String::operator = ( const String & s )
	{
		if (inBounds(s.len))
		{
			for (int i = 0; s.buf[i] != '\0'; ++i)
			{
				buf[i] = s.buf[i];
				if (s.buf[i+1] == '\0')
				{
					buf[i+1] = '\0';
				}
			}
			len = s.len;
		}
		else
		{
			cout << "Assignment Operator: TOO BIG!\n";
			delete[] buf;
			buf = new char[s.maxLength *2];
			maxLength = s.maxLength * 2;
			for (int i = 0; s.buf[i] != '\0'; ++i)
			{
				buf[i] = s.buf[i];
				if (s.buf[i+1] == '\0')
				{
					buf[i+1] = '\0';
				}
			}
			len = s.len;
		}
		return buf;
	}
    char & String::operator [] ( int index )
	{
		return buf[index];
	}
    int String::size()
	{
		return len;
	}
	int String::maxSize()
	{
		return maxLength;
	}
    String String::reverse() // does not modify this String
	{
		String reverse;
		reverse.len = len;
		int index = 0;
		
		for (int i = len - 1; i > -1; --i)
		{
			reverse.buf[index] = buf[i];
			index++;
		}
		reverse.buf[reverse.size()] = '\0';
		return reverse;
	}
    int String::indexOf( char c )
	{
		for (int i = 0; i < len; ++i)
		{
			if (c == buf[i])
			{
				return i;
			}
		}
		return -1;
	}
    int String::indexOf( String pattern )
	{
		int m = pattern.size();
		int n = len;
		if (pattern.size() > len)
			return -1;
		for (int i = 0; i <= n-m; ++i)
		{
			for (int p = 0; p < m; ++p)
			{
				if (buf[i+p] != pattern.buf[p])
					break;
				if (p == m - 1)
					return i;
			}
		}
		return -1;
	}
    bool String::operator == ( String s )
	{
		if (s.len != len)
			return false;
		for (int i = 0; s.buf[i] != '\0'; ++i)
		{
			if (buf[i] != s.buf[i])
				return false;
		}
			return true;
	}
	
    bool String::operator != ( String s )
	{
		if (s.len != len)
			return true;
		for (int i = 0; s.buf[i] != '\0'; ++i)
		{
			if (buf[i] != s.buf[i])
				return true;
		}
			return false;
	}
    bool String::operator > ( String s )
	{
		if (len < s.len)
			return false;
		
		if (len > s.len)
			return true;
		
		for (int i = 0; i < len; ++i)
		{
			if (buf[i] - s.buf[i] < 0)
				return false;
			if (buf[i] - s.buf[i] > 0)
				return true;
			if (i + 1 == len)
				return false;
		}
	}
   bool String::operator < ( String s )
   {
   		if (len > s.len)
			return false;
		
		if (len < s.len)
			return true;
		
		for (int i = 0; i < len; ++i)
		{
			if (buf[i] - s.buf[i] > 0)
				return false;
			if (buf[i] - s.buf[i] < 0)
				return true;
			if (i + 1 == len)
				return false;
		}
   }
   bool String::operator <= ( String s )
   {
    	if (len > s.len)
			return false;
		
		if (len < s.len)
			return true;
		
		for (int i = 0; i < len; ++i)
		{
			if (buf[i] - s.buf[i] > 0)
				return false;
			if (buf[i] - s.buf[i] < 0)
				return true;
			if (i + 1 == len)
				return true;
		}
   }
   bool String::operator >= ( String s )
   {
   		if (len < s.len)
			return false;
		
		if (len > s.len)
			return true;
		
		for (int i = 0; i < len; ++i)
		{
			if (buf[i] - s.buf[i] < 0)
				return false;
			if (buf[i] - s.buf[i] > 0)
				return true;
			if (i + 1 == len)
				return true;
		}
   }
    /// concatenates this and s to return result
   String String::operator + ( String s )
   {
   		char * newBuf = new char[(maxLength + s.maxLength) * 2];
    		for (int i = 0; buf[i] != '\0'; ++i)
   			{
   				newBuf[i] = buf[i];
   			}
    		
    		for (int i = 0; s.buf[i] != '\0'; ++i)
   			{
   				newBuf[len] = s.buf[i];
   				if (s.buf[i+1] == '\0')
   					buf[len+1] = '\0';
   				len++;
   			}
    	return newBuf;
   }
    
    /// concatenates s onto end of this
    String String::operator += ( String s )
    {
    	//cout << "operator+ len: " << s.len << " maxLength: " << s.maxLength << endl;
    	if (inBounds(s.len))
    	{
    		for (int i = 0; s.buf[i] != '\0'; ++i)
   			{
   				buf[len] = s.buf[i];
   				if (s.buf[i+1] == '\0')
   					buf[len+1] = '\0';
   				len++;
   			}
    	}
    	else
    	{
    		cout << "+= operator: TOO BIG!\n";
    		char * oldBuf = buf;
    		buf = new char[s.maxLength * 2];
    		maxLength = s.maxLength * 2;
    		
    		for (int i = 0; oldBuf[i] != '\0'; ++i)
   			{
   				buf[i] = oldBuf[i];
   			}
   			
    		for (int i = 0; s.buf[i] != '\0'; ++i)
   			{
   				buf[len] = s.buf[i];
   				if (s.buf[i+1] == '\0')
   					buf[len+1] = '\0';
   				len++;
   			}
   			oldBuf = nullptr;
   			delete[] oldBuf;
    	}
    	return buf;
    }
    void String::print( ostream & out )
    {
    	out << buf;
    }
    void String::read( istream & in )
    {
		String temp = "";
		char array[1000];
		while (in >> array)
		{
			temp += String(input);
		}
  	}
  
  String::~String()
  {
  	len = 0;
  	buf = nullptr;
  	delete[] buf;
  }
   
   
  ostream & operator << ( ostream & out, String str )
  {
  	str.print(out);
  	return out;
  }
  istream & operator >> ( istream & in, String & str )
  {
  	str.read(in);
  	return in;
  }