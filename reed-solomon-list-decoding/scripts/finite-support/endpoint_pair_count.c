/* Exact L123 enumeration. Input/output text; histogram input little-endian u32. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <assert.h>

static uint32_t q, n, nr, *hist, *row, *scale, *inv;
static uint32_t mod(int64_t x) { x %= q; return (uint32_t)(x < 0 ? x+q : x); }
static uint32_t occupancy(uint32_t u, uint32_t v) {
    return hist[(size_t)row[u]*q + (uint64_t)v*scale[u]%q];
}
int main(int argc, char **argv) {
    assert(argc==4);
    FILE *in=fopen(argv[1],"r"); assert(in);
    assert(fscanf(in,"%u%u%u",&q,&n,&nr)==3);
    uint32_t *H=calloc(n,sizeof(*H)), *reps=calloc(nr,sizeof(*reps));
    inv=calloc(q,sizeof(*inv)); row=calloc(q,sizeof(*row)); scale=calloc(q,sizeof(*scale));
    assert(H && reps && inv && row && scale);
    for(uint32_t i=0;i<n;i++) assert(fscanf(in,"%u",H+i)==1);
    for(uint32_t i=0;i<nr;i++) assert(fscanf(in,"%u",reps+i)==1);
    fclose(in);
    inv[1]=1;
    for(uint32_t a=2;a<q;a++) inv[a]=q-(uint64_t)(q/a)*inv[q%a]%q;
    row[0]=1; scale[0]=1;
    for(uint32_t j=0;j<nr;j++) for(uint32_t i=0;i<n;i++) {
        uint32_t u=(uint64_t)reps[j]*H[i]%q;
        assert(row[u]==0); row[u]=j+2;
        scale[u]=(uint64_t)inv[H[i]]*inv[H[i]]%q;
    }
    for(uint32_t u=1;u<q;u++) assert(row[u]>=2);
    hist=calloc((size_t)(nr+2)*q,sizeof(*hist)); assert(hist);
    in=fopen(argv[2],"rb"); assert(in);
    for(size_t i=0;i<(size_t)(nr+2)*q;i++) {
        unsigned char b[4]; assert(fread(b,1,4,in)==4);
        hist[i]=(uint32_t)b[0]|(uint32_t)b[1]<<8|(uint32_t)b[2]<<16|(uint32_t)b[3]<<24;
    }
    assert(fgetc(in)==EOF); fclose(in);
    uint32_t np=n*(n-1)/2, z=0;
    uint32_t *bs=calloc(np,sizeof(*bs)), *bt=calloc(np,sizeof(*bt));
    uint32_t *bi=calloc(np,sizeof(*bi)), *bj=calloc(np,sizeof(*bj));
    uint64_t *same=calloc(n,sizeof(*same)), *diff=calloc(n,sizeof(*diff));
    assert(bs && bt && bi && bj && same && diff);
    for(uint32_t i=0;i<n;i++) for(uint32_t j=i+1;j<n;j++) {
        bs[z]=(H[i]+H[j])%q; bt[z]=(uint64_t)H[i]*H[j]%q;
        bi[z]=i; bj[z++]=j;
    }
    assert(z==np);
    for(uint32_t k=0;k<n;k++) {
        uint32_t x=H[k]; if(x==1) continue;
        uint32_t s=(1+x)%q, t=x, r=hist[s];
        if(r>=3) same[k]+=3ULL*(r-1)*(r-2);
        for(uint32_t u=0;u<q;u++) {
            if(u==1 || u==x) continue; /* precisely the stars through A */
            r=occupancy(u,mod((int64_t)t-(int64_t)u*s));
            assert(r>=1 && r<=n/2);
            if(r>=3) same[k]+=3ULL*(r-1)*(r-2);
        }
        for(uint32_t p=0;p<np;p++) {
            uint32_t b=H[bi[p]], c=H[bj[p]];
            if(b==1 || c==1 || b==x || c==x) continue;
            uint32_t ds=mod((int64_t)bs[p]-s);
            if(ds==0) r=hist[s];
            else {
                uint32_t u=(uint64_t)mod((int64_t)bt[p]-t)*inv[ds]%q;
                uint32_t v=mod((int64_t)t-(int64_t)u*s);
                assert(v!=mod(-(int64_t)u*u));
                r=occupancy(u,v);
            }
            assert(r>=2 && r<=n/2);
            uint64_t w=6ULL*(r-2);
            diff[bi[p]]+=w; diff[bj[p]]+=w;
        }
    }
    FILE *out=fopen(argv[3],"w"); assert(out);
    for(uint32_t i=0;i<n;i++) if(H[i]!=1)
        fprintf(out,"%u %" PRIu64 " %" PRIu64 "\n",H[i],same[i],diff[i]);
    assert(fclose(out)==0);
    return 0;
}
