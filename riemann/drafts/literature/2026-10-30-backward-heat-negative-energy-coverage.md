# Backward heat flow and negative first-defect energy — source comparison

TARGET: Review source coverage for a backward heat-flow inequality for finite-interval negative first-Laguerre energy, separating bulk production from boundary flux and specifying a polynomial-jet obstruction test.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-energy, Laguerre/heat, Kato/boundary and log-concavity searches; local L058, L126/L128, L471 and L486 scope checks. Queries, primary passages and exclusions are recorded below and in drafts/heat/2026-10-30-negative-energy-source-review-working.md. No inspected source supplies the full zero-safe backward energy estimate; no novelty claim.
SOURCE_EVIDENCE: Inspected Rodgers--Tao v3 Introduction and Theorem 4.1; Csordas v2 Theorem 4.6, Open Problem 4.7 and (4.9)--Proposition 4.9; Brezis--Ponce published Theorems 1.1--1.3 and 7.1 with its zero-trace proof; Alber June 2018 Lemma 5.2 and Theorem 5.3 with proof; Keady Theorems 1.2, 4.0 and Section 4 proof; Schatz November 2025 Proposition 6.3 and stated scope, not its claimed RH proof.
COMPARISON: Standard truncation and boundary tools cover smooth finite rectangles. Keady's relevant concavity propagation requires positive heat solutions and bounded coefficients after localization; it does not cover collisions at interior real zeros. Rodgers--Tao uses a different zero-interaction energy in a real-simple-zero regime. None is an inspected match for the proposed zero-safe clipped-defect estimate.
GAP: The backward bulk estimate through multiple real zeros is unproved. Test it first on exact polynomial heat families with a fixed zero-flux boundary condition; no source theorem or local result currently justifies division by H or by the negative energy near such zeros. Actual-Xi normalization, global flux and all-degree signs remain independent gaps.
REASON: New source comparison resolves the essential convention, truncation and endpoint-source questions sufficiently to nominate an independent obstruction test; it does not establish the energy evolution or its estimate. The fresh mathematical continuation requires separate approval next turn.

## Reviewed target and relevance

The target remains the original proposal, with

    partial_lambda H=-partial_x^2 H, H_0=Xi,
    q_lambda(x)=D_1(H_lambda;x)=H_x^2-H H_xx,
    E_lambda([a,b])=integral_a^b (-q_lambda(x))_+ dx.

These definitions are not a proved evolution equation for q or E.
L471's normalized negative mass is the downstream motivation. L486's
positive sector certificate leaves its complementary sector and full
signed mass uncontrolled. A backward comparison might address that loss,
but converting finite-interval control into N(T)=o(T(log T)^3), controlling
endpoint flux and proving all-degree mixed positivity would still be needed.

Local duplicate/failure check: L058 already proves joint entirety and all
mixed derivative formulas for this exact theta heat family. Its compact
majorant covers finite real parameter/height rectangles without simplicity
or RH. L018 supplies the actual Xi convention; L019/L020 identify its
kernel. L126/L128 and
[the prior heat/Fourier stop](../../ATTEMPTS/2026-09-20-heat-fourier-relevance-audit.md)
concern moving zero-height suprema and nonuniform exhaustion. They neither
prove nor disprove the proposed finite-interval comparison. Their stop is
preserved; no infinite supremum argument is reopened. No cross-notebook input.

## Primary theorem comparison

