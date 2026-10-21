// Distributed seed-277 variation of three_shared_pairs_join.cpp; preserves earlier artifacts.
// Bounded actual-label existence search; an unsuccessful prefix is not an exclusion.
#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <random>
#include <set>
#include <cstdint>
using namespace std;
int md(int x){x%=97;return x<0?x+97:x;}
int iv[97];
int ml(int a,int b){return md(a*b);}
int at(const vector<int>& roots,int x){int r=1;for(int t:roots)r=ml(r,x-t);return r;}
vector<array<int,3>> triples(const vector<int>& v){
 vector<array<int,3>> out;
 for(int i=0;i<(int)v.size();i++)for(int j=i+1;j<(int)v.size();j++)for(int k=j+1;k<(int)v.size();k++)out.push_back({v[i],v[j],v[k]});
 return out;
}
void arr(ostream& f,const vector<int>& v){f<<'[';for(int i=0;i<(int)v.size();i++){if(i)f<<',';f<<v[i];}f<<']';}
int intersection(const vector<int>& x,const vector<int>& y){int n=0;for(int a:x)for(int b:y)n+=a==b;return n;}
struct Row{int tag,mu; array<int,3> weights; vector<int> K;};
struct Pair{int first,second;array<int,3> weights;};
struct Assignment{int a,b,c;vector<int> Y,Z,W;};
void assignment_json(ostream& f,const Assignment& d){
 f<<"\"a\":"<<d.a<<",\"b\":"<<d.b<<",\"c\":"<<d.c<<",\"Y\":";arr(f,d.Y);f<<",\"Z\":";arr(f,d.Z);f<<",\"W\":";arr(f,d.W);
}
void row_json(ostream& f,const Row& r){f<<"{\"tag\":"<<r.tag<<",\"mu\":"<<r.mu<<",\"weights\":";arr(f,{r.weights[0],r.weights[1],r.weights[2]});f<<",\"support\":";arr(f,r.K);f<<'}';}
vector<int> H;
long long assignments=0,tests=0,rows_count[3]={},pairs_count[3]={},pair_bearing[3]={},two_tag_weight_joins=0,three_tag_weight_joins=0,distinct_joins=0,linear_joins=0,full_joins=0,moment_failures=0;
int best_tags=-1;long long best_pair_product=-1;
Assignment last_assignment;
ofstream selections("scripts/triangle-recovery/three-shared-pairs-distributed-selections.csv");
int shared_counts[3][97]={};
long long selection_draws=0, duplicate_draws=0;
ofstream partials("scripts/triangle-recovery/three-shared-pairs-distributed-partials.jsonl");

