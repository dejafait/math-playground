# Source comparison: exterior-delay completion of the neutral primitive symbol

TARGET: Assess a fixed eight-delay positive-symbol completion of the two-moment primitive Weil form at T=4log(3), including an independently checkable feasibility or dual-obstruction certificate.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step866 completed scoped duplicate/failure checks and primary searches for interval positive-definite extension, positive-definite distributions, semi-infinite finite-support duals and exact Weil/exterior multiplier completion. Inspected primary hypotheses and the relevant positivity/dual proof cases below; no matching quantitative eight-delay result was located, and no novelty inference follows.
SOURCE_EVIDENCE: Reuse assessment557's inspected Teschl GSM99 Section9.1/Theorem9.1/Lemmas9.2/9.4, https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf ; new inspection of Jorgensen-Niedzialomski1212.3047v1 Theorem1.1/Lemma2.1/Corollary6.2 and interval proof, https://arxiv.org/html/1212.3047v1 ; Jorgensen-Tian1712.07264v1 Theorem2.1/Corollary2.2/Remark2.3, https://arxiv.org/html/1712.07264v1 ; Basu-Martin-Ryan9April2014 Section1 pp2-3/Theorem2.4/Example3.5 pp8/10-11, https://www.ams.jhu.edu/~abasu9/papers/finite-support.pdf ; DLMF1.14.1/1.14.5-8, https://dlmf.nist.gov/1.14 ; L744(6)-(8), C750a and ready scalar-enclosure assessment861 are reused.
COMPARISON: Known range/Fourier results supply the representation machinery, not a signed gain. Interval extension assumes local positive definiteness and does not prescribe eight exterior atoms or an absolutely continuous spectral density. Haar weak duality supports a sufficient finite negative certificate; no infinite strong alternative is needed or imported. No inspected theorem decides the complete fixed symbol.
GAP: The smooth primitive specialization, exact exterior-annihilation identity, coefficients and global sign or an exact finite negative functional remain mathematical obligations. Source coverage now suffices to attempt these within the fixed family; no bound, coefficient, tail cutoff or identity was derived during this review.
REASON: Completed one literature-only comparison of the saved target. Nominate the unchanged fixed-family mathematical test separately in assessment866; its later approval is separate from this completed work. Do not import missing positivity or retry the audited coarse screen.
SCOPE: Only I=(0,T), T=4log3, C750a's complete31-term symbol, complex C_c^infinity primitives and eight prescribed delays T,...,8T. No weighted-domain extension, extra constant term, window/delay/threshold sweep, RH, complement positivity, H2-prime premise or Xi realization.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED coverage lacked the precise interval-extension assumptions, finite-certificate logic and comparison for this changed signed mechanism; ready range and scalar coverage were reused instead of repeated.

The original nomination below is preserved; its pending-review wording is
historical and superseded by the completed comparison866 at the end.

## Main gap and three-way route comparison

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
One quantitative positive form certificate on this fixed neutral window
could supply a local input toward unrestricted Weil positivity. It would
still leave all larger windows, non-neutral pole directions, assembly,
critical-line signs and actual-Xi realization unresolved.

Three mechanisms were compared only to choose a continuation:

1. Full weighted observation instead of C750a's level1/-M payment.
   It retains information the coarse screen loses, but the existing
   Logvinenko-Sereda/prolate coverage in reviews860/861 provides no
   quantitative complete signed payment. No independent estimate is
   presently specified; do not relabel the failed screen or tune its f.
2. Positive Sonin trace with its arithmetic correction. Completed
   review860, retained in assessment859, records the uniform H2-prime
   tail and finite conditioning still required. There is no new input
   removing those assumptions. Park this dependent route without
   repeating source-access attempts or declaring a global ban.
3. Exterior-delay completion after exact two-moment coordinates.
   This asks for an explicitly testable scalar certificate preserving
   the entire transformed form, rather than obtaining a gain merely
   from invertible coordinates. Select this question for source review.

