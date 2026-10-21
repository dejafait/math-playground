# Catalan–Mihăilescu coverage for the base-one boundary

TARGET: Assess primary Catalan–Mihailescu coverage for excluding every positive Beal solution with at least one base equal to one, retaining arbitrary exponents greater than two.
CHECKED: 2026-10-07
DECISION: IMPORT
SEARCH_EVIDENCE: Exact-title primary-paper, Catalan/Mihailescu consecutive-power and Beal base-one searches; scoped local searches found no uniform exclusion or failed application.
SOURCE_EVIDENCE: Inspected Mihailescu, J. reine angew. Math. 572 (2004), introduction pp. 167–169 and Theorem 5 with concluding proof p. 188 via a published-paper transcription; inspected Bilu, Astérisque 294 (2004), exposé 909, pp. 1–2, including both square cases and Theorem 1.3.
COMPARISON: The full theorem classifies arbitrary positive consecutive perfect powers, stronger than the needed input; existing imports retain unit bases only within their signature scopes. No novelty is claimed.
GAP: No essential source gap remains; the later application must check every unit-base position, overlapping unit cases and exceptional power representations under the original exponents.
REASON: Complete inspected known-theorem coverage replaces an uninspected lead; use citation and applicability checks rather than a cyclotomic reproof.
SCOPE: Source comparison only, preparing the all-positive original-exponent boundary application; the imported theorem requires no primitivity hypothesis.

## Inspected sources

Preda Mihăilescu, *Primary cyclotomic units and a proof of Catalan's conjecture*, **J. reine angew. Math. 572** (2004), 167–195, DOI [10.1515/crll.2004.048](https://doi.org/10.1515/crll.2004.048), **Theorem 5, p. 188**. Publisher HTML/PDF retrieval failed. The inspected [published-paper transcription](https://www.scribd.com/document/629548443/Primary-cyclotomic-units-and-a-proof-of-Catalan-s-conjecture) has imperfect mathematical OCR; the author's article, rather than the host's generated summary, was read. Introduction pp. 167–169 defines the full positive-integer conjecture, reduces exponents to primes and records Lebesgue's and Ko Chao's square cases. Theorem 5 and its complete concluding proof establish the full result from preceding cyclotomic theorems. The proof is imported, not independently audited or reproduced.

Needed statement: for integers U,V,m,n all greater than one, U^m−V^n=1 implies (U,m,V,n)=(3,2,2,3). This is unconditional and assumes neither Beal nor modularity nor abc.

Yuri F. Bilu, *Catalan's conjecture [after Mihăilescu]*, **Astérisque 294** (2004), Séminaire Bourbaki, exposé 909, 1–26; [original PDF](https://www.numdam.org/item/SB_2002-2003__45__1_0.pdf). Printed pp. 1–2 were inspected, including the page images. Conjecture 1.1 states the full classification and p. 1 explicitly says it is proved. The same page records that U^m−V^2=1 has no positive solutions for m>1, while U^2−V^n=1 has only the displayed exception for n>1. Conjecture 1.2 permits nonzero signed bases and odd prime exponents; Theorem 1.3 proves it. These formulations are distinguished: the odd-prime theorem alone would be inadequate here. References [18] and [21] identify Ko Chao and Lebesgue; their original proofs were not independently retrieved. The precise published restatements corroborate the full named theorem, rather than providing a fresh historical reproof.

## Discovery, duplicates and limitations

Queries: `Mihailescu Primary Cyclotomic Units proof Catalan conjecture 2004 theorem 1 pdf`; `"Mihailescu" "Primary" "167" pdf Catalan`; `"Beal" "base" "Catalan" conjecture 1`; primary-title PDF searches excluding Scribd/Scispace; and author/theorem/odd-prime search. Results included the original publication, Bilu's proof exposition, weaker criteria, secondary summaries and purported general Beal proofs. Only the inspected published sources above support this decision. Other purported Beal proofs and recent unrelated cyclotomic claims remain unread leads. Failed searches do not establish novelty.

Read foundations/01-target-and-scope.md and L002's full statement/proof. Scoped Catalan/Mihailescu/consecutive searches in lemmas, foundations, ATTEMPTS, literature and history found only L003's unrelated exposition citation and its historical mention, besides this pending review. No uniform base-one lemma or failed consecutive-power application was found. Supplied overview records the signature-specific exclusions. Fourth-difference and mixed-seventh blockers remain parked and are not premises; no cross-notebook input was read.

[Mauldin's accessible primary Beal formulation](https://sites.math.unt.edu/~mauldin/beal.html) was rechecked on 2026-10-07 and retains positive integers and exponents greater than two. The nominated AMS endpoint again failed retrieval; no access to its current contents or change in prize administration is claimed.

## Relevance and future applicability test

Main gap: zero positive primitive solutions for every residual signature in L002's S^3. Intermediate target: zero positive solutions with a unit base for arbitrary original exponents greater than two. Downstream use: remove this uniform boundary before later inputs requiring bases greater than one. All three-bases-greater-than-one signatures and mixed-seventh algebra/packet gaps remain independent.

The later proof must separately check a unit right-hand base, either unit summand and overlapping unit cases. Establish the source's bases-greater-than-one hypotheses only where needed. Retain the unique exception and check every representation of its larger perfect power under the original exponent. Do not reduce to odd primes alone, dismiss the exception by memory, assume primitivity is necessary or claim Beal from a boundary exclusion. These are future proof obligations, not a derivation in this literature review.

Continue only if every position and exceptional representation passes; restrict or abandon an unsupported case. No application, new lemma or calculation was performed. Full and supporting Mathlib coverage is **not checked**; no absence claim is made. A new application assessment is separately saved and awaits next-turn approval before research.
