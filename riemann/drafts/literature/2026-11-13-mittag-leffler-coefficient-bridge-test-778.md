# Fixed Mittag-Leffler coefficient-to-logarithmic-Hankel discriminator

TARGET: Test whether F(t)=E_(3/2)(-t^2) satisfies the qualitative coefficient conclusions of Kawano Theorem1.1/Corollary2.1 and a positive cosine representation while its single logarithmic Hankel matrix H_3 has a negative direction.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step778 compared exact reciprocal-zero versus inverse-coefficient terminology, gamma-ratio infinite divisibility, M-Wright cosine transforms and the known Mittag-Leffler warning; scoped local searches found the older KPS family comparison but no completed joint-property/H_3 specialization. No novelty inference.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1 Theorems1.1-1.2/Section2/Corollary2.1; Berg math/0412340v1 Theorems5.1-5.2 including Mellin domains and proofs, printed14-15; Mainardi-Mura-Pagnini1004.2950v1 Section4(4.1)-(4.5)/(4.10)-(4.12) positivity/moment/cosine arguments; DLMF5.5.1/5.5.5/5.5.6/5.9.16; exact URLs, scope and reuse below.
COMPARISON: These sources provide general gamma/beta moment laws and the M-Wright cosine family; KPS already uses Mittag-Leffler as a non-real-zero warning. The exact factorial normalization, simultaneous qualitative coefficient properties and fixed H_3 certificate are the necessary model specialization, not a new family or actual-Xi theorem.
GAP: The joint properties and sign of the single 4-by-4 model matrix have not been proved or calculated. The source's quantitative lower bound, its full continuous density premise, actual theta realization and Xi order-one growth are outside the proposed generic-bridge test.
REASON: A known-model compatibility test can decide whether the qualitative coefficient properties plus positive cosine representation are sufficient evidence for logarithmic mixed positivity. Import the general results, then do only the stated applicability checks and one finite sign test after separate approval.
SCOPE: One fixed alpha=3/2,beta=1 model; no parameter, dimension, adjacent-minor or degree sweep. New assessment awaiting the separate next-turn approval; no mathematical specialization or script was produced in step778.

## Precise model and requested difference

The central gap is L030-L032/C032a, with S_k coming from the
logarithm of actual Xi. The proposed intermediate is a scope test of
one possible transfer from a different sequence; it supplies no actual
sign and is allowed to leave the main gap open.

Define E_a(w)=sum_(n>=0) w^n/Gamma(an+1), F(t)=E_(3/2)(-t^2),
e_n=1/Gamma(3n/2+1), and gamma_n=n! e_n. The coefficient convention
is F(t)=sum(-1)^n gamma_n t^(2n)/n!, with gamma_0=1.
These are definitions of the proposed test, not proved joint properties.

The requested qualitative coefficient checks are exactly
(-1)^(r-1) Delta^r log(gamma_n)>0 for n>=0,r>=2,
and that (gamma_n^(-c)) is a normalized Stieltjes moment sequence
for every c>0. A finite list of differences or powers cannot certify
these quantifiers. The positive-kernel check asks for a nonnegative
integrable cosine density with all needed moments and total mass1.

Use the germ at w=0 to define S_k=-k[w^k]log(E_(3/2)(-w)) and
H_3=(S_(i+j+2))_(0<=i,j<=3). The target is a real vector v with
v^T H_3 v<0, certified by a strict negative rational upper bound.
This is one prescribed matrix, requiring e_0,...,e_8. No sign is
predicted or inferred from a search snippet, approximate zero or
nonreal-zero citation. The finite Newton coefficient argument in
L040 may be reused only after checking the model germ and indexing;
L040's actual-Xi hypotheses are not silently asserted for this model.

## Primary inputs and application obligations

