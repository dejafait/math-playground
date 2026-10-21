/* Exhaustive subgroup conjugacy classes by unfiltered one-element extension.
 * Input/output protocol is supplied by all_smaller.py. No GAP catalogue.
 * Right multiplication closure uses positive generators (finite groups).
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#define N 3960
#define W ((N+63)/64)
#define HS (1u<<20)
#define MAXGEN 16
typedef uint16_t E;
typedef struct { uint64_t b[W]; int order, cls; E conj; } Sub;
typedef struct { int node, ng; E gen[MAXGEN]; } Rep;
static E *mt, inv[N], gg[4], ident;
static unsigned char perms[N][15];
static int ph[16384], sh[HS];
static Sub **subs; static int ns, caps;
static Rep *reps; static int nr, capr;
static inline E mul(E a,E b) { return mt[(size_t)a*N+b]; }
static inline int has(const uint64_t *b,E x) { return (b[x/64]>>(x%64))&1; }
static inline void put(uint64_t *b,E x) { b[x/64]|=(uint64_t)1<<(x%64); }
static uint64_t hashbytes(const unsigned char *p,int n) {
    uint64_t h=1469598103934665603ULL;
    for(int i=0;i<n;i++) { h^=p[i]; h*=1099511628211ULL; } return h;
}
static unsigned slot(const uint64_t *b) {
    unsigned k=(unsigned)hashbytes((const unsigned char*)b,sizeof(uint64_t)*W)&(HS-1);
    while(sh[k] && memcmp(subs[sh[k]-1]->b,b,sizeof(uint64_t)*W)) k=(k+1)&(HS-1);
    return k;
}
static int addnode(const uint64_t *b,int order,int cls,E conj) {
    if(ns>=caps) { caps=caps?caps*2:1024; subs=realloc(subs,caps*sizeof(*subs)); }
    Sub *s=malloc(sizeof(*s)); memcpy(s->b,b,sizeof(s->b));
    s->order=order; s->cls=cls; s->conj=conj;
    int i=ns++; subs[i]=s; sh[slot(b)]=i+1; return i;
}
static int closure(const E *gens,int ng,uint64_t *b) {
    memset(b,0,sizeof(uint64_t)*W); E q[N]; int end=1; q[0]=ident; put(b,ident);
    for(int i=0;i<end;i++) for(int j=0;j<ng;j++) {
        E x=mul(q[i],gens[j]); if(!has(b,x)) {put(b,x);q[end++]=x;}
    } return end;
}
static void conjugate(const uint64_t *b,E g,uint64_t *out) {
    memset(out,0,sizeof(uint64_t)*W);
    for(E x=0;x<N;x++) if(has(b,x)) put(out,mul(mul(g,x),inv[g]));
}
static int register_subgroup(const uint64_t *b,int order,const E *gens,int ng,E *witness) {
    unsigned z=slot(b); if(sh[z]) {
        Sub *s=subs[sh[z]-1]; *witness=s->conj; return s->cls;
    }
    if(nr>=capr) {capr=capr?capr*2:64;reps=realloc(reps,capr*sizeof(*reps));}
    int cls=nr++; int first=addnode(b,order,cls,ident);
    reps[cls].node=first; reps[cls].ng=ng; memcpy(reps[cls].gen,gens,ng*sizeof(E));
    /* Orbit of subgroup under the four generators = every conjugate. */
    int *queue=malloc(N*sizeof(int));int end=1;queue[0]=first;
    for(int i=0;i<end;i++) for(int j=0;j<4;j++) {
        Sub *s=subs[queue[i]]; uint64_t c[W];conjugate(s->b,gg[j],c);
        unsigned k=slot(c);
        if(!sh[k]) {
            if(end>=N) {fprintf(stderr,"conjugate bound failure\n");exit(2);}
            queue[end++]=addnode(c,order,cls,mul(gg[j],s->conj));
        } else if(subs[sh[k]-1]->cls!=cls) {fprintf(stderr,"fusion failure\n");exit(2);}
    }
    free(queue); *witness=ident;return cls;
}
static void elems(FILE *f,const uint64_t *b) {
    fputc('[',f);int first=1;for(E x=0;x<N;x++)if(has(b,x)) {
        fprintf(f,"%s%u",first?"":",",x);first=0;
    }fputc(']',f);
}
static void arr(FILE *f,const E *a,int n) {
    fputc('[',f);for(int i=0;i<n;i++)fprintf(f,"%s%u",i?",":"",a[i]);fputc(']',f);
}
int main(int argc,char **argv) {
    if(argc!=3)return 2;
    FILE *fi=fopen(argv[1],"r");if(!fi)return 2;int n,id;
    if(fscanf(fi,"%d %d",&n,&id)!=2 || n!=N)return 2;ident=id;
    for(int j=0;j<4;j++)if(fscanf(fi,"%hu",&gg[j])!=1)return 2;
    for(int i=0;i<N;i++)for(int j=0;j<15;j++){int x;if(fscanf(fi,"%d",&x)!=1)return 2;perms[i][j]=x;}
    fclose(fi);
    for(int i=0;i<N;i++) {
        unsigned k=hashbytes(perms[i],15)&16383;
        while(ph[k])k=(k+1)&16383;ph[k]=i+1;
    }
    mt=malloc((size_t)N*N*sizeof(E));
    for(E a=0;a<N;a++)for(E b=0;b<N;b++) {
        unsigned char p[15];for(int j=0;j<15;j++)p[j]=perms[a][perms[b][j]];
        unsigned k=hashbytes(p,15)&16383;
        while(ph[k]&&memcmp(p,perms[ph[k]-1],15))k=(k+1)&16383;
        if(!ph[k]){fprintf(stderr,"group closure failure\n");return 2;}
        E c=ph[k]-1;mt[(size_t)a*N+b]=c;if(c==ident)inv[a]=b;
    }
    uint64_t full[W];if(closure(gg,4,full)!=N){fprintf(stderr,"group generation failure\n");return 2;}
    char path[1024];snprintf(path,sizeof(path),"%s-multiplication.bin",argv[2]);
    FILE *fb=fopen(path,"wb");if(!fb)return 2;
    if(fwrite(mt,sizeof(E),(size_t)N*N,fb)!=(size_t)N*N)return 2;fclose(fb);
    uint64_t b[W];int order=closure(NULL,0,b);E witness;
    register_subgroup(b,order,NULL,0,&witness);
    snprintf(path,sizeof(path),"%s-classes.jsonl",argv[2]);
    FILE *fo=fopen(path,"w");if(!fo)return 2;
    time_t start=time(NULL);int processed=0;
    for(int k=0;k<nr;k++) {
        /* reps can realloc during register_subgroup, so copy current row. */
        Rep r=reps[k];Sub *s=subs[r.node];
        uint64_t nb[W]={0},nclosure[W];E ngens[MAXGEN];int nng=0;
        for(E x=0;x<N;x++) {
            int ok=1;for(int j=0;j<r.ng;j++)if(!has(s->b,mul(mul(x,r.gen[j]),inv[x]))){ok=0;break;}
            if(ok)put(nb,x);
        }
        closure(NULL,0,nclosure);
        for(E x=0;x<N;x++)if(has(nb,x)&&!has(nclosure,x)) {
            if(nng>=MAXGEN)return 2;ngens[nng++]=x;closure(ngens,nng,nclosure);
        }
        if(memcmp(nb,nclosure,sizeof(nb))) {fprintf(stderr,"normalizer failure\n");return 2;}
        /* Orbits in G under K left/right multiplication and N_G(K) conjugation. */
        int orb[N];for(int i=0;i<N;i++)orb[i]=-1;
        E oq[N],og[N],wg[N];int targets[N],norb=0;
        for(E g=0;g<N;g++)if(orb[g]<0) {
            int end=1;oq[0]=g;orb[g]=norb;
            for(int i=0;i<end;i++) {
                E x=oq[i];
                for(int j=0;j<2*r.ng+nng;j++) {
                    E y=j<r.ng?mul(r.gen[j],x):j<2*r.ng?mul(x,r.gen[j-r.ng]):mul(mul(ngens[j-2*r.ng],x),inv[ngens[j-2*r.ng]]);
                    if(orb[y]<0){orb[y]=norb;oq[end++]=y;}
                    else if(orb[y]!=norb)return 2;
                }
            }
            og[norb]=g;
            E gen[MAXGEN];memcpy(gen,r.gen,r.ng*sizeof(E));int lng=r.ng;
            if(!has(s->b,g))gen[lng++]=g;
            if(lng>MAXGEN)return 2;
            int ord=closure(gen,lng,b);targets[norb]=register_subgroup(b,ord,gen,lng,&wg[norb]);norb++;
        }
        fprintf(fo,"{\"class\":%d,\"order\":%d,\"generators\":",k,s->order);arr(fo,r.gen,r.ng);
        fprintf(fo,",\"elements\":");elems(fo,s->b);
        fprintf(fo,",\"normalizer_generators\":");arr(fo,ngens,nng);
        fprintf(fo,",\"normalizer_elements\":");elems(fo,nb);
        fprintf(fo,",\"element_orbit_ids\":[");for(int i=0;i<N;i++)fprintf(fo,"%s%d",i?",":"",orb[i]);
        fprintf(fo,"],\"extensions\":[");for(int i=0;i<norb;i++)fprintf(fo,"%s{\"element\":%u,\"class\":%d,\"conjugator\":%u}",i?",":"",og[i],targets[i],wg[i]);
        fprintf(fo,"]}\n");fflush(fo);processed++;
        if(k%10==0){printf("Processed %d subgroup classes; discovered %d; actual subgroups %d\n",processed,nr,ns);fflush(stdout);}
        if(time(NULL)-start>240)break;
    }
    fclose(fo);
    snprintf(path,sizeof(path),"%s-summary.json",argv[2]);fo=fopen(path,"w");
    fprintf(fo,"{\"complete\":%s,\"processed_classes\":%d,\"discovered_classes\":%d,\"actual_subgroups\":%d,\"identity\":%u,\"group_order\":3960,\"index_bound\":35,\"failures\":[]}\n",processed==nr?"true":"false",processed,nr,ns,ident);fclose(fo);
    snprintf(path,sizeof(path),"%s-conjugates.jsonl",argv[2]);fo=fopen(path,"w");
    for(int i=0;i<ns;i++){Sub *s=subs[i];fprintf(fo,"{\"class\":%d,\"conjugator\":%u,\"elements\":",s->cls,s->conj);elems(fo,s->b);fprintf(fo,"}\n");}fclose(fo);
    printf("Enumeration %s: processed %d/%d classes, %d actual subgroups\n",processed==nr?"COMPLETE":"UNFINISHED",processed,nr,ns);
    return processed==nr?0:3;
}
