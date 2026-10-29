# L128 — The fixed-spine two-source fixture fails at row weight six

## Hypotheses

Work over F₂, with N=2^k, k>=0, and the original L122 endpoints
A=Prod(F_N,G_N), B=Prod(G_N,F_N). F_N has parallel 1/x edges
f_i->f_(i+1), and G_N has x edges h_i->h_(i+1), for 0<=i<N.
Keep every original vertex, all three constant product connectors and
fresh s,t. Each endpoint's coordinate order is
`s,f0,...,fN,h0,...,hN,t`, and S=g(A)+g(B)=16N+20, where
g(H)=|V(H)|+2|E(H)| counts every singleton occurrence.

The middle graph V is only L122's pure-letter spine, with its own s,t:
vertices s,d_0,...,d_(2N-1),t; constant edges s->d_0 and d_N->t;
x edges d_i->d_(i+1) for i<2N-1 and d_(2N-1)->t. No endpoint
copy is included in V. In particular g(V)=6N+6.

Use the right-closed representation and scalar-arrow convention

    K_H=(I+C_H)^(-1), alpha_H=e_s K_H,
    M_H=D_H K_H, beta_H=e_t^T,
    alpha_U X=alpha_H, M_U X=X M_H, X beta_H=beta_U.

The approved fixture is A<-U->V<-W->B with distinct local sources.
For (A,V), let E_AV be the space of full paired rows (u,v) with equal
complete residual polynomial, where

    R_H(z)=sum_(m>=0) z^m M_H^m beta_H.

The sum is finite for these acyclic graphs. The proposed generator
family H_AV must lie in E_AV, contain at most 8N rows of combined
Hamming weight <=6, and span the paired initial row (alpha_A,alpha_V).
Its span must also be shift invariant; an analogous family is required
for (V,B). No full-relation spanning, independence, functional-row
condition, elementary companion or common-source flattening is assumed.
Zero-residual coordinates, both final coordinates and all boundaries
remain in the row weight. Arbitrary redundant finite generators are
allowed. Literal source realization and the entire expanded ledger are
additional obligations, not consequences of these row-space conditions.

## Conclusion

Every (u,v) in E_AV with u_(f_0)=1 satisfies

    wt(u,v) >= 2 sqrt(2N).                              (1)

At N=8 the minimum is exactly 8. Consequently all weight-at-most-six
rows of E_AV have zero A:f_0 coordinate, whereas the paired initial row
has coordinate one. It is outside their span. The approved fixture is
therefore impossible already at N=8, even without the 8N generator cap,
shift-invariance or occurrence-realization requirements. The same
weight-six obstruction holds for every dyadic N>=8.

The complete finite tests give:

| N | Pair | Relation dimension | Weight <=6 span rank | Initial in span | Span invariant |
|---|---|---:|---:|---|---|
| 4 | (A,V) | 13 | 13 | yes | yes |
| 4 | (V,B) | 13 | 13 | yes | yes |
| 8 | (A,V) | 21 | 20 | no | yes |
| 8 | (V,B) | 21 | 21 | yes | yes |

These are necessary-test results. No U or W occurrence graph, four-map
chain or fitting uniform ledger is constructed from the passing cases.
The separate conceptual audit in §6 validates the quantitative
specialization. It stops this fixed-spine weight-six mechanism, not
all larger-weight families, other middle graphs, arbitrary scalar chains
or the P-versus-NP problem. The recorded EXPLORE comparison did not find
this fixture result; that is not a certification of originality.

## Proof

### 1. Imported input and why a local specialization is needed

