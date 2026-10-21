# Two-postspell cycle exclusion — completed source comparison

TARGET: Assess whether a nontrivial positive shortcut cycle can be represented by two consecutive actual postspell words with J_i>=2, H_i>=3, a_i>=0 congruent to 2 modulo 18 and odd residue-20 junctions.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Targeted cycle, local-minimum, restricted-run and exact-postspell searches; L020/L021 coding and composition, L024 exact-tail transport, Attempts 012/013/017 and prior postspell assessments inspected; queries and limits below.
SOURCE_EVIDENCE: Hercher, JIS 26 (2023), Article 23.3.5, Definitions 1/4/5/6, Theorem 16 and proof, Lemma 20 and proof, Theorem 21 hypotheses and relevant proof cases, Theorem 23 and full proof; Simons–de Weger v1.44 (2010-08-31), sections 1.2 and 2.1–2.2, Theorem 3, Lemmas 4/7/8/12/14/16 and relevant proofs; other inspected and parked leads below.
COMPARISON: Finite affine/parity machinery and fixed-local-minimum cycle restrictions are known; two postspell words are not automatically a two-local-minimum cycle. No inspected theorem excludes the entire unbounded word family; rational closure alone does not establish positive actual integer closure.
GAP: Test whether exact closed-root integrality and both word-boundary parity/valuation constraints yield an obstruction uniform in all six parameters; no such obstruction or guarded closed cycle has been established here.
REASON: Approve one bounded mathematical attempt at the unchanged target, importing existing coding and retaining all closure guards. Source comparison is sufficient for this attempt; it does not certify novelty or approve a general cycle theorem reproof.
SCOPE: Positive shortcut n>1, actual W_1 W_2, J_i>=2,H_i>=3,a_i>=0 congruent to 2 modulo 18, positive odd residue-20 n and x, and closure at n. One symbolic closure/divisibility and boundary-guard test; no parameter-table enlargement, primitive-period or first-return assumption.

## Hypotheses

The precise proposed scope is T on positive integers, n>1,
W_i=(OOEO)^(J_i) O^(H_i) E^(a_i), with independent integer parameters
J_i>=2, H_i>=3, a_i>=0 and a_i=2 modulo 18. Require the complete
actual word W_1 W_2 at n, positive odd n and x=T^|W_1|(n) both
20 modulo 27, and T^(|W_1|+|W_2|)(n)=n. No least-root assumption,
first-return condition, distinctness of n and x or primitive period
condition is imposed. Including a repeated one-word cycle avoids
silently excluding a boundary case. This is a proposed target, not a
claim of existence, impossibility or novelty.

L020 and L021 are the intended local inputs for finite word semantics
and the original-root comparison. The primary positive-cycle
theorems and relevant proof cases inspected below distinguish
period, odd steps and local extrema. In particular, bounds for finitely
many extrema cannot be presumed uniform in the unbounded J_i. Reuse
the existing affine/parity coverage only within its stated hypotheses.
No closed-cycle equation has been newly derived or tested in this turn.

The downstream use would be exclusion of this particular periodic
obstruction to eventual descent, complementary to L021's strict
compensation. Divergent orbits, cycles outside the stated two-word
language and universal entry remain independent gaps. The mechanism
is exact cycle closure with variable contracting tails, not an
extension of the stopped depth-12 cover or the exhausted growing-chain
carry-boundary test. No ancestor horizon is being enlarged.

## Conclusion

EXPLORE is ready for the exact TARGET. This literature-only step is
EXPLORATION / NOVELTY_UNCHECKED: it supplies a completed comparison and
an actionable test, not a new exclusion, imported local lemma or
counterexample. It spends no mathematical exploration turn. No essential
source blocker remains for the approved exact-arithmetic attempt.

