# Source review: centered gaps and the complete logarithmic mean

TARGET: Assess whether every fixed centered-gap profile satisfying L698 has limsup_(q->infinity) A_(12q+3)(e)/(12q+3)<0, where A_n(e)=mean_(|u|=|zeta|=1)log|G_(n,e)(u,zeta)|, with the full angular complement and all spatial moments retained.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 126 made six bounded queries on full logarithmic means, arc smallness, growing-degree Mahler measure and circle Remez/subarc sieve inequalities; inspected the primary statements and relevant proof cases below and reused the step-97/114 Mahler assessments. Scoped L657/L666/L690/L695/L698 and the step-115 stop comparison found no existing proof or counterprofile for this exact sign. Failed searches do not establish novelty.
SOURCE_EVIDENCE: Brunault--Zudilin, Many Variations of Mahler Measures, Propositions 1.4--1.5 pp.6--7, boundary-root complex proof; Tikhonov--Yuditskii, arXiv:1809.09726v2 (20 October 2018), Theorem 1.2 p.3 and final proof pp.10--11; Erdelyi, Sieve-Type Lower Bounds for the Mahler Measure of Polynomials on Subarcs, author PDF, Theorem 2.1 pp.3--4, Lemmas 3.3--3.4 p.6 and theorem proof pp.12--14. Reuse Boyd/Dimitrov--Habegger/BGMP with the exact limitations in step 114; BGMP Proposition 4.10 and boundary-zero handling reinspected.
COMPARISON: Jensen accounts for all charges but does not estimate their balance; fixed-degree continuity supplies no growing-degree rate. Sharp circle Remez retains an exponential degree cost, while L657 permits angular degree M(n-1). The subarc sieve needs sample logarithms and endpoint-coefficient normalization that are not established for this family. None of the inspected results supplies TARGET or a centered-gap counterprofile; L695's absolute-tail stop does not settle the signed mean.
GAP: Control the full signed complementary angular contribution or the complete charge Z_n-P_n at order n for the same fixed L698 profile, with all M moments, zeros, pole factors and logarithmic singularities retained. The universal negative rate and its negation remain unproved.
REASON: Essential comparison is sufficient for one bounded family-specific signed-complement/complete-charge attempt on the unchanged target, after separate supervisor approval of this changed assessment. EXPLORE is permission to test, not a favorable sign, novel theorem or known-result import. No essential source blocker remains; this literature-only step derives no new result and edits no lemma or mathematical script.
LITERATURE_REASON: The essential unread comparison concerns signed full-circle logarithmic compensation and growing-degree small-value estimates, outside the ready fixed-arc assessment; reuse the existing Mahler source assessments rather than repeat their searches.
SCOPE: Exactly TARGET and one bounded signed-complement or complete-charge test: one fixed real l1 profile before n, cap 1/8, the prescribed center omega_* and a fixed gap g>0, n=12q+3, original unit masses and anchor, j=0, denominator angle 1/u, exact -2q<=m<2q, and all M=n/3 moments. A counterprofile must satisfy this same distributional gap. No uniform constants over profiles, effective gap, root separation, derivative interchange, exchange of limits, or conclusion from generic arc smallness is preapproved.

The nomination below is preserved. Its requests for a separate review are
resolved by the completed source comparison following it; its proposed
mathematical estimates remain unproved.

The main gap remains actual-Xi all-degree mixed positivity and realization.
The successful L698 audit supplies a new input for testing the earlier
complete-logarithm route: exponential smallness now concerns the actual full
spatial polynomial on an arc. The unresolved question is whether the rest
of the angular circle compensates for that smallness in the complete mean.
A rigorous negative linear rate, if established, would challenge the
fixed-profile lower-liminf mechanism associated with the L690 baseline.
A rigorous compensation result would instead identify why the arc estimate
does not decide that mechanism. Neither outcome would by itself settle
L666's angular maximum H, its comparison with D, support, realization or RH.

The source review should first inspect L657's complete logarithmic
integrability and charges and L690's exact baseline conclusion, using only
the relevant proof ranges. Reuse the theorem statements and scope records
in `2026-11-03-summable-displacement-complete-log-transfer.md` and the
full-spatial assessment. Compare applicable primary subharmonic/Mahler
results with the growing-degree rational family and its normalizations.
Read relevant hypotheses and boundary-zero proof cases before importing
them. An estimate for a fixed polynomial, an unsigned perturbation norm,
or a single spatial coefficient does not automatically match this target.

