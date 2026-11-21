# Five-node head-annihilator test: source review2203

TARGET: Review source coverage and duplicates for the fixed five-node model with alpha=(57/4,21,25,101+i/4,101-i/4), testing H_(2,r)>0 for every integer r>=4 against Q(X^r P)<0 for some integer 4<=r<=1000, where P annihilates the three real beta=alpha^(-2) nodes.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2203 searched finite complex moments, shifted Hankel dominant nodes, Hermite quadratic forms, fixed-size all-shift power-sum positivity and the exact 57/4/101 nodes; narrowly checked local C919e/h, L030/L032/L057/L839 and recorded finite-Hankel/strip/weak-Toeplitz failures. No exact duplicate was identified in this bounded search; this is not a novelty claim. Primary statements and relevant proof cases actually read are recorded below.
SOURCE_EVIDENCE: Nathanson1911.01745v2 Lemmas1-2/Theorem1 and full conjugate-pair proof, pp2-3; Berg-Szwarc July9,2014 manuscript Theorem1.1/Remark1, pp1-2; Gautschi1975 Section3(3.1)-(3.4), p339; Boyd-Vandenberghe2004 corrected seventh printing2009 A.5.2, pp646-647, with reused A.1.1/A.1.5/A.5.4 and Section2.2.5; Arellano-Pena September30,2026 preprint Theorem12.1/proof p33 and Section12.4(12.14) pp35-36, comparison only. Precise primary links and scope are below. C919e's accepted real-box margin is reusable, subject to checking the explicit model hypotheses.
COMPARISON: Hermite-Sylvester and L032 cover unrestricted polynomial detection, not the prescribed cubic-times-monomial witness. Finite-prefix countermodels, including the inspected preprint, do not assert one frozen five-node model passes every r>=4. Berg-Szwarc requires all degrees of leading determinant data. L839 concerns weak coefficient-Toeplitz rays. Published finite-matrix/interpolation methods cover the ingredients, leaving the frozen all-r margin and exact witness sign as local specialization obligations.
GAP: Neither frozen sign assertion is proved or calculated here. No essential unread source is needed for this bounded finite-method test; an exact theorem giving both assertions was not found. Actual-Xi realization, shift removal and arbitrary-degree positivity remain open. Full matching Mathlib coverage is unchecked.
REASON: Complete the required new-target review once, reuse ready finite-matrix coverage and permit one separate known-method specialization attempt. The purpose is a bounded diagnostic of the restricted shifted family, not a new real-root criterion or an RH claim.
SCOPE: Exactly the COVERED_TARGET below, for one later RESEARCH calculation classified REPRODUCTION after the supervisor's separate continuation approval. Retain five opposite classes once each, both conjugate occurrences, algebraic squares, all integers r>=4 and witness range4..1000. No parameter tuning, actual-Xi inference, old source retry or new theorem reproof. Source approval does not establish either sign.
COVERED_TARGET: Test the frozen five-node model alpha=(57/4,21,25,101+i/4,101-i/4) by proving H_(2,r)>0 for every integer r>=4 and certifying Q(X^r P)<0 for one integer 4<=r<=1000, where P annihilates its three real beta=alpha^(-2) nodes; stop on either failed condition without tuning.
LITERATURE_REASON: The saved next target was REVIEW_REQUIRED and changed from auditing actual-Xi C919h to a common finite model with an all-shift quantifier and a restricted annihilator witness; the ready C919h audit assessment did not cover it.

## Original nomination2202: gap, proposed test and downstream use

The main gap is L030-L032/C032a positivity for every real polynomial
at the actual Xi nodes. C919h has passed its separate audit only
for X^r p with deg p<=2, r>=4, at time0. The target above asks
whether this entire fixed-degree shifted family can miss a
specific nonreal packet once its three real dominant nodes are
annihilated. This is a finite model question, not a proposed Xi law.