Rechecked [MathPrize](https://mathprize.net/posts/collatz-conjecture/),
page dated 2021-07-07, on 2026-10-06: its displayed map still asks for
arrival at 1 from every positive integer under even n/2 and odd 3n+1.
The shortcut equivalence is already in foundations/01-target-and-scope.md.

## Proof

This is source evidence and an applicability comparison, not a proof
of the proposed cycle exclusion.

### Primary hypotheses and proof cases

**Published cycle restriction.** Christian Hercher,
[*There are no Collatz m-Cycles with m <= 91*](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
*Journal of Integer Sequences* 26 (2023), Article 23.3.5, published
15 March 2023. Definitions 1/5/6 (pp. 2–4) use the same shortcut map
and count local minima through exact odd/even runs. Theorem 23
(pp. 15–16) excludes nontrivial cycles with at most 91 such minima.
Its proof uses verification height 695*2^60, continued-fraction
iteration and an m-dependent upper bound; its finite computations
were not rerun. Theorem 16 (pp. 10–11) bounds the cycle step ratio
using reciprocals of odd states. Lemma 20 and Theorem 21 (pp. 12–14)
retain the local-minimum count and conditional run-length inequalities,
including separate m_2=m-1 and m_2=m cases. These statements and
proof cases were read. Two postspell labels do not establish the
small-m hypothesis: OOEO contains an even-to-odd transition. This
is not a uniform exclusion for unbounded J_i.

**Exact rational/integer boundary.** John Simons and Benne de Weger,
[*Theoretical and computational bounds for m-cycles of the 3n+1 problem*](https://deweger.net/papers/%5B35a%5DSidW-3n%2B1-v1.44%5B2010%5D.pdf),
v1.44, 31 August 2010; earlier v1.3 published in *Acta Arithmetica*
117 (2005), 51–70. Section 1.2 permits repeated periods and defines
m by local minima. Sections 2.1–2.2 (pp. 5–6) give cycle chain and
matrix equations: prescribed run lengths determine a rational solution,
usually failing integrality. Theorem 3(a)/(b)/(d), p. 5, gives
finiteness for fixed m, exclusion through m=75, and piecewise
m-dependent bounds. Read Lemma 7's full proof (pp. 8–9), the
logarithmic comparison in Lemmas 8/12/14 and the relevant Lemma 16
proof. Constants and ranges remain attached to each bound; the
coefficient 1.4784 is not an unrestricted all-m input. None supplies
a fixed two-postspell exclusion. Reuse this known rational/integer
distinction and L020/L021, without another general cycle-equation proof.

**Previously inspected extremal bounds.** The full-height assessment
already read Fernández–Ibáñez,
[*Christoffel Words as Extremal Structures in Collatz Dynamics*](https://arxiv.org/html/2607.24844v1),
arXiv:2607.24844v1, 24 July 2026. For this changed cycle scope,
rechecked Theorems 8.1/8.2 and both proofs in section 8: they assert
restrictions on the period/odd-step ratio and an orbit minimum bound
depending on that ratio. These are necessary constraints, not an
exclusion of every prescribed two-word cycle; no uniform ratio gap
for our parameters has been supplied. This unrefereed version is
not adopted as a dependency or reproved. Prior section 7 coverage
is reused; no fresh novelty assertion is made.

**Newer conditional lead, parked.** Xinjun Wang,
[*Non-existence of Collatz m-cycles for m <= 95*](https://www.researchgate.net/publication/408180567_NON-EXISTENCE_OF_COLLATZ_m-CYCLES_FOR_m_95),
author-uploaded text accessed 2026-10-06. Read the abstract, introduction
and section 2's assumed external inputs. The displayed journal
identifier and acceptance dates are placeholders; publication status
is not established. The claim is a finite local-minimum cutoff
conditional on numerical inputs. Later certificates and proofs were
not audited, and no result is imported. It does not fill the
unbounded-scope gap and is nonessential to this attempt.

### Reused inputs, duplicates and failed mechanisms

Read L020's formulas, positive offsets and full actual-word/CRT
construction, and L021 through its original-root and joint guard
argument. Reuse their ready single-word/two-word assessments and
the existing Bernstein–Lagarias/Rozier–Terracol coding inspections.
Those hypotheses apply to finite concatenations; no refresh of
general parity coding is needed. Strict compensation from L021
does not answer equality at closure. Its least-root premise is
unnecessary for the cycle test and must not be inserted.

The saved growing-chain assessment and full-height comparison were
read for duplicate mechanisms. Attempts 012/013 stop the
repeated-smallest-word minimum and single-coordinate budget;
Attempt 017 stops first-boundary carry forcing. None is a cycle
exclusion. L024's exact transport proof was read through (1):
its endpoint formula assumes E^2. Extending it to independent
E^(a_i) tails is an unresolved specialization, not an available
input. Replenishment remains evidence against assuming boundary
valuation monotonicity. L030 and the depth-12 stop remain preserved;
no larger ancestor horizon or Woods source work is proposed.

### One approved discriminating attempt

Use L020/L021's existing constants and actual parity coding to test
closed-root equality with its full integer and positivity guards.
Then test compatibility at both exact final-tail/next-odd boundaries,
using the covered first-stage shifted identities if useful. The
goal is an arithmetic obstruction uniform in J_i,H_i,a_i, or a
rigorously guarded positive closed realization. A mere rational
fixed point, automatic residue preservation or a finite empty
parameter screen supplies neither result. Do not silently promote
L024's E^2 endpoint formula to arbitrary tails.

Continue only if this one attempt yields a new checkable necessary
restriction beyond affine closure, or a specific guarded witness
that changes the route. If only the known closure equation remains,
or an obstruction uses an uncontrolled parameter cutoff, record
EXPLORATION and reassess this mechanism. A counterexample to an
auxiliary restriction stops that restriction, not the main target.
Any complete-looking positive cycle is an UNVERIFIED CANDIDATE
requiring a later independent critical review. No primitive-period,
x!=n, least-root or first-return restriction may erase a boundary
case. This test remains complementary to strict descent.

### Search record and access limits

Executed queries on 2026-10-06 included:

- Collatz m cycles Hercher 91 2023 theorem local minima
- Simons de Weger 3n+1 nontrivial cycles 68 theorem pdf
- Collatz "(OOEO)" cycle postspell
- Collatz cycles "few" "even" "runs" theorem
- Collatz cycles "odd" "3" "local minima" restricted patterns
- Collatz "NON-EXISTENCE" "95" m-cycles
- "Collatz" "postspell" "cycle"
- "Collatz" "(OOEO)" "cycle"
- "Collatz" "two" "long" "runs" cycle theorem
- site:github.com/Sodelin/Collatz-Conjecture-Work "cycle" "postspell"

Search snippets and repository overview hits were discovery only.
No exact matching theorem was located in this bounded search;
that is not evidence of novelty. The 2005 author PDF opened without
extractable lines; the corrected 2010 author URL above was readable.
A direct PDF download failed with DNS resolution, but browser text
supplied the relevant primary statements and proofs. These are
access limitations, not essential blockers. No mathematical program
or new mathematical derivation was made in this literature turn.

## Mathlib

Not checked for the cycle results or this word-language exclusion.
No supporting declaration or full matching theorem is assumed;
unknown coverage is not evidence of absence.
