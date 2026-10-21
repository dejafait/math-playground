// Independent full recurrence check of every mixed support in every case.
// Input is a compact export of the complete JSON, not a positive sample.
#include <array>
#include <fstream>
#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
int mod(int a) { a%=97; return a<0?a+97:a; }
int inv[97], powers[97][9], index_of[97];
vector<int> H;
int eval(const vector<int>& roots,int x) {
    int value=1; for(int a:roots)value=mod(value*(x-a)); return value;
}
struct Match { int mask,mu; bool operator<(const Match& x)const {
    return mask==x.mask?mu<x.mu:mask<x.mask; }};
int maskof(const vector<int>& k) { int mask=0;for(int x:k)mask|=1<<index_of[x];return mask; }
int main(int argc,char** argv) {
    if(argc!=3)throw runtime_error("input and output required");
    for(int x=1;x<97;++x){inv[x]=1;while(mod(x*inv[x])!=1)++inv[x];
        powers[x][0]=1;for(int j=1;j<=8;++j)powers[x][j]=mod(powers[x][j-1]*x);
        if(mod(powers[x][8]*powers[x][8])==1){index_of[x]=H.size();H.push_back(x);}}
    if(H.size()!=16)throw runtime_error("H");
    ifstream input(argv[1]); size_t required; input>>required;
    size_t cases=0,tests=0,admitted=0,max_count=0; array<size_t,251> hist{};
    for(;cases<required;++cases){
        int y1,y2,z1,z2,d,w1,w2,w3,p,q,r;
        input>>y1>>y2>>z1>>z2>>d>>w1>>w2>>w3>>p>>q>>r;
        vector<int> residual(4),first(3),second(3),bprime(5),tail(5);
        for(int& x:residual)input>>x;for(int& x:first)input>>x;for(int& x:second)input>>x;
        for(int& x:bprime)input>>x;for(int& x:tail)input>>x;
        int vmu,mu,nu,n;input>>vmu>>mu>>nu>>n;
        set<Match> expected;for(int i=0;i<n;++i){int mask,m;input>>mask>>m;expected.insert({mask,m});}
        if(!input)throw runtime_error("truncated input");
        vector<int> B={1,d,y1,y2,z1,z2},W={w1,w2,w3},unused;
        set<int> U(B.begin(),B.end());U.insert(W.begin(),W.end());
        for(int x:H)if(!U.count(x))unused.push_back(x);
        array<int,6> c{},a{},b{};
        for(int i=0;i<6;++i)c[i]=eval(unused,B[i]);
        a={mod(c[0]*q),mod(c[1]*(1-r)),0,0,c[4],c[5]};
        b={mod(-c[0]*p),mod(-c[1]*r),mod(-c[2]),mod(-c[3]),0,0};
        if(mod(p*q)==0||mod(1-p-q)==0||r==0||r==1)throw runtime_error("gates");
        auto eligible=[&](const vector<int>& k)->int{
            array<int,4>A{},Bv{};
            for(int j=0;j<4;++j)for(int i=0;i<6;++i){
                int entry=mod(eval(k,B[i])*powers[B[i]][j+1]);
                A[j]=mod(A[j]+a[i]*entry);Bv[j]=mod(Bv[j]+b[i]*entry);}
            int pivot=-1;for(int j=0;j<4;++j)if(Bv[j]){pivot=j;break;}
            if(pivot<0){for(int x:A)if(x)return -1;throw runtime_error("unexpected universal");}
            int m=mod(-A[pivot]*inv[Bv[pivot]]);
            if(m==0||m==96)return -1;
            for(int j=0;j<4;++j)if(mod(A[j]+m*Bv[j]))return -1;
            return m;
        };
        if(eligible(residual)!=vmu)throw runtime_error("V recovery");
        vector<int> k1=first,k2=second;k1.push_back(d);k2.push_back(d);
        if(eligible(k1)!=mu||eligible(k2)!=nu)throw runtime_error("d recoveries");
        set<Match> actual;set<int> distinct;
        for(int tag:vector<int>{1,y1,y2,z1,z2})for(int bp:bprime)
            for(int i=0;i<5;++i)for(int j=i+1;j<5;++j){
                vector<int> k={tag,bp,tail[i],tail[j]};++tests;
                int m=eligible(k);if(m<0)continue;
                actual.insert({maskof(k),m});distinct.insert(m);++admitted;
            }
        if(actual.size()!=expected.size())throw runtime_error("membership size mismatch");
        auto x=actual.begin(),y=expected.begin();for(;x!=actual.end();++x,++y)
            if(x->mask!=y->mask||x->mu!=y->mu)throw runtime_error("membership mismatch");
        ++hist[distinct.size()];max_count=max(max_count,distinct.size());
    }
    int extra;if(input>>extra)throw runtime_error("extra input");
    ofstream output(argv[2]);output<<"{\"complete_cases_checked\":"<<cases
        <<",\"required_cases\":"<<required<<",\"mixed_supports_checked\":"<<tests
        <<",\"required_supports\":"<<250*required<<",\"admitted_memberships_checked\":"<<admitted
        <<",\"maximum_distinct_mixed_scalars\":"<<max_count<<",\"required_for_twelve\":9"
        <<",\"all_membership_sets_match\":true,\"failures\":[],\"mixed_count_histogram\":{";
    bool first=true;for(int i=0;i<251;++i)if(hist[i]){if(!first)output<<',';first=false;output<<'"'<<i<<"\":"<<hist[i];}
    output<<"}}\n";
    cout<<"cases "<<cases<<"/"<<required<<"; complete mixed checks "<<tests<<"/"<<250*required
        <<"; actual maximum "<<max_count<<"; required 9; failures 0; certificate "<<argv[2]<<'\n';
}
