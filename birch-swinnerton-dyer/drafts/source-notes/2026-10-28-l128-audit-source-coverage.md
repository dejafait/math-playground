# Step 532 — source coverage for the separate L128 audit

2026-10-28. LITERATURE only. No proof audit or new derivation is
performed here. The saved source-review TARGET is unchanged.

Main gap: rational rank versus complex order for arbitrary E/Q.
Intermediate target: establish adequate source coverage to audit L128's
completed-branch comparison in its original coefficient module.
Downstream use: a successful later audit would license the conditional
residual formula in L128 (3); it supplies neither rationality nor
nonvanishing nor second-factor finite local membership.
Continuation test: audit the opposite-action transfer first, then the
original-localization comparison and normalized signs; stop at the first
failed identification. A source gate is not acceptance of those claims.

## Existing coverage, duplicates and failure

Read L128 in full, the relevant L123/L126 hypotheses, L127's statement,
the step-531 saved attempt and history, ATTEMPTS/061, the step-527
assessment/source record and the step-529 approval. No sibling notebook
was used. Existing notebook changes and all unfinished work are retained.

Reuse Schmidt, *Some remarks on local newforms for GL(2)* (2002),
Theorems 1.2.1/3.2.2 and Section 3.1; Jacquet--Langlands, LNM 114
(1970), Theorems 4.2/4.3(i)/15.1; and the step-527 inspected proof
cases and local sign conventions. Their accessible primary links and
qualifications remain in
[the existing record](2026-10-27-degree-one-normalizer-scalar-coverage.md).
No repeated discovery search for the unchanged local signs was needed.
ATTEMPTS/061 blocks automatic full-Hecke-linearity, not a scalar after
specialization. L125/ATTEMPTS/060 concern the different omitted-fiber
substitution. Neither is a proof of nonscalarity on the actual A branch.

## Newly inspected supporting inputs

