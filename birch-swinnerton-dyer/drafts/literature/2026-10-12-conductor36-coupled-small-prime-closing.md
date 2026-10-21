# Coupled small-prime cusp closing — source comparison and bounded test

TARGET: Assess whether the full T_5 Hecke identity can be closed as a coupled rational system on the twelve saved Gamma_0(36) cusp classes, retaining every transport correction and the infinity primitive, to plan all 144 endpoints within cutoff 4860 and 1000000 primitive terms at normalized two-sided tail width 2^-38.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: BSD-179 searched numerical modular symbols/nonunitary Hecke, coupled cusp systems, cusp permutation and transportability; read the primary statements/cases below and compared L049/L053, ATTEMPTS/026--027 and BSD-178's attempt/history. The sources cover component algorithms; no matching twelve-class coupled solvability or fixed-workload theorem was located. This bounded search establishes no novelty.
SOURCE_EVIDENCE: Cremona corrected second edition (1997), Proposition 2.2.3 with all proof implications pp.16--17, (2.4.1)/pairing compatibility pp.18--19 and (2.9.1)/arbitrary-cusp remark pp.31--32; Wuthrich arXiv:1608.06423v2 (23 March 2017), (2), Lemma 4 with full proof pp.6--7, Section 5.1 (11)/matrix/height construction pp.11--12 and Section 5.2 good-prime, bad-prime and prime-square cases pp.12--13; Stein--Verrill (2001), Proposition 2.1, Theorem 2.4 with proof, Corollary 2.5/Remark 2.6 and Algorithm 3.2 pp.172--177; official Sage numerical-symbol Algorithm/normalization note/nonunitary warning, accessed 2026-10-12.
COMPARISON: General good-prime Hecke action needs no congruence ell=1 modulo 36; individual same-class scalar closing has extra eligibility. Sources support exact assembly and a finite rank/workload test, but supply neither the proposed coupled inverse nor the thresholds. L053's ell=37 fixed-plan stop remains intact.
GAP: Certify every T_5 image assignment/transport, infinity-normalized rank/consistency and any exact solution weights; then replay all 144 endpoint compositions and full tails against unchanged limits. None of these finite conclusions was calculated in this literature turn.
REASON: Ready only for a bounded specialization/test of known identities; failed rank, closure or workload is an admissible outcome. No invertibility theorem is assumed or approved, and no new mathematics is derived here.
LITERATURE_REASON: Changed eligibility and coupled-system scope: ell=5 is good but not 1 modulo 36; prior per-representative coverage does not establish coupled solvability.
SCOPE: Fixed E=[0,0,0,0,1], N=36, normalized weight-two trivial-character newform, twelve saved representatives and all 144 original oriented endpoints; ordinary Gamma_0(36) transportation, full good-prime T_5, exact rational elimination and audited L049/L051 tail/period conventions. No Atkin--Lehner expansion, bad-prime operator, prime-square closure or assumed spectral theorem.

## Sources actually inspected and their limits

