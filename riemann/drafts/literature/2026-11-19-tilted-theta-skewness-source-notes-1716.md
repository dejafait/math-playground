# Tilted full-theta skewness: source review1716

Working checkpoint, literature only. The exact target is assessment1715;
the supplied startup snapshot is used without rereading it. Main gap:
L030-L032/C032a actual-Xi positivity; C028b's H_d=o(d) remains unpaid.
The proposed intermediate test concerns the centered third moment of
finite Jacobi spectra for exp(theta*u)K(|u|), uniformly in degree and
all real theta. Its downstream use is only three-coefficient reference
admissibility, not a full companion-cost payment.

Read L019 in full, C028j/k's matching arguments through their feasibility
classifications, source-notes1694/1712, approval1714 and source-notes1595.
C028k gives the exact actual centered second/third power sums, without
assuming real actual roots; its recurrence-specific optimization is not
an estimate for theta weights. C028j is likewise family-specific.
Stops1695/1713 and parks1534/1708 remain intact. Narrow local searches
found no previously completed tilted-theta spectral-skewness assessment.
The broad initial notebook-scoped git status produced excessive output;
it was not used as mathematical orientation and no existing work changed.

Primary leads now being inspected: Van Assche's exponential-deformation
Toda equations; Kuijlaars--Van Assche's varying-recurrence zero theorem;
Kuijlaars--Tibboel's analytic varying-potential recurrence asymptotics.
No uniform theta theorem, countersequence or new trace calculation has
been established. No lemma or mathematical script is changed. A source
preview or search snippet is not theorem coverage. Completion follows.

## Completed review: sources and exact scope

Accessed 19 November 2026. No uniform skewness theorem or explicit
countersequence was established. This is EXPLORATION, not an impossibility
result, a novelty certification or an improvement to H_d.

