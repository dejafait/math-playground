# Marked-octic ordinary S-class two-torsion — source assessment

TARGET: Compute the ordinary S-class two-torsion Cl(O_K[1/330])[2] for L115's field with unconditional completeness certificates, using L116's maximal basis and L117's eight support primes.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared notebook class-certification and S-class assessments, L115–L117 and ATTEMPTS/050–051; searched unconditional class algorithms, localization, Smith forms, the exact octic coefficients and discriminant 6818950876320000. No inspected source gives this instance's group or representatives; no novelty inference.
SOURCE_EVIDENCE: Lenstra, Algorithms in algebraic number theory, arXiv:math/9204234v1 (1 April 1992), Section 2.5 p.7, Theorem 5.4 and class-presentation discussion pp.22–25, Theorems 6.1–6.2 and complete proofs pp.26–28; Sharifi, Iwasawa Theory Chapter 1, Definition 1.3.19(a),(c),(d), live author HTML read 2026-10-23; reuse the previously inspected PARI bnfinit/bnfcertify/bnfisprincipal/bnfsunit coverage in the 2026-10-10 global-eleven and 2026-10-16 separated-eleven assessments, with access qualifications below.
COMPARISON: Standard certified ordinary-class computation, localization by the eight prime classes and exact finite-abelian-group arithmetic cover the method. The field-specific completeness run, basis/ideal transport, localized group and representatives are absent; audited prime decomposition alone supplies none of them.
GAP: Carry out and preserve unconditional instance certification and every exact transport/relation/Smith certificate; implementation availability and practical cost remain unverified. No class value, supported-unit basis or point conclusion is imported.
REASON: Essential method coverage is ready for one later instance attempt; reproduce the known algorithms and justify their specialization, without a general reproof or a GRH-dependent substitute.
SCOPE: Exactly TARGET for the entire L115 field and ordinary maximal-ring ideals of L116–L117; certified ordinary class data, complete finite-support quotient and tracked two-torsion extraction. No narrow-class substitution, full supported-square-class enumeration, local-image or point-completeness claim is covered.
LITERATURE_REASON: At invocation start the exact saved arithmetic target was REVIEW_REQUIRED; unconditional completeness and localized two-torsion extraction were outside the prior prime-decomposition assessment. This review fills that essential scope, while reusing adequate earlier general certification coverage.

This completed turn is literature-only. The unchanged calculation target
is now method-ready for a subsequent research turn. No ideal-class
calculation, new lemma or mathematical script was produced. A general
algorithm or software return alone is not the requested instance
certificate. The specializations and certificate obligations below are
requirements for that later work, not already established instance data.

The main Beal gap remains primitive integer emptiness for residual
signatures. The intermediate target is the ordinary localized class
two-torsion for the entire marked-octic field, with its support fixed by
audited L114–L117. Its plausible downstream use is the non-unit part of
supported square-class enumeration for the marked curve's two-cover
method. This does not propose that class two-torsion alone controls
points, computes units or eliminates the known infinity classes.

Essential inputs are L115's entire degree-eight field, audited L116's
maximal basis and L117's complete eight supported primes with their exact
ideal bases and corrected audit evidence. Retain ordinary ideal classes;
real-point conditions and any distinction from narrow classes must not be
silently dropped or conflated. No cross-notebook input is proposed.

The continuation test remains a certified complete group and representatives,
including a certificate of triviality if it is trivial. A partial relation
matrix, bounded failed generator search or unproved conditional class
bound is insufficient. The source review must identify how completeness
would be proved and whether the required computations are feasible;
if execution cannot supply completeness, preserve its partial evidence and
stop that attempt without reporting a group value. Repeated execution
blockers require an independently testable target under the shared recovery
rules. This assessment does not assert feasibility from the degree or
discriminant, approve an enlarged search cap, or authorize a new method.

Supported units, simultaneous real/finite point images, points on surviving
covers, degree-nine distinguished-root recovery, compatible remaining
factors, both L095 integer systems and minus-eleven remain independent
unresolved steps. Preserve unfinished L108 and ATTEMPTS/050–051. Their
bounded-rank and rank-zero failures are not a class-group computation,
and the known rational infinity points forbid an empty fake-Selmer-set
shortcut. Full matching Mathlib coverage has not been checked.

## Known results, duplicates and failed routes

The narrow local review read L115's exact field statement, L116's fixed
maximal basis/discriminant and imported maximality hypotheses, and L117's
entire decomposition and residue maps. The latter audit is accepted in the
startup checkpoint. Its eight kernels, rather than their norms alone,
identify the support inputs. None of these statements computes classes.

The ready general coverage reused is
`drafts/literature/2026-10-10-global-eleven-valuation-image.md`
(primary comparisons and certification limitations) and
`drafts/literature/2026-10-16-separated-eleven-supported-unit.md`
(unconditional certificate methods). Their different degree-twelve and
degree-thirty-six instance conclusions are not inputs here; only the
explicitly inspected general source statements are reused. The existing
marked-octic support assessment's Section 6 comparison retains class
two-torsion rather than assuming S-units exhaust supported square classes.

ATTEMPTS/050's exhausted bounded detector and ATTEMPTS/051's positive-rank
obstruction concern different point/rank mechanisms. Neither computes this
group nor forbids this arithmetic target. No old search box is reopened.

Queries included `PARI bnfcertify bnfsunit unconditional class group`,
`bnfcertify algorithm Zimmert regulator class group proof`, `S integer
class group quotient prime ideals localization theorem Dedekind`,
`PARI matsnf U V`, the coefficient strings `275 2860 6930 3564`,
`275*x^8 2860`, and the exact discriminant `6818950876320000`.
No exact-field class certificate was located. The logarithmic-class-group
package paper was identified as a lead; its logarithmic invariants are
not imported as ordinary S-class data, and its detailed algorithms were
not assessed. No failed search establishes originality.

