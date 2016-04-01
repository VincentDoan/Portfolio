#include <iostream>
using namespace std;

class Shape {
public:
  Shape() {};
  virtual ~Shape(){};
  virtual double perimeter() = 0;
  virtual double area() = 0;

protected:
	double shapeArea = 0.0;
	double shapePerimeter = 0.0;
};
class Circle : public Shape {
public:
  Circle(double radius = 1.0)
  {
	this->radius = radius;
  }
  virtual double area()
  {
	cout << "I'm a circle and my area is: ";
  	return shapeArea = radius * radius * PI;
  }
  
  virtual double perimeter()
  {
	cout << "I'm a circle and my perimeter is: ";
  	return shapePerimeter = radius * 2 * PI;
  }

protected:
	int sides = 0;
	double shapeArea = 0.0;
	double shapePerimeter = 0.0;
private:
	double radius = 0.0;
	const double PI = 3.14159;
};
class Rectangle : public Shape {
public:
   Rectangle(double sideLength1 = 1.0, double sideLength2 = 1.0)
  {
	this->sideLength1 = sideLength1;
	this->sideLength2 = sideLength2;
  }
  virtual double area()
  {
	cout << "I'm a rectangle and my area is: ";
  	return shapeArea = sideLength1 * sideLength2;
  }
  virtual double perimeter()
  {
	cout << "I'm a rectangle and my perimeter is: ";
  	return shapePerimeter = sideLength1 * 2 + sideLength2 * 2;
  }
protected:
	int sides = 4;
	double shapeArea = 0.0;
	double shapePerimeter = 0.0;
private:
	double sideLength1 = 0.0;
	double sideLength2 = 0.0;
};

class Triangle : public Shape {
public:
  Triangle(double base = 1.0, double height = 1.0)
  {
	this->base = base;
	this->height = height;
  }
  virtual double area()
  {
	cout << "I'm an equilateral triangle and my area is: ";
  	return shapeArea = 0.5 * base * height;
  }
  
  virtual double perimeter()
  {
	cout << "I'm an equilateral triangle and my perimeter is: ";
  	return shapePerimeter = base * 3;
  }
protected:
	int sides = 3;
	double shapeArea = 0.0;
	double shapePerimeter = 0.0;
private:
	double base = 0.0;
	double height = 0.0;
};

static void call(Shape * s[], int size)
{
	for (int i = 0; i < size; ++i)
	{
		cout << s[i]->area() <<  "     ";
		cout << s[i]->perimeter() << endl;
	}
	for (int i = 0; i < size; ++i)
	{
		delete s[i];
	}
}

/*
int main() 
{  
	Shape * s[] = {new Circle, new Rectangle, new Triangle, new Circle(4), new Rectangle(2, 3), new Triangle(5, 4)}; //create array
	
	call(s, 6); //use call static function takes in array and size of array
	
	return 0;
}
*/
