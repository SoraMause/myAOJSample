#include <stdio.h>
 
int rot[5][7] = {
{0,1,2,3,4,5,6},{0,2,6,3,4,1,5},{0,4,2,1,6,5,3},{0,3,2,6,1,5,4},{0,5,1,3,4,6,2}};
int assign[7];      // サイコロの1～6の各面に割り当てる数字
int tr['Z'];
 
void dice_init(int *a)
{
    int i;
    int t[5] = {0,'N','E','W','S'};
    for (i = 1; i <= 6; i++) assign[i] = a[i];
    for (i = 1; i <= 4; i++) tr[t[i]] = i;
}
 
char s[102];
int main()
{
    int i, k1, k2;
    int a[7], dice[2][7];
    char *p;
 
    for (i = 1; i <= 6; i++) scanf("%d", a+i);
    dice_init(a);
    scanf("%s", p=s);
    for (i = 1; i <= 6; i++) dice[0][i] = rot[0][i];
    for (k1 = 0, k2 = 1; *p; k1 = k2, k2 = !k2) {
        for (i = 1; i <= 6; i++) dice[k2][i] = dice[k1][rot[tr[*p]][i]];
        p++;
    }
    printf("%d\n", assign[dice[k1][1]]);
    return 0;
}