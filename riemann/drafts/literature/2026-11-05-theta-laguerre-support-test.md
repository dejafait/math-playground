# Theta/Laguerre normalization and two-scale interlacing test

TARGET: Verify the normalized theta/Laguerre averaging identity and test common interlacing of its degree-two reference polynomials at u=1 and u=4, retaining the full theta support.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step499's completed theta-laguerre-mixture-interlacing comparison checked exact mixture/interlacing phrases and relevant local failures; its source notes and query record are reused. No duplicate exact two-scale specialization was located; no novelty claim.
SOURCE_EVIDENCE: NIST DLMF1.2.8 https://dlmf.nist.gov/18.5.E12 ; https://dlmf.nist.gov/13.2.E2 ; https://dlmf.nist.gov/5.5.E5 ; https://dlmf.nist.gov/18.3.T1 ; https://dlmf.nist.gov/18.2#vi ; MSS Annals182 (2015), Definition3.1 pp.331–332/Lemma3.5 p.333, https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_Srivastava_IFII.pdf ; statements and parameter restrictions directly rechecked in step500; earlier proof-case coverage reused.
COMPARISON: Known finite polynomial formulas and common-interlacing criterion cover the method. The local factorial/scale convention and support specialization remain to be checked. This differs from C792a's universal residual operator and L794's nonlinear pointwise kernel.
GAP: Establish the exact averaging normalization and test whether two reference root intervals share an interlacer; no conclusion about failure of the actual weighted average is licensed.
REASON: One bounded symbolic applicability test can accept or stop the full-support sufficient fallback before attempting any theta-specific coupling; no new general theorem is needed or sought.
SCOPE: Source coverage for the exact saved calculation, directly repaired and reviewed in literature-only step500; no mathematics was derived in steps499–500. No degree sweep, root numerics or actual-Xi sign computation is covered.

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is the normalization plus a necessary finite test of the full-support
common-interlacing premise. Its downstream use is to decide whether
that known averaging criterion is available, without confusing input
real-rootedness with real-rootedness of an average.

Use m_j=M_(2j), the kernel K from L019, and the finite positive moments
from L021. L018/L776 fix the completion and scaling context. Define

    P_d(x)=sum_(j=0)^d (-1)^j binom(d,j)
           [j! m_j/((2j)! m_0)] x^j.

The proposed reference to verify is

    F_(d,u)(x)=[d!/(1/2)_d] L_d^(-1/2)(u^2 x/4),
    P_d(x) ?= (1/m_0) integral_0^infinity F_(d,u)(x) K(u) du.

The question mark is intentional. Check the scale, finite coefficients
and absolute integrability at each fixed degree, including m_0 and
constant term. This is a local application of cited formulas, not a
reproof of Laguerre orthogonality or a new averaging theorem. The
source's alpha>-1 and b not a nonpositive integer conditions must be
checked. Any use of Gamma duplication must retain its pole exclusions.

Then work only with F_(2,1) and F_(2,4). Obtain exact roots or equivalent
exact isolating inequalities and apply the common-interlacer definition.
Check the same degree and common leading-sign convention. Justify that
both scale values lie in the support relevant to K(u)du; no atom at
those values is assumed. If using this as an almost-everywhere test,
give a robust neighborhood argument rather than changing the measure
at two null points. Do not discard the remaining unbounded support.

Decisive evidence is either an exact common-interlacer interval for
this pair or rigorously incompatible root intervals. The latter stops
only the full-support common-interlacing fallback. A passing pair is
only a necessary check and cannot certify all support scales. A
normalization failure is a failure of this representation, not a sign
result. No degree sweep or floating root plot is needed.

The actual fixed-weight polynomial may remain real-rooted even if this
sufficient premise fails. Independent rank-one or strongly Rayleigh
realizations have not been constructed; the proposed calculation does
not test their existence. Actual-weighted compensation, degree-uniform
estimates and all-degree signs remain unresolved. L794 is contrast
only, not a positivity input. No cross-notebook result is used.
Full matching Mathlib coverage remains unchecked.

## Direct-source recovery review — 5 November 2026, step500

This repairs the missing direct URL in the ready assessment, without
changing TARGET or deriving the specialization. The prior comparison's
searches, overlap checks and inspected proof cases are reused. No new
search for the same mathematical statement was needed.

Directly reopened NIST DLMF version1.2.8 (release 15 September 2026):
[18.5.12](https://dlmf.nist.gov/18.5.E12) supplies the finite expansion
and hypergeometric prefactor; [13.2.2](https://dlmf.nist.gov/13.2.E2)
supplies the series coefficients and excludes nonpositive-integer b.
The intended b=1/2 is permitted.
[5.5.5](https://dlmf.nist.gov/5.5.E5) excludes nonpositive-integer 2z;
any later coefficient use must check this.
[Table18.3.1](https://dlmf.nist.gov/18.3.T1) requires alpha>-1 for
Laguerre orthogonality, satisfied by alpha=-1/2.
[18.2(vi)](https://dlmf.nist.gov/18.2#vi) locates simple orthogonal
polynomial zeros in their orthogonality interval. These sources do not
assert real-rootedness of a theta-weighted average.

Directly reopened the published
[MSS paper](https://www.cs.yale.edu/homes/spielman/PAPERS/Marcus_Spielman_Srivastava_IFII.pdf),
Definition3.1 (pp.331–332) and Lemma3.5 (p.333). The definition uses
weak alternation of ordered real roots. The lemma equates common
interlacing with real-rootedness of every convex combination for a
finite collection of equal-degree polynomials with positive leading
coefficients. This licenses the finite-pair applicability test only;
it supplies no automatic theorem for the continuous theta law. The
previous review's determinant/conditioning proof-case assessment is
reused; those proofs need not be reopened for this finite test.

Decision remains SPECIALIZE. The identity, scale factors, moment
integrability, support and robust neighborhood argument are deliberately
left to the saved research target. No new lemma, calculation, theorem
import into the assembly, or change of route has occurred. Full matching
Mathlib coverage remains unchecked. Recovery is procedural, not a
mathematical advance; the next action defaults to the same calculation.
