# Logarithmic Hankel Schur complement — completed covariance comparison

TARGET: Assess whether theta-integral covariance inequalities can control the one-step Schur complement of L030's logarithmic-coefficient Hankel matrices, and identify one independently checkable sufficient bound or the exact interface obstruction.
CHECKED: 2026-11-07
DECISION: IMPORT
SEARCH_EVIDENCE: Step95 searched asymmetric Brascamp-Lieb covariance and Riemann theta cumulant/Turan terminology; read the primary statements and relevant proof cases below. Reused the signed-Schur, connected-partition and contact-score comparisons and L044/L057 stops; no exhaustive-search or novelty claim.
SOURCE_EVIDENCE: Carlen-Cordero-Erausquin-Lieb, AIHP49(2013)1-12, Theorem1.1/(1.3)-(1.6) and Section2 pp2-5; Cordero-Erausquin-Livshyts-Rotem arXiv:2610.34289v1, Proposition3.1/full proof p12; Csordas Glasnik33(1998)37-50, Theorem2.2, Corollary2.11/full proof pp39,43 and normalization (1.2). Precise URLs and applicability below; Gallier Schur algebra and cumulant source coverage reused.
COMPARISON: Absolute covariance and even-function variance bounds concern expectations under a positive density, not L030's logarithmic coefficient functional. None identifies its Schur vector/inverse quadratic term with a controlled covariance or compares that term to S_(2d+2). Even granting curvature and integrability does not supply this interface; raw Gram positivity and conditional node certificates are insufficient.
GAP: A root-free actual-theta representation and quantitative inequality for the logarithmic Schur remainder are still absent. Base positivity, singular-block range conditions, uniform degree control and boundary/weighted-integrability checks remain independent obligations. No new inequality or counterexample is established here.
REASON: Import only the inspected known theorem scopes; park automatic covariance-to-logarithm transfer after this negative applicability comparison. A new independent signed interface is needed to reopen it. Reuse existing ready coverage for the first L876 coefficient-exclusion audit; do not invent creative mathematics to fill scheduling preferences.
LITERATURE_REASON: The observable changes from indexed zero enclosures to a root-free theta-to-logarithmic-Hankel inequality; no ready assessment covers that bridge. This is essential new coverage, not extra browsing on L836.
SCOPE: Completed literature-only comparison of at most three candidate interfaces: absolute BL covariance, strengthened even variance, and ready cumulant lifting. IMPORT covers their source scopes only, not a new Schur estimate, actual-Xi sign, lemma, script, induction or creative proof approval.

## Completed comparison — step95

The main gap is L030-L032/C032a: actual-Xi mixed positivity in all
degrees. The intermediate target was an independently justified bound
for a one-step logarithmic Hankel extension. A successful bound could
support induction with a separately proved positive lower block; it
would still owe the base, singular cases and all-degree applicability.
The source-level continuation test fails: no inspected theorem supplies
that bound or a specified actual-theta representation to which it applies.
This is a source-scope negative, not a theorem that the remainder is
negative or that every covariance mechanism fails.

### Exact observable and reused algebra

