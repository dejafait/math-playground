# Directional Fourier mechanism — completed source comparison

TARGET: Assess whether finite-characteristic Fourier analysis of the seven directional constancies can force a common nonzero coefficient annihilator on the pinned full sheet, without a translation action on messages.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the full-sheet, cone, span-three fiber and design-matrix comparisons; checked ATTEMPTS/109–112 and searched corresponding working records for translation invariance and coefficient-function modules. New finite-characteristic Fourier, uncertainty, Fourier-minor and variable-coefficient searches and actual readings are recorded below; no exact matching annihilator theorem was located.
SOURCE_EVIDENCE: Inspected EKL (2017) Proposition 2.6 and proof, Section 3.1/Proposition 3.1 and proof, Definition 4.1/Propositions 4.3–4.4 and proofs; GGI arXiv:math/0310169v1 Theorem B and proof/equality discussion, pp. 2–4, and Theorems C/E hypotheses; Borello–Sole arXiv:2007.04159v2 Section 2.3/Proposition 2 and full proof; Emmrich–Kunis arXiv:2506.02947v2 Lemma 12, Theorem 16/Corollary 17 and proofs, pp. 8–10, plus correction acknowledgement p. 13. Primary links and retained copies appear below.
COMPARISON: Algebraic character decomposition and GGI's arbitrary-field translate-module bound are usable tools without a message action. Neither identifies the generated translate module with the coefficient-function span. Cyclic product uncertainty does not establish a three-function annihilator; complex plane uncertainty does not cover K. Corrected Fourier-minor results require additional hypotheses, not merely characteristic different from 137.
GAP: No common annihilator or uniform bound on label-dependent Fourier mixing is established. The concrete new bridge is whether U=span_K{1,a_0,a_1,a_2} is closed under the two unit translations; it must be proved, never assumed. Its separate proposed test is documented in 2026-10-29-coefficient-function-translation-closure.md.
REASON: Complete this bounded review without importing an annihilator theorem. Park direct complex/full-minor import and narrow the algebraic route to an independently falsifiable closure claim using available finite-field module theory; no residual-rank replay, equivariance assumption or new mathematical result is approved as true.
SCOPE: Pinned L030 full sheet with q=137, T={16,64,70,102,112,118,121}, E=F_65537, F=F_(65537^28), H=<19139>, k=64, arbitrary 61-core C and bijection sigma, K=E or F, repeated quadratic messages and all seven direction classes; no retained-family or RS-transfer assertion.
LITERATURE_REASON: The saved REVIEW_REQUIRED Fourier target had essential unread positive-characteristic and variable-label source hypotheses; this is its first primary-source comparison, not additional browsing of a ready mathematical target.

## Exact proposed intermediate target and downstream use

Write the existing messages as
g_P(X)=a_0(P)+a_1(P)X+a_2(P)X^2. The proposed bound is a common
nonzero lambda=(lambda_0,lambda_1,lambda_2) in K^3 with

\[
 \sum_{j=0}^2\lambda_j\bigl(a_j(P)-a_j(0)\bigr)=0
 \quad\text{for every }P\in\mathbb F_{137}^2.
\]

This is the explicit dimension-at-most-two threshold to be assessed,
not an established statement. C137a would then exclude dimension
exactly two. The full-sheet-to-retained-family and RS-list transfer
remain separate gaps even if this local program succeeds. C137a,
L135 and L137 are available local geometry inputs; L030 supplies the
inherited labeling setup. No cross-notebook result is proposed.

The given directional constancies have label-dependent coefficients:
for fixed t and y, a_0(P)+x_(t,y)a_1(P)+x_(t,y)^2 a_2(P) is constant
on u+tv=y. Review finite-group character decomposition and any relevant
finite-characteristic uncertainty or directional-support theorem against
these exact equations. Do not replace x_(t,y) by a constant, identify
the two fields, assume the labels are affine functions, or assume
auxiliary translations act linearly on the coefficient images.

## Bounded source decision and future creative test

