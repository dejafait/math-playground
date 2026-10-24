# Native omitted-ell term over the normal closure — completed source comparison

TARGET: Determine the exact hypotheses under which the source's omitted-ell term over C_o with selected moduli support S minus {ell} equals H_ell(C_o)/6.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step411 reused steps389/398/399/407/409, L092/L100/L101/L102, foundations/05 and ATTEMPTS/035; searched `Mochizuki "log(q" "Corollary 2.2" "1.9"` and `Mochizuki "q-pilot" "normalized" degree`, then inspected the definition-to-display chain in the primary reproductions. No matching changed-field specialization was imported or novelty inferred.
SOURCE_EVIDENCE: Fresh IUT IV April 2020 reproduction (87 pages), Definition 1.9(i)-(ii) pp.21–22, Theorem 1.10 hypotheses/definitions p.22–23, Corollary 2.2(i)-(ii) pp.41–43 and proof pp.44–47; fresh IUT I May 2020 reproduction (186 pages), Definition 3.1(b)-(e) pp.61–63 and Example 3.2(iv) p.71; reused inspected GenEll Definition 3.3/Remark 3.3.1 p.17 via step399. Optional fresh GenEll retrieval timed out; prior coverage suffices.
COMPARISON: The omitted display subtracts positive normalized arithmetic q-degrees, not negative pilot log-volumes; native pilot magnitude has the separate 1/(2ell) factor. Full inverse-image divisors and global degree normalization cover a later arithmetic dictionary over C_o; native pilot interpretation remains conditional on missing initial data, and Theorem 1.10's exact-generation premise is not repaired.
GAP: Execute only the all-place coefficient/support specialization on C_o, distinguishing arithmetic notation from an instantiated native pilot. Verify nonempty U=S minus {ell}, no extra omitted places, ordinary q-orders versus roots, and the exact denominator; do not establish P4–P7 or a repaired theorem application.
REASON: The essential source chain is now inspected. Known definitions and audited local heights suffice for this bounded specialization; the equality over this changed field is reserved for a separate mathematical turn, with no general reproof.
LITERATURE_REASON: Essential unread or uncompared definition-to-display links for the native omitted term over C_o are outside L102's approved numerical scope; reuse existing source readings and retrieve only those links.
SCOPE: Only TARGET for one L101 member/order/prime, F=G_o, C_o=G_o^nor, original downstairs H, S={p:v_p(j(E))<0}, U=S minus {ell}, fixed L089/L090 family/domains/closure, d=6, epsilon_d=1 and full-coordinate division fields; arithmetic specialization and explicit conditional native dictionary, without constructing initial theta-data or applying Theorem 1.10 over C_o.

## Completed review — 2026-10-23, step411

The completion here supersedes the pending-coverage language in the
preserved proposal below. This is one source comparison, with no new
lemma, arithmetic derivation or mathematical script.

The main gap is original finite B>=A. TARGET is the intermediate
identification needed before L102's numerical estimate can be used in
an omitted-term part of a possible normal-closure repair. The test is
to match source coefficients, complete fibers, sign and field, or to
stop at the precise missing premise. It does not require independently
settling the other repair obligations.

### Primary definition chain