The narrower duplicate checks were assessment557 (two-moment Green
coordinates), assessment623's positive-extension hypotheses, and
assessment854's metric warning. Teschl's standard representation is
not new; the prior Green/RKHS metric did not pay the actual signed form.
The reflection-extension source assumes a positive measure/form, so
cannot simply supply the sign sought here. No exterior-completion
result was found in those selected records; this is not an assertion
of absence from the literature. C759d's shifted Schur stop and the
even-resolvent stops822/823 were also checked for scope: neither is a
premise for, or a computation of, this pointwise completion.

## Exact proposed test, entirely unproved here

Use C750a's w, including all prime powers below 81 and its digamma term.
The proposed primitive relation and proposed scalar family are

    f=(d^2/dx^2-1/4)u,  u in C_c^infinity(I;C),
    H_b(t)=(t^2+1/4)^2 w(t)+sum_(k=1)^8 b_k cos(k*T*t),
    b=(b_1,...,b_8) in R^8.

These formulas define the question; this nomination proves neither
surjectivity onto the smooth two-moment class nor equality of the
proposed transformed form with the original one. Review and justify
both directions of the range statement, compact support, Fourier
normalization and integrations by parts. Do not silently replace the
logarithmically weighted form by an ordinary Sobolev norm.

The intended new mechanism is to seek a nonnegative representative
by corrections whose translations have no overlap on I. The review
must check that this proposed annihilation survives the precise
primitive formulation, endpoints and full quadratic pairing. It must
also identify relevant known completion/positive-distribution results
and their positivity assumptions before approving a constructive test.
An abstract extension theorem assuming the missing sign is insufficient.

The bounded mathematical test, if later approved, is exactly one of:

- Exhibit eight certified coefficients and prove H_b(t)>=0 for every
  real t, with interval bounds on the necessary finite range and an
  explicit rigorous tail. A grid or optimizer output does not suffice.
- Exhibit a finite positive evaluation functional annihilating all
  eight cosine corrections, with rigorously negative value on the
  complete base multiplier; verify its exact annihilation and its
  implication for infeasibility for every real b in this fixed family.

This is a proposed primal/dual acceptance test, not a derived duality
lemma. The source review must justify the certificate logic. A failed
numerical search or overlapping bounds is inconclusive, not infeasibility.
No further delay, period or coefficient-family sweep is preauthorized.
Retain the complete multiplier: no prime-only, modulus, coarse-level,
positive-complement or omitted-tail surrogate is permitted.

Continue after the review only if it covers these precise obligations
and identifies a noncircular, independently checkable finite certificate
with its analytic tail, or a decisive obstruction certificate. Otherwise
record the particular missing premise and park this family. Coordinate
identities alone do not pass this continuation test.

## Routing and qualifications

Immediate action is literature_comparison/standard/high, because this
new scalar completion and its obstructions are outside the approved
audit scope. Reuse assessment557's representation coverage where its
hypotheses suffice; retrieve only essential primary theorem/proof cases
and check duplicates before approving any subsequent mathematics.

If source comparison supports this as a new signed mechanism, the later
attempt can be proof_attempt/creative, deep_research/max. Its escalation
would be the missing complete signed payment after the audited coarse
screen failure; the bounded decisive test is a globally nonnegative
H_b or an exact finite annihilating negative functional for this one
eight-delay family. Source overlap may instead require REPRODUCTION
and ordinary calculation routing. No creative task is approved merely
to satisfy the scheduling preference.

Essential mathematical input IDs for the proposed specialization are
L744 and C750a; L750 supplies witness history only, not a new sign premise.
The range theorem, exterior-annihilation identity and quantitative
completion are unresolved obligations. All31 arithmetic terms, both
exponential moments and whole-real-line errors must be retained. No RH,
H2-prime tail, complement positivity, cross-notebook input or Xi
realization is assumed. Full matching Mathlib coverage has not been
checked. This new assessment remains REVIEW_REQUIRED; the completed
audit865 is independent of its later approval or outcome.