## Inspected primary statements and their scope

H. W. Lenstra, Jr., *Algorithms in algebraic number theory*, Bull. Amer.
Math. Soc. (N.S.) **26** (1992), 211–244,
[arXiv:math/9204234v1](https://arxiv.org/pdf/math/9204234v1), uses the
actual maximal ring. Section 2.5 supplies finite-abelian-group algorithms.
Theorem 5.4, manuscript p.23, sets d=(2/pi)^s sqrt(|disc(K)|), where s
counts complex places. Primes of norm at most d generate Cl(O_K);
their S-units are generated by elements of height at most d². The
valuation presentation on pp.23–24 computes classes from complete
relations. Theorems 6.1–6.2, pp.26–28, prove these bounds via a compact
fundamental set and discrete-subgroup generation; both fractional and
integral-generator cases were read. The p.25 discussion distinguishes
finite-index relations from complete relations and isolates the GRH
factor-base shortcut. No runtime claim from its tentative Theorem 5.5
is used. This is a theoretical completeness alternative, not a proposal
to execute the height enumeration or identify its large support with our
eight primes. No numerical bound or signature was calculated here.

Romyar Sharifi, [*Iwasawa Theory*, Chapter 1](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
live author HTML, accessed 2026-10-23, revision unidentified, Definition
1.3.19(a),(c),(d): the ordinary S-class group is the ordinary class group
modulo classes of finite S-primes, with S-integers defined by nonnegative
valuations outside S and ordinary fractional ideals/principal ideals.
All parts just cited were read directly. This is not a narrow class group;
positivity of principal generators is not imposed. L116 gives the maximal
ring and L117 gives every prime above the inverted rational primes.
The later write-up must explicitly justify that this is the localization
O_K[1/330], using maximal-ring prime factorization. No new localization
lemma was proved in this source turn. Real-point restrictions remain a
separate downstream obligation.

The [official PARI stable number-field catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html)
has no release identifier in the reused assessment. Previously inspected
entries authorize `bnfinit(nf,1)` followed by successful
`bnfcertify(bnf,0)=1`; errors/nontermination give no certificate. Flag one
certifies only a quotient. `bnfisprincipal` returns class coordinates and
a principal ideal relation; `bnfsunit(bnf,S)[5]` returns S-class structure
and generators, whereas its first component omits ordinary units.
The [matrix catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html#matsnf)
documents `matsnf(M,1)=[U,V,D]` with unimodular transformations and
U M V=D; cleanup must not lose the representative maps.

Access qualification: direct manual HTML/PDF fetches timed out this turn;
shell retrieval also failed DNS resolution. Indexed primary excerpts
corroborated the above entries but are not treated as fresh complete
reads. Essential general certification coverage is reused from the two
named ready local assessments, not inferred from those excerpts. Lenstra
and Sharifi were directly accessible. The matrix transformation contract
is also covered by Lenstra's Section 2.5; no unread software algorithm is
an assumed theorem. A later implementation must record its actual
software release and retain any version-specific failure.

## Required instance certificate and applicability work

Use the full characteristic-zero number field of L115. L116 supplies the
maximal order; it does not make its nonintegral theta an integral power
generator. If a backend changes polynomial, generator or integral basis,
save exact inverse field maps and unimodular basis comparisons. Transport
all eight ideals and compare full HNF lattices with L117's kernels.
Discriminant equality or matching (e,f) lists alone is insufficient.

A later successful software-based certificate must preserve the input,
version, replay command, complete certification transcript/result and
reconstructible exact class/unit state required by the cited routine.
Retain ordinary invariant factors and ideal representatives, and exact
principal-relation witnesses for the support coordinates and class-order
relations. Supporting units may be compact products; their use for class
certification is not a computed complete supported-square-class basis.
The trust in the cited implementation must be explicit; this is not a
claim of an independently verified formal certificate.

Localize the certified complete presentation using every supported prime.
Save the entire integer relation matrix, full Smith transformations and
exact product/unimodularity checks. Keep the maps back to ordinary ideal
representatives. Extract the kernel of multiplication by two on the
localized finite group, not just its quotient modulo two, and not an
assumed image of ordinary class two-torsion. The finite abelian group
structure theorem supplies this standard step; its actual group,
involutions, independence and complete list remain uncomputed here.
For each selected representative, save its exact square-principality
relation after allowing the eight supported primes. Distinctness and
completeness require the certified coordinate maps as well as positive
relations. A trivial answer likewise needs a complete certificate.

Do not replace this with a relation-rank check, a decimal regulator
comparison, a conditional logarithmic norm bound, or a bounded failure
to find representatives. The default-zero certification path covers an
arbitrary result; a weaker quotient certificate alone does not certify
the claimed exact group and nontrivial representatives. Any alternative
special-case certificate must prove its own sufficient implication.

`gp`, `pari-gp`, and `sage` were absent from PATH; Python imports
`cypari2` and `sageall` were unavailable. No installation, mathematical
script or class/unit run was attempted. Thus method availability is
established by sources, while executable access and actual cost are not.
Do not spend another literature turn merely reconfirming this distinction:
the next step defaults to one mathematical implementation/calculation
attempt, recording a concrete execution blocker honestly if encountered.

## Classification and limits

This assessment is source preparation (EXPLORATION), not a mathematical
advance or a new class algorithm. A subsequent successful instance would
be REPRODUCTION under SPECIALIZE. No general theorem needs reproof;
field/basis/ideal identification and exact certificate arithmetic are the
necessary differences from citation alone. Full matching Mathlib coverage
for this instance and certified localization computation was not checked.
No mathematical argument changed, so PROOF.md and DAG.md stay untouched.
