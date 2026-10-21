# Degree-27 full-orbit hull — completed source assessment

TARGET: Assess literature coverage for computing the exact hull of G(pi(O_K union J)) in K = Q_3(pi), pi^27 = 3, J = log(O_K^times), I = J/6 and G = Aut_Z_3(I), using L016's complete lattice and comparing its radius with 81.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected logarithm and native/coarse assessments; searched primitive-vector GL_n(Z_p) orbits, local-ring transitivity, DVR Smith normal form, log-shell automorphism enclosures and the degree-27 logarithm setting; found primary lattice inputs but no inspected matching field-specific hull theorem.
SOURCE_EVIDENCE: Read Dupuy–Hilado arXiv:2004.13108v2 §§4.3 and 6.1–6.2, printed pp. 17–20, including group definition, literal branches, coarse formula and chain justifications; read Bürgisser–Kulkarni–Lerario, Selecta Mathematica 32, article 10 (2026), §2.2 Smith normal form, Proposition 2.1.1 with both proof directions, Definition 3.1.1 and Lemma 3.1.5 with proof; reuse L015/L016's inspected analytic and unit-filtration inputs.
COMPARISON: Known lattice results cover coordinate-norm invariance and basis extension supporting full-group saturation; L016 supplies complete generators but no extremal content or orbit radius; the printed coarse estimate remains the assertion under test, and native tensor enclosures have different inputs and hypotheses.
GAP: Determine exact I-content of both literal branches and the attained field-valuation extreme after the whole group acts, then compare the resulting hull radius with 81; no such values are established here.
REASON: The failed sufficient membership mechanism does not decide this different saturation target; specialize known lattice inputs without repeating logarithm derivations or assuming O_K-module invariance.
LITERATURE_REASON: The proposed full-orbit target was expressly excluded by the membership assessment; its essential new coverage concerns lattice saturation and the precise source comparison.
SCOPE: Only K = Q_3(pi), pi^27 = 3, one factor, beta = 1, scalar pi, complete J from L016, I = J/6 and all Q_3-linear extensions of Aut_Z_3(I); permits one exact saturation/hull calculation with a certified basis and attained automorphism witness, but no general-field theorem or original-IUT realization.
COVERED_TARGET: Compute the exact hull of G(pi(O_K union J)) in K = Q_3(pi), pi^27 = 3, J = log(O_K^times), I = J/6 and G = Aut_Z_3(I), using L016's complete lattice; certify both branch contents, whole-group saturation and an attained radius, then compare with 81.

## Sources, versions and bounded search

