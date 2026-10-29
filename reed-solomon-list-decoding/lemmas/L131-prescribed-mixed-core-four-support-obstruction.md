# L131 — A prescribed mixed-core ambient four-support obstruction

## Hypotheses

Use L031's pinned instance, inherited from C001a: E=F_65537,
F=F_(65537^28), k=64, H=<g> of order 1024 with g=19139,
and any integer m>=1. Write h_e=g^e for 0<=e<1024.
In the edge order 12,13,14,23,24,34 set

\[
 U_{ij}=\{h_{2r},h_{2r+1}\}\quad(r=0,\ldots,5),\qquad
 K=\{h_{12},\ldots,h_{71}\},\qquad
 W_i=\{h_{72+2(i-1)},h_{73+2(i-1)}\}.
\]

Take exactly L031's consecutive supports

\[
 S_i=K\cup W_i\cup\bigcup_{j\ne i}U_{\min(i,j),\max(i,j)}.
\]

Put a=h_0, b=h_10, C=K union {a}, C'=K union {b}.
Use L030's auxiliary q=137, T={16,64,70,102,112,118,121},
Omega=(T times F_q) disjoint union {d_0,d_1,d_2,d_3}, and
B_f={(t,f(t)):t in T} for degree-at-most-two auxiliary polynomials.
These auxiliary polynomials do not represent RS messages over F.
Prescribe p(Z)=0 and r(Z)=Z-16 over F_q.

## Conclusion

There are explicitly specified bijections sigma:Omega -> H minus C
and sigma':Omega -> H minus C' satisfying

\[
 C\cup\sigma(B_p)=S_1,\quad C\cup\sigma(B_r)=S_2,\quad
 C'\cup\sigma'(B_p)=S_3,\quad C'\cup\sigma'(B_r)=S_4,
 \qquad \sigma(16,1)=b,\quad \sigma'(d_0)=a.
\]

Thus these maps satisfy L130's left distinguished-column constraint
with y_0=1 and its conditional right-dummy constraint. The right ambient
star through a is empty, hence the two ambient stars have no common
support. The selected left supports omit b. All four supports have
size 68, their six pair intersections have size 62, and every triple
and the fourfold intersection equal K. Each side lies in its unchanged
L030 ambient family; this particular four-support union also satisfies
the distinct-support intersection bound 63.

Nevertheless no four pairwise distinct m-tuples of F-polynomials of
row degree <64 can agree with one center H -> F^m on these respective
supports, for any m>=1, even allowing additional agreements.

This is an explicit ambient example, not a claim that L130's favorable
averaging event or endpoint deletion preserves the four supports. No
simultaneous large retained families for these specific maps, universal
occurrence, extremal cap, unsafe list or improved safety radius follows.

## Proof

**Coverage and imported input.** The invocation-start SPECIALIZE
[assessment](../drafts/literature/2026-10-26-mixed-core-l031-embedding.md)
covers exactly these supports, polynomials, fixed images and ordered
signature matching. L030 supplies the arbitrary-label ambient families;
L130 supplies the distinguished-label sample-space model, not favorable
retention for an arbitrarily chosen right map. L031's separately audited
consecutive-example nonrealizability is imported, without redoing its
rank calculation. Its primary framework is Alrabiah, Guruswami and Li,
*Randomly punctured Reed–Solomon codes achieve list-decoding capacity
over linear-sized fields*, [arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3),
26 July 2023, Definition 2.5 and Lemma 2.7, printed pp. 7–8; the
common-root division is the case in Shangguan–Tamo,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1),
4 November 2019, Lemma 4.3, printed pp. 11–12. The only remaining
specialization is this finite labeling construction. No generic-domain
rank assertion or field-preserving relabeling is used.

**Residual sets.** The distinct exponents show that K, the six U_ij
and four W_i are mutually disjoint. Hence |S_i|=60+6+2=68,
S_i intersect S_j=K union U_ij, and any intersection involving at
least three supports is K: a point outside K belongs to at most two
supports. Also C is contained in S_1,S_2, and C' in S_3,S_4.
Their two residual pairs are

\[
\begin{aligned}
R_1&=\{h_1\}\cup U_{13}\cup U_{14}\cup W_1,&
R_2&=\{h_1\}\cup U_{23}\cup U_{24}\cup W_2,\\
R_3&=\{h_{11}\}\cup U_{13}\cup U_{23}\cup W_3,&
R_4&=\{h_{11}\}\cup U_{14}\cup U_{24}\cup W_4.
\end{aligned}
\]

Here R_1=S_1 minus C, R_2=S_2 minus C, R_3=S_3 minus C',
R_4=S_4 minus C'. Each residual has size seven. The left pair
intersects precisely at h_1, the right pair at h_11. The point b
belongs to neither R_1 nor R_2, and a belongs to neither R_3 nor R_4;
they are in the respective target complements.

**Complete bijection prescription.** A membership signature of a label
is its two indicator bits in the specified ordered pair of sets.
The domain pair is (B_p,B_r) on both sides. Since r(t)=0 iff t=16,
its common part is {(16,0)}, and its two exclusive parts have size six.
The two target pairs are (R_1,R_2) in H minus C and (R_3,R_4) in
H minus C'. All three ground sets have size 963. Thus on each side
the full signature counts are

| Signature | Domain | Target | After the fixed image, on each side |
| --- | ---: | ---: | ---: |
| 00 | 950 | 950 | 949 |
| 01 | 6 | 6 | 6 |
| 10 | 6 | 6 | 6 |
| 11 | 1 | 1 | 1 |

