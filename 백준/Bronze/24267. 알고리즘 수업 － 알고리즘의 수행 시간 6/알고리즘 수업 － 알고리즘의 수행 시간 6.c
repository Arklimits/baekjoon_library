#include <stdio.h>

int main(){
    long long n;
    scanf("%lld", &n);
    printf("%lld\n%d\n", n*(n-1)*(n-2)/6, 3);

    return 0;
}