## Completed comparison866 — 14 November2026

Outcome: EXPLORATION, LITERATURE/NOVELTY_UNCHECKED. This is new source
comparison, not a new mathematical input or a sign calculation. There
is no RH candidate. No lemma, script, DAG or PROOF change is warranted.

### Primary inputs and exact scope

**Range: reuse, without another source retrieval.** Assessment557's
completed comparison558 inspected Teschl, *Mathematical Methods in
Quantum Mechanics*, GSM99, author PDF dated12February2009,
Section9.1 pp181-185, Theorem9.1 and Lemmas9.2/9.4, including the
compact-support inverse and regular-endpoint proof cases. The relevant
case is p=r=1,q=1/4, with the sign of the differential expression
reversed. Its two homogeneous solutions, regular endpoint traces and
smooth-source regularity must be specialized explicitly in the later
attempt. Only smooth compact supports are sought here; no inverse
boundedness in a logarithmically weighted completion is needed or
licensed. The earlier covariance/metric gap remains valid for its
different target; this nomination adds a signed completion test rather
than reopening a bare coordinate rewrite. No range theorem is reproved
or specialized mathematically in this turn.

**Fourier normalization and support.** Directly inspected
[DLMF1.14](https://dlmf.nist.gov/1.14), definition1.14.1,
convolution1.14.5 and the adjoining L1 hypothesis, and Parseval
1.14.6/7/7_5/8 with the L1-intersect-L2 hypotheses. DLMF uses the
positive exponential and factor1/sqrt(2pi); the notebook uses the
negative exponential and unnormalized transform. Smooth zero
extensions meet the stated integrability assumptions. Later work must
track this convention, conjugation, derivatives and both translated
supports when specializing the paired identity. L744 already uses
the derivative identity on this smooth class. No support-annihilation
formula is proved here. In particular an atom at T must be checked
using compact support strictly inside I, not an unsupported endpoint
assertion. The complete logarithmic multiplier must remain in the
integral; ordinary Sobolev positivity would not replace it.

**Positive extension is conditional and has the wrong prescribed
class.** Directly inspected Jorgensen–Niedzialomski,
[*Extension of Positive Definite functions*,1212.3047v1,
13December2012](https://arxiv.org/html/1212.3047v1),
Theorem1.1, Lemma2.1's positivity/Cauchy–Schwarz step and Corollary6.2's
interval proof. Theorem1.1 equates continuous-kernel positive
definiteness with all compact-test quadratic signs. For an interval,
Corollary6.2 extends a continuous positive-definite kernel to the line;
its proof uses the already positive kernel Hilbert space, reflected
conjugation and a self-adjoint extension. These hypotheses cannot
establish the presently missing local sign. The theorem also does not
restrict an extension to eight atoms outside the interval or require
its spectral measure to have the prescribed density. Only its interval
case is relevant; no assertion about disconnected sets is imported.

For the distributional alternative, inspected Jorgensen–Tian,
[*Positive definite (p.d.) functions vs p.d. distributions*,1712.07264v1,
19December2017](https://arxiv.org/html/1712.07264v1),
Theorem2.1(a)-(c), Corollary2.2 with its short referenced proof, and
Remark2.3. The distributional representation still assumes positive
definiteness on convolution squares. The local-extension corollary
explicitly assumes local positivity and invokes JPT16, rather than
deriving it from signed data. No prescribed exterior support or finite
parameter family is provided. That underlying reference was not
inspected anew and is not an essential or imported theorem here: this
route is excluded as a source of the missing sign on its stated
hypotheses alone. No distributional identification is claimed.

**Finite certificate, without a strong-alternative assumption.**
Inspected Basu–Martin–Ryan,
[*On the sufficiency of finite support duals in semi-infinite linear
programming*, author PDF dated9April2014](https://www.ams.jhu.edu/~abasu9/papers/finite-support.pdf),
Section1 pp2-3: arbitrary index set I, unrestricted finite-dimensional
primal, pointwise nonnegative cone, algebraic adjoint, and nonnegative
finite-support Haar dual. Read the Lagrangian derivation including the
zero-adjoint requirement for a finite lower bound. This supplies weak
duality for a proposed finite positive evaluation certificate without
compactness, dual attainment or strict feasibility. Theorem2.4 and its
proof, p8, concern countable constraints and equality of two dual
values; they do not assert equality with the primal. Example3.5,
pp10-11, gives a feasible primal with value0 and infeasible finite
support dual; read the feasible family, limit bound, and dual constraint
argument. Thus finite certificates are sufficient evidence when found,
not an exhaustive solver guarantee. Its example is a duality-gap
warning, not a counterexample to this eight-delay family.

**Validated values and tails: reuse.** Assessment861 (completed and
source-link-repaired862) covers Johansson1802.07942v1 Section2's direct
ball/box integration contract and the scalar digamma recurrence/series
and sector remainder. C750a and L744(8) already record the complete
symbol and scalar bounds. Those sources support validated values of
the later proposed certificate; no old frequency boxes, implementation
output or floating-point margin transfers automatically. A primal
certificate needs a new full finite-range enclosure and an explicit
analytic tail using the existing scalar bound. A finite dual certificate
instead needs only its finitely many complete values and exact
annihilation; it does not discard a frequency tail of the quadratic
form. These are certification requirements, not performed calculations.

### Search, duplicates and source limitations

Queries included `Krein positive definite extension interval theorem
Jorgensen Niedzialomski`, `positive definite distributions extension
interval Bochner Schwartz Jorgensen Tian theorem`, `semi infinite linear
programming finite support dual certificate infeasibility positive
measures`, `exterior Weil positive multiplier completion`, and
`positive completion cos semi-infinite trigonometric polynomial`.
The last two produced no matching inspected theorem. This bounded
search establishes neither novelty nor absence of other relevant work.

Compared assessment557's range/metric warning, assessment623's
positivity-dependent reflection extension, assessment854's IMS/Schur/
wavelet comparisons, assessment861's fixed-witness certification, and
stop863/audit865. The local search for exterior-delay and semi-infinite
completion in neutral/signed assessments and stop records found no
previous certificate for the proposed H_b. The nonmatching finite
Schur and even-resolvent stops remain evidence against their own
families, not premises or bans for this one. No arithmetic envelope,
zero-free region or cross-notebook theorem is being reopened.

Boyd–Vandenberghe's Stanford *Convex Optimization* PDF timed out twice
through web retrieval, and a direct shell request failed DNS. It was
not read and is not cited as theorem evidence; accessible Basu–Martin–
Ryan supplies the necessary finite-certificate logic. Akutowicz1959 and
the Jorgensen–Pedersen–Tian extension monograph were search leads only,
not additional theorem inputs. There is no persistent essential source
blocker for the bounded test. Full matching Mathlib coverage remains
unchecked; supporting Plancherel coverage is not a verified full match.

### Decision and continuation test

EXPLORE permits a separate, bounded attempt on the fixed family, after
separate approval of [assessment866](2026-11-14-neutral-exterior-delay-certificate-866.md).
The sources support its logic without supplying its answer. The
specialized primitive and exterior-annihilation proofs remain work for
that mathematical turn, not results silently approved here. In a dual
branch, failure of the scalar family can be decided without assuming
surjectivity or positivity of any Weil form; its downstream interpretation
must remain limited accordingly.

Continue only with a rigorously global primal sign and paid tail, or a
strictly negative finite positive functional with every cosine exactly
annihilated. Approximate residuals cannot control unrestricted real
coefficients. If neither certificate closes in the single attempt,
record the precise unpaid obstruction and preserve the partial work;
no automatic delay/window/constant-term sweep is authorized. An
infeasible completion would stop only this sufficient representation,
not prove negative neutral energy or disprove RH. A feasible one would
still leave all larger windows, non-neutral directions, assembly and
actual-Xi positivity unresolved. No mathematical exploration counter
is spent or reset by this source turn.