Indeed the union of either pair has size 7+7-1=13. The domain point
(16,1) is in neither graph, since p(16)=r(16)=0; its prescribed left
image b has signature 00. The dummy d_0 is in neither graph; its
prescribed right image a also has signature 00. Fix these two images
on their respective sides, and remove each fixed domain point and
image before matching the remaining labels.

Order graph labels first by T's displayed order, then by the symbol
representatives 0,...,136; place d_0,d_1,d_2,d_3 last in that order.
Order actual labels by their unique exponents 0,...,1023. Within each
signature class match the remaining domain labels to the remaining
target labels in these orders. The last table column proves equal
finite lengths for every match. Each restricted match is a bijection,
different signatures are disjoint, and the removed fixed image is
used exactly once. Their unions with the fixed assignments therefore
give full bijections sigma and sigma'. Signature preservation gives
the exact images of both graphs on each side; adjoining the respective
core gives all four claimed support identities. In particular
sigma(16,0)=h_1 and sigma'(16,0)=h_11. This specifies every map value,
including all unused graph labels and all four dummies.

**Star and packing qualifications.** Since sigma' is injective and
sigma'(d_0)=a, no graph label maps to a. Every B_f consists only of
graph labels, so no right residual block contains a; neither does C'.
Thus the full right ambient star through a is empty. On the left,
both selected graph blocks avoid (16,1); injectivity therefore gives
omission of b. The six selected pair intersections are K union U_ij
of size 62<=63, including all four cross pairs. L030 separately gives
the local packing for each full ambient family. No statement that the
union of those full ambient families is packed is made.

**Common-center obstruction.** These actual four supports are exactly
L031's consecutive example, with its original vertex and edge orders,
core and private sets. All its disjointness and field hypotheses hold.
L031's audited rank-12 conclusion rules out a realization by four
pairwise distinct polynomial tuples for every m>=1. Its necessity
already allows coefficients throughout F and extra center agreements.
Only ambient memberships were constructed here; the actual subgroup
labels of L031 were never transported through a putative field map.

**Finite evidence.** Run
`python3 scripts/finite-support/mixed_core_l031_embedding.py`.
The full certificate is `scripts/finite-support/mixed-core-l031-embedding.json`.
It contains both complete 963-entry maps in domain order, all support,
core, pair and private sets, all eleven intersections of order >=2,
signature counts before/after fixed assignments, and 84 exact checks
with actual and required values. It compares the entire reconstructed
domain and all configuration data with the read-only original
`four-support-rank-results.json`, recording its SHA-256. No rank is
recomputed or certified from a summary: L031 is the proved input.
All 84 checks pass with no failures. Complete signature counts and
check outcomes were inspected; no sampled-map verification substitutes
for the finite-set proof above. This is local REPRODUCTION of the
assessed framework with a new embedding, not certified originality
beyond the sources checked. The separate critical audit below accepts
this restricted statement without correction.

**Separate critical audit (2026-10-26, step 511).** The invocation-start
SPECIALIZE [audit assessment](../drafts/literature/2026-10-26-l131-critical-audit-coverage.md)
covers this exact prescription. Run
`python3 scripts/finite-support/critical_audit_l131.py`; its complete
read-only-input replay is `scripts/finite-support/l131-critical-audit.json`.
All 2215 checks pass, including independent verification of every one
of the 1926 saved map entries. The audit generates H by multiplication
recurrence, rather than importing the embedding generator. It compares
the entire ordered domain, all six pairs, the core, private sets and
four complete supports with both the original L031 certificate and its
prior independent audit; their source hashes agree. No rank is recomputed.

For each side it checks the complete domain order, all 963 distinct
images, the entire target complement and every saved exponent. Each
map entry is checked against its rank within the appropriate ordered
signature class after removing the fixed assignment. Thus the 950/6/6/1
counts, reduced to 949/6/6/1, establish full bijections, including unused
labels and dummies. Both complete residual and support identities,
the images of (16,0), all six pair intersections, four triple
intersections and the fourfold intersection pass. Injectivity and the
entire inverse image sigma'^{-1}(a)={d_0} establish absence of a from
every right graph block, and a is outside C'. This proves an empty
right ambient star for the whole family, without sampling polynomials.

The logical import also passes: the actual supports and vertex/edge
orders are exactly L031's consecutive example, not images of that
example under a proposed field map. Its mutually disjoint 60-core,
six pair-only two-sets and four private two-sets have all 80 distinct
labels in H. Its degree-60 common-root division leaves degree at most
three in each row; the imported full rank over E stays full over F
by its nonzero minor. Hence each reduced row is zero and all four
tuples would be equal, contradicting pairwise distinctness for every
m>=1. Additional center agreements only impose more conditions.
This checks applicability of the already audited input, not a new
rank proof or a scalar-projection assumption.

The audit retains all limitations: these conditional labelings lie
in L130's sample space, but membership alone gives no favorable
averaging event, survival under deletion or simultaneous large
retention for these maps. The full ambient union is not claimed packed.
No universal occurrence, quantitative cap or RS safety improvement
follows. The audit is local REPRODUCTION, with full and supporting
Mathlib coverage still not checked. No direct mathematical input or
DAG edge changes.

## Mathlib

Full matching mixed-core embedding and its fixed-subgroup obstruction:
**not checked**. Supporting finite-set partition, ordered matching,
polynomial and extension-rank results: **not checked**. Unknown coverage
does not assert absence. The nonrealizability input and primary source
citations are given above; no new rank theorem is reproved here.
