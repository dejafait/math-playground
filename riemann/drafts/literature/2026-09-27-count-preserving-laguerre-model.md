# First Laguerre sign with prescribed zero-counting data: source assessment

TARGET: Test whether an even order-one canonical product F can satisfy the Riemann–von Mangoldt count N_F(T)=T/(2π) log(T/(2π))−T/(2π)+O(log T) and eventual real-zero gaps O(1/log T), yet have only one nonreal quartet ±(A±ib) and D_1(F;A)<0 at some A>40 with F(A)≠0 and 0<b<1/2.
CHECKED: 2026-09-27
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searches on 2026-09-27 compared the exact counting/gap/Laguerre combination, prescribed-zero canonical products, finite nonreal-zero perturbations and imaginary-order Bessel zero asymptotics; the inspected statements below cover the standard components but do not state this complete model.
SOURCE_EVIDENCE: Csordás, arXiv:1309.0055v2, Propositions 2.2–2.3 pp. 3–4, https://arxiv.org/pdf/1309.0055v2; Laine, Nevanlinna Theory and Complex Differential Equations (1993), Theorems 1.2.3–1.2.4 and following remark/equations (1.2.6)–(1.2.7), pp. 7–8; HKUST MATH5030 notes, Chapter 4, Definition 4.7.1 and Theorem 4.7.14, pp. 169/174, https://www.math.hkust.edu.hk/~machiang/5030/notes/Chap4.pdf; Gauthier–Xarles, arXiv:0911.5135v1, Theorem 2 p. 7; Paris, arXiv:2204.09306v1, Theorem 2 p. 5. Direct links and read scope below.
COMPARISON: The local sign identity, prescribed-zero product existence and canonical-product order theorem are known inputs. The exact zero sequence, eventual gap bound and symmetric quartet must still be checked together; neither a fixed-background sign theorem nor a generic perturbation theorem is a full match.
GAP: Verify a simple real background with the exact required count and gaps, then justify the even quartet insertion and its strict first-sign failure without treating a displacement-dependent remaining factor as fixed. No such model has been proved in this review.
REASON: A bounded specialization of classical results is justified; rederiving their general product or sign theorems is unnecessary. The model tests only the proposed sufficiency of the selected coarse data and cannot replace an actual-zeta compensation theorem.

## Exact scope

F is real entire and even. N_F(T) counts its zeros with
0<Re z≤T, with multiplicity, so that it corresponds to the positive
ordinate count for zeta in Xi coordinates. All zeros outside the
specified simple nonreal quartet are to be simple and real; finite
initial choices may be made above absolute height 4. The gap condition
concerns consecutive positive real zeros at sufficiently large T.
D_1(F;A)=F'(A)^2−F(A)F''(A).

The exact saved TARGET is unchanged. This completes its literature
gate; it does not execute the model test. No construction, convergence
proof, order calculation, gap estimate or new sign calculation was
performed. The preceding
[actual-zeta assessment](2026-09-27-first-laguerre-zero-compensation.md)
is reused for the density/spacing comparison, rather than repeated.

Plausible downstream use: determine whether these count and gap upper
bounds can by themselves eliminate the known local negative-pair
mechanism. A successful example would stop that proposed sufficiency
argument; it would not settle actual zeta compensation. A failure of
one construction would require identifying which condition caused
it, without inferring a positive theorem for Ξ.

The actual gap remains first Laguerre positivity at every exterior
height, one of the low-index signs needed by L320. L296 covers bands
strictly above coefficient 1/4, not that initial segment. This model
would only decide whether the selected count and gap inputs exclude
one local obstruction; higher signs, actual-theta information and the
endpoint arithmetic margin remain separate unresolved steps.

## Search and redundancy record

Representative queries actually used on 2026-09-27:

