# Projection-weighted reciprocal inertia — source comparison

TARGET: Assess whether generalized Nevanlinna kernel theory controls the signed inertia of L777's projection-weighted reciprocal pairing without global real-zero assumptions, consistently with L780.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step443 searched generalized Nevanlinna/finite-negative-square, divided-difference/Loewner, rational-Hankel, Taylor-subtraction and actual-Xi reciprocal terminology; primary statements and relevant proof cases were inspected as detailed below. Reused step440/441 algebra and checked the recorded interpolation and real-residue scope stops; no novelty inference.
SOURCE_EVIDENCE: Song–Hao–Hu–Chen, Advances in Mathematical Physics 2014, Article605492, Theorems5–7 pp.5–6, expansion(66)/Theorems13–14 pp.9–10 and proof, Lemmas17–18/Theorems20–21 pp.11–14 https://onlinelibrary.wiley.com/doi/pdf/10.1155/2014/605492; Hassi–Wietsma arXiv:1312.7248v1 Section2.2/Proposition2.4 p.4 and Theorem4.5/proof pp.15–18 https://arxiv.org/pdf/1312.7248v1; existing finite-rank/Gallier coverage reused.
COMPARISON: Finite-negative-square membership is a hypothesis, not supplied by L777's local zero-free F. The inspected kernel bounds do not determine the nullity or inertia of the prescribed coupled J-Q. Rational index formulas do not identify the full reciprocal tail as rational. A real-point Taylor-Hankel necessary test is available by precise citation, without global zero assumptions.
GAP: Exact projection weighting, actual half-plane class/index, and a comparison controlling J-Q remain unpaid. No source imports the requested actual-Xi inertia. A separately nominated finite Taylor-Hankel obstruction can test one proposed low index, not certify the desired minor sign.
REASON: New primary-source scope evidence parks the automatic generalized-Nevanlinna-to-inertia import and replaces unsupported membership with a bounded, independently testable necessary condition.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED concerns analytic class and boundary-kernel hypotheses outside step441's Schur/Fredholm coverage; this essential comparison is new, not repeated browsing of a ready target.
SCOPE: Literature-only step443. Known source interfaces are assessed; no kernel identity, actual matrix value, class membership/nonmembership, new lemma or mathematical script is derived. The next finite test has its own saved assessment and requires separate supervisor approval.

## Original step442 nomination — preserved definitions and open questions

Main gap: actual-Xi all-degree mixed positivity. A paid signed-inertia
bound could sign the exceptional family while allowing negative Schur
blocks. It would still leave general zero grouping, complex/multiple
poles, all mixed minors, radii and uniformity unresolved.

Essential inputs for the comparison are L776/L777/L779/L780; the actual
normalization and local real/simple grouping ultimately use
L017/L018/L021. Assume only an admissible pair r>=3, k=r-1 with
independently certified distinct real interior zeros and the zero-free
F neighborhood of L777. Positive coefficients exclude nonnegative real
zeros, so the proposed nodes lie in (-1,0). No statement about the
remaining zeros or a global Laguerre-Pólya representation is available.

## Proposed objects and discriminating source test

These are definitions and questions for review, not asserted identities
or estimates. Let beta_n be the positive Laurent coefficients of p/F.
On its disk of convergence define

    h_r(z)=sum_(n>=0) beta_(r+1+n) z^(n+1),
    K_ij=(h_r(alpha_i)-h_r(alpha_j))/(alpha_i-alpha_j),
    K_ii=h_r'(alpha_i),
    E=diag(sqrt(|d_i| |alpha_i|^r)),
    Q=(-1)^r E K E, J=diag(sign(d_i)).

An unfinished expansion of the exact projected pairing suggests testing
a diagonal similarity between I-C S and I-J Q. Establishing the exact
weighting and any consequent determinant/inertia relation is future
work, with convergence and all signs to be checked. It is not an input.
The proposed strong threshold is

    n_0(J-Q)=0 and n_-(J-Q)=n_-(J).

