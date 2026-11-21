# Source comparison: analytic ellipticity and the fixed bump's support edge

TARGET: Determine whether a primary analytic support theorem applies to L720 and proves limsup_(q->infinity) log|integral_I chi(v)*p_(12q+3)(v)dv|/(12q+3)=max_(v in supp(chi)) Re S(v), for the original fixed L703 bump without an endpoint law.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 193 searched analytic elliptic support/analytic-wavefront theorems, complex-curve Laplace moments and sampled Laplace/Muentz support results; compared the saved inner-symbol, remainder-rate and size-generating-function assessments and common-phase/gamma-Rice failures. The primary statements and relevant proof cases listed below were read; no exact matching transfer theorem was found, with no novelty inference.
SOURCE_EVIDENCE: Deleporte arXiv:2306.15382v1 Definitions 3.1/3.2/3.12/4.5, Propositions 3.5/4.2/4.16/4.23/4.24 and Section 6.2; Hitrik--Sjostrand arXiv:1508.00649v1 Section 2.2 Theorem 2.2.3 and Section 2.7 Theorem 2.7.1; Mazzucchelli--Salo--Tzou author-hosted 46-page version Definition 1.5, Theorems 1.2/1.3/6.1 and Section 5.2; Arendt--Batty--Hieber--Neubrander (2011), Theorem 2.8.3 p.103 and Proposition 2.4.3 pp.79--80. Exact links, reading limits and hypotheses below.
COMPARISON: Known analytic ellipticity preserves analytic singularities for an identified operator; the one-sided support theorem then gives local uniqueness. Sampled real Laplace support already allows signed/vector-valued data, but uses a fixed function and real Laplace coordinate. None identifies L720's nonlinear complex, integer-only array with the needed operator or proves its boundary singularity. Pointwise ellipticity alone is insufficient for importing any of these results.
GAP: Test an exact discrete analytic Cauchy/operator realization near a maximal-Re(S) support point, including phase geometry, collisions of exp(-12*S), an elliptic inverse and the whole exponentially small remainder; only then could a nonremovable singularity force the requested sampled rate. These are unproved applicability obligations, not assumptions granted by this assessment.
REASON: Essential general-tool comparison now supports one bounded discrete support-transfer attempt under EXPLORE, after separate supervisor approval of this changed assessment. No signed rate, new specialization or lemma was derived here; direct real-Laplace and bare-ellipticity imports are not licensed. The construction can fail informatively without settling the rate.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target introduces outer support-edge transfer beyond the ready inner-symbol scope; the present primary comparison answers that missing-coverage request and must be reused if its target and hypotheses remain unchanged.
SCOPE: Only TARGET with the original fixed L703 bump, audited L714 (1)--(5), L715/L716, L719 and L720; one bounded test of a discrete analytic Cauchy/operator realization and its support-edge implications. No endpoint law, analytic extension of chi, replacement bump, noninteger gamma interpolation, common-phase assumption or unproved L713/L714 (6)/L717/L718 input is covered.

## Fixed input and precise question

Use the original positive bump chi on I=[omega-delta,omega+delta],
with all L703 choices fixed before n. Do not select a different bump,
width, endpoint flattening law or analytic extension. Retain L714's
audited finite kernel and signed decomposition, L715 F and L716 moment
identification, and the newly audited L719--L720 expansion. In particular
U=121/64, A=27/10, d=5/4, alpha=11/8, u=(3+4i)/10 and n=12q+3.
S is exactly L720's complex phase. The support is that of this positive
bump in I; it need not fill the prescribed enclosure I. Set log(0)=-infinity.
The equality in TARGET is a question, not an established bound or rate.

The first source test is whether elliptic analytic amplitudes preserve
a support-edge singularity strongly enough to force the stated exponential
limsup on this arithmetic subsequence. A result only for continuous
large parameters, a fixed amplitude, a linear phase, or a specified
endpoint asymptotic must be distinguished from the actual target.
The comparison must address phase geometry, possible cancellation at a
common generating-variable image, and the entire optimally truncated
error. Do not assume these hypotheses hold merely because a_0 is nonzero.

## Continuation or abandonment test

Continue to a later mathematical turn only with a precisely cited primary
theorem and a list of its actual applicability obligations, or a bounded,
independently testable missing specialization after adequate comparison.
Do not infer a signed rate from pointwise ellipticity or from a radius
formula without proving a nonremovable singularity. If the sources only
relabel the desired rate or require an unsupported endpoint/noncancellation
premise, preserve that limitation and select a materially different test.
No mathematics is derived or approved in this nomination.

