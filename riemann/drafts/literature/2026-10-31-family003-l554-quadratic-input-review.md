# L554 quadratic evaluation — source coverage completed

TARGET: Audit the quadratic four-term evaluation needed by L554 on good primes and products of two distinct good primes, checking additive-character and Poisson normalizations.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused base-quadratic/row-character scopes and searched their audit notes, relevant family003 histories and local ATTEMPTS for quadratic-four-term/Gaussian evaluation; those audits expressly retain this input. Queries included quadratic Gauss sum reciprocity number fields trace different Eisenstein integers Poisson summation; Landsberg Schaar formula number field quadratic Gauss sums reciprocity lattice; Deloup Turaev reciprocity formula Gauss sums lattice theorem pdf; Hecke Gauss sums number field quadratic reciprocity different trace formula; and the exact Boylan–Skoruppa titles. Inspected primary sources are distinguished below from inaccessible/unread leads; no novelty inference.
SOURCE_EVIDENCE: OpenAI pinned TeX https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex 557–566, complete 772–859 and required 899–927; Deloup–Turaev https://arxiv.org/pdf/math/0512050 Theorem 1, (1)/(3), p. 1; Tao https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ Exercise 54; Sutherland https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec17.pdf Definition 17.4/Theorem 17.8 with proof, pp. 1–3; Ivrii https://www.math.utoronto.ca/ivrii/PDE-textbook/Chapter5/S5.2.A.html Definition 1/Remarks 1–3; Zhu https://arxiv.org/html/2512.15334v1 Section 6.4, Proposition 6.3 with proof and Proposition 6.7 statement.
COMPARISON: The pinned manuscript already claims the full target for every nonzero odd c. Primary Schwartz Poisson and positive-real-part complex Gaussian formulas supply independent analytic inputs to audit its exact normalization and limits. General lattice reciprocity and explicit Hecke-sum reductions have different quotient/different/phase interfaces; none is asserted already specialized to L554. Reproduction checks a retained source premise rather than discovering a new formula.
GAP: Source coverage is sufficient for a separate analytic application audit, restricted to fixed c=p or pq. The source's self-duality, Gaussian prefactor/branch, coset means, normalized replacement errors and four-class table still need mathematical verification; this literature turn discharges none of them. No uniform-in-c limiting estimate is needed or approved. Alternative Hecke reciprocity specializations remain unverified leads, not inputs.
REASON: Approve only a later reproduction audit using cited standard analytic inputs; importing the manuscript's final quadratic identity would bypass the independent check requested. General Poisson/Gaussian results alone do not certify its character conversion or limiting argument. No new lemma, calculation or proof audit was performed this turn.
SCOPE: O=Z[omega], lambda=1+2omega, e(z)=exp(2pi i Tr(z/lambda)), q_c=|c|^2, good primary primes outside fixed S containing the primes above 6; c=p or c=pq for distinct good p,q. Required evaluation H(c)=q_c^(-1/2) sum_(x mod c)e(x^2/c)=(1/2)sum_(y mod 2O)e(-cy^2/4), with the stated four-class table and correction R. Permit only the fixed-c Poisson/Gaussian application and finite modulo-4 checks needed for that domain; exclude broader arithmetic uniformity, raw theta/coefficient bounds, other Gauss identities and Xi signs.
LITERATURE_REASON: The preceding ready row-character and base-quadratic scopes explicitly excluded independent certification of the retained Gaussian evaluation. Its exact analytic normalization and limit inputs were essential uncovered sources for this unchanged target; they have now been compared.

## Assessment and primary analytic inputs

Completed 2026-10-31, literature-only. The exact TARGET is unchanged.
The formerly pending review now supports a later REPRODUCTION audit,
subject to the supervisor's separate approval. No audit pass follows
from this coverage decision. Full local source notes are in
[the working record](../audits/2026-10-31-family003-l554-quadratic-source-notes.md).

The pinned source is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
The complete statement/proof of `lem:quadratic-four-term` was read,
including every Gaussian, coset-limit, replacement-error and finite-table
case (772–859), and the actual prime/product use (899–927).
Its normalization conventions are 557–566. Previously recorded exclusions
in the base-quadratic family scope, row-character source notes and L554's
critical-review history remain in force until the separate audit passes.