1. **Heat convention and different energies.** Brad Rodgers and Terence Tao,
   *The De Bruijn--Newman constant is non-negative*,
   [arXiv:1801.05914v3, 6 March 2020](https://arxiv.org/html/1801.05914v3),
   Introduction (1)--(4), Theorem 1.1, Section 4 Theorem 4.1 and the
   ensuing energy discussion were read. Their H_0(z)=Xi(z/2)/8 and
   partial_t H_t=-partial_z^2 H_t; use L058 directly to avoid a hidden
   spatial/time normalization change. Theorem 4.1's dynamics are stated
   for Lambda<t<=0, and their interaction energy is over real simple
   zeros, not integral(-D_1)_+. Its proof refers to Csordas--Smith--Varga;
   that older proof is uninspected here. Neither that conditional regime
   nor the formal untruncated energy is imported for our target.

2. **Laguerre sign and collision warning.** George Csordas,
   *Fourier transforms of positive definite kernels and the Riemann
   xi-function*, [arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
   printed pp. 11--12, Theorem 4.6, Open Problem 4.7, (4.9)--(4.10)
   and Proposition 4.9 were read. The first Laguerre sign is posed as
   an open problem in that version; this is not a claim about all 2026
   literature. Heat monotonicity concerns increasing parameter and
   does not supply our decreasing-parameter estimate. Proposition 4.9
   records the importance of multiple zeros; its cited older proof is
   not independently imported. The earlier Gaussian assessment is
   reused only within its documented scope.

3. **Boundary accounting.** Haim Brezis and Augusto C. Ponce,
   *Kato's inequality up to the boundary*, Comm. Contemp. Math. 10
   (2008), 1217--1241, [published author-hosted PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/198journal.pdf).
   Read (1.1), Theorems 1.1--1.3, Theorem 7.1 (p. 1234), Lemma 7.2
   and its proof cases (pp. 1235--1236). For u in W^{2,1}(Omega),
   Theorem 7.1 gives the outward normal trace of u_+:

       partial_n(u_+) = partial_n u       if u>0,
                       0                 if u<0,
                       min(partial_n u,0) if u=0.

   This includes zero boundary values and does not license setting
   their flux to zero. For u=-q on an interval, define the candidate
   diffusion flux F_lambda as the sum of these two outward traces. This
   is boundary notation from the theorem, not a derived energy balance.
   Smooth q meets the Sobolev hypothesis. The Kato inequality controls
   truncation's distributional second derivative, not the heat source
   of the nonlinear q. No energy estimate follows by citation alone.

4. **Negative-part regularity.** Hans-Dieter Alber,
   *Nonlinear elliptic and parabolic partial differential equations
   (PDE 2)*, lecture notes 2007--2013, revised 10 June 2018,
   [Section 5.1, Lemma 5.2 and Theorem 5.3, pp. 89--91](https://www2.mathematik.tu-darmstadt.de/~alber/pde_2.pdf).
   Read their statements and complete approximation/zero-level proof.
   On a bounded open Omega and for 1<=p<infinity, u in W^{1,p}
   implies u_+ in W^{1,p}, with weak partial derivatives
   1_{u>0} partial_j u; derivatives vanish a.e. on {u=0}.
   Taking spacetime as Omega covers the future smooth compact test.
   It is an a.e. weak-derivative tool, not a pointwise derivative claim
   at every degenerate time. Fubini/absolute continuity and the energy
   evolution must still be justified in the research step.

5. **Closest concavity propagation.** G. Keady,
   *The persistence of logconcavity for positive solutions of the one
   dimensional heat equation*, J. Austral. Math. Soc. (Series A) 48
   (1990), 246--263, [doi:10.1017/S1446788700035679](https://doi.org/10.1017/S1446788700035679).
   Read Theorem 1.2 (p. 250), Section 4 (pp. 256--257), Theorem 4.0
   and its proof, together with the bounded-coefficient hypotheses of
   Maximum Principles 2.1--2.2 (pp. 251--252). For smooth positive
   forward-heat solutions, nonpositive I_2=u u_xx-u_x^2 initially and
   in boundary neighborhoods propagates. Here forward time means
   decreasing our lambda. Section 4's logarithmic quantities and
   coefficients involve division by u. Its positivity and coefficient
   conditions do not cover an interval containing an interior zero
   or a collision. No zero-safe quantitative E estimate is stated.
   Reproving its positive-solution preservation would duplicate known
   mathematics; a collision test examines the uncovered difference.

6. **Related claimed backward barrier, not an import.** Kevin Schatz,
   *Riemann Hypothesis: Backward Parabolic Positivity Barriers for the
   Xi Flow*, preprint dated 20 November 2025,
   [doi:10.5281/zenodo.17636625, author's PDF](https://kschatz.github.io/rh-xi-backward-parabolic-barrier/schatz_riemann_hypothesis_backward_parabolic_positivity_barriers_xi_flow.pdf).
   Read its abstract, scope discussion and Proposition 6.3 with the
   surrounding argument on printed pp. 34--35. The proposition concerns
   h=Im(-E_t'/E_t) on collision-free zero-free regions, assumes h_- at
   top time vanishes, and imposes a tube/Carleman parameter coupling
   involving a zero-speed bound. It is not a theorem about our real-axis
   q energy through collisions. Its collision bridge, global exhaustion
   and claimed RH proof are unreviewed; no correctness or falsity
   verdict on that manuscript is made, and no conclusion is imported.

## Bounded continuation and abandonment test

The nominated test is a **calculation**, not a new creative RH mechanism.
Use a real even polynomial P of degree at most eight and its exact finite
heat evolution, at parameters lambda in [-h,0], h>0. Fix I=[-2,2]. Require
H_0(0)=1, H_lambda(iy)>0 for every real y, all zeros in |Im z|<=1/2,
and q_lambda>0 throughout fixed collars [-2,-7/4] and [7/4,2]. Allow
multiple real zeros. These are requested certificate conditions, not
asserted facts about a constructed P. The collars fix F=0 without
needing to sign boundary terms; internal zero-set contributions must
still be retained. Positive imaginary-axis values mimic a limited
L058 property, not the theta representation or arithmetic structure.

Test the proposed inequality -partial_lambda E<=C(lambda)E a.e., where
C is locally bounded through lambda=0. Dependence on the fixed family,
interval and bounded jets is allowed; singular inverse-energy or
inverse-H bounds at a collision are not. Seek either a completely
verified family with E_0=0 and E_lambda>0 at earlier parameters, or an
explicit unbounded production/energy ratio. The standard integral
Gronwall comparison is the criterion for the terminal-zero test.
If this certificate exists, stop this generic mechanism; it is not an
actual-Xi counterexample or a refutation of an arithmetic refinement.
If it does not, record the failed test and the exact missing bulk
inequality; no general theorem follows from absence of a low-degree
example. No polynomial, derivative identity or inequality was derived
in this literature turn.

Known-source regularity is sufficient for this finite test, with no
essential source blocker. The fresh matching assessment is
[the polynomial-test nomination](2026-10-30-polynomial-heat-energy-obstruction.md),
subject to separate approval next turn. Essential inputs are L058 and
L018 for the structural comparison, and L471/L486 for relevance only.
The actual-Xi transfer, height-uniform constants and all signs remain
unresolved. A genuine creative continuation is blocked by the untested
collision/bulk-control premise, rather than by a literature quota.

## Search record, unread leads and Mathlib

Web queries included: `de Bruijn Newman heat equation Laguerre inequality
negative part energy Kato`; `"Laguerre" "heat equation" inequality`;
`"Kato" "Ponce" "boundary" pdf`; `"first Laguerre" "heat" inequality
energy`; `"Laguerre" "negative part" heat energy`; `"Laguerre inequality"
"heat flow" polynomial`; `"log-concavity" "heat equation" Brascamp Lieb
1976 pdf`. Local searches used the named historical heat audit and
Gaussian assessment, then narrow negative-energy/Kato/flux terms in
ATTEMPTS/, drafts/literature/ and foundations/.

Original de Bruijn/Newman/Pólya, Csordas--Smith--Varga, Brascamp--Lieb
and the older proofs cited in these sources are unread leads, not
independently audited inputs. Keady and the directly inspected
truncation sources suffice for the stated comparison/test preparation.
No search absence establishes novelty. Mathlib coverage of the full
heat-family clipped-energy result is **not checked**; supporting
Sobolev/convexity results have not been matched here. No absence claim.