The plausible downstream use is comparison of the actual signed bump
contribution K_n with the actual residue contribution, whose rate still
requires a separate audit. L714 (6), L713, L717 and L718
are not established premises here. The prior common-phase, gamma/Rice,
horizontal-envelope and blend failures retain their scopes; the new
input is L720's verified factorial amplitude, not a renaming of them.
Other response terms, complementary Jensen defect, amplitude/full
charge, H/support, Xi realization and all-degree mixed positivity
remain independent gaps. Full matching Mathlib coverage is not checked.

## Step 193: primary theorem comparison, 3 November 2026

The preceding fixed question and continuation test were nominated in
step 192. This section completes their source review only. It does not
prove a transfer statement. The full RH gap remains actual-Xi
all-degree mixed positivity; this intermediate input could eventually
help compare the signed K_n contribution with P_n in the finite-family
spatial response. That comparison would still leave the other responses,
complementary Jensen defect and Xi realization unresolved.

### Local overlap and recorded stops

Read the hypotheses and conclusions of L703, L714, L719 and L720, the
saved `2026-11-03-signed-bump-remainder-rate.md`,
`2026-11-03-signed-bump-size-generating-function.md` and
`2026-11-03-signed-bump-analytic-symbol.md` assessments, and
`ATTEMPTS/2026-11-03-signed-bump-common-phase-stop.md` and
`ATTEMPTS/2026-11-03-signed-bump-gamma-rice-size-stop.md`.
The latter records are failure evidence within their stated scopes;
L717 and L718 were not promoted to established inputs. The earlier
Pringsheim/root-test and endpoint-saddle comparisons are reused, not
repeated as new findings. A positive chi does not provide positive K_n
coefficients. The original plateau does not specify its support edge
or an endpoint flattening law. L720 supplies only integer samples and
fixed-complex-domain factorial bounds, not a continuous size symbol.

No matching local discrete analytic-support assessment was found in
the specific signed-bump assessment paths searched. This is a local
overlap check, not a claim of mathematical novelty or a notebook-wide
survey.

### Primary statements and proof cases actually read

