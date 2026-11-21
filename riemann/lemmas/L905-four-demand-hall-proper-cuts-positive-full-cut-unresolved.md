# Lemma 905: fourteen proper Hall cuts pass; the full cut remains unresolved

## Hypotheses

Use L898's full actual-theta probability marginal at y=0, with
Phi(u)=K(|u|)/2, p=u+v, q=u-v, W_0=p^2 Phi(u)Phi(v), and
A_0=integral W_0>0. Every theta index and both spatial directions are
included. Set a=pi/16, b=pi/32, F={-2,-1,0,1}, and

\[
 P_j=[(2j-1/2)a,(2j+1/2)a],\quad
 N_k=[(2k+1/2)a,(2k+3/2)a],
\]
\[
 r_j=\int_{P_j}\cos(16q)\,d\mu(q),\qquad
 d_k=-\int_{N_k}\cos(16q)\,d\mu(q),\qquad
 H(S)=\sum_{j\in T(S)}r_j-\sum_{k\in S}d_k,
 \quad T(S)=\bigcup_{k\in S}\{k,k+1\}.
\]

The numerical claims assume L037's outward-rounded Decimal basic
operations, correctly rounded exp widened to adjacent neighbors,
rejection of exceptional arithmetic, and its rational Machin pi
enclosure. Python Decimal and execution of the script below are trusted,
not independently formally verified. Precision is 70. No RH, total
first-sign premise, or allocation feasibility is assumed.

## Conclusion

Under these contracts, every nonempty proper subset S of F satisfies

\[
                         H(S)>1/100.
\]

For the remaining cut the computed rigorous enclosure is only

\[
                         -1/125<H(F)<1/100.
\]

This interval contains zero. No negative cut is certified, and the test
does not certify all fifteen necessary inequalities. It therefore neither
rejects variable nearest-neighbor sharing nor establishes even the selected
four-demand allocation, much less infinite feasibility or Xi positivity.
The fourteen margins are a local specialization/calculation, not a new
general resource theorem or a claimed advance beyond the literature.
The separate critical audit in step139 validates these finite claims under
the stated arithmetic contracts; it leaves the full-cut sign unresolved.

## Proof

### Capacity specialization and locality

