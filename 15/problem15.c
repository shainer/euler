#include <stdio.h>

#define LEN 21

void printMatrix(unsigned long long m[][LEN])
{
	int i,j;
	
	for (i = 0; i < LEN; ++i)
	{
		for (j = 0; j < LEN; ++j)
		{
			printf ("%llu ", m[i][j]);
		}
		printf("\n");
	}
}

int main(int argc, char **argv)
{
	unsigned long long matrix[LEN][LEN] = {0};
	int i, j;
	
	for (i = 0; i < LEN; ++i)
	{
		matrix[i][0] = matrix[0][i] = 1;
	}
	matrix[0][0] = 0;
	
	for (i = 1; i < LEN; ++i)
	{
		for (j = 1; j < LEN; ++j)
		{
			matrix[i][j] = matrix[i-1][j] + matrix[i][j-1];
		}		
	}
	
	printf("Result: %llu\n", matrix[LEN-1][LEN-1]);
	return 0;
}
