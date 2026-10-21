// Two antipodal pairs, arbitrary W; stop at a four-scalar fiber. replay uses L057's original beta
// equations, not the producer's six-singleton interpolation evaluator.
#include <array>
#include <bitset>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
int md(int x) { x%=97; return x<0 ? x+97 : x; }
int iv[97], pw[97][9];
vector<int> H, anti;
struct Support { array<int,4> k; int mask; array<int,97> f{};
                 int inverse[4][4]{}; };
vector<Support> supports;
void require(bool b, const string& s) { if (!b) throw runtime_error(s); }
void initialize() {
  for(int x=1;x<97;x++) {
    for(int y=1;y<97;y++) if(x*y%97==1) iv[x]=y;
    pw[x][0]=1; for(int j=1;j<=8;j++) pw[x][j]=pw[x][j-1]*x%97;
    int t=1; for(int j=0;j<16;j++) t=t*x%97;
    if(t==1) { H.push_back(x); if(x<97-x) anti.push_back(x); }
  }
  for(int i=0;i<16;i++) for(int j=i+1;j<16;j++)
  for(int k=j+1;k<16;k++) for(int l=k+1;l<16;l++) {
    Support s; s.k={H[i],H[j],H[k],H[l]};
    s.mask=(1<<i)|(1<<j)|(1<<k)|(1<<l);
    for(int x:H) { int f=1; for(int y:s.k) f=md(f*(x-y)); s.f[x]=f; }
    int mat[4][8]{};
    for(int r=0;r<4;r++) { for(int c=0;c<4;c++) mat[r][c]=pw[s.k[c]][r+1]; mat[r][r+4]=1; }
    for(int c=0;c<4;c++) {
      int r=c; while(r<4 && !mat[r][c]) r++; require(r<4,"singular Vandermonde");
      for(int j=0;j<8;j++) swap(mat[r][j],mat[c][j]);
      int z=iv[mat[c][c]]; for(int j=0;j<8;j++) mat[c][j]=mat[c][j]*z%97;
      for(int r2=0;r2<4;r2++) if(r2!=c) { z=mat[r2][c]; for(int j=0;j<8;j++) mat[r2][j]=md(mat[r2][j]-z*mat[c][j]); }
    }
    for(int r=0;r<4;r++) for(int c=0;c<4;c++) s.inverse[r][c]=mat[r][c+4];
    supports.push_back(s);
  }
  require(H.size()==16 && anti.size()==8 && supports.size()==1820,"coverage setup");
}
using Row=array<uint8_t,5>; // kind, mu, p, q, r. kind 4 retains zero weights.
struct Evaluation { Row row{}; array<int,97> p{},q{},r{}; };
vector<Evaluation> interpolated(const array<int,6>& S) {
  int dinv[97]{};
  for(int x:S) { int d=1; for(int y:S) if(y!=x) d=md(d*(x-y)); dinv[x]=iv[d]; }
  vector<Evaluation> result;
  for(const Support& f:supports) {
    Evaluation e;
    int uy=md(f.f[S[0]]*dinv[S[0]]+f.f[S[1]]*dinv[S[1]]);
    int uz=md(f.f[S[2]]*dinv[S[2]]+f.f[S[3]]*dinv[S[3]]);
    if(!uy && !uz) e.row[0]=0;
    else if(!uy || !uz) e.row[0]=1;
    else {
      int mu=uz*iv[uy]%97; e.row[1]=mu;
      if(mu==96) e.row[0]=2;
      else {
        e.row[0]=3;
        for(int x:H) if(f.f[x]) {
          bool singleton=false; for(int y:S) singleton|=(x==y); if(singleton) continue;
          int sx=1; for(int y:S) sx=md(sx*(x-y));
          int ty=0,tz=0;
          for(int i=0;i<4;i++) {
            int t=md(f.f[S[i]]*dinv[S[i]]%97 * iv[md(x-S[i])]);
            if(i<2) ty=md(ty+t); else tz=md(tz+t);
          }
          int R=md(sx*md(tz-mu*ty)%97*iv[f.f[x]]);
          e.p[x]=md((1-R)*iv[md(1+mu)]);
          e.q[x]=md(-R*iv[mu]); e.r[x]=R;
        }
      }
    }
    result.push_back(e);
  }
  return result;
}
Row original_row(const Support& f, const array<int,6>& S,
                 const array<int,3>& P, const array<int,97>& cx,
                 uint64_t& moment_tests,uint64_t& zero_weights) {
  int vy=0,vz=0;
  for(int i=0;i<4;i++) {
    int x=S[i],gp=1; for(int t:P) gp=md(gp*(x-t));
    int v=md(cx[x]*x%97*f.f[x]%97*gp);
    if(i<2) vy=md(vy+v); else vz=md(vz+v);
  }
  if(!vy && !vz) return {0,0,0,0,0};
  if(!vy || !vz) return {1,0,0,0,0};
  int mu=vz*iv[vy]%97; if(mu==96) return {2,96,0,0,0};
  int by[3]{},bz[3]{};
  for(int j=0;j<3;j++) {
    int x=P[j],den=1; for(int t:P) if(t!=x) den=md(den*(x-t));
    for(int i=0;i<4;i++) {
      int y=S[i],ell=iv[den]; for(int t:P) if(t!=x) ell=md(ell*(y-t));
      int v=md(-cx[y]*y%97*f.f[y]%97*ell%97*iv[md(x*f.f[x])]);
      if(i<2) by[j]=md(by[j]+v); else bz[j]=md(bz[j]+v);
    }
  }
  int p=md((1-md((bz[0]-mu*by[0])*iv[cx[P[0]]]))*iv[md(1+mu)]);
  int q=md((by[1]-bz[1]*iv[mu])*iv[cx[P[1]]]);
  int r=md((bz[2]-mu*by[2])*iv[cx[P[2]]]);
  bool gated=p!=0&&p!=1&&q!=0&&q!=1&&r!=0&&r!=1;
  Row row={uint8_t(gated?4:3),uint8_t(mu),uint8_t(p),uint8_t(q),uint8_t(r)};
  if(gated) {
    int n[8]{},w[4]{};
    int d[3]={md(1-(1+mu)*p),md(-mu*q),r};
    for(int j=0;j<8;j++) {
      for(int i=0;i<4;i++) n[j]=md(n[j]+(i<2?-mu:1)*cx[S[i]]%97*pw[S[i]][j+1]);
      for(int i=0;i<3;i++) n[j]=md(n[j]+cx[P[i]]*d[i]%97*pw[P[i]][j+1]);
    }
    bool zero=false;
    for(int i=0;i<4;i++) { for(int j=0;j<4;j++) w[i]=md(w[i]+f.inverse[i][j]*n[j]); zero|=(w[i]==0); }
    for(int j=0;j<8;j++) { int v=0; for(int i=0;i<4;i++) v=md(v+w[i]*pw[f.k[i]][j+1]); require(v==n[j],"eight-moment failure"); }
    moment_tests++; zero_weights+=zero;
  }
  return row;
}
int main(int argc,char**argv) {
 try {
  require(argc==4,"usage: executable produce|replay packed-certificate summary-json");
  bool replay=string(argv[1])=="replay"; require(replay || string(argv[1])=="produce","mode");
  initialize();
  fstream packed(argv[2],ios::binary|(replay?ios::in:ios::out|ios::trunc)); require(bool(packed),"certificate open");
  uint64_t rows=0,counts[5]{},moment_tests=0,zero_weights=0;
  int assignments=0,paircases=0,globalmax=0; vector<int> maxima;
  vector<int> histogram(98); array<int,3> maxP{}; array<int,6> maxS{};
  int maxweight=0; bitset<97> maxscalars;
  for(int z:anti) if(z!=1) for(int wi=0;wi<16;wi++) for(int wj=wi+1;wj<16;wj++) {
    int w=H[wi], w2=H[wj];
    if(w==1 || w==96 || w==z || w==97-z || w2==1 || w2==96 || w2==z || w2==97-z) continue;
    array<int,6>S={1,96,z,97-z,w,w2}; paircases++;
    vector<Evaluation> eval; if(!replay) eval=interpolated(S);
    vector<int> outside;
    for(int x:H) { bool in=false; for(int t:S) in|=(x==t); if(!in) outside.push_back(x); }
    require(outside.size()==10,"outside coverage");
    for(int a:outside) for(int b:outside) if(b!=a) for(int c:outside) if(c!=a&&c!=b) {
      array<int,3>P={a,b,c}; int pmask=0;
      for(int i=0;i<16;i++) if(H[i]==a||H[i]==b||H[i]==c) pmask|=1<<i;
      array<int,97>cx{};
      if(replay) {
        for(int x:H) { bool in=false; for(int t:S) in|=(x==t); for(int t:P) in|=(x==t); if(!in) continue;
          int v=1; for(int h:H) { bool used=false; for(int t:S) used|=(h==t); for(int t:P) used|=(h==t); if(!used) v=md(v*(x-h)); } cx[x]=v; }
      }
      unordered_map<int,bitset<97>> fibers; int localrows=0;
      for(size_t i=0;i<supports.size();i++) if(!(supports[i].mask&pmask)) {
        Row row;
        if(replay) {
          row=original_row(supports[i],S,P,cx,moment_tests,zero_weights);
          Row saved; packed.read(reinterpret_cast<char*>(saved.data()),5);
          require(bool(packed),"truncated certificate"); require(saved==row,"complete row replay mismatch");
        } else {
          const Evaluation&e=eval[i]; row=e.row;
          if(row[0]==3) {
            row[2]=e.p[a]; row[3]=e.q[b]; row[4]=e.r[c];
            if(row[2]!=0&&row[2]!=1&&row[3]!=0&&row[3]!=1&&row[4]!=0&&row[4]!=1) row[0]=4;
          }
          packed.write(reinterpret_cast<const char*>(row.data()),5); require(bool(packed),"certificate write");
        }
        counts[row[0]]++; rows++; localrows++;
        if(row[0]==4) fibers[row[2]+97*row[3]+9409*row[4]].set(row[1]);
      }
      require(localrows==715,"support coverage"); int maximum=0;
      for(const auto& entry:fibers) {
        int n=entry.second.count(); maximum=max(maximum,n); histogram[n]++;
        if(n>globalmax) { globalmax=n; maxP=P; maxS=S; maxweight=entry.first; maxscalars=entry.second; }
      }
      maxima.push_back(maximum); assignments++;
      if(globalmax>=4 && !replay) goto enumeration_end;
    }
  }
enumeration_end:
  bool complete=paircases==462 && assignments==332640 && rows==237837600;
  if(replay) { char tail; require(!packed.read(&tail,1),"trailing certificate bytes"); }
  packed.close(); require(complete || (globalmax>=4 && !replay),"unfinished coverage without witness");
  ofstream out(argv[3]); require(bool(out),"summary open");
  out<<"{\n\"coverage_complete\":"<<(complete?"true":"false")<<",\n\"mode\":\""<<(replay?"replay":"produce")<<"\",\n"
     <<"\"scope\":\"two ordered antipodal singleton pairs, arbitrary unordered W, ordered shared triples; subgroup normalization\",\n"
     <<"\"actual_pair_cases\":"<<paircases<<",\"required_pair_cases\":462,\n"
     <<"\"actual_assignments\":"<<assignments<<",\"required_assignments\":332640,\n"
     <<"\"actual_support_rows\":"<<rows<<",\"required_support_rows\":237837600,\n"
     <<"\"certificate_bytes\":"<<rows*5<<",\"maximum_isolated_disjoint_P\":"<<globalmax<<",\"required_four_anchor_threshold\":4,\n"
     <<"\"row_counts\":[";
  for(int i=0;i<5;i++) { if(i) out<<","; out<<counts[i]; }
  out<<"],\n\"all_eight_moment_tests\":"<<moment_tests<<",\"zero_fourth_weight_rows_retained\":"<<zero_weights<<",\n"
     <<"\"failures\":[],\"actual_failures\":0,\"required_failures\":0,\n\"maximum_witness\":{\"P\":[";
  for(int i=0;i<3;i++){if(i)out<<",";out<<maxP[i];}out<<"],\"S_Y_Z_W\":[";
  for(int i=0;i<6;i++){if(i)out<<",";out<<maxS[i];}out<<"],\"weights\":["<<maxweight%97<<","<<(maxweight/97)%97<<","<<maxweight/9409<<"],\"scalars\":[";
  bool first=true;for(int i=0;i<97;i++)if(maxscalars[i]){if(!first)out<<",";first=false;out<<i;}out<<"]},\n\"fiber_histogram\":{";
  first=true;for(int i=0;i<98;i++)if(histogram[i]){if(!first)out<<",";first=false;out<<"\""<<i<<"\":"<<histogram[i];}out<<"},\n\"maximum_by_assignment\":[";
  for(size_t i=0;i<maxima.size();i++){if(i)out<<",";out<<maxima[i];}out<<"]\n}\n";
  out.close(); require(bool(out),"summary write");
  cout<<"Assignments "<<assignments<<"/332640; rows "<<rows<<"/237837600; isolated maximum "<<globalmax<<"; required anchors 4; failures 0/0\n";
  cout<<"Eight-moment checks "<<moment_tests<<"; zero fourth weights retained "<<zero_weights<<"\nCertificate: "<<argv[2]<<"\nSummary: "<<argv[3]<<"\n";
 } catch(const exception&e) { cerr<<"FAILURE: "<<e.what()<<"\n"; return 1; }
}