Read primary theorem hypotheses and the essential field-dependent proof
cases first. Check whether the needed characters exist over K or a
splitting extension, what extension/descent is allowed, and whether any
claimed complex or prime-order Fourier-minor theorem actually holds
in characteristic 65537. A complex norm inequality or unverified
sufficiently-large-characteristic assertion is not an import.

Continue toward a later proof_attempt/creative only if the comparison
provides an applicable algebraic tool and a concrete all-label test
for the displayed annihilator. The obstruction to address is the
mixing caused by arbitrary x_(t,y) in each direction, which prevents
assuming a translation-invariant coefficient system. A successful
future bounded test must establish the annihilator uniformly, or give
an exact allowed full-sheet assignment refuting it. Merely expressing
the stopped residual matrix in another basis is not progress. If the
source only covers equivariant maps, complex positivity, generic
labels or an unverified characteristic range, record that obstruction
and park the dependent Fourier route.

This potential mechanism addresses the remaining coefficient case;
its relevance does not certify feasibility or novelty. Primary source
coverage is the immediate blocker to creative work. The reflected
search budget remains exhausted, and the BDWY/DSW field-transfer
obstruction remains recorded. No result, Fourier calculation,
mathematical script, theorem approval or Mathlib coverage claim for
this continuation is supplied by the completed C137a audit.

## Completed primary-source decision, step 547

The preceding proposed test records the starting gate, superseded as to
unread-source status by this section. This turn supplies source coverage,
not the annihilator or a Fourier reduction of the equations. The main gap
and proposed downstream use remain as stated above. The continue/abandon
test separates applicable algebraic tools from unsupported strong
uncertainty import. A precise closure test is proposed for separate
approval; it is not an established lemma.

### Primary statements, proof cases and applicability

