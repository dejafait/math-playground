// One fixed witness, real interval boxes; no grid values stand for integrals.
// clang++ -O2 -std=c++17 -ffp-contract=off scripts/good-frequency/fixed-witness-863.cpp -o /private/tmp/riemann-good-frequency-863
// /private/tmp/riemann-good-frequency-863 > scripts/good-frequency/fixed-witness-863.json
// Reuse the audited elementary outward intervals, not the old witness numbers.
#define main old_ims_main_315
#include "../corrected-ims/certificate-315.cpp"
#undef main

I safeCos(I x) {
 int n=(int)nearbyint((x.l+x.h)/(4*PI.l));
 I y=x-I(2*n)*PI;
 if(y.l < -4 || y.h > 4) throw runtime_error("cosine Taylor domain");
 return cosSmall(y);
}
I safeSin(I x) {
 int n=(int)nearbyint((x.l+x.h)/(4*PI.l));
 I y=x-I(2*n)*PI;
 if(y.l < -4 || y.h > 4) throw runtime_error("sine Taylor domain");
 return sinSmall(y);
}
I cutoff(I s) {return theta(I(40)*s-I(1))*theta(I(39)-I(40)*s);}
I mode(I s,int k){return cutoff(s)*safeSin(I(k)*PI*s);}
struct PP863 {int n,p; I weight,delay;};
vector<PP863> powers863;
I complete863(I t){
 I v=symbol(t);
 for(auto z:powers863) v=v-I(2)*z.weight*safeCos(t*z.delay);
 return v;
}
struct Cell863 {I z,f;};
struct Box863 {double l,h;I w,F,mass;};
int main(){try{
 if(!numeric_limits<double>::is_iec559)throw runtime_error("IEEE binary64 required");
 LOG2=logUnit(I(2));PI=I(16)*atanSmall(I(1)/I(5))-I(4)*atanSmall(I(1)/I(239));
 T=I(4)*logI(I(3)); DELTA=T/I(40);
 vector<int> primes;
 for(int p=2;p<81;p++){
  bool prime=true;for(int q:primes){if(q*q>p)break;if(p%q==0){prime=false;break;}}
  if(prime){primes.push_back(p);for(int n=p;n<81;){
   powers863.push_back({n,p,logI(I(p))/sqrtI(I(n)),logI(I(n))});
   if(n>80/p)break;n*=p;
  }}
 }
 sort(powers863.begin(),powers863.end(),[](auto a,auto b){return a.n<b.n;});
 const int nm=32768,nx=8192,nt=512; // t cells of width 1/32 cover [0,16].
 I m1(0),m3(0),hs=I(1)/I(nm);
 for(int j=0;j<nm;j++){
  I s=(I(j,j+1))/I(nm),weight=expI(T*s/I(2));
  m1=m1+hs*weight*mode(s,1);m3=m3+hs*weight*mode(s,3);
 }
 m1=T*m1;m3=T*m3;
 if(m1.l<=0)throw runtime_error("positive moment denominator not enclosed");
 moment_ratio=m3/m1;
 I norm(0); vector<Cell863> spatial;I dx=T/I(nx);
 for(int j=0;j<nx;j++){
  I s=I(j,j+1)/I(nx),f=mode(s,3)-moment_ratio*mode(s,1);
  spatial.push_back({T*(s-I(.5)),f});norm=norm+dx*sq(f);
 }
 if(norm.l<=0)throw runtime_error("nonzero norm not enclosed");
 I w0=complete863(I(0));double m0=max(0.,-w0.h);
 I threshold=I(m0)/(I(1)+I(m0));
 vector<Box863> boxes;vector<array<double,3>> skipped;
 I bad(0);int evaluated=0;bool rejected=false;
 for(int j=0;j<nt;j++){
  I t=I(j,j+1)/I(32),w=complete863(t);evaluated++;
  if(w.h>=1){skipped.push_back({double(j)/32,double(j+1)/32,w.h});continue;}
  I F(0);for(auto cell:spatial)F=F+dx*cell.f*safeCos(t*cell.z);
  // Real f symmetric about T/2: |F_f(t)|^2 equals this real square.
  // Retain BOTH reflected frequency boxes, using evenness.
  I mass=I(2)*(I(1)/I(32))*sq(F)/(I(2)*PI);
  // A squared real range has a nonnegative true lower endpoint.
  mass.l=max(0.,mass.l);bad=bad+mass;
  // Save exact nominal dyadic endpoints, not their inflated evaluation boxes.
  boxes.push_back({double(j)/32,double(j+1)/32,w,F,mass});
  I U=I(1)-I(max(0.,bad.l))/I(norm.h);
  if(m0>0 && U.h<=threshold.l){rejected=true;break;}
 }
 double b=max(0.,bad.l);I U=I(1)-I(b)/I(norm.h);
 cout<<setprecision(17)<<"{\"status\":\""<<(rejected?"CERTIFIED_STRICT_SCREEN_REJECTION":"INCONCLUSIVE")<<"\",";
 cout<<"\"method\":\"real interval boxes; exact-ratio witness; symmetry; Plancherel\",";
 cout<<"\"moment_cells\":"<<nm<<",\"spatial_cells\":"<<nx<<",\"frequency_cells_evaluated\":"<<evaluated<<",";
 cout<<"\"T\":";jsonI(T);cout<<",\"delta\":";jsonI(DELTA);
 cout<<",\"M_plus_phi1\":";jsonI(m1);cout<<",\"M_plus_phi3\":";jsonI(m3);
 cout<<",\"exact_ratio_enclosure\":";jsonI(moment_ratio);cout<<",\"norm_squared\":";jsonI(norm);
 cout<<",\"w_zero\":";jsonI(w0);cout<<",\"m0\":"<<m0;
 cout<<",\"bad_mass_enclosure\":";jsonI(bad);cout<<",\"b\":"<<b;
 cout<<",\"good_mass_ratio_upper_enclosure\":";jsonI(U);
 cout<<",\"required_threshold_lower_enclosure\":";jsonI(threshold);
 cout<<",\"actual_upper\":"<<U.h<<",\"required_upper\":"<<threshold.l;
 cout<<",\"prime_powers\":[";bool first=true;
 for(auto z:powers863){if(!first)cout<<",";first=false;cout<<"{\"n\":"<<z.n<<",\"prime\":"<<z.p<<",\"weight\":";jsonI(z.weight);cout<<",\"log_n\":";jsonI(z.delay);cout<<"}";}
 cout<<"],\"positive_bad_boxes\":[";first=true;
 for(auto z:boxes){if(!first)cout<<",";first=false;cout<<"{\"t\":["<<z.l<<","<<z.h<<"],\"w\":";jsonI(z.w);cout<<",\"centered_fourier\":";jsonI(z.F);cout<<",\"paired_mass\":";jsonI(z.mass);cout<<"}";}
 cout<<"],\"skipped_boxes\":[";first=true;
 for(auto z:skipped){if(!first)cout<<",";first=false;cout<<"["<<z[0]<<","<<z[1]<<","<<z[2]<<"]";}
 cout<<"],\"failures\":"<<(rejected?"[]":"[\"One-sided certified bad mass did not reject strict screen\"]")<<"}\n";
 cerr<<setprecision(12)<<"Status: "<<(rejected?"CERTIFIED_STRICT_SCREEN_REJECTION":"INCONCLUSIVE")
     <<"; U <= "<<U.h<<", required <= "<<threshold.l<<"; b >= "<<b
     <<"; N in ["<<norm.l<<","<<norm.h<<"]; retained "<<boxes.size()<<" paired boxes.\n"
     <<"Failures: "<<(rejected?"none":"insufficient certified mass")
     <<". Full certificate: scripts/good-frequency/fixed-witness-863.json\n";
 }catch(const exception&e){cerr<<"FAILURE: "<<e.what()<<"\n";return 1;}}
