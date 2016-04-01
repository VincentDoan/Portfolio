#include "CS 45C Homework 5.h"

int main() 
{  
	Shape * s[] = {new Circle, new Rectangle, new Triangle, new Circle(4), new Rectangle(2, 3), new Triangle(5, 4)}; //create array
	
	call(s, 6); //use call static function takes in array and size of array
	
	return 0;
}
