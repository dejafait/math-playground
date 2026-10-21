# Separating the rational eleven-adic places — source comparison

TARGET: Construct a supported norm-square unit in V_S whose valuation parities at the two rational eleven-adic degree-one factors are unequal.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L073/L074/L076 and audited L077 with ATTEMPTS/032–033 and the ready supported-unit assessments; searched exact defining data, norm-square S-units, prescribed valuations, principal ideals and relative norm algorithms; inspected the primary passages and qualifications recorded below. No exact witness or universal equality theorem was found in the inspected sources.
SOURCE_EVIDENCE: Milne ANT v3.08 (19 July 2020), Theorem 5.11 and full valuation-map proof p.90, norm definition and Proposition 4.1(a),(c) with full nonnormal proof pp.68–69, https://www.jmilne.org/math/CourseNotes/ANTc.pdf ; official PARI stable General number fields, entries bnfcertify/bnfinit/bnfisprincipal/bnfsunit/bnfunits/idealappr/idealfactor/idealval/nfeltval, accessed 2026-10-16, https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html ; reuse the inspected Simon/Stacks/BPT and local-image inputs identified below.
COMPARISON: Known S-unit, principal-ideal and exact norm methods cover a certificate attempt; L077 excludes separation only within its complete rational-cubic family. Neither S-unit rank nor local approximation supplies the requested parity witness, and none of the inspected sources establishes its existence or a global equality obstruction in this D.
GAP: Essential method coverage is ready; existence of the separating supported unit, its supported inverse, exact square relative norm and ordered maximal-prime valuations remain mathematical obligations. A complete negative result would require complete generators or a proved global obstruction, not a failed finite search.
REASON: Approve one later bounded specialization of established methods to the unchanged target, with exact witness verification; do not reprove the general S-unit theorem or launch an uncertified full-field computation.
SCOPE: Exactly TARGET in the full D/K of L069 and support of L074/L076; one bounded witness or supported-principal-ideal attempt, including support, norm and both ordered valuation certificates. No full D-unit basis, class-kernel value, rank or integer exclusion is preapproved as an assumed input.
LITERATURE_REASON: The proposed witness moves beyond L077's complete rational-cubic family; exact-target discovery and comparison of global principal-ideal and norm certification were essential unread coverage at invocation start.

Use exactly the fields K and D and support above two and eleven from
L033, L069 and L076. The two factors in the target are the degree-one
D factors over the two rational base completions of L041, ordered
consistently with L073. Valuations are maximal-prime valuations modulo
two, not residue symbols or rationally rescaled ramified valuations.
Any proposed witness must be nonzero, be an actual supported unit with
supported inverse, and have square D/K norm. Global squares and scalar
quotients must not be substituted for the specified V_S.

Essential inputs: L033, L041, L069, L073, L074, L076, L077. L071/L046
remain available for interpreting the existing dyadic restriction.
No cross-notebook result is proposed. The existence of a separating
unit and the required principal-ideal arithmetic are unresolved; no
complete D-unit basis or localized class-kernel value is assumed.

Plausible downstream use: a separating class could supply a restriction
direction beyond L077's complete rational-cubic family. It would still
leave further pruning to eleven, the localized class contribution and
primitive integer lifting. The source comparison should seek exact or
stronger results and relevant obstructions before choosing a bounded
certificate construction. A certified separating witness would justify
continuation; an equality obstruction would stop this separation test.
A failed bounded search alone would establish neither alternative.
Persistent source blockers require an independent target. Preserve
ATTEMPTS/032–033: this proposal retains exceptional support and imposes
actual local restrictions, without reopening either stopped premise.

## Local overlap and recorded failures

L077, Hypotheses/Conclusion and its complete rational-eleven comparison,
supplies the full family from Q(t), t³−t²+t+1=0, with basis v,w and
two identical eleven-adic rows (0,1). Searching that same family again
cannot meet this target. L076 supplies the full supported dimension
sixteen and all nine primes of D, including both distinct degree-one
primes at eleven. It does not give their principal generators. L073's
full rational-place Kummer images have even component valuations at
both base places. Its odd class at the degree-ten place remains part
of the necessary exceptional support; it is not a global unit witness.

The proof ranges used were L073's hypotheses, conclusion, entire
rational-place image and ramified splitting arguments; L074's
definitions and explicit norm/choice argument; L076's definitions,
eleven-adic factor count and S-unit norm dimensions; and L077's
definitions, full family and rational-eleven comparison. Targeted
searches of the associated attempt and histories 248/250 found no
previous separating witness or global equality proof. The ready
assessments reused are
`drafts/literature/2026-10-16-rational-cubic-supported-pruning.md`
and `drafts/literature/2026-10-15-supported-norm-square-nonunit-quotient.md`.
Their source scope supplies general arithmetic, not this new witness.

ATTEMPTS/032's unfiltered dimension obstruction and ATTEMPTS/033's
counterexample to deleting eleven remain unchanged. This target
retains support and asks for an actual class on which a necessary
restriction acts. No historical stop is treated as a global ban.

## Primary theorem comparison

