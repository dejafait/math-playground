# Actual-theta cubic: finite-free square-root source gate

TARGET: Assess source coverage for a real-rooted finite-free additive convolution square root of the centered monic actual-theta P_3, specifying the coefficient test before authorizing a calculation.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step620 searched finite free additive convolution polynomial convolution roots divisibility cubic; finite free convolution real rooted square root polynomial cubic cumulants; finite free cubic divisibility; finite free square root cubic; finite free fractional powers polynomial real rooted; finite free cubic discriminant. Narrow local searches found only this exact nomination; prior LP/Appell, multiplicative and inverse stops were compared and retained.
SOURCE_EVIDENCE: Inspected Marcus–Spielman–Srivastava arXiv:1504.00350v2 Definition1.1/(1)–(2), Theorems1.2–1.3 pp.2–3; Arizmendi–Perales arXiv:1611.06598v2 Proposition3.4/(3.2)–(3.3), Proposition3.6 and full proofs pp.7–8, Section6 pp.15–17; Marcus arXiv:2108.07054v1 Lemma6.4 and proof pp.33–34; Campbell v3 Definition1.12/(1.15)–(1.18); Dickson First Course in the Theory of Equations ChapterIV Sections44–45 pp.53–54, formulas and all root-sign cases; DLMF1.11(iii)/(1.11.12).
COMPARISON: Known coefficient/cumulant inversion supplies a formal finite-degree construction, and the classical cubic discriminant decides its real-rootedness; Walsh preservation applies only after that test passes. Neither LP input, multiplicative preservation nor large-power/infinite-divisibility results supply the actual square-root sign. No actual factor or discriminant has been computed in this literature turn.
GAP: Specialize the finite construction to centered monic L795 P_3, prove the precise convolution identity and uniqueness, then enclose the factor discriminant using audited L791 coefficient inputs; the actual sign remains untested.
REASON: Essential source coverage is now sufficient for one bounded known-method specialization; no new theorem is needed or claimed. A fresh continuation assessment records the actual calculation for separate approval.
SCOPE: Degree3, real monic factors, symmetric additive convolution at fixed d=3, multiplicities allowed. L019/L021/L795 define the actual law; L791 supplies audited numerical coefficients under its inherited L778 analytic/software contracts. No new quadrature, higher degree, arbitrary convolution powers or automatic LP import. Mathlib coverage unchecked.

## Purpose, comparison and bounded decision test

The following nomination is retained as the pre-review record. Its
pending-review language is superseded by the completed step620 review
below; it is not an instruction to repeat the search.

The main gap remains actual-Xi all-degree mixed positivity. A real-rooted
factor whose finite-free additive self-convolution is the actual centered
monic cubic could give an independently checked finite realization. Its
plausible downstream use is to ask whether analogous coefficient-built
factors have a degree-uniform positive realization. Neither that extension
nor shifted/mixed transfer follows from a cubic certificate. The cubic's
real-rootedness is already known; reproducing it alone is not the target
or a new result beyond the literature.

Three mechanisms were compared for routing, without new mathematics:

1. Restrict the inverse from L822. No independently specified input class
   with sufficient oscillation transfer is available. The audited fixed-square
   stop remains in `ATTEMPTS/2026-11-05-theta-universal-inverse-variation-stop.md`.
2. Close the theta-averaged Laguerre adjoint. The completed
   `2026-11-05-theta-laguerre-adjoint-comparison-scope.md` retains the unpaid
   forcing, boundary and signed-margin estimates. No changed equation or
   independently paid residual is supplied; do not reopen that source stop.
3. Construct one finite-free additive convolution factor directly from
   actual coefficients. This changes both the operator and realization
   premise. Unlike common Favard orthogonality it asks for no common
   positive measure across degrees; unlike an LP representation it must
   build and test the factor before using root preservation. Select this
   narrowly stated source question, not a presumption that a factor exists.