Define exactly five alpha representatives as in TARGET, with each
occurring once, and beta_j=alpha_j^(-2). For this model alone set

    S_m=sum_(j=1)^5 beta_j^m,
    Q(q)=sum_(j=1)^5 beta_j^2 q(beta_j)^2,
    H_(2,r)=(S_(2r+i+j+2))_(0<=i,j<=2),
    P(X)=product_(j=1)^3 (X-beta_j).

The associated formal product for comparison is
F(z)=product_(j=1)^5(1-z^2/alpha_j^2). Its real-coefficient/even
conventions, multiplicities and finite-sum normalization must be
checked locally if a later test is approved. Do not apply a theorem
stated only for actual Xi to this product. In particular Platt2017,
the C919f theta signs and Bellotti-Wong's actual zeta count are not
model hypotheses or sources of model zero information.

One later frozen test would require both a proof for every r>=4
of H_(2,r)>0 and one exact negative value Q(X^r P) with integer
4<=r<=1000. Samples cannot establish the first condition; a phase
plot or floating-point negative cannot establish the second. The
infinite-shift argument would need a finite real head bound and a
complete bound on the two model exterior occurrences. C919e can be
used only after checking its explicit box hypotheses. The cubic
annihilator and both conjugate occurrences must be evaluated in
the algebraic convention. No calculation has been run for these
proposed conditions in step2202.

Continue if source review finds an exact import or adequate methods
for this unmatched finite test without a previously proved identical
counterexample. If approved mathematics later supplies both
conditions, it would obstruct a generic all-shift-H2 completion and
identify head cancellation as a useful higher-degree diagnostic.
Failure of either frozen condition ends this test without changing
nodes or increasing the witness bound. A duplicate should be imported
or the nomination stopped, not rederived to create a result. Even
success leaves actual-Xi realization and all-degree signs unresolved.

## Comparison of three possible continuations

1. More cutoff/onset tuning within C919h changes its numerical margin
   but supplies no new shift-removal or degree-uniform input. Its
   frozen assembly is accepted; repeated scope reviews are closed.
2. A backward-shift inference from finite Hankel positivity would
   need additional signed minors or a new actual-Xi estimate. L057
   and the preserved finite-extrapolation stop prevent using finite
   tests alone. No independent closing hypothesis is presently supplied.
3. The selected head-annihilator model asks a different falsifiable
   question: simultaneous strict positivity on an infinite shifted
   family versus a specific higher-degree negative witness. L032
   motivates detection but does not give the requested restricted
   witness or the simultaneous positive family as stated. This option
   uses finite exact data and requires no inaccessible infinite-source
   theorem. It is selected for separate source coverage, not proved here.

Essential future input is C919e and the finite analogue of L030's
definitions; C919h is comparison context, not an actual-Xi hypothesis
for the model. L032/L057 and L839 are duplicate/obstruction comparisons;
L839's recorded canonical stop was read, not its full proof. Reuse the
ready finite real matrix sources where their hypotheses match. Search
primary results under shifted Hankel dominant nodes, finite complex
moment functionals and polynomial annihilation; inspect hypotheses
and the relevant conjugate-pair cases before longer extracts. Any
unread exact result remains a lead, not coverage. Full Mathlib matching
is unchecked. There is no cross-notebook input or new source blocker.

No protected creative actual-Xi proof attempt is nominated merely to
meet a scheduling preference. A noncircular actual-theta estimate that
survives cancellation of the real head is still missing. This bounded
obstruction can clarify the needed hypothesis; it does not supply it.

## Completed source comparison2203, 21 November 2026

This literature-only step makes the finite-method scope ready. It does
not evaluate a model moment, prove a new inequality, certify a witness,
or accept either proposed sign. The original nomination above is retained.
The outcome is EXPLORATION: a new source/duplicate comparison, with no
mathematical advance or informative negative for the frozen assertions.

### Primary statements and relevant proof cases inspected

