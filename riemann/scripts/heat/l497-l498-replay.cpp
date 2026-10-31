// Independent complete replay. No producer code, aggregates or binary-native decoding.
// Enumerate subsets by decreasing prime index; recompute each radius in increasing
// index order to compare the original intervals exactly. Edge channels are evaluated
// by decreasing divisor and decreasing q, with checked signed endpoint sums.
// Build without NDEBUG, with undefined-behavior sanitizer and no recovery.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>
#ifdef NDEBUG
#error Assertions must be enabled for the audit build
#endif
using Z = int64_t;
using W = __int128_t;
using U = uint64_t;
constexpr Z Q = Z(1) << 56;
constexpr U N = 691004, H = 110560640, T = 31720474772;
struct Box { Z lo=0, hi=0; };
U max_endpoint=0, all_updates=0;
void need(bool b, const char* s) { if (!b) throw std::runtime_error(s); }
Z checked(W v) {
    // Excluding INT64_MIN also makes every later scalar negation safe.
    need(v >= -W(INT64_MAX) && v <= W(INT64_MAX), "endpoint overflow");
    U magnitude=U(v<0?-v:v);
    max_endpoint=std::max(max_endpoint,magnitude);
    return Z(v);
}
Z down(W v) { return checked(v>=0 ? v/Q : -((-v+Q-1)/Q)); }
Z up(W v) { return checked(v>=0 ? (v+Q-1)/Q : -((-v)/Q)); }
Box plus(Box a,Box b) { return {checked(W(a.lo)+b.lo),checked(W(a.hi)+b.hi)}; }
Box minus(Box a,Box b) { return {checked(W(a.lo)-b.hi),checked(W(a.hi)-b.lo)}; }
Box product(Box a,Box b) {
    need(a.lo<=a.hi && b.lo<=b.hi,"invalid multiplicands");
    // Products lie in [-2^126,2^126]; +Q-1 and negation stay inside 128 bits.
    W low=W(a.lo)*b.lo, high=low;
    for(W v : {W(a.lo)*b.hi,W(a.hi)*b.lo,W(a.hi)*b.hi}) {
        low=std::min(low,v); high=std::max(high,v);
    }
    return {down(low),up(high)};
}
Box nonnegative(Box a) {
    need(a.lo<=a.hi && a.hi>=0,"nonnegative clipping mismatch");
    a.lo=std::max<Z>(a.lo,0);return a;
}
Box modulus(Box a) {
    need(a.lo<=a.hi,"coefficient order");
    if(a.lo>0)return a;
    if(a.hi<0)return {-a.hi,-a.lo};
    return {0,std::max(-a.lo,a.hi)};
}
bool same(Box a,Box b) { return a.lo==b.lo && a.hi==b.hi; }
std::string json(Box a) { return "[\""+std::to_string(a.lo)+"\",\""+std::to_string(a.hi)+"\"]"; }
U little_word(std::istream& in) {
    unsigned char buf[8];in.read(reinterpret_cast<char*>(buf),8);
    need(bool(in),"short binary record");
    U v=0;for(unsigned i=0;i<8;i++)v|=U(buf[i])<<(8*i);return v;
}
Z little_signed(std::istream& in) {
    U v=little_word(in);
    // Two's-complement decoding, without implementation-defined unsigned narrowing.
    return v<=U(INT64_MAX)?Z(v):-1-Z(~v);
}
void end_of_file(std::istream& in) {
    char c;need(!in.get(c) && in.eof() && !in.bad(),"trailing bytes or input failure");
}
void text_end(std::istream& in) {
    in>>std::ws;need(in.eof() && !in.bad(),"trailing text or input failure");
}
struct Prime { U p; Box radius,log; };
struct Divisor { U d; Box radius; int sign; };
std::vector<Prime> primes;
std::vector<Box> weights,A,B;
std::vector<Divisor> divisors;
std::array<U,64> depths{};
std::vector<int> chosen;
Box factor,small,small_log,clipped;
U count=0;

