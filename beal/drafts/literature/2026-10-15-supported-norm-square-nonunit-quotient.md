# Exceptional-support norm-square space — completed source comparison

TARGET: Determine the quotient by norm-square S-units of the norm-square square-class space in D/K with even valuations outside primes above 2 and 11.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L069/L072, audited L073 and ATTEMPTS/032–033; searched S-unit norm/class two-torsion, S-class norm Selmer exact sequences, Dedekind localization and integral-closure localization; inspected Simon Proposition 1.3, Milne's localization and norm statements/proofs, and Stacks Tag 0307 as detailed below.
SOURCE_EVIDENCE: Simon, LMS J. Comput. Math. 5 (2002), Section 1.2 Proposition 1.3 pp.8–9; Milne ANT v3.08 (19 July 2020), Propositions 3.4–3.5 p.48, 3.23 p.55 and 4.1 pp.68–69 with their proofs; Stacks Project Lemma 10.36.11 Tag 0307, statement and complete proof, accessed 2026-10-15. Reuse prior BPT Lemma 2.14 coverage only for the odd-degree unit-square method.
COMPARISON: Simon already covers arbitrary finite support; Milne covers localized Dedekind ideal groups and norm compatibility without normality, and Stacks covers localization of integral closure. These supply the general inputs, but neither a norm-compatible splitting nor this field-specific quotient is stated in the inspected results. L072's ordinary criterion does not itself cover the changed groups.
GAP: Write the localized natural exact sequences and norm diagram, track the S-unit norm-lifting obstruction and every choice, then identify the quotient. No quotient formula, vanishing obstruction, S-class-group value, full Kummer containment or rank bound is established in this literature turn.
REASON: Essential source coverage for the changed support is now adequate for a separate specialization attempt; a short application proof is needed rather than assuming Simon's abstract splitting respects norm.
LITERATURE_REASON: The finite support changed from no exceptional primes to all primes above 2 and 11; the localization and relative-norm hypotheses required comparison beyond the ready ordinary-unit assessment.
SCOPE: Exactly TARGET for L033's entire K and L069's entire cubic field D, maximal rings, all primes above 2 and 11, and no sign restrictions; REPRODUCTION is approved for the localized sequence/application proof only, without arithmetic class-group computation or descent containment.

Let S_K be exactly the set of primes of L033's entire K above 2 and 11, and
S_D all primes above S_K in L069's entire cubic field D. In TARGET,
S-units mean maximal-ring units after inverting precisely these primes,
with no sign restrictions. Norm-square means element norm in K*².
The proposed ambient space consists of such square classes in D*/D*²
with even normalized valuations outside S_D; its subgroup in the
quotient consists of classes represented by S_D-units with square norm.
These definitions specify the assessed question, not an asserted exact sequence.

Essential inputs for continuation: L033's K, L069's entire degree-three
extension and fixed generator, L072's ordinary criterion as comparison,
and audited L073's local stop. No cross-notebook input. Reuse existing
primary passages where sufficient; assess localization and relative norm
compatibility before deriving anything. Do not silently assume that an
abstract splitting is compatible with norms.

The downstream use is identifying what non-unit contribution a descent
space retaining exceptional support must control before local pruning
can produce a rank bound. Continue if a precise cited or justified
quotient description accounts for every lifting obstruction; otherwise
record the specific missing term or source hypothesis. Full Kummer
containment, class-group values, S-unit completeness, simultaneous local
filtering, rank and primitive integer lifting remain independent gaps.
L073's odd local class is not assumed globally realized. No mathematics
for this new target was undertaken in the preceding audit turn or this
literature turn. This assessment approves a later specialization attempt.

## Primary evidence and applicability

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
Section 1.2, Proposition 1.3, printed pp.8–9 (PDF pp.2–3).
Inspected definitions, the entire proposition and adjacent discussion.
Its finite set includes infinite places; its field square classes have
even valuations outside that set. It describes this group by S-unit
square classes and S-class two-torsion, defining the S-class group as
the ordinary class group modulo the supported prime classes. It imposes
no odd-class-number or support-generation condition. It states an
abstract isomorphism, not a canonical norm-compatible section. Its proof
is referred to [21], Simon's 1998 Bordeaux thesis, with [17] Poonen–Schaefer
as another reference; neither reference was read in this turn. The cited
published proposition suffices as an imported structural input. The
natural ideal-square map and its compatibility still need a short
specialization proof; no reproof of general descent is proposed.