**Fornea.** [*Plectic Heegner classes*, arXiv:2603.28327v2,
13 April 2026](https://arxiv.org/html/2603.28327v2), Assumption 1.5,
Definitions 2.6/2.8, Remark 2.12, and Section 2.4 through Proposition
2.25, including the displayed control statements and proofs, were
retrieved selectively. These cover physical operators, duality, finite
free homology, augmentation specialization and etaleness. For F=Q the
inertia-degree/different restrictions of Assumption 1.5 are automatic;
the split exponents must still be at most two. The residual, CM and
incoherence assumptions remain. The source does not state the enlarged
opposite-algebra action claimed in L128. Reuse prior extraction for
Corollary 2.21's diagram and the invariant domain in Lemma 4.12/(63);
HTML's empty diagram cells are not new verification.

**Faithful Tate-module detection.** J. S. Milne,
[*Abelian Varieties*, course notes v2.0, 16 March 2008](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I, Theorem 10.15 and Lemma 10.16, printed pp.49--50
(PDF pages 55--56), statement and proof including the general A,B
case. For abelian varieties over a field k and l different from
char(k), Hom(A,B) tensor Z_l injects into Hom(T_l A,T_l B), with
torsion-free cokernel. All the finite-level Jacobians here have
characteristic-zero base, so l=p is allowed. This is the required
faithfulness input without invoking the much stronger Tate/Faltings
surjectivity theorem. It does not identify an ordinary dual summand
or reverse an operator action: those are separate audit obligations.
The older article PDF `math/articles/1986b.pdf` exposed no text through
the web reader; its search preview is not evidence. The inspected
course-note theorem is the replacement, not a guessed article number.

**Finite algebra and local completion.** The Stacks Project, retrieved
2026-10-28, [Lemma 10.97.8, Tag 07N9](https://stacks.math.columbia.edu/tag/07N9),
statement and full proof: for a finite R-algebra T over Noetherian R,
base change to the completion of R at a prime is the product of the
completed local rings of T above that prime. Its proof compares the
ideal topologies and uses the finite-module completion theorem.
This directly covers the ring comparison needed in L128 Step 2 once
its physical T and original I are correctly identified. It does not
assert that an uncompleted local factor equals the base ring, or that
an arbitrary module's completion equals its tensor product.

[Lemmas 10.97.2--3, Tag 0BNH](https://stacks.math.columbia.edu/tag/0BNH),
statements and proofs, give flatness of Noetherian completion and
faithful flatness for local completion. The finite-generation
restriction on exactness of module completion must not be confused
with flat tensor base change, which applies to arbitrary modules.
Thus non-finite generation of L128's coefficient module is not itself
an unavailable-source issue; the actual tensor identifications still
require audit.

**Idempotents and finite modules.** Stacks,
[Lemma 10.153.3(3)--(4), Tag 04GE](https://stacks.math.columbia.edu/tag/04GE),
is the coprime monic-factorization form of Hensel's lemma;
[Lemma 10.153.9, Tag 04GM](https://stacks.math.columbia.edu/tag/04GM)
states that complete local rings are henselian;
[Lemma 10.153.7, Tag 04GK](https://stacks.math.columbia.edu/tag/04GK),
statement and proof, identifies finite etale algebras over a henselian
local ring with their residue algebras. These cover the completed
branch and separating-polynomial tools, not the identification of the
right classical character. [Nakayama, Lemma 10.20.1(2),(6),
Tag 07RC](https://stacks.math.columbia.edu/tag/07RC), statement and
determinant proof, requires a finite module and an ideal in the
Jacobson radical. Audit its uses on finite homology summands and
operator images; it cannot be applied directly to the large coefficient
module without an additional argument.

**Global separation and multiplicity.** A. I. Badulescu, with appendix
by N. Grbac, [*Global Jacquet--Langlands correspondence, multiplicity
one and classification of automorphic representations*, ESI preprint
1970, 19 October 2007](https://www.esi.ac.at/preprints/esi1970.pdf),
Section 4, pp.21--22, and Theorem 5.1(a)--(c), p.25; also inspected
the n=1 proof case on p.28. The global field has characteristic zero,
D is a central division algebra, and all infinite places are split.
The theorem gives the discrete-spectrum transfer, multiplicity one
and strong multiplicity one for GL_n(D). It covers the indefinite
quaternion setting with n=1,d=2, and the split setting with D=F.
The central character is unitary; here it is trivial. This gives a
precise primary source for L128's named global inputs. It does not
give a scalar on an arbitrary oldspace or identify the covariant
Jacobian action. Those still need the exact-conductor and local-vector
checks. No trace-formula reproof is proposed.

Jacquet--Langlands's IAS edition was also searched to locate the named
global input. Proposition 11.1.1, p.174, is multiplicity one;
Theorem 15.1, p.239, is local transfer, not global strong multiplicity
one. Do not miscite either as the latter. Taibi's `notesJL.pdf` timed
out; its search snippet is an unread lead, superseded by the inspected
Badulescu theorem, not an essential source blocker.

## Approved scope of the later audit

SPECIALIZE: all essential source inputs are available for the bounded
conceptual audit. This does not approve L128's conclusion. In particular:

- Check the precise H_m/Tate-module duality, labeled Hecke operators,
  ordinary and finite-diamond projectors, reversed products, surjective
  tower maps and the sandwiched finite-level relations. Milne's theorem
  alone does not supply the proposed B^op action on N_0.
- Check R_0, T and I against their definitions and every map in (5).
  Preserve algebraic tensor base change, the residual projector and
  the original coefficient/invariant domains. Never use an interchange
  of localization with an infinite limit or an uncompleted I=S claim.
- Check good-Hecke separation at exactly the conductor, W stability,
  the projective involution, finite-module Nakayama, split conductor
  exponents one/two and division signs, and only then the existing
  complete-moment projection/descent. Retain both homology copies.

The first failed comparison is a useful audit outcome and must withhold
the affected scalar assertion before downstream use. No direct matching
theorem for the whole complete-moment identity was identified; this
is not an absence or originality claim. Mathlib coverage is not checked.
No lemma, mathematical program, PROOF or DAG is changed in this turn.

Search queries included: Stacks completion/finite algebra/product of
local completions; finite etale henselian/idempotent lifting; Milne
Hom tensor Z_l faithful Tate-module detection; and Jacquet--Langlands
strong multiplicity-one theorem numbering. Search results were leads;
the statements identified above were opened and inspected. This is
new essential supporting coverage, not a repeat of the ready local-sign
review. No mathematical exploration budget is spent or reset.