Melvyn B. Nathanson, *The Hermite-Sylvester criterion for real-rooted
polynomials*, arXiv:1911.01745v2, 24 November 2019, Lemmas1-2 and
Theorem1, pp2-3:
https://arxiv.org/pdf/1911.01745v2 . The PDF is the version used for
this comparison; its internal date is November26,2019, while the HTML
rendering displays an inconsistent 2026 date. Theorem1 concerns a
nonconstant real degree-n polynomial, its n roots with multiplicity,
and the n-by-n unweighted power-sum Hermite form. Positive semidefiniteness
is equivalent to all roots being real. Lemmas1-2 and the complete proof
were read: interpolation at distinct conjugation-closed roots produces
real coefficients, values i and -i on the selected pair, and zero at
the other roots. The proof retains equal conjugate multiplicities and
uses algebraic squares. This is the standard detection method, not a
theorem prescribing X^r P or its exponent. Its unweighted full-degree
form must not be identified with the shifted 3-by-3 matrix. Any use of
its method with beta^2 weights needs an explicit later specialization;
do not reprove the imported theorem or substitute modulus squares.

Walter Gautschi, *Norm Estimates for Inverses of Vandermonde Matrices*,
Numerische Mathematik23 (1975), 337-347, Section3, p339, (3.1)-(3.4):
https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf .
Read the distinct-complex-node hypotheses and inverse derivation: inverse
rows are the coefficients of the Lagrange basis, for nodes arranged in
columns. This supports finite interpolation/real-head conditioning,
not the two requested signs. Reuse C919e's audited weighted real-box
bound after checking its three explicit box hypotheses. Section4's
infinity-norm convention is not a Euclidean-norm identity.

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge
University Press2004, corrected seventh printing2009:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf . Reopened A.5.2,
pp646-647, including the real symmetric spectral decomposition,
Rayleigh quotients and matrix-order definitions. Reuse ready2161/2170
coverage of A.1.1 pp633-634, A.1.5 p636, A.5.4 pp648-649 and
Section2.2.5 pp34-35. These cover finite real Gram order, invertible
congruence and norm comparisons. A later proof must first show that
the paired complex error is real symmetric; individual complex algebraic
outer products are not positive Gram matrices. The sources supply no
model-specific margin or all-shift sign.

Christian Berg and Ryszard Szwarc, *A determinant characterization of
moment sequences with finitely many mass-points*, author manuscript
dated July9,2014, Theorem1.1 and Remark1, printed pp1-2:
https://math.uni.wroc.pl/~szwarc/pdf/berg-szwarc.pdf . Read the real-sequence
theorem and its qualification: positivity of every leading determinant
below an index n0, followed by zero determinants at every larger degree,
implies a unique positive real measure with n0 support points. Remark1
distinguishes strictly positive leading minors from merely nonnegative
ones. These are all-degree hypotheses, not positivity of one fixed
matrix size at many shifts. The theorem supplies neither frozen sign;
its unavailable higher-degree hypotheses cannot close this target.
No proof or specialization of this nonapplicable theorem is needed.

Henry Arellano-Pena, *Moment and Prime-Trace Criteria for the Riemann
Hypothesis, with Spectral Exclusions and Nonlocal Positivity*, preprint,
6 September2026, amended30 September2026, DOI10.13140/RG.2.2.22856.07682,
Theorem12.1 and proof, p33, and Section12.4, (12.14), pp35-36:
https://www.researchgate.net/publication/414031680_Moment_and_Prime-Trace_Criteria_for_the_Riemann_Hypothesis_with_Spectral_Exclusions_and_Nonlocal_Positivity .
Read the author-posted statement, finite-prefix perturbation proof and
the shifted-tower comparison, rather than relying on the search excerpt.
This preprint is comparison evidence only, not an imported premise.
For each finite cutoff it changes the distant conjugate packet to keep
the finite prefix positive. The later comparison treats two towers and
a finite degree prefix; it does not claim simultaneous positivity for
all monomial shifts at a fixed size in the single displayed five-node
model. Its normalization differs, and no quantitative constants or
claims about preserving zero counts are imported. This overlaps L057's
general warning, not the frozen common-model test. No inference of
originality follows from the difference.

### Bounded searches, local duplicates and unused leads

