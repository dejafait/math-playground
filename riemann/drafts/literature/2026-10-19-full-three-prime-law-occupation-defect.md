# Source coverage: L438 and the fixed Gaussian occupation test

TARGET: Determine whether L438's law has a nonzero limsup Gaussian occupation defect for L424's fixed test, retaining its moving Poisson bulk and all rare components.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 252 checked the scoped occupation/covariance/Poisson assessments, L424--L426, L429, L438, L419's selection cases and the recorded Gaussian/core-tail failures; searched Poisson-kernel prime martingales, Kakutani product measures, Gaussian jet occupation constraints and moving-test equidistribution. No inspected theorem decides the exact L438 observable; no novelty inference is made.
SOURCE_EVIDENCE: Reused the step-174/176 occupation and step-183/209 averaging/finite-Poisson primary readings; rechecked Lasserre--Henrion--Prieur--Trelat (2008) (2.7),(2.12), manuscript pp. 3--5, Henrion--Korda--Kruzik--Rios-Zertuche (2023-03-04) Definitions 2.4/2.7 and Lemma B.1 with its proof, pp. 3--4,17--18, and Aistleitner--Berkes--Seip arXiv:1210.0741v5, pp. 10--11, kernel identity and Lemma 1/(23).
COMPARISON: The necessary finite-H trajectory identity and finite-product harmonic identities are covered. Fixed-test compact-group convergence does not evaluate the moving Poisson observable. L424--L426's fixed-weight law comparisons and C426a--C426c's fixed-mixture signs/stops are not results for L438's changed covariance and signed intermediate kernel.
GAP: Estimate the exact complete law using only L429's unchanged cutoff guarantees; control every rare component, translation, full covariance correction and prescribed Borel branches without a moving-test limit or an assumed uniform-integrability statement. No nonzero defect or vanishing result is established here.
REASON: Essential source coverage is adequate for one bounded exact-law proof attempt using finite-H estimates and finite-head Poisson comparisons. The sources do not supply its changed estimates; this literature-only approval proves none of them and changes no lemma or mathematical script.
LITERATURE_REASON: The saved exact L438 target was REVIEW_REQUIRED because its moving covariance and signed intermediate directions fall outside the ready fixed-mixture occupation assessment; this review resolves that scope question without repeating an already ready target.
SCOPE: Exactly the TARGET, with the fixed Q, complete L438 family, actual response and L419 branch rules, and L429's already chosen all-real-H cutoff; no cutoff strengthening, adjustable test, new law or actual clipping assertion.

## Exact proposed test and downstream use

The main RH gap remains global mixed positivity. A selected conditional
law can avoid the joint sign without being the occupation law of ordinary
critical jets. Test precisely the already defined L424 observable, not a
new adjustable test:

    Q(a,b,d)=exp(-a^2-b^2)[b^2(1-2a^2)+ad(1-2b^2)],
    (a,b,d)=X/sqrt(log H).

L424's C^2 trajectory statement has |E_H Q|<=delta_H,
delta_H=O(1/(H log H)), with both endpoint terms and the moving L(t)
correction included. The proposed discrimination threshold is
limsup_(H->infinity)|E_(nu^438) Q(X/sqrt(log H))|>0. Such a result
would separate this specific law from trajectory occupation data agreeing
on the test up to o(1); it would not imply that all admissible counterlaws
fail, evaluate actual clipping, or prove RH. A zero limsup would stop
this fixed leading-scale diagnostic, rather than justify changing the
test or silently demanding a stronger rate in the same step.

Essential inputs to compare are L438's full audited family and L424's
identity, with L419's precise Borel basis and L429's unchanged all-real-H
Poisson cutoff. L425/L426 and C426a--C426c contain the earlier
fixed-mixture covariance-removal/Haar and core-tail work. Read their
relevant exact statements and stops narrowly before any reuse. The
finite-weight integral from those records is not automatically the
moving-weight integral here. The antipodal/radial and capped-clipping
source blockers retain their scopes. No further primes or actual sine
limit is proposed.

