# Downward-order propagation: completed source comparison

TARGET: Assess known differential identities for actual-Xi Laguerre coefficients for a downward-order positivity principle from the logarithmic upper tail to the missing initial segment, retaining central multiplicities and identifying any independent sign or boundary hypothesis.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for generalized Laguerre differential identities, coefficient recurrences and downward positivity located Craven--Csordas Theorem 2.1 and Csordas--Vishnyakova equation (11)/Corollary 3.3; inspected their primary statements and relevant complete proof cases. Notebook-local duplicate searches and the saved initial-sign and height-differential assessments were checked; queries and access qualifications appear below.
SOURCE_EVIDENCE: Craven--Csordas, Iterated Laguerre and Turan inequalities, JIPAM 3(3), article 39 (2002), author PDF pp. 2--4,6: equation (2.1), Theorems 2.1--2.2 with proofs and Remark 2.4 with proof; Csordas--Vishnyakova, Cent. Eur. J. Math. 11(9) (2013), 1643--1650, Remarks 1.4, Theorems 3.1--3.2 with the latter's proof, equation (11), Corollary 3.3 and Open Problem 3.4, pp. 1645,1647--1649. Reused the October 25 initial-sign assessment for upper-tail scope; the primary paper 41 page still displays v4, 24 October 2026 07:18 UTC.
COMPARISON: The cited recursion changes the input by a real linear factor, rather than propagating signs downward for fixed Xi. The vertical second-derivative identity is exact, but its global nonnegative-curvature premise is equivalent to all generalized Laguerre signs for a nonzero real entire input. Neither inspected theorem obtains that premise from the logarithmic upper tail or independently available Xi boundary data.
GAP: No inspected sign-preserving closure connects the known high orders to Xi's missing initial indices. An independent signed defect or boundary mechanism remains unavailable; this bounded search proves no impossibility of all differential or order-based methods.
REASON: The missing primary identities are now identified and their hypotheses compared. Park the direct source shortcut instead of implementing an unspecified propagation equation. This is informative source-scope evidence, not a new theorem, sign result or novelty claim; no lemma or mathematical script is modified.
SCOPE: Completed literature comparison only for actual Xi and coefficients defined in L463/C465a, including central multiplicities. No new recurrence, countermodel, integration formula, sign principle or mathematical proof target for downward propagation is approved.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination lacked primary identity and sign/boundary coverage. Existing upper-tail and first-sign literature is reused; the new work inspects the previously unassessed recursion and complex-Laguerre interface.

## Gap, intermediate target and bounded test

The main gap is actual-Xi all-degree positivity, particularly the
low-index signs at unbounded heights. The intermediate target was a
source-backed downward-order sign principle using independently
available actual-Xi data. Its plausible use was to reduce the missing
initial segment below L463/C465a's tails. Signs outside any transferred
range, effective height overlap and mixed positivity would remain open.
The desired threshold was nonnegativity for every integer
1<=n<ceil((c_0/2)log(t/(2pi))) at all sufficiently large real t,
with fixed c_0>3/8 under L463's premise (or c_0>1/2 using C465a).
No such initial-segment conclusion is obtained.

The discriminating test was to inspect the actual identity and every
sign or boundary premise. The two precise interfaces below do not pass
that application test: one changes the function, and the other assumes
a global sign condition equivalent to the missing conclusion. This
changes the route decision to parking this source shortcut. It does
not establish a generic impossibility theorem. No coefficient identity
has been newly derived and no scalar power-series example constructed.

## Primary identities and exact applicability

