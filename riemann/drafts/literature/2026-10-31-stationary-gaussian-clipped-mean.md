# Stationary Gaussian clipped mean: completed source comparison

TARGET: Determine whether E[(G(0)G''(0)-G'(0)^2)_+] exceeds 1/288 for the centered stationary Gaussian process with covariance r(t)=integral_{-1/2}^{1/2} cos(ut) du.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched stationary Gaussian Laguerre inequalities, sinc-process quadratic forms, positive-part/partial moments of indefinite Gaussian quadratic forms, Pinelis Fourier-Laplace formulas and Imhof inversion; checked the specific local inputs and scoped failures below. Located general exact formulas, but no inspected source evaluates this particular 1/288 comparison. No novelty conclusion follows.
SOURCE_EVIDENCE: Read Feldheim et al., arXiv:1801.10392v2, Section 2, pp.2--3; Pinelis, arXiv:0902.4214v2, Corollary 2 (4)--(6), pp.3--4 and its integer-case proof pp.8--9; Imhof, Biometrika 48 (1961), Section 1 (1.1), p.419, Section 2's finite-expression hypotheses and Section 3's inversion/error discussion, pp.420--423; Broda--Arismendi Zambrano, September 2019 manuscript, Theorem 1 and proof, manuscript pp.2--4 (PDF pp.4--6). Exact citations, limits of inspection and applicability are below.
COMPARISON: Smooth Gaussian jets and finite-dimensional quadratic-form/positive-part formulas are known inputs. Their composition reduces the saved target to an ordinary finite-dimensional specialization, whose exact value or certified threshold interval remains uncomputed. The full bounded-path import failure, L590's certificate-family obstruction and L424's corrected-law transport stop do not decide this scalar mean.
GAP: Specialize the existing K_0 normalization, apply the cited real Gaussian quadratic-form and positive-part formulas, and certify the comparison with 1/288. No general expectation theorem needs reproving. Bounded periodic approximation, strict finite-C_I reserve, fourth/probability assembly and actual-Xi transfer remain independent gaps.
REASON: Essential source coverage is now sufficient for this unchanged scalar target; import the general results and perform only the explicit three-coordinate specialization in a later mathematical turn. This is source approval, not evaluation, a new theorem or a realization result. The changed ready assessment receives separate next-turn supervisor approval before invocation.
SCOPE: Only the exact scalar expectation for the stated centered stationary real Gaussian process and its first two derivatives. No actual-Hardy Gaussian limit, hard support bound, periodic sample path, moment-matching theorem, or larger storage family is assumed.
LITERATURE_REASON: At turn start this new Gaussian clipped-expectation target was REVIEW_REQUIRED and outside the ready L590 audit assessment; primary nonlinear-expectation and Gaussian-jet coverage was essential and unread. This turn completes that coverage, without further research or repeated review of a ready target.

The original nomination below is retained as the pre-review record. Its
REVIEW_REQUIRED language is superseded by the completed comparison at
the end of this file; its mathematical target and stopping test stand.

## Main gap, possible use and bounded decision

The main gap remains actual-Xi all-degree positivity at unbounded
heights. A stationary surrogate with sufficiently large clipped mean
could provide a candidate bulk for a later derivative-consistent
moment-feasibility test; it would not determine any actual-Xi sign.
This is a possible downstream use, not a claim of feasibility.

The proposed numerical threshold is exactly 1/288. After source
approval, a mathematical attempt should give an exact value or a
rigorous interval lying wholly above that threshold or at/below it.
Sampling alone cannot pass the test. A value at/below the threshold
stops this fixed Gaussian bulk. A value above it only justifies a
separate bounded-periodic-approximation target; its covariance reserve,
support and fourth/probability obligations still require proof.

The immediate next turn must check primary Gaussian-process derivative
hypotheses and primary results for positive parts of indefinite
Gaussian quadratic forms, including possible exact formulas. Preserve
the displayed mathematical TARGET while doing that literature-only
comparison. Import a matching result if found; otherwise identify the
precise uncovered scalar specialization before approving calculations.
No integral, covariance specialization or new lemma is derived here.

## Local comparison and retained stops

Use L473's formula (6) and same-height block, and L586's exact ordinary
jet and spectral normalization, when assessing applicability. The
ready L590 audit concerns another target and cannot authorize this one.
Its class-wide obstruction remains in force.

The [stationary-process import stop](../../ATTEMPTS/2026-10-31-stationary-hardy-process-import-stop.md)
specifically retains unbounded Gaussian support and missing fourth
constraints. This narrower scalar target does not reopen direct
substitution for that full realization problem. The prior
[source assessment](2026-10-31-stationary-hardy-path-feasibility.md)
is partial evidence to reuse, not automatic approval of the present
positive-part expectation.

The [Gaussian-damped trajectory stop](../../ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md)
concerns the actual-response transport integral and its corrected
finite-law covariance and basis transitions. Its failure is preserved;
the present nomination does not repeat its unvalidated phase samples.
The separate covariance-stability assessment was inspected only to
distinguish that target's scope. No theorem from it is imported here.

Full matching Mathlib coverage is not checked. This assessment is
REVIEW_REQUIRED: it neither declares the target novel nor approves
its calculation. Essential source gaps, including duplicate and
stronger-result comparison, remain for a separate turn.

## Completed primary-source comparison, 2026-10-31

### Gaussian process and ordinary derivative convention

Reuse the stationary-Hardy assessment only for its already inspected
scope and retained support failure. Reopened Naomi Feldheim, Ohad
Feldheim, Benjamin Jaye, Fedor Nazarov and Shahaf Nitzan,
*On the probability that a stationary Gaussian process with spectral gap
remains non-negative on a long interval*,
[arXiv:1801.10392v2, 21 October 2018](https://arxiv.org/pdf/1801.10392v2),
Section 2, pp.2--3. It states existence for sufficiently decaying finite
symmetric spectral measures, and compact-support analytic regularity,
joint Gaussianity of ordinary derivatives and the derivative spectral
norm identity. Its convention is exp(2*pi*i*x*y). Use the pushforward of
the TARGET's angular spectral measure under u -> u/(2*pi); no spectral
gap is required for these Section 2 facts. The paper's persistence
theorem requires a gap and is not imported. Its classical reference is
Belyaev (1959), not separately inspected here. This review imports the
stated compact-spectrum facts, not a new regularity proof.

The local normalization is already recorded in L473 (6)--(7) and L586
(1), including ordinary rather than factorial-divided derivatives and
the negative value/second-derivative covariance. No new Fourier-moment
integration is done here. Future specialization must explicitly identify
the one-point covariance with that existing K_0, retain all correlations,
and justify any independent-normal representation. Finite Gaussian
polynomial moments meet the integrability requirement below; hard
support does not follow from compact spectral support.

### Imported nonlinear-expectation formula

Iosif Pinelis, *Positive-part moments via the Fourier-Laplace transform*,
J. Theoret. Probab. 24 (2011), 409--421,
[DOI 10.1007/s10959-010-0276-9](https://doi.org/10.1007/s10959-010-0276-9),
[arXiv:0902.4214v2, 5 January 2010](https://arxiv.org/pdf/0902.4214v2),
Corollary 2, (4)--(6), pp.3--4, covers any real X with E|X|^p finite.
In its p=1 case the source identity is

    E X_+ = (E X)/2
            + (1/pi) integral_0^infinity (1-Re E exp(itX))/t^2 dt.

This is a cited general formula, not an evaluated integral for the TARGET.
Read the proof on pp.8--9 through the integer odd-moment case: the
semicircle term supplies the half moment; the cosine remainder bound
and Fubini justify the real integral under the absolute-moment hypothesis.
The displayed PDF footer says June 22, 2021 despite its v2 title date;
the citation identifies the version and locations actually read.
No exponential-moment premise from Theorem 1 is needed for Corollary 2,
and no reproof or unchecked formal Fourier interchange is proposed.

### Quadratic-form reduction, exact formulas and numerical limits

J. P. Imhof, *Computing the distribution of quadratic forms in normal
variables*, Biometrika 48 (1961), 419--426,
[DOI 10.1093/biomet/48.3-4.419](https://doi.org/10.1093/biomet/48.3-4.419),
[published scan, UNIGE](https://access.archive-ouverte.unige.ch/access/metadata/4a7195a7-be6d-4605-8f1e-94ff4b638b8d/download),
Section 1 (1.1), p.419, reduces a real Gaussian quadratic form with
nonsingular covariance to a signed weighted sum of independent
noncentral chi-squares. The central case is included. Section 3,
pp.422--423, discusses inversion for indefinite as well as positive forms. The finite
formula theorem in Section 2, pp.420--421, has even-degree multiplicity
hypotheses and cannot be applied merely because a form is Gaussian.
The future three-coordinate application must check nonsingularity,
the real-symmetric matrix and its eigenvalue multiplicities. No values
are calculated in this review.

Equation (2.3)'s characteristic-function formula was located, but its
OCR was incomplete; no exact transcription or branch verification of
that formula is claimed. This is not an essential blocker for direct
integration under the Gaussian law. Any use of a characteristic-function
product must establish it by the elementary independent-normal integral
with its branch fixed at zero, rather than copy an unread OCR formula.

Section 3 separates truncation from quadrature errors; its practical
step-refinement comparison does not certify quadrature error. Therefore
an unvalidated Imhof implementation or agreement between resolutions
cannot certify the required threshold. The Pinelis formula or direct
Gaussian integration may be used instead with explicit error control.

For a stronger partial-moment comparison, read S. Broda and J. Arismendi
Zambrano, *On Quadratic Forms in Multivariate Generalized Hyperbolic
Random Vectors*, September 2019 manuscript,
[institutional PDF](https://assets.henley.ac.uk/v3/fileUploads/research/ICM-2020-03-Broda-and-Zambrano-mtime20200624135425_2020-10-14-083941.pdf),
Theorem 1 and its complete proof, manuscript pp.2--4 (PDF pp.4--6).
It gives the nth lower partial moment from derivatives of the
characteristic function, assuming a finite nth moment and continuity
of the distribution at the cutoff. Its general inversion integral is
improper, not automatically absolutely convergent. This is an alternate
known route, with an extra cutoff-continuity obligation; Pinelis suffices
without that extra premise. Theorem 6's generalized-hyperbolic statement
and displayed reduction were located on manuscript p.9; its supplementary
Lemma 5 proof was not inspected and is not imported. No limiting
generalized-hyperbolic argument is needed for this Gaussian target.

### Discovery, duplicates, failures and decision

Queries included `Pinelis positive part moments characteristic functions
p=1 absolute moment quadratic form Gaussian`, `Gaussian indefinite
quadratic form positive part expectation first partial moment Imhof`,
`stationary Gaussian Laguerre inequality`, `Gaussian process positive
part second derivative`, `sinc Gaussian process quadratic form`,
`partial moments quadratic forms Gaussian Broda`, and the exact Gaussian
observable/1/288 combination. They led to the primary formulas above;
no inspected result states this normalized comparison. This is bounded
coverage, not evidence of originality. Yueh--Wong (2010), *Analytical VaR
and Expected Shortfall for Quadratic Portfolios*, is a reference lead
identified through Broda, not an inspected theorem. It is not essential
to the approved Pinelis/Imhof specialization. Al-Naffouri--Hassibi's
2009 CDF paper was located at its introduction and real-case heading;
no real-case formula or complex-to-real specialization is imported.

Locally searched `drafts/literature`, `ATTEMPTS`, `foundations` and
`lemmas` for Imhof, Pinelis, positive-part moments and Gaussian clipped
or quadratic-form phrases. Read the two specific failure records linked
above, the stationary-path comparison, L473's hypotheses and (6)--(7),
L586's normalization/conclusion and L590's certificate scope. No matching
local scalar evaluation was found. L590 is a different sufficient-dual
family stop, and L424 concerns a different observable and corrected law;
neither is a negative result for this test. No broader historical ban
is inferred. Existing unfinished work is preserved.

The exact target remains unevaluated. SPECIALIZE covers a rigorous
finite-dimensional expectation calculation using the imported facts,
algebraic reduction and, if needed, certified integration. It does not
cover a new process-realization theorem or authorize proving one. No
source theorem is to be reproved: the only unperformed difference is the
explicit covariance/form specialization and the rational threshold
comparison. A later result is a reproduction/specialization of known
methods, with no established novelty. Full matching Mathlib coverage
and supporting formal Gaussian theorems were not checked; that is not
an absence claim.

Essential continuation inputs are L473 (6)--(7), L586's K/A/I
normalization, L590's retained scoped stop, and the cited compact-spectrum,
quadratic-form and positive-part facts. The decisive test remains an
exact value or a rigorous interval wholly above or at/below 1/288.
At/below stops only this fixed Gaussian bulk. Above permits nomination
of a separately reviewed bounded-periodic approximation question; it
does not prove a strict covariance reserve, fourth-moment/probability
assembly, any Hardy Gaussian limit or an actual-Xi sign. Intervals
straddling 1/288 remain inconclusive. No lemma, mathematical script,
target expectation or RH argument was produced in this literature turn.