The review must search the exact statement, standard finite-free additive
divisibility terminology, stronger results and obstructions. Read primary
definitions, theorem hypotheses and relevant proof cases before deciding
IMPORT, SPECIALIZE or EXPLORE. In particular distinguish additive from
multiplicative convolution and finite-degree roots from classical free
infinite divisibility. Check the normalization, translations, monicity,
degree, multiplicities and real coefficients. A real-rootedness-preserving
operation is useful only after its factor hypotheses are verified.

Continue to a separately gated mathematical test only if the review supplies
a finite coefficient construction or necessary-and-sufficient cubic
criterion with a discriminating real-rootedness threshold, plus the exact
convolution preservation theorem. Then one bounded actual-law test can
accept or reject this factor construction. If the source criterion already
assumes the actual polynomial's desired roots without giving an independent
factor certificate, or reduces to an exhausted universal-preserver premise,
park the mechanism. Absence of a located theorem proves neither novelty
nor impossibility. No factor, discriminant inequality or new identity has
been derived in this nomination.

Essential local inputs are L019/L021/L795. L822 and L796 are route contrasts,
not mathematical premises of a factor-existence assertion. A later numerical
test would need separately assessed coefficient enclosures and their complete
analytic contracts; none is assumed or requested by this source question.
Unresolved assumptions include factor existence and hyperbolicity, any
degree-uniform extension, and all shifted/mixed sufficient-sign transfer.
No cross-notebook input. This new continuation needs separate approval;
it does not revoke the completed L822 audit. It is not yet a justified
creative proof attempt: the independent factor criterion is the missing
input, and finite cubic specialization would itself be reproduction.

## Completed source comparison — 5 November 2026, step620

SPECIALIZE approves a later finite calculation, not the truth of the
actual factor assertion. The coefficient test is the constructed cubic's
discriminant against zero. No specialized factor, new identity, numerical
evaluation or mathematical script was produced in this literature turn.

### Operation and preservation hypotheses

