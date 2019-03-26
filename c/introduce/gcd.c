#include <stdio.h>

int gcd( int x, int y )
{
  int temp = 0;

  if ( x < y ) {
    temp = x;
    x = y;
    y = temp;
  }

  if ( y < 1 ) return 1;

  if ( x % y == 0 ) return y;
  else gcd( y, x % y );

}

int main()
{
  int x, y;
  int result = 0;

  scanf("%d %d",&x, &y);

  result = gcd(x, y);
  printf("%d\n",result);
  return 0;
}