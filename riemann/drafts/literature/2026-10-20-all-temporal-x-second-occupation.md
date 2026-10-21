# Source coverage: all temporal x-second occupation tests

TARGET: Determine whether a uniformly bounded, exactly w-height-recentered bulk covariance perturbation of L443, with zero 11 entry and unchanged rare components, mean and cutoff, can satisfy the x-squared occupation identity for every temporal test a in C_c^1((H,2H)) at each sufficiently large real H while retaining L443's selected constraints and three exact identities.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 272 searched arbitrary-test occupation/Liouville constraints, prescribed-density bounded-flux and covariance feasibility, and weak-derivative/Lipschitz and L1-duality terminology; compared L438/L440/L441/L442/L443 and the fixed-Gaussian stop. No inspected theorem settles this complete constrained law; unsuccessful searches establish no novelty.
SOURCE_EVIDENCE: Inspected Lasserre--Henrion--Prieur--Trelat math/0703377v1 (2.7), (2.10)--(2.12), printed pp. 4--5; Hunter, Notes on Partial Differential Equations, revision 2014-06-18, Definition 3.1, Examples 3.4--3.5, Theorems 3.53 and 3.60--3.63, pp. 47--49 and 77--80; Hunter, Measure Theory (2011), Proposition 7.13 including its p=1 proof and the sigma-finite p=1 extension stated after Theorem 7.14, pp. 84--87. Reuse prior real Schur--Horn and finite-Poisson source assessments at their stated scope.
COMPARISON: The arbitrary C1 occupation identity covers the necessary test family. Standard weak-derivative and L1-duality results provide regularity and bounded-functional tests, not estimates for L443's complete raw matrix or a supported uniformly bounded recentered covariance solving the infinite family. Its finite triangular inverse cannot supply those missing estimates.
GAP: Specialize the weak identity to the complete conditional raw seconds and determine whether a uniform bounded-correction condition survives all temporal tests; retain exact weighted recentering, the fixed 11 density, both other finite identities and all selected-law requirements. Neither feasibility nor an obstruction is established by this review.
REASON: Essential source coverage is sufficient for one later mathematical attempt on exactly TARGET. The remaining weak-balance calculation, complete-law estimates and preservation checks are local mathematical obligations; import the standard results instead of reproving them. No new law-specific identity, lemma, derivative bound or impossibility result is derived here.
LITERATURE_REASON: The invocation required a separate review of the changed all-temporal target; prior ready assessments approved only specified finite occupation blocks. This turn adds the missing weak-derivative and bounded-functional source comparison without repeating their calculations.
SCOPE: Start with exactly L443's complete Borel law on its eventual real-H ray, including all rare raw seconds and translation. The test is phi(t,x)=a(t)x^2, with arbitrary a in C_c^1((H,2H)); preserve conditional x-second density, exact integrated raw seconds, first B mean, every selected tolerance and the three previously exact identities.

The main gap remains global mixed positivity. This intermediate target
tests whether the freedom used to repair finitely many occupation
identities survives an entire temporal test class. A supported construction
would clarify the limits of a stronger necessary diagnostic; a rigorous
bounded-perturbation obstruction would isolate a constraint beyond the
validated finite block. Neither outcome would prove actual/global
realization or evaluate actual clipping.

Essential inputs are L419's exact forms and Borel realization,
L438's complete law and tolerances, L440/L442's occupation interface,
L441's bounded perturbation estimates and audited L443. L429's
unchanged cutoff is used only through the exact local interfaces unless
a later reviewed target requires a narrow read of its proof.

