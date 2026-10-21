// Complete L107 fixed-(S,P) seed filter. No incidence pruning.
// Binary seed records: little-endian uint32; high bit denotes rejection
// (low bits = first failed gate 1..8), otherwise zero-based candidate ID.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
int md(int x){x%=97;return x<0?x+97:x;}
int mul(int x,int y){return x*y%97;}
int iv[97],G[36][16];
const array<int,7> S={1,8,12,18,22,27,33};
vector<int> H,J; vector<array<int,2>> K,edges,rows;
using Key=array<int,11>; // p[0..2], A[0..3], B[0..3]
struct Row {int i,j,k;};
vector<Row> rowlist;
int val(const Key&w,int z,int mu){return z<3?w[z]:md(w[7+z-3]+mu*w[3+z-3]);}
int gv(int k,int z){return G[k][find(H.begin(),H.end(),S[z])-H.begin()];}
char rowtest(const Key&w,Row r,int&mu){
 int z=0;while(z==r.i||z==r.j)z++;
 int c=mul(w[z],iv[gv(r.k,z)]);
 for(int x=0;x<3;x++)if(x!=r.i&&x!=r.j&&w[x]!=mul(c,gv(r.k,x)))return 'p';
 int y=3;while(y==r.i||y==r.j)y++;
 mu=mul(md(mul(c,gv(r.k,y))-w[y+4]),iv[w[y]]);
 for(int x=3;x<7;x++)if(x!=r.i&&x!=r.j&&val(w,x,mu)!=mul(c,gv(r.k,x)))return 'r';
 if(val(w,r.i,mu)==mul(c,gv(r.k,r.i)))return 'i';
 if(val(w,r.j,mu)==mul(c,gv(r.k,r.j)))return 'j';
 return 's';
}
int reconstruct(array<int,2>e1,array<int,2>e2,int k1,int k2,Row r3,Key&w){
 w.fill(0);w[0]=1;
 array<int,3> p={1,0,0};
 for(int round=0;round<2;round++)for(auto ek:vector<pair<array<int,2>,int>>{{e1,k1},{e2,k2}}){
  int u=-1,v=-1;for(int x=0;x<3;x++)if(x!=ek.first[0]){if(u<0)u=x;else v=x;}
  if(p[u])p[v]=mul(mul(p[u],gv(ek.second,v)),iv[gv(ek.second,u)]);
  if(p[v])p[u]=mul(mul(p[v],gv(ek.second,u)),iv[gv(ek.second,v)]);
 }
 for(int x=0;x<3;x++){assert(p[x]);w[x]=p[x];}
 array<Row,3> rr={Row{e1[0],e1[1],k1},Row{e2[0],e2[1],k2},r3};
 int c[3];
 for(int t=0;t<3;t++){
  int z=0;while(z==rr[t].i||z==rr[t].j)z++;
  c[t]=mul(p[z],iv[gv(rr[t].k,z)]);
  for(int x=0;x<3;x++)if(x!=rr[t].i&&x!=rr[t].j&&p[x]!=mul(c[t],gv(rr[t].k,x)))return 1;
 }
 int y1=e1[1],y2=e2[1];vector<int>Z;
 for(int x=3;x<7;x++)if(x!=y1&&x!=y2){
  Z.push_back(x);w[x+4]=mul(c[0],gv(k1,x));w[x]=md(mul(c[1],gv(k2,x))-w[x+4]);
  if(!w[x])return 2;
 }
 int pivot=Z[0];if(pivot==r3.i||pivot==r3.j)pivot=Z[1];
 int theta=mul(md(mul(c[2],gv(r3.k,pivot))-w[pivot+4]),iv[w[pivot]]);
 if(theta==0||theta==1)return 3;
 for(int z:Z)if(z!=r3.i&&z!=r3.j&&val(w,z,theta)!=mul(c[2],gv(r3.k,z)))return 4;
 w[y1]=mul(md(mul(c[2],gv(r3.k,y1))-mul(c[1],gv(k2,y1))),iv[md(theta-1)]);
 w[y1+4]=md(mul(c[1],gv(k2,y1))-w[y1]);
 w[y2+4]=mul(c[0],gv(k1,y2));
 w[y2]=mul(md(mul(c[2],gv(r3.k,y2))-w[y2+4]),iv[theta]);
 if(!w[y1]||!w[y2])return 5;
 for(int t=0;t<3;t++){
  int mu=t==0?0:t==1?1:theta;
  for(int z=0;z<7;z++)if(z!=rr[t].i&&z!=rr[t].j&&val(w,z,mu)!=mul(c[t],gv(rr[t].k,z)))return 6;
  if(val(w,rr[t].i,mu)==mul(c[t],gv(rr[t].k,rr[t].i)))return 7;
  if(val(w,rr[t].j,mu)==mul(c[t],gv(rr[t].k,rr[t].j)))return 8;
 }
 return 0;
}
void record(ofstream&f,uint32_t a){for(int j=0;j<4;j++)f.put(char((a>>(8*j))&255));}
int main(){
 for(int x=1;x<97;x++){iv[x]=1;while(mul(x,iv[x])!=1)iv[x]++;int t=1;for(int i=0;i<16;i++)t=mul(t,x);if(t==1)H.push_back(x);}
 for(int h:H)if(find(S.begin(),S.end(),h)==S.end())J.push_back(h);
 for(int a=0;a<9;a++)for(int b=a+1;b<9;b++)K.push_back({J[a],J[b]});
 for(int k=0;k<36;k++)for(int h=0;h<16;h++){int v=1;for(int z:J)if(z!=K[k][0]&&z!=K[k][1])v=mul(v,md(H[h]-z));G[k][h]=v;}
 for(int x=0;x<3;x++)for(int y=3;y<7;y++)edges.push_back({x,y});
 for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)rows.push_back({i,j});
 rows.insert(rows.end(),edges.begin(),edges.end());
 for(auto e:rows)for(int k=0;k<36;k++)rowlist.push_back({e[0],e[1],k});
 ofstream seeds("scripts/seven-coordinate/one-anchor-seeds.bin",ios::binary);
 ofstream candidates("scripts/seven-coordinate/one-anchor-candidates.tsv");
 assert(seeds&&candidates&&rowlist.size()==540);
 map<Key,int> seen;array<long long,9> gates{};map<int,long long>hist;map<char,long long>rowcounts;
 long long n=0,full=0;int maximum=0;vector<int> maximizers;
 for(int a=0;a<12;a++)for(int b=a+1;b<12;b++){
  auto e1=edges[a],e2=edges[b];if(e1[0]==e2[0]||e1[1]==e2[1])continue;
  for(int k1=0;k1<36;k1++)for(int k2=0;k2<36;k2++)if(k1!=k2)
  for(auto e3:rows)if(e3[1]!=e1[1]&&e3[1]!=e2[1])for(int k3=0;k3<36;k3++){
   n++;Key w;int status=reconstruct(e1,e2,k1,k2,{e3[0],e3[1],k3},w);gates[status]++;
   if(status){record(seeds,0x80000000u|status);continue;}
   auto [it,added]=seen.emplace(w,seen.size());int cid=it->second;record(seeds,cid);
   if(!added)continue;
   set<int> mus;string codes;vector<pair<int,int>>success;
   for(int rid=0;rid<540;rid++){int mu=-1;char code=rowtest(w,rowlist[rid],mu);codes+=code;rowcounts[code]++;if(code=='s'){mus.insert(mu);success.push_back({rid,mu});full++;}}
   assert(mus.size()==success.size());int m=mus.size();hist[m]++;
   if(m>maximum){maximum=m;maximizers.clear();}if(m==maximum)maximizers.push_back(cid);
   candidates<<cid;for(int v:w)candidates<<'\t'<<v;candidates<<'\t'<<codes<<'\t'<<mus.size();for(int mu:mus)candidates<<'\t'<<mu;candidates<<'\n';
  }
 }
 assert(n==14696640);seeds.close();candidates.close();
 ofstream out("scripts/seven-coordinate/one-anchor-table.json");
 out<<"{\n\"complete\":true,\"seed_count\":"<<n<<",\"required_seed_count\":14696640,\"candidate_count\":"<<seen.size()<<",\"row_count\":"<<seen.size()*540LL<<",\"required_rows_per_candidate\":540,\"full_successes\":"<<full<<",\"maximum_distinct_scalars\":"<<maximum<<",\"required_threshold\":9,\"seed_gate_counts\":[";
 for(int i=0;i<9;i++)out<<(i?",":"")<<gates[i];out<<"],\"row_gate_counts\":{";bool comma=false;
 for(auto [c,num]:rowcounts){out<<(comma?",":"")<<'"'<<c<<"\":"<<num;comma=true;}
 out<<"},\"histogram\":{";comma=false;for(auto [m,num]:hist){out<<(comma?",":"")<<'"'<<m<<"\":"<<num;comma=true;}
 out<<"},\"maximizer_ids\":[";for(int i=0;i<(int)maximizers.size();i++)out<<(i?",":"")<<maximizers[i];
 out<<"],\"seed_artifact\":\"one-anchor-seeds.bin\",\"candidate_artifact\":\"one-anchor-candidates.tsv\",\"failures\":0}\n";
 cout<<"Complete seeds "<<n<<"/14696640; lifts "<<seen.size()<<"; rows "<<seen.size()*540LL<<"; maximum "<<maximum<<"/9; failures 0; scripts/seven-coordinate/one-anchor-table.json\n";
}