Use [IV, April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
printed pages as above. Definition 1.9(i) weights finite-place
coefficients by log(#k_v) and divides the global degree by [F:Q].
Theorem 1.10 defines an effective q-divisor on the complete inverse
image of selected moduli places, using Galois intermediate fields
F_mod subset F' subset K. It defines log(q) as its normalized degree,
states field independence, and gives |log(q)|=log(q)/(2ell).
Corollary 2.2(i) defines the all-finite and non-dyadic variants.
Its proof p.44 gives H as the full height sum; P5 p.46 selects the
multiplicative places away from 2ell; p.47 subtracts the selected
degree from the non-dyadic degree, both with coefficient 1/6.

Use [I, May 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
Definition 3.1(b),(c) requires nonempty odd selected support, all
extending-place multiplicative reduction, Galois base of degree prime
to ell, full rational six-torsion, the large mod-ell image, and
selected residue/height coprimality. Clauses (d),(e) impose the
core/cover and section conditions. Example 3.2(iv) uses geometric
q-parameters and their 2ell-th roots, up to roots of unity.

The source statement relating the two q-normalizations is imported
as a definition-chain assertion, not a verification of III's disputed
comparison. The actual pilot has negative log-volume -|log(q)|;
the source's omitted display concerns the positive arithmetic
quantity. No extra 2ell is to be inferred from the displayed 1/6.

GenEll's extension-normalized local height, including nonsplit
reduction, is reused from the already inspected step399 assessment,
`2026-10-22-literal-to-normal-closure-selected-prime-transfer.md`,
Primary statements. The exact citation is *Arithmetic Elliptic Curves
in General Position*, Math. J. Okayama Univ. 52 (2010), Definition 3.3
and Remark 3.3.1, p.17; L100's separately audited specialization is
the local input here. No split model at every C_o-place is assumed.

### Obligations approved for the separate specialization

Use L089/L090 for the unchanged member, rational j and F_mod=Q;
L092 for C_o and its actual degree; L100 for semistability and the
integer height formula at every actual C_o-place; L101 for the same
ell and original downstairs H; and L102 only for the already audited
arithmetic contribution and estimate. Their conclusions are not
enlarged during this review.

The later proof should introduce explicitly arithmetic notation for
the source-shaped divisors over C_o, before assigning any native
meaning. Its exact test is

    Delta_C := (log(q^{not-dividing-2}_C)-log(q_{U,C}))/6
    Delta_C = H_ell(C_o)/6,       U=S minus {ell}.

These are proposed specialization statements, not results proved in
this literature turn. Required checks are:

- Identify every actual C_o-place contributing to each divisor.
  U must be nonempty and satisfy the selected reduction predicates;
  L089's retained pole at three, L101's ell>=7 and L100's all-place
  classification are available inputs for that check. Do not invoke
  L098's ell-integrality-dependent support conclusion.
- Use the source's ordinary q-parameter orders, with the GenEll
  nonsplit convention. Check them against L100's h_w. Use complete
  fibers with weights f_w log(p_w)/[C_o:Q], where f_w is the absolute
  residue degree. Do not replace them by one place from the section,
  by unweighted sums, or by a normalized E-degree from Definition
  1.9(ii). No extra ramification factor belongs on an integer h_w.
- Check all possible surviving places of the difference, including
  good places over ell with zero coefficient. Neither ell-integrality
  nor a positive omitted contribution is required by the proposed
  formula. No arbitrary pole other than ell may be omitted.
- Keep C_o as the arithmetic computing field. A hypothetical native
  realization with base C_o would use K_C=C_o(E_o[ell]) and F'=C_o.
  C_o is not asserted to lie in the old G_o(E_o[ell]); no such inclusion
  was checked. The full native data and III situation must be supplied
  separately before the arithmetic expression is called a pilot term.

Theorem 1.10 has additional hypotheses beyond defining an effective
arithmetic divisor. Its exact-generation requirement cannot simply be
retained on replacing G_o by C_o: in L090/L092's fixed literal-model
prescription the generated field remains G_o, and [C_o:G_o]=4.
This is the recorded obstruction, not a new nonexistence theorem for
all repairs. A conditional native dictionary must expose missing
initial data; it must not hide a complete repaired application in its
hypotheses or report one as constructed. The original factor-four
relative excess and essentiality questions remain independent.

### Reuse, limits and decision

Step389 compared reduction/support clauses; step398 checked prime
selection; step407 scoped arithmetic P3; L102 and step410 audited the
weighted transfer. None completed this changed-field dictionary.
The older q-pilot admissibility review and foundations/05 concern
markings and pilot-image regions, not this omitted arithmetic degree.
ATTEMPTS/035 parks authentication retries and does not prohibit the
different definition comparison carried out here.

The two recorded external queries supplied native-text leads and
unneeded exposition/formalization leads. Only the specified native
passages and reused inspected GenEll coverage are mathematical
sources; the newer *Explicit Estimates* paper was a search hit only
and was not used to alter the April formulation. Primary continuous
text was read at the cited ranges, including P5/P7 and the p.47
case. Screenshot calls returned references without viewable images;
no visual verification is claimed. Reproduction authentication and
the explicit def= qualification remain exactly as in L091; no retry
of the parked author/journal authentication route was made.

SPECIALIZE approves the separate arithmetic/conditional-native
application above, classified REPRODUCTION. Continue only if the
complete coefficient comparison gives exactly Delta_C=H_ell(C_o)/6;
a support, sign or denominator mismatch must be recorded rather than
repaired by assumption. Then L102 may be cited for the existing bound.
If native data cannot be instantiated, report that limitation while
retaining any proved arithmetic dictionary. No general theorem needs
reproof, and no result beyond checked sources is claimed. Full and
supporting Mathlib coverage remain unchecked. PROOF.md and DAG.md
are unchanged because this review adds no mathematical argument.

## Preserved proposal at invocation start

The main gap remains original finite B>=A. This comparison could
determine whether the verified numerical transfer supplies the omitted
term needed by a possible normal-closure repair, or precisely which
additional data prevent that use. It is not a proposed proof of P7
or of the original comparison.

Essential inputs are L092,L100,L101,L102; L089/L090 fix the inherited
family and field conventions. L097's explicit full-pole-support bound
and L098's conditional support result are existing comparisons, not
permission to delete their hypotheses. Read their relevant ranges only
if the selected-divisor comparison actually requires them.

Reuse `2026-10-21-native-selected-support-comparison.md`,
`2026-10-22-height-selected-prime-avoidance-comparison.md` and
`2026-10-23-normal-closure-p3-and-omitted-ell-height.md` first. Then
trace the native definitions actually used in the cited p.47 display:
identify both q quantities, their sign and denominator, the underlying
base/ell-division fields, and the full fibers represented by the
selected support. Check whether the proposed support must satisfy
additional conditions before the expression is defined, including
nonemptiness and the all-place reduction clauses. No support or
native-term identity is derived in this proposed assessment.

The decision test is a precise conditional dictionary with all essential
source hypotheses inspected. If the expression needs missing theta-data,
record those requirements explicitly and determine whether only a
conditional arithmetic identification can be approved. A mismatch of
weights, sign or field is a limitation, not permission to equate the
quantities. Repeated authentication attempts are parked by ATTEMPTS/035;
retain the April/May reproduction and explicit def= qualifications.

Do not assume ell-integrality, P4–P7/full selected-theta data, exact
generation, a complete repair or removal of the relative factor-four
excess. Native input/action/factorization/pilot, essentiality and finite
B>=A remain unresolved. Mathlib coverage is unchecked. This is a new
REVIEW_REQUIRED continuation, not a newly approved mathematical target.