**Analytic symbol inversion.** M. Hitrik and J. Sjostrand,
*Two Minicourses on Analytic Microlocal Analysis*,
[arXiv:1508.00649v1](https://arxiv.org/pdf/1508.00649v1),
Section 2.2, (2.2.1), printed pp.32--33, Lemmas 2.2.1--2.2.2 and
Theorem 2.2.3 with proof, pp.35--36; Section 2.7, Theorem 2.7.1
and proof, pp.54--55 (PDF indices 53--54). A classical analytic symbol
has holomorphic coefficients with locally uniform C^(k+1) k^k bounds.
An elliptic symbol has an analytic symbolic inverse; the proof uses a
small remainder and a convergent symbolic Neumann series. The
elliptic-regularity application concerns a fixed distribution and an
analytic-coefficient differential operator, conjugated by an FBI
transform. It uses an actual operator inverse on weighted holomorphic
germs. This extends the earlier stationary-phase reading to the
inverse mechanism; it supplies neither a discrete moment operator nor
a theorem for the present scalar samples. No reproof is needed or
authorized for this known inverse theorem.

**Analytic operators, realizations and Fourier modes.** A. Deleporte,
*The Szego kernel in analytic regularity and analytic Fourier Integral
Operators*, [arXiv:2306.15382v1](https://arxiv.org/pdf/2306.15382v1),
27 June 2023: Definitions 3.1--3.2, Proposition 3.5 and its
optimal-truncation/cutoff-derivative proof cases, pp.11--14; Definition
3.12, p.22; Definition 4.5 and (7), p.25; Propositions 4.2,
4.16(1)--(3), 4.23--4.24 and their relevant proofs, pp.24,35,40--41;
Section 6.2 in full, pp.52--53. The
[versioned HTML](https://arxiv.org/html/2306.15382v1) was used to resolve
formula extraction. Formal amplitudes have joint factorial derivative
estimates; realizations differ exponentially little on complex
neighborhoods. Positive nondegenerate phases and boundary positivity
are operator hypotheses. Proposition 4.23 gives
WF_a(u) subset {a_0=0} union WF_a(Op(a)u); its proof applies a
microlocal inverse. Proposition 4.24 supplies only the forward
wavefront inclusion for general FIOs. Section 6.2 uses an
S^1-invariant structure and a nonzero contact pairing to pass to Fourier
modes; it is not a theorem for arbitrary sampled arrays. Its
realizations and exponential-error cases were inspected, not imported
as an identification of our array.

**Support from analytic singularities.** M. Mazzucchelli, M. Salo and
L. Tzou, *A general support theorem for analytic double fibration
transforms*, [author-hosted 46-page version](https://users.jyu.fi/~salomi/pub/MazzucchelliSaloTzou2023.pdf),
retrieved 2026-11-03; associated preprint arXiv:2306.05906. Numbering
here is that of the retrieved author file, not an asserted byte match
with an arXiv version. Read Definition 1.5 and Theorems 1.2--1.3,
pp.4--5; Theorem 5.1 and its localization proof, pp.27--28; Theorem
6.1 and its immediate application, p.42. The analytic double fibration
has submersive projections, an analytic nowhere-zero weight and the
stated dimension restrictions. Bolker requires a unique preimage and
injective differential of the left canonical projection. The proof
uses uniqueness to exclude the remote localized term. Theorem 6.1
states the standard microlocal one-sided uniqueness theorem for a
distribution across a C^2 hypersurface, assuming absence of either
conormal analytic-wavefront direction; it cites Hormander,
*The Analysis of Linear Partial Differential Operators I*,
Theorem 8.5.6'. These are continuous transform statements, not sampled
scalar-rate assertions. The original SKK/Hormander proof was not
reconstructed here.

**Sampled signed Laplace support.** W. Arendt, C. J. K. Batty,
M. Hieber and F. Neubrander, *Vector-valued Laplace Transforms and
Cauchy Problems*, 2nd ed., Monographs in Mathematics 96,
Birkhauser, 2011,
[Theorem 2.8.3, p.103](https://link.springer.com/book/10.1007/978-3-0348-0087-7),
read in the [book-text reproduction](https://epdf.mx/vector-valued-laplace-transforms-and-cauchy-problems-second-edition.html).
It assumes tau>=0, f in L1_loc(R_+,X), and finite abscissa of
Laplace convergence. Support starting at tau is equivalent to
limsup beta_n^(-1) log||f-hat(beta_n)||=-tau on every Muentz sequence
(gaps at least one and divergent reciprocal sum). No positivity of f
is required. Read all five clauses, the definition of the convergence
abscissa in Section 1.4, and Proposition 2.4.3 with both proof
directions, pp.79--80. Its inversion proof uses a fixed real-coordinate
Laplace transform. The notes attribute the sampled extension to
B. Baeumer, *On the inversion of the convolution and Laplace transform*,
Trans. AMS 355 (2003), 1201--1212,
DOI 10.1090/S0002-9947-02-03174-4. That original article was inaccessible
and its proof is not claimed read. The complete book statement is
available; the article is not an additional premise for this comparison.

### Applicability obligations, all still unpaid

The following are tests for a later mathematical turn, not derivations
or granted hypotheses. They isolate a possible specialization rather
than replacing the target by a noncancellation assumption.

1. **Exact discrete object.** Test whether the generating germ formed
   directly from the permitted samples, with the fixed polynomial
   normalization in size handled explicitly, has a local analytic
   Cauchy/FIO description. A continuous-size realization chosen from a
   formal symbol is not automatically the exact sequence. Neither a
   gamma interpolation nor a guessed generating-function pole suffices.
2. **Geometry and arithmetic sampling.** Determine the maximal-Re(S)
   support point(s), check regularity and injectivity of the phase
   coordinate there, and check collisions under the candidate image
   v -> exp(-12*S(v)). Separate all other supported points with the
   same image or prove their contribution cannot remove the germ's
   singularity. This is the sampling/alias obligation, not a fact
   inferred from the narrow interval alone. Use L719's audited phase
   and saddle facts, not L717's unaudited winding conclusion.
3. **Applicable ellipticity.** Identify an operator whose principal
   symbol is the required nonzero amplitude after all coordinate,
   density and size changes. Verify the actual positive-phase,
   nondegeneracy and domain conditions of the chosen calculus, or
   justify a different precise known analytic-operator theorem. The
   scalar inequality inf|a_0|>0 is only an input to this test. A
   forward FIO wavefront inclusion cannot be read backwards.
4. **Actual support boundary.** Test whether a faster sampled rate
   would force analytic regularity across an actual support boundary
   of this same chi via that inverse. Specify the boundary value or
   analytic functional on which the inverse acts and account for
   the one-sided support premise. No analytic continuation of chi,
   known endpoint law or absence of cancellation may be assumed.
5. **Whole remainder.** Prove that the exact L720 remainder, including
   its full contour complement, produces a holomorphic/analytic error
   through the relevant local boundary after the discrete construction.
   Finite-order errors relative to a signed integral do not suffice.
   Exponential smallness must hold on the required common complex
   domain and with the growth weights of the operator construction;
   no comparison with an unknown signed leading integral is assumed.

The real-coordinate Laplace theorem cannot be applied by declaring
f(v)=chi(v)*a_n(v): that varies with n. Nor does replacing S by Re(S)
represent the signed samples. The double-fibration theorem does not
apply just because there is a scalar integral: its geometry and data
space have to be constructed. Section 6.2 of Deleporte gives a
Fourier-mode mechanism under substantial extra structure, rather than
permission to discard the arithmetic subsequence. These are
hypothesis comparisons, not counterexamples to TARGET.

Continue only if a bounded construction supplies the missing exact
operator/germ and checkable local hypotheses, or establishes an
informative obstruction to that construction. Stop this specialization
if it merely assumes the desired boundary singularity, hides an alias
cancellation, requires an unsupported positive phase, or controls only
a finite asymptotic truncation. A partial operator/geometry result may
be useful while other obligations remain explicit. Do not assert the
limsup equality before proving its lower implication for the exact
samples; retain log(0)=-infinity. The actual residue rate and all full
response/Xi comparisons remain separate.

### Search record, access limits and decision

Queries included the following exact formulations (variants with
author names were used to retrieve the primary statements):

- `"analytic symbol" "support theorem" Laplace transform`
- `"Laplace transform" "support" "complex curve" theorem`
- `"analytic wave front" "elliptic" "Fourier integral" support theorem`
- `"Laplace transform" "support theorem" complex ray signed compact support`
- `"moments" "analytic arc" "Cauchy transform" singularities`
- `"Deleporte" "analytic Fourier" elliptic 2023`
- `Baeumer "support theorem" "Laplace" Muentz` (also accented spellings)
- `"Phragmen-Mikusinski" support theorem Baeumer` (accented spellings)
- `"Laplace transform" "support theorem" "Muentz"` (accented spelling)
- `Baeumer 2003 Laplace transform "support" theorem inversion`
- `"A generalization of Carleman" "discrete" Phragmen authors`
- `"Baeumer" "Phragmen" "1997"` (accented spellings)
- `"Baeumer" "Laplace Transform Methods" pdf`
- `"Support theorem" "1.7.7" Laplace`
- `"Baeumer" "inversion" "Phragmen" Laplace support` (accented spelling)
- `Baeumer "On the inversion of the convolution and Laplace transform" pdf`
- `Arendt Batty Hieber Neubrander "1.7.7" support pdf`
- `"support theorem" "Muentz" "Laplace" pdf Arendt` (accented spelling)
- `"Vector-valued Laplace" "pdf" Arendt Batty 2011`
- `"Laplace" "Theorem 2.8.3" support`
- `"Baeumer" "inversion" site:maths.otago.ac.nz`
- `"On the inversion of the convolution" site:otago.ac.nz`
- `"Baeumer" "1201" "pdf" inversion`
- `"A general support theorem for analytic double fibration transforms" arxiv`

The Citeseer *Operational Methods* lead failed to open; the ABHN book
statement above replaced that lead. AMS access to Baeumer failed
(403/unavailable); Springer chapter access also failed, while the
book-text reproduction was readable. Direct shell retrieval from arXiv
failed DNS, so versioned web PDF/HTML were used. A modern
`arXiv:2610.18992` Section 3.1 citation was followed only to locate
ABHN Theorem 2.8.3; its derived theorem is not an imported input.
Complex-arc Pade, complex-curve Laplace uniqueness and discrete
Carleman search leads were not inspected at theorem level and are not
premises. No essential inaccessible theorem is being silently used.

DECISION EXPLORE records sufficient tool comparison for one bounded
specialization test after separate next-turn approval. It is not an
IMPORT or a proof that the displayed tools apply. The exact target is
preserved. This is literature EXPLORATION, with no new mathematical
lemma, calculation or script. The proposed work develops known
analytic elliptic machinery in a difficult discrete setting; it is not
labeled creative merely to meet discovery scheduling. No independently
source-ready new central mechanism was identified in this bounded
review. Full matching Mathlib coverage remains not checked.
