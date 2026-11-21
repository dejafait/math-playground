# Simultaneous boundary control and spectral approximation — source comparison

TARGET: Review simultaneous unit-circle control and two-window polynomial approximation for C997s's original coefficient cap and exp(-n/64) residual target.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step401 searched bounded analytic approximation on circle arcs, constrained polynomial extremal problems, outer-function lower certificates and coefficient-constrained superoscillations; inspected Baratchart-Leblond-Seyfert Sections3-5/Theorems1-3 and Alpay-Colombo-Sabadini Theorems2.2/3.3. Reused reviews381/387/390 and the scalar393/exact398/spectral-tail341 stops. Exact queries, inspected cases and unused leads follow below.
SOURCE_EVIDENCE: L. Baratchart, J. Leblond, F. Seyfert, Constrained L2-approximation by polynomials on subsets of the circle, author manuscript22 March2017, Sections3-5, equations(2)-(7),(13)-(15), Theorems1-3/statements and selected proof cases, printed pp2-10, https://www-sop.inria.fr/members/Juliette.Leblond/Papiers/BLSFields2017.pdf ; D. Alpay, F. Colombo, I. Sabadini, JFAA27,28(2021), Theorems2.2/3.3, https://doi.org/10.1007/s00041-020-09808-9 . C997c/s and prior primary comparisons are reused.
COMPARISON: Constrained polynomial approximation on arcs is already a known problem; the inspected convergence theorem has fixed data, an L2 objective and a complementary-circle modulus bound, without the needed coupled exponential rate or monomial cap. Hardy Cauchy/outer-function formulas support a different boundary-annihilator test. Prescribed jets, exact moment representation and scalar slope propagation are not imposed by that test.
GAP: No source supplies the original capped Delta_n bound or its impossibility. A later boundary-annihilator attempt must pay complementary-circle leakage and obtain a noncancelling target pairing at a decisive rate. Neither estimate, a coefficient-norm conversion, a new E_n bound nor an RH input is derived here. Full matching Mathlib coverage is unchecked.
REASON: The bounded comparison identifies a concrete outer-function dual family for a later test, rather than another qualitative approximation citation or another stopped interpolant. Tool coverage permits exploration only; the newly written continuation401 requires separate next-turn approval. This literature turn establishes no new mathematical bound or originality.
LITERATURE_REASON: Changed hypothesis is simultaneous original coefficient-cap control for an arbitrary polynomial, absent from review381's uncapped problem and review387's prescribed-jet problem; review390 left this candidate without a concrete method. Assess boundary-controlled approximation tools rather than repeating finite-energy superoscillation comparisons.
SCOPE: Completed source review only for the precise prospective sufficient objective below. No new lemma, mathematical script, cap conversion, contour estimate or rate derivation was performed; the original nomination below and its stop test are preserved.

## Exact prospective test and downstream purpose

For integer n>=64 retain C997s's original I, gamma_j, z_star, complete
kernel and B_n=exp(sqrt(n)). Consider arbitrary complex polynomials

    p_n(y)=sum_(j=0)^n A_(j,n)y^j,
    sum_(j=0)^n |A_(j,n)|<=exp(sqrt(n)),
    e_n(t)=exp(i z_star t)-exp(15it/8)p_n(exp(it/(4n))).

Let U_n=[7n/4,9(n+2)/4] and L_n=[n,n+2]. Using exactly the positive
upper-density bounds T_U,T_L of C997c(5), set the proposed objective

    Delta_n(p_n)=T_U sup_(t in U_n)|e_n(t)|
                  +T_L sup_(t in L_n)|e_n(t)|.

The prospective success threshold is a single finite C, independent of
n, with Delta_n(p_n)<=C exp(-n/64) for all sufficiently large n,
while paying the original coefficient cap. C997c's existing complete
window contract explains its downstream use as a sufficient upper
certificate for C997s's integrated residual. No converse is asserted.
Both windows, all closed endpoints, both beta terms and the subtraction
in K remain in that contract. No pointwise lower bound is substituted
for an integrated-residual lower bound.

The precise source question is whether quantitative polynomial
approximation with simultaneous boundary norm control can construct
such p_n, or rigorously rule out this sufficient objective for all such
p_n. The original sum of coefficient moduli remains the constraint;
any proposed replacement by a circle supremum or Hardy norm requires
an explicit, paid conversion. No such conversion is derived here.
The varying complex-power target and arcs cannot be replaced by fixed
data without a uniform estimate. Do not assume interpolation jets.

## Source review boundary and stop test

Reuse review381's inspected Sete-Liesen Theorem2.3, Charpentier-Levenberg-
Wielonsky Theorem2.4 and Christiansen-Eichinger-Rubin-Zinchenko
Theorem4.1 hypothesis mismatches. Reuse review390's Ferreira-Kempf
finite-energy/atomic-cap mismatch. These are comparisons, not missing
proofs to reread by default. Search specifically for simultaneous
boundary-controlled analytic/polynomial approximation with a varying
exponential target and coefficient growth constraints. Read primary
statements and essential proof cases for any promising new method.
Do not infer originality from absence of a match.

Continue only if this bounded review identifies a concrete method and
states which remaining quantitative estimate a later mathematical
attempt would test. A genuine construction meeting the above threshold,
or a universal obstruction to that objective, would discriminate it.
An inadequate upper envelope or a failed individual approximant would
not settle the all-polynomial question. If no usable method is found,
record that evidence and choose a different independently testable
target; do not restart the stopped centered Taylor or prescribed-jet
families under new names.