J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
[author PDF](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 5.11, printed p.90 (PDF p.92), applies to any number field
and finite set of maximal primes. The statement and complete proof
were inspected. Its valuation map has ordinary units as kernel;
principal generators of h-th powers of supported primes establish
full valuation rank, with h the class number. This does not assert
odd h or surjectivity modulo two. Thus the theorem cannot import the
requested witness from the dimension count. Prescribed supported
divisors still require principal-ideal evidence.

The norm definition and Proposition 4.1(a),(c), printed pp.68–69
(PDF pp.70–71), including the complete nonnormal proof, were also
inspected. For a finite separable extension and integral closure of
a Dedekind ring, ideal norm uses residue degrees, agrees with norms
of principal ideals, and sends extended ideals to degree-th powers.
Normality is not needed for these clauses. These cover support/norm
bookkeeping, without supplying element square roots or generators.

Reuse the second ready assessment above for Simon, *Computing the
rank of elliptic curves over number fields*, LMS J. Comput. Math.
5 (2002), Section 1.2, Proposition 1.3, pp.8–9; Stacks
[Lemma 10.36.11, Tag 0307](https://stacks.math.columbia.edu/tag/0307);
and BPT arXiv:2001.02263v3, Lemma 2.14, pp.12–13. The inspected
support/class-square description, localization of integral closure
and odd-degree scalar-unit argument apply to the unchanged groups.
L074 supplies the local justification and explicit norm correction;
its unsquared-norm surjectivity is never assumed. No new general
norm theorem needs reproof. Reuse L073 and the first ready assessment
for full local images and maximal-DVR conventions.

## Unconditional certificate methods and limitations

The [official PARI stable catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
accessed 2026-10-16, has no printed release identifier on this page.
The named entries, examples and flags were inspected. `bnfinit(P,1)`
retains exact data; unconditional completeness needs
`bnfcertify(bnf,0)=1`. Flag one certifies weaker information.
`bnfunits(bnf,S)` includes ordinary and torsion units;
`bnfsunit(bnf,S)[1]` is only modulo ordinary units.
`bnfisprincipal` supplies ideal generators; exact ideal equality can
verify a positive output. `idealval`/`nfeltval` use maximal primes.
`idealfactor` with a limit is partial. `idealappr` permits positive
valuations at unlisted primes, so approximation alone is insufficient.

`gp` was absent from PATH when checked in this turn. No backend was
installed or executed, and no runtime or class-group completeness is
claimed. A direct alternative is to exhibit the element and its inverse
in a specified integral order localized at 22, verify their product
exactly, give an exact relative-norm square witness in K, and certify
both ordered valuations by proved completion arithmetic. Such a
positive certificate needs neither full unit generation nor a
class-number assertion. This is a verification specification, with no
element, ideal relation, norm identity or valuation calculated here.
If maximal ideals are used instead, retain exact field identifications,
maximal-ring correctness and a complete supported ideal factorization.
Power-order reduction alone does not identify maximal primes.

## Search record and optional unread leads

Queries included `"norm" "S-units" "prescribed valuations" number fields`,
`"X0(11)" "units" number field descent`,
`"S-units" "principal ideals" norm kernel computation`,
`"norm-square" "S-unit" "valuation"`,
`"X^3-4X^2-160X-1264" "unit"`,
`"9261/8" "S-units"`, `"1264" "9261/8" descent units`,
`"S-units" "prescribed" "parity" norm`,
`"S-units" "norm kernel" principal ideal`, and searches for Simon's
relative-norm paper. A query on the beginning of K's defining
polynomial was also tried. The exact-data searches supplied no usable
matching theorem. Irrelevant hits, discussion forums and generated
research posts were not used as mathematical evidence. This bounded
comparison does not establish novelty or completeness of the literature.

Simon's author publication list confirms *Solving norm equations in
relative number fields using S-units*, Math. Comp. 71 (2002),
1287–1305, DOI 10.1090/S0025-5718-02-01309-1. The linked AMS PDF and
a CiteSeer mirror failed retrieval. Its theorem hypotheses and proof
were NOT inspected; no theorem from that paper is imported. General
relative-norm solvers can enlarge support, so they must not silently
replace this fixed-support problem. Subfield principal-ideal algorithms
and normal-extension norm-relation search hits were not opened and
remain optional unread leads. They are unnecessary for the direct
positive-certificate test approved here; no dependent source blocker
is being concealed as ready coverage.

## One bounded mathematical continuation

Keep TARGET exactly as written. Before any search, save its finite
candidate family or ideal list and a stopping cap in a draft. Work
outside the exhausted rational-cubic family and use one exact
certificate strategy above. A proposed element must retain the same
K, D, distinguished generator and both base embeddings. Check every
support and norm obligation, then the actual unequal maximal-prime
parities; a norm valuation alone is not a square-norm certificate.
If a scalar norm correction is used, its effect on these parities
must be checked after correction, not assumed harmless.

A fully certified witness meets this intermediate target and permits
testing the additional restriction direction. A complete obstruction
forcing equal parities stops this test. Exhausting the recorded finite
list only rejects that list; it proves neither existence nor universal
equality. Backend absence is not mathematical evidence. Do not extend
the search without a new discriminating idea or claim a third direction
before its independence is justified. Other units, localized class
contributions, pruning from fourteen to eleven and primitive integer
lifting remain unresolved.

This LITERATURE turn approves the unchanged target for a subsequent
RESEARCH attempt classified REPRODUCTION of the assessed methods.
No new lemma, mathematical script, specialized witness or nonexistence
claim was produced. Mathlib coverage of the full target and supporting
arithmetic interfaces is not checked; unknown availability is not absence.
