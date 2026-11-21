// Independent inequalities used by the derivative and elementary-series bounds.
#define main certificate_entry_315
#include "certificate-315.cpp"
#undef main
I fact(int n){I a(1);for(int j=2;j<=n;j++)a=a*I(j);return a;}
I ep(int n){return powi(I(n),n)*expI(I(-n));}
int main(){
 LOG2=logUnit(I(2));cout<<setprecision(17);
 vector<pair<string,I>> values={
  {"eta_first",ep(2)},
  {"eta_second",ep(4)+I(2)*ep(3)},
  {"eta_third",ep(6)+I(6)*ep(5)+I(6)*ep(4)},
  {"eta_fourth",ep(8)+I(12)*ep(7)+I(36)*ep(6)+I(24)*ep(5)},
  {"theta_denominator_lower",expI(I(-2))},
  {"theta_second",I(8*(8+2*2*5+16))},
  {"theta_third",I(8)*(I(280)+I(3)*I(2)*I(352)+I(3)*I(16)*I(5)+I(560))},
  {"theta_fourth",I(8)*(I(20000)+I(4)*I(2)*I(26000)+I(6)*I(16)*I(352)+I(4)*I(560)*I(5)+I(40000))},
  {"sin_remainder",powi(I(4),67)/fact(67)},
  {"cos_remainder",powi(I(4),66)/fact(66)},
  {"exp_remainder",I(2)*powi(I(1)/I(8),19)/fact(19)},
  {"log_remainder",I(2)*powi(I(1)/I(3),121)/(I(121)*(I(1)-I(1)/I(9)))},
  {"atan_remainder",powi(I(1)/I(4),181)/I(181)},
  {"small_exp_upper",expI(I(-100))}
 };
 vector<double>bounds={1,8,280,20000,.125,352,26000,3000000,0x1p-160,0x1p-150,0x1p-100,0x1p-180,0x1p-300,4e-44};
 bool ok=true;cout<<"{\"checks\":[";for(size_t j=0;j<values.size();j++){bool pass=j==4?values[j].second.l>bounds[j]:values[j].second.h<=bounds[j];ok&=pass;if(j)cout<<",";cout<<"{\"name\":\""<<values[j].first<<"\",\"actual\":";jsonI(values[j].second);cout<<",\"required\":"<<bounds[j]<<",\"comparison\":\""<<(j==4?">":"<=")<<"\",\"pass\":"<<(pass?"true":"false")<<"}";}
 cout<<"],\"status\":\""<<(ok?"PASS":"FAIL")<<"\"}\n";cerr<<"Elementary and derivative bounds: "<<(ok?"PASS":"FAIL")<<"; full evidence scripts/corrected-ims/constants-315.json\n";return ok?0:1;
}