The notation n_0,n_- denotes nullity and negative eigenvalue count of a
real symmetric matrix. This allows indefinite blocks and is not the
abandoned demand for positive eliminated and reduced blocks. It must
not simply be assumed as an equivalent sign condition. The review must
identify a separately verifiable property of the actual h_r that could
imply it, or explain why the inspected kernel theory cannot do so.

Look for exact and stronger statements under generalized Nevanlinna,
finite-negative-square, divided-difference/Loewner and rational-Hankel
terminology. Retrieve primary hypotheses and load-bearing proof cases
before larger passages. Compare the exact prescribed coupling, the
Taylor-tail subtraction and the local-only real-zero premise. Real
coefficients and disk zero-freeness alone are not membership in a
half-plane function class. An import requiring all remaining zeros real
would be circular here. L780 must remain a consistency constraint; its
old positive-block test must not reappear under a new name.

Continue only if a source comparison yields an independently testable
actual-Xi kernel bound or a concrete analytic obstruction. If the only
premise is the desired inertia/minor sign, or global real zeros, park
that particular import and report the obstruction; do not derive and
approve uncovered mathematics during the literature turn. No parameter
sweep or full-certificate replay is proposed. Full matching Mathlib
coverage is unchecked. No essential source has yet been sought or
declared persistently blocked, and no cross-notebook input is needed.

## Completed source comparison — step443, 2026-11-04

The main gap remains actual-Xi all-degree mixed positivity. The reviewed
intermediate target is the proposed signed-inertia mechanism above; its
plausible downstream use is an exceptional-minor certificate that permits
the adverse blocks of L780. No general mixed-minor implication is supplied.

### Primary source statements and proof coverage

