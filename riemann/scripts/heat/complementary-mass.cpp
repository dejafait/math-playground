// Exact fixed binary-grid intervals. No floating-point arithmetic is used.
// Build: clang++ -O3 -std=c++17 scripts/heat/complementary-mass.cpp -o /tmp/riemann-complementary-mass
// Run from notebook: /tmp/riemann-complementary-mass scripts/heat
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>
using i64=int64_t;
using i128=__int128_t;
using u64=uint64_t;
struct I { i64 l,h; };
i64 Q;
u64 operations=0;
i64 narrow(i128 x) {
    if (x<std::numeric_limits<i64>::min() || x>std::numeric_limits<i64>::max())
        throw std::runtime_error("signed interval overflow");
    return (i64)x;
}
i128 floordiv(i128 x,i64 d) { assert(d>0); i128 z=x/d; return z-(x%d<0); }
i128 ceildiv(i128 x,i64 d) { return -floordiv(-x,d); }
I add(I a,I b) { return {narrow((i128)a.l+b.l),narrow((i128)a.h+b.h)}; }
I sub(I a,I b) { return {narrow((i128)a.l-b.h),narrow((i128)a.h-b.l)}; }
I mul(I a,I b) {
    i128 v[4]={(i128)a.l*b.l,(i128)a.l*b.h,(i128)a.h*b.l,(i128)a.h*b.h};
    return {narrow(floordiv(*std::min_element(v,v+4),Q)),
            narrow(ceildiv(*std::max_element(v,v+4),Q))};
}
I absolute(I a) {
    assert(a.l<=a.h);
    if(a.l>=0) return a;
    if(a.h<=0) return {narrow(-(i128)a.h),narrow(-(i128)a.l)};
    return {0,std::max(narrow(-(i128)a.l),a.h)};
}
std::string dec(i128 x) {
    if(x==0) return "0";
    bool neg=x<0; if(neg)x=-x;
    std::string s;
    while(x) { s.push_back('0'+x%10); x/=10; }
    if(neg)s.push_back('-'); std::reverse(s.begin(),s.end());return s;
}
std::string ji(I a) { return "[\""+dec(a.l)+"\",\""+dec(a.h)+"\"]"; }
struct D { u64 d; I r; int sign; };
struct P { u64 p; I r,log; };
int main(int argc,char**argv) {
    std::string root=argc>1?argv[1]:"scripts/heat";
    try {
        u64 N,H,T; I factor;
        std::ifstream cf(root+"/complementary-mass-config.txt");
        if(!(cf>>Q>>N>>H>>T>>factor.l>>factor.h))throw std::runtime_error("config");
        assert(Q==(1LL<<56) && N==691004 && H==160*N && H<T);
        std::vector<P> primes; P p;
        while(cf>>p.p>>p.r.l>>p.r.h>>p.log.l>>p.log.h) {
            assert(p.r.l>0 && p.r.l<=p.r.h && p.r.h<Q);
            assert(primes.empty() || primes.back().p<p.p);
            primes.push_back(p);
        }
        // Independently certify that the config's prime list is exhaustive.
        size_t pi=0;
        for(u64 n=2;n<=307;n++) {
            bool prime=true; for(u64 d=2;d*d<=n;d++)if(n%d==0)prime=false;
            if(prime) { assert(pi<primes.size() && primes[pi].p==n); pi++; }
        }
        assert(pi==63 && primes.size()==pi);
        std::vector<I> a(N+1),logs(N+1),A(N+1),B(N+1);
        std::ifstream seeds(root+"/complementary-mass-seeds.bin",std::ios::binary);
        for(u64 n=1;n<=N;n++) {
            i64 row[4]; seeds.read((char*)row,sizeof(row));
            if(!seeds)throw std::runtime_error("short seed ledger");
            a[n]={row[0],row[1]}; logs[n]={row[2],row[3]};
            assert(0<=a[n].l && a[n].l<=a[n].h && logs[n].l<=logs[n].h);
            A[n]=add(A[n-1],a[n]); B[n]=add(B[n-1],mul(a[n],logs[n]));
        }
        char extra; assert(!seeds.get(extra));
        for(auto p:primes) assert(p.r.l==a[p.p].l && p.r.h==a[p.p].h &&
                                  p.log.l==logs[p.p].l && p.log.h==logs[p.p].h);
        // Euler zeroth/first logarithmic moments, including the empty subset.
        I R{Q,Q},Rlog{0,0};
        for(auto p:primes) {
            Rlog=add(mul(Rlog,add({Q,Q},p.r)),mul(R,mul(p.r,p.log)));
            R=mul(R,add({Q,Q},p.r));
        }
        I smallR{0,0},smallLog{0,0},clipped{0,0};
        u64 divisors=0; std::array<u64,64> depthcounts{};
        std::vector<D> edge;
        std::ofstream dl(root+"/complementary-mass-divisors.bin",std::ios::binary);
        std::function<void(size_t,u64,I,I,int,size_t)> visit;
        visit=[&](size_t start,u64 d,I r,I logd,int sign,size_t depth) {
            divisors++; depthcounts[depth]++;
            smallR=add(smallR,r); smallLog=add(smallLog,mul(r,logd));
            if(d<=H) {
                edge.push_back({d,r,sign});
                i64 row[4]={(i64)d,r.l,r.h,sign}; dl.write((char*)row,sizeof(row));
            }
            u64 q0=std::min(N,H/d),qc=std::min(N,T/d);
            assert(q0<=qc && qc>=1);
            I da=sub(A[N],A[qc]), db=sub(B[N],B[qc]);
            // Prefix differences are exact nonnegative sums.
            da.l=std::max<i64>(0,da.l); db.l=std::max<i64>(0,db.l);
            I unit=sub(A[qc],A[q0]);unit.l=std::max<i64>(0,unit.l);
            I logpart=sub(mul(factor,add(mul(logd,da),db)),da);
            logpart.l=std::max<i64>(0,logpart.l);
            I contribution=mul(r,add(unit,logpart));
            clipped=add(clipped,contribution);
            for(size_t j=start;j<primes.size();j++) {
                auto p=primes[j];
                if(d>T/p.p)break;
                visit(j+1,d*p.p,mul(r,p.r),add(logd,p.log),-sign,depth+1);
            }
            if(divisors%10000000==0)std::cout<<"divisors processed="<<divisors<<std::endl;
        };
        visit(0,1,{Q,Q},{0,0},1,0); dl.close();
        I residualR=sub(R,smallR),residualLog=sub(Rlog,smallLog);
        assert(residualR.h>=0 && residualLog.h>=0);
        residualR.l=std::max<i64>(0,residualR.l);
        residualLog.l=std::max<i64>(0,residualLog.l);
        I far=sub(mul(factor,add(mul(A[N],residualLog),mul(B[N],residualR))),mul(A[N],residualR));
        far.l=std::max<i64>(0,far.l);
        I tail=add(clipped,far);
        std::cout<<"Enumeration complete: d<=T "<<divisors<<", d<=H "<<edge.size()
                 <<"; positive tail grid="<<ji(tail)<<std::endl;
        // Persist the complete moments before the longer grouped calculation.
        std::ofstream mo(root+"/complementary-mass-moments.json");
        mo<<"{\n\"Q\":\""<<Q<<"\",\"N\":"<<N<<",\"H\":"<<H<<",\"T_floor\":"<<T
          <<",\"divisors_le_T\":"<<divisors<<",\"divisors_le_H\":"<<edge.size()
          <<",\"depth_counts\":[";
        for(size_t i=0;i<64;i++)mo<<(i?",":"")<<depthcounts[i];
        mo<<"],\"A_N\":"<<ji(A[N])<<",\"B_N\":"<<ji(B[N])<<",\"R\":"<<ji(R)
          <<",\"Rlog\":"<<ji(Rlog)<<",\"enumerated_R\":"<<ji(smallR)
          <<",\"enumerated_Rlog\":"<<ji(smallLog)<<",\"residual_R\":"<<ji(residualR)
          <<",\"residual_Rlog\":"<<ji(residualLog)<<",\"clipped_tail\":"<<ji(clipped)
          <<",\"far_tail\":"<<ji(far)<<",\"positive_tail\":"<<ji(tail)<<",\"failures\":[]}\n";
        mo.close();
        constexpr u64 BLOCK=1000000;
        I edgeSum{0,0}; u64 rows=0,updates=0,pos=0,neg=0,zero=0; i64 maxwidth=0;
        std::ofstream bl(root+"/complementary-mass-blocks.tsv");
        bl<<"first\tlast\tupdates\tlower\tupper\tpositive\tnegative\tstraddling\tmax_width\n";
        for(u64 lo=N+1;lo<=H;lo+=BLOCK) {
            u64 hi=std::min(H,lo+BLOCK-1),bu=0,bp=0,bn=0,bz=0;
            std::vector<I> c(hi-lo+1,{0,0});
            for(auto d:edge) {
                if(d.d>hi)continue;
                u64 qlo=(lo+d.d-1)/d.d,qhi=std::min(N,hi/d.d);
                for(u64 q=qlo;q<=qhi;q++) {
                    I v=mul(d.r,a[q]);
                    I &z=c[d.d*q-lo];
                    z=d.sign>0?add(z,v):sub(z,v); bu++;
                }
            }
            I s{0,0}; i64 bw=0;
            for(auto z:c) {
                s=add(s,absolute(z)); bw=std::max(bw,narrow((i128)z.h-z.l));
                if(z.l>0)bp++;else if(z.h<0)bn++;else bz++;
            }
            edgeSum=add(edgeSum,s); updates+=bu;rows+=c.size();
            pos+=bp;neg+=bn;zero+=bz;maxwidth=std::max(maxwidth,bw);
            bl<<lo<<'\t'<<hi<<'\t'<<bu<<'\t'<<s.l<<'\t'<<s.h<<'\t'<<bp<<'\t'<<bn<<'\t'<<bz<<'\t'<<bw<<'\n';
            bl.flush();
            if((lo-N-1)/BLOCK%10==0)std::cout<<"edge through "<<hi<<"/"<<H<<" grid="<<ji(edgeSum)<<std::endl;
        }
        bl.close();assert(rows==H-N && pos+neg+zero==rows);
        I complement=add(edgeSum,tail);
        // Exact comparison with .301408572679396256667379418689.
        // numerator and denominator need >128 bits when multiplied by Q.
        // Use an equivalent certified, slightly stricter rational threshold.
        i64 threshold_floor=21718776569683232LL; // checked independently by Python reporter
        bool pass=complement.h<threshold_floor;
        std::ofstream out(root+"/complementary-mass-result.json");
        out<<"{\"Q\":\""<<Q<<"\",\"edge\":"<<ji(edgeSum)<<",\"positive_tail\":"<<ji(tail)
           <<",\"complement_majorant\":"<<ji(complement)<<",\"rows\":"<<rows
           <<",\"channel_updates\":"<<updates<<",\"positive\":"<<pos<<",\"negative\":"<<neg
           <<",\"straddling\":"<<zero<<",\"max_coefficient_width\":\""<<maxwidth
           <<"\",\"threshold_floor_grid\":\""<<threshold_floor<<"\",\"provisional_pass\":"<<(pass?"true":"false")
           <<",\"failures\":[]}\n";
        out.close();
        std::cout<<"Complete complement majorant grid="<<ji(complement)<<"; exact threshold comparison in Python reporter\n"
                 <<"Full results: "<<root<<"/complementary-mass-{moments,result}.json; all blocks/divisors saved; failures=0"<<std::endl;
    } catch(std::exception const&e) {
        std::ofstream out(root+"/complementary-mass-failure.json");
        out<<"{\"complete\":false,\"failure\":\""<<e.what()<<"\"}\n";
        std::cerr<<e.what()<<std::endl;return 1;
    }
}
