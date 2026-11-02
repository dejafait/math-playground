
#include <cstdint>
#include <iostream>
#include <string>
using Z = __int128_t;
std::string decimal(Z value) {
    if(value==0) return "0";
    std::string answer;
    while(value>0) {answer.insert(answer.begin(), char('0'+value%10)); value/=10;}
    return answer;
}
int main() {
    const int64_t c[]={16777216,16633685,16205546,15500126,14529495,13310260,11863283,10213322,8388608,6420363,4342263,2189866,0,-2189866,-4342263,-6420363,-8388608,-10213322,-11863283,-13310260,-14529495,-15500126,-16205546,-16633685,-16777216,-16633685,-16205546,-15500126,-14529495,-13310260,-11863283,-10213322,-8388608,-6420363,-4342263,-2189866,0,2189866,4342263,6420363,8388608,10213322,11863283,13310260,14529495,15500126,16205546,16633685}, s[]={0,2189866,4342263,6420363,8388608,10213322,11863283,13310260,14529495,15500126,16205546,16633685,16777216,16633685,16205546,15500126,14529495,13310260,11863283,10213322,8388608,6420363,4342263,2189866,0,-2189866,-4342263,-6420363,-8388608,-10213322,-11863283,-13310260,-14529495,-15500126,-16205546,-16633685,-16777216,-16633685,-16205546,-15500126,-14529495,-13310260,-11863283,-10213322,-8388608,-6420363,-4342263,-2189866};
    Z totals[17]={}; uint64_t positive[17]={};
    uint64_t nodes=0;
    // Phase-first order, with independent pair expansion; every product
    // is promoted before multiplication to signed 128-bit arithmetic.
    for(int a=0;a<48;++a) for(int b=0;b<48;++b) for(int d=0;d<48;++d) {
        Z A=Z(c[a])*c[a]+Z(s[a])*s[a]+Z(c[a])*c[b]+Z(c[a])*c[d];
        Z B=Z(c[b])*c[b]+Z(s[b])*s[b]+Z(c[b])*c[a]+Z(c[b])*c[d];
        Z C=Z(c[d])*c[d]+Z(s[d])*s[d]+Z(c[d])*c[a]+Z(c[d])*c[b];
        Z AB=2*Z(s[a])*s[b], AC=2*Z(s[a])*s[d], BC=2*Z(s[b])*s[d];
        for(int k=16;k>=0;--k) for(int j=16;j>=0;--j) for(int i=16;i>=0;--i) {
            Z raw=-(i*i*A+j*j*B+k*k*C+i*j*AB+i*k*AC+j*k*BC);
            int weight=(i==0||i==16?1:2)*(j==0||j==16?1:2)*(k==0||k==16?1:2);
            if(raw>0) {totals[i]+=weight*raw; ++positive[i];}
            ++nodes;
        }
    }
    Z total=0; uint64_t positives=0;
    std::cout<<"[";
    for(int i=0;i<=16;++i) {
        if(i) std::cout<<",";
        std::cout<<"{\"i\":"<<i<<",\"weighted_raw\":\""<<decimal(totals[i])
                 <<"\",\"positive_nodes\":"<<positive[i]<<"}";
        total+=totals[i]; positives+=positive[i];
    }
    std::cout<<"]\n"<<decimal(total)<<"\n"<<nodes<<"\n"<<positives<<"\n";
}