Queries included “finite complex moment Hankel matrix positive definite
nonreal nodes polynomial annihilating real nodes shifted moments”,
“Hermite quadratic form power sums real roots signature conjugate pairs
theorem”, “shifted Hankel dominant nodes”, “Hankel matrices fixed size
all shifts nonreal roots power sums positive counterexample”,
“57/4 101 Hankel”, and “power sums nonreal shifted Hankel positive”.
Additional conjugate-pair/dominant-node searches did not identify an
exact import. Failure to locate a result is not evidence of novelty.

Local searches were restricted to this notebook's lemmas, relevant
shifted/Hankel/head assessments and failure records. Read L030/L032/L057,
C919e and L839, the scope records2200/2201, the relevant C919h statement
and head method, and the finite-Hankel/strip/weak-Toeplitz stops. Exact
node/head-annihilator searches gave the nomination and its route-closure
record; unrelated numerical substring hits were excluded by inspecting
only matching lines. L032's unrestricted interpolation does not settle
the prescribed witness. L057's cutoff-dependent family has different
quantifiers. L839's coefficient Toeplitz rays, weak signs and tied-modulus
example are different observables. The small-angle strip failure remains
a warning about algebraic squares. No stop is treated as a global ban.

The Basu-Pollack-Roy author PDF timed out; it is an unused optional
Hermite-form lead, not an essential blocker, since the inspected
Nathanson theorem/proof supplies that comparison. Search hits on
Hadamard preservation, total positivity, quasi-complex truncated moment
representations and finite-source reconstruction were not read as
theorem inputs; none is claimed as coverage. No retry of the earlier
blocked infinite-Toeplitz route was undertaken. Full matching Mathlib
coverage remains unchecked, with no claim of absence.

### Approved specialization obligations and limits

The COVERED_TARGET preserves the original mathematical proposal while
replacing its review verb by one executable test. Its hypotheses are
exactly the five alpha representatives occurring once, beta=alpha^(-2),
the displayed finite S/Q/H definitions and the fixed monic cubic P.
The formal product is only a model; a later proof must check the even,
real-coefficient and opposite-class conventions without importing Xi
zero information. Essential mathematical local input is C919e after
explicit box checks and the finite algebraic convention of L030.
C919h is method/comparison context; L032/L057/L839 are duplicate and
failure comparisons, not premises for either proposed sign. There is
no cross-notebook input.

Known finite-matrix methods cover the real-head estimate and the
finite conjugate-pair error calculation. What remains is to establish
a strict comparison at the frozen onset and justify its validity for
every integer r>=4, then test the prescribed cubic witness with exact
arithmetic on the fixed finite range. These are future proof and
arithmetic obligations, not conclusions of this review. A finite sample
of shifts cannot discharge the first obligation. A rounded phase or
negative floating-point number cannot discharge the second. A general
interpolated witness is not a substitute for X^r P.

One later calculation may use exact rational/rational-complex arithmetic
and a written uniform bound, citing the imported finite-matrix facts.
If a script is used, retain its full certificate on disk: model and
normalization, all conjugate occurrences, denominator checks, head/error
operands, actual and required margins, uniform extension justification,
selected exponent and exact negative value, and every failure. Print
only the result, bounds, failures and paths. Correct CPython/Fraction
arithmetic must remain an explicit computational assumption if used;
C919f's Decimal/actual-theta contracts do not transfer to this model.
No new lemma or mathematical script was written in this source step.

Pass requires both frozen assertions with complete evidence. An exact
failure of either assertion rejects this model test. A failed chosen
bound is only an inconclusive method failure and ends that bounded
attempt without asserting the underlying sign false. Exhausting the
exact witness range without a negative also ends the test. Do not move
nodes, increase the range or substitute another witness in that turn.
Success would diagnose a limitation of the restricted shifted family;
actual-Xi realization and all-degree positivity would still be open.
This is routine known-method specialization, not a creative central
proof attempt. The missing actual-theta estimate surviving real-head
cancellation still blocks a justified creative nomination. The ready
continuation is recorded for separate supervisor approval next turn.
