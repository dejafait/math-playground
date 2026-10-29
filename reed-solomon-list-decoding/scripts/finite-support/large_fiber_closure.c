/* Exact auxiliary equality-fiber closure; no coefficient assignment is made.
 * Build: cc -O3 -std=c11 scripts/finite-support/large_fiber_closure.c
 *        -o scripts/finite-support/large-fiber-closure-bin
 * Run: scripts/finite-support/large-fiber-closure-bin
 * Certificate records are little-endian uint16 values:
 * seed C, full flag, trace length, followed by the ordered point trace.
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum { Q=137, N=18769, D=7, NL=959, STOP=411, B=258 };
static const int directions[D]={16,64,70,102,112,118,121};
static uint16_t point_lines[N][D], line_points[NL][Q];
static uint16_t queue[N];
static uint8_t seen[N], counts[N], active[NL];

static void put16(FILE *f, unsigned n) {
    if (fputc(n & 255, f)==EOF || fputc((n>>8)&255, f)==EOF) {
        perror("write certificate"); exit(1);
    }
}

static void setup(void) {
    for (int v=0;v<Q;v++) for (int u=0;u<Q;u++) {
        int p=u+Q*v;
        for (int j=0;j<D;j++) {
            int y=(u+directions[j]*v)%Q;
            point_lines[p][j]=(uint16_t)(j*Q+y);
            line_points[j*Q+y][v]=(uint16_t)p;
        }
    }
}

/* All queued points have already been justified by previously processed
 * lines, apart from the explicitly supplied seeds. A successful certificate
 * uses only the processed prefix; a proper closure uses the whole queue. */
static int closure(const uint16_t *seeds, int nseed, int *trace_len,
                   int *line_count) {
    memset(seen,0,sizeof seen); memset(counts,0,sizeof counts);
    memset(active,0,sizeof active);
    int head=0, tail=0, total=0;
    for (int i=0;i<nseed;i++) if (!seen[seeds[i]]) {
        seen[seeds[i]]=1; queue[tail++]=seeds[i];
    }
    while (head<tail) {
        int p=queue[head++];
        for (int j=0;j<D;j++) {
            int l=point_lines[p][j];
            if (active[l]) continue;
            active[l]=1; total++;
            if (total==STOP) {
                *trace_len=head; *line_count=total; return 1;
            }
            for (int k=0;k<Q;k++) {
                int r=line_points[l][k];
                counts[r]++;
                if (counts[r]>=3 && !seen[r]) {
                    seen[r]=1; queue[tail++]=(uint16_t)r;
                }
            }
        }
    }
    *trace_len=tail; *line_count=total; return 0;
}

static int collinear(void) {
    const char *cert="scripts/finite-support/large-fiber-collinear-traces.u16";
    const char *tab="scripts/finite-support/large-fiber-collinear-results.tsv";
    FILE *f=fopen(cert,"wb"), *g=fopen(tab,"w");
    if (!f || !g) { perror("open collinear outputs"); return 1; }
    fprintf(g,"direction_index\tparameter\tforces_full\ttrace_points\tactive_lines\n");
    for (int j=0;j<D;j++) {
        int bad=0, full=0;
        for (int r=0;r<Q;r++) {
            int u=(Q-(directions[j]*r)%Q)%Q;
            uint16_t seeds[3]={0,(uint16_t)(Q+Q-directions[j]),(uint16_t)(u+Q*r)};
            int len, lines, yes=closure(seeds,3,&len,&lines);
            if (yes) full++; else bad++;
            put16(f,j); put16(f,r); put16(f,yes); put16(f,len);
            for (int k=0;k<len;k++) put16(f,queue[k]);
            fprintf(g,"%d\t%d\t%d\t%d\t%d\n",j,r,yes,len,lines);
        }
        printf("Direction %d: %d full, %d exceptional parameters including 0,1.\n",directions[j],full,bad);
    }
    if (fclose(f) || fclose(g)) { perror("close collinear outputs"); return 1; }
    printf("Certificate: %s\nResults: %s\n",cert,tab);
    return 0;
}

int main(int argc, char **argv) {
    const char *cert="scripts/finite-support/large-fiber-pair-traces.u16";
    const char *tab="scripts/finite-support/large-fiber-pair-results.tsv";
    const char *summary="scripts/finite-support/large-fiber-pair-summary.json";
    setup();
    if (argc==2 && strcmp(argv[1],"collinear")==0) return collinear();
    if (argc!=1) { fprintf(stderr,"Usage: %s [collinear]\n",argv[0]); return 1; }
    FILE *f=fopen(cert,"wb"), *g=fopen(tab,"w");
    if (!f || !g) { perror("open outputs"); return 1; }
    fprintf(g,"seed_C\tforces_full\ttrace_points\tactive_lines\n");
    int bad=0, full=0, max_bad=0, max_trace=0;
    for (int c=0;c<N;c++) {
        uint16_t seeds[3]={0,B,(uint16_t)c}; int len, lines;
        int yes=closure(seeds,3,&len,&lines);
        if (yes) full++; else { bad++; if (len>max_bad) max_bad=len; }
        if (len>max_trace) max_trace=len;
        put16(f,c); put16(f,yes); put16(f,len);
        for (int k=0;k<len;k++) put16(f,queue[k]);
        fprintf(g,"%d\t%d\t%d\t%d\n",c,yes,len,lines);
    }
    if (fclose(f) || fclose(g)) { perror("close outputs"); return 1; }
    FILE *h=fopen(summary,"w"); if (!h) { perror("summary"); return 1; }
    fprintf(h,"{\n  \"q\":137,\n  \"directions\":[16,64,70,102,112,118,121],\n");
    fprintf(h,"  \"pair\":[[0,0],[121,1]],\n  \"seeds_checked\":%d,\n",N);
    fprintf(h,"  \"full_seeds\":%d,\n  \"exceptional_seeds\":%d,\n",full,bad);
    fprintf(h,"  \"required_exceptional_bound\":272,\n  \"pair_bound_pass\":%s,\n",bad<=272?"true":"false");
    fprintf(h,"  \"max_proper_closure\":%d,\n  \"max_trace_points\":%d,\n",max_bad,max_trace);
    fprintf(h,"  \"full_stop_active_lines\":411,\n  \"traces\":\"%s\",\n  \"results\":\"%s\"\n}\n",cert,tab);
    if (fclose(h)) { perror("close summary"); return 1; }
    printf("Checked %d seeds: %d full, %d exceptional; required <=272.\n",N,full,bad);
    printf("Largest proper closure %d; longest proof trace %d.\n",max_bad,max_trace);
    printf("Summary: %s\nCertificate: %s\n",summary,cert);
    return 0;
}
