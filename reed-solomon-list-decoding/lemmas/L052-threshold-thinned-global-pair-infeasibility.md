# L052 — The threshold-thinned global pair prescription is infeasible

## Hypotheses

Let H be a 1024-set and V its 68-subsets. Define

\[
 M=\binom{1024}{68},\quad L=137^3=2571353,\quad
 v=\binom{963}{7},\quad \rho=L/v,\quad
 \tau=65537^{28}/2^{128},\quad T=\lfloor\tau\rfloor+1,\quad
 \theta=T/(M\rho),\quad f=\theta\rho=T/M.
\]

These are C001a's ambient threshold and L030's local moments. Put
N_h=binomial(7,h)binomial(956,7-h) and
(d_0,d_1,d_2)=(2442832,125664,2856).
Seek a real symmetric F indexed by V, with singleton vector f*1,
diagonal F_SS=f, all entries nonnegative, and

\[
 \begin{pmatrix}1&f\mathbf1^t\\f\mathbf1&F\end{pmatrix}\succeq0.
\]

For distinct supports S,U with intersection 61+h, h=0,1,2, require
F_SU=theta^2*rho*d_h/N_h. Require zero for intersections 64–67.
Nonnegative entries at intersections 0–60 are free. Singular PSD is
allowed. No higher moments, representing measure or labeled RS
determinant restrictions are imposed.

## Conclusion

No such F exists. This rules out only the specified independently
thinned pair prescription at the smallest integer above the true list
threshold. It does not bound other assignments or arbitrary-center
RS lists, construct a packing, or improve the bracket 955–957.
The separate critical review below retains this fixed-prescription exclusion.

## Proof

**Assessed input and applicability.** The pre-invocation SPECIALIZE
assessment is
[the threshold-thinning comparison](../drafts/literature/2026-10-11-thinned-global-pair-threshold.md).
It matches this exact target and covers the changed diagonal/distinct-pair
scaling. L030 supplies the complete local pair counts; C001a supplies
tau. Independent thinning is imported from Last–Penrose, *Lectures on
the Poisson Process*, author version 21 August 2017, Definitions 5.3
and 5.7, equation (5.6) and Proposition 5.4 with its product-integral
proof, pp. 40–43, as recorded in
[foundations/11](../foundations/11-independent-thinning-source.md).
The finite local random subset is a proper simple point process;
independent marks give factor theta on singletons and theta^2 on
distinct pairs. No Poisson hypothesis or global distribution is assumed.
L051's unthinned exclusion is a contrast, not an input to the new proof.
In particular its zero-variance equations are not imposed.

Import the Johnson eigenvalue formula from Brouwer–Cioaba–Ihringer–McGinnis,
arXiv:1709.09011v2, Section 3, printed p. 10, and common orthogonal
decomposition/constant projector from Brouwer–Haemers, *Spectra of
Graphs*, author preprint, Section 11.2, pp. 162–163. Their Theorem
2.7.1(i), p. 36, gives the Schur congruence. Exact sources and
normalizations are in
[foundations/09](../foundations/09-global-pair-johnson-source.md);
L021 uses the same coefficients. Here n=1024>=2w=136, so all
69 eigenspaces occur. These known results are not reproved. Only the
finite prescribed-coordinate certificate is specialized here; this is
REPRODUCTION of assessed methods, without a novelty claim.

**Exact endpoint and reduction.** Integer division gives

```text
T = 2136899816051353757057904852229805411030924365970844208573659527927004771612162841121670742371612
theta = 178074984670946146421492071019150450919243697164237017381138293993917064301013570093472561864301 / 298789536848979652293603811564741264483828081833628868220776051025221452892835192867139735853020
```

Thus T-1<=tau<T and 0<theta<1, verified with exact integer products.
T is an expected singleton mass in this relaxation, not a deterministic
family size or a claimed RS list. All fixed entries depend only on
intersection, so averaging a hypothetical augmented matrix over all
permutations of H preserves every hypothesis and PSD. The constant
index is fixed by these permutations. No actual-label RS condition
is averaged.

Let A_i be the distance-i Johnson relation matrix, i.e. intersection
68-i. Write the averaged F=f*sum_i b_i A_i, and put
v_i=binomial(68,i)binomial(956,i), a_i=v_i*b_i. Then

\[
 a_0=1,\quad a_1=\cdots=a_4=0,\qquad
 a_i=\theta v_i d_{7-i}/N_{7-i}\quad(i=5,6,7).
 \tag{1}
\]

For i=8,...,68 the a_i are nonnegative free coordinates. With
out-of-range binomials interpreted as zero, define

