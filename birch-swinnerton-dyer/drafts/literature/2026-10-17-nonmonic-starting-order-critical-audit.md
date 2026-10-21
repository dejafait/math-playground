# Fixed starting-order critical audit — source scope approved

TARGET: Critically audit L077's complete fixed nonmonic starting-order certificate, including all basis transports, products, trace entries and both determinant eliminations, without extending to maximality.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact construction comparison in drafts/literature/2026-10-17-nonmonic-order-discriminant-test.md and drafts/2026-10-17-maximal-order-source-review.md; checked L077, L067 hypotheses/conclusion, histories 281--283 and ATTEMPTS/034 and /036. No matching separate L077 audit is recorded in these inputs; no novelty inference is made.
SOURCE_EVIDENCE: Del Corso--Dvornicich--Simon, Decomposition of primes in non-maximal orders, Acta Arith. 120.3 (2005), 231--244, https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; reopened Section 2 pp. 232--234, order definition, Proposition 1, Proposition 2 proof and complete Proposition 4 triangular discriminant proof; page 234 also requested as a rendered page.
COMPARISON: The source supplies the same nonmonic order and discriminant identity; the remaining work is a separate critical audit of the complete fixed arithmetic, source applicability and signed determinant interpretation, not a new general theorem or a maximal-order construction.
GAP: No essential source gap remains for this fixed audit; certificate correctness is still unaudited, and index-prime coverage, maximality, field discriminant and complete unit/class arithmetic remain outside coverage.
REASON: The newly selected audit target required separate scope approval after step 283; this confirms reusable coverage and specifies its audit obligations without claiming new mathematics or completed verification.
SCOPE: L077 and audited L067 only; the entire degree-48 field, primitive H=343h, full nonmonic lattice and both rational transports, all 110592 product slots, all 2304 trace entries and both complete signed determinant eliminations. Proposed research classification REPRODUCTION.
LITERATURE_REASON: Separate comparison of the newly selected L077 critical-audit scope was essential; the existing construction sources suffice and no expanded literature search is needed next turn.

## Precise source comparison

The primary paper takes a Dedekind domain R, its fraction field, and a
primitive irreducible degree-n polynomial F with nonzero leading
coefficient. Its order has first basis vector 1, not T0=a0; the remaining
vectors are Ti(alpha)=a0*alpha^i+...+ai, i=1,...,n-1. L077 states exactly
this basis. Its application uses R=Z, n=48 and a0=343, with fieldness
and primitive H supplied by audited L067. These must remain actual
checked inputs, not assumptions about integrality of t or residual
surjectivity of E[7]. Characteristic zero supplies separability.

Section 2 states that this lattice is an order and references Simon [6]
for its construction; Proposition 2 additionally identifies it as the
intersection of the two polynomial rings in alpha and alpha inverse.
Its proof uses primitive polynomial divisibility (Proposition 1), then
separately handles degrees below n and at least n by induction. No new
result from the unread Simon paper is required for this audit: the
published Section 2 order statement is imported, while L077 already
provides a full instance ring-closure certificate. Checking that certificate
is justified because the theorem does not validate its saved coefficients.
Do not turn that check into a general reproof or extend the intersection
argument to a different lattice.

Proposition 4 explicitly proves equality of the order and polynomial
discriminants by its triangular basis transformation, with diagonal
1,a0,...,a0. The audit must keep the squared determinant factor and the
nonmonic polynomial convention. L077's resultant convention and its
signed trace determinant must be checked against the displayed formulas
in L077, not an absolute value, number of decimal digits, floating roots,
or agreement modulo selected primes. The primary theorem concerns an
order discriminant, not a field discriminant. The maximality results
reviewed previously are unnecessary here and are not being imported.
Full or supporting Mathlib coverage remains unchecked; no absence is inferred.

## One later bounded audit

Read the complete L077 proof and the relevant producer/verifier code;
reconstruct the full fixed evidence in a fresh audit output directory.
Do not invoke the original one-shot runner against existing outputs.
Use audited L067's complete field certificate and unchanged transports;
check its recorded hash, all 49 coefficients of H, content, leading
coefficient, all 48 basis vectors, both inverse matrices and both
full transports. Retain identity checks and every ordered product,
including all zero coefficients. Check every trace as an actual field
multiplication trace and every Gram entry by full matrix composition.

Reconstruct the entire 48-by-48 trace matrix and 95-by-95 Sylvester
matrix, their conventions, every pivot/swap and exact division, all
stages and both terminal signed integers. Check nonvanishing and the
full discriminant equality. Stage hashes supplement complete arithmetic;
a bounded JSON preview or a fresh success label cannot replace it.
Review whether producer/verifier share a mathematical error; agreement
alone is insufficient. Any alternate method used must check complete
load-bearing evidence, not a sample. No new discriminant theorem is needed.

One aggregate audit stage has 180 seconds internal, 181 seconds external
and at most 134217728 new bytes, retaining partial reports on failure;
no retry, cap increase or retrospective stage split. These are audit
limits, not a runtime prediction from step 283. Preserve original bytes
with before/after hashes. Record actual/required bounds and the precise
failed identity if any. A failed audit preserves L077 and diagnoses its
claim; it does not authorize replacement arithmetic in this step.

Continue only after complete source applicability and full signed evidence
pass; missing evidence, a false identity or cap failure stops this audit
with its partial output. Do not claim critical audit has occurred today.
The source approval repeats established coverage and is reported STALLED,
not a mathematical advance or an informative negative result.

## Relevance and prior stops

A reliable starting order is a prerequisite for later separately assessed
index-prime/maximality and unit/class computations toward L066. It is not
a Selmer enclosure. ATTEMPTS/034 stops repeated conditional-descent
interface work, and /036 stops a particular incidence implementation;
this audit does neither and does not reopen them. Histories 281--283
supply the source review, URL repair and construction, rather than an
already completed critical audit. No matching fixed computation beyond
those sources was inspected and no originality claim is made.

L026 premises, faithful global power classes, complete S-units/S-classes,
functions/local bounds, successful localization, rational membership,
divisible Sha and arbitrary-curve rank/complex-order comparison remain
unresolved. No cross-notebook input enters the audit. The main gap is
still rank equality for arbitrary analytic order at least two. This
literature-only step modifies no lemma, mathematical script, DAG or proof
assembly. The exact same target is ready for a separate mathematical turn.
