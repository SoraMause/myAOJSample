#include <stdio.h>
#include <math.h>
#include <string.h>

int main()
{
  int n;
  double ss, s;
  double average = 0.0;
  double data[1001];

  while( scanf("%d",&n) ) {
    if ( n == 0 ) break;

    for ( int i = 0; i < n; i++ ){
      scanf(" %lf", &data[i] );
      average += data[i];
    }

    average /= n;

    for ( int i = 0; i < n; i++ ){
      ss += (data[i] - average) * (data[i] - average); 
    }

    ss /= n;

    s = sqrt(ss);

    printf( "%10.10lf\n", s );

    average = 0.0;
    ss = 0.0;
    s = 0.0;

  }

  return 0;
}