# Low-height mollifier source review1443 (nomination1442)

TARGET: Assess primary Selberg--Delange coverage for |M(t)| >= c sqrt(L)/(log L)^(5/2), uniformly on |t| <= 1/5, for the original linearly tapered zeta^(-1/2) mollifier.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1443 searched complex/negative-exponent Selberg--Delange summatory theorems, the de la Breteche--Tenenbaum paper and tapered fractional mollifiers; checked the scoped November17/18 Jensen assessments and stops1407/1408/1431/1437. A primary untapered expansion was found; no inspected theorem directly states the requested tapered uniform bound. No novelty inference.
SOURCE_EVIDENCE: https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf author-corrected Remarks on the Selberg--Delange method, Acta Arith.200.4 (2021),349-369, DOI10.4064/aa201024-26-5: Theorem1.2/(1.2),(1.10)-(1.13) internal pp1-3; Section3.3/(3.8) p7; Section4.4/(4.5)-(4.9) pp10-12, and Section5.1 limitation statement p12. Read the complex-exponent expansion, coefficient formulas and relevant proof cases; https://dlmf.nist.gov/5.4.E6 and https://dlmf.nist.gov/5.5.E1 check the Gamma factor. Exact evidence and qualifications below.
COMPARISON: The source's tau_rho is the coefficient sequence of the Euler-product branch zeta(s)^rho; rho=-1/2 is permitted and its leading untapered coefficient is nonzero. Formula(3.8) supplies arbitrary fixed finite expansion order. The finite linear taper and uniform bounded-t weighting require a separate Abel-summation specialization; neither the proposed M bound nor an H_L lower bound is established here.
GAP: Prove the stated uniform lower bound from the inspected untapered expansion, keeping the original finite taper, endpoint and a relative error tending to zero. Only afterwards can it test H_L/q^6 with the original h; C020i still needs independent audit. No essential unread theorem is needed for the nominated specialization.
REASON: C020i exposed a fixed low-height contribution absent from the earlier high-height comparisons. This review resolves its newly essential negative-half-power source question and changes the continuation from source discovery to ordinary specialization; it does not revisit a ready target merely for balance.
SCOPE: Original alpha(n) from zeta(s)^(-1/2) on Re(s)>1, M(t)=sum_(n<=L) alpha(n) log(L/n)/log(L) n^(-1/2-it), L=floor(X^(1/1000)), h=3pi/log X, prescribed integer d. No continuation of a reciprocal Dirichlet series into the critical strip is requested or assumed.
LITERATURE_REASON: The target was REVIEW_REQUIRED at invocation; the negative-half-power summatory expansion was an essential unread input newly exposed by C020i, not additional browsing on a ready target.

## Original nomination1442 (historical rationale)

The following rationale records the state before review1443. Its source
questions are answered below; its mathematical lower bound remains unproved.

The completed, unaudited local specialization is canonical in C020i.
It proves E(Y0)>=c H_L/(Xq^4), with
H_L=integral_(-1/10)^(1/10) |M(t)M(t+h)|^4 dt. Thus the proposed
O(Bq^2/U^2) energy requires H_L=O(q^6). The translated sinc weight
does not vanish at these heights. Every prime pair, coefficient,
individual taper, shifted factor and frozen own heat time was retained.
This lower bound has not established a violation of the required scale.

The exact target above asks whether a known negative-half-power
summatory theorem can provide a uniform lower bound for the finite
mollifier after the original linear taper. Selberg--Delange is an
unread lead here, not a claimed applicable theorem. In particular,
negative z, the branch of zeta(s)^z, an error small relative to the
leading term, and bounded-height uniformity all need verification.
A result only for nonnegative coefficients or z>0 cannot silently be
substituted. A pointwise untapered asymptotic is not by itself the
requested uniform statement.

Read a primary theorem's hypotheses and the proof cases needed for
negative z before larger extracts. Compare the strongest inspected
conclusion with the exact displayed target, retaining the endpoint
n=L and the two occurrences of t+h in the eventual four-factor test.
Do not claim a nonzero leading term without checking its formula.
Keep any required partial-summation and uniform-error work as a future
research specialization rather than deriving and approving it here.
No new lemma or mathematical script is authorized in that literature
turn. If the essential theorem is unavailable, record that fact and
identify a bounded independent test; do not keep repeating access attempts.

