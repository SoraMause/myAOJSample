#include <stdio.h>
#include <ctype.h>

int main(void)
{
  int a[26] = { 0 };       // アルファベット（'a'-'z'）は26文字
  int ch, i;

  //input
  while ((ch = getchar()) != EOF) {
    //走査
    if (islower(ch)) {
      a[ch - 'a']++;
    }
    
    if (isupper(ch)) {
      a[ch - 'A']++;
    }
  }

  //output
  for (i = 0; i < 26; i++) {
    printf("%c : %d\n", i + 'a', a[i]); 
  }
  return 0; 
}