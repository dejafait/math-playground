// Self-contained outward binary64 interval certificate; no external libraries.
// Build: clang++ -O2 -std=c++17 -ffp-contract=off certificate-315.cpp -o /private/tmp/riemann-ims-315
// Run from notebook: /private/tmp/riemann-ims-315 > scripts/corrected-ims/certificate-315.json
// Elementary functions below use finite series with explicit remainders.
#include <algorithm>
#include <cfenv>
#include <array>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using namespace std;
double dn(double x){return nextafter(x,-INFINITY);}
double up(double x){return nextafter(x,INFINITY);}
struct I { double l,h;
 I(double x=0):l(x),h(x){if(!isfinite(x))throw runtime_error("nonfinite point");}
 I(double a,double b):l(a),h(b){if(!isfinite(a)||!isfinite(b)||a>b)throw runtime_error("invalid interval");}
};
double max_trig=0,max_atan=0,max_exp_base=0,max_delay_width=0;
double min_log_base=2,max_log_base=1,min_delay_cell_margin=1;
int simpson_calls=0,delay_calls=0;
I operator+(I a,I b){return {dn(a.l+b.l),up(a.h+b.h)};}
I operator-(I a){return {-a.h,-a.l};}
I operator-(I a,I b){return a+(-b);}
I operator*(I a,I b){double p[]={a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h};return {dn(*min_element(p,p+4)),up(*max_element(p,p+4))};}
I operator/(I a,I b){if(b.l<=0&&b.h>=0)throw runtime_error("zero interval denominator");return a*I(dn(1/b.h),up(1/b.l));}
I sq(I a){if(a.l>=0)return {dn(a.l*a.l),up(a.h*a.h)};if(a.h<=0)return sq(-a);return {0,up(max(a.l*a.l,a.h*a.h))};}
I ab(I a){if(a.l>=0)return a;if(a.h<=0)return -a;return {0,max(-a.l,a.h)};}
I powi(I a,int k){I r(1);for(int j=0;j<k;j++)r=r*a;return r;}
I hull(I a,I b){return {min(a.l,b.l),max(a.h,b.h)};}
I widen(I a,double r){return a+I(-r,r);}
I sqrtI(I a){if(a.h<0)throw runtime_error("negative sqrt");double l=sqrt(max(0.,a.l)),h=sqrt(max(0.,a.h));
 while(sq(I(l)).h>a.l&&l>0)l=dn(l);while(sq(I(h)).l<a.h)h=up(h);return {l,h};}
