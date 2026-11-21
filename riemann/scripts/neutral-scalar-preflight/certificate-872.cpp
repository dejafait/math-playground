// Fixed U12 scalar-floor rejection: outward enclosures, no mode/window sweep.
// clang++ -O2 -std=c++17 -ffp-contract=off scripts/neutral-scalar-preflight/certificate-872.cpp -o /private/tmp/riemann-neutral-scalar-872
// /private/tmp/riemann-neutral-scalar-872 > scripts/neutral-scalar-preflight/certificate-872.json
#define main unused_ims_main_315
#include "../corrected-ims/certificate-315.cpp"
#undef main
using Vec=array<I,6>;
using Mat=array<Vec,6>;
Mat gram;
Vec moments;
I dotG(Vec a,Vec b){I r(0);for(int i=0;i<6;i++)for(int j=0;j<6;j++)r=r+a[i]*gram[i][j]*b[j];return r;}
Vec addV(Vec a,Vec b){for(int i=0;i<6;i++)a[i]=a[i]+b[i];return a;}
Vec scaleV(I t,Vec a){for(auto &v:a)v=t*v;return a;}
Vec neutral(int index){Vec a{};a[index]=I(1);a[0]=-moments[index]/moments[0];return a;}
Vec project(Vec r,Vec b,Vec c){
 I h00=dotG(b,b),h01=dotG(b,c),h11=dotG(c,c),det=h00*h11-sq(h01);
 if(det.l<=0)throw runtime_error("retained Gram determinant not positive");
 I p0=dotG(r,b),p1=dotG(r,c);
 I a=(h11*p0-h01*p1)/det, d=(h00*p1-h01*p0)/det;
 return addV(r,addV(scaleV(-a,b),scaleV(-d,c)));
}
I trial(I x,const Vec &c){I f(0);for(int j=0;j<6;j++)if(c[j].l!=0||c[j].h!=0)f=f+c[j]*phi(x,2*j+2);return f;}
J trialJ(J x,const Vec &c){J f;for(int j=0;j<6;j++)if(c[j].l!=0||c[j].h!=0)f=f+J(c[j])*phiJ(x,2*j+2);return f;}
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
 for(auto [p,weight]:pp){I u=logI(I(p))/step;int m=(int)floor((u.l+u.h)/2);I corr(0);
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
void jsonV(Vec v){cout<<"[";for(int j=0;j<6;j++){if(j)cout<<",";jsonI(v[j]);}cout<<"]";}
int main(){try{
 if(!numeric_limits<double>::is_iec559)throw runtime_error("IEEE binary64 required");
 LOG2=logUnit(I(2));PI=I(16)*atanSmall(I(1)/I(5))-I(4)*atanSmall(I(1)/I(239));
 T=I(4)*logI(I(3));DELTA=T/I(40);
 const int nm=65536,n=262144;
 I h=T/I(nm);array<array<I,5>,6>pb;
 for(int j=0;j<6;j++)pb[j]=phiBounds(2*j+2);
 for(int l=0;l<=nm;l++){
  I x=I(l)*h,e=expI(x/I(2)),weight(l==0||l==nm?1:l%2?4:2);Vec f;
  for(int j=0;j<6;j++){f[j]=phi(x,2*j+2);moments[j]=moments[j]+weight*e*f[j];}
  for(int j=0;j<6;j++)for(int k=0;k<=j;k++)gram[j][k]=gram[j][k]+weight*f[j]*f[k];
 }
 array<I,5> eb;for(int j=0;j<5;j++)eb[j]=I(9)/I(1<<j);
 for(int j=0;j<6;j++){
  I err=T*powi(h,4)*mulBounds(eb,pb[j])[4]/I(180);
  moments[j]=widen(h/I(3)*moments[j],err.h);
  for(int k=0;k<=j;k++){
   I errG=T*powi(h,4)*mulBounds(pb[j],pb[k])[4]/I(180);
   gram[k][j]=gram[j][k]=widen(h/I(3)*gram[j][k],errG.h);
  }
 }
 if(moments[0].h>=0)throw runtime_error("negative even pivot moment not enclosed");
 Vec b=neutral(1),c=neutral(2);
 Vec v=addV(scaleV(I(23)/I(100),b),scaleV(I(58)/I(100),c));
 Vec rawZ=addV(addV(scaleV(I(38)/I(100),neutral(3)),scaleV(-I(52)/I(100),neutral(4))),scaleV(I(19)/I(100),neutral(5)));
 Vec rawY=addV(addV(scaleV(I(32)/I(100),neutral(3)),scaleV(I(42)/I(100),neutral(4))),scaleV(I(50)/I(100),neutral(5)));
 Vec z=project(rawZ,b,c),y=project(rawY,b,c),vy=addV(v,y);
 I nz=dotG(z,z),ny=dotG(y,y),nv=dotG(v,v);
 if(nz.l<=0||ny.l<=0||nv.l<=0)throw runtime_error("nonzero trial norm not enclosed");
 cerr<<"Exact moment/Gram/projection enclosures complete. Norm z ["<<nz.l<<","<<nz.h<<"], y ["<<ny.l<<","<<ny.h<<"].\n";
 vector<int>primes;
 for(int p=2;p<81;p++){bool ok=true;for(int q:primes){if(q*q>p)break;if(p%q==0){ok=false;break;}}if(ok){primes.push_back(p);for(int k=p;k<81;){pp.push_back({k,logI(I(p))/sqrtI(I(k))});if(k>80/p)break;k*=p;}}}
 sort(pp.begin(),pp.end(),[](auto a,auto b){return a.first<b.first;});
 vector<C>tw(n/2);vector<I>symbols(n/2+1);
 for(int k=0;k<n/2;k++){I angle=-I(2)*PI*I(k)/I(n);tw[k]=C(cosI(angle),sinI(angle));}
 for(int k=0;k<=n/2;k++)symbols[k]=symbol(I(2)*PI*I(k)/I(64));
 cerr<<"Outward FFT roots, digamma head and all "<<pp.size()<<" prime powers ready.\n";
 Result rv=eval872(v,n,tw,symbols);cerr<<"Retained energy ["<<rv.energy.l<<","<<rv.energy.h<<"].\n";
 Result rz=eval872(z,n,tw,symbols);cerr<<"Floor trial energy ["<<rz.energy.l<<","<<rz.energy.h<<"].\n";
 Result ry=eval872(y,n,tw,symbols);cerr<<"Coupling trial energy ["<<ry.energy.l<<","<<ry.energy.h<<"].\n";
 Result rvy=eval872(vy,n,tw,symbols);cerr<<"Sum trial energy ["<<rvy.energy.l<<","<<rvy.energy.h<<"].\n";
 I cross=(rvy.energy-rv.energy-ry.energy)/I(2),dp=rz.energy/nz;
 I cross2=sq(cross),sUpper;
 bool positiveUpper=dp.h>0;
 if(positiveUpper)sUpper=rv.energy-I(cross2.l)/(I(ny.h)*I(dp.h));
 bool reject=positiveUpper&&sUpper.h<0;
 cout<<setprecision(17)<<"{\"status\":\""<<(reject?"CERTIFIED_SCALAR_FLOOR_REJECTION":"INCONCLUSIVE")<<"\",\"grid_size\":"<<n<<",\"moment_panels\":"<<nm<<",\"derivative_panels\":32768,\"period\":64,\"T\":";jsonI(T);
 cout<<",\"moments\":";jsonV(moments);cout<<",\"gram\":[";for(int j=0;j<6;j++){if(j)cout<<",";jsonV(gram[j]);}cout<<"],\"directions\":{\"v\":";jsonV(v);cout<<",\"z\":";jsonV(z);cout<<",\"y\":";jsonV(y);cout<<"}";
 cout<<",\"norm_v\":";jsonI(nv);cout<<",\"norm_z\":";jsonI(nz);cout<<",\"norm_y\":";jsonI(ny);
 cout<<",\"energies\":{\"v\":";printResult(rv);cout<<",\"z\":";printResult(rz);cout<<",\"y\":";printResult(ry);cout<<",\"v_plus_y\":";printResult(rvy);cout<<"}";
 cout<<",\"cross\":";jsonI(cross);cout<<",\"d_plus_enclosure\":";jsonI(dp);cout<<",\"retained_upper_comparison\":";jsonI(sUpper);
 cout<<",\"required_upper\":0,\"prime_powers\":[";for(int j=0;j<(int)pp.size();j++){if(j)cout<<",";cout<<pp[j].first;}cout<<"],\"failures\":"<<(reject?"[]":"[\"Signed bounds do not establish scalar-floor rejection\"]")<<"}\n";
 cerr<<"Status "<<(reject?"CERTIFIED_SCALAR_FLOOR_REJECTION":"INCONCLUSIVE")<<"; actual retained upper "<<sUpper.h<<", required <0; d upper "<<dp.h<<"; cross lower "<<cross.l<<". Full certificate scripts/neutral-scalar-preflight/certificate-872.json\n";
 }catch(const exception&e){cerr<<"FAILURE: "<<e.what()<<"\n";return 1;}}
