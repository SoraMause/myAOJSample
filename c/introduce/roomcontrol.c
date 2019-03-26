#include <stdio.h>

int main( void ){
    int n,tou_buff,floor_buff,room_buff,person_buff;
    int room[5][4][11];
    int i,j,k;

    for( i = 1; i < 5; i++ ){
        for( j = 1; j < 4; j++ ){
            for( k = 1; k < 11; k++ ){
                room[i][j][k] = 0;
            }
        }
    }
    
    scanf( "%d",&n );
    for( i = 0; i < n; i++ ){
        scanf( " %d %d %d %d", &tou_buff, &floor_buff, &room_buff, &person_buff );
        room[tou_buff][floor_buff][room_buff] += person_buff;
    }

    for( i = 1; i < 5; i++ ){
        for( j = 1; j < 4; j++ ){
            for( k = 1; k < 11; k++ ){
                printf( " %d",room[i][j][k] );
            }
            printf( "\n" );
        }
        if( i < 4 ) printf( "####################\n");
    }
}