C997c and C997s are the essential prospective inputs. C997r/v/w/x/y/z
are scope comparisons; no new dependency is asserted. The capped
integrated E_n, C997a(8), selected/both-sign transfer, assay/reconstruction,
complements/regulators, L993, L984(H), L966/L968 forcing and actual-Xi
positivity remain unresolved. No cross-notebook input is proposed.
Full matching Mathlib coverage is unknown and unchecked.

The exact next task is literature_comparison, not a proof attempt.
If a genuinely new central mechanism emerges with adequate coverage,
nominate its bounded proof_attempt/creative test and precise escalation
then. This nomination does not manufacture that justification from the
number of turns since the last creative attempt.

## Completed literature-only comparison — step401, 11 November 2026

The last paragraph above describes the nomination at invocation start.
This section completes that source review. It does not carry out or
self-approve the newly nominated mathematical continuation.

### Primary contracts and inspected proof cases

**Baratchart–Leblond–Seyfert**, author manuscript cited in SOURCE_EVIDENCE,
Section3, printed pp2-4, (2)-(7), gives Hardy boundary/Cauchy formulas
and the Riesz–Herglotz transform of real integrable boundary data.
Its exponential outer construction has prescribed positive boundary
modulus rho when log(rho) is integrable; membership in H^p requires
rho in L^p. Section4 treats fixed L2 data on finitely many open circle
arcs, with complementary-circle interior and modulus constraint.
Theorems1-3, pp5-10, give uniqueness, finite critical-point conditions
and fixed-data convergence, without a quantitative degree rate.
Read their statements, Theorem2's finite separation proof, Theorem1's
indicator-set outer perturbation (15), and Theorem3's complete proof:
endpoint modification, radial
dilation and eventual Taylor truncation. The truncation degree is chosen
after the tolerance and data; it is not a uniform degree-n certificate.
Only the standard Cauchy/outer tools are prospective inputs. This source
does not pay our varying target, sup error or coefficient cap.

**Alpay–Colombo–Sabadini**, cited article, Theorem2.2 and Remark2.3,
gives convergence of its binomial superoscillating sequence for fixed
complex a in an exponential-type entire-function space, hence on fixed
compact sets. Theorem3.3 treats a fixed entire function with coefficients
bounded by C b^u/u!; read its proof through continuity of the stated
infinite-order differential operator. Neither statement gives the
required coupled growing-window error or our coefficient cap. No
theorem from this article is imported. It closes review390's specific
unread Schur-analysis lead on the present question without reopening
its other superoscillation comparisons.

### Applicability and comparison with the recorded stops

Our original sum of coefficient moduli remains the constraint. A later
lower certificate may use the one-way triangle estimate on the unit
circle, but must write and pay that specialization; a construction
bounded on the circle would still require the reverse coefficient-cost
estimate. No norm equivalence or such estimate is proved in this turn.
The source's outer multiplier does not preserve polynomial degree;
it must not be imported as a polynomial construction. Its prospective
use here is as a dual test function, not as p_n.

An outer boundary test could combine the complete circle's analytic
annihilation with independently charged leakage outside a spectral arc.
This differs from C997x's prescribed jets and C997z's exact centered
moment representation. It need not recover moments or propagate a
scalar prior from the slope interval. The source supplies the tools,
not a lower bound on the oscillatory target pairing. The concrete
family, bounded parameter range and decisive score to test are recorded
in [continuation401](2026-11-11-outer-boundary-annihilator-review-401.md).

The test only seeks an obstruction to the stronger sufficient Delta_n
objective. Its failure would park this dual family; its success would
still not obstruct the integrated E_n, whose oscillatory kernel may
cancel. An upper-window subarc can be a necessary test of simultaneous
window control, but cannot replace either window in an upper certificate.
Endpoint issues in the outer weight must be handled by Hardy boundary
limits, not by claiming continuous values there.

Reused reviews381/387/390's primary Faber-Walsh, weighted-pair,
fixed-weight arc, Bernstein and finite-energy comparisons. Read the
complete C997c(4)-(6) contract, C997s's original objective and the exact
scalar393/spectral-tail341 stop records; reused the supplied audited
C997z outcome and review398's scope. The local targeted searches for
outer functions, Hardy/boundary annihilators and Riesz–Herglotz in the
band/capped/spectral records found no matching prior test. This limited
duplicate search does not establish novelty. Prior stops remain intact.

### Searches and access qualifications

Query groups included `bounded analytic approximation on arc unit circle
prescribed function bounded extremal problem polynomials error rate`,
`polynomial approximation subexponential norm constraint arc unit circle
varying exponential target`, `superoscillations Schur analytic`,
`polynomial approximation arc outer function lower bound norm constrained`,
`superoscillation Hardy outer lower bound`, `bounded extremal exponential
polynomial circle approximation`, and `superoscillations bounded
coefficients arc duality`. Followed the author-hosted constrained-
approximation paper and the open-access Schur article to their actual
statements and the relevant proof cases specified above.

Danielyan, *On a polynomial approximation problem*, JAT162(2010),717-722,
DOI10.1016/j.jat.2009.09.001, was accessible only as a publisher abstract
in this review. No theorem from it is assessed or imported. An IIT
Hardy-course PDF returned404; no claim relies on it. These are
nonessential leads, not a blocker to the accessible Hardy tools.
Do not retry review381's inaccessible Pritsker–Varga lead or reopen the
spectral cutoff without its actual target-tail input. Search snippets,
unrelated RH webpages and broad superoscillation narratives were not
used as theorem evidence.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. A concrete,
independently testable boundary-dual mechanism is nominated, with no
derived rate and no claim of progress beyond the inspected sources.
No mathematical exploration counter is spent or reset. PROOF.md/DAG.md
remain unchanged because the mathematical argument has not changed.