Marcus, Spielman and Srivastava, *Finite free convolutions of polynomials*,
[arXiv:1504.00350v2](https://arxiv.org/pdf/1504.00350v2), 3 July 2019,
printed pp.2–3, Definition1.1/(1)–(2), Theorems1.2–1.3:
for degree-at-most-d polynomials
\(p(x)=\sum_{i=0}^d(-1)^i a_i x^{d-i}\) and
\(q(x)=\sum_{i=0}^d(-1)^i b_i x^{d-i}\),

\[
 (p\boxplus_d q)(x)=\sum_{k=0}^d(-1)^k x^{d-k}
 \sum_{i+j=k}\frac{(d-i)!(d-j)!}{d!(d-k)!}a_i b_j.
\]

The differential form is \(\widehat p(D)\widehat q(D)x^d\), where
\(\widehat p(D)x^d=p\). Translation commutes with convolution in
either argument; the identity is \(x^d\). Theorem1.2 uses normal
d-by-d matrices and Haar unitary averaging. Walsh's Theorem1.3 requires
both inputs real-rooted of degree d, and preserves real-rootedness;
positive roots and simplicity are not required. These are forward
statements, not convolution-root existence assertions. Fix d=3; ordinary
multiplication, asymmetric addition and multiplicative convolution are
different operations. The inspected differential identity suffices for
the proposed algebraic construction; no preservation theorem is reproved.

### Inversion and fractional-power scope

Arizmendi and Perales, *Cumulants for finite free convolution*,
[arXiv:1611.06598v2](https://arxiv.org/pdf/1611.06598v2), 7 March 2017,
printed pp.7–8: Proposition3.4/(3.2)–(3.3) gives coefficient/cumulant
inversion through degree d; Proposition3.6 and Corollary3.7 give
additivity for monic degree-d inputs. Their full proofs use finite
partition identities, not a positive root law. This supplies the
algorithm for the planned halved-cumulant test. Section6, pp.15–17,
defines fractional powers and real-rooted infinite divisibility;
Remark6.7 records a degree-four non-preservation example. Theorem6.5
concerns normalized infinite divisibility, not one square root. Its
displayed proof uses fourth cumulants; it is not a cubic obstruction
input here. Proposition6.6 is eventual in large powers; its proof first
normalizes the second cumulant to one. Do not import its broad wording
for arbitrary real polynomials without that hypothesis. Neither result
settles t=1/2. The power definition also prints an apparent extra t on
the left; use Proposition3.6 and coefficient equations directly. No
source counterexample is reverified or used as a local theorem.

Marcus, *Polynomial convolutions and (finite) free probability*,
[arXiv:2108.07054v1](https://arxiv.org/pdf/2108.07054v1), 16 August 2021,
Lemma6.4 and proof, pp.33–34, reconstructs the polynomial through a
differential/logarithmic-derivative formula up to scalar. Campbell,
[arXiv:2412.20488v3](https://arxiv.org/html/2412.20488v3), Definition1.12,
(1.15)–(1.18), treats that logarithmic derivative formally and flags
Marcus's truncation: retain terms modulo s^d. Fix monicity and use finite
coefficient equations to avoid scalar or truncation ambiguities.

Reuse the LP/Appell comparison in
[step385](2026-11-04-actual-jensen-mechanism-discovery.md) and the
multiplicative comparison in
[step597](2026-11-05-degree-dependent-central-jacobi-feasibility.md).
Their positivity premises remain unpaid here. The searches recorded above
found no inspected theorem certifying this specific actual square root.
This is not a novelty claim; no desired spectrum is presumed realized.

### Coefficient threshold, including equality

L. E. Dickson, *First Course in the Theory of Equations* (1922),
ChapterIV, Sections44–45, printed pp.53–54,
[PDF pages63–64](https://www.gutenberg.org/files/29785/29785-pdf.pdf),
equations(11)–(12) and the complete root-sign proof, supplies the test.
For a real monic cubic \(q(x)=x^3+b x^2+c x+e\),

\[
 \Delta(q)=18bce-4b^3e+b^2c^2-4c^3-27e^2.
\]

Positive discriminant means three distinct real roots; negative means
one real root and a nonreal conjugate pair; zero means all roots real
with repetition. Equality is accepted for hyperbolicity, not simplicity.
The inspected proof handles the repeated-root case explicitly. NIST DLMF
[1.11(iii), (1.11.12)](https://dlmf.nist.gov/1.11#iii) also gives the monic
depression convention and depressed discriminant. Apply these general
formulas later; no actual centered coefficients or factor discriminant
have been derived here.

### Input reuse and bounded continuation

Read L795's definition and the needed L019/L021 statements/proofs: moments
through m_3 are real, positive and finite. These supply a nonzero leading
coefficient, not a factor root law. Use L791's **actual coefficient** input
only. Its proof and step478 audit certify full outward enclosures under
L778's uniform complex-disk analytic error and documented software
contracts. The audit verifies
\(\gamma(j)=j!M_{2j}/(2j)!=8\,4^j j!a_j\), including analytic coefficient
error addition. No common Favard measure, model-root conclusion or
index-five residual is needed.

Relevant complete evidence is `actual_a`/`gamma` in
`scripts/central-jacobi/fixed-model-certificate-476.json`, with the input
audit at `scripts/central-jacobi/audit-478/audit-report.json`. This review
checked the canonical input contract, not those JSON values; the later
calculation must inspect every load-bearing interval and audit evidence
with the bounded inspector. A preview or printed midpoint is insufficient.
If inherited evidence does not support these inputs, record the blocker;
no replacement quadrature is authorized here.

The calculation must verify monic centering, construct a real monic q,
prove its exact self-convolution identity and uniqueness, then certify
the full discriminant sign using outward intervals. A positive lower
bound continues this finite realization. A negative upper bound abandons
this mechanism at degree three, only after uniqueness is established.
A straddling interval is INCONCLUSIVE unless exact equality is proved;
no sweep or automatic refinement is licensed. Even success leaves
degree-uniform extension and shifted/mixed transfer to the main gap open.

Full matching Mathlib coverage is unchecked. This is source progress for
known methods, not a new theorem beyond the checked sources. Direct shell
download failed at DNS resolution; primary statements and relevant proofs
were accessible through the web tool, so essential coverage is not blocked.
No lemma, mathematical script, DAG or PROOF was changed. The fresh
calculation nomination needs separate next-turn approval; that does not
undo this completed review.