I expPoint(double x){
 if(x < -100) return {0,4e-44};
 int k=0;double z=x;while(abs(z)>.125){z*=.5;k++;}
 max_exp_base=max(max_exp_base,abs(z)); if(abs(z)>.125)throw runtime_error("exp base"); I v(z),sum(1),term(1);for(int n=1;n<=18;n++){term=term*v/I(n);sum=sum+term;}
 // |z|<=1/8: exponential Taylor remainder < 2^-100.
 sum=widen(sum,0x1p-100);for(int j=0;j<k;j++)sum=sq(sum);return sum;
}
I expI(I x){return {expPoint(x.l).l,expPoint(x.h).h};}
I logUnit(I x){if(x.l<1||x.h>2)throw runtime_error("log base"); min_log_base=min(min_log_base,x.l);max_log_base=max(max_log_base,x.h);I t=(x-I(1))/(x+I(1)),t2=sq(t),term=t,sum(0);for(int j=0;j<60;j++){sum=sum+term/I(2*j+1);term=term*t2;}
 // x in [1,2], |t|<=1/3; 120-term-power geometric tail < 2^-180.
 return widen(I(2)*sum,0x1p-180);
}
I LOG2;
I logPoint(double x){if(x<=0)throw runtime_error("nonpositive log");int e;double m=frexp(x,&e);m*=2;e--;return logUnit(I(m))+I(e)*LOG2;}
I logI(I x){return {logPoint(x.l).l,logPoint(x.h).h};}
I atanSmall(I x){max_atan=max(max_atan,max(abs(x.l),abs(x.h)));if(max_atan>.25)throw runtime_error("atan domain");I t=x,sum(0);for(int j=0;j<90;j++){sum=sum+((j%2)?-t:t)/I(2*j+1);t=t*sq(x);}return widen(sum,0x1p-300);}
I PI,T,ELL,R,DELTA;
I sinSmall(I x){max_trig=max(max_trig,max(abs(x.l),abs(x.h)));if(max_trig>4)throw runtime_error("trig domain");I term=x,sum=x;for(int n=1;n<=32;n++){term=-term*sq(x)/I((2*n)*(2*n+1));sum=sum+term;}return widen(sum,0x1p-160);}
I cosSmall(I x){max_trig=max(max_trig,max(abs(x.l),abs(x.h)));if(max_trig>4)throw runtime_error("trig domain");I term(1),sum(1);for(int n=1;n<=32;n++){term=-term*sq(x)/I((2*n-1)*(2*n));sum=sum+term;}return widen(sum,0x1p-150);}
// Arguments reduced to [-pi,pi]; initial arguments here have |x|<20.
I sinI(I x){int n=(int)nearbyint((x.l+x.h)/(4*PI.l));return sinSmall(x-I(2*n)*PI);}
I cosI(I x){int n=(int)nearbyint((x.l+x.h)/(4*PI.l));return cosSmall(x-I(2*n)*PI);}
I eta(I s){if(s.h<=0)return I(0);if(s.l<=0)return {0,expI(-I(1)/I(s.h)).h};return expI(-I(1)/s);}
I theta(I s){if(s.h<=0)return I(0);if(s.l>=1)return I(1);I v=eta(s)/(eta(s)+eta(I(1)-s));return {max(0.,v.l),min(1.,v.h)};}
I beta(I x,I c){return eta(I(1)-sq((x-c)/R));}
I phi(I x,int k){if(x.h<=DELTA.l||x.l>=(T-DELTA).h)return I(0);return theta((x-DELTA)/DELTA)*theta((T-DELTA-x)/DELTA)*sinI(I(k)*PI*x/T);}
I rho(I x){return cosI(PI/I(2)*theta((x-I(3)*logI(I(3)))/(I(2)*logI(I(3)))));}

