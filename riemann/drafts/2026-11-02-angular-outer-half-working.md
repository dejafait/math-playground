# Outer-half inner input — bounded working record

Prepared STEP_ID: 2026-11-02-angular-outer-half-01.
The unchanged invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md`.
This is one mathematical attempt on its exact angular operator target.

Main gap: actual-Xi all-degree mixed positivity and signs at unbounded
height. Intermediate test: the full angular L2 response of the unit
Hardy input formed from grid indices ceil(n/2)<=j<n, against the
uniform c exp(-n/32) threshold. A successful test would supply a
synthetic detector input; layer isolation, other poles, census and
clearance, simultaneous realization, an independent upper bound and
actual-Xi signs remain unresolved.

Retain n>=5, x=-5/4, R=11/8, U=R^2, eta=1/100, t_j=j/n,
common distinct poles Re(a)=x, |a|<=R-eta, x in Z, positive integer
original simple-pole residues and M<=n/3. Put u=i exp(i theta),
K=ceil(n/2), B_low=product_(0<=j<K) b_j and
B_out=product_(K<=j<n) b_j, where
b_j(v)=R*(v-t_j*u)/(U-t_j*conjugate(u)*v).
The nominated input is f_u(zeta)=B_out(R*zeta).

Inspected C645g's normalization, C645n's complete finite analytic-input
projection and full-cancellation stop, C645o's exact weights and signed
Gram, and the related angular working/failure records. C645l's
Chebyshev contour formulas are a possible counterfamily tool, not an
assumption of an angular estimate. No duplicate outer-half test was
found in these scoped paths. The ready primary Fourier/residue
assessment is reused; no new source review is needed.

The projection specialization gives the exact response

    H_q_u f_u = (B_out(x)/R) * sum_a r_a
                  [B_low(x)/B_low(a)]/(zeta-a/R).

All factors are analytic near the closed spatial disk, and f_u has
unit boundary modulus. This identity alone supplies no lower bound:
the low-grid weighted residues remain complex and correlated.
Full cancellation's exponent and entrywise Gram positivity cannot
be substituted. Evaluation at angular zero also crosses common
interior poles, as the preserved C645p stop warns.

Continuation/abandonment test: establish a uniform full-response lower
bound, or an admissible sequence with its whole angular response
o(exp(-n/32)). A finite screen is diagnostic only. If neither follows,
save the exact unresolved inequality and any quantitatively justified
refinement; do not claim that failure of this input refutes the operator.
No new theorem or numerical bound has yet been established.

## Saved refinement before exact verification

The diagnostic `scripts/one-sided-hankel/angular-outer-half-diagnostic.json`
is explicitly uncertified. It suggests a countersequence for the input
using odd m, n=3m, unit Chebyshev residues and radius r=27/50.
This remains within the approved family. The proposed proof must bound
the whole spatial boundary uniformly in u, not just sampled coefficients.

Use the left arc |v|=sqrt(d^2+r^2)>34/25 and an ellipse centered at
x with horizontal width 13/200 and vertical width sqrt(r^2+(13/200)^2).
On the arc, every low-grid factor has modulus >=1892/1937, while
C645n gives |B_full(x)|<=exp(-lambda*n), lambda>47/1000.
The resulting candidate arc exponent is
47/1000-45/3784 > 7/200 > 1/32. This arithmetic still needs checking.

For the ellipse, pair a low factor at t with an outer factor at t+1/2.
The desired elementary bound is
|b_t(x)*b_(t+1/2)(x)/b_t(v)|<=21/20 for 0<=t<=1/2,
|u|=1, Re(v)<=-237/200 and |v|<R. A half-plane level-circle
calculation reduces this to rational inequalities in t and Re(u).
Certify those over the entire rectangle, then charge the actual
outer-grid shift error 1/(2n). The exact C645l finite-node identity
would give a quadrature exponent exceeding the arc exponent.
This is the single current bounded test; no estimate is yet accepted.

## Completed bounded attempt

The full proof is canonical in
[C645t](../lemmas/C645t-outer-half-inner-input-chebyshev-response-stop.md).
For odd m>=5, n=3m and r=27/50 it proves that the entire nominated
output is <=22000*m*exp(-7*n/200), uniformly in both angles.
Since 7/200-1/32=3/800, this is an admissible response countersequence.
It does not bound the largest operator norm from above. Outcome:
NEGATIVE for this specific partial-cancellation input; the full
angular detector and all actual-Xi bridges remain unresolved.

The final exact certificate covers the full (t,Re(u)) rectangle with
6322 dyadic boxes, maximum depth 16, and passes all 16 checks. The
complete selected minimum-bound, geometry/rate, check and empty-failure
fields were inspected. The first pass failed only the auxiliary claim
that the quadrature denominator exponent exceeds 1 already at n=9.
That first certificate is preserved; the theorem starts at n=15.
No diagnostic sample or tail truncation enters the proof.

The new DAG row lists C645g (normalization), C645l (the contour and
finite-node identity) and C645n (analytic-input projection and anchor
product rate). C645o/C645p/C645s are contrasts, not inputs. There is
no claimed independent audit or certified originality. A separate
conceptual audit is nominated to test the half-plane implication,
complete interval coverage, contour endpoints, actual odd-grid shift
and finite-node normalization. Its ready source reuse receives a
separate approval next turn; this attempt does not approve its proof.