bool process(const Assignment& d,bool seed){
 ++assignments;
 last_assignment=d;
 ++shared_counts[0][d.a];++shared_counts[1][d.b];++shared_counts[2][d.c];
 selections<<assignments<<','<<d.a<<','<<d.b<<','<<d.c;
 for(auto pair:{d.Y,d.Z,d.W})for(int x:pair)selections<<','<<x;
 selections<<'\n';
 vector<int>P={d.a,d.b,d.c},U=P;
 for(auto pair:{d.Y,d.Z,d.W})U.insert(U.end(),pair.begin(),pair.end());
 vector<vector<int>> base={{d.a,d.b,d.Y[0],d.Y[1]},{d.a,d.c,d.Z[0],d.Z[1]},{d.b,d.c,d.W[0],d.W[1]}};
 vector<int> outside;for(int x:H)if(find(U.begin(),U.end(),x)==U.end())outside.push_back(x);
 int cx[97]={};for(int x:U)cx[x]=at(outside,x);
 vector<Row> rows;vector<Pair> pairs[3];int localrows[3]={};
 for(int tag=0;tag<3;tag++){
  vector<int> pool;
  for(int x:H){if(x==P[tag])continue;bool allowed=true;
   for(auto B:base)if(find(B.begin(),B.end(),P[tag])!=B.end()&&find(B.begin(),B.end(),x)!=B.end())allowed=false;
   if(allowed)pool.push_back(x);
  }
  vector<int>J;for(int j=0;j<3;j++)if(j!=tag)J.push_back(P[j]);
  map<pair<int,int>,vector<int>> groups;
  for(auto S:triples(pool)){
   vector<int>K={P[tag],S[0],S[1],S[2]};
   bool linear=true;for(auto B:base)if(intersection(K,B)>1)linear=false;
   if(!linear)continue;
   ++tests;
   int yz[2][2]={};
   for(int which=0;which<2;which++)for(int x:(which?d.Z:d.Y)){
    int v=ml(ml(ml(cx[x],x),at(K,x)),ml(x-J[0],x-J[1]));
    yz[which][0]=md(yz[which][0]+v);yz[which][1]=md(yz[which][1]+ml(v,x));
   }
   if((!yz[0][0]&&!yz[0][1])||(!yz[1][0]&&!yz[1][1]))continue;
   int pivot=yz[0][0]?0:1,mu=ml(yz[1][pivot],iv[yz[0][pivot]]);
   if(mu==0||mu==96||md(yz[1][0]-ml(mu,yz[0][0]))||md(yz[1][1]-ml(mu,yz[0][1])))continue;
   array<int,3>w={-1,-1,-1};
   for(int j=0;j<2;j++){
    int x=J[j],other=J[1-j],beta[2]={};
    for(int which=0;which<2;which++){
     int sum=0;for(int u:(which?d.Z:d.Y))sum=md(sum+ml(ml(ml(cx[u],u),at(K,u)),ml(u-other,iv[md(x-other)])));
     beta[which]=md(-ml(sum,iv[ml(x,at(K,x))]));
    }
    int delta=md(beta[1]-ml(mu,beta[0]));
    if(x==d.a)w[0]=ml(md(1-ml(delta,iv[cx[x]])),iv[md(1+mu)]);
    if(x==d.b)w[1]=md(-ml(ml(delta,iv[mu]),iv[cx[x]]));
    if(x==d.c)w[2]=ml(delta,iv[cx[x]]);
   }
   bool gated=true;for(int j=0;j<3;j++)if(j!=tag&&(w[j]==0||w[j]==1))gated=false;
   if(!gated)continue;
   int id=rows.size();rows.push_back({tag,mu,w,K});++rows_count[tag];++localrows[tag];
   vector<int>fixed;for(int j=0;j<3;j++)if(j!=tag)fixed.push_back(w[j]);
   auto &prior=groups[{fixed[0],fixed[1]}];
   for(int old:prior)if(rows[old].mu!=mu&&intersection(rows[old].K,K)==1)pairs[tag].push_back({old,id,w});
   prior.push_back(id);
  }
 }
 int tags=0;long long score=1;for(int t=0;t<3;t++){pairs_count[t]+=pairs[t].size();if(!pairs[t].empty()){++pair_bearing[t];++tags;}score*=max(size_t(1),pairs[t].size());}
 if(tags>0){partials<<"{\"ordinal\":"<<assignments<<',';assignment_json(partials,d);partials<<",\"rows\":";arr(partials,{localrows[0],localrows[1],localrows[2]});partials<<",\"pairs\":";arr(partials,{int(pairs[0].size()),int(pairs[1].size()),int(pairs[2].size())});partials<<",\"gated_rows\":[";
  for(int i=0;i<(int)rows.size();i++){if(i)partials<<',';row_json(partials,rows[i]);}
  partials<<"],\"pair_indices\":[";
  for(int t=0;t<3;t++){if(t)partials<<',';partials<<'[';for(int i=0;i<(int)pairs[t].size();i++){if(i)partials<<',';arr(partials,{pairs[t][i].first,pairs[t][i].second});}partials<<']';}
  partials<<"]}\n";}
 bool improve=tags>best_tags||(tags==best_tags&&score>best_pair_product);
 if(improve){best_tags=tags;best_pair_product=score;}
 for(int output=0;output<2;output++)if((output==0&&seed)||(output==1&&improve)){
  ofstream f(output==0?"scripts/triangle-recovery/three-shared-pairs-distributed-seed.json":"scripts/triangle-recovery/three-shared-pairs-distributed-best.json");
  f<<"{\"ordinal\":"<<assignments<<',';assignment_json(f,d);f<<",\"rows\":[";
  for(int i=0;i<(int)rows.size();i++){if(i)f<<',';row_json(f,rows[i]);}f<<"],\"pairs\":[";
  for(int t=0;t<3;t++){if(t)f<<',';f<<'[';for(int i=0;i<(int)pairs[t].size();i++){if(i)f<<',';arr(f,{pairs[t][i].first,pairs[t][i].second});}f<<']';}f<<"]}\n";
 }
 for(auto pa:pairs[0])for(auto pb:pairs[1]){
  if(pa.weights[2]!=pb.weights[2])continue;
  ++two_tag_weight_joins;
  array<int,3>w={pb.weights[0],pa.weights[1],pa.weights[2]};
  for(auto pc:pairs[2]){
   if(pc.weights[0]!=w[0]||pc.weights[1]!=w[1])continue;
   ++three_tag_weight_joins;
   vector<int>ids={pa.first,pa.second,pb.first,pb.second,pc.first,pc.second},mus;
   for(int id:ids)mus.push_back(rows[id].mu);
   auto sorted=mus;sort(sorted.begin(),sorted.end());if(unique(sorted.begin(),sorted.end())!=sorted.end())continue;
   ++distinct_joins;bool linear=true;
   for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)if(intersection(rows[ids[i]].K,rows[ids[j]].K)>1)linear=false;
   if(!linear)continue;++linear_joins;
   // Independent verification will select a chart; test full numerator weights here.
   bool full=true;
   for(int id:ids){auto row=rows[id];int mu=row.mu;
    vector<int>N(97);for(int x:d.Y)N[x]=md(-ml(mu,cx[x]));for(int x:d.Z)N[x]=cx[x];
    N[d.a]=ml(cx[d.a],md(1-ml(1+mu,w[0])));N[d.b]=md(-ml(ml(mu,cx[d.b]),w[1]));N[d.c]=ml(cx[d.c],w[2]);
    int omega[4]={};
    for(int k=0;k<4;k++){
     vector<int>other;for(int j=0;j<4;j++)if(j!=k)other.push_back(row.K[j]);
     int value=0;for(int x:U)value=md(value+ml(ml(N[x],x),ml(at(other,x),iv[at(other,row.K[k])])));
     omega[k]=ml(value,iv[row.K[k]]);if(!omega[k])full=false;
    }
    for(int power=1;power<=8;power++){
     int lhs=0,rhs=0;for(int k=0;k<4;k++){int xp=1;for(int j=0;j<power;j++)xp=ml(xp,row.K[k]);lhs=md(lhs+ml(omega[k],xp));}
     for(int x:U){int xp=1;for(int j=0;j<power;j++)xp=ml(xp,x);rhs=md(rhs+ml(N[x],xp));}
     if(lhs!=rhs){++moment_failures;full=false;}
    }
   }
   if(!full)continue;++full_joins;
   ofstream f("scripts/triangle-recovery/three-shared-pairs-distributed-candidate.json");f<<'{';assignment_json(f,d);f<<",\"weights\":";arr(f,{w[0],w[1],w[2]});f<<",\"rows\":[";
   for(int i=0;i<6;i++){if(i)f<<',';row_json(f,rows[ids[i]]);}f<<"]}\n";return true;
  }
 }
 return false;
}
int main(){
 for(int x=1;x<97;x++)for(int y=1;y<97;y++)if(ml(x,y)==1)iv[x]=y;
 for(int x=1;x<97;x++){int t=1;for(int j=0;j<16;j++)t=ml(t,x);if(t==1)H.push_back(x);}
 const long long limit=250000;bool found=false;
 mt19937 rng(277);set<array<int,9>> seen;
 auto bounded=[&](uint32_t n){uint32_t r,threshold=uint32_t(-n)%n;do{r=rng();}while(r<threshold);return r%n;};
 while(!found&&assignments<limit){
  ++selection_draws;auto perm=H;
  for(int i=15;i>0;--i)swap(perm[i],perm[bounded(i+1)]);
  array<int,9> key;copy_n(perm.begin(),9,key.begin());
  for(int i:{3,5,7})if(key[i]>key[i+1])swap(key[i],key[i+1]);
  if(!seen.insert(key).second){++duplicate_draws;continue;}
  Assignment d={key[0],key[1],key[2],{key[3],key[4]},{key[5],key[6]},{key[7],key[8]}};
  found=process(d,assignments==0);
 }
 ofstream f("scripts/triangle-recovery/three-shared-pairs-distributed-prefix.json");
 f<<"{\"random_seed\":277,\"selection_draws\":"<<selection_draws<<",\"duplicate_draws\":"<<duplicate_draws<<",\"complete_assignment_census\":false,\"assignment_limit\":"<<limit<<",\"assignments\":"<<assignments<<",\"support_tests\":"<<tests<<",\"candidate_found\":"<<(found?"true":"false")<<",\"row_counts\":["<<rows_count[0]<<','<<rows_count[1]<<','<<rows_count[2]<<"],\"pair_counts\":["<<pairs_count[0]<<','<<pairs_count[1]<<','<<pairs_count[2]<<"],\"pair_bearing_assignments\":["<<pair_bearing[0]<<','<<pair_bearing[1]<<','<<pair_bearing[2]<<"],\"best_pair_tags\":"<<best_tags<<",\"two_tag_weight_joins\":"<<two_tag_weight_joins<<",\"three_tag_weight_joins\":"<<three_tag_weight_joins<<",\"distinct_scalar_joins\":"<<distinct_joins<<",\"linear_joins\":"<<linear_joins<<",\"full_joins\":"<<full_joins<<",\"moment_failures\":"<<moment_failures<<",\"last_assignment\":{";assignment_json(f,last_assignment);f<<"}}\n";
 ofstream counts("scripts/triangle-recovery/three-shared-pairs-distributed-role-counts.json");
 counts<<"{\"H\":";arr(counts,H);counts<<",\"shared_role_counts\":[";
 for(int t=0;t<3;t++){if(t)counts<<',';vector<int>v;for(int x:H)v.push_back(shared_counts[t][x]);arr(counts,v);}counts<<"]}\n";
 cout<<"Bounded assignments "<<assignments<<'/'<<limit<<"; support tests "<<tests<<". Full joins "<<full_joins<<" versus witness threshold 1; moment failures "<<moment_failures<<".\n";
 cout<<"Tag-pair counts "<<pairs_count[0]<<','<<pairs_count[1]<<','<<pairs_count[2]<<"; two/three-tag weight joins "<<two_tag_weight_joins<<'/'<<three_tag_weight_joins<<". No uniform exclusion.\nCertificates: scripts/triangle-recovery/three-shared-pairs-distributed-{prefix,seed,best}.json; three-shared-pairs-distributed-partials.jsonl\n";
 return moment_failures?2:0;
}
