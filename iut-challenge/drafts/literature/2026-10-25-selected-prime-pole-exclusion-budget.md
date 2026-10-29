# Rational pole-prime exclusion — source comparison for the budget test

TARGET: Test whether adding the rational j-pole primes to L101's excluded primes preserves its weighted sieve budget and yields v_ell(j(E))>=0 within the same P1+ interval.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step474 reused the completed step398/403 selection assessments; read L101's height/selection/audit, L098's conditional support premise and L105's scope; screened ATTEMPTS/035 and targeted local pole-exclusion/failure records. Bounded searches located the later primary Explicit Estimates paper; queries, inspected passages and search-only leads are distinguished below. No exact enlarged-pole-exclusion theorem was located; no novelty is inferred.
SOURCE_EVIDENCE: Mochizuki, IUT IV, April 2020, 87-page reproduction https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf Proposition 2.1(ii) p.40 and Corollary 2.2(ii) proof pp.44–45, complete normalized height and S1–S3 weighted displays; reuse antecedent/P4–P7 coverage from step398/403. Mochizuki–Fesenko–Hoshi–Minamide–Porowski, Explicit Estimates in Inter-universal Teichmuller Theory, Kodai Math. J. 45 (2022), 175–236, https://ivanfesenko.org/wp-content/uploads/eeiutp.pdf Proposition 2.2(ii) pp.197–198 and Corollary 5.2 selection proof pp.213–214, with antecedent pp.211–212, inspected as a stronger-result comparison only.
COMPARISON: IV's arbitrary finite-prime-set theorem covers an enlarged exclusion set, but its existing bound covers only S1–S3. The remaining specialization is the union's added pole-prime weight within the unchanged interval, with overlaps counted once. The later paper improves constants and raises the height threshold, but retains S1–S3/P1–P3 and does not supply good reduction at ell. Neither L101 nor L105 already proves this refinement.
GAP: A later mathematical attempt must bound the additional weight and compare it with the exact finite-set existence benchmark below; no such bound, sufficient-budget verdict or refined prime is proved here. Failure of a sufficient estimate would stop this automatic enlargement, not disprove existence or IUT.
REASON: Essential source statements, weighted proof cases, duplicates and a stronger relevant primary lead have now been compared. Only the bounded cost calculation remains; general prime counting is imported by citation rather than reproved. This newly completed coverage is subject to the supervisor's separate next-turn approval.
LITERATURE_REASON: Adding all interval-relevant rational j-poles changes the exclusion set beyond the ready step398/403 assessments; its precise finite-set budget and stronger-result comparison were essential unread coverage.
SCOPE: Exactly TARGET for one L089-L090 member/order, literal F=G_o, L101's H, d=6, delta=3317760, fixed domains and finite exceptions before selection; original P1+ interval and P2/P3 retained. No L105 large-image conclusion for a newly selected prime is included; no field/family/interval change or effective-PNT substitution is approved.

## Original proposal (retained)

Main gap remains original finite B>=A. The proposed intermediate is a
specific missing hypothesis for L098's support comparison. A successful
sieve refinement could supply that hypothesis while retaining the same
selected member and original fields; a failed bound would rule out
this particular automatic strengthening, not ell-integrality itself.

Keep L101's source height H over the literal F=G_o and its interval

    sqrt(H)<ell<=10 delta sqrt(H) log(2 delta H).

Use S={rational primes p : v_p(j(E))<0}. The proposed added exclusions
are the primes in S relevant to this interval, together with the
source's already required exclusions. Review the exact weighting,
union overlaps, quantifiers and sufficient inequality before attempting
to bound the new cost. Do not replace H by the C_o or ell-division-field
height, or make the fixed exceptional set depend on the chosen member.
No inequality for this new exclusion cost has been derived or approved.

Essential input IDs for a later application: L089,L090 for the family,
literal fields and invariant; L098 for the conditional downstream use;
L100,L101 for the height/prime-selection transfer; L105 if its retained
large-image choice is claimed. First inspect only the relevant selection
proof ranges and existing source assessment. The complete primary
selection inequalities and any stronger result must be covered before
research. Existing ready coverage should be reused, not retrieved again
merely to repeat its original no-integrality conclusion.

Continue only if a sufficient budget inequality for the enlarged
exclusion set follows from the retained hypotheses. If their available
bounds do not suffice, record the precise deficit and stop this automatic
enlargement mechanism; do not treat a sufficient-bound failure as a
counterexample or silently enlarge the prime interval. Any changed
family or interval is another target requiring review.

