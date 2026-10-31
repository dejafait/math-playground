# Full-frequency Mellin reflection — source review notes

Literature-only step, 2026-10-31. No analytic implication is proved here.
The saved target is unchanged. Main gap: actual-Xi all-degree positivity.
The bounded intermediate target is the analytic reflection premise in
L541, retaining L547's finite construction and the coefficient/Gauss
contracts in L546. It could support the conditional energy route;
global closure and a sign bridge remain independent gaps.

## Search and preserved boundary

Notebook-local searches of family003 assessments, source notes and
histories for `mellin`, `constant.term`, `unit.fourier` and
`reflection-direct` found the canonical-cusp and reflection-phase
reviews, but no completed full-frequency analytic audit. Their finite
construction coverage is reused. Existing changes throughout this
notebook are preserved. No cross-notebook result is used.

External queries performed:

- `"cubic theta" "Mellin" reflection constant term Dunn Radziwill`
- `"Dunn" "Radziwill" "5.25" Mellin`
- `"The Quasi-Riemann Hypothesis" "reflection" Mellin`

The inspected primary texts are the pinned family003 TeX and DR v3
below. Other returned leads are not theorem evidence. A failed search
does not imply novelty. The local issue is checking a source-claimed
application, not discovering a new Mellin identity.

## Primary material inspected

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, 30 September 2026, commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex):
definitions and proposition at 1551–1678; raw cusp/whole-index support
at 1782–1934; complete Mellin and continuation argument at 2139–2260;
pointwise Mellin-tail hypotheses at 1073–1091 and proof at 1158–1166.
The direct and reflected identities are separately asserted on
Re(s)>1 and Re(s)<0. The source keeps arithmetic data fixed for these
analytic statements; its growth constants may depend on that data.

Dunn–Radziwill, *Bias in cubic Gauss sums: Patterson's conjecture*,
Annals of Mathematics 200 (2024), no. 3, 967–1057,
[arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3), 14 May 2024:
(5.1), (5.6)–(5.16), Lemma 5.2's hypotheses and proof opening,
Corollary 5.1, Lemma 5.3 and Proposition 5.1, including
(5.43)–(5.60) and all Mellin/continuation proof cases, were read.
Lemma 5.2/Corollary 5.1 require a primary period and unit-supported
finite Fourier transform. Proposition 5.1's ell=0 pole and ell!=0
entire cases must be distinguished. These ready-made twisted results
do not directly cover the full-frequency target.

The raw list (5.15)–(5.16) has constant
sigma*v^(2/3), sigma=3^(5/2)/2, for F_1, but none for F_19,F_10.
It specifies conjugation with -mu. Appendix A row identifications
are reused from the canonical-cusp review, not re-audited here.

The manuscript instead proposes differentiating the raw automorphy
identity for each reduced rational cusp; the source records a vanishing
vertical-coordinate first derivative at z=0 and removal of the raw
constant term before Mellin transformation. This remains an assertion
to audit, not an implication established during this review.