Walter Van Assche, *Orthogonal polynomials, Toda lattices and Painleve
equations*, [arXiv:2202.11017v1](https://arxiv.org/pdf/2202.11017),
22 February 2022: read Section1.1 pp1-2, Section2 pp3-6, Lemma2.1
and its complete proof, and the subsequent recurrence compatibility
calculation. For positive mu with all moments of exp(t*x)mu, its monic
recurrence uses diagonal b_n and squared off-diagonal a_n^2. Equations
(2.1)-(2.2) give

    (a_n^2)'=a_n^2*(b_n-b_(n-1)),
    b_n'=a_(n+1)^2-a_n^2,    a_0=0.

Lemma2.1 gives partial_t P_n=-a_n^2 P_(n-1). The proof differentiates
orthogonality and then compares recurrence coefficients; it is not a
uniform-in-degree estimate. Section2 explicitly distinguishes the finite
system, with its terminal coefficient zero, from the semi-infinite
system. A finite principal block for an infinite-support measure cannot
be substituted for the former by dropping its exterior coefficient.
No isospectral conclusion for such blocks is imported. The publisher
page returned403; the author preprint supplied these statements and
proof cases. No inaccessible source remains essential to this import.

A.B.J. Kuijlaars and W. Van Assche, *The asymptotic zero distribution
of orthogonal polynomials with varying recurrence coefficients*,
J.Approx.Theory99(1999),167-197, DOI10.1006/jath.1999.3316,
[author manuscript](https://wis.kuleuven.be/analyse/members/walter/varrec.pdf):
read Theorem1.4 and the definition of ray convergence, manuscript pp3-4;
Theorem1.10/Remark1.11 p5; and Section3 pp8-11, including the bounded
coefficient case and its associated-polynomial extension. Positive
off-diagonals and continuous limits a(t),b(t) of the varying recurrence
coefficients along every n/N-to-t sequence are hypotheses. The limiting
zero measure is an average of arcsine laws on
[b(s)-2a(s),b(s)+2a(s)]. Theorem1.10 adds endpoint continuity and
convergence at t=0 for extreme-zero limits. The general proof of1.4
discards a vanishing fraction of zeros; it does not supply third-moment
control on discarded zeros. Neither the required recurrence limits,
moment control nor a symmetric limiting law is supplied for tilted theta.
Thus weak zero-measure convergence alone cannot be used here as a
standardized third-moment estimate.

A.B.J. Kuijlaars and P.M.J. Tibboel, *The asymptotic behaviour of
recurrence coefficients for orthogonal polynomials with varying
exponential weights*, [arXiv:0708.3956v2](https://arxiv.org/pdf/0708.3956):
PDF identifier24September2007 (the retrieved title page additionally
prints29August2021). Read pp1-3 through Theorem1.1 and its assumptions;
no proof or asymptotic is imported. The potential V in exp(-N*V) is
fixed, real analytic, grows faster than log(1+x^2), and is one-cut
regular: a single equilibrium interval, a strictly positive analytic
density factor and the strict exterior variational inequality.
Theorem1.1 concerns diagonal recurrence asymptotics with constants
depending on V. The tilted-theta family has not been reduced to this
fixed-potential setting with these hypotheses and uniform constants.
The word 'varying' in the title does not establish the required
unbounded-tilt uniformity. No theta analytic-potential or regularity
claim is made.

NIST DLMF v1.2.8, [18.2(viii)](https://dlmf.nist.gov/18.2#viii),
rechecked Favard/uniqueness qualifications; reuse1694/1714 for monic
recurrence, positive norm ratios and even-weight parity. Favard alone
does not assert uniqueness for an arbitrary unbounded measure. The
additional18.9 page was opened but no new formula from it is an input.
The Cameroon lecture notes were inspected as a preliminary Toda lead;
the precisely numbered2022 preprint above supplies the chosen import.

## Applicability and normalization obligations

For every finite T, L019 supplies an integrable majorant for
|u|^r exp(T|u|)K(|u|), for each fixed r>=0: choose its decay exponent
B>T and absorb the polynomial by the remaining exponential decay.
Consequently each finite real tilt has positive finite normalization,
all moments and full support; the same domination permits moment
differentiation on compact tilt intervals. This is the applicability
check for the source, not an estimate uniform in unbounded theta or d.
Multiplying a measure by a scalar normalization does not change its
monic orthogonal polynomials or recurrence coefficients. These facts
allow direct use of the unnormalized source deformation.

Use the empirical spectral convention

    J_d(theta): principal block on indices0,...,d-1,
    m_d=tr(J_d)/d,
    M_r(d,theta)=tr((J_d-m_d*I)^r)/d,
    g_d(theta)=M_3(d,theta)/M_2(d,theta)^(3/2).

This defines the reviewed observable; no identity for its derivative is
calculated here. M_2 is positive for d>=3 by positive off-diagonals.
C028k's canonical matching calculation gives actual centered power sums
d(d-1)v and -d(d-1)(d-2)tau, with v=S_2>0,tau=S_3>0. They are formal
root sums without a real-root hypothesis. Any future comparison must
divide these sums by d before standardizing, and account for the sign
of a real affine dilation. Neither the comparison nor feasibility is
proved in this review. Raw traces and empirical moments must not be
silently interchanged.

## Search, duplicates and bounded route decision

Queries included: `orthogonal polynomials exponential deformation
measure Toda zeros varying weight asymptotics tilt`; `orthogonal
polynomials Riemann xi weight theta recurrence coefficients zeros
exponential weight`; `orthogonal polynomials log concave weight skewness
zeros convex external field`; `Walter Van Assche orthogonal polynomials
Toda lattice exponential modification e tx recurrence coefficients
differential equations pdf`; `Kuijlaars Van Assche asymptotic zero
distribution orthogonal polynomials varying recurrence coefficients
theorem 1.4 pdf`; `orthogonal polynomials Erdos weights exponential
tilt exp tx zeros asymptotic`; `"orthogonal" "theta" "skewness" Jacobi`;
`"orthogonal polynomials" "third moment" "zeros" skewness`;
`"orthogonal polynomials" "exponential tilt" "Toda"`. No exact theorem
for this kernel and all real varying tilts was located. Failed searches
do not show that such a result is unknown.

Search-only leads included polynomial-potential/Freud asymptotics,
even Erdos-weight interpolation, Romik's Xi expansions in a different
orthogonal basis, matrix-valued deformations, and Riemann theta-function
formulas. Their abstracts/snippets are not hypotheses or proof coverage
for this weight; none is imported. The Princeton chapter initially
opened concerns discrete ensembles and is not an input. Screenshot
requests did not yield inspected images; the relevant text proof cases
were readable, and no visual verification is claimed.

Local filename and content screening was confined to theta/Pollaczek
assessments and attempts. The September23 tilt-variance and large-tilt
first-sign attempts concern the probability law's mean/variance, not
equal-weight finite-Jacobi spectral moments. The September9 log-concavity
stop concerns Fourier root reality. None answers this skewness question;
none authorizes assuming a favorable sign. Their stops remain intact.

Park the global all-tilt vanishing diagnostic pending a new uniform input
or an independently controlled countersequence. Do not spend another
turn merely searching the same asymptotic titles. One narrower test has
source coverage: exact first tilt variation at zero, including centering
and the exterior recurrence coefficient, followed by its precise cubic
matching normalization. Nomination1716 states this test for separate
approval. Nonzero response would show a locally adjustable odd spectral
coordinate only; it would not disprove uniform vanishing as d grows,
achieve the required cubic magnitude, match three coefficients, control
the remaining residuals or pay H_d=o(d). Zero or unboundedly inconclusive
response stops that local test without a higher-order sweep.

No central creative upper-payment mechanism is justified yet: an odd
parameter alone supplies no control of the full cost. The proposed
finite Toda specialization is REPRODUCTION, not creative work. This
completed source review is LITERATURE/NOVELTY_UNCHECKED/EXPLORATION;
no counter is reset. Full matching Mathlib coverage remains unchecked.
No cross-notebook input, lemma/script write, PROOF/DAG edit or new
mathematical result is made.