void consume_subset(U d) {
    Box r{Q,Q},logd{};
    // This is a fresh evaluation from the selected prime set, not a cached
    // producer radius. Increasing product order preserves exact comparability.
    for(auto it=chosen.rbegin();it!=chosen.rend();++it) {
        r=product(r,primes[*it].radius);
        logd=plus(logd,primes[*it].log);
    }
    ++count;++depths[chosen.size()];
    small=plus(small,r);small_log=plus(small_log,product(r,logd));
    if(d<=H)divisors.push_back({d,r,chosen.size()%2?-1:1});
    U cut0=std::min(N,H/d),cut1=std::min(N,T/d);
    need(cut0<=cut1 && cut1>=1,"split floors");
    Box rest_a=nonnegative(minus(A[N],A[cut1]));
    Box rest_b=nonnegative(minus(B[N],B[cut1]));
    Box unit=nonnegative(minus(A[cut1],A[cut0]));
    Box linear=nonnegative(minus(product(factor,plus(product(logd,rest_a),rest_b)),rest_a));
    clipped=plus(clipped,product(r,plus(unit,linear)));
}
void descending_subsets(int exclusive,U d) {
    consume_subset(d);
    // Distinct decreasing prime lists are precisely all squarefree subsets.
    // A too-large candidate is skipped, not used to prune smaller primes.
    for(int j=exclusive-1;j>=0;--j) {
        if(primes[j].p>T/d)continue;
        chosen.push_back(j);
        descending_subsets(j,d*primes[j].p);
        chosen.pop_back();
    }
}
// Deliberately wrapping FNV checksum is only a traversal fingerprint, never proof.
void checksum(U& hash,Z value) {
    U v=U(value);
    for(int j=0;j<8;j++){hash^=(v&255);hash*=1099511628211ULL;v>>=8;}
}
int main(int argc,char**argv) {
    std::string root=argc==2?argv[1]:"scripts/heat",outdir=root+"/mass-audit";
    try {
        static_assert(sizeof(Z)==8 && sizeof(W)==16,"integer widths");
        std::ifstream cf(root+"/complementary-mass-config.txt");
        U q,n,h,t;Z fl,fh;
        need(bool(cf>>q>>n>>h>>t>>fl>>fh),"config header read");
        need(q==U(Q)&&n==N&&h==H&&t==T&&0<fl&&fl<=fh,"config values");
        factor={fl,fh};
        for(U p=2;p<=307;++p) {
            bool prime=true;for(U k=2;k<=p/k;++k)if(p%k==0)prime=false;
            if(!prime)continue;
            Prime record;
            need(bool(cf>>record.p>>record.radius.lo>>record.radius.hi>>record.log.lo>>record.log.hi),"config prime read");
            need(record.p==p&&0<record.radius.lo&&record.radius.lo<=record.radius.hi&&record.radius.hi<Q,
                 "prime radius list");
            need(0<record.log.lo&&record.log.lo<=record.log.hi,"prime log");
            primes.push_back(record);
        }
        text_end(cf);need(primes.size()==63,"63 primes");
        weights.resize(N+1);A.resize(N+1);B.resize(N+1);
        std::ifstream seeds(root+"/complementary-mass-seeds.bin",std::ios::binary);
        size_t prime_index=0;
        for(U i=1;i<=N;i++) {
            Box w{little_signed(seeds),little_signed(seeds)};
            Box log{little_signed(seeds),little_signed(seeds)};
            need(0<=w.lo&&w.lo<=w.hi&&0<=log.lo&&log.lo<=log.hi,"seed positivity");
            if(i==1)need(same(w,{Q,Q})&&same(log,{0,0}),"q=1 seed");
            if(prime_index<primes.size()&&primes[prime_index].p==i) {
                need(same(w,primes[prime_index].radius)&&same(log,primes[prime_index].log),"prime seed match");
                prime_index++;
            }
            weights[i]=w;A[i]=plus(A[i-1],w);B[i]=plus(B[i-1],product(w,log));
        }
        end_of_file(seeds);need(prime_index==63,"all prime rows");
        descending_subsets(63,1);
        std::sort(divisors.begin(),divisors.end(),[](auto a,auto b){return a.d<b.d;});
        std::cout<<"Independent decreasing-subset enumeration: "<<count<<" through T, "<<divisors.size()<<" through H"<<std::endl;
        // Read the original complete edge divisor file with explicit endian decoding,
        // sort it, and compare every record with the independent enumeration.
        std::vector<Divisor> original;original.reserve(divisors.size());
        std::ifstream df(root+"/complementary-mass-divisors.bin",std::ios::binary);
        for(size_t i=0;i<divisors.size();++i) {
            Z d=little_signed(df);Box r{little_signed(df),little_signed(df)};Z sign=little_signed(df);
            need(d>=1&&U(d)<=H&&r.lo>=0&&r.lo<=r.hi&&(sign==1||sign==-1),"divisor record domain");
            original.push_back({U(d),r,int(sign)});
        }
        end_of_file(df);
        std::sort(original.begin(),original.end(),[](auto a,auto b){return a.d<b.d;});
        U expected_updates=0;
        for(size_t i=0;i<divisors.size();i++) {
            auto d=divisors[i],e=original[i];
            need(d.d==e.d&&same(d.radius,e.radius)&&d.sign==e.sign,"all divisor records");
            need(i==0||divisors[i-1].d<d.d,"unique divisors");
            U upper=std::min(N,H/d.d),lower=N/d.d;
            need(lower<=upper,"whole-edge q range");
            expected_updates+=upper-lower;
        }
        original.clear();original.shrink_to_fit();
        Box R{Q,Q},RL{};
        for(auto p:primes) {
            Box nextRL=plus(product(RL,plus({Q,Q},p.radius)),product(R,product(p.radius,p.log)));
            R=product(R,plus({Q,Q},p.radius));RL=nextRL;
        }
        Box residual=nonnegative(minus(R,small)),residual_log=nonnegative(minus(RL,small_log));
        Box far=nonnegative(minus(product(factor,plus(product(A[N],residual_log),product(B[N],residual))),product(A[N],residual)));
        Box tail=plus(clipped,far);
        std::map<std::string,Box> moments{{"A_N",A[N]},{"B_N",B[N]},{"R",R},{"Rlog",RL},
            {"enumerated_R",small},{"enumerated_Rlog",small_log},{"residual_R",residual},
            {"residual_Rlog",residual_log},{"clipped_tail",clipped},{"far_tail",far},{"positive_tail",tail}};
        std::ifstream expected(outdir+"/expected-moments.txt");
        for(size_t i=0;i<moments.size();i++) {
            std::string key;Box value;
            need(bool(expected>>key>>value.lo>>value.hi),"expected moment read");
            need(moments.count(key)&&same(value,moments.at(key)),"independent full moment equality");
        }
        std::string label;U c0,c1;
        need(bool(expected>>label>>c0>>c1)&&label=="counts"&&c0==count&&c1==divisors.size(),"divisor counts");
        need(bool(expected>>label)&&label=="depth","depth header");
        for(U d:depths){U e;need(bool(expected>>e)&&d==e,"every depth count");}
        text_end(expected);
        // Persist moments before the longer edge replay, explicitly incomplete.
        std::ofstream partial(outdir+"/replay-moments.json");partial.exceptions(std::ios::failbit|std::ios::badbit);
        partial<<"{\"complete_edge\":false,\"divisors_le_T\":"<<count<<",\"moments\":{";
        bool comma=false;for(auto kv:moments){if(comma)partial<<',';comma=true;partial<<'"'<<kv.first<<"\":"<<json(kv.second);}
        partial<<"},\"failures\":[]}\n";partial.close();
        std::cout<<"All clipped/residual moments and all 64 depth counts match exactly; edge replay starts"<<std::endl;
        std::ifstream blocks(root+"/complementary-mass-blocks.tsv");
        std::string header;std::getline(blocks,header);
        need(header=="first\tlast\tupdates\tlower\tupper\tpositive\tnegative\tstraddling\tmax_width","block header");
        std::ofstream hashes(outdir+"/coefficient-blocks.tsv");hashes.exceptions(std::ios::failbit|std::ios::badbit);
        hashes<<"first\tlast\tcount\tfnv1a64\tlower\tupper\n";
        Box edge{};U rows=0,total_positive=0,total_negative=0,total_zero=0,block_count=0;
        Z max_width=0;
        for(U first=N+1;first<=H;first+=1000000) {
            U last=std::min(H,first+999999);
            std::vector<Box> coeff(last-first+1);
            U updates=0;
            for(auto it=divisors.rbegin();it!=divisors.rend();++it) {
                U d=it->d;
                if(d>last)continue;
                U low=first/d+(first%d!=0),high=std::min(N,last/d);
                for(U k=high;k>=low;--k) {
                    need(k>=1&&d<=H/k,"channel index product bound");
                    U index=d*k;need(first<=index&&index<=last,"channel block membership");
                    Box contribution=product(it->radius,weights[k]);
                    auto& target=coeff[index-first];
                    target=it->sign==1?plus(target,contribution):minus(target,contribution);
                    ++updates;
                }
            }
            Box sum{};U positive=0,negative=0,zero=0,hash=14695981039346656037ULL;Z width=0;
            for(U i=0;i<coeff.size();i++) {
                Box value=coeff[i];sum=plus(sum,modulus(value));
                width=std::max(width,checked(W(value.hi)-value.lo));
                if(value.lo>0)++positive;else if(value.hi<0)++negative;else ++zero;
                checksum(hash,Z(first+i));checksum(hash,value.lo);checksum(hash,value.hi);
            }
            U oldfirst,oldlast,oldupdates,oldpositive,oldnegative,oldzero;Box oldsum;Z oldwidth;
            need(bool(blocks>>oldfirst>>oldlast>>oldupdates>>oldsum.lo>>oldsum.hi>>oldpositive>>oldnegative>>oldzero>>oldwidth),"full block read");
            need(first==oldfirst&&last==oldlast&&updates==oldupdates&&same(sum,oldsum)&&positive==oldpositive&&
                 negative==oldnegative&&zero==oldzero&&width==oldwidth,"every original block field");
            need(positive+negative+zero==coeff.size(),"every signed edge output");
            hashes<<first<<'\t'<<last<<'\t'<<coeff.size()<<'\t'<<hash<<'\t'<<sum.lo<<'\t'<<sum.hi<<'\n';hashes.flush();
            edge=plus(edge,sum);rows+=coeff.size();all_updates+=updates;
            total_positive+=positive;total_negative+=negative;total_zero+=zero;
            max_width=std::max(max_width,width);++block_count;
            if(block_count%20==0)std::cout<<"Every edge output replayed through "<<last<<"/"<<H<<std::endl;
        }
        text_end(blocks);hashes.close();
        need(rows==H-N&&all_updates==expected_updates&&block_count==110,"complete edge totals");
        Box complement=plus(edge,tail);
        std::ofstream result(outdir+"/replay.json");result.exceptions(std::ios::failbit|std::ios::badbit);
        result<<"{\"complete\":true,\"Q\":\""<<Q<<"\",\"divisors_le_T\":"<<count
              <<",\"divisors_le_H\":"<<divisors.size()<<",\"depth_counts\":[";
        for(size_t i=0;i<depths.size();i++)result<<(i?",":"")<<depths[i];
        result<<"],\"moments\":{";comma=false;
        for(auto kv:moments){if(comma)result<<',';comma=true;result<<'"'<<kv.first<<"\":"<<json(kv.second);}
        result<<"},\"edge\":"<<json(edge)<<",\"positive_tail\":"<<json(tail)
              <<",\"complement_majorant\":"<<json(complement)<<",\"rows\":"<<rows
              <<",\"channel_updates\":"<<all_updates<<",\"positive\":"<<total_positive
              <<",\"negative\":"<<total_negative<<",\"straddling\":"<<total_zero
              <<",\"max_coefficient_width\":\""<<max_width<<"\",\"blocks_checked\":"<<block_count
              <<",\"max_abs_endpoint\":\""<<max_endpoint<<"\",\"signed_64_limit\":\""<<INT64_MAX
              <<"\",\"failures\":[]}\n";result.close();
        std::cout<<"Complete independent replay: "<<rows<<" outputs, "<<all_updates<<" channels; complement grid "<<json(complement)
                 <<"; failures=0; certificate "<<outdir<<"/replay.json"<<std::endl;
    }catch(const std::exception& e){
        std::ofstream failure(outdir+"/replay-failure.json");
        failure<<"{\"complete\":false,\"failure\":\""<<e.what()<<"\"}\n";
        std::cerr<<e.what()<<std::endl;return 1;
    }
}