1. Thomas Craven and George Csordas, *Iterated Laguerre and Turan
   inequalities*, JIPAM **3**(3), article 39 (2002),
   [author PDF](https://math.hawaii.edu/~tom/mathfiles/iteratedLT.pdf),
   18-page version, printed pp. 2--4,6. Equation (2.1) defines the same
   analytic-product coefficients as L463/C465a; Remark 2.4 extends
   the explicit derivative expression to any real entire function.
   Theorem 2.1 states, for real a and integer n>=1,

       L_n((x+a)f;x)=(x+a)^2 L_n(f;x)+L_(n-1)(f;x).

   Its other conditions are L_0(f)=f^2 and L_n(c)=0 for constants
   c and n>=1. Read the entire coefficient-product proof. Theorem
   2.2 assumes nonzero f=exp(-alpha x^2)g, alpha>=0, with real
   entire g of genus zero or one, and characterizes LP membership
   by all L_n(f;x)>=0 for all n>=0 and real x. Its proof uses
   the full sign premise or real-rooted polynomial approximation.
   It is not an order-only recurrence for a fixed function. Theorem
   2.1 needs neither division nor nonvanishing at the center, so
   central multiple zeros are not excluded by this identity.

   **Comparison:** L463/C465a supplies no coefficient signs for every
   modified input (x+a)Xi. The cited theorem alone therefore supplies
   no downward implication for actual Xi. The product-based mechanism
   is already represented locally in L255 and is not a new discovery.

2. George Csordas and Anna Vishnyakova, *The generalized Laguerre
   inequalities and functions in the Laguerre--Polya class*,
   Cent. Eur. J. Math. **11**(9) (2013), 1643--1650,
   DOI [10.2478/s11533-013-0269-x](https://www.degruyterbrill.com/document/doi/10.2478/s11533-013-0269-x/pdf).
   Equation (11), printed p. 1648, gives for real x,y and z=x+iy

       partial_y^2 |f(x+iy)|^2
         = sum_(n>=0) (2n+1)(2n+2)L_(n+1)(f;x)y^(2n)
         = 2(|f'(z)|^2-Re(conj(f(z))f''(z))).

   Corollary 3.3 makes nonnegativity of this complex expression at
   every z equivalent to all coefficient signs for nonzero real
   entire f. Theorem 3.2 removes the earlier growth assumption.
   Read its proof, including the zero/nonzero real-center cases,
   continuity and the y=0 derivative boundary value. That boundary
   value is zero; it is not a boundary estimate at infinity. The
   logarithmic proof uses prior zero exclusion. Open Problem 3.4
   asks what extra assumptions suffice for arbitrary entire-series
   coefficients; it does not assert that convexity alone signs them.

   **Comparison:** the identity specializes to actual Xi by L018's
   entirety/reality and the coefficient convention in L463/C465a.
   This is applicability of a cited identity, not a new derivation.
   No global curvature sign, logarithm across possible nonreal zeros,
   or controlled signed boundary/source term is supplied by the tails.
   Assuming the Corollary 3.3 premise would assume an equivalent sign
   criterion. No such premise is installed in the notebook.

These are theorem comparisons, not independent audits of both papers.
The central-zero qualifications are retained. No limit at infinity,
spatial integration, interchange or division by Xi is performed.
Full matching Mathlib coverage and supporting APIs are unchecked;
unknown coverage is not evidence of absence.

## Reuse, duplicates and failures

Read canonical L018, L463 and C465a. L018 specifies the completion;
the nomination's attribution of the coefficient definition to L018
alone was imprecise: its exact convention is in L463/C465a. L463
retains the pinned external half-plane premise and manuscript-audit
qualifications. C465a is unconditional with c_0>1/2. Both leave initial
indices and effective overlap unresolved; their existing source
assessments are reused without another tail import.

The [initial-sign assessment](2026-10-25-initial-laguerre-sign-coverage.md)
and [height-differential assessment](2026-10-26-first-sign-height-differential-coverage.md)
already compare finite-height, scalar-comparison, operator-membership
and theta-versus-Fourier-variable scopes. The new comparison is the
specific primary recursion and vertical-curvature interface above.
Read L255's product proof; L251's global first-sign masking example
and the L257 finite-level failure record remain contrasts, not inputs
for a new propagation theorem. The [backward-energy stop](../../ATTEMPTS/2026-10-30-bounded-backward-laguerre-energy-comparison.md)
concerns a heat parameter; L569 concerns absolute approximation error.
Neither stop is a global prohibition on differential methods.

A possible L470 audit reroute was screened narrowly and rejected as
a duplicate: drafts/audits/2026-10-27-l470-critical-audit.md already
contains a completed application replay. Its stale overview label
is not evidence that the audit remains undone. No metadata repair or
second audit was performed here. No cross-notebook input was used.

## Search and access record

Representative queries actually executed on 31 October 2026:

- `generalized Laguerre inequalities differential identities L_n derivative recurrence Csordas Vishnyakova`
- `generalized Laguerre inequalities positivity higher order implies lower order recurrence`
- `Craven Csordas "Iterated Laguerre" "Theorem 2.1"`
- `"Laguerre inequalities" "downward" positivity`
- `"Laguerre inequalities" "differential identity"`
- `"Laguerre inequalities" "second derivative" recurrence`
- `"generalized Laguerre inequalities" "derivatives" recurrence`
- `"Laguerre inequalities" "differential recurrence"`
- `"Laguerre inequalities" "Laplacian"`

Orthogonal Laguerre-polynomial recurrences concern a different object.
Search results are discovery aids, not theorem evidence. Initial EMIS
requests failed; a CiteSeer mirror returned 403 and the German-library
mirror 429. Both essential primary texts were subsequently accessible
via the author/publisher links above. A shell download failed DNS;
the web tool supplied the primary texts. There is no essential source
blocker. Csordas arXiv:1309.0055v2 Remarks 2.6 was read as the pointer
to the recursion, not as a substitute for Theorem 2.1.

## Route disposition

The saved target is reviewed, with a negative application comparison
rather than a new mathematical obstruction. No independently controlled
actual-Xi propagation defect was found; consequently no creative
sign-proof target is justified by this review. Reopening this shortcut
requires an explicit independent sign/boundary input and a bounded
application test, not the same identity with its premise unstated.

The unaudited shifted-saddle source estimate behind L463 is a different,
independently checkable correctness target. Its exact source was already
inspected in the October 25 assessment; the primary page/version and
(18n)'s range were rechecked only to prepare the bounded continuation.
A [separate audit scope](2026-10-31-l463-shifted-saddle-audit.md) is
nominated for next-turn approval. This does not upgrade L463's trust
status or assert that its source proof is correct. PROOF.md and DAG.md
are unchanged because the mathematical argument has not changed.