## Primary theorem scope

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[math/0703377v1](https://arxiv.org/pdf/math/0703377v1), Sections
2.2--2.3, (2.7), (2.10)--(2.12), printed pp. 4--5 (PDF pages 4--5),
gives the generator and endpoint identity for every C1 test along an
admissible trajectory on compact state/control sets. The occupation
measure is defined from that trajectory; the displayed identity follows
by its differential equation and the chain rule. The word "conversely"
in Remark 2.2 concerns a measure already defined from a trajectory;
it does not represent an arbitrary Borel kernel by a trajectory.

Reuse L424/L440's state (x,y), control z and ordinary dynamics. For
each fixed H, ordinary C2 trajectories fit finite compact boxes. A
compactly supported temporal C1 coefficient gives a C1 polynomial
state test with zero endpoints. No uniform box in H is required.
L443's finite-H envelopes make the law's tested integrals finite.
Writing its full arbitrary-test specialization is deferred to research.

John K. Hunter, *Notes on Partial Differential Equations*, author-hosted
[full notes](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf), revision
18 June 2014, Definition 3.1, printed p. 47; Examples 3.4--3.5,
pp. 48--49; Appendix 3.A, Theorems 3.53 and 3.60--3.63, pp. 77--80.
For locally integrable functions, a weak derivative is defined by
integration against derivatives of smooth compactly supported tests.
In one dimension an integrable weak derivative gives an absolutely
continuous representative; an essentially bounded one gives a Lipschitz
representative with the same derivative norm. These are statements up
to almost-everywhere equality, not pointwise regularity of chosen atoms.
The appendix states the characterizations without complete proofs;
the inspected discussion gives the fundamental-theorem argument and
integration by parts. The worked jump and Cantor cases show why
pointwise differentiation almost everywhere alone is insufficient.

John K. Hunter, *Measure Theory* (2011), author-hosted
[notes](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf),
Section 7.5, Proposition 7.13, printed pp. 84--85, and the paragraph
after Corollary 7.15, p. 87. On a sigma-finite measure space, integration
against an L-infinity function defines a bounded L1 functional with
equal norm. Its p=1 proof selects a finite-measure subset of a near
essential-supremum level set. The converse identification is explicitly
stated as the p=1 extension of Theorem 7.14; its detailed endpoint proof
is omitted. The printed theorem itself has 1<p<infinity. Finite Lebesgue
intervals satisfy sigma-finiteness. This is scalar duality, not matrix
positivity, mean calibration or joint Borel selection in H. No endpoint
proof is claimed independently verified here.

These inputs justify testing weak regularity and bounded action on
temporal functions before seeking a covariance field. They provide no
automatic uniform bound in H, exact recentering, or compatible values
for the remaining entries. No reproof of the cited characterizations,
duality theorem or occupation identity is needed.

## Local applicability and continuation test

L443 (1) is the complete raw matrix to use, including all of R, w,
translation, constant calibration, L441's field and L443's field. The
11 entry is fixed by the permitted perturbation, but nothing in the
selected constraints asserts its weak differentiability. L438 (12)--(15)
and L440 (3)--(5) give useful size and integrated error bounds; an
integrated small error does not assert any derivative bound. Hold H and
its cutoff stage fixed within the temporal interval. Do not differentiate
selected atoms or infer smoothness from the finite atomic realization.

L429's product is finite at each fixed H, and its source assessment
already covers finite Poisson character integrals. The unchanged
growing cutoff and L440's finite-Fourier interface remain available.
Those facts alone supply neither regularity of the complete raw matrix
nor a uniform bound on the correction forced by all temporal tests.
A Poisson leading term may suggest a test, but the complete rare and
translation contributions must be retained in any conclusion. No new
actual-zeta moment theorem or actual sine limit is needed merely to
test this explicitly specified conditional law.

Continue with one weak-balance feasibility attempt: formulate the full
arbitrary-test constraint, then test the requisite regularity and the
size of a correction by localized temporal tests or the cited L1 norm
comparison. The discriminating threshold is one absolute covariance
bound independent of H, with exactly zero w-weighted height mean.
A construction must also preserve the zero 11 entry, the two other
finite identities, all selected tolerances and supported Borel
realization. Reuse L441/L443's established bounded-perturbation support
estimates only within their hypotheses.

Abandon this bounded-correction target only after an obstruction applying
to every allowed field: failure of the required weak regularity, an
incompatible exact mean condition, or a necessary correction norm
unbounded along sufficiently large heights. Failure of one ansatz,
a large derivative of one summand, a jump in an atom choice, or a
Poisson-only calculation is insufficient. If the first necessary test
passes, feasibility remains open until a complete supported field and
all preservation checks are supplied. No such test is performed here.

L440/L442 separated particular old laws; L443 now passes their finite
block. L439's fixed-Gaussian nonzero-limsup stop does not decide this
all-temporal question. L428's bounded normalized density obstruction
must not be silently applied to L443's unchanged growing density.
Other occupation classes, actual/global realization, clipping, capped
nondegeneracy, L413's full-error margin and global mixed positivity
remain open. Full matching Mathlib coverage has not been checked;
no absence claim is made. This source review changes neither PROOF.md
nor DAG.md, and establishes no progress beyond the known sources.

## Discovery record and qualifications

Queries included "Lasserre Henrion Prieur Trelat 0703377 occupation
measures Liouville equation", "distribution derivative bounded function
W1 infinity weak derivative characterization", "occupation measures
prescribed moments covariance weak Liouville feasibility bounded
perturbation", "occupation measures covariance prescribed Liouville",
"prescribed density bounded flux continuity equation", "occupation
measures second moments Liouville covariance", and author-site
weak-derivative and dual-Lp queries. Inspected primary statements are
the three sources above. Search hits about stochastic occupation times,
Markov chains and unrelated covariance problems did not match the
deterministic constrained raw-moment target and are not theorem inputs.
The Purdue-hosted Ziemer--Torres text was located but no theorem was
inspected; it is an unused lead. One alternate Hunter URL failed before
the author-hosted www URL succeeded; optional screenshot failure did
not block the complete relevant text. No essential source remains
inaccessible. The earlier ready Schur--Horn/Borel and finite-Poisson
assessments are reused, not independently reaudited in this turn.
