# Rounded endpoint attempt — working checkpoint

Completion note: the attempt is now written in full in
[L453](../lemmas/L453-rounded-endpoint-uniform-laguerre-margin.md).
The original pre-assembly checkpoint below is retained as working history;
the canonical proof, with a separate critical audit still pending, governs
the result. No numerical or formal verification is claimed.

Approved scope: the exact covered target in
[the prior assessment](literature/2026-10-23-rounded-endpoint-height-coverage.md).
This is a mathematical specialization attempt, not new source discovery.

Main gap: global mixed positivity. The intermediate target is one positive
Laguerre coefficient at the rounded logarithmic index at every large height.
Its downstream use is removal of the paired-height restriction; smaller
indices and bounded exterior heights remain separate gaps. Continue only
if the full relative Mellin error tends to zero and the additive sector
error is smaller than a proved reciprocal-series square margin uniformly
over the ceiling position, including jump heights.

Unfinished reasoning saved before full proof assembly:

- Write R=log(a/(2π))/2, n=ceil(R/2), m=2n, and use the exact
  L269 saddle r,h. Then r=R+log(1+h²/a²)/4 and h=9/2+m/(2r).
  Since r≥R and n≤R/2+1, h≤6 for large a and 0<r−R≤9/a².
  Hence −9/a²≤m−r<2. At a=2π exp(4k), n=k and h<5.
- A useful uniform proof domain is r−1≤m≤r+2, with m even.
  Retain W=(jk)^(-1/2)(1−log(jk)/(2r))_+^m. The transformed
  mass majorant is Q(L)≤e exp(−L²/(16r)); this gives total mass
  O(r) and moving cutoff tails O(r exp(−r/64)).
- L299's local derivatives stay bounded on every nonempty patch because
  m/(r−log(jk)/2) stays bounded. L300/L301's infinite summation must
  keep the lower limits: the new index power is j^(-ν),
  ν=h−4=1+(m−r)/(2r), and its head/tail sum is still O(r).
  Polynomial strip curvature retains exp(−r/256). Mixed-sector
  variation can be rechecked on 39/8≤h≤21/4, crossing five.
- Use the exact Mellin kernel Γ(m+1)(2r)^(-m)e^(2rz)z^(-m−1),
  with c=1/2+2/r and σ=1+2/r. Its integral is one. Its peak is
  O(sqrt(r)) since 2rc−m is bounded, rather than silently replacing
  m by r. Gaussian localization and L452 (1) should give relative
  O(r^(-1/6)); the reciprocal-series square is ≥(1+r/2)^(-2).

These observations are not yet a signed whole-plane theorem. Full
boundary terms, exact normalization, all errors and the common onset
are being checked in the canonical proof. No mathematical script is
needed. Reused failures are absolute coefficient freezing, automatic
positive Mellin averaging, and fixed-r arbitrary-phase positivity;
none supplies the coupled-height estimate. The pinned external theorem
and its unaudited manuscript/import closure remain qualifications.