- `"Laguerre" "Riemann-von Mangoldt" canonical product`
- `"canonical product" "zero counting" "nonreal" Laguerre`
- `"Laguerre inequality" "prescribed" zeros`
- `"Laguerre inequality" "zero counting"`
- `"Laguerre inequalities" "finite" "nonreal zeros" Csordas`
- `"Riemann-von Mangoldt" "prescribed zeros"`
- `"order one" "Laguerre inequality" counterexample`
- `"Laguerre" "gaps" "canonical product"`
- `canonical product convergence exponent order theorem entire function prescribed zeros`
- `"The Laguerre inequalities with applications" pdf`
- `Gauthier Zeron perturbations zeta functions Riemann hypothesis`
- `"zeros" "K" "imaginary order" "log" Paris 2022`

These are discovery queries, not evidence of novelty. Primary texts
and an accessible textbook section supplied the comparisons below.
No exact full-model theorem was located in this bounded search.

The whole overview and DAG, current gate and preceding assessment
were read before choosing this step. L251 and L264 were reread;
L255's scope was reused from the preceding review and overview.
The polynomial/cosine and compact-kernel examples do not claim the
requested counting law. Repeating their local mechanism alone would
therefore add nothing. L353's pole test addresses a different stopped
implementation and is not reopened by this review.

## Inspected source statements

### Local first-sign mechanism

