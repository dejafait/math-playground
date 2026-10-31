# Fixed-interval trace audit — work in progress

2026-10-30. Gate: the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-30-weil-renewal-trace-input-coverage.md`,
whose COVERED_TARGET is the exact current Next action.

Audit only paper 67 v1 (3.11)–(3.19) for one fixed ell>0,
u in Dom(G_(0,ell)), u and h=G_(0,ell)u bounded, retaining the
interval-to-half-line domain split. L512's general eigenfunction,
collar, and varying-operator hypotheses are outside this audit.

The main gap is actual-Xi all-degree positivity. The intermediate
target is the normalized signed endpoint trace. Its potential use is
to justify an analytic input to a later arithmetic flux estimate.
Continue only if renewal constants, absolute potentials, spectral
identification, and continuous-representative passage all check;
otherwise retain the first failed implication as an assumption.

Local duplicate/failure screen: L512 explicitly retains these traces.
The automatic-support and rank-trace stops in ATTEMPTS concern
arithmetic uniformity and single-pair detection, not this audit.
No cross-notebook input. No mathematical scripts are needed.

Initial issue: the extended g is not bounded globally. Signed
occupation is not a direct application of GR's nonnegative formula.
The spectral argument must use ker(G_+)={0}, not a spectral gap.
Exact leading renewal normalization and the a.e.-to-pointwise step
remain to be checked. No result is asserted at this checkpoint.

## Partial reasoning saved before canonical write-up

The local-time scaling gives kappa=kappa_GR/sqrt(2), V=sqrt(2)V_GR,
v=sqrt(2)v_GR and K=2K_GR. The constant b in v remains sqrt(2).
Concavity gives |log(Psi(sr)/Psi(s))|<=2|log r|, an integrable
dominator with weight (1+r^2)^(-1). The two Laplace sandwich
inequalities in (3.14) recover the constant one in V's asymptotic.

The exterior forcing has the absolute majorant
(||u||_infinity/2) integral_r^(r+ell) exp(-t)/t dt, r=y-ell.
It lies in L1 and L2. The absolute double integral without v equals
at most ||u||_infinity/2, since its scalar kernel integral is
integral_0^infinity min(t,ell) exp(-t)/(2t) dt <= 1/2.
Thus weighting this exterior integral by v(y)<=v(ell) is legitimate.

For x<epsilon/2, the normalized near-zero potential is at most
||h||_infinity V(epsilon). For y>=epsilon the normalized kernel is
bounded by v(epsilon/2), and converges to v(y). The source's diagonal
kernel can be infinite; its integrated occupation bound is the input,
not a false bounded diagonal assertion.

The spectral theorem gives exp(-T G_+)U -> 0 strongly because
ker(G_+)={0}; no positive spectral gap is used. Integer-time signed
Bochner potentials converge in L2 and, by absolute occupation, to
the Green potential pointwise near zero; an a.e.-convergent subsequence
identifies them. A continuous u/V inherits the limit from its a.e.
equal representative by density. Continuous representatives follow
from HLS Theorem 1.1 after the bounded q-convolution comparison,
with the full weak form and real/imaginary parts checked.

The standard part-form/killed-process identification is being checked
at the level of its actual hypotheses. General eigenfunction bounds,
the retained domain split and collar uniformity are not proved here.

## Completed disposition

The audit passes at its stated scope; full proof and qualifications
are canonical in [L513](../../lemmas/L513-fixed-interval-signed-renewal-trace.md).
The supplemental standard-theorem check inspected the primary text of
Fukushima–Oshima–Takeda, second edition, Section 4.4, Theorems
4.4.2–4.4.3, pp. 173–175, in a hosted scan. This verifies the named
part-process correspondence within the already covered semigroup
identification target; it does not change the assessment or add a
new research target. The open-half-line, regular symmetric form and
killed-process hypotheses are checked in L513.

This is ADVANCE in the notebook's audited inputs, classified
REPRODUCTION, with no result beyond the checked manuscript claimed.
No mathematical experiment or numerical evidence was used. The
remaining domain split is still explicit; no claim about every full
Weil eigenfunction, collars, or vanishing-eigenvalue uniformity is made.
