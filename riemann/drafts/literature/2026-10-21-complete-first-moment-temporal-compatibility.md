# Source comparison: complete first-moment temporal compatibility

TARGET: Test whether L449's unchanged complete conditional first moments satisfy the temporal x identity in distributions on every sufficiently large real-H interval.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 303 reused the raw-second occupation/regularity assessments, searched complete-mean and first-moment compatibility in the scoped local records, and searched occupation measures/conditional first moments/Liouville and prescribed moments/weak derivative terminology externally. No inspected theorem decides this constructed law; unsuccessful searches establish no novelty.
SOURCE_EVIDENCE: Lasserre--Henrion--Prieur--Trelat math/0703377v1 (2007-03-13), Sections 2.1--2.3, (2.1)--(2.3), (2.7), (2.10)--(2.12), printed pp. 3--5; Hunter, Notes on Partial Differential Equations (revision 2014-06-18), Definition 3.1, Examples 3.3--3.5, pp. 47--49, and Theorems 3.60, 3.62--3.63, pp. 79--80; Bell (2015-10-21), Section 1 Theorem 1 and derivative uniqueness, Section 3 Lemmas 2--3 with complete proofs and the argument preceding Theorem 4.
COMPARISON: The known necessary occupation identity admits linear state tests, and known one-dimensional weak-derivative calculus applies to locally integrable signed means. Neither source supplies the complete mean's regularity, branch cancellation, actual defect, or eventual compatibility. L445's raw-second regularity does not decide these questions.
GAP: In a separate research turn test the full M_H=pY+k_+Z_++k_-Z_-+wm against the saved identity, keeping every original branch, probability and translation; establish complete cancellation or a genuine distributional defect with the required real-H quantifier. No such verdict is derived here.
REASON: Essential general source coverage now suffices for this exact necessary-condition test. The remaining signed-branch analysis is a law-specific specialization, not a missing general theorem, and must occur after this literature turn.
SCOPE: Exactly the unchanged L449 complete first mean and the temporal x identity on each fixed [H,2H], with L429's original cutoff; no changes of law, covariance completion, new occupation family, actual excursion or trajectory sufficiency claim.
LITERATURE_REASON: The supplied target was REVIEW_REQUIRED because it changes the raw-second scope to complete signed first moments. This separate comparison resolves that missing scope; it does not repeat literature on an already ready target.

## Exact target and relevance

The main gap remains global mixed positivity. The intermediate target
is a necessary realization test independent of the derivative-forced
covariance block. A failure would stop an eventual-ray extension with
these means fixed; success would remove only this necessary condition.
It supplies no RH sign or zero-exclusion range.

Use the original pointwise definitions and write

    M_H(t)=p(t)Y(t)+k_+(t)Z_+(t)+k_-(t)Z_-(t)+w(t)m(t).

The saved question is whether, for every phi in C_c^1((H,2H)),

    integral_H^(2H) [phi'(t)(M_H)_1(t)
                         +L(t)phi(t)(M_H)_2(t)] dt=0

holds for every sufficiently large real H. This is the question to
be tested, not a proved identity. Do not replace its exact zero by o(1).
No new law-specific lemma or calculation is made in this source turn.

## Primary inputs inspected and limits

J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat,
*Nonlinear optimal control via occupation measures and LMI-relaxations*,
SIAM J. Control Optim. 47 (2008), 1643--1666,
DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, printed pp. 3--5: the system has smooth vector
field, bounded measurable controls and compact state/control sets.
Equation (2.12), read with its defining measures and preceding
chain-rule argument, is a necessary identity for every C1 test.
It is not restricted to quadratic tests. For the local dynamics in
L443 (2), linear state tests with compact temporal support are admissible
on each fixed finite box. The boxes need not be uniform in H.
For an ensemble of trajectories, integration of the necessary identity
requires integrable tested quantities; it does not require continuous
conditional atom selections. Remark 2.2's converse concerns a measure
already defined from a trajectory, not arbitrary Borel laws. No
optimal-control converse or superposition theorem is used here.