The pre-invocation assessment is
`drafts/literature/2026-10-29-two-local-source-spine-construction.md`.
The standard scalar simulation equations are imported from Ésik–Maletti,
*Simulation vs. Equivalence*, [arXiv:1004.2426v1, 14-Apr-2010,
Definition 3.1, p.4](https://arxiv.org/pdf/1004.2426v1).
F₂ and these finite word representations satisfy that definition.
Theorem 4.2's qualitative common-source construction supplies no sparse
row bound and is not used as a quantitative premise or reproved here.

The direct local inputs are L122 §2's complete original closed endpoint
and spine rows, and L126 §§1–2's Pascal identification and multilinear
support-product inequality, with its separate §7 audit. Specifically,
for P_N[j,ell]=binom(j,ell) mod 2 and a nonzero r in F₂^N, identify
r with f_r(X)=sum_j r_j product_(i in bits(j)) X_i. Then

    wt(r) wt(r P_N) >= 2^deg(f_r).                      (2)

All cancellations are already permitted in this input. Its full-relation
generating-set conclusion is not used. L127's restricted K_N obstruction
and Attempts 053–060 are contrasts, not premises. The new obligation is
to determine how coefficients are charged in the different (A,V) space.
This requires the specialization below; it does not require a reproof
of (2) or of qualitative simulation existence.

### 2. Complete residuals and the paired coefficient equations

Write y=1+z. L122's right-closed rows give

    R_A(f_i)=z^(N+1) y^(N-1-i)       (0<=i<N),
    R_A(h_i)=z^(N-i)                 (0<=i<N),
    R_A(s)=R_A(f_N)=R_A(h_N)=0,      R_A(t)=1.

For clarity, the last h row gives z, and each earlier h row adds one
letter. The f_i row gives
`z*(sum_(j=i+1)^(N-1) z^(N+1)y^(N-1-j)+z^N)`.
Using `1+z sum_(q=0)^(m-1) y^q=y^m`, with m=N-1-i and the empty
sum at m=0, this equals the stated f_i residual. Thus constants have
not been incorrectly counted as final values of closed states.

In V, the only exceptional letter rows are d_(N-1)->d_N+t and
d_(2N-1)->t. Hence

    R_V(d_i)=z^(N-i)+z^(2N-i)        (0<=i<N),
    R_V(d_i)=z^(2N-i)                (N<=i<2N),
    R_V(s)=0,                       R_V(t)=1.

In particular R_V(d_N)=z^N; its raw constant edge to t is not an
extra beta value. Both exceptional rows remain distinct for N=1.

For a full pair (u,v), define, without changing the charged coordinates,

    r_j=u_(f_(N-1-j))                          (0<=j<N),
    a_j=u_(h_(N-j)), b_j=v_(d_(N-j)),
    c_j=v_(d_(2N-j))                           (1<=j<=N),
    q=r P_N.

The high-degree residual of A is z^(N+1) sum_(ell=0)^(N-1) q_ell z^ell.
The high-degree residual of V is sum_(j=1)^N b_j z^(N+j).
Comparing degrees N+1,...,2N and then degrees 1,...,N proves that
the pair belongs to E_AV exactly when

    b_j=q_(j-1),    a_j=b_j+c_j       (1<=j<=N),
    u_t=v_t.                                             (3)

The four other coordinates u_s,u_(f_N),u_(h_N),v_s are free.
Every coefficient, including the constant coefficient, is covered.
The low and high degree ranges are disjoint, so no cross-range
cancellation was suppressed. Formula (3) also gives dimension 2N+5:
r and c are arbitrary, followed by the four free coordinates and one
common final coordinate.

The r,a,b,c blocks occupy distinct original coordinates. Since a+c=b,
wt(a)+wt(c)>=wt(b)=wt(q). All free and final contributions are
nonnegative. Consequently every full relation row satisfies

    wt(u,v) >= wt(r)+wt(a)+wt(b)+wt(c)
            >= wt(r)+2 wt(q).                            (4)

For each r this lower bound can be attained by choosing c=0, a=b,
all four free coordinates zero and both final coordinates zero.
No output-dead coordinate has been deleted or used to cancel a charged
core coordinate.

### 3. The forced initial coordinate rules out the fixture

If u_(f_0)=1, then r_(N-1)=1. The index N-1 has all k binary bits
set, so deg(f_r)=k, including k=0. Equation (2) gives
wt(r) wt(q)>=2^k=N. Both weights are positive. Applying AM–GM to
the two nonnegative quantities wt(r) and 2 wt(q) in (4) proves (1).
For N=8 the resulting bound is exactly 8, greater than the allowed 6.

Sharpness at N=8 is witnessed in the full original coordinates by

    u=f_0+f_1+f_2+f_3+h_0+h_4,   v=d_0+d_4.             (5)

Here r has indices 4,5,6,7, and q has indices 3,7. Both residuals
are z^4+z^8+z^12+z^16. Thus this really is a weight-eight relation
row with u_(f_0)=1. At N=4, the analogous pair
`u=f_0+f_1+h_0+h_2, v=d_0+d_2` has weight six, consistent with
the passing finite test. Neither witness alone spans the initial pair.

L122's closed initial row is
`alpha_A=s+sum_(i=0)^N f_i+h_0`, while `alpha_V=s+d_0`.
Their full pair has A:f_0=1. The coordinate functional extracting
A:f_0 vanishes on every admissible weight-six row at N=8, so it
vanishes on their entire span and separates that span from the
required initial pair. This rejects even arbitrarily many redundant
weight-six generators. The same argument applies for N>=8 because
2 sqrt(2N)>=8. Shift closure and an occurrence realization cannot
repair failed initial inclusion.

This condition is necessary for actual scalar arrows, not merely a
particular way of choosing a common source. If X:U->A and Y:U->V
are such arrows, their transition and final equations give, for every
m>=0,

    X M_A^m beta_A = M_U^m beta_U = Y M_V^m beta_V.

Thus each paired row of (X,Y) lies in E_AV. Their initial equations
give `alpha_U (X,Y)=(alpha_A,alpha_V)`. If all those paired rows have
weight <=6, the separating functional makes this impossible. Equivalently,
any proposed weight-six generating family whose span contains these rows
also fails. Adding a heavier boundary row would leave the assessed
fixture. No equality with the full relation or with a paired reachable
space is needed.

### 4. Complete finite evidence and independent computational reception

The constructor builds every literal A,V,B occurrence, checks topology,
right closure, both boundaries, all transition rows and the complete
residual columns against the displayed formulas. For B the formulas are
`R_B(f_i)=z y^(N-1-i)` and `R_B(h_i)=z^(N-i)+z^(2N-i)` for i<N,
with the same three zero rows and final residual one. They follow from
L122's complete closed B rows. All three accepted polynomials are
z^N+z^(2N).

For each pair it computes an independent kernel basis of the entire
residual matrix. Its rank is 2N+1: V alone spans degrees 0,...,2N,
and no displayed residual has greater degree. Hence each paired kernel
has dimension 2N+5. Gray enumeration visits every linear combination
of that independent basis, exactly 8,192 rows per pair at N=4 and
2,097,152 at N=8, and retains every weight-at-most-six row. The full
kernel, all retained rows, threshold ranks, span basis, initial row,
complete paired Krylov sequence and every tested shift image are saved.

An independent receiver imports no producer helpers. It binds the full
vertex and occurrence lists to the literal recipes, recomputes closure
using finite matrix powers and residuals by reverse topological
substitution, and enumerates coordinate subsets through weight six.
It examines all 110,056/110,056 subsets per pair at N=4 and all
3,345,616/3,345,616 at N=8. Every passing row agrees exactly with the
producer's full list. Independent elimination with lowest pivots checks
all threshold ranks, initial inclusion, paired Krylov inclusion and
invariance of each complete low-weight span. All four invariance checks
pass; the N=8 AV initial and Krylov inclusion checks fail as recorded.
Invariance alone has therefore not been confused with initial inclusion.

The complete lists of rank by threshold 0,...,6 are

    N=4 AV: [0,4,9,10,12,12,13];  VB: [0,4,10,12,13,13,13].
    N=8 AV: [0,4,13,14,17,17,20]; VB: [0,4,14,17,20,20,21].

Both scripts also check every r with r_(N-1)=1, namely 8/8 parameter
values at N=4 and 128/128 at N=8. They compute the complete q and
wt(r)+2wt(q) table, receiving minima 6 and 8. The receiver reconstructs
Pascal rows by multiplying by 1+z and checks every support product
against N. The minimum witnesses are received directly against every
residual coefficient. This finite evidence supports, but does not
replace, the all-k proof using (2). No partial enumeration, sampled
value, hash or preview supplies the obstruction.

The full artifacts are
`scripts/batched-incidence/output-554/two-local-source-certificate.json`
and `scripts/batched-incidence/output-554/two-local-source-receipt.json`.
The former's complete histograms are produced by kernel enumeration;
the independent reception concerns every weight-six row, rank and
initial/shift test, and the full selected parameter table, not every
higher-weight histogram bin. Neither script reports a verification
failure. The rejected fixture test is preserved separately as a failure.

Reproduce in order:

```bash
python3 scripts/batched-incidence/check_two_local_sources.py \
  --output scripts/batched-incidence/output-554/two-local-source-certificate.json
python3 scripts/batched-incidence/receive_two_local_sources.py \
  scripts/batched-incidence/output-554/two-local-source-certificate.json \
  --output scripts/batched-incidence/output-554/two-local-source-receipt.json
```

### 5. Scope and remaining gaps

The proposed uniform threshold was the sum of all four expanded map
supports plus 2(g(U)+g(V)+g(W)) <= C*(16N+20), with C independent
of k, subject to the fixed weight-six mechanism. Initial inclusion
already fails, before any source graph or ledger exists. There is no
claim here that the unrestricted linear threshold fails: larger or
nonuniform row weights, different middle graphs and other chains are
outside this stop. In particular the single-row square-root bound is
not itself a superlinear total-support theorem.

The computational reception above belongs to the construction attempt;
the separate conceptual audit and complete replay are recorded in §6.
General operands and mixed letters, actual fourth comparison reception,
Boolean/K/H/nonzero-fJ reception, total resources and certificate
availability, L087 W₂, unrestricted ER/Frege/SAT and P versus NP remain
unresolved. No transport, cap, format or historical failed evidence is
changed.

### 6. Separate conceptual audit — 2026-10-29, step 556

**Verdict: the stated fixed-spine obstruction passes.** This is a
reproduction and independent scrutiny of §§1–5, not a stronger bound,
new construction or certified novelty. The pre-existing EXPLORE scope
`drafts/literature/2026-10-29-two-local-source-obstruction-conceptual-audit.md`
is reused. L122 §2 and L126 §§1–2 with its §7 audit remain the only
direct local mathematical inputs. The scalar equations retain the
precise Ésik–Maletti citation in §1. No large-characteristic theorem,
full-relation spanning or common-source flattening is imported.

**Complete residuals and all coordinates.** Starting with L122's rows,
the final h letter gives z and each predecessor contributes one factor
z. For f_i, the f_N residual is zero and h_0 contributes z^N; the
finite sum in §2 gives z^(N+1)y^(N-1-i), including the empty sum at
i=N-1. In V the letter into d_N has a constant tail to t, whereas
beta_(d_N)=0. Hence its two possible exit lengths give exactly the
two displayed terms for i<N and one term for i>=N. At N=1, d_0 and
d_1 are distinct and both exceptional rows are still included. The
rows s,f_N,h_N in A and s in V have residual zero, while each t has
residual one. No raw constant suffix has been counted twice.

For each j=1,...,N, the high coefficient z^(N+j) is q_(j-1) on A
and b_j on V; the low coefficient z^j is a_j on A and b_j+c_j on
V. Constants give u_t=v_t. There are no other degrees. This proves
both necessity and sufficiency of (3), not merely some relations.
The r block is the N original f coordinates with indices below N;
a is the N original h coordinates below N; b uses V's d_0,...,d_(N-1);
c uses d_N,...,d_(2N-1). These four blocks and the four free coordinates
and two final coordinates are pairwise disjoint. Free coordinates add
nonnegative weight and the shared final parameter adds either zero or
two. In each position a_j+c_j=b_j forces at least b_j ones in (a,c).
This proves wt(u,v)>=wt(r)+2wt(q) after all cancellations, with no
double charge. Taking c=0, a=b and the free/final coordinates zero
also verifies attainability for every r. The parameter count is 2N+5.

**Degree, threshold and witnesses.** Pascal row multiplication is
translation of the multilinear coefficient polynomial, as checked in
L126. The forced index N-1 corresponds to its unique degree-k monomial;
no other index can cancel it. This includes the nonzero constant case
k=0. Thus the nonzero r and q satisfy wt(r)wt(q)>=N, and AM–GM applied
to wt(r) and 2wt(q) gives 2sqrt(2N). At N=8 the lower bound is 8>6;
for larger dyadic N it is at least 8. At N=1 the lower bound is
2sqrt(2), consistent with the attainable integer weight three; the
argument never asserts a weight-six stop for all N.

For the displayed N=8 witness, the sum of the four relevant Pascal
rows is y^4(1+y+y^2+y^3)=z^3+z^7. Its A high part is therefore
z^12+z^16, with h_0+h_4 adding z^8+z^4. The two V coordinates give
exactly those four degrees. For N=4 the corresponding sum is
y^2+y^3=z+z^3; both residuals are z^2+z^4+z^6+z^8. The supplementary
audit checks every coefficient and both weights in the original graphs.
These witnesses establish the two stated sharpness values only.

**The initial condition is necessary for arbitrary scalar rows.**
The A initial row has f_0 coefficient one because its constant closure
visits f_0 exactly once. In the full paired space that coordinate
functional is zero on every admitted weight-six row at N>=8. Linearity
therefore excludes the entire span, independent of redundancy or the
number of generators. For any alleged U arrows, induction from
M_U X=X M_A and X beta_A=beta_U gives
X M_A^m beta_A=M_U^m beta_U for every m; the Y equation gives the
same column on the V side. Each paired map row consequently satisfies
all residual coefficients, including degree zero. The initial equations
express the paired initial row as the alpha_U-weighted sum of these
rows, contradicting the functional. The inference does not assume a
particular alpha_U, a functional map, full E_AV spanning, a paired Krylov
basis, or acyclicity of U. Those extra promises cannot repair it.

**Finite coverage and full saved evidence.** Read both producer and
receiver in full, together with the producer's directly imported
`act`, `endpoint`, `insert`, `pascal`, and `rank` helpers. The producer's
kernel is independent, consists of zero-syndrome rows and has dimension
width minus the residual rank. V spans every degree 0,...,2N: its last
N coordinates supply degrees 1,...,N; its first N then supply the high
degrees after cancelling those low terms; t supplies degree zero.
The binary reflected Gray traversal toggles basis index v_2(i) on step
i. It therefore enumerates every combination once. The counts are
8,192/8,192 for each N=4 pair and 2,097,152/2,097,152 for each N=8 pair.

The independent receiver binds every vertex and literal occurrence,
uses finite constant-matrix powers for K and topological substitution
for all residual coefficients, then visits every coordinate subset of
weights zero through six. Its exact counts are 110,056/110,056 per N=4
pair and 3,345,616/3,345,616 per N=8 pair. Complete passing lists agree,
and lowest-pivot elimination reproduces all four threshold-rank lists
in §4. Kernel independence, initial inclusion, every paired Krylov row,
and images of a full admitted-span basis are checked. This last basis
test suffices for invariance by linearity; it is not evidence of initial
inclusion. The N=8 AV initial/Krylov failure and all four successful
invariance tests remain exactly as stated.

Both scripts were rerun into `scripts/batched-incidence/output-556/`.
Every value of the regenerated producer certificate equals the original
step-554 value. Every receiver value equals its original counterpart
except the input path, with both distinct paths checked explicitly.
The supplementary script `scripts/batched-incidence/audit_two_local_source_replay.py`
also checks stored coordinate labels, echelon pivots, every serialized
initial/Krylov remainder, every shift image and remainder, all 400/400
and 966/966 admitted AV rows against the full coefficient equations and
disjoint charge, and both displayed witnesses. All 65/65 comparison
checks pass. The receiver independently checks all 8/8 and 128/128
selected r parameters, their complete q values and support products,
and obtains minima six and eight. There are no verification failures;
the sole fixture failure remains N=8 AV initial inclusion.

The original higher-weight histograms are fully reproduced and compared,
but their bins are not independently received by coordinate enumeration.
Neither those bins nor a status flag or preview is used to establish
the all-k obstruction. The complete supplementary evidence is in
`scripts/batched-incidence/output-556/audit-replay-comparison.json`.
Reproduce with the two §4 commands using output-556 in both paths, then:

```bash
python3 scripts/batched-incidence/audit_two_local_source_replay.py
```

**Limits retained.** This establishes an audited obstruction for the
stated weight-six fixed-spine mechanism. It is not a superlinear
total-support theorem. No U/W occurrence realization, four-map chain,
new wire/work/live bound or actual fourth-comparison receipt results.
The independent gaps in §5 and the exact P-versus-NP goal remain open.

## Mathlib

Full matching coverage has not been checked. Finite-dimensional kernels,
Pascal coefficients and AM–GM are supporting mathematics, not a received
Mathlib theorem for this exact fixed-spine obstruction. The quantitative
input (2) is L126's canonical proof and separate local audit; neither
script is a formal proof certificate received by Mathlib. Unknown
availability is not evidence of absence.
