# Marked elliptic quotient — explicit two-descent source assessment

TARGET: Test whether an explicit two-descent on L112's elliptic model can certify rank E(Q) <= 1 without the parked class-group backend.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the rank-zero and pair-Jacobian rank-bound assessments, L111/L112 and ATTEMPTS/050–052; searched exact cubic coefficients, general two-descent without class groups, bounded quartic enumeration and corrections to quartic equivalence; no inspected exact-instance rank certificate was found.
SOURCE_EVIDENCE: Inspected Cremona's corrected online second edition, III.3.1 Proposition 3.1.1 pp.63–64, III.3.2 minimal-model algorithm pp.64–65, III.3.6 local tests pp.80–82 and general descent pp.89–96; Cremona–Fisher (2009), inspected 3 December 2008 author manuscript, Sections 3–6, Lemma 10, Theorems 11–13 and final remarks; book errata dated 26 September 2003.
COMPARISON: The known finite binary-quartic method avoids class/unit computation and gives a complete algebraic rank-upper-bound certificate if its invariant regions and local/class processing finish. The older unrestricted equivalence test is unsafe for reducible resolvents; use the corrected criterion. L112 supplies only the existing lower bound one; instance workload and Selmer size are uncomputed.
GAP: Specialize and measure the complete quartic search before implementing it; certify exact model normalization, every required invariant pair and real type, complete enumeration and local exclusions, and valid class identifications. No practical workload bound, Selmer dimension or upper rank is established by this source review.
REASON: Missing essential theorem coverage is supplied by an independently testable class-group-free method; approve one bounded mathematical feasibility attempt on the unchanged target, without another backend probe or an assumption that the threshold will be attained.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; prior witness/formula and number-field descent coverage did not cover complete binary-quartic enumeration or the corrected equivalence cases needed for an upper bound.
SCOPE: Exactly TARGET on L112's Q-model: imported minimal-model and general binary-quartic descent algorithms, certified coefficient-region workload assessment, and conditional-on-finishing finite enumeration/local/class certification. No new descent theory, backend installation, higher descent, point completeness or Beal exclusion is approved.

## Relevance and exact input

The main gap is exclusion of positive primitive solutions in the residual
Beal signatures. The exact intermediate input is L111's elliptic curve
with O_E=(2,165), identified
in L112 with the Q-Jacobian model

    E': y²=x³−2874960x+1739350800.

L112 already proves rank at least one, with a non-torsion point. An upper
bound one would therefore determine the elliptic summand of L127's
audited rank identity. This could inform later rank/point methods on the
marked genus-three curve. An upper bound above one does not show that
rank exceeds one; neither bound alone controls marked lifts.

## Primary results inspected and applicability

