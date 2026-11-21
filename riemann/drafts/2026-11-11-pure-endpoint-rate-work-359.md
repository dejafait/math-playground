# Fixed theta=1 rate attempt — work saved before completion

Completion note: the reasoning below was preserved before completion.
The completed proof, including all previously pending checks, is now
canonical in C997p (`lemmas/C997p-fixed-endpoint-packet-data-growth.md`).
Its independent conceptual audit remains pending. The final checkpoint
is PROGRESS.md; the provisional statements below are historical notes.

11 November 2026, step359. Work only under the pre-invocation SPECIALIZE
assessment `literature/2026-11-11-pure-endpoint-data-rate-review-357.md`.
This is established-route specialization, not a new central mechanism.

The audited C997o proof gives |s_*|<1/112 and Im(s_*)>0. For
Phi(s)=log(1-64s^2)+beta*(2+s), beta=1/8+i, the proposed exact
saddle has Phi'(s_*)=0. Proposed bounds to finish and check:

- |S-2beta|<9/896+1/195<1/64, hence Re(S)>15/64>13/64.
- On horizontal outer pieces |x|>=1/16 and 0<=y<=1/112,
  |1-64(x+iy)^2|<=44/49. On both vertical endpoints it is
  <=29/196. Their common rate is <=17/64-5/49<13/64.
- On |x|<=1/16, |64(x+iy)^2|<=25/98<1/3; the same elementary
  curvature calculation as C997m gives Re(Phi'')<=-12.
- On the whole deformation, Re(phi')>1/3; the plus branch loses
  the fixed factor exp(-2n*Im(s_*)/3) on the horizontal center.
- At c_*=2+s_*, |q(c_*)-1/2|<1/223. With d=3/8+2i-iq,
  |c_*d(c_*)-2*(3/8+3i/2)|<5/112<1/16, proving the limiting
  minus amplitude is nonzero by its explicit exponential numerator.

Still to finish: justify these rational/branch estimates, write the
complete response identity for the new real weight, retain both
vertical segments, apply complex dominated convergence with the
exact n-dependent amplitudes, normalize by N_n, and compare C997n's
original-TV correction. None is claimed established by this checkpoint.
The independent actual-Xi/forcing/point-bridge gaps stay open.
