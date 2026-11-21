# Fixed centered bump propagation — working record, step 169

The unchanged invocation-start EXPLORE scope is
`drafts/literature/2026-11-03-spatial-doubling-growth-attempt-scope.md`.
Its exact target is the full fixed-family B_sp(n)=o(n) test at s=65/64.
No new essential theorem or new profile is proposed.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target:
L710's max_(D_*)|E_n|>=exp(-n/10000) along every allowed n. L711
supplies the full unit maximum rate. Together these would give a
positive lower limiting B_sp/n on a fixed angular arc, stopping this
sufficient sublinear-growth mechanism. Complementary Jensen defect,
amplitude/full charge, L657 accounting, H/support and Xi realization
remain independent. The required disk lower bound cannot be inferred
from positivity on the imaginary axis alone.

Read L703's fixed nonnegative plateau bump and parameter selection,
L708's audited width/frequency identity, L710's full signed reduction,
L711's complete contour argument, the parent source comparison and
the interpolation/pole-free-extension stops. Those stops remain;
no source states the complete fixed-family B_sp conclusion. Reuse
Ramachandra Theorem 1.5.2 exactly as previously assessed. L709–L711
remain unaudited; no independent source-proof audit is claimed here.

## Proposed mechanism, not yet a completed proof

Put f(t)=eta(t/delta), delta=2*pi*w, b=sup supp(f), and C=integral f.
Use the ACTUAL support endpoint, which need not equal delta. The
normalized entire transform

    P_n(y)=exp(i*b*y/h)*E_n(y)/C

is bounded by 1 for Im y>=0, because t<=b on the support. At y=i*c,
c>0 fixed, nonnegativity and positive mass arbitrarily near b should
give log(P_n(i*c))/n -> 0 without an assumed nonflat endpoint.

A finite horizontal chain of disks in Im y>0, using only the cited
three-circles theorem at radii r,2r,4r, can transfer this subexponential
lower maximum to a disk inside D_*. The chain length is fixed before
n and may be large. This avoids requiring an explicit lower bound
for the endpoint mass or an effective onset. The coefficient gain in
L710 and unit maximum in L711 then remain to be assembled carefully.

Continuation/abandonment test: prove the disk maximum threshold with
all signs, fixed-parameter quantifiers, zero cases and the full signed
G_n reduction retained. A pointwise noncancellation claim is unnecessary.
If the propagation loses an unavoidable linear rate exceeding 1/10000,
record that precise loss and require a quantitative refinement before
repetition. Do not import an unassessed indicator theorem.

## Completed attempt

[L712](../lemmas/L712-centered-bump-propagation-spatial-growth-stop.md)
contains the full proof and source citation. Normalize at b=sup supp(f),
which can be smaller than delta. The normalized transform is bounded
by one throughout the upper half-plane. Nonnegative mass arbitrarily
close to b gives a subexponential lower value at i/20. A fixed finite
horizontal chain of radius-r disks propagates the lower maximum by
M_j(r)>=M_(j-1)(r)^2. Its fixed factor 2^J only changes the existential
onset; the disk and profile never depend on n. Undoing the endpoint
normalization gives a positive lower exponential rate on the target
disk and therefore pays L710's exp(-n/10000) threshold.

L710's full signed reduction and L711's full unit maximum then give
liminf B_sp/n>=mu(I)/5000>0. This is an informative NEGATIVE result
for the sufficient sublinear-growth mechanism, not a lower bound for
J_sp, an RH result or a certified new theorem beyond the checked
sources. No mathematical script or numerical test is needed for the
exact disk inequalities. L709–L712 remain unaudited; the next proposed
task is a separate critical review, whose source coverage must be
approved independently. Preserve all previous stops and current work.
