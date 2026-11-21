// One fixed exact U12 compression. Original L2 coordinates, complete energy.
#include "elementary-875.hpp"
using Vec=array<I,12>;
using Mat=array<Vec,12>;
Mat gram;
Vec moments;
I dotG(Vec a,Vec b){I r(0);for(int i=0;i<12;i++)for(int j=0;j<12;j++)r=r+a[i]*gram[i][j]*b[j];return r;}
Vec addV(Vec a,Vec b){for(int i=0;i<12;i++)a[i]=a[i]+b[i];return a;}
Vec scaleV(I t,Vec a){for(auto &v:a)v=t*v;return a;}
Vec neutral(int index,int pivot){Vec a{};a[index]=I(1);a[pivot]=-moments[index]/moments[pivot];return a;}
Vec project(Vec r,Vec b,Vec c){
 I h00=dotG(b,b),h01=dotG(b,c),h11=dotG(c,c),det=h00*h11-sq(h01);
 if(det.l<=0)throw runtime_error("retained Gram determinant not positive");
 I p0=dotG(r,b),p1=dotG(r,c);
 I a=(h11*p0-h01*p1)/det, d=(h00*p1-h01*p0)/det;
 return addV(r,addV(scaleV(-a,b),scaleV(-d,c)));
}
I trial(I x,const Vec &c){I f(0);for(int j=0;j<12;j++)if(c[j].l!=0||c[j].h!=0)f=f+c[j]*phi(x,j+1);return f;}
J trialJ(J x,const Vec &c){J f;for(int j=0;j<12;j++)if(c[j].l!=0||c[j].h!=0)f=f+J(c[j])*phiJ(x,j+1);return f;}
Result eval872(const Vec &c,int n,const vector<C>&tw,const vector<I>&symbols){
 I step=I(64)/I(n);vector<C>a(n);I norm(0),deriv(0),b2(0);
 int stop=(int)ceil(T.h/step.l)+2;
 for(int j=0;j<=stop;j++)a[j].r=trial(I(j)*step,c);
 for(int j=0;j<=stop;j++){I u=a[j].r,v=a[j+1].r;norm=norm+step/I(3)*(sq(u)+u*v+sq(v));deriv=deriv+sq(u-v)/step;}
 const int panels=32768;I h=T/I(panels);
 for(int j=0;j<panels;j++){I x((I(j)*h).l,(I(j+1)*h).h);b2=b2+h*sq(trialJ(J(x,I(1)),c).dd);}
 fft(a,tw,false);I arch(0);
 for(int k=0;k<=n/2;k++){
  I sinc=k==0?I(1):sinI(PI*I(k)/I(n))/(PI*I(k)/I(n));
  I fq2=sq(step)*powi(sinc,4)*(sq(a[k].r)+sq(a[k].i));
  arch=arch+I(k==0?1:2)/I(64)*symbols[k]*fq2;
 }
 for(auto &z:a)z=C(sq(z.r)+sq(z.i));fft(a,tw,true);
 I prime(0),Cprime(0);
 for(auto [p,weight]:pp){I u=logI(I(p))/step;int m=(int)floor((u.l+u.h)/2);if(floor(u.l)!=m||floor(u.h)!=m)throw runtime_error("delay crosses cell");I corr(0);
  for(int j=m-2;j<=m+2;j++)corr=corr+step*a[(j+n)%n].r*b3(u-I(j));
  prime=prime+I(2)*weight*corr;Cprime=Cprime+I(2)*weight;
 }
 I R0=PI/step,A=I(2)+I(8)*sqrtI(I(2))/I(3)+logI(I(4)*PI);
 I tail=(A+logI(I(2)+R0))*deriv/sq(R0);
 // Use the prior diameter<9 bound unchanged: our diameter<4.4.
 I images=I(27)*norm*expI(-I(55)/I(2))/(I(1)-expI(-I(32)));
 I eps=powi(step,4)*b2,C0=A+logI(I(3));
 I ew=eps*(C0+logI(I(1)+I(1)/sq(step))/I(2));
 if(norm.l<=0)throw runtime_error("interpolant norm not positive");
 I qw=norm*(C0+logI(I(1)+deriv/norm)/I(2));
 I interp=I(2)*sqrtI(qw*ew)+ew+Cprime*(I(2)*sqrtI(norm*eps)+eps);
 I energy=widen(arch-prime,(tail+images+interp).h);
 return {norm,deriv,b2,arch,prime,tail,images,interp,energy,Cprime,ew,qw,eps};
}
void jsonV(Vec v){cout<<"[";for(int j=0;j<12;j++){if(j)cout<<",";jsonI(v[j]);}cout<<"]";}

