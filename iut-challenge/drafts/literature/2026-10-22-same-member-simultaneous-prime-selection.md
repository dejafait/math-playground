# Same-member simultaneous prime selection — completed source comparison

TARGET: Apply the inspected P1–P3 prime construction to a same-member L089-L090 literal field outside a fixed finite exceptional set, obtaining ell>=7 and L100's P2 premise.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step403 reused step398's prime-selection assessment, L089/L090 hypotheses, L091's finite-exception/antecedent proof, L092's audited degrees, L100's hypotheses/audit and ATTEMPTS/035; targeted searches followed the height-finiteness reference and located Silverman's primary Northcott statement. Exact retrievals and limitations are below; no originality is inferred.
SOURCE_EVIDENCE: Inspected April 2020 IV reproduction, Proposition 2.1(ii) p.40, Corollary 2.2(i)–(ii) pp.41–43, proof pp.43–45 through S1–S3/P1–P3, and degree inputs E3–E5 p.24; Silverman, Canonical Heights on Abelian Varieties, 13 February 2024, Definitions 4.4–4.5/Proposition 4.6 pp.13–14 and Theorem 4.8(a)–(d) p.15. Reused GenEll Definition 3.3/Remark 3.3.1 p.17 from the ready transfer assessment; fresh detailed GenEll retrieval failed.
COMPARISON: The prime-selection subargument needs semistable integer local heights, [F:Q]<=delta and sqrt(H)>=xi_prm; it precedes P4–P7 and uses no Galoisness of F/Q. Existing inputs cover the literal field and degree. IV's bounded-discrepancy height comparison and Northcott cover the finite-threshold method. The source chooses outside all primes <=sqrt(H), a stronger detail than the weak lower inequality printed in P1.
GAP: A later research turn must fix the finite exceptions including the low-height set before selecting the member, identify its actual normalized G_o-height, and apply the simultaneous construction for one ordering; check ell>=7 from the strict S1 exclusion before invoking L100. No application or selected prime is established here; essential source coverage is ready.
REASON: Target-specific degree, height, finite-exception and normality comparison is now complete, with a precise independent finiteness citation; the remaining work is a known-method specialization, not further source approval or a reproof of prime selection.
LITERATURE_REASON: Actual simultaneous selection and the finite-height threshold were outside the earlier conditional-transfer scope; this required the separate review requested at invocation start.
SCOPE: Exactly the saved target, same fixed L089 family/domains/closure, d=6, epsilon_d=1, any fixed finite exceptional parameter set, one arbitrary fixed ordering, literal full-coordinate G_o and C_o=G_o^nor; no common prime for six orderings, P4–P7, ell-integrality or complete repair.

## Original proposed scope (retained)

The main gap is original finite B>=A. This target would replace L100's
conditional premise by an actual simultaneously chosen prime for one
fixed ordered model of a surviving member, after the finite exceptional
set has been fixed. It would clear one further prerequisite for a
possible normal-closure repair, without removing the relative degree
excess or proving ell-integrality.

Essential inputs are L089, L090, L091, L092 and audited L100. Keep the
same family, closure, domains, d=6, epsilon_d=1, full-coordinate G_o
and C_o=G_o^nor. Use H for the source height, distinct from L089's
congruence modulus. Check the actual finite-exception quantifiers and
height threshold; do not infer unbounded height through an unproved
change of convention. A prime common to all six orderings is not
requested. For an arbitrary fixed ordering, all three clauses must
concern the same prime and G_o. Neither P4–P7 nor full initial data
may be assumed to justify the earlier prime construction.

Reuse `2026-10-22-height-selected-prime-avoidance-comparison.md` and
the general local coverage in
`2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`.
Further literature is justified by the changed scope: actual
simultaneous existence and height/finite-exception specialization,
which L100 leaves conditional. Distinguish inspected statements from
uninspected leads before approval. ATTEMPTS/035 remains parked;
preserve the April reproduction/def= qualifications. Mathlib unchecked.

Continue only if the source construction applies to the literal
field and gives ell>=7 with P2 together with P1 and P3. If it depends
on an unavailable height threshold, normality or later initial data,
record the precise obstruction instead of importing a circular
conclusion. This is a proposed test, not a proof or source approval.
Integrality/native support, full selected/theta data, exact generation
and repair, native input/action/factorization/pilot, essentiality and
finite B>=A remain unresolved.

## Completed review — 2026-10-23, step403

This is source approval for a later attempt, not that attempt. The main
gap is still finite B>=A. The intermediate target is actual simultaneous
P1–P3 on a literal field; its plausible use is to supply L100's P2 premise
for a possible normal-closure repair. L092's relative factor-four excess,
ell-integrality/native support and all essentiality obligations remain
independent. No new lemma or mathematical script is written.

### Precise imports and source limits

