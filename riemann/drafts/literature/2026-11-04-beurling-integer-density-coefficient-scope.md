# Proposed source review: integer counting and the coefficient diagnostic

TARGET: Assess whether L735's coefficient-1 psi asymptotic is compatible with N_P(x)=kappa x+O(x^theta), kappa>0 and 0<=theta<3/4, by checking primary Mellin-continuation and logarithmic-derivative theorems with multiplicities.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 254 searched Beurling Axiom A, Mellin continuation, logarithmic-derivative residues and coefficient/zero-multiplicity necessity; inspected three primary chains (two Revesz papers and NIST DLMF). Scoped November 4 assessments and coarse-kernel failure records contain no earlier necessity specialization. Queries and inspected ranges below; no novelty claim.
SOURCE_EVIDENCE: Revesz arXiv:2202.01837v3 Section 1 (1)–(7) and endpoint footnote, Section 7 pp. 17–18 (52)–(54); Revesz arXiv:2110.11463, Definition 1.1 and (1.1)–(1.6), Lemma 2.1 (2.2),(2.4) and complete proof pp. 4–5; NIST DLMF 1.10(i),(ii),(iv), especially (1.10.1),(1.10.8),(1.10.9). Version qualification and exact links below.
COMPARISON: Inspected standard inputs cover formal multiplicities, Axiom-A continuation, the psi Mellin identity, power transforms, and integer zero orders. They permit a bounded necessity specialization; Theorem 8 remains an existence comparison, not a universal coefficient theorem. L735 itself assumes no integer-count regularity.
GAP: No exact matching coefficient-1 compatibility theorem was located. A separate mathematical step must assemble the inspected inputs, handle theta=0, endpoints and analytic remainder convergence, and compare the local logarithmic-derivative residue with a legitimate zero order. No compatibility verdict is proved in this literature turn.
REASON: Essential missing source coverage is resolved; specialize known analytic inputs rather than reprove discretization or infer necessity from a prescribed-zero construction. The diagnostic identifies a possible extra arithmetic constraint, without paying actual-prime prefix norms or Xi signs.

## Original nomination — step 253, preserved scope

Essential local input: audited L735, with b=3/4, coefficient exactly 1
and error O(sqrt(x)log x), counting formal generalized integers with
multiplicity. Define N_P(x) as the number of those formal integers of
norm <=x, including the unit. The new counting hypothesis is hypothetical;
it is not asserted for L735's system. Constants kappa>0 and theta<3/4
must be fixed, and compact endpoints and the unit must be retained.
If a source uses kappa(x-1), compare its exact remainder convention.

Begin with Revesz's primary definitions and analytic preliminaries,
following only a necessary cited theorem for the continuation or Euler
product statement. Search the exact coefficient/zero-multiplicity
necessity question and standard Beurling Axiom A terminology. Inspect
the theorem hypotheses and relevant proof cases, rather than infer a
necessity assertion from the prescribed-zero construction. At most
three relevant source chains are proposed for this review. Record
unread leads separately from inspected results and check exact overlap
before suggesting a local proof. No discretization reproof is needed.

The discriminating question is compatibility of these two asymptotic
statements for a single system. A documented standard necessity result
may settle the question; it must be imported with a precise citation
and only the justified specialization. If coverage is incomplete,
record the exact missing theorem; persistent source obstruction parks
this dependent target. Neither answer licenses another power sweep,
an actual-prime prefix bound, an arbitrary-zero exclusion or RH.

L734's fixed-kernel stop, L735's coarse self-generated-kernel stop and
L639's localization stop remain in force. This nomination changes the
hypothesis rather than a power parameter or route name. The relevance
is limited to identifying additional arithmetic structure missing from
the countermodel; a new central sign mechanism is still absent.
Mathlib coverage of the newly proposed necessity question is unchecked.

At step 253 this assessment was deliberately REVIEW_REQUIRED. That step
performed only the approved L735 audit. Step 254 completes the source
review below, without performing the new necessity specialization.

## Completed literature-only review — step 254

LITERATURE_REASON: The added N_P remainder hypothesis was outside all previously ready assessments; its essential continuation and zero-order inputs required this review. No repeat construction search is needed.

The precise main gap is unconditional actual-Xi mixed positivity. This
intermediate target tests an additional structural condition absent from
L735. A verdict could separate coarse multiplicative consistency from
integer-count regularity; independent upper-prefix, sign-transfer and
complementary-residual gaps remain. The bounded test is whether the
inspected analytic inputs apply in a neighborhood of b=3/4 with the
specified error and all endpoints. Stop the specialization if that local
coverage fails; do not replace the coefficient or sweep other powers.

### Primary input A: continuation proof