// Second-derivative jets, with ordinary (not factorial-divided) entries.
struct J {I v,d,dd;J(I a=I(0),I b=I(0),I c=I(0)):v(a),d(b),dd(c){} };
J operator+(J a,J b){return {a.v+b.v,a.d+b.d,a.dd+b.dd};}
J operator-(J a){return {-a.v,-a.d,-a.dd};}
J operator-(J a,J b){return a+(-b);}
J operator*(J a,J b){return {a.v*b.v,a.d*b.v+a.v*b.d,a.dd*b.v+I(2)*a.d*b.d+a.v*b.dd};}
J inv(J a){return {I(1)/a.v,-a.d/sq(a.v),I(2)*sq(a.d)/powi(a.v,3)-a.dd/sq(a.v)};}
J operator/(J a,J b){return a*inv(b);}
J compose(J s,I v,I d,I dd){return {v,d*s.d,dd*sq(s.d)+d*s.dd};}
double etaPowerBound(double a,int k){ // sup e^-1/s s^-k, 0<s<=a
 if(a<=0||k<2||k>4)throw runtime_error("eta endpoint bound domain"); I u=I(1)/I(a);if(u.l<k)u=I(k);if(u.l>100)u=I(100);return (powi(u,k)*expI(-u)).h;
}
J etaJ(J s){if(s.v.h<=0)return J();I v=eta(s.v),d,dd;
 if(s.v.l<=0 || s.v.l<.0001){double a=s.v.h;d=I(0,etaPowerBound(a,2));double z=(I(etaPowerBound(a,4))+I(2)*I(etaPowerBound(a,3))).h;dd=I(-z,z);}
 else {I u=I(1)/s.v;d=v*sq(u);dd=v*(powi(u,4)-I(2)*powi(u,3));}
 return compose(s,v,d,dd);
}
J thetaJ(J s){if(s.v.h<=0)return J();if(s.v.l>=1)return J(I(1));return etaJ(s)/(etaJ(s)+etaJ(J(I(1))-s));}
J sinJ(J s){return compose(s,sinI(s.v),cosI(s.v),-sinI(s.v));}
J cosJ(J s){return compose(s,cosI(s.v),-sinI(s.v),-cosI(s.v));}
J phiJ(J x,int k){if(x.v.h<=DELTA.l||x.v.l>=(T-DELTA).h)return J();return thetaJ((x-J(DELTA))/J(DELTA))*thetaJ((J(T-DELTA)-x)/J(DELTA))*sinJ(J(I(k)*PI/T)*x);}
J betaJ(J x,I c){J t=(x-J(c))/J(R);return etaJ(J(I(1))-t*t);}
J rhoJ(J x){return cosJ(J(PI/I(2))*thetaJ((x-J(I(3)*logI(I(3))))/J(I(2)*logI(I(3)))));}
I moment_ratio,c1,c2;
I fun(I x,int which){I f=phi(x,3)-moment_ratio*phi(x,1);if(which==0)return f;return rho(x)*f-c1*beta(x,ELL/I(3))-c2*beta(x,I(2)*ELL/I(3));}
J funJ(J x,int which){J f=phiJ(x,3)-J(moment_ratio)*phiJ(x,1);if(which==0)return f;return rhoJ(x)*f-J(c1)*betaJ(x,ELL/I(3))-J(c2)*betaJ(x,I(2)*ELL/I(3));}
int choose(int n,int k){int a=1;for(int j=1;j<=k;j++)a=a*(n-j+1)/j;return a;}
array<I,5> mulBounds(array<I,5>a,array<I,5>b){array<I,5>c;for(int n=0;n<=4;n++){c[n]=I(0);for(int j=0;j<=n;j++)c[n]=c[n]+I(choose(n,j))*a[j]*b[n-j];}return c;}
array<I,5> phiBounds(int k){array<I,5>chi,s;double tb[]={1,5,352,26000,3000000};for(int j=0;j<=4;j++){chi[j]=I(tb[j])/powi(DELTA,j);s[j]=powi(I(k)*PI/T,j);}return mulBounds(chi,s);}
array<I,5> rhoBounds(){array<I,5>o;I width=I(2)*logI(I(3));I a1=PI/I(2)*I(5)/width,a2=PI/I(2)*I(352)/sq(width),a3=PI/I(2)*I(26000)/powi(width,3),a4=PI/I(2)*I(3000000)/powi(width,4);
 o[0]=I(1);o[1]=a1;o[2]=sq(a1)+a2;o[3]=powi(a1,3)+I(3)*a1*a2+a3;o[4]=powi(a1,4)+I(6)*sq(a1)*a2+I(3)*sq(a2)+I(4)*a1*a3+a4;return o;}
template<class F>I simpson(F f,I a,I b,int n,I derivative4){if(n<=0||n%2||a.h>=b.l||derivative4.l<0)throw runtime_error("Simpson hypotheses");simpson_calls++;I h=(b-a)/I(n),sum(0);for(int j=0;j<=n;j++)sum=sum+I(j==0||j==n?1:(j%2?4:2))*f(a+I(j)*h);I ans=h/I(3)*sum;I err=(b-a)*powi(h,4)*derivative4/I(180);return widen(ans,err.h);}