Continuation test: coverage must permit a rigorously uniform lower
bound strong enough to test H_L/q^6. If it does, nominate only that
specialization and retain C020i's need for independent audit. If it
does not, state the exact missing hypothesis or error and keep the
energy question unresolved. A hypothetical lower bound for H_L would
stop only this sufficient Gallagher estimate, not the original norm.

At nomination1442 this target was REVIEW_REQUIRED. Review1443 below
supplies source coverage, but proves no target bound.
Full matching Mathlib coverage is unchecked. Motion, the full real
denominator, the signed numerator, E_P and actual-Xi transfer remain
independent gaps. No justified central creative mechanism follows yet;
the newly exposed source obligation must be resolved before claiming
an obstruction or proposing a replacement window.

## Completed primary-source comparison1443

Main gap: L030--L032/C032a actual-Xi all-degree positivity. The present
intermediate target tests one sufficient denominator-energy estimate;
motion, the full real denominator, signed numerator, E_P and Xi transfer
remain independent gaps. A successful low-height lower bound could
rule out the sufficient energy scale, conditional on C020i's later
audit. It would not reverse Gallagher's upper inequality or refute RH.

Queries included `Selberg Delange theorem complex z negative half
coefficients zeta power summatory Tenenbaum theorem pdf`, `de la Breteche
Tenenbaum remarks Selberg Delange method theorem 1.1 pdf`, and
`"Selberg Delange" "mollifier" "negative" taper`. The primary paper and
its publisher's DOI record were inspected. A search result or an
abstract was not used as the theorem. The November17/18 Jensen source
records contained no inspected Selberg--Delange input for this target;
the older unread shifted-Selberg-moment lead is a different theorem.
Stops1407/1408/1437 concern other sufficient budgets; exhausted1431
concerns an unpaid divisor-completion remainder. None proves or refutes
this low-height mollifier bound.

### Exact inspected input and its scope