John K. Hunter, *Notes on Partial Differential Equations*,
[author-hosted revision 18 June 2014](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
Definition 3.1 and Examples 3.3--3.5, printed pp. 47--49;
Theorems 3.60 and 3.62--3.63, pp. 79--80. The definition uses locally
integrable functions and smooth compact interior tests. The
one-dimensional characterization gives an AC representative for an
integrable weak derivative; the fundamental theorem and integration
by parts include representative and endpoint qualifications. The
appendix gives a proof outline, not full proofs of all statements.
The jump and Cantor cases show why a.e. classical differentiation alone
is insufficient. Apply these results on compact interior subintervals
without presupposing AC of M_H. Compact temporal tests impose no
endpoint equality. The C1 test class in the saved target must be
retained; if research works through smooth tests, it must justify its
passage back to that class. No general theorem is to be reproved.

Jordan Bell, *Sobolev spaces in one dimension and absolutely continuous
functions*, [author's note, 21 October 2015](https://jordanbell.info/LaTeX/mathematics/sobolev1d/),
Section 1 Theorem 1 and subsequent uniqueness paragraph, and Section 3
Lemmas 2--3: read the complete mollifier/Lebesgue-point proof,
zero-integral-test-primitive proof, and Fubini proof of the indefinite
integral derivative. These use local integrability. The proof preceding
Theorem 4 explains reconstruction up to an a.e. constant; Theorem 4
itself assumes H1(R) and adds an L2 Holder bound. Do not cite that
final theorem as an unrestricted W1,1 interval theorem. Hunter gives
the required interval characterization. The cited Brezis, Leoni,
Rudin and Hormander references were not independently inspected and
are not additional imports.

## Local hypotheses and precise specialization still owed

The precise local formula ranges read were L421's high definition and
sign rule (3), L437's direction definitions (3)--(4), L438 (6)--(17),
L443 (1)--(2), L445's high/intermediate/translation analysis through
(6), and L449's preservation hypotheses/conclusion. Their existing
Borel definitions and fixed-H envelopes ensure that the complete
first-moment integrals are well-defined. L449 changes centered
covariance and preserves the conditional mean. Thus neither its
endpoint bump nor the bulk basis selection gives a new mean formula.

For the later mathematical test retain the high sign s=1 when
D(X0;t)B(X0;t)>=0 and s=-1 otherwise, both branches of r, and the
rho0=0 convention. Retain L421's larger-absolute-projection rule,
its prescribed equality choice and final positive-B orientation for
n_+, and L437's exact n_-=U/|U|. Retain F_H's two signed parts,
both positive h denominators, w=1-p-k_+-k_-, the complete J_R and
W_H entering d_H, and m=d_H b/|b|^2. At fixed H, the stage j(H),
F_H calibration parameters and all integrated parameters are constants
in temporal differentiation. The original cutoff remains unchanged.

L445 proves cancellation of sign choices in raw squares and proves
regularity of w and m; it expressly leaves pY and complete first-mean
compatibility undecided. A selected vector may jump without the full
mean having a distributional defect. The later attempt must therefore
check the complete sum, including cancellation with both intermediate
terms and wm. It cannot assume a sign crossing exists, that a tie
is isolated, that a high contribution is nonzero at a switch, or that
one summand's jump survives. Changing isolated values on a null set
cannot provide a distributional obstruction. Proving full AC alone
would also leave the specified derivative identity to be tested.

## Duplicates, recorded failures and continuation decision

Reused assessments:
`drafts/literature/2026-10-20-all-temporal-x-second-occupation.md`,
`drafts/literature/2026-10-20-complete-x-second-weak-regularity.md`, and
`drafts/literature/2026-10-20-complete-x-second-integrated-xy-compatibility.md`.
Their ready scope concerns raw seconds, not the present signed mean.
Targeted local searches found only explicit unresolved mean statements,
not a duplicate proof of this target. The L445 singular-variation stop,
L446 unchanged-density endpoint stop, and L448 narrow-layer PSD stop
concern different complete quantities; none is a first-mean verdict.
Their ATTEMPTS records remain preserved. The width-one conditional
signed certificate and parked excursion application are not reopened.

External queries actually run were `"occupation measures" "first moments"
Liouville conditional mean derivative`, `"weak derivative" "absolutely
continuous" Hunter 3.63`, `"conditional first moments" "occupation
measures" Liouville`, and `"prescribed moments" "weak derivative"
occupation mean`. Search results did not furnish a matching law-specific
theorem or stronger automatic compatibility result. Adjacent stochastic
conditioning and control leads were not inspected and are unused.
The primary evidence is the cited passages, not search snippets.
No originality is inferred.

Continue with one mathematical attempt on the unchanged TARGET.
A rigorous complete-mean distributional defect on arbitrarily large
real-H intervals would stop this fixed-mean eventual extension. A proof
of the full identity on an eventual ray would remove only this necessary
constraint. If branch occurrence or cancellation cannot be controlled,
report that exact obstruction as incomplete; do not declare a failed
law or infer realization. A separate new target would need its own
review. A successful specialization is REPRODUCTION, with no claim of
progress beyond the checked general sources.

Essential continuation inputs are L421, L437, L438, L443, L445 and
L449, with L429's original stages. Actual crossings and L450's
monotonicity, x0^2>=cu and duration (22), the remaining PSD regions
and layers, other identities, actual/global realization, clipping,
capped nondegeneracy, L413's full-error margin and mixed positivity
remain unresolved. No cross-notebook input is used. Full matching
Mathlib coverage is unchecked, not absent.