struct C {I r,i;C(I a=I(0),I b=I(0)):r(a),i(b){} };
C operator+(C a,C b){return {a.r+b.r,a.i+b.i};}
C operator-(C a,C b){return {a.r-b.r,a.i-b.i};}
C operator*(C a,C b){return {a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r};}
void fft(vector<C>&a,const vector<C>&w,bool inverse){size_t n=a.size();for(size_t i=1,j=0;i<n;i++){size_t bit=n>>1;for(;j&bit;bit>>=1)j^=bit;j^=bit;if(i<j)swap(a[i],a[j]);}
 for(size_t len=2;len<=n;len<<=1){size_t hop=n/len;for(size_t b=0;b<n;b+=len)for(size_t j=0;j<len/2;j++){C z=w[j*hop];if(inverse)z.i=-z.i;C u=a[b+j],v=a[b+j+len/2]*z;a[b+j]=u+v;a[b+j+len/2]=u-v;}}
 if(inverse)for(auto &z:a){z.r=z.r/I(n);z.i=z.i/I(n);}
}
I symbol(I xi){int shift=xi.l<512?256:0;I x=I(1)/I(4),y=xi/I(2),a=x+I(shift),den=sq(a)+sq(y);I val=logI(den)/I(2)-a/(I(2)*den)-logI(PI);
 for(int j=0;j<shift;j++){I t=x+I(j);val=val-t/(sq(t)+sq(y));}
 return widen(val,(I(1)/I(4)/den).h); // sec^3/12 <= sqrt(2)/6 < 1/4
}
I b3(I x){x=ab(x);if(x.l>=2)return I(0);if(x.h<=1)return I(2)/I(3)-sq(x)+powi(x,3)/I(2);if(x.l>=1)return powi(I(2)-x,3)/I(6);return hull(b3(I(x.l,1)),b3(I(1,min(2.,x.h))));}
vector<pair<int,I>> pp;
void jsonI(I a){cout<<"["<<a.l<<","<<a.h<<"]";}
struct Result {I qnorm,qderiv,b2,arch,prime,tail,images,interp,energy,Cprime,ew,qw,epsn;};
Result evaluate(int which,int n,const vector<C>&twiddle){
 I step=I(64)/I(n);vector<C> a(n);I norm(0),deriv(0),b2sum(0);
 for(int j=0;j<n;j++)a[j].r=fun(I(j)*step,which);
 for(int j=0;j<n;j++){I u=a[j].r,v=a[(j+1)%n].r;norm=norm+step/I(3)*(sq(u)+u*v+sq(v));deriv=deriv+sq(u-v)/step;}
 const int panels=16384;I h=I(9)/I(panels);
 for(int j=0;j<panels;j++){I x((I(j)*h).l,(I(j+1)*h).h);b2sum=b2sum+h*sq(funJ(J(x,I(1)),which).dd);}
 fft(a,twiddle,false);I arch(0);for(int k=0;k<=n/2;k++){
  I sinc=k==0?I(1):sinI(PI*I(k)/I(n))/(PI*I(k)/I(n));
  I fq2=sq(step)*powi(sinc,4)*(sq(a[k].r)+sq(a[k].i));
  arch=arch+I(k==0?1:2)/I(64)*symbol(I(2)*PI*I(k)/I(64))*fq2;
 }
 for(auto &z:a)z=C(sq(z.r)+sq(z.i));fft(a,twiddle,true);
 I prime(0),Cprime(0);int bound=which==0?6561:729;
 for(auto [p,weight]:pp){if(p>=bound)continue;I u=logI(I(p))/step;int m=(int)floor((u.l+u.h)/2);
 if(floor(u.l)!=m||floor(u.h)!=m)throw runtime_error("delay crosses interpolation cell");
 delay_calls++;max_delay_width=max(max_delay_width,up(u.h-u.l));
 min_delay_cell_margin=min(min_delay_cell_margin,min(dn(u.l-m),dn(m+1-u.h)));
 I corr(0);
  for(int j=m-2;j<=m+2;j++)corr=corr+step*a[(j+n)%n].r*b3(u-I(j));
  prime=prime+I(2)*weight*corr;Cprime=Cprime+I(2)*weight;
 }
 // All |xi|>R0: W(xi)/xi^2 decreases, periodic Parseval applies.
 I R0=PI/step,A=I(2)+I(8)*sqrtI(I(2))/I(3)+logI(I(4)*PI);
 I tail=(A+logI(I(2)+R0))*deriv/sq(R0);
 // Periodic images: support diameter <9, P=64; ||q||_1^2 <=9||q||_2^2.
 I images=I(27)*norm*expI(-I(55)/I(2))/(I(1)-expI(-I(32)));
 // Linear interpolation bounds (deliberately weak constants 1).
 I epsn=powi(step,4)*b2sum,epsd=sq(step)*b2sum,C=A+logI(I(3));
 I ew=epsn*(C+logI(I(1)+I(1)/sq(step))/I(2));
 I qw=norm*(C+logI(I(1)+deriv/norm)/I(2));
 I interp=I(2)*sqrtI(qw*ew)+ew+Cprime*(I(2)*sqrtI(norm*epsn)+epsn);
 I total=arch-prime;I err=tail+images+interp;
 Result out{norm,deriv,b2sum,arch,prime,tail,images,interp,widen(total,err.h),Cprime,ew,qw,epsn};
 return out;
}
void printResult(Result z){cout<<"{";bool first=true;auto field=[&](const char*k,I v){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":";jsonI(v);};
 field("q_norm_squared",z.qnorm);field("q_derivative_squared",z.qderiv);field("smooth_second_derivative_squared_bound",z.b2);field("periodic_archimedean_head",z.arch);field("all_prime_delays",z.prime);field("fourier_tail_bound",z.tail);field("periodic_images_bound",z.images);field("interpolation_energy_bound",z.interp);field("C_prime",z.Cprime);field("error_L2_squared_bound",z.epsn);field("error_W_squared_bound",z.ew);field("q_W_squared_bound",z.qw);field("smooth_energy",z.energy);cout<<"}";}