The [primary challenge announcement](https://zen.ac.jp/news/0ul6zqed9-0), dated July 7, 2023, was checked on October 5, 2026. Its Challenger paragraph retains the inherent-flaw target; adjudication is separate from correctness.

[Dupuy–Hilado arXiv:2004.13108v2](https://arxiv.org/pdf/2004.13108v2) is dated April 29, 2020, with PDF title-page date April 30, 2020. Page locators below are printed pages. The current primary PDF text was inspected; no author-hosted IUT access blocker was retried.

Reuse [the general coarse assessment](2026-10-04-general-one-factor-coarse-enclosure.md) for April 2020 IUT IV Proposition 1.2(i)–(ii), its proof and Proposition 1.4(iii), retaining reproduction/access and at-least-two-field qualifications. Reuse [the membership assessment](2026-10-04-degree-27-logarithm-membership.md) for Hess–Pauli–Pohst, *Computing the Multiplicative Group of Residue Class Rings*, author-hosted manuscript, §3 pp. 3–5 and Proposition 5.1(iii–iv) pp. 9–10. Those inputs support L015/L016's existing complete lattice. No cyclotomic image formula, withdrawn theorem or unread revised-exposition theorem is imported.

New queries included “GL_n Z_p primitive vectors transitive”, “primitive vectors transitive Z_p GL”, “GL primitive vectors local ring”, “Smith normal form discrete valuation ring lecture notes”, “log-shell automorphism enclosure Dupuy Hilado”, and “Q_3 27 logarithm lattice”, with quotation marks on the specific terms. A targeted Conrad/PID search supplied another standard-algebra lead. Searches did not identify an inspected exact-field hull theorem; this does not establish novelty.

The new inspected source is [Bürgisser–Kulkarni–Lerario, *Nonarchimedean integral geometry*, Selecta Mathematica 32, article 10 (2026)](https://doi.org/10.1007/s00029-025-01120-y), version of record January 5, 2026. Read numbered HTML statements and relevant proofs. The [arXiv record 2206.03708](https://arxiv.org/abs/2206.03708) was opened as a version lead; its theorem numbering was not identified with the published version. Peter Sin's author-hosted *Smith Normal Form* PDF was opened but supplies no additional imported input. Conrad's *Modules over a PID* was a search lead only; its detailed theorems were not read or used.

## Lattice inputs and specialization scope

The published Bürgisser–Kulkarni–Lerario source assumes a characteristic-zero nonarchimedean local field with valuation ring R. Proposition 2.1.1 identifies GL_n(R) with coordinate-maximum-norm isometries. The forward proof uses a matrix and its inverse; the converse uses Smith normal form and unit diagonal entries. Section 2.2 recalls Smith normal form for rank-r fraction-field matrices, with invertible integral row/column transformations and diagonal uniformizer powers of integer exponents. For a finite-dimensional V with a finite spanning R-lattice V_R, Lemma 3.1.5 extends any basis of U intersect V_R to one of V_R; its proof constructs a complement using the quotient lattice and Smith normal form.

For applicability take the source's scalar field to be Q_3, R = Z_3, V the 27-dimensional Q_3-space underlying K, and V_R = I. L015/L016 supply the required full finite lattice. These are not statements with R = O_K. The cited inputs cover coordinate changes and primitive-line basis extension. Applying them to justify orbit equality and computing contents are reserved for research. An elementary basis argument would explain a specialization of known inputs, rather than reprove a new general transitivity theorem.

The lattice-coordinate norm differs from the field absolute value defining the hull. The next calculation must connect them explicitly. Its group comprises Q_3-linear extensions of lattice automorphisms, not merely K-linear maps. No new saturation result, content value or radius is derived here.

## Auxiliary source comparison

Dupuy–Hilado Definition 4.3.1 gives I = J/(2p), Lemma 4.3.2 contains O and J in I, and Remark 4.3.3 does not supply O-module stability. Section 6.1 defines component field hulls. Section 6.2, p. 19, defines Aut(L:I) using all extended lattice automorphisms. Its finite-extension and strict-nonunit hypotheses cover the toy singleton packet. The p. 20 post-chain formula, already specialized in L015, requires radius 81 and differs from (6.8). The (6.6) explanation compares hulls before saturation; (6.7) uses preservation of I. Neither independently settles the intervening issue. Remark 6.2.1(1) proposes explicit basis computations. Footnote 7 and §6.3 distinguish the toy group from actual tensor permutations and initial theta data. The printed coarse assertion is the tested conclusion, not independent evidence.

The reused IUT IV Proposition 1.2(ii) and Proposition 1.4(iii) bound normalized-order inputs with different/logarithm corrections, in a family of cardinality at least two. They do not match this singleton saturated union pi(O union J). Proposition 1.2(i)'s individual-field estimates remain usable through L015's two-field applicability argument; no tensor automorphism assertion is imported as a singleton theorem. A toy violation would not refute these native results without a separately justified exact specialization.

## Local overlap, stopped routes and bounded test

Read the canonical L015/L016 proofs and L012's branch-enclosure, sharp-automorphism and whole-group-saturation ranges. L012 is a degree-nine methodological precedent; its lattice and radii are not degree-27 inputs. L015's upper radius 243 versus required 81 is not a lower bound. L016 gives complete generators and rigorous tails, but its separator refutes only the sufficient multiplication inclusion. The existing diagonalization may be reused with full verification; a preview is not evidence for a new orbit claim.

The exhausted mechanisms remain recorded in [ATTEMPTS/013](../../ATTEMPTS/013-generic-coarse-ideal-sandwich.md) and [ATTEMPTS/014](../../ATTEMPTS/014-degree-27-coarse-membership.md), with decisions in history/028 and history/030. Enlarged-input, rounded-hull and printed-terminal failures do not decide this coarse target. Parked categorical/quotient and source-access routes supply no premises. No cross-notebook input is proposed.

The main gap remains original finite B >= A in IUT III Corollary 3.12. The intermediate target is the exact hull of the literal saturated input in this fixed packet. Its downstream use is to decide this auxiliary coarse-bound objection. Original initial-data realization, distinguished-pilot transport, identification of all permitted images, essentiality and numerical normalization remain independent gaps.

The covered bounded test uses L015/L016 and the cited lattice inputs to verify a basis of I, compute exact I-content of both pi O and pi J, justify the entire automorphism orbit and attain its field-radius extreme. If exact representatives furnish a witness, cite why they are actual elements of J; an original infinite-log witness requires its tail error to be controlled. Store complete exact certificates, upper/lower bounds and paths. A sampled automorphism or membership failure is insufficient.

Continue the local objection only if a certified attained radius exceeds 81. If the exact hull is within radius 81, abandon that objection in this packet while retaining L016's independent membership obstruction. If content, completeness or attainment cannot be certified in the bounded attempt, save the exact unresolved obligation without claiming enclosure or violation. Do not resume the exhausted ideal sandwich under another name.

## Completed-step boundary and Mathlib

Outcome **EXPLORATION**, classification **NOVELTY_UNCHECKED**: this literature-only step completes the changed-scope assessment and records supporting known results; it establishes no field-specific orbit radius or new mathematical result. Mathematical exploration usage remains 0/3. No lemmas, mathematical scripts, DAG or PROOF were modified. The newly covered continuation receives the supervisor's separate approval before invocation; no dependent mathematics is performed this turn.

Full matching degree-27 orbit/hull theorem and supporting Mathlib coverage: **not checked**. Unknown availability is not absence. Supporting citations do not provide the entire proposed conclusion. A subsequent verification of the printed coarse bound is REPRODUCTION; a contrary certified local diagnostic may be POTENTIALLY_NEW only in the bounded-search sense, without an originality or original-IUT counterexample claim.