using Small=array<array<I,5>,5>;
void jsonSmall(Small m){cout<<"[";for(int i=0;i<5;i++){if(i)cout<<",";cout<<"[";for(int j=0;j<5;j++){if(j)cout<<",";jsonI(m[i][j]);}cout<<"]";}cout<<"]";}
int main(){try{
 if(!numeric_limits<double>::is_iec559||numeric_limits<double>::digits!=53||fegetround()!=FE_TONEAREST)throw runtime_error("binary64 environment");
 volatile double tiny=numeric_limits<double>::denorm_min(),one=1;if(!(tiny*one>0))throw runtime_error("subnormals flushed");
 LOG2=logUnit(I(2));PI=I(16)*atanSmall(I(1)/I(5))-I(4)*atanSmall(I(1)/I(239));T=I(4)*logI(I(3));DELTA=T/I(40);
 const int nm=65536,n=262144;
 if((DELTA-I(64)/I(n)).l<=0||(T+I(128)/I(n)).h>=9)throw runtime_error("support");
 I h=T/I(nm);array<array<I,5>,12>pb;
 for(int j=0;j<12;j++)pb[j]=phiBounds(j+1);
 for(int l=0;l<=nm;l++){
  I x=I(l)*h,e=expI(x/I(2)),weight(l==0||l==nm?1:l%2?4:2);Vec f;
  for(int j=0;j<12;j++){f[j]=phi(x,j+1);moments[j]=moments[j]+weight*e*f[j];}
  for(int j=0;j<12;j++)for(int k=0;k<=j;k++)if((j-k)%2==0)gram[j][k]=gram[j][k]+weight*f[j]*f[k];
 }
 array<I,5> eb;for(int j=0;j<5;j++)eb[j]=I(9)/I(1<<j);
 for(int j=0;j<12;j++){
  moments[j]=widen(h/I(3)*moments[j],(T*powi(h,4)*mulBounds(eb,pb[j])[4]/I(180)).h);
  for(int k=0;k<=j;k++)if((j-k)%2==0)gram[k][j]=gram[j][k]=widen(h/I(3)*gram[j][k],(T*powi(h,4)*mulBounds(pb[j],pb[k])[4]/I(180)).h);
 }
 if(moments[0].l<=0||moments[1].h>=0)throw runtime_error("pivot moments");
 array<array<Vec,5>,2> basis;
 for(int p=0;p<2;p++){
  Vec b=neutral(p+2,p),c=neutral(p+4,p);basis[p][0]=b;basis[p][1]=c;
  for(int j=2;j<5;j++)basis[p][j]=project(neutral(p+2*j+2,p),b,c);
 }
 cerr<<"All12 moments, original metric and exact projection coefficients enclosed.\n";
 vector<int>primes;for(int p=2;p<81;p++){bool ok=true;for(int q:primes){if(q*q>p)break;if(p%q==0){ok=false;break;}}if(ok){primes.push_back(p);for(int k=p;k<81;){pp.push_back({k,logI(I(p))/sqrtI(I(k))});if(k>80/p)break;k*=p;}}}
 sort(pp.begin(),pp.end(),[](auto a,auto b){return a.first<b.first;});
 vector<C>tw(n/2);vector<I>symbols(n/2+1);for(int k=0;k<n/2;k++){I angle=-I(2)*PI*I(k)/I(n);tw[k]=C(cosI(angle),sinI(angle));}
 for(int k=0;k<=n/2;k++)symbols[k]=symbol(I(2)*PI*I(k)/I(64));
 cout<<setprecision(17)<<"{\"status\":\"ENTRY_ENCLOSURES_ONLY\",\"grid_size\":"<<n<<",\"moment_panels\":"<<nm<<",\"derivative_panels\":32768,\"period\":64,\"T\":";jsonI(T);
 cout<<",\"moments\":";jsonV(moments);cout<<",\"gram\":[";for(int j=0;j<12;j++){if(j)cout<<",";jsonV(gram[j]);}cout<<"],\"prime_powers\":[";for(int j=0;j<(int)pp.size();j++){if(j)cout<<",";cout<<pp[j].first;}cout<<"],\"sectors\":[";
 for(int p=0;p<2;p++){
  if(p)cout<<",";cout<<"{\"pivot_mode\":"<<p+1<<",\"basis\":[";for(int j=0;j<5;j++){if(j)cout<<",";jsonV(basis[p][j]);}cout<<"],\"basis_norms\":[";for(int j=0;j<5;j++){if(j)cout<<",";jsonI(dotG(basis[p][j],basis[p][j]));}cout<<"],\"diagonals\":[";
  array<Result,5>diags;Small energy;
  for(int j=0;j<5;j++){diags[j]=eval872(basis[p][j],n,tw,symbols);energy[j][j]=diags[j].energy;if(j)cout<<",";printResult(diags[j]);cout.flush();cerr<<"Sector "<<p<<" diagonal "<<j<<" ["<<energy[j][j].l<<","<<energy[j][j].h<<"].\n";}
  cout<<"],\"pairs\":[";bool first=true;
  for(int j=0;j<5;j++)for(int k=0;k<j;k++){
   Result r=eval872(addV(basis[p][j],basis[p][k]),n,tw,symbols);energy[j][k]=energy[k][j]=(r.energy-diags[j].energy-diags[k].energy)/I(2);
   if(!first)cout<<",";first=false;cout<<"{\"i\":"<<j<<",\"j\":"<<k<<",\"sum\":";printResult(r);cout<<",\"cross\":";jsonI(energy[j][k]);cout<<"}";cout.flush();cerr<<"Sector "<<p<<" pair "<<j<<","<<k<<" complete.\n";
  }
  cout<<"],\"energy_matrix\":";jsonSmall(energy);cout<<"}";cout.flush();
 }
 cout<<"],\"cross_parity_entries\":\"exactly_zero_by_reflection\",\"failures\":[]}\n";
 cerr<<"Full30 energy evaluations complete; signs require separate interval block check. Certificate scripts/neutral-exact-schur/certificate-875.json\n";
 }catch(const exception&e){cerr<<"FAILURE: "<<e.what()<<"\n";return 1;}}
