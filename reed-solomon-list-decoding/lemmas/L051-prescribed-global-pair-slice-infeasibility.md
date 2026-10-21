# L051 — The prescribed global pair slice is infeasible

## Hypotheses

Let H be a set of 1024 points and V its 68-subsets. Set

\[
 L=137^3=2571353,\quad v=\binom{963}{7},\quad \rho=L/v,
 \quad N_h=\binom7h\binom{956}{7-h},\quad
 (d_0,d_1,d_2)=(2442832,125664,2856).
\]

These are exactly L030's prescribed local first and second moments.
Seek a real symmetric matrix F indexed by V, with f_S=rho,
F_SS=rho, all pair entries nonnegative, and

\[
 R=\begin{pmatrix}1&f^t\\f&F\end{pmatrix}\succeq0.
\]

For distinct S,T with intersection 61+h, h=0,1,2, require
F_ST=rho*d_h/N_h. For distinct S,T with intersection at least 64
require F_ST=0.
For intersections 0–60 leave the nonnegative entries free.
No global representing measure, labeled triple constraints or higher
moments are assumed. Singular PSD matrices are allowed.

## Conclusion

No such F exists. In particular, L030's fixed local moments cannot be
restrictions of this global augmented pair matrix. This excludes only
the prescribed slice; it does not bound arbitrary RS lists or exclude
other local moment assignments. The bracket 955–957 is unchanged.

## Proof

**Known inputs and specialization.** The prior SPECIALIZE assessment is
[the global pair comparison](../drafts/literature/2026-10-07-global-pair-marginal-extension.md).
The Johnson eigenvalue formula, simultaneous orthogonal decomposition,
permutation averaging and Schur congruence are imported from the exact
primary passages in [foundations/09](../foundations/09-global-pair-johnson-source.md):
Brouwer–Cioaba–Ihringer–McGinnis, arXiv:1709.09011v2, Section 3,
printed p. 10; Brouwer–Haemers, author-hosted *Spectra of Graphs*
preprint, Section 11.2, pp. 162–163 and Theorem 2.7.1(i), p. 36;
and Polak, arXiv:1703.05171v1, Section 1.2, p. 3.
Here n=1024>=2w=136. Relation distance i means intersection 68-i;
it is not the moment order or the RS dimension. L021 uses precisely
the same eigenvalue normalization. These standard theorems are not
reproved. The finite zero-variance consequence and arithmetic below
are the needed specialization; no inspected source already gives this
fixed-slice exclusion. This is REPRODUCTION of assessed methods for
one specified assignment, with no originality claim.

**Averaging and the covariance kernel.** If F exists, average it over
all permutations of H. Every prescribed entry, nonnegativity, diagonal
and singleton coordinate is invariant under this action, and convexity
preserves R PSD. Thus it suffices to consider invariant F. This averaging
uses only the unlabeled pair slice, not actual RS determinant constraints.
Write F_ST=rho*b_i when the relation distance is i, including b_0=1.
Then

\[
 b_1=\cdots=b_4=0,\qquad
 b_5=d_2/N_2,\quad b_6=d_1/N_1,\quad b_7=d_0/N_0.
 \tag{1}
\]

The Schur congruence with leading block [1] gives
K=F-rho^2 J PSD. There is no inversion of F and no exclusion of
zero eigenvalues. For any 61-subset C of H let u_C indicate all
S containing C. There are v such S. For each of them, removing C
leaves a seven-subset in a 963-set. Its numbers of partners at residual
intersection h are exactly N_h. The prescribed local row sum is

\[
 (Fu_C)_S=\rho(1+d_0+d_1+d_2)=\rho L
 \quad(S\supseteq C).
\]

L030's computation gives 1+d_0+d_1+d_2=L and v*rho=L. Hence

\[
 u_C^tKu_C=v\rho L-\rho^2v^2=0.
 \tag{2}
\]

For a real symmetric PSD K, (2) implies Ku_C=0: for each real vector
z, the nonnegative quadratic (u_C+t z)^tK(u_C+t z) has zero constant
term, so its linear coefficient 2z^tKu_C must vanish. This retains
singular matrices and uses no representing distribution. Therefore
for every S, including those not containing C,

\[
 (Fu_C)_S=\rho^2v=\rho L.
 \tag{3}
\]

