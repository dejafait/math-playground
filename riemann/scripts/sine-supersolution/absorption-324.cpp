// Bounded enclosure replay on the unchanged four-dimensional exact kernel.
// Reuses the audited elementary intervals and full-energy method of L750.
// Build with -O2 -std=c++17 -ffp-contract=off; no fast-math.
#define main original_certificate315_main
#include "../corrected-ims/certificate-315.cpp"
#undef main

array<I,6> trial;
I trialValue(I x){I f(0);for(int k=1;k<=6;k++)f=f+trial[k-1]*phi(x,k);return f;}
J trialJet(J x){J f;for(int k=1;k<=6;k++)f=f+J(trial[k-1])*phiJ(x,k);return f;}

Result trialEnergy(int n,const vector<C>&twiddle){
 I step=I(64)/I(n);vector<C>a(n);I norm(0),deriv(0),b2sum(0);
 for(int j=0;j<n;j++)a[j].r=trialValue(I(j)*step);
 for(int j=0;j<n;j++){I u=a[j].r,v=a[(j+1)%n].r;norm=norm+step/I(3)*(sq(u)+u*v+sq(v));deriv=deriv+sq(u-v)/step;}
 const int panels=16384;I dx=I(9)/I(panels);
 for(int j=0;j<panels;j++){I x((I(j)*dx).l,(I(j+1)*dx).h);b2sum=b2sum+dx*sq(trialJet(J(x,I(1))).dd);}
 fft(a,twiddle,false);I arch(0);
 for(int k=0;k<=n/2;k++){
  I sinc=k==0?I(1):sinI(PI*I(k)/I(n))/(PI*I(k)/I(n));
  I fq2=sq(step)*powi(sinc,4)*(sq(a[k].r)+sq(a[k].i));
  arch=arch+I(k==0?1:2)/I(64)*symbol(I(2)*PI*I(k)/I(64))*fq2;
 }
 for(auto &z:a)z=C(sq(z.r)+sq(z.i));fft(a,twiddle,true);
 I prime(0),Cprime(0);
 // Every n>=6561 has delay >=T and exactly zero overlap for both
 // the smooth trials and their linear interpolants. The enclosing
 // window remains L=9log3, not T: these edges are retained as zeros.
 for(auto [p,weight]:pp){if(p>=6561)continue;I u=logI(I(p))/step;int m=(int)floor((u.l+u.h)/2);I corr(0);
  for(int j=m-2;j<=m+2;j++)corr=corr+step*a[(j+n)%n].r*b3(u-I(j));
  prime=prime+I(2)*weight*corr;Cprime=Cprime+I(2)*weight;
 }
 I R0=PI/step,A=I(2)+I(8)*sqrtI(I(2))/I(3)+logI(I(4)*PI);
 I tail=(A+logI(I(2)+R0))*deriv/sq(R0);
 I images=I(27)*norm*expI(-I(55)/I(2))/(I(1)-expI(-I(32)));
 I epsn=powi(step,4)*b2sum,C0=A+logI(I(3));
 I ew=epsn*(C0+logI(I(1)+I(1)/sq(step))/I(2));
 I qw=norm*(C0+logI(I(1)+deriv/norm)/I(2));
 I interp=I(2)*sqrtI(qw*ew)+ew+Cprime*(I(2)*sqrtI(norm*epsn)+epsn);
 I total=arch-prime,err=tail+images+interp;
 return {norm,deriv,b2sum,arch,prime,tail,images,interp,widen(total,err.h),Cprime,ew,qw,epsn};
}

