# Height-selected prime — completed source comparison

TARGET: Compare IV Corollary 2.2(ii)'s height-selected prime construction with the conditions v_ell(j(E))>=0 and ell not dividing any -v_p(j(E)) for p in S on the same L089-L090 survivors.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step398 reused steps360/389/394 and audited L089-L092/L098-L099, checked ATTEMPTS/035 and L091's deliberate prime-selection exclusion; searched exact Corollary 2.2/P2/P3 and local-height/prime terminology, then inspected IV Proposition 2.1(ii), the complete corollary antecedent and proof through P7. No matching normal-closure transfer theorem was located or originality inferred.
SOURCE_EVIDENCE: Fresh April 2020 IV reproduction, 87 pages, Proposition 2.1(ii) p.40, Corollary 2.2 opening/(ii) pp.41-43, proof pp.43-46 including the height sum, S1-S3, P1-P7; reused GenEll Definition 3.3/Remark 3.3.1 p.17, Silverman/Kedlaya and Milne coverage from step394. Exact clauses, source limits and later specialization obligations are below.
COMPARISON: P2 excludes divisors of every nonzero local height over the literal field F=G_o; P3 allows a positive height below sqrt(H) at residue characteristic ell. Thus integrality at ell is not supplied by this construction. A later arithmetic transfer to C_o is required before claiming rational pole-order avoidance or all-place coprimality there; L099's explicit integrality hypothesis cannot be silently dropped.
GAP: Essential source comparison is complete, but no G_o-to-C_o height specialization, actual survivor/exceptional-set application or proof of ell-integrality is performed. The source assertion is existential, not a statement about every prime in its interval.
REASON: The comparison separates an available height-avoidance clause from the still-missing integrality premise and changes the next target to a conditional same-member transfer. No new theorem, source reproof or mathematical script is authorized in this literature-only step.
LITERATURE_REASON: The target moves from a conditional local equivalence to the essential unread selection argument and its applicability; it is not another review of L099 or an authentication retry.
SCOPE: Same L089-L090 member, c,h,d_*,e_*, both domains/fixed closure, all six E_o,G_o,C_o and S={p:v_p(j(E))<0}; compare the source's actual prime choice without substituting seven or passing to an ell-division-field height.

## Original bounded screening (retained)

The original main gap is finite B>=A. The intermediate target is to
decide whether the existing native prime-selection construction supplies
the two rational conditions needed to apply the verified L098-L099
criteria. A positive comparison could authorize a later same-member
application; a missing hypothesis or an allowed bad ell-place could
instead show that this conditional repair must change. No such verdict
or new arithmetic deduction is made in this screening.

