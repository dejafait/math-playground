# Lemma 489: finite collision at a positive all-real transition

## Hypotheses

Let F(lambda,z) be the exact theta heat family of L058, with the Xi and
kernel conventions of L018/L019. Use L488's common real/simple tail and
strip theorem with its cited-source qualifications. The underlying
asymptotic and strip proofs remain unaudited; L488's local replay passed
its separate independent audit on 2026-10-30.

Suppose 0<lambda_*<1/8 and:

1. There exists epsilon>0 such that every zero of F(lambda,.) is real
   whenever lambda_*<lambda<=lambda_*+epsilon.
2. There is a sequence of real numbers lambda_j<lambda_* increasing to
   lambda_* such that F(lambda_j,.) has a nonreal zero for every j.

Neither endpoint reality nor simplicity is assumed. Fix any
0<a<lambda_*<b<=1/8, and use L488's common threshold

    R(a) = (1/2) exp(C_*/(4a)),

where C_*>0 is the existential absolute constant in that lemma.

## Conclusion

Every zero of F(lambda_*,.) is real. There is a real x_* with

    |x_*|<R(a),
    F(lambda_*,x_*)=0,
    F_z(lambda_*,x_*)=0,

whose exact multiplicity is a finite integer m>=2. In particular this
zero lies strictly between the vertical edges of L488's common closed
rectangle |Re z|<=R(a), |Im z|<=1/2.

This is a standard compactness specialization of the cited inputs,
not a collision-exclusion theorem or progress beyond known tools.
It proves an implication under the stated transition hypotheses; it
does not establish that such a transition or multiple zero exists.

## Proof

### Named inputs and why a local specialization is needed

L058 supplies joint entirety of F, conjugation for real lambda, and
F(lambda,0)>0 for every real lambda. Thus no real-parameter slice is
identically zero. The isolated-zero theorem implies that each of its
zeros has finite positive multiplicity and is isolated. Joint
continuity implies convergence uniform on any fixed compact z-set as
the parameter tends to a fixed real value.