George Csordás, *Fourier transforms of positive definite kernels and
the Riemann ξ-Function*,
[arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
Propositions 2.2–2.3 and proofs, pp. 3–4, were inspected. Equation
(2.3) supplies the reciprocal-square block formula. Proposition 2.3
states, for a fixed real entire g with g(α)≠0 and
f(x)=((x−α)²+β²)^m g(x), where α∈R, β>0 and m∈N,

\[
 L_1(\alpha;f)=-2m\beta^{4m-2}g(\alpha)^2
                 +\beta^{4m}L_1(\alpha;g).
\]

Consequently its first sign is negative for sufficiently small β>0.
This is the covered sign mechanism, not a uniform assertion over
changing backgrounds. Its source is cited there as Csordás–Ruttan–Varga,
*Numerical Algorithms* **1** (1991), 305–329,
[DOI](https://doi.org/10.1007/BF02142328). The publisher supplied only
the landing page for that original article; the later author's full
statement and proof suffice for this component.

### Product existence, exact zeros and order

Ilpo Laine, *Nevanlinna Theory and Complex Differential Equations*,
de Gruyter Studies in Mathematics 15 (1993),
[publisher preview, §1.2, pp. 6–8](https://api.pageplace.de/preview/DT0400.9783110863147_A19976604/preview-9783110863147_A19976604.pdf).
Read Definition 1.2.2, Theorems 1.2.3–1.2.4, the following order remark,
and equations (1.2.6)–(1.2.7). A discrete nonzero zero sequence of finite
convergence exponent admits the indicated fixed-genus product with
exactly the prescribed multiplicities. The remark records equality
of the canonical product's order and its zero convergence exponent,
referring to Ash, Theorem 4.3.6. The equations relate this exponent to
the counting function. These are supporting inputs, not a construction
of the particular sequence or an eventual consecutive-gap theorem.

The standard **Borel order theorem** was also checked as Theorem
4.7.14 in the author-hosted
[HKUST MATH5030 notes, Chapter 4](https://www.math.hkust.edu.hk/~machiang/5030/notes/Chap4.pdf),
p. 174 (PDF p. 31), with the canonical genus definition on p. 169.
The chapter file is undated; accessed 2026-09-27. Its theorem equates
canonical-product order and zero convergence exponent; the proof is
assigned as an exercise. No claim is made to have read that proof.
The named theorem can be cited once its sequence/genus hypotheses
are verified. Order one must not be silently strengthened to finite
exponential type. The unrestricted Weierstrass existence theorem alone
does not fix a function's order.

### Related perturbation result, not a full match

P. M. Gauthier and X. Xarles, *Perturbations of L-functions with or
without non-trivial zeros off the critical line*,
[arXiv:0911.5135v1, 26 November 2009](https://arxiv.org/pdf/0911.5135v1).
Read the functional-equation class definitions, Theorem 1 and its
polynomial construction (pp. 2–4), Proposition 1 and Theorem 2
(pp. 6–7). Theorem 2 allows prescribed extra zeros while retaining
the completed function's other zeros and multiplicities, functional
equation, and strong approximation away from a small exceptional set.
It assumes symmetric disjoint discrete sets and a starting member of
the stated meromorphic class. It gives no order-one guarantee, no
particular real background counting/gap law, and no Laguerre sign.
Thus finite symmetric zero modification is established literature,
but this theorem is not imported as the requested model. Its
approximation strength is unnecessary for the diagnostic.

### A possible special-function background, not used as an input

R. B. Paris, *On the ν-zeros of the Bessel functions of purely imaginary
order*, [arXiv:2204.09306v1, 20 April 2022](https://arxiv.org/pdf/2204.09306v1).
Read the introduction (pp. 1–2) and Theorem 2 with its preceding
equation (p. 5). The theorem gives the positive ν-zero expansion for
K_(iν)(x), fixed x>0, beginning with m_-/W(λm_-), where
m_-=(n−1/4)π and λ=2/(ex), and gives further correction terms.
This is relevant background on a comparable zero-density scale;
it does not state the quartet/negative-sign model. The full complex
zero classification cited to Bagirova–Khanmamedov was not checked.
No scaled counting formula, all-zero assertion or gap estimate is
inferred here. This optional background would need further comparison
if chosen; the prescribed-sequence specialization does not depend on it.

## Exact specialization still to be tested

The following are proof obligations for a later turn, not conclusions
of this review:

1. Specify a simple positive real sequence with both the full counting
   main term and O(log T) error, and the eventual O(1/log T) gap bound.
   A sequence defined from the inverse of the increasing large-T main
   term is a concrete candidate to test; neither bound is proved here.
2. Check canonical convergence, exact zero multiplicities, evenness,
   reality and order exactly one using the cited standard theorems.
   The counting convention is positive real part, not the radial or
   two-sided count. Finite initial choices above height 4 are allowed.
3. Insert exactly the permitted quartet and retain all the preceding
   conditions. In using the fixed-background sign result, account for
   the reflected pair: its factor changes when the common displacement
   b changes. A bound uniform over that change, or another explicitly
   justified application of the known block identity, is still needed.
4. Obtain F(A)≠0 and the strict negative first sign for one A>40 and
   one 0<b<1/2. There is no requirement of a uniform b for all A or
   of a negative sign for every allowed displacement.

The achieved input is a source-level reduction to these checks; the
required output remains the complete model. A full sign or product
reproof is not justified. Checking these additional simultaneous
hypotheses is the reason for SPECIALIZE instead of IMPORT.

Continue for this one bounded compatibility test. If it succeeds,
stop using these count and gap assumptions alone as a proposed
first-sign certificate. If it fails, identify the failed requirement
and distinguish failure of that construction from a theorem of
sufficiency for Ξ. Complete that decision within the inherited
three-turn exploration budget; a renamed approach does not reset it.

The target demands neither a theta representation nor an Euler
product, and does not reproduce every pair-correlation or gap statistic
in the preceding assessment. Its eventual real-gap upper bound is a
chosen model hypothesis, not a newly imported theorem about actual
critical-line gaps. A successful model would not be a counterexample
to RH or an extension of the existing sign/exclusion ranges.

## Review outcome and access boundary

Outcome: EXPLORATION; LITERATURE; NOVELTY_UNCHECKED. The assessment is
complete, but no full model has been imported or reproduced and no
progress beyond the checked literature is claimed. The intended
mathematical follow-up is a reproduction/specialization of classical
inputs, with only the identified compatibility checks to supply.
This is the second consecutive unresolved exploration turn after
L353, including the preceding actual-zeta source review. The exact
saved action is retained; its current record remains in PROGRESS.md.

All essential statements for this decision were accessed. The
original 1991 article and the optional Bessel classification remain
unread, with the limited roles stated above. A Levin book PDF request
failed; it is not evidence. Laine and the HKUST chapter supply the
needed product statements. No conclusion uses search snippets,
forum posts or unrelated claimed RH proofs. No mathematical lemma,
script, DAG row or part of the overall argument was changed.

## Mathlib

Full-target coverage: **not checked**. Supporting coverage for the
canonical-product and first-sign statements: **not checked**. The
named results and direct links above are mathematical references,
not asserted Mathlib matches.