This is distinct from the completed all-place pointed-model audit,
blocked directed-module extraction, repeated IV authentication and
stopped Frobenius-power separator. Those records remain intact.
The source reproduction/journal-equivalence limitation remains.
Full initial data, directed (*), generation/full repair, factor-four
excess, action/factorization/pilot, essentiality and finite B>=A remain
independent. Matching and supporting Mathlib coverage is unchecked.
This proposal does not authorize a derivation in step473 or claim
novelty, adequate coverage or a complete candidate.

## Completed comparison — 2026-10-25, step474

This is approval of source coverage for a later cost test, not a result
of that test. Original finite B>=A remains open. Successful refinement
could supply the additional premise of L098's selected-support bridge;
L115's pointed reduction does not supply it. No lemma or mathematical
script is written, and no new mathematical estimate is derived here.

### Source statements and proof cases actually inspected

Use the qualified [IV April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=40).
Proposition 2.1(ii), printed p.40, has an absolute xi>=5 and

    (2/3)x <= theta(x) <= (4/3)x  (x>=xi),
    theta(A)=sum_(p in A) log p,
    some prime outside A is <=2(theta(A)+xi)

for every finite set A of rational primes, including the empty set.
Its proof cites PNT (Edwards p.76 and GenEll Lemma 4.1/Remark 4.1.1).
No special elliptic-curve hypothesis restricts this finite-set theorem.
These references are not independently reproved or freshly verified.

The Corollary 2.2(ii) proof, pp.44–45, uses nonnegative integer
semistable heights, finite support, [F:Q]<=delta, and sqrt(H)>=xi,
with H=[F:Q]^(-1) sum_v h_v f_v log(p_v). Its displayed estimates are

    sum_(h_v>=sqrt(H)) log(p_v) <= delta sqrt(H),
    sum_(h_v>=sqrt(H)) log(h_v)
        <=2 delta sqrt(H) log(2 delta H).

The intermediate sums retain f_v>=1 and the factor H^(-1/2)h_v;
the second uses 2log(p_v)>=1. S1 comprises primes <=sqrt(H), S2
divisors of nonzero h_v, S3 the p_v with h_v>=sqrt(H). The source
then gives, for their union A,

    theta(A) <=2sqrt(H)+delta sqrt(H)
                   +2 delta sqrt(H) log(2 delta H)
             <=4 delta sqrt(H) log(2 delta H)
             <=-xi+5 delta sqrt(H) log(2 delta H).

Small positive h_v have no prime divisor exceeding sqrt(H), so their
divisors are already covered by S1; large h_v are the displayed second
sum's case. This explains the source's S2 accounting rather than
introducing a new bound. S3 controls only large local heights, hence
the ensuing P3 remains a strict upper bound and does not impose zero.
L101 has already checked these statements' literal-field, all-place
and strict-endpoint specialization; no reproof is needed here.

The full antecedent and later P4–P7 coverage in the completed
`2026-10-22-height-selected-prime-avoidance-comparison.md` and
`2026-10-22-same-member-simultaneous-prime-selection.md` is reused.
The authentication/def= qualification is unchanged; no current
author-byte identity or complete initial-data assertion is imported.

### Stronger primary result compared, without importing its IUT claims

