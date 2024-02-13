#include<stdio.h>

int eat(n){
	if (n==1) return 1;
	return (eat(n-1)+1)*2;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d",eat(n));
}