The general finite weighted-Hall feasibility theorem is Koperberg,
*Couplings and Matchings: Combinatorial notes on Strassen's theorem*,
[arXiv:2202.02092v1](https://arxiv.org/pdf/2202.02092v1), Proposition 4,
pp5–6. It assumes equal side totals and nonnegative vertex weights.
Only its necessary-cut calculation is used here; its sufficient direction
is not applied with unequal totals or to countably many lobes.

For the present upper capacities, suppose a proposed conserved allocation
uses nonnegative amounts f_{j,k}, supported only when j=k or j=k+1,
with sum_j f_{j,k}=d_k and sum_k f_{j,k}<=r_j. Then for any finite S,

\[
 \sum_{k\in S}d_k
 =\sum_{j\in T(S)}\sum_{k\in S}f_{j,k}
 \leq\sum_{j\in T(S)}r_j.
\]

This checks the necessary calculation with demand equality and resource
upper capacity, instead of assuming equal positive and negative totals.
Each resource is counted once in the union T(S). Any unused resource is
a nonnegative surplus; it is not removed from a prospective global
identity. No positive lobe outside T(S) is permitted to supply S under
this rule, regardless of how much mass it contains. Consequently a
negative finite cut would be a genuine obstruction without an infinite
tail-sign premise. This implication does not assert existence of an
allocation. Absolute integrability in L898 makes all the individual
resources and demands finite; cosine has the asserted sign on each lobe.

### Full density, reflection and normalization

Put t=(u+v)/2. Then u=t+q/2, v=t-q/2, and the absolute Jacobian is one.
The factor four in p^2 cancels the factor 1/4 in Phi(u)Phi(v). Reflection
in t and in q gives the even unnormalized density

\[
 \rho(q)=2\int_0^\infty
 t^2K(t+q/2)K(|t-q/2|)\,dt\quad(q\geq0).
 \tag{1}
\]

L898 supplies absolute Fubini and polynomial domination for these
operations. If M_r=integral_0^infinity u^r K(u)du, r=0,2, expanding
(u+v)^2 and using oddness of the cross term gives

\[
                             A_0=2M_0M_2>0.                 \tag{2}
\]

Let B_0 be the integral of rho(q)cos(16q) on [0,b]; let B_l be its
integral on [(2l-1)b,(2l+1)b] for 1<=l<=4. Evenness gives exactly

\[
 A_0r_0=2B_0,\quad A_0r_{-1}=A_0r_1=B_2,\quad
 A_0r_{-2}=A_0r_2=B_4,
\]
\[
 A_0d_{-1}=A_0d_0=-B_1,\qquad
 A_0d_{-2}=A_0d_1=-B_3.                                \tag{3}
\]

Thus the complete central positive lobe is retained, and every other
selected lobe is a complete lobe. In particular A_0H(F)=2 sum_{l=0}^4 B_l.
Reflection identifies values, not two independent supplies of one resource.
L904's earlier fixed-half-share sign is motivation only, not an input.

### Complete errors on the larger domain

The domain now extends to q=9b, beyond L904's tested q=5b. Use L312's
proved uniform estimates, with K_4 the four-term theta head:

\[
 0<K_4\leq K<16,\quad 0\leq K-K_4\leq\epsilon=160000e^{-75},
 \qquad K(u)\leq256e^{9u/2-3e^{2u}}\quad(u\geq0).
\]

Choose T=pi/2 in the t direction. On 0<=t<=T, product subtraction
is between zero and 32 epsilon, so (1)'s density error is at most

\[
 E_\theta=512\epsilon/3,
\]

since 2 integral_0^T t^2dt<16/3. For t>=T and 0<=q<=9pi/32,
t-q/2>=23pi/64>0. The two exponentials therefore combine exactly to give

\[
 K(t+q/2)K(t-q/2)
 \leq65536\exp(9t-3e^{2t}(e^q+e^{-q}))
 \leq65536\exp(9t-6e^{2t}).
\]

Enlarge t>=T to t>=3/2. For t=3/2+w, e^3>20 and e^{2w}>=1+2w
give 9t-6e^{2t}<=-106-231w. Integrating 2t^2 times the product bound
yields the uniform complete spatial-density error

\[
 E_s=131072e^{-106}
 \left(\frac9{4\cdot231}+\frac3{231^2}+\frac2{231^3}\right).
 \tag{4}
\]

Both transverse directions are already included by (1)'s factor two.
The absolute omitted error is <=b(E_theta+E_s) in B_0 and
<=2b(E_theta+E_s) in each other B_l. These are bounds for every theta
index and the complete unbounded t tails, uniformly on the enlarged
domain. No tail outside the q lobes belongs to these defined capacities.

For (2), finite-interval theta errors are <=2 epsilon and <=8 epsilon/3.
For u=3/2+w, L312 gives K(u)<=256 exp(-53-115w). The omitted spatial
errors in M_0,M_2 are therefore at most

\[
 H_0=256e^{-53}/115,\qquad
 H_2=256e^{-53}\left(\frac9{4\cdot115}+\frac3{115^2}+\frac2{115^3}\right).
 \tag{5}
\]

### Finite-box inclusion and implementation

For M in {64,128}, put h=pi/(64M). Partition [0,T] into 32M t cells
[ih,(i+1)h] and [0,9b] into 9M q cells [2jh,2(j+1)h]. On each cell,
the kernel arguments are enclosed by

\[
 [(i+j)h,(i+j+2)h],\qquad
 \big|[(i-j-1)h,(i-j+1)h]\big|.
\]

An interval crossing the reflected seam has absolute image starting at
zero. Evaluate K_4's explicit finite exponential formula with L037's
interval operations, intersecting with [0,16] justified by L312. Positive
summands for u>=0 justify the lower intersection. Kernel cache entries
are indexed by the exact integer endpoints of these pi-scaled intervals.

The separable weights, integrated exactly before interval evaluation, are

\[
 T_i=2h^3((i+1)^3-i^3)/3,\quad
 Q_j=\{\sin(\pi(j+1)/(2M))-\sin(\pi j/(2M))\}/16.
\]

Each q cell lies within one fixed-sign cosine lobe. If [l,r] bounds the
nonnegative kernel product throughout a cell, its integral lies in
T_i Q_j[l,r], reversing endpoints when Q_j<0. This integrates pointwise
inequalities against a measure of fixed sign; it has no unproved
midpoint or analytic quadrature remainder. Lobe boundaries j=M,3M,5M,
7M,9M are exact grid boundaries. The central half-lobe starts at j=0.

Pi uncertainty is propagated through the exact grid and integrated
weights; there is no missing irrational endpoint strip. The reused
degree-49 sine/cosine Taylor enclosures reduce by an integer multiple of
2pi, check absolute radius <=4, and add radius^50/50!. Exact multiples
of pi/2 are replaced by 0 or +/-1 only after containment checks. Every
Q_j is checked strictly signed. No differentiation crosses a reflection
seam. The finite M_0,M_2 boxes use K_4 on [ih,(i+1)h] with weights h and
h^3((i+1)^3-i^3)/3; add the positive errors (5) and the theta errors.

The whole-box method reuses the source-reviewed method of Fredrik
Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1), Section 2,
steps 2–4 and Section 2.1, pp2–4. The elementary separable-weight
specialization and the enlarged-domain tails are justified above; the
source itself supplies no theta capacity signs. No general Hall theorem
is reproved, and no higher-order quadrature theorem is assumed.