Start with the existing source records
`2026-10-21-native-selected-support-comparison.md` and
`2026-10-21-normal-closure-all-support-q-orders.md`, and L091's exact
source references. Extract only the selection clauses in the qualified
[IV April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Corollary 2.2(ii), pp.41-46, and follow its precise theorem references
for the prime choice. These references are leads for this target,
not an assertion that their full selection hypotheses were checked.
Reuse any adequate local extracts before retrieving more source text.
Separate a selected set of bad places from all rational j-poles,
an existence assertion from every-prime assertions, and the choice
before field construction from conditions on an already fixed field.

The source review passes only with complete relevant hypotheses and
quantifiers for an independently testable later specialization. If
the source permits ell to be a pole, record that distinction rather
than silently importing integrality. If a necessary passage remains
inaccessible, name it and park the dependent target; do not repeat
ATTEMPTS/035's authentication mechanism. Authentication of current
author/journal bytes is a separate unresolved qualification.

Essential local inputs for any later application are audited L089,
L090, L092, L098 and L099; no other notebook is involved. The same
member must meet any additional height/exceptional-set hypotheses
before applying a selected-prime theorem. Full native selected/theta
data, L092's relative factor-four excess, exact generation/repairs,
the source-version and def= boundary, actual input/action/factorization,
pilot transport and essentiality remain unresolved. Mathlib coverage
for the selection construction is unchecked. No new lemma, mathematical
script or proof of prime avoidance is authorized by this draft.

## Completed review — 2026-10-22, step398

The screening above records the starting question, not an additional
pending retrieval. This review supplies source coverage and a changed
continuation, without deriving a new mathematical result. Original finite
B>=A remains the main gap. The intermediate test concerns the prime
needed by a possible field repair; even a passing test leaves the
factor-four relative degree excess and the native/essentiality bridges.

### Primary imports and exact scope

Use Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020,
the [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
This is the same qualified version as L091. Its current author/journal
authentication is unresolved; ATTEMPTS/035 remains parked.

Proposition 2.1(ii), printed p.40, states the prime-number-theorem
bounds (2/3)x <= theta(x) <= (4/3)x for x>=xi_prm>=5, and, for a
finite prime set A, existence of a prime outside A no larger than
2(theta_A+xi_prm). Its proof cites the named prime number theorem,
Edwards p.76 and GenEll Lemma 4.1/Remark 4.1.1. The IV statement
and its proof were inspected; those additional references were not
independently reverified here. No PNT reproof is needed.

Corollary 2.2(ii), pp.41-43, fixes the compact domains and dyadic
j-bound first, then d, epsilon_d and a finite exceptional parameter
set; only subsequently does it take the curve and its prescribed
Legendre 15-division field. Full rational 15-torsion and the exact
field expression are explicit antecedents. No Galois assumption is
added here to evade L091's qualified fixed-field objection.

In its proof, pp.43-45, write H for the source's h, to distinguish
it from L089's fixed congruence modulus. The normalization is

    H = (1/[F:Q]) sum_v h_v f_v log(p_v),

over all finite F-places; f_v is the residue degree, h_v=0 for good
reduction and h_v is the integer GenEll local height for multiplicative
reduction. Semistability comes before this good/multiplicative split.
The source uses [F:Q]<=delta=2^12*3^3*5*d and enlarges its finite
exceptional set to arrange sqrt(H)>=xi_prm>=5. Its set A includes
primes <=sqrt(H), prime divisors of nonzero h_v, and residue primes
p_v at places with h_v>=sqrt(H). The displayed weighted estimates
bound theta_A and apply Proposition 2.1(ii). The resulting existential
choice, printed p.45, is exactly:

    (P1) sqrt(H)<=ell<=10 delta sqrt(H) log(2 delta H);
    (P2) ell divides no nonzero h_v, for every finite F-place v;
    (P3) for every v above ell, h_v<sqrt(H).

These are simultaneous clauses for a chosen prime, not assertions
for arbitrary primes in the interval. The height normalization is
over the prescribed F, before adjoining ell-torsion. In the current
comparison that literal field is G_o, not C_o or the later K.

The remainder of pp.45-46 was read to check whether a later clause
strengthens P3: P4 excludes a global ell-cyclic subgroup after a
further finite enlargement; P5 chooses multiplicative moduli places
away from 2ell and proves that set nonempty; P6 obtains the large
image; P7 asserts initial data on the fixed field. These clauses do
not state good reduction at ell. The proof explicitly estimates the
omitted ell contribution using P3. The independent derivations of
P4/P6 and their GenEll inputs are not imported as proved here.

### Comparison, duplicates and limits

P2 is the inspected source input relevant to pole-order avoidance.
P3 bounds a height at ell instead of requiring height zero. Thus the
source does not supply L098-L099's ell-integrality premise through
its displayed prime exclusions. This is a scope verdict: no actual
selected prime with a pole has been constructed, and existence of a
different selection satisfying integrality has not been ruled out.

L099 computes heights over C_o under its stated hypotheses; it does
not compare P2 over G_o with heights over C_o. L092 supplies actual
field degrees but no height transfer. L091 deliberately avoids
verifying prime selection; its finite-exception argument and L089's
infinitude must not be relabeled as a selected-prime computation.
L061/L084 use different fields and do not fill this gap. The reviewed
Tate, GenEll and Milne statements cover finite local extensions and
nonsplit multiplicative reduction in general, so a later conditional
transfer can use their existing coverage without a general reproof.
No extension of L099 is proved in this literature turn.

Queries were `Mochizuki "Corollary 2.2" "P2" "P3"`,
`Mochizuki "prime" "local heights" "Lemma 4.1"`, and
`"inter-universal" "prime" "good reduction" "Corollary 2.2"`.
Search hits supplied no stronger inspected integrality statement.
The IV reproduction was read at printed pp.40-46, including the
complete height estimates and the later ell-contribution case.
GenEll's journal endpoint timed out; its already adequate local-height
coverage in step394 is reused. This optional failed fresh retrieval
does not block the inspected IV selection statement. Search-only
hits, including formalization leads, are not theorem inputs.
Full matching or supporting Mathlib coverage remains unchecked.

### Continuation and discriminating test

The next independent target is conditional transfer of P2 from G_o
to C_o and rational pole orders, allowing an ell-pole. Its separate
assessment is
`2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`.
Approval belongs to the next invocation; no transfer is derived or
approved by a new lemma here. A later proof must verify semistability
and the downstairs height at actual G_o-places, compare actual
extending places of C_o, and retain ell>=7 and every p in S. If a
normalization or ramification assumption fails, abandon that transfer
claim. Even success would leave ell-integrality, simultaneous source
exception avoidance and all independent repair conditions unresolved.
