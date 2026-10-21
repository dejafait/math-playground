# Full-descent upper enclosure for the finite quotient — source comparison

TARGET: Assess a full-descent upper-enclosure certificate of dim_Fp Sel_p<=2 under every L026 premise as an independent test of D=D_div.
CHECKED: 2026-10-15
DECISION: IMPORT
SEARCH_EVIDENCE: Exact full-p-descent/class-group/upper-bound searches and the bounded local comparison below identify an existing full algorithm; no novelty inference is made. Reused the earlier evaluation/injectivity assessment and inspected the changed global/local completeness passages directly.
SOURCE_EVIDENCE: Schaefer--Stoll, author long version 2001-06-13, Proposition 4.6 (p. 7), Section 5 including (5.1), algorithm steps 1--8 and local completeness discussion (pp. 8--10), Corollary 7.9/Proposition 7.10 (pp. 18--19); https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf . L021's existing residual-dimension criterion and audited L061's coefficient matching/finite generation complete the local comparison.
COMPARISON: The full computation is known and stronger than an upper enclosure; L021 already supplies the finite-quotient criterion. Only applicability and supplied-certificate obligations need assembly, without reproof or a new algorithm.
GAP: No complete global arithmetic data, local-image matrices, upper-bound certificate or actual D=D_div evidence is produced. The source method does not guarantee dimension at most two under L026; successful localization, rational membership, divisible Sha and complex-order comparison remain unresolved.
REASON: Essential changed completeness coverage is now inspected; move from source discovery to a bounded known-result application, preserving the stopped scalar and individual-interface routes.
SCOPE: Every L026 premise and audited L061 coefficient matching; the entire nonzero E[p] algebra, unconditional global completeness and classical local conditions; no D=D_div, rational-point basis, two-prime unit, successful localization or runtime assumption.
COVERED_TARGET: Import the full-descent upper-enclosure certificate under every L026 premise, reusing L021's finite-quotient criterion and specifying certified global completeness and exact local-image bounds.

## Gap, target and decision test

The main gap remains arbitrary higher-analytic-order rank equality. The
intermediate target is the saved TARGET: an independently verifiable
upper enclosure of dimension at most two for the full classical Sel_p.
Its downstream use is to test L065's independent e=0 premise. A useful
certificate need not settle successful localization, rational Kummer
membership, divisible Sha or complex-order comparison.

The startup test was source coverage for completeness and the handoff,
not production on an unspecified curve. That coverage is adequate for
IMPORT. Require the later application to certify containment of *every*
Selmer class and an exact upper dimension of two or less. Stop an
instance with missing completeness evidence or an enclosure of larger
dimension; the latter is an inconclusive bound, not evidence that the
actual Selmer group is larger. No new mathematical implication is
derived in this literature turn.