Song–Hao–Hu–Chen, *Some Propositions on Generalized Nevanlinna Functions
of the Class N_k*, 2014, Article605492, [publisher PDF](https://onlinelibrary.wiley.com/doi/pdf/10.1155/2014/605492):
Theorems5–7, pp.5–6, require conjugation-symmetric meromorphy on C\R;
membership means a uniform negative-index bound over all upper-half-plane
packets, attained by some packet. Confluent packets retain the bound.
Read the congruence/coalescence argument (30)–(44) and converse proof.
Theorem14, p.10, assumes f in N_kappa and the real nontangential
expansion (66), p.9,

    f(z)=h_-1+sum_(j=0)^(2m) h_j(z-t)^(j+1)+o((z-t)^(2m+1)),
    t real, m>=1, all h_j real.

It bounds n_-((h_(i+j))_(i,j=0)^m)<=kappa. Read Theorem13's
boundary-limit statement and Theorem14's complete limiting proof;
no strict sign/nullity conclusion follows. Lemmas17–18 and
Theorems20–21, pp.11–14, were also inspected: rational index formulas
require rational input; addition's exact-index conditions include pole
separation and boundary/infinity limits. They do not classify this tail.
These are cited inputs, not reproofs or claims of actual membership.

Hassi–Wietsma, *Products of generalized Nevanlinna functions with
symmetric rational functions*, [arXiv:1312.7248v1](https://arxiv.org/pdf/1312.7248v1),
27 December2013: Section2.2/Proposition2.4, p.4, characterizes an
N_kappa function by a finite rational canonical factor times an ordinary
Nevanlinna function. All nonreal poles and exceptional real poles/zeros,
with their multiplicities, enter that factor. A local zero-free disk
does not give it. Theorem4.5, p.15, starts with Q in N_kappa and a
real-symmetric degree-one rational s; finite-index product membership
is equivalent to nonnegativity of s on the spectral support except
finitely many poles. Inspected the proof pp.17–18 and Lemma4.6's
constant-sign/sign-changing and transformed negative-scalar cases
pp.16–17. Their spectral support, canonical factor and boundary signs
are additional data, absent here. No product theorem is imported for
p/F or a Taylor-subtracted tail. Higher-degree Theorem4.9 is an
unneeded lead, not assessed coverage.

### Applicability and exclusions

L777 supplies annular Laurent convergence and real coefficients; beta_n
means a coefficient of a positive Laurent *index*, not a positive value.
The coefficients retain their real signs. Its finite-rank theorem is
for the principal parts of c=F/p. The proposed h_r uses positive modes
of b=p/F. These are different functions; finite rank of H(tilde c)
does not identify h_r as a rational function of the same degree.
No such identification appears in L777 or the inspected sources.

The primary membership definitions quantify over arbitrary packets,
not just the k selected interior nodes. No canonical factor, positive
spectral measure or uniform kernel-index bound for the actual h_r is
in the local inputs. This is missing mathematical payment, not missing
source access and not a proof that no finite class can contain it.
Real analyticity on the node interval would make a boundary comparison
meaningful, but supplies neither a finite class index nor the coupling
to J. In particular an upper bound for the negative index of a kernel
matrix is not the requested equality for J-Q, and does not pay nullity.
No theorem inspected identifies that prescribed matrix as a realization
with the required index. This is the new source-scope obstruction.

L779, under its retained arithmetic contracts, supplies one positive
signed determinant despite norm>1. L780's negative eliminated block
does not assert that the proposed J-Q fails: the exact new similarity
has not been proved. Do not infer an inertia from either benchmark or
reintroduce positive eliminated-block margins. The analytic weighting,
its signs and its convergence remain future proof obligations.

Duplicate/failure checks: read the actual normalizations and needed
pairing ranges of L776/L777/L779/L780; reused the balanced-Schur and
signed-Schur assessments. The November1 generalized-Schur import
scope stop already separates interpolation existence from membership
of the actual function. The November3 real-residue assessment left
generalized-Nevanlinna work as an unread lead, not a prohibition.
Their obstructions survive; this comparison adds precise class and
real-point hypotheses for the new reciprocal-tail object. No other
notebook was read or used.

### Search record and route decision

Queries included `generalized Nevanlinna functions canonical factorization
negative squares poles theorem rational function`; `generalized
Nevanlinna divided differences Loewner matrix negative squares Taylor
polynomial subtraction`; `"Loewner" "Hankel" "negative index" rational
functions generalized Nevanlinna`; `"generalized Nevanlinna" "Taylor"
"subtraction"`; `"generalized Nevanlinna" "finite rank perturbation"
polynomial`; `"projection" "reciprocal" "xi" "Nevanlinna"`;
`"Riemann xi" "reciprocal" "Hankel"`; `"xi" "Taylor" "negative
squares"`; and `"generalized Nevanlinna" "reciprocal" "Riemann"`.
The bounded search found the above standard machinery, not a theorem
for this prescribed tail/coupling. Search results about reciprocal-square
zero moments, logarithmic derivatives and finite interpolation concern
different functions; they remain unread leads, not theorem evidence.
No conclusion of novelty or comprehensive absence follows.

Park the automatic class-to-inertia import. Nominate only the concrete
necessary-condition diagnostic in
`drafts/literature/2026-11-04-reciprocal-tail-taylor-index-test.md`.
It tests the optional low-index ansatz g_3=-h_3 in N_1 at L779's
fixed pair by a small Taylor matrix. N_1 is a proposed premise to test;
it is neither known nor asserted necessary or sufficient for the
desired J-Q threshold. A certified excess index would reject that
ansatz even if the exact weighting were later established. Passing
the finite test would establish no membership or sign. No matrix was
formed or inspected this turn. The new assessment receives separate
approval before mathematics; no full-certificate replay, radius sweep
or automatic increase of matrix size is justified.

All needed cited sources were accessible. One publisher screenshot
request timed out, while the complete relevant PDF text was available;
this is not an essential source blocker. Full matching Mathlib coverage
is unchecked. No known-result reproof, lemma/script write, mathematical
exploration, PROOF update or DAG change occurred.
