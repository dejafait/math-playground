// Complete F_97 ratio-system test. No H-labeling or realization census.
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using Row = std::array<int,4>;
using Matrix = std::array<Row,5>;
int f(long long x) { x%=97; return int(x<0?x+97:x); }
int inv[97];
int rank(Matrix m, int columns) {
 int n=0;
 for(int c=0;c<columns && n<5;c++) {
  int p=n; while(p<5 && !m[p][c]) p++;
  if(p==5) continue;
  std::swap(m[p],m[n]); int scale=inv[m[n][c]];
  for(int j=0;j<4;j++) m[n][j]=f(m[n][j]*scale);
  for(int i=0;i<5;i++) if(i!=n) {
   int q=m[i][c]; for(int j=0;j<4;j++) m[i][j]=f(m[i][j]-q*m[n][j]);
  }
  n++;
 }
 return n;
}
Matrix rref(Matrix m) {
 int n=0;
 for(int c=0;c<3 && n<5;c++) {
  int p=n; while(p<5 && !m[p][c]) p++;
  if(p==5) continue;
  std::swap(m[p],m[n]); int scale=inv[m[n][c]];
  for(int j=0;j<4;j++) m[n][j]=f(m[n][j]*scale);
  for(int i=0;i<5;i++) if(i!=n) {
   int q=m[i][c]; for(int j=0;j<4;j++) m[i][j]=f(m[i][j]-q*m[n][j]);
  }
  n++;
 }
 return m;
}
Matrix matrix(int a,int b,int c,int d) {
 return {{
  Row{f(a*b),f(-b*d),f((1-d)*(1-b)*c),f(d-1)},
  Row{f((1-c)*a),f(c*b*d),f(-c*(d-1)),96},
  Row{a,f(d*(1-a)*b),f(-a*(1-d)*c),f(-d)},
  Row{f(a*a*(1-c)-a*c*(b-1)),0,f(c*(b*(a-1)-c*(1-b))),f(c-a)},
  Row{0,f(b*b*(1-a)-a*b*(c-1)),f(b*c*(a-1)-c*c*(1-b)),f(c-b)}
 }};
}
int main(int argc,char **argv) {
 if(argc!=2) { std::cerr<<"Usage: affine_plane_affine_rank output-prefix\n"; return 2; }
 std::string prefix=argv[1];
 std::ofstream rows(prefix+"-rows.csv"), drops(prefix+"-rank-drops.jsonl");
 rows<<"A,B,C,D,coefficient_rank,augmented_rank,status,d1,d2,d3\n";
 if(!rows || !drops) return 2;
 for(int a=1;a<97;a++) for(int b=1;b<97;b++) if(f(a*b)==1) inv[a]=b;
 std::array<std::vector<int>,97> roots;
 for(int x=0;x<97;x++) roots[f(x*x)].push_back(x);
 long long triples=0, tuples=0, failures=0, unique=0, distinct=0, drops_count=0;
 int max_roots=0;
 std::map<std::string,long long> histogram;
 std::array<int,4> first_distinct{};
 std::array<int,12> first_directions{};
 const int js[12]={0,0,0,1,1,1,2,2,2,3,3,3};
 const int ks[12]={1,2,3,0,2,3,0,1,3,0,1,2};
 const int ls[12]={3,1,2,2,3,0,3,0,1,1,2,0};
 for(int a=2;a<97;a++) for(int b=2;b<97;b++) for(int c=2;c<97;c++) {
  triples++;
  int u=f(a+b-a*b-a*c), v=f(a+c-a*c-b*c);
  int leading=f(v*v), linear=f(-2*u*v+4LL*b*c*(1-a)*(1-b)), constant=f(u*u);
  std::vector<int> ds;
  if(!leading) {
   if(!linear) { failures++; continue; }
   ds.push_back(f(-constant*inv[linear]));
  } else {
   int disc=f(linear*linear-4*leading*constant);
   for(int s:roots[disc]) ds.push_back(f((-linear+s)*inv[f(2*leading)]));
  }
  if(int(ds.size())>max_roots) max_roots=int(ds.size());
  for(int d:ds) {
   if(d==0 || d==1) continue;
   tuples++;
   if(f(leading*d*d+linear*d+constant)) failures++;
   Matrix m=matrix(a,b,c,d); int cr=rank(m,3), ar=rank(m,4);
   std::string status; std::array<int,3> x{-1,-1,-1};
   if(ar>cr) status="inconsistent";
   else if(cr==3) {
    unique++; Matrix rr=rref(m);
    for(int i=0;i<3;i++) x[i]=f(-rr[i][3]);
    for(auto row:m) if(f(row[0]*x[0]+row[1]*x[1]+row[2]*x[2]+row[3])) failures++;
    int h[4]={0,f((1-(1-b)*c*x[2])*inv[b]),
                 f((1-(1-c)*a*x[0])*inv[c]),
                 f((1-(1-a)*b*x[1])*inv[a])};
    int dd[4]={1,x[0],x[1],x[2]};
    int e[4]={f((h[1]+(a-1)*x[2])*inv[a]),f(b*x[1]),f(c*x[2]),f(a*x[0])};
    int ratios[12]={a,b,c,inv[f(1-b)],d,f((a-1)*inv[a]),
                   inv[f(1-c)],f((b-1)*inv[b]),f((d-1)*inv[d]),
                   inv[f(1-a)],inv[f(1-d)],f((c-1)*inv[c])};
    for(int i=0;i<12;i++) if(f(e[ls[i]]-(1-ratios[i])*h[js[i]]-ratios[i]*dd[ks[i]])) failures++;
    std::array<int,12> vals;
    for(int i=0;i<4;i++) { vals[i]=h[i]; vals[4+i]=dd[i]; vals[8+i]=e[i]; }
    bool collision=false;
    for(int i=0;i<12;i++) for(int j=0;j<i;j++) if(vals[i]==vals[j]) collision=true;
    status=collision?"unique_collision":"unique_distinct";
    if(!collision) { distinct++; if(distinct==1) { first_distinct={a,b,c,d}; first_directions=vals; } }
   } else status="consistent_rank_drop";
   std::string key=std::to_string(cr)+","+std::to_string(ar)+","+status;
   histogram[key]++;
   rows<<a<<','<<b<<','<<c<<','<<d<<','<<cr<<','<<ar<<','<<status;
   for(int y:x) rows<<','<<y;
   rows<<'\n';
   if(cr<3) {
    drops_count++; Matrix rr=rref(m);
    drops<<"{\"ratios\":["<<a<<','<<b<<','<<c<<','<<d<<"],\"coefficient_rank\":"<<cr
         <<",\"augmented_rank\":"<<ar<<",\"rref\":[";
    for(int i=0;i<5;i++) { if(i) drops<<','; drops<<'[';
     for(int j=0;j<4;j++) { if(j) drops<<','; drops<<rr[i][j]; } drops<<']'; }
    drops<<"]}\n";
   }
  }
 }
 rows.close(); drops.close();
 std::ofstream cert(prefix+".json");
 cert<<"{\n\"scope\":\"Complete admissible F_97 V0 ratio systems; no H-labeling census, no realization\",\n"
     <<"\"required\":{\"triples\":857375,\"max_roots_per_triple\":2,\"arithmetic_failures\":0},\n"
     <<"\"actual\":{\"triples\":"<<triples<<",\"R_zero_tuples\":"<<tuples
     <<",\"unique_affine_solutions\":"<<unique<<",\"unique_distinct_solutions\":"<<distinct
     <<",\"coefficient_rank_drops\":"<<drops_count<<",\"max_roots_per_triple\":"<<max_roots
     <<",\"arithmetic_failures\":"<<failures<<"},\n"
     <<"\"histogram\":{";
 bool first=true; for(auto [key,count]:histogram) { if(!first) cert<<','; first=false; cert<<'"'<<key<<"\":"<<count; }
 cert<<"},\n\"first_unique_distinct\":{\"ratios\":[";
 for(int i=0;i<4;i++) { if(i) cert<<','; cert<<first_distinct[i]; }
 cert<<"],\"directions_h_d_e\":[";
 for(int i=0;i<12;i++) { if(i) cert<<','; cert<<first_directions[i]; }
 cert<<"]},\n\"full_rows\":\""<<prefix<<"-rows.csv\",\n\"full_rank_drops\":\""<<prefix
     <<"-rank-drops.jsonl\",\n\"failures\":"<<(failures?"[\"arithmetic failure; see actual count\"]":"[]")<<"\n}\n";
 cert.close();
 std::cout<<(failures?"FAIL":"PASS")<<": triples "<<triples<<"/857375; R=0 tuples "<<tuples
          <<"/1714750 bound; unique "<<unique<<"; distinct "<<distinct<<"; rank drops "<<drops_count
          <<"; arithmetic failures "<<failures<<"/0.\n";
 for(auto [key,count]:histogram) std::cout<<key<<": "<<count<<'\n';
 std::cout<<"Certificates: "<<prefix<<".json, "<<prefix<<"-rows.csv, "<<prefix<<"-rank-drops.jsonl\n";
 return failures || triples!=857375;
}
