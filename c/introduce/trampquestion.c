#include <stdio.h>
 
int main(void) {
    int sonzai[52];
    int n;
    int i;
    char kindc[4]={'S','H','C','D'};
    char kind;
    int num = 0;

    for(i=0;i<52;i++)sonzai[i]=0;

    scanf("%d",&n);
    
    for(i=0;i<n;i++) {
        scanf(" %c %d ",&kind,&num );
        switch(kind) {
            case 'D':num+=13;
            case 'C':num+=13;
            case 'H':num+=13;
            //case 'S':num+=13;
        }
        sonzai[num-1]=1;
    }
    for(i=0;i<52;i++) {
        if(sonzai[i]==0)
            printf("%c %d\n",kindc[i/13],i%13+1);
    }
    return 0;
}
