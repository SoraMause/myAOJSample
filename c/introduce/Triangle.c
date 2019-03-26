#include <stdio.h>
#include <math.h>
#define _USE_MATH_DEFINES

int main()
{
  double a, b, deg;
  double S, L, h;
  
  scanf( "%lf %lf %lf",&a, &b, &deg );

  S = 1 / 2.0 * a * b * sin(deg*M_PI/ 180.0);
  L =  a + b + sqrt(a*a + b*b - 2.0*a*b*cos(deg*M_PI/ 180.0) );
  h = b * sin(deg*M_PI/ 180.0);

  printf( "%10.10lf %10.10lf %10.10lf\n",S, L, h );
  return 0;
}