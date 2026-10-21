# CM coefficient-enclosure source comparison

TARGET: Assess whether L027's quadratic-coefficient enclosure extends to the CM curve y^2=x^3+1 at p=7 using L056's normalized table, separately from L004's non-CM rank implication.
CHECKED: 2026-10-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched "Mazur Tate Teitelbaum 1986 p adic analogues conjectures Birch Swinnerton Dyer pdf modular symbols measure", "ordinary p-adic L function CM elliptic curve modular symbols precision bound Stein Wuthrich" and exact MTT section/access queries; inspected Balakrishnan--Muller--Stein Section 2 and Stein--Wuthrich Section 3 statements and essential proof cases. Notebook-scoped searches found no prior CM enclosure approval and found the already recorded Banwait rank-two lead.
SOURCE_EVIDENCE: Balakrishnan--Muller--Stein, Math. Comp. 85 (2016), 983--1016, DOI 10.1090/mcom/3029, Section 2.1 pp.987--990 (including running c_A=1), Section 2.2 pp.991--993, Proposition 2.9 and complete proof pp.992--993, equations (2.4), (2.6)--(2.9); Stein--Wuthrich, Math. Comp. 82 (2013), Section 3 pp.1761--1766, Propositions 3.1/3.5, Lemma 3.2, Corollary 3.3 and their complete relevant proofs.
COMPARISON: Stein--Wuthrich's standing non-CM hypothesis prevents a direct citation for this curve; Balakrishnan--Muller--Stein Proposition 2.9 supplies general-newform convergence and explicitly the same coefficient bounds. L052 supplies the optimal degree-one identification and differential scale one required by the latter's running hypothesis. L028's existing orientation identity matches the primary plus-symbol definitions to L056 via S(r)=F({infinity,r}), not F({r,infinity}).
GAP: The fixed CM specialization has not been written as a canonical theorem or critically audited; no finite coefficient or nonvanishing has been computed. L004's non-CM arithmetic implication, lower vanishing, rational directions, Sha and complex-order comparison remain outside coverage.
REASON: Changed analytic hypotheses have primary coverage; a later proof may reuse L027's elementary precision bookkeeping with the general-newform input and the certified table, without re-proving measure construction or extending arithmetic rank theorems.
LITERATURE_REASON: The saved target changes L027's CM scope and requires essential source and orientation comparison; no repeated fixed-table audit was undertaken.
SCOPE: Fixed y^2=x^3+1, p=7, rational normalized level-36 weight-two trivial-character newform, total minimal real period, primitive untwisted trivial Teichmuller branch, kappa(gamma)=8, exact L056 full-relative functional and all-level denominator 12; future conditional enclosure at n>=2 with certified root residual precision M>=1.

The main gap remains rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2.
The intermediate target is a fixed CM analytic quadratic enclosure.
A later bounded coefficient test could separate analytic certification
from a rank implication. Uniform useful coefficient production, rational
directions and complex/p-adic comparison remain missing. Continue only
with matching primitive normalization and all-level denominators; abandon
a dependent application if an essential source hypothesis or exact
normalization fails. This turn performs source comparison only: no lemma,
coefficient, mathematical script or CM error-bound derivation is produced.

## Primary scope and strongest matching result