The later mathematical test, if separately approved, must bound or obstruct
the complete signed mean at order n for the same fixed profile. The
complementary angular contribution and negative logarithmic integrability
must be paid; the small-arc supremum alone is insufficient. A valid known
result or counterexample that settles this implication changes the route;
an unquantified compensation possibility does not. If coverage instead
shows that the proposed universal sign is too broad, record the exact
obstruction and nominate a materially narrower independently testable
observable before attempting uncovered mathematics.

The existing L695 absolute-tail stop is preserved. This nomination does
not reopen its closure: the proposed input is the newly audited signed
full-polynomial bound, and the missing task is the full logarithmic
complement. No new theorem, script, calculation or complete-mean estimate
has been derived in this nomination. Matching Mathlib coverage is not
checked. A separate source review is required before research on TARGET.

## Completed comparison — 3 November 2026, step 126

### Exact local interfaces and recorded failures

Read L657's hypotheses and conclusions and its clearing/integrability
and complete-divisor proof, Sections 2--3. In this family G=K/Q,
deg_u K<=M(n-1), deg_zeta K<=M-1, and Q has no angular circle zeros.
Its established identity A_n=m_0+Z_n-P_n includes actual degrees,
multiplicities, cancellations and boundary zeros; exceptional center-zero
slices have measure zero. Its bounds on m_0 and nonnegativity of Z_n
are retained, without claiming a new asymptotic charge comparison.

Read L666's exact family and rational continuation, L690's hypotheses
and audited conclusion, and L698's hypotheses/conclusion and source
interface. L690 applies to a common shift, including zero, and gives
A_n(0)=-log R+o(1). Its full-circle compensation does not assert the
same estimate for the fixed gap profiles of L698. L698 controls the
original complete spatial polynomial near +1, with fixed existential
delta,c,C,N; it does not control the remaining angular circle. No
effective values or additional regularity of the profile are assumed.

Read L695's statement, source scope and final qualifications, the
step-115 history, and
`ATTEMPTS/2026-11-03-fixed-summable-absolute-tail-stop.md`.
The obstruction concerns a specified absolute termwise tail norm; its
explicit profile is not asserted to have the centered gap. It supplies
neither a counterexample to TARGET nor a bound for the signed mean.
L695's finite-head conclusion is unaudited and is not needed as a
premise of the proposed direct complete-charge test. The step-105
n-dependent numerical screen remains parked. The earlier full-spatial
assessment explicitly excludes full-circle logarithmic conclusions;
no duplicate complete-mean proof was found in these relevant records.

### Primary theorem comparison

**Exact logarithms.** F. Brunault and W. Zudilin, *Many Variations of
Mahler Measures*, ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
Reinspected the complex proof's inside, outside and boundary-root cases:
the normalized root integral is log max(1,|alpha|); boundary indentation
cost tends to zero. The polynomial identity retains its actual leading
coefficient and every root with multiplicity. L657 already specializes
this input and establishes integrability/Fubini, including its exceptional
slices. Ordinary submean reasoning for a holomorphic numerator cannot
be applied directly to meromorphic G while omitting Q. These theorems
give accounting, not a signed compensation estimate. No reproof is needed.

**Reused quantitative coverage.** Reuse
`2026-11-03-summable-displacement-complete-log-transfer.md` and
`2026-11-03-independent-shift-mahler-homotopy.md`: Boyd's theorem p.127
has fixed ambient degree; Dimitrov--Habegger, arXiv:1909.06051v2,
Appendix A, Lemmas A.3--A.5, has term-count-dependent constants and
exponents. Neither hypothesis can silently be made uniform in n.
No renewed search or reproof of these unchanged results was necessary.