Mochizuki, Fesenko, Hoshi, Minamide and Porowski,
[*Explicit Estimates in Inter-universal Teichmuller Theory*](https://ivanfesenko.org/wp-content/uploads/eeiutp.pdf),
Kodai Mathematical Journal **45** (2022), 175–236, received
1 December 2020/revised 18 June 2021, has an independently stated
Proposition 2.2(ii), printed pp.197–198:

    |theta(x)-x| <=0.00071 x  (x>=10^15),
    some prime outside any finite A is
       <=(1-0.00071)^(-1)(theta(A)+10^15)
       <=1.00072(theta(A)+10^15).

Its proof reduces the theta estimate to Rosser–Schoenfeld,
*Sharper Bounds for the Chebyshev Functions theta(x) and psi(x)*,
Math. Comp. **29** (1975), 243–269, Theorem 7. That underlying
proof was not independently checked; the later proposition is a
read primary statement, not a fresh verification of its constants.

Corollary 5.2's antecedent, pp.211–212, retains a prescribed
full-coordinate torsion adjunction and a fixed exceptional set, with
additional k/height or mono-complex alternatives. Its selection proof,
pp.213–214, first requires sqrt(H)>=10^15 delta, then uses the same
S1–S3 and yields P1 with upper bound
1.464 delta sqrt(H) log(1.45 delta H), P2, and still P3 with
h_v<sqrt(H) above ell. The sharper weighted display and the passage
to P1–P3 were read, not inferred from the abstract. This inspected
selection has no all-pole exclusion. No general IUT conclusion,
changed m6 theory, mono-complex applicability, heightened-threshold
selection or replacement constant is used in the proposed test.
This is a stronger relevant lead whose stated conclusion does not
settle the target; it is not a new essential source blocker.

### Exact future test and its quantifiers

The future attempt retains L101's input height and interval. Put

    U=10 delta sqrt(H) log(2 delta H),
    S={p : v_p(j(E))<0},
    S_I=S intersect (sqrt(H),U],  A'=A union S_I.

The source's finite-set theorem supplies the following benchmark to
test, without any need to prove a new prime-distribution theorem:

    2(theta(A')+xi) <= U.                         [test only]

No value or upper bound for theta(A') is established by this review.
In particular the source's bound for theta(A) may not simply be
reused for A'. The later calculation must account for A-overlaps,
the interval cutoff, the residue-prime/height-divisor distinction,
and all F-places. Using all S is a potentially stronger sufficient
test, but a deficit from counting poles outside the interval must
not be presented as failure of the interval-relevant test.

L101's existing formula H=sum_p max(0,-v_p(j(E)))log p, for rational
j(E), is the available arithmetic input, not a new result of this
review. Whether it gives a sufficient added-cost bound is precisely
the unperformed calculation. A conclusion for arbitrary nonnegative
height arrays is not automatically a conclusion for actual L089
members; any illustrative obstruction must be labeled accordingly.

Keep all exceptional sets fixed before selecting the member. Work
existentially within the unchanged family and then retain that member,
order and literal F. No post-selection deletion of an inconvenient
prime or member is legitimate. An arbitrary existing L101 witness need
not have a second acceptable prime. L105's same-member large-image
argument is not automatically a theorem about a reselected prime;
retaining that conclusion would require checking its additional
pre-selection exception and same-prime hypotheses separately.

Continue if a sufficient bound passes this benchmark under the
retained hypotheses. Otherwise record the actual sufficient-bound
deficit and stop the automatic strengthening, distinguishing it from
nonexistence. The unchanged finite-set method and rational-height
specialization are the approved mechanism; a new family, interval or
arithmetic distribution estimate needs its own assessment.

### Search, overlap, failure record and remaining limits

Bounded queries included `Mochizuki "Corollary 2.2" "good reduction"
prime`, `"Mochizuki" "S1" "S2" "S3" primes height`,
`"Inter-universal Teichmuller" "Proposition 2.1" prime`,
`"Mochizuki" "prime" "good reduction" "height"`,
`"elliptic" "least prime of good reduction" height`, and
`"Inter-universal Teichmuller Theory IV" "S3"`. Follow-up queries
used `"elliptic curves" "prime of good reduction" "height" bound`
and `Rosser Schoenfeld "Sharper bounds" "Theorem 7" 0.0242269`.
Only the two primary PDFs above enter the comparison. Yamashita's
2017 exposition and older IV preprint were search-only leads; generic
good-reduction/density hits do not supply this same-interval assertion.
No inference of originality is made from failure to locate a match.

The scoped duplicate/failure screen covered L101's normalized-height
and prime-selection proofs/audit, L098's explicit extra premise,
L105's no-integrality and existential-choice qualifications, the
completed step398/403 assessments, history/473's distinct proposal,
and ATTEMPTS/035. The parked authentication route is not reopened.
No prior completed enlarged-pole-budget estimate was found there.
The existing P3 limitation is motivation, not this step's new result.

Fresh PDF retrieval succeeded as continuous text. Screenshot calls
returned no inspectable images, so no visual-page verification is
claimed. Printed locators above distinguish the journal PDF's page
numbers from its zero-based PDF page indices. Complete matching and
supporting Mathlib coverage is unchecked, not asserted absent.

Essential input IDs remain L089,L090,L098,L100,L101; L105 is only a
qualification unless separately retained. Full initial data/III/P7,
directed (*), generation/repair, relative factor-four excess,
action/factorization/pilot, authentication/def=, essentiality and
finite B>=A remain unresolved. This review neither supplies the
missing integrality premise nor proposes a complete flaw candidate.
