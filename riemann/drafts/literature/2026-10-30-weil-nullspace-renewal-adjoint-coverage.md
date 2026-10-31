# Nullspace renewal-adjoint cancellation — completed source comparison

TARGET: Test whether the full signed renewal formula in L513 forces both endpoint traces to vanish on a real simple nullvector at a finite first-zero radius through an adjoint cancellation retaining every prime power and the pole.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Queried Weil renewal adjoint boundary traces; logarithmic Laplacian Pohozaev eigenfunction boundary trace; renewal derivative harmonic killed half-line adjoint; logarithmic Laplacian Green boundary integration by parts; and Weil nullspace trace renewal. Searched only local Weil assessments and recorded stops for adjoint/nullspace/Martin duplicates. No matching full-arithmetic annihilation theorem was located; this bounded search does not establish novelty.
SOURCE_EVIDENCE: Read Grzywny–Ryznar arXiv:1107.0745v1 Proposition 3.2, Proposition 3.5 occupation formula and upper-bound proof, Remark 3.6 and Lemma 4.1 including parameter two; Biocic–Vondracek–Wagner arXiv:2010.06240v1 Sections 2.1 (H)/(2.6), 2.6 Definition 2.1/(2.15), Definition 3.1/(3.2), Section 4.2 scope and Section 4.6 (4.22)–(4.24), Lemma 4.6 with complete proof and subsequent dual formula, printed pp.23–24; Hernandez-Santamaria–Lopez Rios–Saldana arXiv:2401.18033v2 Theorems 1.1/1.4; paper 67 v1 Sections 3.2–3.3 and 9. Exact links, limits and reused assessments follow.
COMPARISON: Renewal occupation and regularity supply representation, not annihilation for the perturbed arithmetic operator. The newly inspected weak-dual source requires d>=2 and positive lower power scaling, unlike this one-dimensional slowly varying symbol; its zero boundary-datum operator is distinct from its normalized boundary derivative. No import of that formula into L516 is justified. The direct cutoff test remains uncovered mathematics, with sufficient sources to attempt it without that import.
GAP: Determine an admissible cutoff adjoint identity and its complete endpoint remainder for L513 (T) under L516's exact zero-eigenvalue equation. Neither a domain-valid singular adjoint test nor cancellation of its arithmetic and exterior terms has been established. No endpoint-to-branch rate or actual-Xi positivity follows.
REASON: The literature-only step excludes an apparently relevant dual-boundary shortcut by its exact hypotheses and observable, then permits one bounded direct test of the unchanged target. It neither proves nor disproves the proposed nullspace cancellation; the assessment is prepared for the supervisor's separate approval before mathematics.
LITERATURE_REASON: Nullspace cancellation via a signed renewal-adjoint identity is outside the assessed finite-Abel technique and needs primary theorem and obstruction comparison before a mathematical attempt.
SCOPE: Only the exact TARGET under the retained L516 realization and assumed real normalized simple nullvector at a finite first-zero radius; direct smooth-cutoff weak-equation testing using L513–L515 is covered for exploration, not a singular integration-by-parts theorem or the near-zero branch estimate.

## Proposed scope and discriminating test

The main gap remains actual-Xi all-degree positivity. The proposed
intermediate target is only zero endpoint traces at an assumed finite
first zero with a real normalized simple nullvector. This is a necessary
endpoint condition for the desired relative-flux mechanism if the
relevant branch and trace limits extend to that endpoint; it does not
by itself give tau_L^2+tau_R^2=O(lambda) along the approaching branch.
That quantitative rate and the extension to the endpoint are still
unproved, and no such continuity is taken as an input here.

Keep the exact complete model of L516 on a finite interval, with the
L512 normalization, and use L513 (T) only through its audited L514–L515
domain and bounded-data application. The candidate observable is the
pair of absolutely convergent signed trace functionals already stated
in L513, evaluated on the assumed nullvector. Seek an adjoint identity
using the full zero-eigenvalue equation that makes these functionals
vanish. This nomination does not assert that an admissible adjoint
test exists, that it annihilates the traces, or that the nullvector
exists. Its required domains and all boundary/exterior terms must be
specified before an application.

A successful source comparison must locate applicable primary
hypotheses or define a bounded concrete test of a proposed adjoint
identity. Merely saying that a trace must be orthogonal to a nullspace
is a reformulation. The known scalar-shift contrast prevents inferring
vanishing from regularity or a first crossing alone; the new mechanism
must use the actual arithmetic coefficients. An exact nonzero residual
or a mismatch of domains would be informative negative evidence for
the proposed identity. No sign or RH-equivalent positivity may be
silently assumed.

Retain the unaudited full-Weil identification and original source
qualifications. First-zero endpoint existence, quantitative trace
control near it, multiple branches, collar/support laws and Xi transfer
remain separate. L517 is a contrast and route-selection reason, not a
nullspace theorem. The nomination was previously uncovered; the source
comparison below completes this literature-only step without executing
the proposed test. Mathlib coverage is unchecked and no cross-notebook
input is proposed.

## Primary theorem comparison