L488 specializes D. H. J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the de
Bruijn–Newman constant*, Research in the Mathematical Sciences **6**
(2019), article 31, [arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
Theorem 1.5(i)–(ii), pp.9–10. Its strip input is N. C. de Bruijn,
*The roots of trigonometric integrals*, Duke Math. J. **17** (1950),
197–226, Theorem 13, in the form of Polymath Theorem 3.2. The exact
normalization is F(lambda,z)=8 H_(4lambda)(2z), as checked in L488.
Hence, for every lambda in the single fixed interval [a,b], every
nonreal zero satisfies |Re z|<R(a), |Im z|<=1/2, and every zero with
|Re z|>=R(a), including equality, is real and simple.

The same Polymath paper, Section 3, Proposition 3.1(i)–(ii), gives
simple-zero continuation and local splitting at every finite repeated
order. Those results are supporting comparisons, not additional inputs
to the proof below. Only the standard named Rouché theorem, the
isolated-zero theorem, compactness and conjugation are needed after
L058/L488. We give the short applicability argument because endpoint
reality, capture of arbitrary incoming zeros, and the strict spatial
threshold are precisely the local obligations. No source asymptotic
or multiple-zero splitting theorem is reproved.

### Endpoint reality from the right

Put delta=min(epsilon/2,(b-lambda_*)/2)>0. The times
lambda_*<lambda<=lambda_*+delta lie in [a,b] and satisfy hypothesis 1.
Suppose w is a nonreal zero of f(z)=F(lambda_*,z). By nonzero entirety
and isolation, choose r>0 with r<|Im w|/2 such that the closed disk
|z-w|<=r has w as its only zero of f and no zero on its boundary.
Let m_w>=1 be its finite multiplicity. The disk is disjoint from the
real axis, and

    eta = min_{|z-w|=r} |f(z)| > 0.

Joint continuity, uniformly on this fixed circle, gives rho>0 such
that for real |lambda-lambda_*|<rho,

    sup_{|z-w|=r} |F(lambda,z)-f(z)| < eta.

Choose lambda with lambda_*<lambda<lambda_*+min(delta,rho). Rouché's
theorem gives exactly m_w zeros of F(lambda,.) inside the disk,
counted with multiplicity. All are nonreal, contrary to hypothesis 1.
Thus every endpoint zero is real. This argument is applied to any
putative nonreal endpoint zero; it assumes no global enumeration and
requires no uniform disk over the entire zero set.

### Compact capture of incoming nonreal zeros

Since lambda_j tends to lambda_* and a<lambda_*<b, all sufficiently
large indices have lambda_j in [a,b]. For each such j choose any
nonreal zero z_j of F(lambda_j,.). L488 puts every possible choice in
the same closed compact rectangle

    Q = {z in C: |Re z|<=R(a), |Im z|<=1/2}.

Although each chosen zero has |Re z_j|<R(a), we take the closure here
and do not assume that strictness survives passage to the limit.
Compactness gives a subsequence z_(j_k) tending to z_* in Q.
Joint continuity gives

    F(lambda_*,z_*) = lim_k F(lambda_(j_k),z_(j_k)) = 0.

By endpoint reality z_*=x_* is real. Since the endpoint slice is
not identically zero, x_* has finite positive multiplicity m.

### A simple limit is impossible

Suppose m=1. Choose r>0 such that the closed disk |z-x_*|<=r contains
only the zero x_* of f and its boundary is zero-free. Its center is
real, so the disk is invariant under conjugation. As in the first
Rouché comparison, the positive boundary minimum and compact
continuity give rho>0 for which F(lambda,.) has exactly one zero in
this disk, counted with multiplicity, for real
|lambda-lambda_*|<rho.

For sufficiently large k, both |lambda_(j_k)-lambda_*|<rho and
|z_(j_k)-x_*|<r. Thus the nonreal zero z_(j_k) lies in the disk.
Its distinct conjugate also lies in the disk and is also a zero,
because lambda_(j_k) is real and L058 gives conjugation. Each has
multiplicity at least one, contradicting the count of exactly one.
Consequently m>=2, equivalently F_z(lambda_*,x_*)=0.

We already know |x_*|<=R(a). If equality held, L488 applied at
lambda_* in [a,b] would make this zero simple. Thus |x_*|<R(a),
as claimed. The argument applies to arbitrary choices of the incoming
nonreal zeros; none can evade the fixed rectangle or converge to a
simple endpoint zero. A global labeling of zeros is unnecessary. ∎

### Qualifications and verification

The two transition hypotheses are unproved for any proposed positive
transition of the actual family in this lemma. L488's source imports
and limited audit scope are retained. The compactness
argument passed its separate critical audit on 2026-10-30, conditional
on those qualified inputs, with no proof correction required. There is no
assumption of boundary nonvanishing for the rectangle: its boundary
may contain other zeros, and Rouché is used only on isolated local
circles. No infinite supremum, zero-motion sum, inverse-gap bound,
all-time labeling or interchange of infinite limits is used.

Verification is the analytic count above; no numerical certificate or
mathematical script is relevant. The counts are m_w>=1 at a hypothetical
nonreal endpoint and exactly 1 versus at least 2 at a hypothetical
simple limit. The spatial conclusion is strict because L488 covers
threshold equality. Exact multiplicity two, a numerical R(a), collision
exclusion at positive time, uniformity as a decreases to zero, and
actual-Xi all-degree signs remain unproved. In particular this result
does not prove RH or produce a counterexample to it.

### Separate critical audit — 2026-10-30

The audit checks the implication as stated, accepting L058 and qualified
L488 rather than re-auditing the latter's asymptotic replay. Both
transition assumptions are essential to this proof and remain assumptions.

For the first count, the endpoint slice is nonzero because its value at
zero is positive. Isolation permits a closed disk with precisely the
one proposed endpoint zero, counted with its finite multiplicity m_w,
and radius below |Im w|/2. On its compact boundary the minimum eta is
positive. Joint continuity on a small closed parameter interval times
this circle is uniform, giving the displayed strict comparison for
all sufficiently close real parameters. The right interval contains
such a parameter, since both delta and rho are positive. Rouché then
gives m_w>=1 nonreal zeros, contradicting the all-real assumption.
This verifies endpoint reality without assuming it.

For compact capture, discard only finitely many j to put lambda_j in
[a,b]. L488 controls every nonreal zero at each remaining time with the
same R(a), regardless of which zero is chosen. The closed rectangle Q
is compact; no condition on its boundary zero set is needed. A convergent
subsequence of the selected zeros, together with lambda_j tending to
lambda_*, converges in the product space. Joint continuity therefore
gives an endpoint zero. Endpoint reality makes its coordinate real;
the nonzero entire endpoint slice makes its multiplicity finite.

For the second count, a hypothetical simple endpoint zero has an
isolating circle centered on the real axis. Its positive boundary
minimum and the same uniform-continuity argument give count exactly
one with multiplicity for all sufficiently close real times. Along
the selected subsequence both the time and zero eventually enter the
required neighborhoods. Conjugation places the distinct conjugate zero
in that same open disk, so the count is at least two, a contradiction.
This rules out simplicity without any global labeling or zero-gap bound.

Finally compactness gives only |x_*|<=R(a). Applying L488 at the
endpoint time itself rules out equality because its real/simple tail
includes |Re z|=R(a). Thus the strict cutoff follows after multiplicity
at least two is established; strictness was not passed through a limit.
The audit passes with no missing local hypothesis or correction found.
It does not certify L488's separate replay, prove either transition
assumption, exclude finite collisions, or control a decreasing to zero.

## Mathlib

Full matching coverage has not been checked; absence is not asserted.
Rouché's theorem, isolated zeros and compactness are the supporting
standard results. No specific Mathlib declaration is claimed to
formalize the complete transition implication or L488's source input.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