**Evra, Kowalski and Lubotzky**, *Good cyclic codes and the uncertainty
principle*, L'Enseignement Mathématique 63 (2017), 305–332,
[journal PDF](https://ems.press/content/serial-article-files/44351),
Proposition 2.6/proof, pp. 309–310; Section 3.1/Proposition 3.1/proof,
pp. 312–313; Definition 4.1/Propositions 4.3–4.4/proofs, pp. 316–318.
For a finite coefficient field B of cardinality Q and prime p different
from its characteristic, Proposition 2.6 decomposes B[X]/(X^p-1) as B
plus (p-1)/r copies of B's degree-r extension, r=ord_p(Q). Its proof
checks separability, CRT, splitting degree and every nontrivial factor's
degree. Either K is allowed at p=137; no particular r is calculated here.
Section 3.1 is stated over C. Proposition 4.3 concerns prime-base-field
coefficients and primitive characteristic modulo p, not arbitrary
splitting-field coefficients. Proposition 4.4 uses characteristic p,
so cannot be used at characteristic 65537 with p=137. These are module
tools, not label rigidity; there is no auxiliary-field embedding or
characteristic-zero transfer.

**Goldstein, Guralnick and Isaacs**, *Inequalities for finite group
permutation modules*, [arXiv:math/0310169v1](https://arxiv.org/pdf/math/0310169v1),
11 October 2003, Theorem B/full proof, PDF p. 3; equality discussion,
pp. 3–4; Theorems C/E hypotheses, pp. 4–5. For a finite transitive
G-set S, any field B and nonzero v in B[S], Theorem B gives
|supp(v)| dim_B<vG> >= |S|. The translate-basis proof uses support
coverage without norms. Equality entails block support and proportional
translates with equal support. It applies to translating functions on
the auxiliary domain, without an action on messages. The module <vG>
contains all translates and need not lie in span{1,a_0,a_1,a_2}.
Theorem C needs a primitive action; Theorem E needs prime cardinality
and characteristic zero. Neither is an automatic sheet bound. No
specialization or equality-case result is proved in this turn.

**Borello and Solé**, *The uncertainty principle over finite fields*,
[arXiv:2007.04159v2](https://arxiv.org/pdf/2007.04159v2), 23 March 2021,
Section 2.3, p. 4, and Proposition 2/full proof, p. 7. For length n
coprime to the coefficient-field cardinality, evaluation at powers of
a primitive n-th root in the algebraic closure gives Hamming-weight
product at least n. The proof retains both divisibility cases in its
cyclic zero-gap/BCH argument. This covers a cyclic restriction of length
137, not the noncyclic sheet group relabeled as length 137^2. A scalar
support conclusion does not bound the joint coefficient span.

**Biró and Lev**, *Uncertainty in finite planes*,
[arXiv:1808.07424v2, author copy](https://users.renyi.hu/~biroand/pdfs/Uncer.pdf),
31 August 2018, p. 1 setup and Theorem 1, p. 5, were inspected online.
The function space is complex-valued; Theorem 1 additionally requires
rational values. A finite domain does not give a finite coefficient
field. No theorem is imported for K; later proofs were not read.

**Emmrich and Kunis**, *Real and finite field versions of Chebotarëv's
theorem*, [corrected arXiv:2506.02947v2](https://arxiv.org/pdf/2506.02947v2),
30 September 2025, Lemma 12/proof, p. 8; definition of m_(A,B) and
Lemma 13/proof, pp. 8–9; Theorem 16/Corollary 17/full proofs, p. 10.
Write ell for the characteristic and p for matrix order. Frobenius
propagates vanishing only under powers of ell. Theorem 16/Corollary 17
assume ord_p(ell)=p-1 and use the integer
m_(A,B)p-s_A(1,...,1), with m_(A,B) the Schur coefficient mass having
B-weighted exponent divisible by p. Nondivisibility by ell suffices
for that minor; a displayed maximum gives a sufficient all-minor cutoff.
Neither all the nondivisibilities nor the cutoff at (137,65537) is
verified. The p. 13 acknowledgement corrects v1's Lemma 12/nonprimitive
corollary. That broad v1 statement must not be imported. The corrected
result still gives no variable-label annihilator theorem. No cutoff
calculation or new minor claim is made here.

### Decision and reading limits

Arbitrary x_(t,y)-multiplication remains in the original equations.
No inspected theorem says it preserves a frequency or the small
coefficient-function space. Pointwise cancellation cannot be replaced
by a support assertion for each summand. A splitting extension is
available; transform identities and any annihilator descent still
need justification when actually used. Working with K-valued cyclic
modules offers a route independent of positivity and all-minor claims.

The proposed next test asks for translation closure of the small
function space itself: uniform membership of each translated a_j in U,
or an exact allowed assignment violating it. This is a bridge to prove,
not a presumed message action, renamed residual-rank solve or reopened
reflection search. If it holds, the source's nontrivial cyclic factor
degrees offer a possible dimension obstruction. The arithmetic and
conditional implication remain future mathematical obligations.

Queries included `Fourier transform finite fields uncertainty principle
arbitrary field characteristic Chebotarev Meshulam`; `uncertainty
principle finite fields Fourier minors characteristic p Goldstein
Guralnick Isaacs`; `Inequalities for finite group permutation modules
pdf`; `finite field Fourier transform convolution theorem arbitrary
field roots unity Maschke uncertainty`; and targeted directional,
variable-coefficient and coefficient-function translation searches.
The latter yielded no matching theorem, which is not a novelty claim.
The Fourier-minor lead exposed the v2 correction, then checked in the
primary text. Nicholson's 1971 abstract was a lead only (publisher full
text returned 403), not an essential input. There is no persistent
access blocker for the limited algebraic tools selected.

Downloaded version-pinned PDFs and extracted text are retained in
`drafts/sources/directional-fourier/`; v1 records the superseded claim.
The working record preserves reading scope. Full and supporting
Mathlib coverage is not checked. No lemma, mathematical script,
PROOF.md or DAG change was made. NEGATIVE concerns direct strong
uncertainty import, not the truth of the annihilator or RS target.
The 955–957 bracket is unchanged; PROGRESS.md selects the next action.