R. de la Breteche and G. Tenenbaum, *Remarks on the Selberg--Delange
method*, Acta Arithmetica **200** (2021), no.4, 349--369,
[DOI](https://doi.org/10.4064/aa201024-26-5),
[author's corrected PDF](https://tenenb.perso.math.cnrs.fr/PPP/On-SD.pdf),
accessed 18 November 2026. The PDF explicitly includes minor corrections
to the published version and has 15 internally numbered pages. All page
numbers here refer to that version, not to journal page offsets. No
uninspected version is silently substituted.

Their Theorem1.2, internal p3, applies to a complex multiplicative f,
parameters A>0, r>0, rho in C and 0<sigma<1, J=ceil(A-1), under

\[
 \sum_{p\le x}(f(p)-\rho)\log p=O(x/(\log x)^A),\quad x\ge2,
\]
\[
 \sum_{v<p\le w}\frac{|f(p)|}{p}
 \le r\log\frac{\log w}{\log v}+O(1),\quad w>v>2,
\]
\[
 \sum_p\left(\frac{|f(p)|^2}{p^{2\sigma}}
       +\sum_{\nu\ge2}\frac{|f(p^\nu)|}{p^{\nu\sigma}}\right)<\infty.
\]

It gives (1.12)

\[
 \sum_{n\le x}f(n)
 =x(\log x)^{\rho-1}\sum_{j=0}^J
          \frac{\lambda_j(f)}{(\log x)^j}
 +O\left(\frac{x(\log_3 x)^\beta}{(\log x)^{A+1-r}}\right)
\]

for a suitable beta>0. Here log_3 is the third iterated logarithm;
use the error only for sufficiently large x. Formula(1.10) gives

\[
 \lambda_j(f)=\frac1{j!\Gamma(\rho-j)}
 \left.\frac{d^j}{ds^j}
       \left\{\frac{s^\rho F(1+s)}{1+s}\right\}\right|_{s=0+}.
\]

In particular the theorem does not require rho>0 or f>=0. The
nonnegative-only Theorem2.1 is not the applicable replacement.

For this notebook an even more direct input is Section3.3, internal
p7, formula(3.8). For fixed complex rho and the coefficients tau_rho
of zeta(s)^rho, with T_rho(x)=sum_(n<=x)tau_rho(n), it states

\[
 T_\rho(x)=x(\log x)^{\rho-1}
 \left\{\sum_{j=0}^{H}\frac{\nu_j}{(\log x)^j}
 +O\left(\frac{(bH+1)^{H+1}}{(\log x)^{H+1}}\right)\right\},
 \qquad x>2,
\]

with a suitable b, uniformly at least for H bounded by a constant
times (log x)^(1/3). Only fixed H is needed here. Formulas(1.9) and
(3.8) specify nu_j as the j-th Taylor coefficient of
{s zeta(1+s)}^rho/(1+s), divided by Gamma(rho-j). This is the
classical Selberg--Delange expansion, explicitly attributed in the
primary paper to G. Tenenbaum, *Introduction to analytic and
probabilistic number theory*, third edition, Graduate Studies in
Mathematics163, AMS2015, TheoremII.5.2. That book's full proof was not
retrieved; the displayed expansion itself and its use in the inspected
primary proof were read. No claim to have audited the book is made.
The independently stated Theorem1.2 is an alternative citation after
its arithmetic hypotheses are verified; it is not necessary to invoke
a short-interval prime theorem from Theorem1.1.

The local alpha is precisely this paper's tau_(-1/2), with the
Euler-product branch normalized on real s>1. The coefficient problem
does not require extending a reciprocal Dirichlet series to Re(s)=1/2.
At the local pole removal, the analytic power of s zeta(1+s) is
normalized to 1 at s=0, as in the paper's Taylor-coefficient formula.
This identifies the branch used in the summatory expansion; the future
specialization must retain it. The source coefficient nu_0 is
1/Gamma(rho). At rho=-1/2 it is finite and nonzero: this is the
standard half-integer Gamma value checked against
[DLMF5.4.6](https://dlmf.nist.gov/5.4.E6) and the
[recurrence5.5.1](https://dlmf.nist.gov/5.5.E1). The source's warning
after(1.10) concerns nonpositive *integer* rho, not -1/2.
No tapered leading coefficient is calculated in this review.

### Proof cases and limitations actually read

The complex-rho setup in Section1 and Section3.3's expansion and
signed-convolution completion were read, including the explicit
max(0,Re rho) error dependence. Section4.4, internal pp10--12,
uses (3.8) in (4.5)--(4.7), bounds the remainder after taking fixed
expansion orders sufficiently large, then treats the signed
hyperbola terms in (4.9). These steps do not replace f by a positive
function in the main term and do not restrict rho to positive values.
The final iteration improves a power of log_2 x to one of log_3 x;
this improvement is not essential when using (3.8) directly.
The Section5.1 limitation statement was also read: one may not replace
max(0,Re rho) by Re rho in the general Theorem1.1 error. Its whole
counterexample proof was not audited and is not a local premise.
No sharper general error for negative rho is asserted here.

This resolves coverage for the *untapered* negative-half-power input,
including arbitrarily many fixed logarithmic terms. The exact target
has an additional finite weight n^(-1/2-it) log(L/n)/log L. The paper
does not state its uniform bounded-t asymptotic. Abel summation and
a uniform endpoint estimate are the identified difference; they must
be written in a research turn, not supplied as a hidden theorem here.
They should use the untwisted summatory expansion and then weight it;
one must not assume the twisted coefficients satisfy the same
prime-mean hypothesis with constant rho.

### Discriminating continuation

Nominate one ordinary specialization: derive the displayed uniform
lower bound for the unchanged finite M on |t|<=1/5. Keep its t-dependent
main term and prove an error uniformly smaller than its modulus;
retain the n=L endpoint and the small-n contribution. Failure to
obtain a nonzero uniform main term or a relative o(1) error leaves
the target unproved and requires a precise recorded obstruction.
No altered taper or unproved critical-strip continuation is allowed.

If the bound is later proved, the original h tends to zero, so the
shifts occurring in C020i can be checked within this same compact
t-range. Applying that result to H_L and comparing with q^6 is a
subsequent mathematical use, not a conclusion of this review.
C020i's independent audit must precede any retained stop of the
Gallagher estimate. No new lemma, proof or mathematical script was
written in1443. Full matching Mathlib coverage remains unchecked;
the classical theorem is cited rather than reproved. The newly saved
ready continuation receives a separate supervisor approval next turn.