[Cremona, Algorithms for Modular Elliptic Curves, corrected second
edition (1997), Proposition 2.2.3, pp.16--17; (2.4.1), pp.18--19;
(2.9.1), pp.31--32](https://johncremona.github.io/book/fulltext/chapter2.pdf)
gives constructive reduced-cusp equivalence and full good-prime action
with integration adjointness. Both diagonal and translated/divided
branches are essential. Eligibility is p not dividing N, so p=5 is
eligible here. Section 2.9's coprime-denominator and p=1 modulo N
restrictions concern integral absolute homology, not validity of the
general identity. They establish no coupled inverse. The cumulative
cusp-list implementation is known (p.17).

[Wuthrich, Numerical modular symbols for elliptic curves,
arXiv:1608.06423v2, 23 March 2017, (2), Lemma 4, Sections 5.1--5.2,
pp.6--7,11--13](https://arxiv.org/pdf/1608.06423v2)
uses the infinity-based primitive and interior-point transportation.
Lemma 4 requires positive height; its full proof uses |a_n|<=n and a
geometric tail. Section 5.2 distinguishes unrestricted coprime Hecke
action from same-class closing controlled by
d=gcd(gcd(m,N),N/gcd(m,N)), and gives a prime-square alternative.
It does not certify the proposed coupled system. Ordinary balanced
transport points have height 1/|C| for C nonzero. Use L049's audited
orientation/matrix convention for sign-sensitive source displays.
The [author-deposited accepted manuscript](https://nottingham-repository.worktribe.com/preview/851837/modsym.pdf)
was also inspected for the complete Section 5.2 cases and complexity
paragraph; its scope agrees. The [publication record](https://nottingham-repository.worktribe.com/output/851829/numerical-modular-symbols-for-elliptic-curves)
identifies Math. Comp. 87 (313) (2018), 2393--2423,
doi:10.1090/mcom/3274. Final journal typesetting was not inspected;
the theorem/page citations here refer to the identified v2 manuscript.

[Stein--Verrill, Cuspidal modular symbols are transportable,
LMS J. Comput. Math. 4 (2001), 170--181, Proposition 2.1,
Theorem 2.4 and Algorithm 3.2](https://wstein.org/papers/transport/lms2001-006.pdf)
is a stronger transportability comparison, not a substitute for coupled
solvability. Its rational-symbol theorem assumes cuspidality; the full
proof clears torsion, retains the infinity coefficient and produces a
transportable expression. Remark 2.6 isolates weight two. Algorithm
3.2 uses positive-height interior points. This supplies no claimed
identification of every relative generator with an absolute cycle,
specified cusp matrix, inverse weights or workload. Proposition 3.3's
Atkin--Lehner improvement was seen as a lead, not approved or imported.

[Official Sage numerical modular-symbol documentation,
Algorithm, normalization note and nonunitary warning](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html)
describes exact space methods and numerical transport with denominator
and error control, retaining a Manin-constant qualification. Its
nonunitary warning gives no execution guarantee. No software output is
used as a theorem; linked implementation code remains an unread lead.

## Discovery, local comparison and prospective finite test

Queries included: numerical modular symbols Hecke non-unitary;
modular symbols coupled cusp linear system Hecke numerical Wuthrich;
modular symbols cusps linear system numerical Hecke;
Hecke coupled cusps modular symbols; modular symbols Hecke cusp
permutation; Stein Verrill Cuspidal modular symbols are transportable.
Non-primary snippets and unrelated function-field/higher-rank results
were discovery leads only. The relevant Wuthrich reference to
Stein--Verrill was followed to the author's primary paper and compared
at theorem level. No search failure establishes originality.

L049's oriented full Hecke primitive identity and L053's representative
transport composition are reusable as written. Equivalence does not
equate primitive values without corrections. L053 covers the saved
endpoint domain, not every newly generated Hecke image: certify this
additional closure. An unassigned reduced image stops the twelve-class
target; do not silently enlarge the domain. No completed local coupled
certificate was found in the specific artifacts searched. Preserve
unfinished work and ATTEMPTS/025--027's different fixed-schedule stops.

The concrete approved scope is one plan-only implementation.
Reconstruct the saved domain/representatives, verify good-prime
arithmetic/eigenvalue, reduce every full T_5 image and certify each
assignment and transporting matrix. Include the actual infinity
primitive equation, fixed at zero, and retain the full infinity Hecke
equation as a consistency check even if redundant. Do not replace
infinity by a finite cusp, choose an arbitrary free-variable value,
or assume central vanishing.

As the mathematical test, assemble the coupled equations directly
from the cited identities, retaining every occurrence and sign, and
save exact rational elimination witnesses. Require uniqueness after
infinity normalization before asserting solved representative values.
Rank deficiency or inconsistency stops this test with an exact witness;
do not repair it using other primes, period inputs or a conjectural
spectral bound during this attempt. This specification approves testing
an unknown finite property, not its conclusion. Keep all transport
corrections, including those belonging to the infinity class.

If successful, save/reconstruct all solution weights and all endpoint
compositions. Independently check matrices/inverses, Mobius images and
positive rational heights; C=0 needs witnessed integer translation.
Propagate full absolute-weight errors through solution weights and both
endpoint signs. Caching cannot erase repeated error occurrences; any
combined equal-point coefficients need exact reconstruction. Use the
unchanged conservative tail convention and independent positive total
period lower bound; no sharper tail convention is approved.

Continue toward analytic table production only if independent complete
plan replay has zero failures, maximum cutoff <=4860, total distinct
primitive terms <=1000000 and normalized two-sided tail width <=2^-38
for every original generator. Otherwise save actual/required bounds
and stop this schedule. No analytic sums belong to the proposed plan
test. Save full certificates in scripts/conductor36-table/ and print
summaries/paths. Implementation belongs to a later approved research turn.

Essential inputs: L038's full saved N=36 domain (structural critical
audit pending); audited L049 transports/full Hecke identity; L050's
exact curve/conductor; audited L051 periods and coefficients through
4860; audited L052 clearing integer 24 for downstream recovery; L053's
representatives, transports and complete failed compression certificate
(new instance critical audit pending). No cross-notebook input.
No coupled certificate, improved bound, table or rank consequence
exists. Downstream use is a complete normalized integration table.
CM still excludes L027; arbitrary rank equality, uniform coefficients,
rational directions, Sha and complex-order comparison remain open.

Mathlib coverage of the coupled algorithm was not checked; absence is
not asserted. No new lemma, mathematical script, matrix, eigenvalue
calculation or proof is written in this literature turn. The changed
ready assessment receives separate next-turn approval before research.
Only component-source coverage is completed; no mathematical advance
beyond the sources or on arbitrary-curve BSD is claimed.
