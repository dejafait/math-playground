# Signed first-zero comparison: working record1728

Approved target: assessment1726, separately approved1727. One research
attempt only. Main gap L030-L032/C032a remains actual-Xi positivity.
The bounded target is a uniform negative upper bound for C032n's
W/f^2 on [1,2], a=1/8, b=1/4, retaining every divisor member and E.
Success pays only the conditional two-point minor; an enclosure
containing zero parks this estimate. Existing work is preserved.

Inputs read: C032j/m/n, C033f, C032y's analytic resolvent interface;
source-working1726 and source-notes1721; stops1711/1725. The corrected
Bellotti--Wong count is required; C032y's older count is not an input.
No new source theorem or numerical zero calculation is proposed.

Initial check: C032n(15)-(17) retain the factor1/2 and the width
normalization. At w=iy, O=iA, dot A=2*pi*p'(y), dot e=e_yy+a_sigma;
the a_sigma terms cancel in the logarithmic ratio. The exact target
is (g/f)'=(g/f)[dot A(b)*cot A(b)-dot A(a)*cot A(a)
-(e_yy(b)-e_yy(a))], once both phases are positive and below pi.

Proposed proof path, not yet established: keep the unique simple real
center r in (14,15) as p0=c exp(-x^2/(4*sigma))*cosh(r*x/(2*sigma));
control the complete remaining centers gamma>20 relative to c using
Gaussian shell bounds. Obtain a signed core logarithmic-ratio margin
from its width score, then bound E_yy(b)-E_yy(a) using a compact/far
split of the defining removable integral. This avoids assuming a
real-center formula for the complex remainder. All quantitative
claims and the final sign remain unfinished at this checkpoint.

Completion: the proposed path succeeded in this first attempt. Full
proof and qualifications are canonical in
[C033g](../lemmas/C033g-signed-first-zero-width-ratio-margin.md).
The rational certificate is scripts/signed_first_zero/margin-1728.json;
23/23 encoded strict comparisons pass. The script does not audit the
analytic proof or the external computations. The claimed bound is
W/f^2<-1/2000 uniformly, with a later critical audit still required.
The initial unfinished reasoning above is preserved as recorded.