The script `scripts/theta-marginal/variable_hall_cuts_137.py` reuses the
checked interval/trigonometric helpers, executes their arithmetic
self-check, forms every neighbor union, and uses (3) to generate all
fifteen integer coefficient vectors. It saves every kernel-cache value,
cosine weight, tail, lobe enclosure, resource, demand and cut. Reproduce:

```
python3 scripts/theta-marginal/variable_hall_cuts_137.py --mesh 64 --output scripts/theta-marginal/variable-hall-cuts-137-m64.json
python3 scripts/theta-marginal/variable_hall_cuts_137.py --mesh 128 --output scripts/theta-marginal/variable-hall-cuts-137-m128.json
```

The declared budget was M=64 and, only if unresolved, M=128. These used
1,179,648 and 4,718,592 boxes, respectively. The first run already passed
all fourteen proper cuts, but its full cut contained zero. The final
run's complete `/bounds`, `/result/complete_B`, `/result/A0` and
`/result/cuts` were inspected using the shared JSON inspector with
`--full` on each selected field. The decisive coarser strict rational
enclosures from the second certificate are:

| S (reflected pairs grouped) | Lower A_0 H(S) | Upper A_0 H(S) |
| --- | --- | --- |
| {-2}, {1} | 0.00114816 | 0.00121249 |
| {-1}, {0} | 0.00224814 | 0.00248407 |
| {-2,-1}, {0,1} | 0.00182739 | 0.00208212 |
| {-2,0}, {-1,1} | 0.00339630 | 0.00369656 |
| {-2,1} | 0.00229633 | 0.00242498 |
| {-1,0} | 0.00066034 | 0.00102719 |
| {-2,-1,0}, {-1,0,1} | 0.00023960 | 0.00062524 |
| {-2,-1,1}, {-2,0,1} | 0.00297556 | 0.00329461 |
| F | -0.00018115 | 0.00022330 |

Also 0.022681<A_0<0.023. Thus all proper cuts satisfy
H(S)>0.00023960/0.023>1/100. For F, the displayed bounds imply
H(F)>-0.00018115/0.022681>-1/125 and
H(F)<0.00022330/0.022681<1/100. They do not determine its sign.

For error scale, E_theta<7.315e-26, E_s<1.185e-43, and the respective
B_l tail errors are <7.181e-27 and <1.437e-26. Normalizer spatial errors
are <2.138e-23 and <4.866e-23. The full-cut enclosure width is greater
than 0.000404 in unnormalized units: interval range overestimation, not
the omitted tails, prevents a sign decision. No midpoint is used as
evidence for the unknown sign. The required threshold is H(S)>=0 for
every S, or a strict negative upper endpoint for an obstruction. Neither
full-batch decision is achieved. Stop at this budget, preserving both
certificates; no further grid or lobe/frequency sweep follows.