[Berg, *On powers of Stieltjes moment sequences, II*,
arXiv:math/0412340v1](https://arxiv.org/pdf/math/0412340v1),
Theorems5.1-5.2, printed14-15, were read with their proofs and general
Mellin domains Re(z)>-a. Gamma laws require a>0; beta laws require
0<a<b. Their product-convolution semigroups provide every positive
power, including noninteger Mellin exponents in the displayed domains.
The future specialization may use gamma multiplication, a beta/gamma
factorization and positive-variable pushforwards, checking normalization,
all parameters and domains. None of that factorization is derived here.
Theorems5.1-5.2 are imported, not reproved. Do not assume that arbitrary
quotients of infinitely divisible moment sequences remain in the class.

[Mainardi-Mura-Pagnini, *The M-Wright function in time-fractional
diffusion processes: a tutorial survey*, arXiv:1004.2950v1](https://arxiv.org/html/1004.2950v1),
Section4(4.1)-(4.5), positivity discussion and(4.10)-(4.12), supplies
nonnegativity, moments and the cosine transform for 0<nu<1. The
candidate nu=3/4 lies within that open parameter range. Import these
family statements rather than reprove stable-density theory. Check the
normalization at moment0 and the model series convention. If expanding
cosine under the integral, supply absolute-integrability/dominating
justification; the source's informal analyticity sentence alone is not
an interchange theorem. No endpoint nu=1 or theta identification is used.

[NIST DLMF5.5](https://dlmf.nist.gov/5.5) equations5.5.1,5.5.5 and5.5.6
supply recurrence/duplication/Gauss multiplication away from gamma poles;
[5.9.16](https://dlmf.nist.gov/5.9#E16), within the Re(z)>0 scope of
Section5.9(ii), supplies the digamma integral. Read the formulas and
hypotheses. The future qualitative finite-difference specialization
must justify differentiation, changes of variables and finite-difference
integration, retaining endpoint integrability and strictness at n=0.
A geometric coefficient rescaling changes an affine logarithm and must
be accounted for explicitly; it cannot replace factorial normalization.

[Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, Preprints.org202611.0383v1](https://www.preprints.org/manuscript/202611.0383),
posted4 November2026, Theorems1.1-1.2/Section2/Corollary2.1, identifies
the proposed qualitative conclusions. Its analytic/computer proof is
not independently audited or needed as a premise for the model's
properties. The numerical lower bound and complete continuous
Mellin-ratio assertion are not demanded of the model. A negative H_3
would therefore disprove only the specified qualitative generic
implication, not the source theorem or every possible stronger bridge.

## Duplicates, stopping test and downstream use

The completed step778 comparison is in
`2026-11-13-mixed-positivity-replacement-discovery-777.md`.
It reuses November6/8 contact coverage and compares the C040a stop,
L057 finite-test warning, L772's nonlinear Turan property and L773's
closed atomic grid. None proves the above qualitative linear-logarithm
property for this model or its H_3 sign. The KPS74(2024) Section4.2.4
example, [printed399](https://www.numdam.org/item/10.5802/aif.3600.pdf#page=24),
is prior art for the model family. Its book-based nonreal-zero assertion
is not an input to this finite test. The broader Levy sufficient-class
route remains parked; no actual-Xi interpolation or saddle is reopened.

Continue only to record a joint-property proof and certified negative
quadratic form for this one H_3, or to identify exactly which required
property/sign is not established. A certified nonnegative H_3 closes
this finite discriminator without implying all degrees. Inconclusive
intervals or an unproved class premise are inconclusive, not a negative
form. No parameter tuning, larger H_d, repeated precision campaign or
adjacent-minor sweep follows automatically; save incomplete reasoning
and end the attempt. A finite rational-arithmetic certificate must
retain every relevant input enclosure and negative upper threshold.

A joint countermodel would show why a coefficient positivity import
alone needs an additional theta-specific bridge. A favorable matrix
would pass only one necessary compatibility test. Actual Xi structure,
all-degree signs, shifted/mixed/global assembly and a complete RH proof
remain open in either case. The model's growth class must be stated;
no claim that it has Xi's order-one growth is authorized.

Known-method specialization/reproduction is the appropriate future
classification; neither novelty nor creative central proof routing is
claimed. Essential notebook inputs are L030-L032/C032a and L040's
coefficient identity; L024 is a product/summability comparison if a zero
interpretation is used, not an actual-Xi hypothesis granted to the model.
The bounded matrix can be defined entirely by the local logarithm.
C040a, L057, L772/L773 and the Levy stops are contrasts, not positivity
premises. No cross-notebook input. Full matching Mathlib coverage is
unchecked; retain supporting source links in any later canonical proof.