Import standard Schwartz Poisson summation, rather than reprove it:
Terence Tao, *245C, Notes 2: The Fourier transform*, 6 April 2009,
[Exercise 54](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
for f in S(R^d), with the Euclidean kernel exp(-2pi i x dot xi).
The entire exercise statement and its sum identity were inspected.
For an explicit proof of the same Schwartz periodization mechanism,
Andrew V. Sutherland, MIT 18.785, Lecture 17, 8 November 2021,
[Definition 17.4 and Theorem 17.8](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec17.pdf),
PDF pp. 1–3, were read, including the complete proof. His statement is
one-dimensional; use Tao's R^d statement for dimension two. Schwartz
regularity supplies absolute convergence. Lattice basis changes and the
conversion to the source's bilinear pairing remain audit work; neither
reference states that conversion automatically for Eisenstein integers.

Victor Ivrii, *Partial Differential Equations*,
[Section 5.2.A](https://www.math.utoronto.ca/ivrii/PDE-textbook/Chapter5/S5.2.A.html),
Definition 1 and Remarks 1–3 (accessed 2026-10-31), were read in full.
Remark 2 gives the Fourier transform of exp(-x^T A x/2) for complex
symmetric A with Re(x^T A x)>=epsilon |x|^2, epsilon>0. Its prefactor
uses det(A^(-1/2)), with matrix powers on the branch avoiding the
nonpositive real axis. Definition 1 uses exp(-i k dot x) and a
(kappa/(2pi))^d prefactor. Remark 1 records invertible real linear
changes; Remark 3 records the corresponding lattice formula. Use the
Schwartz theorem above for convergence hypotheses, not a mere
continuous-function shorthand. This gives a precise Gaussian import;
the source's matrix and frequency/measure conversion must be checked.
No undamped oscillatory integral or distributional boundary-value
formula is needed as an input to the proposed audit.

## Other known results and limitations of direct import

Florian Deloup and Vladimir Turaev, *On Reciprocity*,
[arXiv:math/0512050v1, 2 December 2005](https://arxiv.org/pdf/math/0512050),
Theorem 1 and hypotheses (1), printed p. 1, were inspected. Its objects
are a finite-rank inner-product lattice W, its Euclidean dual W-bullet,
a self-adjoint automorphism h preserving W-bullet, a vector psi and a
positive integer r. In addition to integrality of <x,h(x')>, it requires
r<x,h(x)>/2 and r<x,psi> integral on W; on W-bullet it requires
r<y,h(y)>/2, <y,ry'> and r<y,psi> integral. Formula (3) relates W/rW
and W-bullet/h(W-bullet), with absolute determinant and signature phase.
The authors explicitly correct the earlier formula's phase ambiguity
and missing factor. Its hypotheses/quotients are not the ready-made
ideal quotient O/(c) and four-class formula here. No specialization of
that theorem is performed or approved by this assessment. An uncorrected
Jeffrey formula must not replace the positive-real-part Gaussian input.

Xiao-Jie Zhu, *Quadratic Gauss sums over Z^n/cZ^n*,
[arXiv:2512.15334v1, 17 December 2025](https://arxiv.org/html/2512.15334v1),
Section 6.4 was inspected through Proposition 6.7's statement.
Proposition 6.3 and its complete proof reduce a Hecke sum, with coprime
ideals defined by w times the different, to an integral symmetric-matrix
sum and a quotient-size factor. Proposition 6.7 gives the quadratic-field
version, with separate integrality and coprimality conditions for its
simplified formula. These are known broader reduction tools, not an
already verified modulo-4 phase table under L554's conventions. The
evaluation theorems behind their final matrix sums were not audited and
are not inputs. This alternative is unnecessary for the selected
analytic audit and is not an essential source blocker.

Unread leads: Boylan–Skoruppa, *Explicit formulas for Hecke Gauss sums
in quadratic number fields*, Abh. Math. Semin. Univ. Hambg. 80 (2010),
213–226, [DOI](https://doi.org/10.1007/s12188-010-0041-0), and
*A quick proof of reciprocity for Hecke Gauss sums*, J. Number Theory
133 (2013), 110–114,
[publisher](https://www.sciencedirect.com/science/article/pii/S0022314X12002247).
The first publisher endpoint was inaccessible; the second search result
exposed bibliographic/abstract material only. No primary theorem from
either was read. Search snippets and transcript mirrors do not establish
their exact applicability. They are alternatives to the covered analytic
proof, not premises of it; no claim of originality or superiority is made.

## Exact later audit and discriminating test

For each fixed c in the stated prime/product domain, the later audit must:

1. Check the character extension, annihilator and covolume for the
   bilinear e(zy) pairing and dmu=(2/sqrt(3)) dx dy, including the
   distinction from the Hermitian pairing and Euclidean dual.
2. Apply the cited Gaussian formula at positive epsilon, checking the
   real-part hypothesis, linear frequency, determinant branch and
   prefactor in the displayed source transform. Do not assume that
   displayed transform as the proof of its own normalization.
3. Justify the fixed-c coset Gaussian means and all three replacement
   errors relative to I_epsilon, allowing c-dependent constants. The
   manuscript's claimed unnormalized phase error O_c(1) is not required
   to tend to zero: the required comparison is o(I_epsilon). No exchange
   of an undamped infinite sum with a boundary limit is authorized.
4. Check the four residues, square-class invariance, nonvanishing table
   and correction R on the exact prime/product domain. The lambda-class
   representative is a finite residue-class calculation, not a request
   to extend the analytic audit to bad prime moduli.

Continue only with a complete character/measure/branch match and the
required normalized error limit. A failed factor, conjugation or limit
requires recording a canonical repair/restriction, not silently retaining
the desired identity or importing L554's final row conclusion. No scripts
or numerical sample values can replace those analytic checks.

## Mathlib

Inspected the primary
[PoissonSummation documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/PoissonSummation.html).
`Real.tsum_eq_tsum_fourier` gives a one-dimensional version with explicit
compact uniform summability and Fourier summability assumptions; the file
also lists `SchwartzMap.tsum_eq_tsum_fourier`. These support standard
Poisson summation only. A full matching Eisenstein four-term evaluation
and the complex matrix Gaussian specialization were not checked in
Mathlib; no absence claim is made.

Bounded downstream test after approval: recover the precise correction
R([p],[q]) on distinct good primes with no conjugation or missing local
factor. This would remove the Gaussian premise from L554's reciprocity
step only; it would leave the raw theta/Gauss, global uniformity and
actual-Xi sign gaps open. A failed normalization or limit requires a
canonical repair or restriction, not import of the final row lemma as
its own proof. There is no cross-notebook input.