int main(){try{
 cout<<setprecision(17);
 if(!numeric_limits<double>::is_iec559)throw runtime_error("IEEE binary64 required");
 LOG2=logUnit(I(2));PI=I(16)*atanSmall(I(1)/I(5))-I(4)*atanSmall(I(1)/I(239));
 T=I(8)*logI(I(3));ELL=I(6)*logI(I(3));R=ELL/I(12);DELTA=T/I(40);
 array<I,5> expo;for(int j=0;j<=4;j++)expo[j]=I(81)/I(1<<j);
 array<I,6>M;const int nm=262144;
 for(int k=1;k<=6;k++)M[k-1]=simpson([&](I x){return expI(x/I(2))*phi(x,k);},I(0),T,nm,mulBounds(expo,phiBounds(k))[4]);
 if(M[0].l<=0||M[1].h>=0)throw runtime_error("anchor signs not certified");
 array<array<I,6>,4>basis{};int modes[]={3,5,4,6};
 for(int j=0;j<4;j++){int k=modes[j],anchor=k%2?0:1;basis[j][k-1]=I(1);basis[j][anchor]=-M[k-1]/M[anchor];}
 vector<int>primes;int active=0,inactive=0;
 for(int p=2;p<19683;p++){bool ok=true;for(int q:primes){if(q*q>p)break;if(p%q==0){ok=false;break;}}if(ok){primes.push_back(p);for(int k=p;k<19683;k*=p){pp.push_back({k,logI(I(p))/sqrtI(I(k))});if(k<6561)active++;else inactive++;if(k>19682/p)break;}}}
 const int n=524288;vector<C>twiddle(n/2);
 for(int k=0;k<n/2;k++){I angle=-I(2)*PI*I(k)/I(n);twiddle[k]=C(cosI(angle),sinI(angle));}
 vector<Result>results;
 for(int j=0;j<6;j++){
  if(j<4)trial=basis[j];else {int offset=j==4?0:2;for(int k=0;k<6;k++)trial[k]=basis[offset][k]+basis[offset+1][k];}
  results.push_back(trialEnergy(n,twiddle));
  cerr<<"Trial "<<j<<" energy ["<<results.back().energy.l<<","<<results.back().energy.h<<"].\n";
 }
 array<array<I,4>,4>mat{};
 for(int j=0;j<4;j++)mat[j][j]=results[j].energy;
 mat[0][1]=mat[1][0]=(results[4].energy-results[0].energy-results[1].energy)/I(2);
 mat[2][3]=mat[3][2]=(results[5].energy-results[2].energy-results[3].energy)/I(2);
 I det0=mat[0][0]*mat[1][1]-sq(mat[0][1]);
 I det1=mat[2][2]*mat[3][3]-sq(mat[2][3]);
 bool psd=mat[0][0].l>0&&mat[2][2].l>0&&det0.l>=0&&det1.l>=0;
 cout<<"{\"status\":\""<<(psd?"CERTIFIED_RESTRICTED_POSITIVE":"INCONCLUSIVE")<<"\",\"required_witness_upper\":0,\"grid_size\":"<<n<<",\"moment_subintervals\":"<<nm<<",\"period\":64,\"prime_power_count_full_window\":"<<pp.size()<<",\"prime_power_count_evaluated\":"<<active<<",\"prime_power_count_exact_zero_delay_ge_T\":"<<inactive<<",\"moments\":[";
 for(int k=0;k<6;k++){if(k)cout<<",";jsonI(M[k]);}cout<<"],\"basis_coefficients\":[";
 for(int j=0;j<4;j++){if(j)cout<<",";cout<<"[";for(int k=0;k<6;k++){if(k)cout<<",";jsonI(basis[j][k]);}cout<<"]";}cout<<"],\"trials\":[";
 for(int j=0;j<6;j++){if(j)cout<<",";printResult(results[j]);}cout<<"],\"matrix\":[";
 for(int j=0;j<4;j++){if(j)cout<<",";cout<<"[";for(int k=0;k<4;k++){if(k)cout<<",";jsonI(mat[j][k]);}cout<<"]";}
 cout<<"],\"parity_block_determinants\":[";jsonI(det0);cout<<",";jsonI(det1);cout<<"],\"failures\":"<<(psd?"[]":"[\"Outward parity-block determinant enclosures do not certify positivity; no negative witness is certified\"]")<<"}\n";
 cerr<<"Determinants ["<<det0.l<<","<<det0.h<<"], ["<<det1.l<<","<<det1.h<<"], required lower >=0 for block positivity.\n";
 cerr<<"Negative witness requires energy upper <0; none certified. Failures: "<<(psd?"none":"crossing determinant enclosures; neither sign certified")<<".\n";
 cerr<<"Result "<<(psd?"restricted positive":"inconclusive")<<"; full certificate scripts/sine-supersolution/absorption-324.json\n";
 }catch(const exception&e){cerr<<"FAILURE: "<<e.what()<<"\n";return 1;}}
