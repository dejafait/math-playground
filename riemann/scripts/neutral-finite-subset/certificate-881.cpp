// One fixed whole-box retained-zero test. No midpoint sample is evidence.
#include "../neutral-exact-schur/elementary-875.hpp"
#include "inputs-881.hpp"
using Vec=array<I,12>;
using Mat=array<Vec,12>;
Mat gram; Vec moments;
I dotG(Vec a,Vec b){I r(0);for(int i=0;i<12;i++)for(int j=0;j<12;j++)r=r+a[i]*gram[i][j]*b[j];return r;}
Vec addV(Vec a,Vec b){for(int i=0;i<12;i++)a[i]=a[i]+b[i];return a;}
Vec scaleV(I t,Vec a){for(auto &v:a)v=t*v;return a;}
Vec neutral(int index,int pivot){Vec a{};a[index]=I(1);a[pivot]=-moments[index]/moments[pivot];return a;}
Vec project(Vec r,Vec b,Vec c){
 I h00=dotG(b,b),h01=dotG(b,c),h11=dotG(c,c),det=h00*h11-sq(h01);
 if(det.l<=0)throw runtime_error("retained Gram determinant not positive");
 I p0=dotG(r,b),p1=dotG(r,c);
 I a=(h11*p0-h01*p1)/det,d=(h00*p1-h01*p0)/det;
 return addV(r,addV(scaleV(-a,b),scaleV(-d,c)));
}
void jsonV(Vec v){cout<<"[";for(int j=0;j<12;j++){if(j)cout<<",";jsonI(v[j]);}cout<<"]";}
int main(){try{
 if(!numeric_limits<double>::is_iec559||numeric_limits<double>::digits!=53||fegetround()!=FE_TONEAREST)throw runtime_error("binary64 environment");
 volatile double tiny=numeric_limits<double>::denorm_min(),one=1;if(!(tiny*one>0))throw runtime_error("subnormals flushed");
 LOG2=logUnit(I(2));PI=I(16)*atanSmall(I(1)/I(5))-I(4)*atanSmall(I(1)/I(239));T=I(4)*logI(I(3));DELTA=T/I(40);
 for(int j=0;j<12;j++){moments[j]=I(source_moments[j][0],source_moments[j][1]);for(int k=0;k<12;k++)gram[j][k]=I(source_gram[j][k][0],source_gram[j][k][1]);}
 array<array<Vec,5>,2>basis;
 for(int p=0;p<2;p++){Vec b=neutral(p+2,p),c=neutral(p+4,p);basis[p][0]=b;basis[p][1]=c;for(int j=2;j<5;j++)basis[p][j]=project(neutral(p+2*j+2,p),b,c);}
 // Decimal endpoints are dyadic; the EXTRA transport allowance is enclosed.
 double roots[10][2]={{14.111328125,14.16015625},{20.99609375,21.044921875},{25,25.048828125},{30.419921875,30.4443359375},{32.91015625,32.958984375},{37.548828125,37.59765625},{40.91796875,40.966796875},{43.310546875,43.3349609375},{47.998046875,48.0224609375},{49.755859375,49.7802734375}};
 I allowance=I(1)/I(1000000000000.0);
 array<I,10>frequencies;for(int z=0;z<10;z++)frequencies[z]=I((I(roots[z][0])-allowance).l,(I(roots[z][1])+allowance).h);
 const int panels=32768,half=panels/2;I ds=I(1)/I(panels);
 vector<Vec>values(half);vector<I>center(half);
 for(int n=0;n<half;n++){
  // s endpoints are exact dyadics, T remains an interval.
  I s(double(n)/panels,double(n+1)/panels);
  I cutoff=theta(I(40)*s-I(1))*theta(I(39)-I(40)*s);
  for(int k=0;k<12;k++)values[n][k]=cutoff*sinI(I(k+1)*PI*s);
  center[n]=T*(s-I(.5));
 }
 array<Vec,10>raw;
 for(int z=0;z<10;z++){
  Vec sum{};
  for(int n=0;n<half;n++){
   I phase=frequencies[z]*center[n],co=cosI(phase),si=sinI(phase);
   for(int k=0;k<12;k++)sum[k]=sum[k]+values[n][k]*(k%2?si:co);
  }
  for(int k=0;k<12;k++)raw[z][k]=I(2)*T*ds*sum[k];
  cerr<<"Root interval "<<z+1<<" of 10 enclosed.\n";
 }
 cout<<setprecision(17)<<"{\"status\":\"ENCLOSURES_ONLY\",\"full_window_panels\":"<<panels<<",\"half_window_panels\":"<<half<<",\"T\":";jsonI(T);
 cout<<",\"transport_allowance\":";jsonI(allowance);cout<<",\"frequencies\":[";for(int z=0;z<10;z++){if(z)cout<<",";jsonI(frequencies[z]);}
 cout<<"],\"raw_centered_samples\":[";for(int z=0;z<10;z++){if(z)cout<<",";jsonV(raw[z]);}
 cout<<"],\"sectors\":[";
 for(int p=0;p<2;p++){
  if(p)cout<<",";cout<<"{\"pivot_mode\":"<<p+1<<",\"basis\":[";for(int j=0;j<5;j++){if(j)cout<<",";jsonV(basis[p][j]);}
  array<array<I,5>,10> samples;
  cout<<"],\"samples\":[";for(int z=0;z<10;z++){
   if(z)cout<<",";cout<<"[";for(int j=0;j<5;j++){I a(0);for(int k=0;k<12;k++)a=a+basis[p][j][k]*raw[z][k];samples[z][j]=a;if(j)cout<<",";jsonI(a);}cout<<"]";
  }
  cout<<"],\"retained_gram\":[";
  for(int i=0;i<5;i++){if(i)cout<<",";cout<<"[";for(int j=0;j<5;j++){
   I entry(0);for(int z=0;z<10;z++)entry=entry+I(2)*(i==j?sq(samples[z][i]):samples[z][i]*samples[z][j]);
   if(j)cout<<",";jsonI(entry);
  }cout<<"]";}cout<<"]}";
 }
 cout<<"],\"cross_parity\":\"EXACT_ZERO_AFTER_PAIRING_BOTH_SIGNS\",\"failures\":[]}\n";
 }catch(const exception&e){cerr<<"FAILURE: "<<e.what()<<"\n";return 1;}}
