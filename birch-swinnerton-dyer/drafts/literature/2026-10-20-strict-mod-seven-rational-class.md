# Single strict rational mod-seven class — source comparison

TARGET: Combine audited L096 and L097 to certify a nonzero order-seven rational Kummer class in the strict classical mod-seven Selmer kernel without a saturation or Sha premise.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused foundations/02 and the 2026-10-18 fixed-seven all-depth applicability/audit assessments; inspected the relevant L083 proof and L096/L097 hypotheses, conclusions and applicability arguments; compared ATTEMPTS/045 and history/380. Exact-curve/class and strict-Kummer searches are recorded below; no exact additional fixed-class theorem was established by those searches.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), IV Proposition 1.5 and connecting-cocycle proof p.108, IV.1.9 pp.110–111, IV Lemma 2.1 with characteristic-zero proof case and equation (28) p.112, global/local diagram pp.112–113, classical Selmer definition, Lemma 2.2 and equation (29) p.113 inspected in the primary PDF on 2026-10-20.
COMPARISON: Finite Kummer theory covers injection, all classical local conditions and localization naturality without saturation, rank or Sha vanishing; L083 has stronger full-kernel conclusions using additional global inputs. Only the fixed single-class applicability assembly remains, with no novelty claim.
GAP: No essential source blocker remains for this exact depth-one target; a separate research turn must assemble and document the class, its exact order and strict restriction from audited L096/L097, without importing L083's global identification.
REASON: Approve a known-method specialization with fewer global premises than L083; import Kummer theory by citation rather than reprove it, and justify only the named fixed inputs and coefficient/strict-kernel interpretation.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changes from global nondivisibility to a cohomology class; essential finite-Kummer scope and overlap with the stronger L083 statement required comparison before assembly.
SCOPE: Only E=[0,1,1,-2,0] over Q, p=7, P=(0,0), Q=(1,0), R=Q-4P and finite coefficients E[7]; classical Kummer conditions at every place, with zero restriction in H^1(Q_7,E[7]) at seven. No all-depth generator, full-kernel dimension, rational zero-log point or rationalized strict class is approved.

## Relevance and decision test

The main gap remains rank E(Q)=m(E) for arbitrary analytic order at least
two. The intermediate target is exactly TARGET. Its plausible downstream
use is an explicit fixed rational representative for a strict finite-level
class, isolating local/global divisibility from published rank and Sha
computations. It does not itself supply the rationalized strict input of
L005, an inverse-limit class or a uniform arithmetic production theorem.

Continue with one mathematical applicability assembly only if the cited
Kummer maps cover every place and the audited local/global inputs refer
to precisely the same R. Abandon or revise if a missing premise enters;
do not infer saturation or Sha vanishing. This source-scope test passes.
The mathematical assembly is reserved for a separate research invocation.

## Primary coverage and hypotheses

[J. S. Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
IV Proposition 1.5, p.108, defines the connecting map by a lift and its
Galois cocycle. IV.1.9, pp.110–111, constructs localization on those
cocycles. IV Lemma 2.1 and its characteristic-zero proof, p.112,
supply geometric multiplication surjectivity. Equation (28), p.112,
gives the injective point-quotient Kummer map. The global/local diagram,
pp.112–113, commutes. The Selmer definition on p.113 includes every
finite place and infinity; the convention Q_infinity=R is on p.112.
Lemma 2.2 and equation (29), p.113, give the Selmer exact sequence.
These statements do not assume finite Sha or a rational basis.

Use the source integer n=7 over the characteristic-zero fields Q and
Q_v. At v=7, invertibility in the residue field is not needed for these
Kummer statements. Do not apply IV.3.2's prime-to-residue-characteristic
result there. No unramified, Greenberg or ordinary local condition may
replace the classical Kummer condition. The source theorem is imported;
no reproof or new general cohomology lemma is warranted.

## Exact approved specialization obligations

For the later assembly, define the classical group as in foundations/02
and define its strict kernel by restriction to H^1(Q_7,E[7]). This is
not the kernel of the map to H^1(Q_7,E), whose vanishing is already a
classical Selmer condition. If using L083's quotient-valued lambda_1,
explain the equivalence through the injective local Kummer map, without
using its surjectivity or global group identification.

The candidate is delta_7([R]). Check nontriviality using precisely
L097's nonzero point quotient and the global injection; check its exact
order at these finite coefficients. Verify every classical condition
by the global/local diagram for the rational point, retaining bad primes
and the real place. Match the restriction at seven to the local point
quotient and use exactly L096's local divisibility. These are proof
obligations for the research turn, not conclusions proved in this review.
No fresh arithmetic, prime search or upstream certificate replay is
needed absent a specific defect.

L096's local conclusion is explicitly independent of rank and Sha: its
use of L083 is confined to the local quotient argument, as checked in
L096's applicability audit. L030/L033 supply its model and local group
order, and L081 supplies the primitive local value. L097's independent
reduction witness supplies its global input without a published basis.
The later canonical proof must state this restricted use; it must not
activate L034 or L082 through the stronger part of L083.

## Duplicates, failures and search record

L083 already states a cyclic rational Kummer kernel at every finite
depth using published rank two and primary Sha vanishing. Thus this is
not a new general strict-kernel theorem. The proposed difference is an
explicit class from the two audited witnesses without those global
premises; it must not be presented as progress beyond known Kummer
theory or the published fixed-curve group result. L096 stops at local
divisibility; L097 stops at global nondivisibility. Neither canonical
statement already carries out this cohomological assembly.

Reused search/theorem comparisons are in
`2026-10-18-fixed-seven-all-depth-localization.md` and
`2026-10-18-fixed-seven-all-depth-localization-critical-audit.md`.
Additional queries on 2026-10-20 were `"389a1" "Q-4P" Kummer Selmer`
and `"Kummer" "Selmer" "strict" "E(Q)" "E[p]" localization`.
No exact fixed-class primary theorem was established by the search.
Results on other Selmer conventions and secondary or speculative BSD
pages were not used as theorem evidence. Only the inspected Milne
passages and reused local assessments support approval; search failure
is not evidence of novelty. No essential unread lead remains.

ATTEMPTS/045 and step 371 concern the parked order-table adaptation,
not this finite cohomology application; that stop and all unfinished
files remain intact. Generic rational-membership obstructions in the
supplied overview remain: a class killed locally modulo seven need
not give a rational point of zero local logarithm. Do not transfer this
finite class into L005's Q_7-coefficient strict space. Full Selmer-kernel
identification, higher-depth compatibility, uniform rational production,
complex-order comparison and the refined formula remain unproved.

## Mathlib and turn boundary

Full matching Mathlib coverage and supporting Kummer/naturality theorem
names are not checked; no absence claim is made. This literature-only
turn approves source scope and records applicability obligations. It
adds no lemma or mathematical script and changes no argument or DAG.
