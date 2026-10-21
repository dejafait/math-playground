// Independent complete replay: brute-force D; eliminate the ORIGINAL twelve
// equations in ten unknowns, not L078's reduced matrix or quadratic roots.
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
int mod(int x) { int y=x%97; return y<0?y+97:y; }
int inverse(int x) {
 int result=1, base=mod(x), exponent=95;
 while(exponent) { if(exponent&1) result=mod(result*base); base=mod(base*base); exponent>>=1; }
 return result;
}
using Equation=std::array<int,11>;
using System=std::array<Equation,12>;
int eliminate(System &s,int width) {
 int used=0;
 for(int col=0;col<width && used<12;col++) {
  int pivot=used; while(pivot<12 && !s[pivot][col]) pivot++;
  if(pivot==12) continue;
  std::swap(s[pivot],s[used]); int factor=inverse(s[used][col]);
  for(int j=col;j<11;j++) s[used][j]=mod(s[used][j]*factor);
  for(int i=0;i<12;i++) if(i!=used && s[i][col]) {
   int multiple=s[i][col];
   for(int j=col;j<11;j++) s[i][j]=mod(s[i][j]-multiple*s[used][j]);
  }
  used++;
 }
 return used;
}
size_t index(int a,int b,int c,int d) {
 return (((size_t(a-2)*95+(b-2))*95+(c-2))*95+(d-2));
}
int main(int argc,char **argv) {
 if(argc!=2) return 2;
 std::string prefix=argv[1];
 std::ifstream input(prefix+"-rows.csv");
 std::ofstream full(prefix+"-replay.csv");
 if(!input || !full) return 2;
 full<<"A,B,C,D,original_coefficient_rank,original_augmented_rank,status,all_original_residuals_zero\n";
 std::vector<bool> seen(81450625,false);
 long long cases=0, failures=0, distinct=0, inconsistent=0, collision=0;
 std::map<std::string,long long> hist;
 int ji[]={0,0,0,1,1,1,2,2,2,3,3,3};
 int ki[]={1,2,3,0,2,3,0,1,3,0,1,2};
 int li[]={3,1,2,2,3,0,3,0,1,1,2,0};
 std::string line; std::getline(input,line);
 while(std::getline(input,line)) {
  std::stringstream ss(line); std::vector<std::string> fields; std::string value;
  while(std::getline(ss,value,',')) fields.push_back(value);
  if(fields.size()!=10) { failures++; continue; }
  int a=std::stoi(fields[0]),b=std::stoi(fields[1]),c=std::stoi(fields[2]),d=std::stoi(fields[3]);
  if(a<2||a>96||b<2||b>96||c<2||c>96||d<2||d>96) { failures++; continue; }
  size_t ix=index(a,b,c,d); if(seen[ix]) failures++; seen[ix]=true;
  int cr0=std::stoi(fields[4]),ar0=std::stoi(fields[5]);
  int r[]={a,b,c,inverse(1-b),d,mod((a-1)*inverse(a)),
           inverse(1-c),mod((b-1)*inverse(b)),mod((d-1)*inverse(d)),
           inverse(1-a),inverse(1-d),mod((c-1)*inverse(c))};
  System original{};
  for(int i=0;i<12;i++) {
   original[i][6+li[i]]=1;
   if(ji[i]) original[i][ji[i]-1]=mod(r[i]-1);
   if(ki[i]) original[i][ki[i]+2]=mod(-r[i]);
   else original[i][10]=mod(-r[i]);
  }
  System reduced=original, augmented=original;
  int cr=eliminate(reduced,10),ar=eliminate(augmented,11);
  if(cr!=cr0+7 || ar!=ar0+7) failures++;
  bool residuals_zero=true;
  std::string status;
  if(ar>cr) { status="inconsistent"; inconsistent++; }
  else if(cr!=10) { status="consistent_rank_drop"; failures++; }
  else {
   std::array<int,10> solution{};
   for(int j=0;j<10;j++) solution[j]=mod(-reduced[j][10]);
   for(int j=0;j<3;j++) if(solution[3+j]!=std::stoi(fields[7+j])) failures++;
   for(auto equation:original) {
    int sum=equation[10]; for(int j=0;j<10;j++) sum+=equation[j]*solution[j];
    if(mod(sum)) { residuals_zero=false; failures++; }
   }
   std::array<int,12> directions{};
   directions[0]=0; directions[4]=1;
   for(int j=1;j<4;j++) { directions[j]=solution[j-1]; directions[4+j]=solution[j+2]; }
   for(int j=0;j<4;j++) directions[8+j]=solution[6+j];
   bool bad=false;
   for(int j=0;j<12;j++) for(int k=0;k<j;k++) if(directions[j]==directions[k]) bad=true;
   status=bad?"unique_collision":"unique_distinct";
   if(bad) collision++; else distinct++;
  }
  if(status!=fields[6]) failures++;
  hist[std::to_string(cr)+","+std::to_string(ar)+","+status]++;
  full<<a<<','<<b<<','<<c<<','<<d<<','<<cr<<','<<ar<<','<<status<<',';
  if(ar>cr) full<<"NA"; else full<<(residuals_zero?"true":"false");
  full<<'\n'; cases++;
 }
 // Complete case-set equality by direct substitution for ALL 95^4 tuples.
 long long universe=0,zeros=0;
 for(int a=2;a<97;a++) for(int b=2;b<97;b++) for(int c=2;c<97;c++) for(int d=2;d<97;d++) {
  int u=mod(a+b-a*b-a*c),v=mod(a+c-a*c-b*c);
  int t=mod(u-d*v);
  bool zero=mod(t*t+mod(4*b*c)*mod(d*(1-a)*(1-b)))==0;
  if(zero) zeros++;
  if(zero!=seen[index(a,b,c,d)]) failures++;
  universe++;
 }
 full.close();
 if(cases!=847570 || zeros!=cases || inconsistent!=8648 || collision!=166898 || distinct!=672024) failures++;
 std::ofstream cert(prefix+"-replay.json");
 cert<<"{\n\"scope\":\"Full direct-D coverage and original twelve-equation replay; no H-label census\",\n"
     <<"\"required\":{\"ratio_universe\":81450625,\"R_zero_tuples\":847570,\"failures\":0},\n"
     <<"\"actual\":{\"ratio_universe\":"<<universe<<",\"R_zero_tuples\":"<<zeros<<",\"replayed\":"<<cases
     <<",\"inconsistent\":"<<inconsistent<<",\"unique_collision\":"<<collision
     <<",\"unique_distinct\":"<<distinct<<",\"failures\":"<<failures<<"},\n\"histogram\":{";
 bool first=true; for(auto [key,count]:hist) { if(!first) cert<<','; first=false; cert<<'"'<<key<<"\":"<<count; }
 cert<<"},\n\"full_replay\":\""<<prefix<<"-replay.csv\",\n\"failures\":"
     <<(failures?"[\"verification failure; see actual count\"]":"[]")<<"\n}\n";
 cert.close();
 std::cout<<(failures?"FAIL":"PASS")<<": universe "<<universe<<"/81450625; original systems "<<cases
          <<"/847570; inconsistent "<<inconsistent<<"/8648; collision "<<collision<<"/166898; distinct "<<distinct
          <<"/672024; failures "<<failures<<"/0.\nCertificates: "<<prefix<<"-replay.json, "<<prefix<<"-replay.csv\n";
 return failures>0;
}
