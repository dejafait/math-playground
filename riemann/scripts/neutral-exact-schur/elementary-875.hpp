// Inherited certificate315 elementary library, with domain guards; no old numerical result used.
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
struct I { double l,h; I(double x=0):l(x),h(x){} I(double a,double b):l(a),h(b){if(!isfinite(a)||!isfinite(b)||a>b)throw runtime_error("invalid interval");} };
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
 if(abs(z)>.125)throw runtime_error("exp domain");I v(z),sum(1),term(1);for(int n=1;n<=18;n++){term=term*v/I(n);sum=sum+term;}
 // |z|<=1/8: exponential Taylor remainder < 2^-100.
 sum=widen(sum,0x1p-100);for(int j=0;j<k;j++)sum=sq(sum);return sum;
}
I expI(I x){return {expPoint(x.l).l,expPoint(x.h).h};}
I logUnit(I x){if(x.l<1||x.h>2)throw runtime_error("log domain");I t=(x-I(1))/(x+I(1)),t2=sq(t),term=t,sum(0);for(int j=0;j<60;j++){sum=sum+term/I(2*j+1);term=term*t2;}
 // x in [1,2], |t|<=1/3; 120-term-power geometric tail < 2^-180.
 return widen(I(2)*sum,0x1p-180);
}
I LOG2;
I logPoint(double x){if(x<=0)throw runtime_error("nonpositive log");int e;double m=frexp(x,&e);m*=2;e--;return logUnit(I(m))+I(e)*LOG2;}
I logI(I x){return {logPoint(x.l).l,logPoint(x.h).h};}
I atanSmall(I x){if(max(abs(x.l),abs(x.h))>.25)throw runtime_error("atan domain");I t=x,sum(0);for(int j=0;j<90;j++){sum=sum+((j%2)?-t:t)/I(2*j+1);t=t*sq(x);}return widen(sum,0x1p-300);}
I PI,T,ELL,R,DELTA;
I sinSmall(I x){if(max(abs(x.l),abs(x.h))>4)throw runtime_error("trig domain");I term=x,sum=x;for(int n=1;n<=32;n++){term=-term*sq(x)/I((2*n)*(2*n+1));sum=sum+term;}return widen(sum,0x1p-160);}
I cosSmall(I x){if(max(abs(x.l),abs(x.h))>4)throw runtime_error("trig domain");I term(1),sum(1);for(int n=1;n<=32;n++){term=-term*sq(x)/I((2*n-1)*(2*n));sum=sum+term;}return widen(sum,0x1p-150);}
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
 if(a<=0||k<2||k>4)throw runtime_error("eta domain");I u=I(1)/I(a);if(u.l<k)u=I(k);if(u.l>100)u=I(100);return (powi(u,k)*expI(-u)).h;
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
template<class F>I simpson(F f,I a,I b,int n,I derivative4){I h=(b-a)/I(n),sum(0);for(int j=0;j<=n;j++)sum=sum+I(j==0||j==n?1:(j%2?4:2))*f(a+I(j)*h);I ans=h/I(3)*sum;I err=(b-a)*powi(h,4)*derivative4/I(180);return widen(ans,err.h);}

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
void printResult(Result z){cout<<"{";bool first=true;auto field=[&](const char*k,I v){if(!first)cout<<",";first=false;cout<<"\""<<k<<"\":";jsonI(v);};
 field("q_norm_squared",z.qnorm);field("q_derivative_squared",z.qderiv);field("smooth_second_derivative_squared_bound",z.b2);field("periodic_archimedean_head",z.arch);field("all_prime_delays",z.prime);field("fourier_tail_bound",z.tail);field("periodic_images_bound",z.images);field("interpolation_energy_bound",z.interp);field("C_prime",z.Cprime);field("error_L2_squared_bound",z.epsn);field("error_W_squared_bound",z.ew);field("q_W_squared_bound",z.qw);field("smooth_energy",z.energy);cout<<"}";}