NIST DLMF version 1.2.8 (15 September 2026), inspected 2026-10-31:
[10.43.19](https://dlmf.nist.gov/10.43.E19),
[10.25.3](https://dlmf.nist.gov/10.25.E3),
[10.30.2](https://dlmf.nist.gov/10.30.E2),
[10.29.5](https://dlmf.nist.gov/10.29.E5),
[5.11.9](https://dlmf.nist.gov/5.11.E9).
The Bessel Mellin integral requires Re(w)>|Re(nu)|; the manuscript
uses nu=1/3, w=2s+1 on its direct side and w=3-2s on its reflected
side. The raw Bessel argument is positive real. Large-argument
asymptotics hold away from the negative-real cut, the small-argument
formula has Re(nu)>0, and Stirling's modulus formula is uniform for
bounded real part. Integer derivative formulas use the DLMF modified
cylinder convention. These are imported supporting formulas, not a
matching theorem for the full-frequency application.

## Displayed source assertions to audit, not proved here

Write q_mu=|mu|^2 and alpha(mu)=mu/|mu|. The source defines

    J(s)=integral_0^infinity [partial_bar_z F(z,v)]_(z=0) v^(2s-1) dv.

Its direct identity is

    J(s)=(3^(5/2)/4)(27/(2pi)^2)^s Gamma(s+1/3)Gamma(s+2/3)T(s,Psi),

initially on Re(s)>1. For a single translated cusp a/c, the reflected
contribution asserted on Re(s)<0 is

    -(i/4)(2pi)^(2s-2) bar(alpha(c))^2 q_c^(1-2s) bar(kappa(G))
      * Gamma(3/2-s-1/6)Gamma(3/2-s+1/6)
      * sum_(mu!=0) d_H(mu)alpha(mu)check-e(-delta' mu/c) q_mu^(-(1-s)).

These are transcriptions of the two labeled source equations, not
independently verified equalities. The finite coefficients C(h) must
still weight and sum the reflected contributions.

The later source quotient uses K=(2pi)^4/27 and
R(t)=product_(+/-) Gamma(1+t+/-1/6)/Gamma(1-t+/-1/6), t=1/2-s.
Its displayed scalar before local finite sums is
-(i/81)bar(alpha(c))^2 q_mu^(-1/2), and its profile argument is
q_mu X/q_c^2. Checking these normalizations is part of the future
audit; no cancellation was derived in this literature step.

## Bounded obligations and coverage decision

1. Keep L547's rational cusps, including a zero numerator and c a unit,
   empty active radical, nonunit h_0 and all local zero frequencies.
   Read the complete chain rule from DR (5.1), without assuming a
   constant term stays independent of z after a coordinate change.
   Check the vertical-coordinate derivative at z=0 explicitly.
2. Check local uniform convergence for differentiation, and absolute
   integrability for each termwise Mellin operation using the retained
   coefficient/support bound, on both original half-planes.
3. Reconcile the whole-index mask and cubic/sextic conversion with T;
   preserve shared n,b primes, every zero extension and the unmasked
   dual support. Finite Gauss formulas remain contracts.
4. Check endpoint decay of every required logarithmic derivative for
   each fixed translate before claiming J entire/rapid in strips.
   No uniformity as c varies is licensed by the source's fixed-data
   estimates. Verify division by gamma using reciprocal entire factors.
5. Check the claimed exponential preliminary bound, polynomial bounds
   on both boundary lines and the e^(epsilon*s^2) maximum-modulus
   argument, including the epsilon limit. This is not a consequence
   of rapid vertical decay of J alone.
6. Check the shifted contour and sum/integral exchange with the stated
   V hypotheses and pointwise tail bound. Verify the gamma quotient,
   scalar and scale, with no residual contribution from a zero mode.

All essential primary proof cases for these bounded obligations are now
accessible and inspected. Decision: SPECIALIZE for a separate
conceptual reproduction audit of the unchanged target. The difference
from DR's ready-made theorem is full-frequency applicability through
raw cusps; it cannot be removed by citing the restricted theorem.
No source blocker persists. The search of ATTEMPTS for unit-Fourier,
unit-supported, (5.25), Dunn/5.2 and Mellin-reflection terms returned
no matching attempt; prior unit-Fourier limitations in the two source
assessments remain preserved. No novelty is inferred.

Continue only if the application passes all six obligations; record and
narrow or park any exact failed implication. Successful source review
does not independently review L547 or discharge any analytic premise.
No uniform conductor bounds, new kernel seminorm estimates or actual-Xi
signs are licensed. Mathlib matching coverage was not checked. No lemma,
mathematical script, DAG or PROOF change was needed.

Additional literature reason: the Mellin proof after its opening and
DR's exact Mellin/zero-term proof cases were essential unread inputs
outside the prior ready finite-cusp scope. This review fills that
specific source gap; subsequent unchanged work defaults to mathematics
after the supervisor's separate gate approval.