\[
 q_{ji}=\frac{\sum_{h=0}^i(-1)^h\binom jh
                    \binom{68-j}{i-h}\binom{956-j}{i-h}}{v_i},
 \qquad s_j=\sum_{i=0}^{68}q_{ji}a_i.
 \tag{2}
\]

The imported theorem makes f*s_j the eigenvalue of F on eigenspace j.
The Schur congruence reduces the augmented matrix to [1] and
F-f^2 J. It uses no inverse of F and retains singular cases.
On j>=1 the Schur eigenvalue is f*s_j; on j=0 it is
f*(s_0-M*f)=f*(s_0-T). Since f>0, feasibility is exactly the
nonnegative coordinate conditions together with
s_j>=0 (j=1,...,68) and s_0>=T. All coordinates are retained in
the calculation; the certificate below happens to give weight zero
to the constant inequality.

**A compact exact dual witness.** Define lambda_j for j=1,...,68 by

\[
 \lambda_{63}=\frac{23191266}{140599441},\quad\lambda_{64}=1,
 \quad\lambda_{61}=\lambda_{65}=\lambda_{66}=\lambda_{67}
 =\lambda_{68}=0.
\]

The remaining 61 coordinates, with indices in
J_*={1,...,60,62}, are the unique rational solution of the 61 equations

\[
 \sum_{j\in J_*}\lambda_j q_{ji}
       =-\frac{23191266}{140599441}q_{63,i}-q_{64,i}
       \quad (i=8,...,68).
 \tag{3}
\]

This is a solver-independent finite specification: use increasing i
for rows and increasing j for columns; in each elimination column
select the first nonzero remaining pivot row, swap, divide by that
pivot, eliminate and back-substitute. All 61 pivots are nonzero.
Independent Gauss–Jordan elimination reconstructs the same vector.
The full rational vector and all pivots are in the certificate files
specified below. Exact arithmetic establishes the following complete
identities and signs:

- lambda_j>0 for j in {1,...,60,62,63,64}; the other five weights vanish.
- sum_(j=1)^68 lambda_j*q_ji=0 for every i=8,...,68.
- For the eight fixed coordinates (1),

```text
B = sum_(j=1)^68 lambda_j sum_(i=0)^7 q_ji*a_i
  = -57539408985872266892783222337453789811454309811752432100691463179882099080025884399735228200167087026797908212329737 / 40154924132166285452144723123784809687482870805462368376994217998236293063208654201524896095640399248629464245009890
```

In particular -1433/1000<B<-1432/1000<0. The exact fraction,
not its decimal approximation, is the load-bearing strict sign.
If a feasible assignment existed, (2), nonnegative lambda and (3)
would imply

\[
 0\le\sum_{j=1}^{68}\lambda_j s_j
   =\sum_{i=0}^7 a_i\sum_{j=1}^{68}\lambda_j q_{ji}=B<0,
\]

a contradiction. This is a direct Farkas certificate in the original
unscaled coordinates. Its constant-constraint weight is zero; no
constant or singular case is dropped from the original feasibility
test. Failed primal candidates and the solver's status play no role
in this implication.

**Complete finite verification and failed discovery retained.** Run
`python3 scripts/finite-support/thinned_global_pair.py`, then
`python3 scripts/finite-support/audit_thinned_global_pair.py`.
The constructor writes
`scripts/finite-support/thinned-global-pair-results.json`, including
all 4761 spectral coefficients, exact parameters, both failed primal
candidates, the full 115-pivot Decimal phase-I trace, exact phase-I
primal/dual data and the direct witness. Discovery used 240-digit
arithmetic; final acceptance uses rational arithmetic only. Two trial
tail weights, 165 and 164, failed nonnegativity; the third bounded
rational reconstruction gives precisely (3). All trial failures are
preserved. The initial primal fails rows 63,64; the final phase-I
primal fails rows 60,62. These are genuine candidate failures,
distinct from verification failures of the successful dual.

The independent audit imports no construction or LP solver. It
reconstructs binomials by integer products and every numerator in (2)
as the coefficient of Z^i in
(1-Z)^j sum_r binomial(68-j,r)binomial(956-j,r)Z^r.
It independently reconstructs (3), checks every pivot and weight,
all 61 free-term cancellations, every fixed parameter, exact rounding,
and B. It also reconstructs every saved primal spectral sum and
preserves the reported failures. Complete evidence is written to
`scripts/finite-support/thinned-global-pair-audit-results.json`.
The full displayed B, theta and witness specification were inspected.
All 5172 checks pass with no verification failure. These were initially
arithmetic evidence, distinct from the later critical review below.

**Separate critical review, 11 October 2026.** The pre-invocation
[SPECIALIZE audit assessment](../drafts/literature/2026-10-11-thinned-pair-critical-audit.md)
covers this exact review. The complete proof, independent reconstruction
code and all load-bearing source specializations were checked. No proof
defect was found. This is a reproduction and validation of the stated
finite exclusion, not a new uniform bound or a novelty claim.

