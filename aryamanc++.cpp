#include <bits/stdc++.h> 
using namespace std;
#define all(x) x.begin(), x.end()
#define fo(i, n) for(int i = 0; i < n; i++)
#define ll long long
#define vl vector<ll>
#define vi vector<int>
#define ui unordered_set<int>
#define pb push_back

int main() {
    int n,i,s,a,b,j,t,sum;
    cin >> n;
    for(i=1;i<=n;i++){
    scanf("%d\n%d\n%d",&s,&a,&b);
    if(a>b){
        t=b;
        b=a;
        a=t;
    }
    else if(a==b){
        printf("%d",(s-1)*a);
        break;
    }
    for(j=0;j<s;j++){
        sum=((a*(s-1-j))+(b*j));
        printf("%d ",sum);
    }
    printf("\n");
    }
    
    return 0;
}