**Unique triangular reconstruction.** Put r=|S intersect C|=61-t.
Every t=0,...,61 is possible: choose r points inside S and 61-r
outside S. A support T containing C has seven additional points.
To have relation distance i from S, choose 68-i-r of these points
from S minus C and i+r-61 from outside S union C. Consequently
the number is

\[
 c_{t,i}=\binom{7+t}{t+7-i}\binom{956-t}{i-t},
 \quad t\le i\le t+7.
\]

Dividing (3) by positive rho gives the forced equations

\[
 \sum_{i=t}^{t+7}c_{t,i}b_i=L\quad(0\le t\le61).
 \tag{4}
\]

The t=0 equation is already the local row identity. For t=1,...,61
its last coefficient is binomial(956-t,7)>0. Starting with (1), the
following rational recursion uniquely determines every remaining entry:

\[
 b_{t+7}=\frac{L-\sum_{i=t}^{t+6}c_{t,i}b_i}
                  {\binom{956-t}{7}}.
 \tag{5}
\]

Thus (5) is necessary for any invariant feasible matrix, not merely a
chosen candidate. The averaging step shows that excluding this vector
also excludes every noninvariant matrix in the original slice.

**Exact spectral obstruction.** Let
v_i=binomial(68,i)binomial(956,i), a_i=v_i*b_i, and use the imported
Johnson coefficients, with out-of-range binomials zero,

\[
 q_{ji}=\frac{\sum_{h=0}^i(-1)^h\binom jh
               \binom{68-j}{i-h}\binom{956-j}{i-h}}{v_i},
 \qquad s_j=\sum_{i=0}^{68}q_{ji}a_i.
 \tag{6}
\]

The eigenvalue of F on Johnson eigenspace j is rho*s_j. Each
eigenspace j=0,...,68 is nonzero under n>=2w. On nonconstant
eigenspaces j>=1, J is zero, so K has the same eigenvalue. For j=0,
K has eigenvalue rho*(s_0-|V|rho). PSD requires all these quantities
to be nonnegative. Direct exact evaluation of (5)–(6) gives

\[
 s_{63}=-\frac{4972581118802}{268545631575}<0,\qquad
 s_{64}=-\frac{4715156067501}{3197483319953}<0.
 \tag{7}
\]

Either contradicts PSD. Both denominators and rho are positive.
For completeness, all b_i are nonnegative, s_1,...,s_61 are zero,
and s_0-|V|rho=0. The remaining spectral sums are

| j | s_j |
| --- | --- |
| 62 | 15540082423679/124914617475 |
| 65 | 1297679718979138/713038780349519 |
| 66 | 3043881446887/3298277723049 |
| 67 | 64021336754404/63814503772035 |
| 68 | 56728116432388091/56731093853339115 |

Every eigenspace and the augmented constant coordinate is retained;
the contradiction is not a numerical eigenvalue estimate or a solver
status. The exact slice singleton mass |V|rho is between 1.677 and
1.678 times 65537^28/2^128. This prescribed mass is not a list bound
or an actual packing size, and is not used in the contradiction.

**Full finite evidence and reproducibility.** Run
`python3 scripts/finite-support/global_pair_slice.py` and
`python3 scripts/finite-support/audit_global_pair_slice.py`.
The full rational certificate is
`scripts/finite-support/global-pair-slice-results.json`, under
`exact_obstruction`: all 69 b_i and a_i, every triangular coefficient
and positive pivot, all 62 residuals, all 69 spectral sums and the
constant Schur sum. Its `q_matrix` stores all 4761 coefficients.
The independent audit imports no construction module. It reconstructs
binomials by integer products, counts core extensions by the number
of the seven added points outside S, and recomputes all q coefficients
by polynomial convolution. All 5038 checks pass, including exact
agreement of every saved coefficient, entry and spectral sum,
all fixed entries, all core equations, all pivots and both values (7).
The complete checks are saved in
`scripts/finite-support/global-pair-slice-audit-results.json`.
The selected load-bearing fractions (7) and the five other nonzero
nonconstant sums were also inspected in full.

