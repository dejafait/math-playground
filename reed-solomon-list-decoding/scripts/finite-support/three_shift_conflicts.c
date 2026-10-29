/* Exact complete-support scan for L131, only c=0,1,-1.
 * Input: the 2*7*137 graph-label images as subgroup exponents.
 * Outputs: every intersection byte and every qualifying (f,g,size) record.
 * Index f=((w*137)+v)*137+u. Records use little-endian uint32 fields.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { Q=137, N=2571353, WORDS=16 };
static const int ts[7]={16,64,70,102,112,118,121};
static const int shifts[3]={0,1,-1};
static void put(uint64_t *s,int e) { s[e/64]|=UINT64_C(1)<<(e%64); }
static int size(const uint64_t *s) {
    int n=0; for(int j=0;j<WORDS;j++) n+=__builtin_popcountll(s[j]); return n;
}
static void u32(FILE *f,uint32_t x) {
    for(int j=0;j<4;j++) if(fputc((x>>(8*j))&255,f)==EOF) exit(3);
}
int main(int argc,char **argv) {
    if(argc!=3) return 2;
    FILE *in=fopen(argv[1],"r"); if(!in) return 2;
    int map[2][7][Q];
    for(int s=0;s<2;s++) for(int t=0;t<7;t++) for(int y=0;y<Q;y++)
        if(fscanf(in,"%d",&map[s][t][y])!=1 || map[s][t][y]<0 || map[s][t][y]>=1024) return 2;
    int extra; if(fscanf(in,"%d",&extra)!=EOF) return 2; fclose(in);
    FILE *counts[3],*edges[3]; char path[4096];
    for(int c=0;c<3;c++) {
        snprintf(path,sizeof path,"%s/shift-%d-intersections.u8",argv[2],shifts[c]);
        counts[c]=fopen(path,"wb");
        snprintf(path,sizeof path,"%s/shift-%d-conflicts.u32",argv[2],shifts[c]);
        edges[c]=fopen(path,"wb"); if(!counts[c] || !edges[c]) return 2;
    }
    unsigned char *seen[3][2];
    for(int c=0;c<3;c++) for(int s=0;s<2;s++) {
        seen[c][s]=calloc(N,1); if(!seen[c][s]) return 2;
    }
    uint64_t core[2][WORDS]={{0}},hist[3][69]={{0}},qual[3]={0};
    uint64_t repeated[3]={0},bad_sizes=0;
    for(int s=0;s<2;s++) { for(int e=12;e<72;e++) put(core[s],e); put(core[s],s?10:0); }
    for(int w=0;w<Q;w++) for(int v=0;v<Q;v++) for(int u=0;u<Q;u++) {
        uint32_t f=(w*Q+v)*Q+u;
        uint64_t left[WORDS],right[3][WORDS]; memcpy(left,core[0],sizeof left);
        for(int c=0;c<3;c++) memcpy(right[c],core[1],sizeof left);
        for(int j=0;j<7;j++) {
            int y=(u+v*ts[j]+w*ts[j]*ts[j])%Q;
            put(left,map[0][j][y]);
            for(int c=0;c<3;c++) put(right[c],map[1][j][(y+shifts[c]+Q)%Q]);
        }
        if(size(left)!=68) bad_sizes++;
        for(int c=0;c<3;c++) {
            if(size(right[c])!=68) bad_sizes++;
            int intersection=0;
            for(int j=0;j<WORDS;j++) intersection+=__builtin_popcountll(left[j]&right[c][j]);
            hist[c][intersection]++;
            if(fputc(intersection,counts[c])==EOF) return 3;
            if(intersection>63 && intersection<68) {
                uint32_t g=(w*Q+v)*Q+(u+shifts[c]+Q)%Q;
                if(seen[c][0][f] || seen[c][1][g]) repeated[c]++;
                seen[c][0][f]=seen[c][1][g]=1; qual[c]++;
                u32(edges[c],f); u32(edges[c],g); u32(edges[c],intersection);
            }
        }
    }
    printf("{\"bad_support_sizes\":%llu,\"shifts\":[",(unsigned long long)bad_sizes);
    for(int c=0;c<3;c++) {
        if(fclose(counts[c]) || fclose(edges[c])) return 3;
        printf("%s{\"c\":%d,\"matching_size\":%llu,\"repeated_tagged_endpoints\":%llu,\"histogram\":[",
            c?",":"",shifts[c],(unsigned long long)qual[c],(unsigned long long)repeated[c]);
        for(int j=0;j<=68;j++) printf("%s%llu",j?",":"",(unsigned long long)hist[c][j]);
        printf("]}");
    }
    printf("]}\n"); return bad_sizes?1:0;
}