Reinspected F. Brunault, A. Guilloux, M. Mehrabdollahei and R. Pengo,
[*Limits of Mahler Measures in Multiple Variables*, arXiv:2203.12259v2](https://arxiv.org/pdf/2203.12259v2),
27 June 2022, Theorem 4.6 pp.9--10 and Proposition 4.10 with its
layer-cake proof p.11. For d variables, k>=2 nonzero terms,
L_infinity(P)=1, 0<alpha<1, integer m-by-d matrix A, m<=d,
rho(A)>diam(P), the regularization error is nonnegative and at most
C_2(d,k,alpha)*epsilon^((1-alpha)/(2(k-1))), with the explicit
constant recorded in step 114. A=I_d covers the ordinary torus.
Zeros are retained, but normalization and growing k remain obligations;
the proposition gives neither a signed complement bound nor a
relative comparison of the present rational families. No new bound is
specialized from it here.

**Sharp circle Remez.** S. Tikhonov and P. Yuditskii,
[*Sharp Remez inequality*, arXiv:1809.09726v2](https://arxiv.org/pdf/1809.09726v2),
20 October 2018, Theorem 1.2 p.3: for a complex polynomial P of
degree d bounded by one on measurable E subset T, with angular
length |E|>=2*pi-s and 0<s<2*pi,

    sup_T |P| <= T_d(sec(s/4)).

Read the equality case (1.6) and final single-gap proof pp.10--11;
the conformal extremal-reduction lemmas were not independently audited.
This is a known supremum inequality, not a signed-log identity.
It permits complex coefficients and boundary zeros. Its Chebyshev
factor retains exponential dependence on d. Applying a cleared-numerator
bound would still require Q's normalization and all growing degree
costs. L657 permits d=M(n-1), so no required order-n complement
bound is supplied by this theorem alone. Sharpness concerns general
polynomials, not a counterprofile in L698. No extremizer is specialized
or new counterexample derived in this review.

**Subarc logarithmic sieve.** T. Erdelyi,
[*Sieve-Type Lower Bounds for the Mahler Measure of Polynomials on Subarcs*](https://people.tamu.edu/~terdelyi/papers-online/mahleronarcs.pdf),
author PDF, accessed 3 November 2026 (undated file), Theorem 2.1
pp.3--4. For P(z)=sum_(k=0)^d b_k z^k, b_0*b_d!=0,
a<b<=a+2*pi, ordered samples a<=t_0<...<t_l<=b,
t_(-1)=2a-t_0, t_(l+1)=2b-t_l, and maximum mesh
Delta<=sin((b-a)/2)/2, it states

    sum_j (t_(j+1)-t_(j-1))/2 * log|P(exp(i*t_j))|
      <= integral_a^b log|P(exp(i*t))|dt + C*E,
    E=(b-a)*d*Delta+d*Delta^2*log(1/Delta)
       +sqrt(d*log S)*(Delta*log(1/Delta)+Delta^2/(b-a)),
    S=||P||_T/sqrt(|b_0*b_d|),

with absolute C. Read Lemmas 3.3--3.4 p.6 and the theorem proof
pp.12--14: nearby endpoint zeros and missing endpoint samples incur
explicit errors. This is a lower integral bound requiring actual sample
values and coefficient control; neither is supplied for our slices.
Degree drops/zero constant slices and spatial integration would need
justification. Theorem 2.2's Fekete specialization has different
coefficients. No family-specific application is asserted. One image
request timed out; accessible complete theorem/proof text resolved access.

### Search scope and decision

New query strings, 3 November 2026:

- `polynomial small on arc circle logarithmic mean Mahler measure Remez inequality degree Nazarov`
- `rational functions Remez inequality logarithmic integral poles circle compensation`
- `"Mahler measure" "growing degree" "small" arc`
- `"Sieve-Type Lower Bounds" "Mahler" subarcs`
- `Erdelyi sharp Remez inequality unit circle complex polynomials 2018 pdf`
- `"Remez- and Nikolskii-Type Inequalities for Logarithmic Potentials" pdf`

The 1994 Erdelyi--Li--Saff logarithmic-potential paper and the recent
disk-growth Remez preprint arXiv:2606.24823 are unread leads, not
imported statements. The inspected sharp polynomial theorem suffices
to identify why a generic degree-based arc propagation does not supply
the proposed rate; no dependent claim requires those leads. There is
no essential source-access blocker. No inspected theorem matches the
complete rational family with this fixed-profile distributional gap.
This bounded search does not establish originality or impossibility.

DECISION is EXPLORE for the unchanged exact target. A later single
attempt may test the signed complementary angular integral or L657's
complete zero-minus-pole charge directly, using L698 for the controlled
arc and L690 only for its established baseline. It must keep the same
fixed profile, all moments and endpoints, and must justify any singular
log limit. The desired evidence is a rigorous negative order-n full-mean
rate, or a rigorous admissible fixed-gap counterprofile violating the
universal sign. Quantified compensation is useful intermediate evidence,
but is not automatically a refutation of TARGET. No charge bound,
derivative formula, zero census or complement estimate is proved here.

Continue only if the attempt produces a paid order-n signed estimate
or a materially informative obstruction. Abandon that attempted closure
if it reduces to a generic growing-degree Remez loss, L695's absolute
tail norm, unproved cancellation, or omitted roots; preserve the original
target as open if no counterprofile is proved. A different observable
requires separate source review. This does not repeat the stopped
absolute-tail mechanism, nor authorize arbitrary repeated Jensen rewrites.

Mathlib: full matching coverage of TARGET is not checked. Reuse only
the supporting one-variable Mahler/root-formula coverage already
recorded in L657/L690. No absence claim, formal verification, RH
candidate or progress beyond the checked literature is claimed.