The output preserves an initial candidate. The complete bounded
unsuccessful 120-basis discovery output is separately retained in
`scripts/finite-support/global-pair-slice-discovery-results.json`;
adding `--discover` to the construction command reproduces that search.
Its candidate/discovery failures are
genuine failed feasibility reconstructions, not the final obstruction's
verification failures. No search exhaustion is used to prove (7).
The zero-variance argument instead proves that the initial candidate
is the only possible invariant assignment, as independently verified
by (5).

**Separate critical proof review, 11 October 2026 (step 162).** The
review retains the proof and its restricted conclusion. It reuses
the pre-invocation SPECIALIZE critical-audit assessment and the primary
inputs cited above. In particular, it imports the Johnson spectral
theorem rather than inferring its normalization from the finite output.
The following checks concern the proof's implications as well as its
arithmetic.

The permutation action fixes the augmented constant index. Congruence
by each permutation preserves PSD, and averaging preserves every
specified pair value because these depend only on intersection size.
The averaged matrix is invariant on every pair orbit, including the
diagonal. No labeled determinant constraint is being averaged. With
f=rho*1, the invertible matrix
T=[[1,-f^t],[0,I]] satisfies T^t R T=diag(1,F-ff^t).
Thus the covariance step is valid even when F or K is singular.
For a fixed C the diagonal contributes rho and the distinct residual
intersection classes h=0,1,2 contribute rho*d_h to each local row;
all other distinct classes contribute zero. This checks the exact
zero in (2), without probabilistic or integrality assumptions. In the
quadratic argument following (2), a nonzero linear term would give a
negative value for one sufficiently small signed t, whatever the
nonnegative quadratic coefficient. Hence all coordinates of Ku_C
really vanish, including those indexed outside the core slice.

For any r=0,...,61, one can choose C using r points of S and 61-r
points of its 956-point complement. The disjoint sets S minus C and
H minus (S union C) have sizes 68-r and 895+r. Choosing respectively
7-l and l new points gives every T containing C exactly once, with
distance 61-r+l, for l=0,...,7. All these choices are possible and no
extra case is omitted. This independently recovers every coefficient
in (4), including both endpoint rows r=61 and r=0. With the eight
fixed b_0,...,b_7, the remaining 61 equations successively introduce
b_8,...,b_68. Their last coefficients are binomial(895+r,7)>0, so
no free parameter survives. Verifying a candidate against all these
equations is therefore a verification of the uniquely forced vector,
not an assumption that the discovery solver found the only candidate.

Finally F=rho*sum_i b_i A_i and the source gives the eigenvalue p_j(i)
of A_i. Since q_ji=p_j(i)/v_i and a_i=v_i*b_i, (6) is exactly the
eigenvalue of F divided by rho; no eigenspace multiplicity belongs in
this sum. All 69 Johnson eigenspaces occur for n=1024>=136. Only the
constant eigenspace sees J, where its eigenvalue is |V|. This verifies
both the sign test at j=63,64 and the distinct constant Schur test.
The diagonal exception is explicitly stated in the hypotheses: zero
pair entries apply only to distinct supports.

The review read both complete arithmetic programs and the constructor's
imported hahn/solve_exact routines, reran the constructor without basis
discovery, and reran the independent audit. All 5038 checks pass with
no failure. These reconstruct all 4761 spectral coefficients, all
69 coordinates and spectral sums, all 62 core equations, all 61
positive pivots, all eight fixed entries and the constant Schur sum.
The two exact fractions in (7) and the zero constant Schur sum were
inspected in full. The independent audit checks the forced equations
using outside-S extension counts and checks the spectrum by polynomial
convolution without importing the construction module. Its complete
saved certificate remains the arithmetic evidence cited above.
The constructor's printed FAILED refers to its infeasible discovery
candidate, whose negative rows are precisely 63 and 64; its obstruction
verification has no failures. This distinction is essential.

The audit makes no new bound or originality claim. It confirms that
every higher-order extension retaining this augmented pair principal
matrix is excluded, while L030's separate local distributions remain
valid. It does not assume every RS list has these singleton or pair
moments, and supplies no conclusion for changed moments, representing
measures, arbitrary-center safety or the finite boundary.

## Mathlib

Full matching global fixed-slice exclusion and Johnson eigenvalue
theorem: not checked. Supporting PSD-kernel, Schur complement,
finite-set and binomial coverage: not checked. Unknown availability
is not evidence of absence. Primary spectral inputs are precisely
cited above; no Mathlib result is claimed to supply this certificate.
