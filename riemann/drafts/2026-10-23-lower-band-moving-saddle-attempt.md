# Lower-band moving-saddle attempt — 2026-10-23

The approved target is the exact TARGET in
[the saved assessment](literature/2026-10-23-lower-band-moving-saddle-coverage.md).
This is one RESEARCH / REPRODUCTION proof attempt under the pinned
external premise, not a new source review. Existing unfinished work is
preserved. The main gap is initial low-index signs and global mixed
positivity. A uniform arithmetic margin could support a separately
assessed lower-band theta reduction; no such reduction is assumed.

Inputs inspected: L303/L330's inversion and retained phase, L331's
local saddle criterion and old shrinking-domain obstruction, L452's
analytic mechanism, L454's inversion/pole bookkeeping, and L456's
full fixed-disk logarithm bound and fixed-circle failure. The October
source register and overlap assessment were read. The existing
fixed-circle, L323/L327, and fixed-r stops retain their scopes.

Unfinished reasoning saved before the full contour comparison:
write x0=(m+1)/(2r), d=1/4096 and use the entire radius-273/256
logarithm disk about 2+ia from L456. A fixed disk about x0 appears
to leave room for all Cauchy derivatives. For
H(z)=2rz-(m+1)Log z+log zeta(1/2+z+ia)+log zeta(1/2+z-ia),
the log perturbation and each fixed-order derivative should be
O(r^(2/3)); the bare curvature is comparable to r. This suggests
a real saddle x*=x0+O(r^(-1/3)) with curvature comparable to r.
The proposed positive normalization is A exp(H(x*))/sqrt(2*pi*H''(x*)).
The factorial must be retained to show its logarithm is o(r).

The test is incomplete until the vertical local Taylor error, the
annulus out to a fixed d, the entire remaining vertical line, both
shift connectors and the two original residues are bounded relative
to that same normalization. A fixed-width middle cutoff may permit
exp(-k r+O(r^(2/3))) decay; the shrinking-window annulus instead
needs cancellation of the real linear variation in the paired log.
Continue only if all these errors are little-o of a positive
exp(-o(r)) scale. Otherwise record the exact failed threshold and
park this implementation. No local computation here is an established
full asymptotic or a changed sign range.

Completed outcome: [L457](../lemmas/L457-lower-band-uniform-moving-saddle-margin.md)
contains the full conditional proof. The fixed analytic disk supports
the displaced saddle and all required derivatives. Quadratic real-part
control handles the shrinking annulus; a fixed-window exponential
kernel tail handles the middle range. The entire far range, including
zero shifted heights, and both original residues are negligible relative
to the same positive factorial-normalized scale. The resulting uniform
margin is exp(-C r^(2/3)). This is local known-method reproduction,
pending a separate critical audit of the result and its inherited L456
disk input. No new mathematical script was needed; the proof's exact
disk inclusions, normalization and full integral inequalities are the
evidence, rather than a numerical saddle preview. The changed-band
theta reduction and all independent main gaps remain unresolved.
