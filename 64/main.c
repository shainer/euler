#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define UPLIMIT 10000

int periodLength(int n)
{
   int a_0, a, b, c, b_0, c_0, result=0;
   a_0=sqrt(n*1.0);
   b=b_0=a_0;
   c=c_0=n-a_0*a_0;
   do {
      a=(a_0+b)/c;
      b=a*c-b;
      c=(n-b*b)/c;
      result++;
   } while ((b!=b_0)||(c!=c_0));
   return result;
}

void setSquares(int sq[])
{
  int i, power;

  for (i = 0; i <= sqrt(UPLIMIT); i++)
  {
    power = pow(i, 2);
    sq[power] = 1;
  }
}

int main()
{
  int N;
  int period;
  int count = 0;

  int squares[UPLIMIT] = {0};
  setSquares(squares);

  printf("+----------------------------------------------------------------+\n");
  printf("| How many continued fractions for N ≤ 10000 have an odd period? |\n");
  printf("+----------------------------------------------------------------+\n");

  for (N = 2; N <= UPLIMIT; N++)
  {
    if (squares[N] == 0)
    {
      period = periodLength(N);
      if (period % 2 != 0)
      {
        count++;
      }
    }
  }

  printf("%d\n", count);
  return 0;
}
