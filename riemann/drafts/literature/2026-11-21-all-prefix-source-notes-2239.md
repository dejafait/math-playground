# All-prefix real-zero removal: source review2239

21 November 2026. Literature-only review of nomination2238. No model
identity, moment bound, zero certificate or growth calculation is proved
here. The main gap remains L030-L032/C032a. The intermediate question
tests a generic sufficiency implication, not actual-Xi positivity.

## Inspected identities and exact scope

NIST DLMF, version1.2.8 (15 September2026),
[5.12.5](https://dlmf.nist.gov/5.12.E5), states

    integral_0^(pi/2) cos(t)^(a-1) cos(bt) dt
      = pi / (2^a a B((a+b+1)/2,(a-b+1)/2)), Re(a)>0.

Principal powers are used. Read the parameter condition, surrounding
conventions, and [5.12.1](https://dlmf.nist.gov/5.12.E1), whose beta
integral requires positive real parts of both parameters. The section
attributes5.12.5 to N. Nielsen, *Handbuch der Theorie der Gammafunktion*
(Teubner,1906), section64. That original proof was not inspected; the
precise imported identity is the DLMF statement, not a reconstructed
Nielsen argument. The proposed later substitution is a=2n+1 and
b=2z/pi, with t=pi*u/2. Its normalization and identification with the
finite quotient remain specialization obligations. Outside the initial
beta-integral domain use analytic continuation, not a divergent integral.

[DLMF5.5.1 and5.5.3](https://dlmf.nist.gov/5.5) provide gamma recurrence
and reflection, the latter away from integer poles.
[DLMF5.2(i)](https://dlmf.nist.gov/5.2.i) states that reciprocal gamma
is entire, with simple zeros at the nonpositive integers. These cover
the continuation/removability tools needed for the intended quotient
comparison; no gamma identity or pole-removal proof is to be reinvented.

[DLMF4.22.1](https://dlmf.nist.gov/4.22.E1) is Euler's sine product for
complex z. [4.14.1-4.14.2](https://dlmf.nist.gov/4.14) give the complex
exponential definitions of sine and cosine. These cover the ordinary
product and zero-equation tools. Exhaustiveness and multiplicities for
this model, lack of real zeros of its extra factor, and persistence of
a specified nonreal zero still require an explicit later check. A
product citation alone is not that check.

T. Tao, *245C, Notes2: The Fourier transform*,6 April2009,
[sections1 and3](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/):
Exercises14/16 give convolution for L1 functions/finite Radon measures;
Exercise29 requires the function and its coordinate-weighted version
in L1 for differentiation. Exercise41 gives the Gaussian transform for
r>0; read its square-completion/contour hint. Read the inversion argument
through(11), using Schwartz approximation by Gaussians. These are standard
inputs, not newly proved results. Tao uses exp(-2*pi*i*xi*u); the proposed
angular convention requires xi=-z/(2*pi), initially real. Entire extension
must be justified separately. Schwartz decay alone does not imply the
requested super-exponential derivative bounds. Those need a direct
Gaussian-convolution tail estimate in the later specialization.

## Stronger criteria and an exact base-factor overlap

G. Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*, [arXiv:1309.0055v2](https://arxiv.org/pdf/1309.0055v2),
21 February2014: read Theorem3.7 and its complete proof, printed p8,
and the order-one statement beside(4.1), printed p10. The theorem assumes
a strictly logarithmically concave admissible kernel and characterizes
LP membership by positive definiteness of every weighted correlation
kernel(3.7). Its proof uses the generalized Laguerre expressions and
Theorem3.3. This is a different family from direct quotient inverses;
their pointwise positivity cannot be substituted. No application or
counterexample to that theorem is claimed. The order-one assertion
concerns the Xi transform after its explicit scaling and normalization,
and retains the known growth distinction from Gaussian examples.

H. Arellano-Peña, *Moment and Prime-Trace Criteria for the Riemann
Hypothesis, with Spectral Exclusions and Nonlocal Positivity*,6 September
2026, amended30 September2026, author-uploaded preprint,
[section5.3, printed p10, (5.12)-(5.13)](https://www.researchgate.net/publication/414031680_Moment_and_Prime-Trace_Criteria_for_the_Riemann_Hypothesis_with_Spectral_Exclusions_and_Nonlocal_Positivity),
DOI10.13140/RG.2.2.22856.07682: inspected the complete subsection.
It already gives exp(-z^2)(2+cos z) as a positive Gaussian-translate
transform with nonreal zeros, explicitly excluding an inference within
the zeta class. This is exact overlap with the proposed base factor;
no originality is claimed for it. The inspected subsection contains
neither the sinc multiplier nor the every-prefix quotient assertion.
The rest of that preprint is not imported, reviewed or endorsed here.

## Local reuse and recorded stops

Read the hypotheses/conclusions of accepted C919m/C919o, and reused
source notes2225/2234 for their finite actual-Xi scope and the distinction
between direct inverse kernels, reciprocal Laplace densities and
correlation kernels. C919o still assumes the second actual root and
retains C919f's numerical backend contracts. None of those contracts
is a premise for a new explicit model. L018 supplies the zero
correspondence, not the growth-order input; the latter source is above.

Read canonical L262 and its order-two qualification. Its three
Laguerre levels do not establish the new all-prefix quantifier.
Read the nonreal-deflation stop: it deletes the detecting pair, while
the present test must retain one. Read finite-block1117 and the
finite-divisor signed-composition667 stop, with their relevant source
comparisons. Changing finite countermodels cannot prove a statement
for one fixed model; signed residual minors are a different observable.
No historical stop is enlarged into a global ban. No cross-notebook input.

## Bounded discovery record and remaining difference

Local searches were confined to drafts/literature, ATTEMPTS, the named
lemma files and source records, using all-prefix, cosine-power, sinc,
finite-block1117 and finite-divisor667 terms. External query groups:

- cosine power Fourier integral gamma; cosine power Fourier gamma zeros;
  DLMF beta cosine integral; Nielsen Gammafunktion1906.
- sinc zeros division positive definite; Fourier sinc divided finite
  zeros; characteristic functions removal real zeros; real zeros
  division positive kernels Fourier; quadratic factors positive definite.
- Exact title search for the base-factor preprint and its Gaussian
  cosine construction.

The antenna cosine-power slides and generic numerical transform pages
were search leads only, not imported identities. Nielsen's original
section64 remains unread, not an essential blocker because the exact
DLMF identity is accessible. No matching all-prefix theorem was located
in the inspected sources; that is not a novelty or nonexistence claim.
The original Wintner/Spira and optional Spigler leads remain parked.

SPECIALIZE is warranted for a later proof: ordinary identities are
covered, while their simultaneous all-n realization in the fixed F
is not an imported theorem. Required differences are the exact normalized
quotient identity including n=0 and removable points; smooth strict
positivity and tails of all derivatives; an n-independent second-moment
bound; the complete real-root list; a surviving nonreal zero; and exact
growth order. Compact support of the proposed cosine-power inputs is
a possible route to uniform moments, not an established estimate here.
The later proof should cite the identities and prove only these
applicability/gluing obligations, rather than reprove classical formulas.

Continue only if all obligations hold for every integer n>=0 for this
single F. Stop the candidate at the first genuine failure, without
changing its parameters. Failure of one proof method alone is inconclusive.
Even success only limits the generic bridge in its stated growth class;
actual-Xi iteration, order-one sufficiency, arithmetic structure and the
all-degree mixed signs remain independent gaps. Full matching Mathlib
coverage and supporting theorem names were not checked. No RH candidate.