For the normalization, fixing a 61-core inside S intersect U leaves
seven-subsets with intersection h when |S intersect U|=61+h. L030's
ordered-pair count is therefore exactly rho*d_h/N_h; it has no additional
core multiplicity. Thinning gives theta^2 on distinct pairs, while
F_SS=f=theta*rho. Dividing the former by f gives theta*d_h/N_h,
which is (1) after multiplication by the global valency v_i.
Intersections 64 through 67 correspond precisely to i=4 through 1;
the diagonal is i=0 and is not a distinct-pair condition.

A hypothetical feasible F can be averaged by conjugating its augmented
matrix by diag(1,P), for every permutation P induced from H. This preserves
the fixed singleton vector, Boolean diagonal, every prescribed pair entry,
entrywise nonnegativity and PSD. Transitivity on ordered pairs of each
intersection size gives the asserted relation expansion. This only
concerns the unlabeled slice in the hypotheses. No actual-label triple
restriction or global representing measure is transported or assumed.

The imported orthogonal decomposition has multiplicities
binomial(1024,j)-binomial(1024,j-1)>0 for j=0,...,68, with the
out-of-range binomial zero. They sum to M, so no eigenspace is omitted.
The constant projector is J/M and q_0i=1. Applying the source Schur
congruence with leading block [1] leaves F-f^2 J; hence the constant
eigenvalue is f*(s_0-T), while all other eigenvalues are f*s_j.
The lower matrix need not be invertible. Conversely these inequalities
on an invariant matrix imply the augmented PSD condition. Thus the
reduction is exact, including zero eigenvalues, although the contradiction
uses only the nonconstant inequalities. No L051 kernel or zero-variance
equation appears.

The independent Gauss–Jordan reconstruction was rerun in full: all
5172 checks pass, including the 61 nonzero pivots and every reconstructed
weight. An additional solver-free integer audit is reproduced by
`python3 scripts/finite-support/critical_audit_thinned_pair.py` after that
reconstruction. Its complete certificate is
`scripts/finite-support/thinned-pair-critical-audit-results.json`.
It passes all 7326 checks with no failure. The audit checks all 4761
spectral coefficients and all 2415 upper-triangular trace-orthogonality
identities, using the imported eigenspace multiplicities. These checks
corroborate the source normalization; they do not replace the spectral
theorem or the averaging proof.

Specifically, let D be the least common multiple of every saved weight
denominator, including the zero constant weight, and c_j=D*lambda_j.
The additional certificate records every integer c_j and verifies its
exact equality with the reconstructed rational weight and nonnegativity.
For each i=0,...,68 it independently computes the integer
R_i=sum_(j=1)^68 c_j*p_j(i), where p_j(i)=v_i*q_ji is the numerator
in (2). All 61 integers R_8,...,R_68 vanish. In this notation the
fixed contribution is computed independently as

\[
 B=\frac{R_0}{D}
   +\frac{\theta}{D}\sum_{i=5}^7
               \frac{d_{7-i}R_i}{N_{7-i}}.
\]

It equals the full displayed negative fraction exactly. Thus every
unknown-coordinate coefficient disappears from the weighted inequalities;
the contradiction does not use numerical feasibility, nonzero slack,
strict PSD or a bound on a free variable. All 63 positive nonconstant
weights, five zero nonconstant weights and the zero constant weight
are checked. Both failed primal candidates are independently reconstructed
on all 69 spectral coordinates, retaining failed rows {63,64} initially
and {60,62} finally. Their failure is separate from the successful dual.

The integer endpoint is checked by
(T-1)*2^128<=65537^28<T*2^128, and the full theta is checked in (0,1).
Consequently T is the smallest unsafe integer for the threshold tau,
even though M*f=T is only an expected mass in this relaxation. There is
no assertion that an arbitrary list has these prescribed local pairs.
Other pair assignments and arbitrary-center safety remain unresolved.

**Limits.** This test provides no uniform quantitative bound over
other local pair choices and no global representing measure. Local
thinning remains valid; its global pair extension here is impossible.
Neither safety at 67/68 agreements nor any complete solution is
claimed. The expected-size interpretation and strict integer endpoint
do not assert deterministic cardinality or realization at one center.

## Mathlib

Full matching finite fixed-slice infeasibility and Johnson spectral
theorem: not checked. Supporting Schur, PSD, rational linear algebra,
binomial and finite-probability coverage: not checked. Unknown coverage
is not evidence of absence. The precise primary inputs above, rather
than any claimed Mathlib theorem, support this specialization.