**Renewal representation, not a full-operator adjoint identity.**
[Grzywny–Ryznar, *Potential theory of one-dimensional geometric stable
processes*, arXiv:1107.0745v1](https://arxiv.org/html/1107.0745v1),
4 July 2011, Proposition 3.2 assumes a symmetric non-compound-Poisson
Levy process with exponent psi(xi^2), psi complete Bernstein. Its
renewal density is completely monotone. Proposition 3.5's proof invokes
Bertoin VI.20 for nonnegative occupation data; Remark 3.6 bounds the
half-line Green integral. Lemma 4.1 includes alpha=2 and its separate
b=1 case; near zero it gives v(x) comparable to
1/[x log(1/x)^(3/2)]. The L513 time normalization is reused, not
reproved. These statements do not supply an admissible operator-domain
test for the full signed perturbation. L513 already handles the signed
potential and the nonzero exterior forcing: calling a renewal function
harmonic does not remove either obligation. No new harmonicity or
singular-adjoint theorem is imported.

**A relevant dual formula has different hypotheses and two different
boundary observables.**
[Biocic–Vondracek–Wagner, *Semilinear equations for non-local operators:
Beyond the fractional Laplacian*, arXiv:2010.06240v1](https://web.math.pmf.unizg.hr/~vondra/semilinear.pdf),
13 October 2020, Section 2.1, printed pp.3–4, assumes d>=2 and
complete Bernstein phi with (H):

    a1(t/s)^delta1 <= phi(t)/phi(s) <= a2(t/s)^delta2,
    t>=s>=R0, 0<delta1<=delta2<1.

Section 4 concerns bounded C^(1,1) sets. Section 4.6, printed pp.23–24,
defines d(G_D psi)/dV by the limit (G_D psi)/V(distance).
Lemma 4.6 represents this derivative by the modified Martin kernel
for bounded compactly supported psi. Its complete proof uses the
support's positive boundary distance and bounded convergence. The
subsequent dual formula keeps exterior data and pairs boundary data
against the test's derivative. In contrast, Definition 2.1's W_D
satisfies W_D(G_D f)=0 in (2.15). That is not a statement that
d(G_D f)/dV=0. The log symbol here has slow variation rather than
(H)'s positive lower power scaling, and dimension is also outside
scope. This is a source-scope exclusion, not a new impossibility
theorem for the target. No extension of this source is used.

**Regularity and Hopf conclusions do not give the desired cancellation.**
[Hernandez-Santamaria–Lopez Rios–Saldana, arXiv:2401.18033v2](https://arxiv.org/html/2401.18033v2),
Theorem 1.1 assumes a bounded set with uniform exterior sphere condition,
bounded forcing and a bounded energy-space weak solution. It gives
continuity and a boundary upper estimate. Theorem 1.4 requires a
nontrivial globally nonnegative supersolution and an interior sphere;
its normalized inward liminf is strictly positive. These extra sign
hypotheses are unavailable for the full signed operator. Neither
theorem is a zero-trace result. Reuse L513's checked regularity
application; no new application is asserted here.

**Exact arithmetic source and prior stops.**
[bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67),
27 October 2026, (3.16)–(3.19) retains the exterior forcing in its
signed trace. Section 9, (9.1)–(9.5), explicitly lacks the relative
trace estimate near a finite first zero. Its scalar-shift contrast
does not settle the arithmetic nullspace question. No adjoint
annihilation theorem was found there. Original realization and collar
proofs remain unaudited. Reuse the local renewal/domain/smoothing and
L516 audit assessments; the withdrawn Pohozaev import remains parked.
L517 and its saved Abel stop concern non-eigenvectors, not this target.
No duplicate exact nullspace calculation was located in the narrow
local search. None of these comparisons certifies originality.

## One bounded mathematical continuation, not performed here

Keep the TARGET verbatim. Under L516's retained model, translate the
assumed nullvector to (0,ell), ell=2a, and use L515's bounded-data
application of L513. Investigate smooth compactly supported cutoffs of
the left renewal-density weight and its reflection as weak tests.
At each positive cutoff use only the justified weak equation. Retain
the scalar term, continuous nu_rho part, all prime-power atoms including
cutoff equalities, signed pole, and L513's exterior tail. Seek a
controlled cutoff limit and compare its *complete* remainder with (T).
This specifies a test, not an assertion that it yields an identity
or that the relevant limits vanish. No uncut singular test is admitted
by fiat, and no new residual formula is derived this turn.

Continue only if the exact zero equation yields a justified identity
forcing both traces to zero through actual coefficient cancellation.
An explicit surviving boundary/exterior residual or demonstrated
domain failure ends this proposed adjoint implementation; a mere
restatement of (T) is not progress. Preserve any such evidence. Even
successful endpoint cancellation leaves the O(lambda) branch rate,
trace-topology convergence, multiple branches, source identification,
collars/support transfer and actual-Xi signs unresolved.

No mathematical scripts, new lemmas, numerical evidence or Mathlib
coverage claims were produced. The generalized boundary-regularity
references underlying the inapplicable dual source remain unread
leads, not missing inputs to this direct cutoff test. The arXiv HTML
mirror of that source timed out once; its complete relevant PDF
passages were accessible, so there is no essential source blocker.