Reuse Gallier, *The Schur Complement and Symmetric Positive Semidefinite
(and Definite) Matrices*, 24 August 2019, Propositions2.1-2.2, pp3-4,
[author PDF](https://www.cis.upenn.edu/~jean/schur-comp.pdf), as already
read in `2026-11-04-signed-schur-coercivity-discovery.md`. Here L030's
matrix is real symmetric, so the adjoint mismatch of the earlier residue
matrix is absent. For d>=1, its lower-degree block is A=H_(d-1), its
last-column vector is b_i=S_(i+d+2), 0<=i<d, and its last diagonal
entry is s=S_(2d+2). With A positive definite, the standard theorem
requires s-b^t A^(-1)b>=0 for a positive semidefinite extension.
This is an applicability statement of the cited theorem, not a bound.
The singular case is not imported or replaced by an unchecked inverse.

L025 already exhibits the nonlinear interface:
S_2=(3M_2^2-M_0 M_4)/(12M_0^2). L021's raw Cauchy-Schwarz bound has
the opposite direction to the upper moment bound needed even there.
No new recurrence, determinant or cumulant calculation was made.
L032 and L895 detect negativity conditional on nonreal node data;
neither is an independently positive input for A, b or s.

### Primary sources and hypotheses

**Absolute covariance.** E. A. Carlen, D. Cordero-Erausquin and E. H.
Lieb, *Asymmetric covariance estimates of Brascamp-Lieb type and related
inequalities for log-concave measures*, AIHP Probab.Stat.49(2013),1-12,
DOI10.1214/11-AIHP462,
[author-hosted published PDF](https://webusers.imj-prg.fr/~dario.cordero/Docs/articles/Carlen_CE_Lieb_IHP.pdf).
Read Theorem1.1, (1.3)-(1.6), and Section2's proof, pp2-5. The density
is exp(-V) on R^n, normalized, with V C^2 and everywhere positive
Hessian. Tests are locally Lipschitz and square integrable. At n=1,p=2:

    |Cov(g,h)|^2 <= (integral g'^2/V'' dmu)(integral h'^2/V'' dmu).

The general theorem covers 2<=p<=infinity with conjugate exponent and
inverse-Hessian weights. Its proof solves Lu=h for a centered test,
uses integration by parts and Holder, regularizes by epsilon|x|^2,
then removes regularization; infinity is a limit case. These operations
give an absolute estimate, without a sign or a logarithmic-Hankel
identification. Finite raw moments do not certify weighted derivative
integrability. The exact theta Schur vector b is not identified with
the theorem's covariance tests.

**Even-function improvement.** D. Cordero-Erausquin, G. V. Livshyts
and L. Rotem, *Remarks on the Brascamp-Lieb inequality*,
[arXiv:2610.34289v1](https://arxiv.org/pdf/2610.34289v1),25 October2026,
Proposition3.1, printed p12, statement and full proof. If V is even,
C^2, and Hess V>=cI for a fixed c>0, the normalized exp(-V) law obeys,
for smooth even f,

    Var(f) <= integral <(Hess V+cI)^(-1) grad f, grad f> dmu.

The proof first reduces to compact support and zero mean; the Poisson
solution is even, its derivatives odd and centered, and the usual BL
inequality plus Bochner and Cauchy-Schwarz prove the claim. This retains
a positive uniform curvature hypothesis. It strengthens a variance
upper bound but gives no representation of s-b^t A^(-1)b. Neither a
usable actual-theta c nor the inverse-block comparison is established
here. The whole preprint is not audited or imported.

**Actual-kernel scope.** G. Csordas, *Convexity and the Riemann
xi-function*, Glasnik Matematicki33(53)(1998),37-50,
[journal PDF](https://web.math.pmf.unizg.hr/glasnik/33.1/33105.pdf).
Read (1.2), Theorem2.2, and Corollary2.11 with its proof, printed
pp37,39,43. The cited square-coordinate strict log-concavity yields
strict potential curvature for t>0; the proof establishes full-line
convexity using smooth evenness. The established normalization
K(u)=4Phi(u/2) is reused from the Nuttall assessment; probability
normalization removes the multiplier. No uniform positive curvature
constant, endpoint inverse-curvature estimate or logarithmic-Hankel
positivity is stated in these passages. Earlier original 1988 and
Newman1991 proofs were not newly read. Their access is unnecessary for
this narrower interface obstruction: even granting all curvature
premises does not identify the required logarithmic form.

Screenshot requests for these theorem pages returned no inspectable
images in this interface. Text extraction supplied the theorem
hypotheses and complete relevant proofs; no disputed OCR formula is
used for a sign computation or a new mathematical import.

### Third candidate, duplicates and limits

Reuse `2026-11-06-theta-connected-partition-interface.md` for the exact
Leonov-Shiryaev/Burchardt identities and Zhu's shifted-cumulant moment
premise. That reviewed route cannot turn positive ordinary theta
moments into positive logarithmic Hankel forms without a further sign
input. No re-search, new identity or original-source reproof is needed.
Reuse `2026-11-06-actual-theta-contact-score-pairing.md` for the distinct
Stein/GHS test-class mismatch; it does not supply a Schur bound either.
These are comparisons, not sign premises.

Read complete L044 and L057 and the September9/September20 failure
records. L044 disproves generic Gram-to-log preservation. L057 permits
any fixed number of positive logarithmic Hankel tests alongside its
strict square-coordinate log-concavity and nonreal zeros. Neither
comparison law is asserted to obey every arithmetic theta identity;
neither proves failure of a future inequality using that full law.
No new generic example or finite actual sign computation is warranted.

Thus the exact unpaid interface is a specified family of admissible
tests/weights, together with a theorem relating their covariance or
energy to b and s, strong enough to compare b^t A^(-1)b with s under
an independently justified lower-block premise. Merely naming the
Schur inequality assumes the sought extension; merely bounding an
unrelated raw covariance leaves it untouched. No all-degree sign
premise, zero location or singular-block hypothesis was inserted.

### Decision and continuation

Park this automatic transfer. Reopen only with an explicit actual-law
identity or estimate and an independently discriminating bounded test;
a new label, stronger generic variance constant or repeat of a finite
positive determinant is insufficient. This review supplies no such
creative target. The blocker is the missing logarithmic observable
representation, not a quota or a global ban on theta research.

The ready, independently testable continuation is the existing first
L876 audit in `2026-11-06-l876-coefficient-stop-audit.md` (SPECIALIZE),
whose exact target and scope are unchanged. Its operator sources and
the step23 production coverage are reused; no new assessment is written.
Audit the full-half-line certificate and strict residual, not another
coefficient campaign or a fitted replacement operator. Essential inputs
are L019/L021/L025 and L876, with narrow L016/L024 reads only if needed.
An independently valid nonzero residual retains that fixed-ansatz stop;
a defect requires correction, and an enclosure containing zero leaves
the exclusion unresolved. This audits route evidence, not RH.

No lemma, mathematical script, DAG or PROOF edit was made in step95.
Outcome NEGATIVE records a new primary-source scope comparison, not
new mathematics beyond the sources checked. Full matching Mathlib
coverage and supporting covariance/Schur coverage were not checked;
no library absence is asserted. Current routing lives in PROGRESS.md.

## Original nomination — preserved; source status superseded above

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is an independently supported sufficient
one-step estimate, with a separately verified positive lower block as
an explicit induction hypothesis. Its plausible use is an induction
mechanism for logarithmic Hankel positivity; it would still owe a
base, degeneracy cases, all degrees and actual-theta applicability.
No induction is asserted. In particular, a source merely restating
the Schur positivity criterion has not supplied the required estimate.

Continuation inputs: L019/L021 for actual theta integrals and moment
normalization, L025 for logarithmic power sums, L030/L032 for the
exact target. L057's finite-test obstruction and L895's conditional
node-data certificate are safeguards, not hypotheses giving signs.
Resolve their exact needed statements before detailed source work.
The indexed endpoints, L836 contour bound and PF-order enlargement
are not mathematical inputs to this proposed mechanism.

First compare known covariance inequalities and logarithmic/cumulant
moment identities with the required coefficient space. Assess at
most three source-supported candidates; a Brascamp–Lieb-type estimate
is only an unread terminology lead, not a theorem imported here.
Search narrowly for duplicates and relevant recorded theta/logarithm
failures. Reuse ordinary Schur algebra if its assumptions match; do
not reprove it or infer a positive logarithmic form from raw moments.

Continue only if inspected primary hypotheses give a concrete,
noncircular bound on the actual Schur remainder, or identify a bounded
model/actual-theta test with all parameters and a discriminating sign.
If covariance controls only raw moment Gram forms, or the transfer
requires the desired logarithmic positivity itself, record that exact
obstruction and park this mechanism. Do not rename an RH-equivalent
criterion as a covariance estimate or expand to an automatic degree
campaign. A genuinely new central proof attempt would need that
bounded test and a separately approved assessment before creative
routing is justified. Mathlib matching coverage is unchecked.