J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second edition,
CUP 1997, [corrected online edition](https://johncremona.github.io/book/fulltext/index.html),
[Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf):

- Proposition 3.1.1 and Section 3.2, pp.63–65, give integral-invariant
  conditions and minimal-model normalization, with separate 2/3 cases.
- Section 3.6, Method 2, pp.89–96, covers general Q-elliptic two-descent.
  The finite representative search, unlike the field-algebra method,
  requires no number-field unit or class-group input. Propositions
  3.6.1–3.6.2 and Step 1 retain the possible larger dyadic invariant pair.
  Step 2 and equation (3.6.9), pp.93–95, give coefficient regions for all
  three real types, including both leading-coefficient signs for type 2,
  a syzygy sieve and exact reconstruction. Step 6, p.96, subtracts the
  rational two-torsion dimension from the complete Selmer dimension.
- The local algorithm, pp.80–82, handles both projective charts, infinity,
  2 and odd discriminant primes, with separate odd/2-adic lifting cases.

These are imported results, not proposed reproofs. L112's nonsingular
integral Q-model meets the starting hypotheses. Minimality, invariant
pairs and rational two-torsion must still be certified on this instance;
the model is not assumed minimal or the cubic irreducible. The
[2003 errata](https://johncremona.github.io/book/errata.pdf) correct the
reconstruction denominator to 8a²; the inspected chapter has this form.

J.E. Cremona and T.A. Fisher, *On the equivalence of binary quartics*,
J. Symbolic Comput. **44** (2009), 673–682,
[DOI 10.1016/j.jsc.2008.09.004](https://doi.org/10.1016/j.jsc.2008.09.004).
Locators below refer to the inspected
[author manuscript dated 3 December 2008](https://johncremona.github.io/papers/quartequiv.pdf),
not assumed identical journal pagination. Its hypotheses are nonzero
quartic discriminant, characteristic different from 2 and 3, and K not
the five-element field; Q qualifies.

Section 3, p.4, defines proper equivalence. Lemma 10, pp.6–7, and
Theorems 11–12, pp.7–9, give corrected equivalence criteria, including
reducible cases. Theorem 12 uses a rational bilinear factor of
g1(X1,Y1)h2(X2,Y2)−g2(X2,Y2)h1(X1,Y1), with h the Hessian covariant.
The proof's trivial-linear-factor case and nonzero-sextic-seminvariant
case were inspected. The p.9–10 specialization requires a nonzero
sextic-covariant value; zero requires a preliminary proper change.
Theorem 13, pp.10–11, identifies soluble proper classes with E(K)/2E(K).
The final remarks, p.12, confirm that the old auxiliary-quartic test
fails for reducible resolvents. Do not use the book's Proposition 3.6.3
unconditionally or equate arbitrary genus-one isomorphism with equivalence
as coverings. No failure of a local notebook proof is alleged here.

The old rank assessment's Fisher (2022) Selmer inequality and exact
Jacobian coverage remain adequate and are reused. No BSD premise,
Sha vanishing or finite-point search is needed for the algebraic upper
bound. Larger Selmer rank can prevent the desired sharp bound.

## Certificate requirements and bounded next execution

This is source approval for a test, not an instance feasibility result.
The next invocation should first assess workload using the imported
coefficient regions; it need not implement all descent stages in one turn.

1. Certify the minimal invariants/model with exact rational model changes.
   Determine rational two-torsion dimension t on the actual cubic, without
   presuming a rational two-isogeny or split cubic. Retain the L112 model
   and its rank witness as cross-checks, not generators of the whole group.
2. Apply Step 1 on p.92 to select every required invariant pair. Do not
   treat L112's already recorded quartic invariants as a universal
   representative pair. Retain the larger pair unless its omission meets
   the stated sufficient condition. Record all 2/3 divisibility tests.
3. Isolate the roots of the resolvent with rational intervals and evaluate
   the p.94 coefficient bounds with certified outward rounding. Include
   all applicable types and signs. Ambiguous boundary cases are retained,
   not lost to floating-point rounding. Save the complete workload
   certificate and print the required versus actual work bounds.
4. For this first feasibility attempt, cap workload counting at 200,000
   (a,b) rows and full enumeration at 2,000,000 (a,b,c) triples across all
   required regions. A certified lower workload beyond the cap suffices
   to stop this unsieved implementation; it does not refute feasibility
   of a materially different sieve. If the count is unresolved within
   the row cap, report that explicitly. Do not silently enlarge caps or
   execute a truncated region as though it covered all classes.
5. Only if the complete region fits the cap, enumeration may use the
   sourced syzygy sieve and exact integrality/invariant checks. Retain
   both seminvariant signs and zero unless a recorded equivalence
   justifies removing one. Retain the identity class. Record every
   local rejection with complete projective-chart evidence; incomplete
   local tests leave candidates present. Merge classes only by the
   corrected criterion with checked hypotheses, preferably saving the
   explicit proper transformation identity. Account for overlaps between
   invariant pairs by their rational scalings. Mere matching invariants,
   matching modular data or an apparent root is not a merge certificate.
6. A finished exact Selmer computation reports s and t and compares s−t
   with the required upper threshold one. Without complete local/class
   processing, do not label survivors an exact Selmer group. Any claimed
   upper bound from an overcount must explicitly justify coverage and
   that every exclusion/merge is valid. Timeout, large workload or an
   upper bound above one leaves the rank-one question unresolved.

Scripts and full certificates, if made in that future research turn,
belong under `scripts/pair-genus-two/`; no such writes occur in this
literature turn. The discriminating test is either a complete upper
bound one or a documented workload/certificate obstruction. If the
bounded direct enumeration fails, preserve that exact stop and reassess
the mechanism instead of repeating backend probes or increasing caps.

## Duplicates, source limits and remaining obligations

New queries included `Cremona two descent elliptic curves without number
fields quartic enumeration class group`, `Cremona algorithms modular
elliptic curves chapter III general two descent quartics bounds invariants`,
`Cremona Algorithms modular elliptic curves errata second edition section
3.6 quartic bounds`, `Cremona 1996c classical invariants 2 descent elliptic
curves quartics`, `Birch Swinnerton Dyer Notes on elliptic curves I 1963
lemmas quartic bounds pdf`, `Cremona Fisher On the equivalence of binary
quartics 2009 2010`, the exact pair `2874960 1739350800`, and the existing
quartic coefficient combination. No exact-instance upper bound was found
in inspected sources; failed searches do not establish novelty.

The original Birch–Swinnerton-Dyer (1963) paper, Cremona (2001), and
Cremona–Fisher–Stoll (2010) appeared as leads; their full statements were
not independently inspected or used as substitute inputs. The specified
Cremona algorithm and corrected Cremona–Fisher criteria supply the needed
coverage. No source-access blocker remains for the bounded test. The
finite general method is covered; its practical size and sharpness for
this instance are precisely what remain to test. No new theorem or
arithmetic result was derived in this review. Mathlib coverage of the
full descent, normalization and equivalence algorithms was not checked.

Preserve ATTEMPTS/050's bounded-search stop, ATTEMPTS/051's positive-rank
obstruction to rank zero, ATTEMPTS/052's execution blocker and unfinished
L108. The proposed method does not require those parked class computations;
their stops are neither reopened nor treated as a global ban on descent.
Remaining independent obligations are the genus-two
upper rank, rational-point control, supported arithmetic, degree-nine
recovery, complementary factors, both L095 systems, minus-eleven and
other residual signatures. No Beal exclusion or complete candidate is
asserted. PROOF.md and the DAG have no mathematical change this turn.
