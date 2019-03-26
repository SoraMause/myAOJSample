#include <stdio.h>

int main( void ){
    int a_ij[100][100];
    int b[100];
    int c[100];
    int m,n;
    int i,j;

    scanf( " %d %d", &n, &m );
    for( i = 0; i < n; i++ ){
        for( j = 0; j < m; j++ ){
            scanf( " %d", &a_ij[i][j] );
        }
    }

    for( i = 0; i < m; i++ ){
        scanf( " %d", &b[i] );
    }

    for( i = 0; i < n; i++ ){
        for( j = 0; j < m; j++ ){
            c[i] += a_ij[i][j] * b[j];
        }
        printf( "%d\n",c[i] );
    }

    return 0;

}