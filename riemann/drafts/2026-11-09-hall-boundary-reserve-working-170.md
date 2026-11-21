# Step170 working record: conserved boundary reserve

The approved target is the exact TARGET in
`literature/2026-11-09-hall-monotone-tail-boundary-reserve-test.md`.
This is one research specialization, not another source approval.
The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
No new lobe integration, mesh change or parameter sweep is permitted.

Source reuse: Csordas v2 Theorems3.5/4.5 and (4.2), with L019's
normalization, give rho(q)=128 J_1(q/4), decreasing for q>0.
L898 supplies full-law domination. L905 fixes every lobe and the fourteen
proper cuts; L912 supplies the raw full-cut margin under L037. The
previous equal-share and whole-box stops remain unchanged.

Unfinished reasoning saved before the analytic calculation:
- Translation q -> q-pi/16 sends each positive-side exterior negative
  lobe to its inward positive neighbor, preserves absolute cosine, and
  increases rho. Reflect to obtain the other side. This should pay all
  exterior demands, charging only d_2 to r_2 and d_-3 to r_-2 at the core.
- Raw boundary expenditure is C=A0(d_2+d_-3), with d_-3=d_2. Reduced
  core resources must subtract these exact charges, never reserve them
  on top of the existing finite margins. Every crossing cut needs proof.
- One full-series analytic envelope will be tested: retain exact pi in
  the leading exponential, sum the positive n>=2 majorants geometrically,
  split the transverse integral at t=q/2, and integrate a Gaussian bound
  on the inner piece and an exponential tangent bound on the outer piece.
  This includes every theta index and the complete transverse tail.
  It is an analytic upper bound, not numerical lobe quadrature.
- Required threshold: C<15/10^6, then all reduced cuts must be compared
  with saved evidence. If this bound misses, stop this sufficient closure
  and retain the exact deficit; it does not prove C>=15/10^6 or a negative
  Hall cut. No second envelope campaign or new lobe integration follows.

The reduction, envelope and arithmetic are not yet completed or verified.
Independent other-parameter and higher-form gaps remain even if it works.

## Completion

The preceding text is the preserved pre-calculation checkpoint.
The completed proof and exact qualifications are canonical in L913,
`lemmas/L913-monotone-exterior-payment-boundary-reserve-unpaid.md`.
The certificate is `scripts/theta-marginal/boundary-reserve-170.json`.
It establishes exterior payment and the reduced proper cuts but misses
the declared reserve threshold. The sufficient closure is stopped.

The initial script execution stopped before writing a certificate because
the reused interval class has no reflected int/interval division.
Replacing `2 / lam**3` by `I(2) / lam**3` fixed that type error without
changing the formula. The completed evaluation has no failed verification
checks. Independent critical audit remains pending; no complete allocation
or actual-Xi sign has been established.