### Separate critical audit, 8 November 2026 — step139

The locality argument uses only nonnegative conserved flows, demand
equality and upper capacities; Koperberg's equal-total sufficient direction
is not invoked. The Jacobian of (t,q) to (u,v) is -1. Reflection in t
gives exactly (1), and evenness in q gives (3), including the central
factor two. The domination in L898 applies to these changes of variables
and the normalizer expansion. L019/L020's kernel conventions agree.
No total cosine sign, L904 sign or L313 sign is used.

The audit checked the enlarged-domain and complete-tail bounds directly.
For t>=pi/2 and q<=9pi/32, t-q/2>=23pi/64>0, so both arguments admit
L312's half-line exponential bound. With t=3/2+w the exponent is at most
13.5+9w-120(1+2w)=-106.5-231w<=-106-231w; integration yields (4).
For a single kernel the corresponding exponent is at most
6.75+4.5w-60(1+2w)<=-53-115w, yielding (5). The finite-head product
error is <=32epsilon, and 2T^3/3<16/3 gives E_theta. Integrating a
uniform density error over each complete lobe gives the stated errors.
For the moments, T<2 gives theta errors <=2epsilon and <=8epsilon/3.
The absolute-image seam, fixed cosine signs and pi-scaled endpoints are
included as described above; no derivative or midpoint assumption is used.

The independent audit script is
`scripts/theta-marginal/audit_variable_hall_139.py`. It reads both original
certificates without modifying them, runs the inherited arithmetic
self-check, regenerates every cached K_4 enclosure and every integrated
cosine weight, and compares all tail constants. Its transcendental
evaluations retain L037's trusted Decimal/exp contract.

The summation check uses exact integer arithmetic instead of replaying the
original interval summation. All saved decimal kernel endpoints have a
common denominator 10^D; all cosine-weight endpoints have another such
denominator. Put Delta_i=(i+1)^3-i^3. For each q cell, it sums
Delta_i times the products of the appropriate nonnegative lower kernel
endpoints, and separately the upper products, over every t cell. It then
multiplies by the cosine-weight endpoints, reversing lower/upper choices
on negative cells, and accumulates into the five lobes. Dividing by the
exact common integer scales and multiplying by the interval for 2h^3/3
gives rational bounds for every finite B_l. Both endpoints of every such
bound lie inside the corresponding saved finite enclosure. This check
covers all 1,179,648 and 4,718,592 boxes and the complete cache key sets.
The same exact procedure checks M_0 and M_2, adds the complete positive
errors and verifies A_0=2M_0M_2. It checks the symmetric lobe errors,
resources, demands and all fifteen neighbor unions/coefficient vectors.
Exact rational sum/division checks verify every saved cut interval and
every displayed coarse rational bound above, including the error scales
and the full-cut width. Thus summation rounding cannot explain away an
unresolved sign or invalidate a claimed strict comparison.

Run the audit with
`python3 scripts/theta-marginal/audit_variable_hall_139.py`.
The complete check results, source-certificate hashes, exact reconstructed
sums and cut comparisons are saved in
`scripts/theta-marginal/variable-hall-audit-139.json`.
There were no failed checks. M=64's weakest proper lower bound is only
0.00202718956..., still positive; M=128's is
0.01041768752...>1/100. The latter certificate's full normalized enclosure
remains [-0.00798658997...,0.00984476745...], where these displayed
approximations are descriptive only: the exact original endpoints and
rational comparisons are retained in the certificates. The audit
validates the stated M=128 conclusions, not a stronger claim for M=64.
It supplies neither an all-cut sign nor an infinite allocation, and does
not reopen the exhausted numerical campaign. ∎

## Mathlib

Full matching coverage and supporting formalizations are not checked;
availability is unknown. No Mathlib theorem is claimed for this finite
calculation, weighted-Hall specialization, or implementation. The
inherited arithmetic contract is documented in L037 with Python's
[official Decimal reference](https://docs.python.org/3/library/decimal.html).
The two cited primary mathematical sources are reused from the approved
assessment; their statements do not certify these actual theta integrals.
