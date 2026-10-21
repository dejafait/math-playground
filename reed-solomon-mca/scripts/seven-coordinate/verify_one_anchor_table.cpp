// Independent full replay of L107's fixed-(S,P) certificate.
// No producer imports: Gaussian tree solve, generic affine interpolation,
// and four-column moment inversion with all eight moments restored.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Key=array<int,11>;
using Mat=vector<vector<int>>;
int invs[97];
int mod(int x){int r=x%97;return r<0?r+97:r;}
int power(int a,int n){int r=1;while(n-- >0)r=r*a%97;return r;}
void require(bool b,const string& why){if(!b)throw runtime_error(why);}
Mat inverse(Mat a){
 int n=a.size();for(int i=0;i<n;i++)for(int j=0;j<n;j++)a[i].push_back(i==j);
 for(int j=0;j<n;j++){
  int p=j;while(p<n&&!a[p][j])p++;require(p<n,"singular inverse");swap(a[p],a[j]);
  int v=invs[a[j][j]];for(int&x:a[j])x=x*v%97;
  for(int i=0;i<n;i++)if(i!=j){int c=a[i][j];for(int k=0;k<2*n;k++)a[i][k]=mod(a[i][k]-c*a[j][k]);}
 }
 Mat b(n,vector<int>(n));for(int i=0;i<n;i++)for(int j=0;j<n;j++)b[i][j]=a[i][j+n];return b;
}
const array<int,7> labels={1,8,12,18,22,27,33};
vector<int> h,jset;vector<array<int,2>> ks,edges,pairs;
int g[36][16],gs[36][7],mom[8][7];
struct Row{int x,y,k;};
vector<Row> rows;
int value(const Key&w,int z,int mu){return z<3?w[z]:mod(w[z+4]+mu*w[z]);}
struct Prefix{Key w{};array<int,2> e1,e2;int k1,k2,c1,c2;vector<int> common;bool slopes;};
Prefix prefix(array<int,2>e1,array<int,2>e2,int k1,int k2){
 Prefix t;t.e1=e1;t.e2=e2;t.k1=k1;t.k2=k2;
 Mat a={{1,0,0}};
 for(auto ek:vector<pair<array<int,2>,int>>{{e1,k1},{e2,k2}}){
  vector<int> rem;for(int x=0;x<3;x++)if(x!=ek.first[0])rem.push_back(x);
  vector<int> eq(3);eq[rem[0]]=gs[ek.second][rem[1]];eq[rem[1]]=mod(-gs[ek.second][rem[0]]);a.push_back(eq);
 }
 auto ai=inverse(a);for(int z=0;z<3;z++){t.w[z]=ai[z][0];require(t.w[z]!=0,"zero normalized P");}
 int z=0;while(z==e1[0])z++;t.c1=t.w[z]*invs[gs[k1][z]]%97;
 z=0;while(z==e2[0])z++;t.c2=t.w[z]*invs[gs[k2][z]]%97;
 t.slopes=true;
 for(int x=3;x<7;x++)if(x!=e1[1]&&x!=e2[1]){
  t.common.push_back(x);t.w[x+4]=t.c1*gs[k1][x]%97;
  t.w[x]=mod(t.c2*gs[k2][x]-t.w[x+4]);t.slopes&=t.w[x]!=0;
 }
 return t;
}
int seed(const Prefix&t,Row r,Key&w){
 w=t.w;int z=0;while(z==r.x||z==r.y)z++;
 int c3=w[z]*invs[gs[r.k][z]]%97;
 array<Row,3> rr={Row{t.e1[0],t.e1[1],t.k1},Row{t.e2[0],t.e2[1],t.k2},r};
 array<int,3> cs={t.c1,t.c2,c3};
 for(int q=0;q<3;q++)for(int x=0;x<3;x++)if(x!=rr[q].x&&x!=rr[q].y&&w[x]!=cs[q]*gs[rr[q].k][x]%97)return 1;
 if(!t.slopes)return 2;
 int pivot=t.common[0];if(pivot==r.x||pivot==r.y)pivot=t.common[1];
 int theta=mod(c3*gs[r.k][pivot]-w[pivot+4])*invs[w[pivot]]%97;
 if(theta==0||theta==1)return 3;
 for(int x:t.common)if(x!=r.x&&x!=r.y&&mod(w[x]*theta+w[x+4]-c3*gs[r.k][x]))return 4;
 array<int,3> mu={0,1,theta};
 // Reconstruct each missing coordinate from its two observed values.
 for(int x:array<int,2>{t.e1[1],t.e2[1]}){
  vector<int> obs;for(int q=0;q<3;q++)if(x!=rr[q].x&&x!=rr[q].y)obs.push_back(q);
  require(obs.size()==2,"missing-coordinate observations");int u=obs[0],v=obs[1];
  int vu=cs[u]*gs[rr[u].k][x]%97,vv=cs[v]*gs[rr[v].k][x]%97;
  w[x]=mod(vv-vu)*invs[mod(mu[v]-mu[u])]%97;w[x+4]=mod(vu-mu[u]*w[x]);
 }
 if(!w[t.e1[1]]||!w[t.e2[1]])return 5;
 for(int q=0;q<3;q++){
  for(int x=0;x<7;x++)if(x!=rr[q].x&&x!=rr[q].y&&value(w,x,mu[q])!=cs[q]*gs[rr[q].k][x]%97)return 6;
  if(value(w,rr[q].x,mu[q])==cs[q]*gs[rr[q].k][rr[q].x]%97)return 7;
  if(value(w,rr[q].y,mu[q])==cs[q]*gs[rr[q].k][rr[q].y]%97)return 8;
 }
 return 0;
}
struct Block{array<int,4> support;int m[8][4],wt[4][7],res[4][7];};
Block block(Row r){
 Block b;b.support={labels[r.x],labels[r.y],ks[r.k][0],ks[r.k][1]};
 Mat top(4,vector<int>(4));for(int i=0;i<8;i++)for(int z=0;z<4;z++){b.m[i][z]=power(b.support[z],i+1);if(i<4)top[i][z]=b.m[i][z];}
 auto iv=inverse(top);
 for(int i=0;i<4;i++)for(int z=0;z<7;z++){int v=0;for(int q=0;q<4;q++)v+=iv[i][q]*mom[q][z];b.wt[i][z]=v%97;}
 for(int i=0;i<4;i++)for(int z=0;z<7;z++){int v=mom[i+4][z];for(int q=0;q<4;q++)v-=b.m[i+4][q]*b.wt[q][z];b.res[i][z]=mod(v);}
 return b;
}
char gatecode(const Key&w,Row r,int&mu){
 int z=0;while(z==r.x||z==r.y)z++;
 // Cross products check P compatibility before division.
 for(int x=0;x<3;x++)if(x!=r.x&&x!=r.y&&mod(w[x]*gs[r.k][z]-w[z]*gs[r.k][x]))return 'p';
 int c=w[z]*invs[gs[r.k][z]]%97;
 int y=3;while(y==r.x||y==r.y)y++;
 mu=mod(c*gs[r.k][y]-w[y+4])*invs[w[y]]%97;
 for(int x=3;x<7;x++)if(x!=r.x&&x!=r.y&&mod(value(w,x,mu)-c*gs[r.k][x]))return 'r';
 if(value(w,r.x,mu)==c*gs[r.k][r.x]%97)return 'i';
 if(value(w,r.y,mu)==c*gs[r.k][r.y]%97)return 'j';return 's';
}
bool direct(const Key&w,const Block&b,int&mu,long long&all8){
 int r0[4],ri[4],pivot=-1;
 for(int q=0;q<4;q++){
  int a=0,c=0;for(int z=0;z<3;z++)a+=b.res[q][z]*w[z];
  for(int z=3;z<7;z++){a+=b.res[q][z]*w[z+4];c+=b.res[q][z]*w[z];}
  r0[q]=a%97;ri[q]=c%97;if(ri[q]&&pivot<0)pivot=q;
 }
 require(pivot>=0,"whole-line/infinity exception");mu=mod(-r0[pivot])*invs[ri[pivot]]%97;
 for(int q=0;q<4;q++)if((r0[q]+mu*ri[q])%97)return false;
 int weights[4],lift[7];for(int z=0;z<7;z++)lift[z]=value(w,z,mu);
 bool full=true;for(int q=0;q<4;q++){int a=0;for(int z=0;z<7;z++)a+=b.wt[q][z]*lift[z];weights[q]=a%97;full&=weights[q]!=0;}
 for(int q=0;q<8;q++){
  int a=0,c=0;for(int z=0;z<4;z++)a+=b.m[q][z]*weights[z];for(int z=0;z<7;z++)c+=mom[q][z]*lift[z];
  require(mod(a-c)==0,"full eight-moment residual");
 }
 all8++;return full;
}
int main(){try{
 for(int x=1;x<97;x++){for(int y=1;y<97;y++)if(x*y%97==1)invs[x]=y;if(power(x,16)==1)h.push_back(x);}
 require(h.size()==16,"H size");for(int x:h)if(find(labels.begin(),labels.end(),x)==labels.end())jset.push_back(x);
 for(int a=0;a<9;a++)for(int b=a+1;b<9;b++)ks.push_back({jset[a],jset[b]});
 for(int k=0;k<36;k++)for(int z=0;z<16;z++){int v=1;for(int y:jset)if(y!=ks[k][0]&&y!=ks[k][1])v=mod(v*(h[z]-y));g[k][z]=v;}
 for(int k=0;k<36;k++)for(int z=0;z<7;z++){gs[k][z]=g[k][find(h.begin(),h.end(),labels[z])-h.begin()];require(gs[k][z]!=0,"generator evaluation");}
 for(int q=0;q<8;q++)for(int z=0;z<7;z++)mom[q][z]=power(labels[z],q+1);
 for(int k=0;k<36;k++)for(int q=0;q<8;q++){int v=0;for(int z=0;z<16;z++)v+=g[k][z]*power(h[z],q+1);require(v%97==0,"generator moment");}
 for(int x=0;x<3;x++)for(int y=3;y<7;y++)edges.push_back({x,y});
 for(int x=0;x<3;x++)for(int y=x+1;y<3;y++)pairs.push_back({x,y});pairs.insert(pairs.end(),edges.begin(),edges.end());
 for(auto p:pairs)for(int k=0;k<36;k++)rows.push_back({p[0],p[1],k});require(rows.size()==540,"rows count");
 vector<Block> blocks;for(auto r:rows)blocks.push_back(block(r));
 vector<Key> keys;set<Key> unique;map<int,long long>hist;map<char,long long>rowcounts;vector<int>maximizers;
 long long rowtotal=0,full=0,all8=0;int maximum=0;
 ifstream cf("scripts/seven-coordinate/one-anchor-candidates.tsv");require(bool(cf),"candidate file");string line;
 while(getline(cf,line)){
  istringstream ss(line);int cid;Key w;string codes;int m;ss>>cid;for(int&v:w){ss>>v;require(v>=0&&v<97,"candidate residue");}ss>>codes>>m;
  require(bool(ss)&&cid==int(keys.size())&&codes.size()==540,"candidate format/ID");
  require(w[0]==1&&w[1]&&w[2],"P normalization");for(int z=3;z<7;z++)require(w[z]!=0,"nonzero R slope");
  require(unique.insert(w).second,"duplicate candidate key");keys.push_back(w);
  vector<int> stated(m);for(int&v:stated)ss>>v;require(bool(ss),"scalar list");string extra;require(!(ss>>extra),"trailing candidate field");
  set<int>mus;int successes=0;
  for(int rid=0;rid<540;rid++){
   int mu=-1,dm=-1;char code=gatecode(w,rows[rid],mu);require(code==codes[rid],"first failed row gate");rowcounts[code]++;rowtotal++;
   bool ok=direct(w,blocks[rid],dm,all8);require(ok==(code=='s'),"independent moment acceptance");
   if(ok){require(mu==dm,"independent moment scalar");mus.insert(dm);successes++;full++;}
  }
  require(int(mus.size())==successes,"duplicate full support scalar");require(vector<int>(mus.begin(),mus.end())==stated&&m==successes,"scalar list equality");
  hist[m]++;if(m>maximum){maximum=m;maximizers.clear();}if(m==maximum)maximizers.push_back(cid);
 }
 require(cf.eof(),"candidate read failure");
 cerr<<"Moment replay complete: "<<keys.size()<<" lifts, "<<rowtotal<<" rows, maximum "<<maximum<<"/9. Replaying every seed.\n";
 ifstream sf("scripts/seven-coordinate/one-anchor-seeds.bin",ios::binary);require(bool(sf),"seed file");
 array<long long,9>gates{};vector<bool>reached(keys.size());int next=0;long long seedtotal=0;
 for(int a=0;a<12;a++)for(int b=a+1;b<12;b++)if(edges[a][0]!=edges[b][0]&&edges[a][1]!=edges[b][1])
 for(int k1=0;k1<36;k1++)for(int k2=0;k2<36;k2++)if(k1!=k2){
  auto t=prefix(edges[a],edges[b],k1,k2);
  for(auto p:pairs)if(p[1]!=edges[a][1]&&p[1]!=edges[b][1])for(int k3=0;k3<36;k3++){
   uint32_t record=0;for(int byte=0;byte<4;byte++){int c=sf.get();require(c!=EOF,"truncated seed file");record|=uint32_t(c)<<(8*byte);}
   Key w;int status=seed(t,{p[0],p[1],k3},w);gates[status]++;seedtotal++;
   if(status)require(record==(0x80000000u|status),"seed rejection discrepancy");
   else {require(record<keys.size()&&keys[record]==w,"seed reconstructed lift discrepancy");if(!reached[record]){require(record==uint32_t(next++),"first-encounter candidate ID");reached[record]=true;}}
  }
 }
 require(sf.get()==EOF,"extra seed data");require(seedtotal==14696640&&next==int(keys.size()),"complete seed/candidate coverage");
 ofstream out("scripts/seven-coordinate/one-anchor-table-verification-raw.json");require(bool(out),"verification output");
 out<<"{\n\"complete\":true,\"seed_count\":"<<seedtotal<<",\"required_seed_count\":14696640,\"candidate_count\":"<<keys.size()<<",\"row_count\":"<<rowtotal<<",\"required_rows_per_candidate\":540,\"full_successes\":"<<full<<",\"maximum_distinct_scalars\":"<<maximum<<",\"required_threshold\":9,\"generator_moment_checks\":288,\"compatible_rows_checked_in_all_eight_moments\":"<<all8<<",\"seed_gate_counts\":[";
 for(int i=0;i<9;i++)out<<(i?",":"")<<gates[i];out<<"],\"row_gate_counts\":{";bool comma=false;for(auto [c,n]:rowcounts){out<<(comma?",":"")<<'"'<<c<<"\":"<<n;comma=true;}
 out<<"},\"histogram\":{";comma=false;for(auto [m,n]:hist){out<<(comma?",":"")<<'"'<<m<<"\":"<<n;comma=true;}
 out<<"},\"maximizer_ids\":[";for(int i=0;i<int(maximizers.size());i++)out<<(i?",":"")<<maximizers[i];
 out<<"],\"failures\":0}\n";
 cout<<"Independent replay: seeds "<<seedtotal<<"/14696640; rows "<<rowtotal<<"/"<<keys.size()*540LL<<"; maximum "<<maximum<<"/9; failures 0.\n";
 return 0;
 }catch(const exception&e){cerr<<"VERIFICATION FAILURE: "<<e.what()<<'\n';return 1;}}