Sz. Gy. Révész, *A Riemann-von Mangoldt-type formula for the distribution
of Beurling primes*, [arXiv:2110.11463, requested v1 PDF](https://arxiv.org/pdf/2110.11463v1),
Definition 1.1 and (1.1)–(1.6), printed p. 2; Lemma 2.1,
(2.2),(2.4) and its complete proof, printed pp. 4–5.

Hypotheses: a locally finite normed free commutative semigroup with unit,
and |N(x)-kappa(x-1)|<=A x^theta for x>=1, kappa,A>0,
0<theta<1. The source gives zeta(s)=kappa/(s-1)+integral
x^(-s)dR(x), meromorphic for Re(s)>theta, with only the simple pole
at 1. The proof splits the finite and infinite Stieltjes integrals,
continues their common identity, and integrates the remainder by parts;
(2.4) bounds its tail by A(|s|+sigma-theta)X^(theta-sigma)/(sigma-theta).
The unit is included using the p. 2 footnote's 1-minus convention.

Version qualification: the abstract lists v1 (21 October 2021), but
both the unversioned and requested-v1 PDF retrieved on 2026-11-04 bear
a v2 footer and contain 29 pages. The exact inspected manuscript is
identified here by URL, pagination and equations; no assertion about an
unavailable version is made. Its continuation statement is independently
present in input B. A screenshot timeout did not block the complete
text proof. No other estimates in this manuscript are imported.

### Primary input B: Mellin normalization and multiplicity conventions

Sz. Gy. Révész, *Oscillation of the remainder term in the prime number
theorem of Beurling, caused by a given zeta-zero*,
[arXiv:2202.01837v3, 15 September 2022](https://arxiv.org/pdf/2202.01837v3).
Inspected Section 1 (1)–(7), pp. 1–3 including footnote 1;
Section 7, pp. 17–18, from the Mellin paragraph through (52)–(54).

Formal elements remain distinct when norms coincide. The source states
the Euler product and -zeta'/zeta=sum_g Lambda(g)|g|^(-s),
and identifies this with the Stieltjes Mellin transform of psi.
Its construction proof transforms x^z into z/(s-z), represents the
error transform as analytic for Re(s)>1/2, then factors the resulting
zeta as a rational product times an analytic nonvanishing factor.
The selected zero multiset has integer multiplicities. This is the
relevant proof case, not a necessity theorem for arbitrary coefficients.
Theorem 8's reciprocal-zero formula was already inspected in step 250;
its existence conclusion is not substituted for the present question.

The source's power-transform shorthand must not silently replace the
unit convention: the continuation must keep the lower-endpoint terms
when applying integration by parts to its actual psi and remainder.
No new transform or coefficient comparison is calculated here.

### Primary input C: local complex analysis

[NIST DLMF, Section 1.10](https://dlmf.nist.gov/1.10), accessed 2026-11-04:
(i), Taylor formula (1.10.1) and the zero-multiplicity definition;
(ii), the analytic-continuation uniqueness statement; (iv), residue
formula (1.10.8) and argument principle (1.10.9), including its text.

For a positively oriented simple closed contour, a meromorphic function
with finitely many interior singularities, analytic and nonzero on the
contour, has integral of f'/f divided by 2pi i equal to the number of
zeros minus poles, with multiplicities. Taylor order is an integer.
These are standard local inputs for a residue comparison; a later
application must choose an admissible neighborhood and establish the
required continuation. No global contour estimate is needed or imported.

### Search record, overlap, and limits

External queries actually used:

- Beurling Axiom A zeta logarithmic derivative psi power term zero multiplicity coefficient
- Beurling generalized primes N(x) kappa x O(x theta) meromorphic continuation zeta Mellin Revesz
- "Beurling" "coefficient" "multiplicity" "psi"
- "Beurling" "residue" "logarithmic derivative"

Only the three primary chains above supply evidence. Search snippets,
secondary overviews, lecture abstracts and unrelated recent leads were
not theorem inputs. No essential unread reference remains for the
bounded analytic specialization. This is not an exhaustive search or a
novelty assertion. Mathlib coverage of the combined statement remains
unchecked; the local complex analysis inputs are supporting results,
not a checked full matching formal theorem.

The scoped duplicate/failure comparison reused the November 4
self-consistent diagnostic assessment, L735's statement/qualifications,
its step-253 audit history and the self-generated-coarse-kernel stop.
None establishes the added N hypothesis or a necessity theorem.
L734/L639 stops are retained; no generalized Selberg theorem, construction
reproof, ordinary-prime transfer or RH claim is approved.

## Continuation scope

The source decision is SPECIALIZE. The exact later mathematical action
is saved in 2026-11-04-beurling-integer-density-specialization.md; it
requires the supervisor's separate approval next turn. Essential local
input is audited L735. Imported inputs are A–C above. Hypothetical N_P
regularity is to be tested, never asserted for L735. Compact x ranges,
the unit, formal multiplicities, theta=0 versus the source's positive
exponent, and a common analytic domain must be justified in that proof.
Do not import a precomputed residue or compatibility verdict. If the
hypotheses cannot be matched, retain that failure and stop this target.
No mathematical exploration budget is spent by this source review.