Jennifer S. Balakrishnan, J. Steffen Muller and William A. Stein,
*A p-adic analogue of the conjecture of Birch and Swinnerton-Dyer for
modular abelian varieties*,
[Math. Comp. 85 (2016), 983--1016](https://wstein.org/papers/mcom3029.pdf),
Section 2 treats newforms in S_2(Gamma_0(N)), a totally real coefficient
field and the associated optimal quotient A_f, without excluding CM.
The running assumption c_A=1 is explicit. Equation (2.4) fixes the
product of Shimura periods to the Neron period. Section 2.2 constructs
the ordinary unit-root measure, trivial branch and finite polynomials.
Proposition 2.9 gives coefficientwise convergence; its complete proof
explicitly carries over the coefficient bounds in Stein--Wuthrich's
Proposition 3.1 proof. Equation (2.9) keeps (1-alpha^(-1))^2.

The inspection included the hypotheses in Sections 2/2.1, period
Theorem 2.2 and Theorem 2.4 with its relevant proof, the running
hypothesis, exact plus-symbol formula, complete Proposition 2.9 and
its proof. It was not an abstract-only assessment. L050 supplies the
rational-coefficient newform; L052 supplies the origin-preserving
degree-one optimal identification and proved differential scale one,
meeting c_A=1. In dimension one (2.4) selects the total real minimal
period. CM of E does not make K_f a CM coefficient field: here K_f=Q.

## Error input and its qualifications

[Stein--Wuthrich, Section 3](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=5)
has a standing non-CM restriction from p.1761 onward. Read Proposition
3.1, Lemma 3.2 and its finite-character/Teichmuller-coset proof,
Corollary 3.3's monic-divisor proof, Proposition 3.5 and its complete
proof, and Lemma 3.6's denominator discussion. The general-newform
Proposition 2.9 above explicitly extends the same bounds; this is
coverage from a broader primary theorem, not permission to silently
remove the old source's hypothesis.

L027 already supplies the monic integral-division, uniform-denominator
closed-lattice tail and simple-root Hensel bookkeeping. Keep its
avoidance of the unrestricted integral-quotient assertion of Lemma 3.4
and the stronger two-level tail claim after Lemma 3.6. A later fixed
specialization may reuse that bookkeeping with the new convergence
input. No reproof of measure construction or any main conjecture is
needed or authorized. No actual finite coefficient is imported.

## Sign, period, denominator and ordinary eligibility

L056 defines F({a,b})=Re(2*pi*i integral_a^b f)/Omega(E).
Both primary plus formulas (Stein--Wuthrich p.1762 and the 2016 paper
p.991) use -pi*i times the sum of the r-to-infinity and -r-to-infinity
integrals divided by the plus period. L028's existing identity (5)
gives exactly S(r)=F({infinity,r}). Thus an implementation storing
{r,infinity} must negate that value. No new scale or factor two is
required. L050's one real component makes the least positive and total
real periods equal in this instance; the convention remains total.

L052's complete #E(F_7)=12 and good-reduction evidence supply the source
trace t=7+1-12=-4, prime to 7; no new count was run. L056 certifies
12F integral on the full relative module, including every rational
cusp path, so the denominator premise applies at all construction
levels and gives the future specialization's C=0 at seven. The later
proof must state these applicability checks and retain every
binomial(j,2) summand and certified root residual. No a_2, lower
vanishing or nonvanishing conclusion was obtained in this review.

## Duplicates, failed routes and unread leads

Reuse the 2026-10-06 assessments
`primitive-quadratic-coefficient-error-bounds`,
`quadratic-finite-error-specialization` and
`quadratic-enclosure-critical-audit` for unchanged bookkeeping.
ATTEMPTS/022 stops repeated conditional audits without symbols;
L056 now supplies that different missing input. The L050 rectangle
failure and L053/L054 workload stops remain preserved and are not
reopened. Earlier CM exclusions correctly describe L027 as stated.

The existing `2026-10-03-cyclotomic-kato-derivative.md` already
screened Banwait's CM rank-two lead. A bounded primary recheck of
[arXiv:2609.08431v1, 8 September 2026, Theorems A/B and Section 7.8](https://arxiv.org/html/2609.08431v1#S1.SS3)
confirms rational rank two, central vanishing and root number +1 as
premises. It is a different arithmetic criterion, not the rank-free
finite-polynomial input. Its proofs, constants and formalisation were
not audited and no theorem from it is imported.

MTT, Invent. Math. 84 (1986), I.10/I.13/I.14, remains an indirect
reference: EuDML returned 403 and Harvard scan endpoints were
inaccessible. No original MTT proof is claimed read. The published
generalization suffices, so these access failures are nonessential.
The 2016 paper's arithmetic results and Rubin's main conjecture were
not assessed for transfer to L004; no CM rank implication is approved.

## Continuation contract

Essential inputs: L027 (bookkeeping only), L028 (orientation identity),
audited L038 N=36 domain, L050, L051, L052 and audited L056. L004 and
foundations/05 define separate arithmetic scope. No cross-notebook
input. Full matching Mathlib coverage is not checked; Banwait's
conditional Lean statements are not a matching Mathlib theorem.

The separate `2026-10-13-cm-quadratic-enclosure-specialization.md`
assessment records the exact later proof target. Its newly saved ready
coverage receives separate supervisor approval next turn before
research. This is known-method source progress, not mathematics beyond
the checked sources or a BSD candidate. No independent gap is removed.
