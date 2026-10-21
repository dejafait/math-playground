# Relative normality test — source-approved coverage

TARGET: Test whether L96/Q(T) is normal using L051's fields and L052's audited ramification data.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused recorded theorem searches and BFHP scope comparison; checked L051-L053, histories 145-146 and ATTEMPTS/020 for overlap; opened the three primary PDFs directly to repair missing source URLs, without repeating discovery searches.
SOURCE_EVIDENCE: https://www.jmilne.org/math/CourseNotes/ANT.pdf v3.08 Theorem 3.34 pp.59-60; https://math.mit.edu/classes/18.785/2021fa/LectureNotes5.pdf Fall 2021 Lemmas 5.28,5.30 pp.8-9; https://www.jmilne.org/math/CourseNotes/FT.pdf v5.10 Proposition 2.20 p.32 and Definitions 3.6-3.9 p.37; inspected statements and essential proof cases, reusing recorded BFHP scope.
COMPARISON: These standard prime/tower/Galois results cover the changed number-field base; they do not already state the exact local field decision.
GAP: Execute one relative normality test, retaining actual maximal primes and every tower; relative normality and all global certificate obligations remain unresolved.
REASON: Known general results permit a field-specific applicability attempt without theorem reproof or class enumeration.
SCOPE: Exactly TARGET, using L051,L052 and contrasting L053; no group identification, norm-relation construction, normal-closure test or class/unit certification approved.

The separate source-approval turn on 2026-10-11 repaired the direct-URL
omission and confirms SPECIALIZE for the unchanged TARGET. The completed
source review is not a relative-field proof. Essential inputs are L051's exact m,h and cited
degrees, and L052's audited maximal-ring ramification; L053 preserves
the direct-over-Q stop, and L032 supplies eventual branch relevance.
No cross-notebook input is involved.

Use only the already inspected prime-existence, tower, separability and
Galois degree results cited in the source assessments. Verify their
hypotheses at Q(T) and do not assume the base is normal over Q. A
contradiction under relative normality parks this variant. If the
obstruction does not decide it, record that limitation; passing a
necessary condition is not normality. Any materially different test
needs separate coverage. No GRH or class completeness is assumed.

Possible downstream use is to settle the first relative-base premise
before expensive arithmetic. Norm relations, abelian-group conditions
for the specific certification algorithm, subfield certificates, unit
indices, torsion lifts, support/norm maps and full-disk disjointness
remain unresolved independently. Mathlib coverage is not checked.

## Primary hypotheses and proof cases inspected

Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
v3.08 (July 19, 2020), Theorem 3.34, printed pp.59-60, uses a
Dedekind domain A, fraction field K, finite separable L/K and integral
closure B. For a nonzero prime it gives sum e_i f_i=[L:K]; in the
Galois case the indices are common and efg=[L:K]. Read the dimension
argument, its localization for nonprincipal A, and conjugacy proof.
Thus the theorem does not require the number-field base to be Q or
its maximal integer ring to be principal. No new reproof is needed.

Sutherland, [18.785 Lecture 5](https://math.mit.edu/classes/18.785/2021fa/LectureNotes5.pdf),
September 22, 2021, Lemma 5.28 and following paragraph, printed p.8,
identify contraction and provide primes above base primes in the
integral-closure setup. Lemma 5.30, printed p.9, takes a finite
separable tower and integral closures and gives multiplicativity of
ramification and residue degrees. Read the proofs, including integral
closure transitivity and refinement of ideal factorizations. Neither
tower multiplicativity nor prime existence needs normality. Corollary
5.27, printed p.7, confirms that number-field integer rings are Dedekind.

Milne, [Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf),
v5.10 (September 2022), Proposition 2.20, printed p.32, and its full
derivative proof exclude inseparable irreducible polynomials in
characteristic zero. Definitions 3.6-3.9, printed p.37, supply the
finite normal plus separable interface to Galoisness. Source versions
and printed numbering agree with the prior assessment.

For the future specialization set the base to F=Q(T) and use O_F and
O_L, not power orders. Use L051's field identifications and cited
degrees and L052's audited maximal primes. Compare the two actual
towers through K96 and F when transporting ramification. Apply the
Galois degree constraint to L96/F only under the contrary relative
normality assumption and with the relative degree. Do not transfer
L053's absolute degree contradiction unchanged. This is an applicability
instruction, not an executed field-specific argument.

## Recovery and remaining scope

The source decision is unchanged; this is a process repair, not new
mathematics or progress beyond inspected sources. The existing BFHP
comparison in `2026-10-11-ninety-six-relative-base-norm-scope.md` is
reused; its direct author URL is
https://www.normalesup.org/~page/Recherche/Documents/articles/brauer.pdf.
No essential source is blocked for this bounded test. No exact
relative-normality result was found in the checked local records;
this is not a novelty claim. The direct-over-Q failure and enumeration
stops remain in force for those approaches. The ready continuation
is exactly TARGET, with the same inputs, qualifications and stop test.