int main(){try{
 if(fegetround()!=FE_TONEAREST||numeric_limits<double>::digits!=53||numeric_limits<double>::radix!=2)throw runtime_error("binary64 environment");
 volatile double tiny=numeric_limits<double>::denorm_min(),one=1;
 if(!(tiny*one>0))throw runtime_error("subnormals flushed");
 cout<<setprecision(17);if(numeric_limits<double>::is_iec559!=true)throw runtime_error("IEEE binary64 required");
 LOG2=logUnit(I(2));PI=I(16)*atanSmall(I(1)/I(5))-I(4)*atanSmall(I(1)/I(239));T=I(8)*logI(I(3));ELL=I(6)*logI(I(3));R=ELL/I(12);DELTA=T/I(40);
 array<I,5> expo;for(int j=0;j<=4;j++)expo[j]=I(81)/I(1<<j);
 auto p1=phiBounds(1),p3=phiBounds(3);int nm=262144;
 I M1=simpson([](I x){return expI(x/I(2))*phi(x,1);},I(0),T,nm,mulBounds(expo,p1)[4]);
 I M3=simpson([](I x){return expI(x/I(2))*phi(x,3);},I(0),T,nm,mulBounds(expo,p3)[4]);moment_ratio=M3/M1;if(M1.l<=0||moment_ratio.l<0||moment_ratio.h>=1)throw runtime_error("moment moment_ratio scope");
 array<I,5> fb;for(int j=0;j<=4;j++)fb[j]=p3[j]+I(moment_ratio.h)*p1[j];auto gb=mulBounds(fb,rhoBounds());
 I dp=simpson([](I x){return expI(x/I(2))*rho(x)*fun(x,0);},I(0),T,nm,mulBounds(expo,gb)[4]);
 array<I,5> expoMinus;for(int j=0;j<=4;j++)expoMinus[j]=I(1)/I(1<<j);
 I dm=simpson([](I x){return expI(-x/I(2))*rho(x)*fun(x,0);},I(0),T,nm,mulBounds(expoMinus,gb)[4]);
 // eta derivative suprema <= (1,1,8,280,20000), 0<=s<=1.
 array<I,5> bb;I z1=I(2)/R,z2=I(2)/sq(R);bb[0]=I(1);bb[1]=z1;bb[2]=I(8)*sq(z1)+z2;bb[3]=I(280)*powi(z1,3)+I(24)*z1*z2;bb[4]=I(20000)*powi(z1,4)+I(1680)*sq(z1)*z2+I(24)*sq(z2);
 array<I,5> eb;for(int j=0;j<=4;j++)eb[j]=I(2)/I(1<<j);
 I b=simpson([](I x){return expI(x/I(2))*beta(x,I(0));},-R,R,65536,mulBounds(eb,bb)[4]);
 // First window bump centers 2log3,4log3: H=b [[3,9],[1/3,1/9]].
 c1=(I(9)*dm-dp/I(9))/(b*(I(8)/I(3)));
 c2=(dp/I(3)-I(3)*dm)/(b*(I(8)/I(3)));
 cerr<<"Moment and correction enclosures complete.\n";
 vector<int> primes;for(int p=2;p<6561;p++){bool ok=true;for(int q:primes){if(q*q>p)break;if(p%q==0){ok=false;break;}}if(ok){primes.push_back(p);for(int k=p;k<6561;k*=p){pp.push_back({k,logI(I(p))/sqrtI(I(k))});if(k>6560/p)break;}}}
 const int n=524288;vector<C>twiddle(n/2);for(int k=0;k<n/2;k++){I angle=-I(2)*PI*I(k)/I(n);twiddle[k]=C(cosI(angle),sinI(angle));}
 Result f=evaluate(0,n,twiddle);cerr<<"Global energy enclosed.\n";Result v=evaluate(1,n,twiddle);cerr<<"Local energy enclosed.\n";
 I defect=f.energy-I(2)*v.energy;bool success=defect.h<0;
 cout<<"{\"status\":\""<<(success?"CERTIFIED_NEGATIVE":"INCONCLUSIVE")<<"\",\"grid_size\":"<<n<<",\"period\":64,\"moment_panels\":"<<nm<<",\"prime_power_count\":"<<pp.size()<<",\"M1\":";jsonI(M1);cout<<",\"M3\":";jsonI(M3);cout<<",\"moment_ratio\":";jsonI(moment_ratio);cout<<",\"b\":";jsonI(b);cout<<",\"d_plus\":";jsonI(dp);cout<<",\"d_minus\":";jsonI(dm);cout<<",\"c1\":";jsonI(c1);cout<<",\"c2\":";jsonI(c2);cout<<",\"f\":";printResult(f);cout<<",\"v1\":";printResult(v);cout<<",\"Delta\":";jsonI(defect);cout<<",\"required_upper\":0,\"failures\":"<<(success?"[]":"[\"Defect enclosure does not prove negativity\"]")<<"}\n";
 ofstream audit("scripts/corrected-ims/implementation-domains-317.json");audit<<setprecision(17);
 audit<<"{\"status\":\"PASS\",\"max_trig_abs\":"<<max_trig<<",\"trig_required\":4,\"max_atan_abs\":"<<max_atan<<",\"atan_required\":0.25,\"max_exp_base_abs\":"<<max_exp_base<<",\"exp_required\":0.125,\"log_base_range\":["<<min_log_base<<","<<max_log_base<<"],\"log_required\":[1,2],\"max_delay_interval_width\":"<<max_delay_width<<",\"min_delay_cell_margin\":"<<min_delay_cell_margin<<",\"required_cell_margin\":0,\"simpson_calls\":"<<simpson_calls<<",\"all_simpson_subinterval_counts_even\":true,\"delay_calls\":"<<delay_calls<<",\"prime_powers\":[";
 for(size_t j=0;j<pp.size();j++){if(j)audit<<",";audit<<pp[j].first;}audit<<"],\"failures\":[]}\n";
 cerr<<"Defect ["<<defect.l<<","<<defect.h<<"], required upper < 0. Full certificate: scripts/corrected-ims/certificate-315.json\n";
 }catch(const exception&e){cerr<<"FAILURE: "<<e.what()<<"\n";return 1;}}