Primary source lead, already cited in L424:
[2008-01-30 author manuscript, Sections 2.1--2.3](https://homepages.laas.fr/henrion/Papers/ocp.pdf),
[published DOI](https://doi.org/10.1137/070685051).
L424 also records Henrion--Korda--Kruzik--Rios-Zertuche's
[2023-03-04 occupation-measure manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7 and Lemma B.1, for integrability qualifications.
Their relevance to the changed estimates remains to be compared; these
links do not constitute a new reading or an assertion of realization.
Full matching Mathlib coverage is unchecked.

The proposal above was written in step 251; the completed review below
approves one attempt, not a mathematical conclusion about this test.

## Completed source comparison — step 252

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison, with
outcome EXPLORATION. It supplies a new scope comparison and a bounded
test, not progress beyond the checked theorems, a defect estimate or a
reset of the mathematical exploration budget.

### Necessary identity and integrability: reuse, not a new theorem

The primary occupation coverage is recorded in
`drafts/literature/2026-10-17-jet-trajectory-compatibility.md` and
`drafts/literature/2026-10-17-gaussian-jet-transport-audit.md`.
Lasserre, Henrion, Prieur and Trelat, *Nonlinear optimal control via
occupation measures and LMI-relaxations*, SIAM J. Control Optim. 47
(2008), 1643--1666, DOI 10.1137/070685051, uses smooth dynamics,
compact state/control sets and a C^1 test; (2.12) retains both terminal
values. Its hypotheses and (2.7)/(2.12) were rechecked in the linked
2008-01-30 author manuscript. L424 already supplies the ordinary-C^2-jet
specialization at each fixed H, including the nonautonomous L(t) term.
It requires no uniform compact box as H grows. Import that audited
identity; no reproof or no-gap/realization theorem is needed.

Henrion, Korda, Kruzik and Rios-Zertuche, *Occupation measure relaxations
in variational problems: the role of convexity*, linked 2023-03-04
manuscript, Definitions 2.4/2.7 and Lemma B.1, distinguishes affine
constraints from the full nonlinear test identity. The finite-p test
class has p-growth in the test/time derivative and (p-1)-growth in the
state derivative, with the requisite interior and boundary moments.
The rechecked complete proof uses Holder for finite p and bounded
support in its p=infinity discussion. It establishes integrability
at a fixed measure, not H-uniform integrability or convergence of this
moving family. The source's lemma statement prints p in [1,infinity),
although its proof also discusses infinity; no endpoint extension is
needed here. Neither source decides the value of L438's statistic.

### Finite Poisson input and the limit-order boundary

Reuse the published-primary comparison in
`drafts/literature/2026-10-18-growing-prime-poisson-covariance.md`:
C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, section 3, p. 1527, identity preceding Lemma 1
and (23). This turn additionally read the complete finite kernel
identity and iterated-circle proof in
[arXiv:1210.0741v5, 2013-11-11, pp. 10--11](https://real.mtak.hu/33507/1/berkes.pdf).
For finitely many coordinates of radii in (0,1), it identifies character
integrals against the product Poisson kernel, and hence polynomial
square integrals. The choice p^(-1/2) meets these hypotheses at every
finite stage; infinite square summability is not a hypothesis for this
finite identity. It gives no actual-height nonlinear moving-test limit.
Import the identity rather than reprove it. Any fractional-power or
tail estimate needed for Q remains a mathematical obligation, not a
conclusion attributed to Lemma 1.

The ready compact-group coverage in
`drafts/literature/2026-10-17-covariance-free-bulk-phase-averaging.md`
is also reusable at its stated scope: Kowalski, *Arithmetic Randonnee*,
2021-01-19 manuscript, B.6.3/B.6.5(2), pp. 146--147, and
Proposition 3.2.5/Lemma 3.2.6, pp. 42--43, cover fixed characters
and fixed tests; Morters--Peres, *Brownian Motion*, 2008-05-25 draft,
Appendix Theorem 1.6(v), pp. 331--333, requires a bounded measurable
test with a null discontinuity set for the limiting law. This does
not permit substituting a different test at every H without a separate
comparison. L426's application uses a fixed compact covariance range.

L429 (10) and its cutoff paragraph name a particular finite list of
controlled averages at each stage. Its thresholds B_j are chosen
qualitatively, with log B_j>=M_j^8, and no numerical sequence or
additional nonlinear-test guarantee is specified. L438 explicitly
keeps that selection. A later argument must work for an arbitrary
fixed admissible selection using those saved properties, or identify
precisely what additional information it needs. It cannot increase
the thresholds to include Q and call that an estimate for the saved law.

### Duplicate and failure comparison

The narrowly read local evidence gives the following boundaries:

- L424 (1)--(2) is the exact trajectory benchmark. Its law comparison
  (3)--(7) uses fixed compact normalized atoms. L438 (9)--(17) instead
  supplies two signed intermediate directions, g_H between
  (1/2)ell^(-1/8) and 2ell^(1/8), bounded mean and the full
  O(ell^(1/2)) covariance subtraction. Neither L424's compact Hessian
  argument nor its old intermediate exponential formula is an already
  proved estimate for these new states.
- L419's literal two-stage rule includes first-index equality cases
  and ordered strict pairs. L425 proves continuity off the three leading
  diagonal ties and actual-height small-arc control, but its final
  covariance-removal conclusion has fixed g_-,g_+ hypotheses. Smooth
  positive square roots or closeness of covariance matrices alone
  cannot substitute for that selected-basis comparison here.
- L426 and C426a--C426c concern the fixed k=13,14 mixture. The Gaussian
  screen in `ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`
  was uncertified; the global-complement and smaller-complement stops
  in the corresponding October-17 ATTEMPTS files concern their saved
  bounds and partitions. No fixed-mixture integral sign was settled.
  Those are preserved stops, not evaluations or prohibitions for L438.
- The scoped October-18 Poisson and October-19 full-law assessments
  contain no completed estimate of this observable. This is a local
  duplicate check, not a claim of novelty. Actual clipping and its
  source blockers are outside the present necessary-test problem.

Search queries this turn were `"Poisson kernel" "prime" "martingale"
product`, `"Kakutani" "Poisson" "product measures"`, `"occupation
measures" "Gaussian" "Liouville" constraint`, `"On equivalence of
infinite product measures" Kakutani 1948 pdf`, `"GCD sums from Poisson
integrals" pdf`, `"Gaussian" "jet" "occupation" "Poisson" law`, and
`"equidistribution" "moving" "test functions" Kronecker Weyl`.
The inspected primary statements above do not settle the exact target.
Kakutani's 1948 paper, DOI 10.2307/1969123, was located, but both JSTOR
article/PDF URLs exposed only a landing page; its theorem and proof
were not read and are not imported. Other unrelated Poisson-space and
Gaussian random-occupation results were search leads only. This is
not an essential source blocker: the proposed finite-product test below
does not invoke an infinite-product singularity theorem. Any decision
to use such a theorem later requires its own adequate source coverage.

### One bounded mathematical continuation

Keep the exact TARGET unchanged. A materially different candidate
mechanism from the parked fixed-mixture signing calculations is to seek
an absolute estimate for the complete Q observable via a fixed finite
prime head and a scalar Poisson tail bound. First test whether a
Gaussian envelope valid for every selected atom, together with a
finite-head concavity/fractional-moment comparison on actual heights,
can address the moving covariance without changing the cutoff. These
are proposed estimates only; no such envelope, concentration result,
conditional comparison or limit has been derived in this source review.

Start from L438's exact kernel, L424's test and audited trajectory
identity, L419's actual Borel selection and L429's saved cutoff. Use
L438's own high and two-intermediate component bounds, not the old
L423 intermediate formula. Retain the complete mean and covariance
subtraction. If an estimate is independent of the selected basis,
prove that it applies at every tie as well; otherwise control both
selection stages. Do not assume that the Gaussian damps a state whose
third coordinate alone is large. A finite-head argument must justify
its actual-height averages and limit order, rather than assume
independence of prime phases or uniform integrability.

Continue upon either a rigorous nonzero limsup for the full law, or
a rigorous vanishing limsup, which would stop this fixed leading-scale
diagnostic. If the bounded attempt cannot close these estimates, record
the specific missing bound and whether it concerns the unchanged
cutoff, large states or branch ties. Mere source availability or more
floating phase samples is not progress. Do not alter Q or demand a
stronger rate after a zero-limsup result in the same attempt. No outcome
would itself decide actual clipping, L413's regulator margin, global
mixed positivity or RH. Full matching Mathlib coverage remains unchecked;
generic calculus, Haar integration or matrix support would not be a
formalization of this complete moving-law comparison.
