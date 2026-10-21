// Complete all-48 cross-ratio test using the replayed V0 solutions.
// Auxiliary F4 is used ONLY to construct the incidence table.
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
int f(long long x) { x%=97; return int(x<0?x+97:x); }
int inv[97];
using Point=std::array<int,2>; // (1,z), infinity=(0,1).
int bracket(Point a,Point b) { return f(a[0]*b[1]-a[1]*b[0]); }
Point finite(int z) { return {1,z}; }
int mul4(int a,int b) {
 int out=0; while(b) { if(b&1) out^=a; a<<=1; b>>=1; if(a&4) a^=7; } return out;
}
struct Quad { std::array<int,4> blocks,labels,permutation; int group; };
int main(int argc,char**argv) {
 if(argc!=3) return 2;
 std::string input_path=argv[1],prefix=argv[2];
 std::ifstream input(input_path);
 std::ofstream rows(prefix+"-rows.csv"),passing(prefix+"-passing.jsonl"),incidence(prefix+"-incidence.json");
 if(!input||!rows||!passing||!incidence) return 2;
 for(int a=1;a<97;a++) for(int b=1;b<97;b++) if(f(a*b)==1) inv[a]=b;
 std::array<std::array<int,4>,16> blocks;
 for(int e=0;e<4;e++) for(int j=0;j<4;j++) blocks[e][j]=4*e+j;
 for(int m=0;m<3;m++) for(int e=0;e<4;e++) for(int x=0;x<4;x++)
  blocks[4+4*m+e][x]=4*x+(mul4(m,x)^e);
 int groups[4][4]={{2,12,11,5},{3,4,13,10},{1,8,6,15},{0,9,7,14}};
 std::vector<Quad> quads;
 long long failures=0;
 for(int i=0;i<4;i++) for(int j=0;j<4;j++) for(int k=0;k<4;k++) {
  if(k==(i^j)) continue;
  int e=i^mul4(3,k)^mul4(2,j);
  Quad q; q.blocks={i,4+j,8+k,12+e}; q.group=-1;
  std::array<int,16> degrees{};
  for(int b:q.blocks) for(int x:blocks[b]) degrees[x]++;
  for(int s=0;s<4;s++) {
   int count=0;
   for(int x:blocks[q.blocks[s]]) if(degrees[x]==1) { q.labels[s]=x; count++; }
   if(count!=1) failures++;
  }
  for(int g=0;g<4;g++) {
   std::array<int,4> permutation{}; bool good=true;
   for(int s=0;s<4;s++) {
    int pos=0; while(pos<4 && groups[g][pos]!=q.labels[s]) pos++;
    if(pos==4) good=false; permutation[s]=pos;
   }
   if(good) { if(q.group!=-1) failures++; q.group=g; q.permutation=permutation; }
  }
  if(q.group<0) failures++;
  quads.push_back(q);
 }
 incidence<<"{\"block_index\":\"V0..V3,M0D0..M0D3,M1D0..M1D3,M2D0..M2D3\","
          <<"\"point_index\":\"row-major L072 table\",\"quadruples\":[";
 for(size_t n=0;n<quads.size();n++) {
  auto q=quads[n]; if(n) incidence<<','; incidence<<"{\"blocks\":[";
  for(int s=0;s<4;s++) { if(s) incidence<<','; incidence<<q.blocks[s]; }
  incidence<<"],\"singletons\":[";
  for(int s=0;s<4;s++) { if(s) incidence<<','; incidence<<q.labels[s]; }
  incidence<<"],\"ratio_group\":"<<q.group<<",\"permutation\":[";
  for(int s=0;s<4;s++) { if(s) incidence<<','; incidence<<q.permutation[s]; }
  incidence<<"]}";
 }
 incidence<<"]}\n"; incidence.close();
 if(failures || quads.size()!=48) { std::cerr<<"FAIL: incidence construction\n"; return 1; }
 rows<<"A,B,C,D,status,first_collision_i,first_collision_j,first_failed_quad\n";
 long long input_rows=0,candidates=0,collision_count=0,equation_rejected=0,passed=0;
 std::map<int,long long> rejection_hist;
 std::string line; std::getline(input,line);
 while(std::getline(input,line)) {
  std::stringstream ss(line); std::vector<std::string> fields; std::string value;
  while(std::getline(ss,value,',')) fields.push_back(value);
  input_rows++;
  if(fields.size()!=10) { failures++; continue; }
  if(fields[6]!="unique_distinct") continue;
  candidates++;
  std::array<int,4> ratios;
  for(int i=0;i<4;i++) ratios[i]=std::stoi(fields[i]);
  int a=ratios[0],b=ratios[1],c=ratios[2];
  int d1=std::stoi(fields[7]),d2=std::stoi(fields[8]),d3=std::stoi(fields[9]);
  int h[]={0,f((1-(1-b)*c*d3)*inv[b]),f((1-(1-c)*a*d1)*inv[c]),f((1-(1-a)*b*d2)*inv[a])};
  int dd[]={1,d1,d2,d3};
  int ee[]={f((h[1]+(a-1)*d3)*inv[a]),f(b*d2),f(c*d3),f(a*d1)};
  std::array<Point,16> points;
  points[0]={0,1};
  for(int i=0;i<4;i++) { points[4+i]=finite(h[i]); points[8+i]=finite(dd[i]); points[12+i]=finite(ee[i]); }
  int vr[]={f((c-1)*inv[c]),f((a-1)*inv[a]),f((b-1)*inv[b])};
  for(int i=1;i<4;i++) points[i]={f(ee[i]-vr[i-1]),f(ee[i]*(1-vr[i-1]))};
  int ci=-1,cj=-1,failed=-1;
  for(int i=0;i<16;i++) for(int j=0;j<i;j++) if(!bracket(points[i],points[j]) && ci<0) { ci=i; cj=j; }
  std::string status;
  if(ci>=0) { collision_count++; status="sixteen_direction_collision"; }
  else {
   for(size_t n=0;n<quads.size();n++) {
    auto q=quads[n];
    std::array<Point,4> canonical={Point{0,1},finite(0),finite(1),finite(ratios[q.group])};
    Point x[4],t[4];
    for(int i=0;i<4;i++) { x[i]=canonical[q.permutation[i]]; t[i]=points[q.blocks[i]]; }
    int num=f(bracket(x[0],x[2])*bracket(x[1],x[3]));
    int den=f(bracket(x[0],x[3])*bracket(x[1],x[2]));
    if(!den) { failures++; break; }
    int left=f(bracket(t[0],t[2])*bracket(t[1],t[3]));
    int right=f(bracket(t[0],t[3])*bracket(t[1],t[2]));
    if(f(left*den-right*num) && failed<0) failed=int(n);
   }
   if(failed>=0) { equation_rejected++; rejection_hist[failed]++; status="equation_rejected"; }
   else {
    passed++; status="all_48_pass";
    passing<<"{\"ratios\":["<<a<<','<<b<<','<<c<<','<<ratios[3]<<"],\"directions\":[";
    for(int i=0;i<16;i++) { if(i) passing<<','; passing<<'['<<points[i][0]<<','<<points[i][1]<<']'; }
    passing<<"]}\n";
   }
  }
  rows<<a<<','<<b<<','<<c<<','<<ratios[3]<<','<<status<<','<<ci<<','<<cj<<','<<failed<<'\n';
 }
 rows.close(); passing.close();
 if(input_rows!=847570||candidates!=672024||candidates!=collision_count+equation_rejected+passed) failures++;
 std::ofstream cert(prefix+".json");
 cert<<"{\n\"scope\":\"Complete admissible four-ratio necessary system, all 48 equations; no H-labeling enumeration or moment sufficiency\",\n"
     <<"\"required\":{\"input_rows\":847570,\"V0_distinct_candidates\":672024,\"quadrilaterals\":48,\"failures\":0},\n"
     <<"\"actual\":{\"input_rows\":"<<input_rows<<",\"V0_distinct_candidates\":"<<candidates<<",\"quadrilaterals\":"<<quads.size()
     <<",\"sixteen_direction_collision\":"<<collision_count<<",\"equation_rejected\":"<<equation_rejected
     <<",\"all_48_pass\":"<<passed<<",\"failures\":"<<failures<<"},\n\"first_failed_quad_histogram\":{";
 bool first=true; for(auto [key,count]:rejection_hist) { if(!first) cert<<','; first=false; cert<<'"'<<key<<"\":"<<count; }
 cert<<"},\n\"full_rows\":\""<<prefix<<"-rows.csv\",\n\"passing\":\""<<prefix<<"-passing.jsonl\",\n"
     <<"\"incidence\":\""<<prefix<<"-incidence.json\",\n\"failures\":"<<(failures?"[\"verification failure; see actual count\"]":"[]")<<"\n}\n";
 cert.close();
 std::cout<<(failures?"FAIL":"PASS")<<": original rows "<<input_rows<<"/847570; candidates "<<candidates
          <<"/672024; collisions "<<collision_count<<"; equation rejections "<<equation_rejected
          <<"; all-48 survivors "<<passed<<"; failures "<<failures<<"/0.\nCertificates: "<<prefix
          <<".json, "<<prefix<<"-rows.csv, "<<prefix<<"-passing.jsonl, "<<prefix<<"-incidence.json\n";
 return failures>0;
}
