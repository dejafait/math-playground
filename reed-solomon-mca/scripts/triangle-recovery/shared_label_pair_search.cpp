// Witness search for L057's named-a pair. No negative prefix is a theorem.
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int mod(int x){x%=97;return x<0?x+97:x;}
int iv[97];
int mul(int a,int b){return mod(a*b);}
int product_at(const vector<int>& roots,int x){int r=1;for(int t:roots)r=mul(r,x-t);return r;}
vector<array<int,3>> triples(const vector<int>& v){
 vector<array<int,3>> out;
 for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)for(int k=j+1;k<(int)v.size();k++)out.push_back({v[i],v[j],v[k]});
 return out;
}
bool disjoint(const array<int,3>& x,const array<int,3>& y){for(int a:x)for(int b:y)if(a==b)return false;return true;}
struct Row{array<int,3> outside;int mu,q,r;};
void arr(ostream& f,const vector<int>& v){f<<'[';for(int i=0;i<(int)v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
int main(){
 for(int x=1;x<97;x++)for(int y=1;y<97;y++)if(mul(x,y)==1)iv[x]=y;
 vector<int> H;for(int x=1;x<97;x++){int t=1;for(int j=0;j<16;j++)t=mul(t,x);if(t==1)H.push_back(x);}
 long long assignments=0,tests=0,isolated=0,pairtests=0;
 const long long limit=1000000;
 for(int a:H){
  vector<int> rest;for(int x:H)if(x!=a)rest.push_back(x);
  auto ts=triples(rest);
  for(auto A:ts)for(auto B:ts){
   if(!(A<B)||!disjoint(A,B))continue; // existence only: swap bases 0,1 is not needed for a found witness
   vector<int> pool;for(int x:rest)if(find(A.begin(),A.end(),x)==A.end()&&find(B.begin(),B.end(),x)==B.end())pool.push_back(x);
   auto outs=triples(pool);
   for(int b:A)for(int c:B){
    vector<int> Y,Z;for(int x:A)if(x!=b)Y.push_back(x);for(int x:B)if(x!=c)Z.push_back(x);
    for(int wi=0;wi<9;wi++)for(int wj=wi+1;wj<9;wj++){
     vector<int> W={pool[wi],pool[wj]},U={a,b,c,Y[0],Y[1],Z[0],Z[1],W[0],W[1]},outside;
     for(int x:H)if(find(U.begin(),U.end(),x)==U.end())outside.push_back(x);
     int cx[97]={0};for(int x:U)cx[x]=product_at(outside,x);
     assignments++;
     map<pair<int,int>,vector<Row>> groups;
     for(auto S:outs){
      if(find(S.begin(),S.end(),W[0])!=S.end()&&find(S.begin(),S.end(),W[1])!=S.end())continue;
      tests++;
      vector<int>K={a,S[0],S[1],S[2]};
      int yy[2]={0,0},zz[2]={0,0};
      for(int tag=0;tag<2;tag++)for(int x:(tag?Z:Y)){
       int v=mul(mul(mul(cx[x],x),product_at(K,x)),mul(x-b,x-c));
       int* vv=tag?zz:yy;vv[0]=mod(vv[0]+v);vv[1]=mod(vv[1]+mul(v,x));
      }
      if((!yy[0]&&!yy[1])||(!zz[0]&&!zz[1]))continue;
      int piv=yy[0]?0:1,mu=mul(zz[piv],iv[yy[piv]]);
      if(mu==0||mu==96||mod(zz[0]-mul(mu,yy[0]))||mod(zz[1]-mul(mu,yy[1])))continue;
      int by[2]={0,0},bz[2]={0,0},J[2]={b,c};
      for(int j=0;j<2;j++){
       int x=J[j],other=J[1-j];
       for(int tag=0;tag<2;tag++){
        int sum=0;for(int u:(tag?Z:Y))sum=mod(sum+mul(mul(mul(cx[u],u),product_at(K,u)),mul(u-other,iv[mod(x-other)])));
        (tag?bz:by)[j]=mod(-mul(sum,iv[mul(x,product_at(K,x))]));
       }
      }
      int q=mul(mod(by[0]-mul(bz[0],iv[mu])),iv[cx[b]]),r=mul(mod(bz[1]-mul(mu,by[1])),iv[cx[c]]);
      if(q==0||q==1||r==0||r==1)continue;
      isolated++;
      Row row{S,mu,q,r};
      auto &prior=groups[{q,r}];
      for(auto old:prior){pairtests++;if(old.mu==mu||!disjoint(old.outside,S))continue;
       // Full moments and all gates are deliberately checked by a separate Python program.
       ofstream f("scripts/triangle-recovery/shared-label-pair-candidate.json");
       f<<"{\"scope\":\"positive candidate only; prefix is not a census\",\"a\":"<<a<<",\"b\":"<<b<<",\"c\":"<<c<<",\"Y\":";arr(f,Y);f<<",\"Z\":";arr(f,Z);f<<",\"W\":";arr(f,W);
       f<<",\"K\":";arr(f,{a,old.outside[0],old.outside[1],old.outside[2]});f<<",\"L\":";arr(f,K);
       f<<",\"mu\":["<<old.mu<<','<<mu<<"],\"q\":"<<q<<",\"r\":"<<r<<",\"assignments_tested\":"<<assignments<<",\"support_tests\":"<<tests<<",\"gated_isolated_rows\":"<<isolated<<",\"same_weight_pair_tests\":"<<pairtests<<"}\n";
       cout<<"Projected candidate: 1; required full witnesses: 1 (verification pending). Assignments "<<assignments<<"; support tests "<<tests<<". Certificate scripts/triangle-recovery/shared-label-pair-candidate.json\n";return 0;
      }
      prior.push_back(row);
     }
     if(assignments>=limit){
      ofstream f("scripts/triangle-recovery/shared-label-pair-search-prefix.json");f<<"{\"complete\":false,\"assignments\":"<<assignments<<",\"support_tests\":"<<tests<<",\"gated_isolated_rows\":"<<isolated<<",\"same_weight_pair_tests\":"<<pairtests<<",\"candidates\":0}\n";
      cout<<"Incomplete prefix: "<<assignments<<" assignments; candidates 0 versus witness threshold 1. No exclusion. Certificate scripts/triangle-recovery/shared-label-pair-search-prefix.json\n";return 0;
     }
    }
   }
  }
 }
 return 2;
}