Reuse the inspected [April 2020 IV reproduction, 87 pages](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Proposition 2.1(ii), printed p.40, provides an absolute xi_prm>=5,
the two Chebyshev-function bounds for x>=xi_prm and the finite-prime-set
existence estimate. Corollary 2.2(ii)'s proof, pp.44–45, applies it to
S1–S3 and states simultaneous P1–P3. Import this construction by citation;
no new prime-counting estimate or reproof is needed. The displayed proof
cases, including the height sums, were read, rather than inferred from
the final corollary's initial-data assertion.

For the height threshold, Corollary 2.2(i), pp.41/43, compares the
normalized total q-height on K_V with a height of the degree-one
log-canonical bundle on P^1. The proof of (ii), p.44, explicitly uses
this comparison and GenEll Proposition 1.4(iv) to put the low-height
parameters into a finite exceptional set. This part occurs before
the prime choice. It does not invoke the numerical conclusion (C2).

The finiteness input can be cited independently as Silverman,
[*Canonical Heights on Abelian Varieties*, AWS notes, dated 13 February
2024](https://swc-math.github.io/aws/2024/2024SilvermanNotes.pdf#page=15),
Theorem 4.8(d), printed p.15: for a smooth projective variety over a
number field and an ample divisor, bounded absolute logarithmic height
and bounded degree over that number field give a finite point set.
Definitions 4.4–4.5 and Proposition 4.6, pp.13–14, specify absolute
normalization and field independence; 4.8(a)–(c), p.15, give bounded
change under linear equivalence, functoriality and additivity. These
are named standard height results, imported without reproof. The
relevant prospective specialization has base Q, variety P^1, an ample
degree-one divisor and parameter degree at most six. A later proof
must use the actual q-height comparison, rather than replace it by
coefficient size or by the fixed congruence modulus h=3^M.

The local height is exactly the convention already inspected in
[GenEll, Definition 3.3/Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf#page=17)
and used in audited L100: integer order in the split case, extended
by division by the splitting ramification index. Its general local
coverage is reused from
`2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`.
No new local-height theorem is needed. Full matching Mathlib coverage
for the simultaneous selection/specialization is unchecked.

### Applicability comparison and obligations of the next proof

| Source hypothesis or quantifier | Existing coverage and remaining specialization |
| --- | --- |
| Fixed compact domains in the open lambda-line, support including two, bounded dyadic j | Audited L089 supplies exactly these domains with N=0. Keep them fixed before all finite exceptions and the survivor. |
| Literal prescribed F and full rational 15-torsion | L090/L091 identify T=F_tpd=Q(t_o) and G_o=T(iota,E_o[15]) with both coordinates. Retain L091's explicit def= reading; an independent ordinary F_mod-model division-field condition is outside the verdict. |
| Parameter degree <=d, absolute field degree <=delta | L089 supplies the parameter bound six; L092 already records [G_o:Q]=276480 and delta=3317760 for d=6. These are distinct degree conditions. Do not replace G_o by C_o when defining the source height. |
| Semistable curve and nonnegative integer h_v at every finite F-place | Audited L100 proves precisely this for G_o, including nonsplit multiplicative places. No G_o/Q normality is required. |
| Normalized total height | IV p.44 defines H=[G_o:Q]^(-1) sum_v h_v f_v log(p_v). The later proof must identify these h_v with L100's actual downstairs heights before using P2. No ell-division field enters. |
| Finite exceptions and sqrt(H)>=xi_prm | IV's height comparison and the inspected Northcott theorem cover the source's low-height exclusion method. The later proof must form the finite union with the initially fixed exceptional set before choosing its survivor, using L091's all-six finite-avoidance argument. Infinitely many equations alone would not suffice; L089 supplies distinct moduli. |
| One prime satisfying all three clauses | The same exclusion set A contains S1 (all primes <=sqrt(H)), S2 (all divisors of nonzero h_v) and S3 (residue primes of heights >=sqrt(H)). The cited construction selects outside this one set. The ell>=7 check must retain S1, not rely only on the weaker printed P1 lower inequality. |
| Later initial data | P4 starts after P1–P3 on p.45; neither P4–P7 nor Galoisness over F_mod occurs as a premise of the reviewed selection subargument. Its failure at fixed-F P7 does not block this earlier test. |

This comparison finds no essential missing source hypothesis for the
saved attempt. It does not choose a member, construct the finite union
for this family, establish its height threshold or assert an actual
selected ell. Those are the later mathematical specialization.
For any fixed ordering all clauses must concern the same G_o and prime;
no prime common to every ordering is requested. Apply L100 only after
its ell>=7 and P2 hypotheses have actually been discharged.

### Search record, duplicates and retrieval failures

Reused step398's general P1–P3 comparison; this review addresses its
explicitly unfilled actual-survivor/threshold scope. L091 handles finite
avoidance and the displayed antecedent but deliberately does not apply
prime selection. L092's exact degrees and L100's local height proof
prevent unnecessary reproofs. L098–L099 retain their extra integrality
assumptions; none is inferred from P3. ATTEMPTS/035's repeated IV
authentication mechanism remains parked. The April reproduction and
def= interpretation are qualifications, not newly authenticated facts.

Targeted queries included `Mochizuki "Arithmetic Elliptic Curves in
General Position" "finiteness"`, the author-hosted title, and
`Silverman Arithmetic Elliptic Curves "Northcott" "Theorem"`.
These located primary height coverage; only the opened Silverman theorem
and the inspected IV passages are new theorem readings used here.
The GenEll journal PDF initially supplied front matter, but detailed
page requests timed out; its institutional repository returned 429,
the author mirror timed out, and shell retrieval failed DNS. These
failures supply no detailed GenEll reading or version authentication.
The independently inspected Northcott statement supplies the required
finiteness coverage, so no dependent work is waiting on those endpoints.
Other search hits, including formalization leads, are not theorem inputs.
Screenshot calls returned no inspectable page images in this interface;
the source comparisons above use continuous extracted theorem/proof
text, not a claimed visual check.

### Continuation and abandonment test

Proceed to the exact TARGET using L089–L092 and audited L100, plus
the cited IV prime construction and Northcott/height comparison. Pass
only after exceptions are fixed before the member, the source degree
and normalized height have been checked, and one same-field prime
satisfies P1–P3 and ell>=7. Stop or narrow the application if a needed
height convention, finite-exception assertion or field interpretation
does not match; do not insert P7 or normality to repair the proof.
Even success would clear only L100's conditional premise. Native
support/integrality, exact generation and complete repairs, the relative
degree excess, native input/action/factorization/pilot and essentiality
remain unresolved, as does original finite B>=A.
