#include <stdio.h>
#include <string.h>

int main()
{
  char s[100];
  char temp;
  char p[100];
  int string_length = 0;
  unsigned char flag = 0;

  scanf( " %s", s );
  scanf( " %s", p );

  string_length = strlen(s) - 1;

  for ( int i = 0; i <= string_length; i++ ){
    temp = s[string_length];
    for ( int j = string_length; j > 0; j-- ){
      s[j] = s[j-1];
    }

    s[0] = temp;

    if ( strstr( s, p ) != NULL ) {
      flag = 1;
      printf( "Yes\n" );
      break;
    }
  }

  if ( !flag ) printf( "No\n" );

  return 0;
}