J.S. Milne, [*Algebraic Number Theory*, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf).
Inspected Propositions 3.4–3.5 and their full localization proofs, printed
p.48; Proposition 3.23 with its proof, p.55; the norm definition and
complete Proposition 4.1 proof, pp.68–69. Localization preserves the
Dedekind property, and localized fractional ideals are freely described
by primes surviving localization. For a Dedekind domain and its integral
closure in a finite separable extension, ideal norm uses residue degrees,
commutes with principal ideals, and sends extended ideals to their
degree-th powers. The proof includes the nonnormal case via a Galois
overfield and torsion-free ideal groups. Thus normality is not a source
obstruction. Fractional inverses and the precise localized-ring
identification must be retained in the later application.

The Stacks Project, [Lemma 10.36.11, Tag 0307](https://stacks.math.columbia.edu/tag/0307),
accessed 2026-10-15: inspected the statement and both directions of its
proof. For any ring map and multiplicative subset of the source,
integral closure commutes with localization. The proof clears
denominators and does not assume normality of a field extension.
It supplies the integral-closure input for applying Milne after inverting
22; the future proof should explicitly identify both maximal localized
rings and the surviving primes. No new localization theorem is needed.

The prior assessment
`drafts/literature/2026-10-15-even-valuation-unit-exhaustion.md`
already inspected BPT arXiv:2001.02263v3, Lemma 2.14 and Remark 2.15,
pp.12–13. Reuse its odd-degree scalar-unit square-class method and its
warning about lifting norms; no additional BPT browsing is needed.
Whether that method removes every obstruction in the localized diagram
is an application to prove, not an outcome of this review. No assertion
about norms on unsquared S-units is imported.

## Bounded comparison and next proof test

Queries included `"S-units" "norm" "2-torsion" "class" Simon`,
`"S-class" "norm" "Selmer" exact sequence`,
`site.jmilne.org ANT localization Dedekind integral closure norm`,
and `site:stacks.math.columbia.edu "Integral closure commutes with localization"`.
Search snippets were discovery aids only. A follow-up search found
Simon's separate *Solving norm equations in relative number fields using
S-units*, Math. Comp. **71** (2002), 1287–1305. This is an unread lead,
not the cited proof [21] of Proposition 1.3 and not an essential input:
the target concerns norms modulo squares, rather than solving an exact
norm equation with an unchanged support. No novelty inference follows
from these bounded searches.

Scoped duplicate/failure checks found that L069 counts ordinary units,
L072 establishes only the ordinary criterion, and L073 supplies a local
odd class without global realization. ATTEMPTS/032 forbids inferring
rank below twelve from an unfiltered space retaining those units;
ATTEMPTS/033 forbids deleting eleven via universal local evenness.
The present target computes neither rank nor a smaller local image and
does not reopen either exhausted claim. No sibling notebook was read.

The later attempt should import Simon's structural statement, construct
the natural ideal-square map over the localized maximal rings, and check
the element/ideal/class norm diagram using the exact same full support
on both fields. Track the possible S-unit square-class norm cokernel
before claiming surjectivity on norm kernels; check the degree-three
scalar method explicitly rather than choosing an abstract splitting.
Check independence of fractional-ideal representatives and generators.
Use the two-torsion of the actual S-class groups, not an unjustified
replacement by images of ordinary class-group two-torsion. A successful
conditional quotient description suffices; no class-group vanishing,
S-unit basis, localized unit dimension or exact-norm-one assertion is
required by TARGET. If an obstruction remains, state it explicitly.

This is source-coverage progress only, with no claim beyond the checked
literature and no new lemma, calculation or mathematical script.
Mathlib coverage of the full localized norm-kernel statement and its
supporting ideal/S-unit machinery: not checked; no absence is inferred.