## Primary statements and essential proof passages inspected

Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS 356 (2004), 1209--1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X).
All numbering uses the [34-page author long version dated 13 June
2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
not the published layout.

Proposition 4.6 gives the finite-place Selmer intersection. Section 5
constructs its global ambient group through S-units and S-class
p-torsion, allowing a unit subgroup of index prime to p. Equation (5.1)
and steps 1--8 compute the full group. The local discussion on pp. 9--10
certifies spanning by independence and known quotient size. Read Lemmas
4.3--4.5's unramifiedness/cardinality argument, the complete algorithm
and local discussion, and Corollary 7.9/Proposition 7.10's image/norm
description. Earlier injectivity/evaluation proof-case coverage is
[reused](2026-10-15-explicit-descent-finite-localization.md).

Also inspected Proposition 7.11 and its proof (p. 19). Its equality
uses conditions at all places; it is not a finite sampled-place
completeness certificate. No reliance on it is proposed. Section 8's
smaller CM algebra is outside scope. No unread lead is essential.

## Applicability and existing local criterion

Use K=Q, theta=[p] and E'=E, as in audited L065. Retain *all* L026
premises: non-CM E; good ordinary p>=5; surjective E[p]; p prime to
#E(F_p), Manin constant and every Tamagawa factor; E(Q_p)[p]=0;
independent residual Kurihara-family nonvanishing with the stated
period/logarithm matching; L(E,1)=0; root number +1; and independently
certified nonzero quadratic coefficient in the fixed primitive series.
No reduction of that list is assessed here. The origin and full torsion
set are the same as L065's audited evaluation setup; choose S containing
p and all bad primes. Rename the descent algebra R to avoid confusing
it with L061's Selmer group D.

L021 already states, under its premises, that the residual Selmer
dimension is 2+2t and the finite quotient vanishes exactly when t=0.
L026 supplies its corank premise; the remaining arithmetic/residual
premises are retained. Audited L061 identifies classical Sel_p with
D[p] without dropping local torsion away from p. Thus the proposed
finite-quotient handoff is already covered locally; do not write another
dimension lemma or infer finite *full* Sha. The later assembly must
explicitly match these groups. A complete upper bound is independent
arithmetic evidence, whereas assuming dimension two is not its
production.

## Obligations for the proposed subsequent import

These are requirements to make the subsequent conditional application
reviewable, not a certificate already constructed here.

- Require a certified presentation of the full R and its power classes,
  with the torsion-scheme identification used in L065. For global
  completeness require a proved spanning description of R(S,p): unit
  completeness modulo p, complete S-class p-torsion, and lifts with
  verified ideal identities. A list of units or ideal relations alone
  is insufficient. Any conditional class-group computation must retain
  its assumption and cannot certify the unconditional target. Do not
  demand irrelevant prime-to-p class-group data if a complete p-primary
  certificate suffices.
- State whether the cohomology-image constraints are imposed exactly
  or omitted conservatively. If imposed, certify their matrices on the
  entire global space; if omitted, justify the direction of the bound.
  Do not mislabel the resulting enclosure as the exact Selmer group.
- At every place used to cut the global space, require the exact local
  restriction matrix and a proved local-image *upper* bound. A span of
  sampled local evaluations is only a lower bound until completeness
  is certified. The source's known-size stopping test is available;
  good divisors, faithful power-class arithmetic and exact independence
  must all be justified. No global point is required.
- Supply finite-field linear algebra proving the dimension of the
  surviving full global space, including a verifiable rank witness.
  Account for unramifiedness and every omitted classical condition;
  distinguish an upper enclosure from equality throughout. Require a
  complete containment argument before applying L021/L061.

No code, general implementation or successful arithmetic instance is
authorized by this source comparison alone. No new reproof is needed.
The covered application may state supplied exact arithmetic hypotheses
but must not assert that they have been obtained. Full and supporting
Mathlib coverage remains not checked.

## Search, duplicates and continuation

Queries: `Schaefer Stoll how to do a p descent elliptic curve Section 5
class group upper bound Selmer` and `"Schaefer" "Stoll" "7.9"
"Selmer"`. Search results led back to the pinned primary paper;
Stoll's short course and Schaefer's class-group paper were unread
supporting leads, not used imports. Existing evaluation coverage is
adequate and was not re-searched. No source-access blocker remains.

Read the relevant statements/proofs of L021, L026, L061 and L065, and
ATTEMPTS/021/032/033/034. L021 is the duplicate for the dimension
criterion, L065 the contrast for individual membership. ATTEMPTS/021
excludes the primitivity shortcut; 032 preserves the capped zero;
033 parks scalar-to-coordinate reconstruction; 034 stops repetition
of the individual interface. None is a ban on complete upper bounds.

The single proposed continuation is COVERED_TARGET, a known-result
application with explicit completeness evidence and the existing local
criterion. As a newly written covered continuation it receives the
supervisor's separate approval next turn; this completed source review
does not execute it. Essential inputs are L026 and audited L061, with
L021's existing criterion and L065's full-algebra setup. D=D_div is the
conclusion being tested, not an input; residual-family nonvanishing is
still supplied. No cross-notebook result is used. All independent gaps
listed in GAP persist.
