# Lemma 812: actual-theta nested thresholds fail the strongly Rayleigh premise

## Hypotheses

Let K be the theta kernel of L019, let m_0=integral_0^infinity K(u)du,
and let U have the probability law dmu(u)=K(u)du/m_0 on [0,infinity).
L021 gives 0<m_0<infinity. This is exactly the scalar law used in
L795; no polynomial representation from that lemma is assumed here.
Fix finite real thresholds 0<a_1<a_2<infinity. Set
B_i=1_{U>=a_i} and S={i in {1,2}:B_i=1}. Define its probability
generating polynomial by

\[
 g(z_1,z_2)=\mathbb E[z_1^{B_1}z_2^{B_2}].
\]

A nonzero real polynomial is real stable if it has no zero when every
variable has strictly positive imaginary part. A finite-subset probability
law is strongly Rayleigh when its generating polynomial is real stable.

## Conclusion

Put p=mu([0,a_1)), q=mu([a_1,a_2)), and r=mu([a_2,infinity)). Then
p,q,r>0, p+q+r=1, and

\[
 g(z_1,z_2)=p+qz_1+rz_1z_2,\qquad
 \Delta_{12}(g)=(\partial_1g)(\partial_2g)-g\partial_{12}g=-pr<0.
\]

Consequently this actual-theta threshold law is not strongly Rayleigh.
No strongly Rayleigh law on a larger finite coordinate set can have
this exact two-coordinate marginal. The conclusion stops this literal
encoding, including refinements that retain that marginal. It makes
no assertion about real-rootedness of P_d in L795, other encodings,
signed theta compensation, mixed positivity or RH. No positive lower
bound on pr uniform over degenerating thresholds is claimed.

## Proof

**Probability cells and strictness.** L019 gives a positive measurable
kernel on [0,infinity), and L021 gives its finite positive total mass.
The absolutely continuous law has no atoms at either threshold. Its
three displayed cells partition [0,infinity); changing endpoint
conventions has no effect. Each cell contains an open interval of
positive length: for example (a_1/3,2a_1/3), (a_1,a_2), and
(a_2,a_2+1), respectively. Since K is strictly positive throughout
each such interval, its integral there is positive. Thus p,q,r>0,
and normalization gives p+q+r=1. This uses the full actual law,
without truncating its tail or replacing U by independent copies.

The ordered thresholds imply B_2<=B_1. The four cells (B_1,B_2)
=(0,0),(0,1),(1,0),(1,1) therefore have probabilities p,0,q,r.
Their generator is the stated real multiaffine polynomial. It is
nonzero because g(1,1)=1 (also g(0,0)=p>0).

**Imported criterion and its specialization.** P. Branden,
*Polynomials with the Half-Plane Property and Matroid Theory*,
[arXiv:math/0605678v4, Theorem 5.6 and Example 5.7](https://arxiv.org/html/math/0605678v4),
characterizes nonzero real multiaffine stable polynomials by
nonnegative Rayleigh differences at every real vector. Example 5.7
gives the bivariate coefficient criterion with orientation
coefficient(z_1)*coefficient(z_2)-coefficient(1)*coefficient(z_1z_2).
We import this theorem, not its proof. The real, multiaffine and
nonzero hypotheses were checked above; homogeneity is not required.
Direct differentiation for our coefficients gives

\[
 \partial_1g=q+rz_2,\quad \partial_2g=rz_1,\quad
 \partial_{12}g=r,
\]
\[
 (q+rz_2)rz_1-r(p+qz_1+rz_1z_2)=-pr.
\]

All variable terms cancel, so the difference is strictly negative
at every real point. In particular at (0,0) the product of first
derivatives is zero and g partial_12 g=pr, independently checking
the determinant orientation. The necessary condition fails.

**Scope under projection.** J. Borcea, P. Branden and T. Liggett,
*Negative Dependence and the Geometry of Polynomials*,
[arXiv:0707.2340v2, Definitions 2.9--2.10, Section 2.1(ii), and
Proposition 3.1(2)](https://arxiv.org/html/0707.2340v2),
give the strongly Rayleigh terminology, projection of finite laws,
and closure of real stability under real specialization, allowing
the zero polynomial. These are reused primary-source imports from
the approved assessment. If a larger law has generator G, its
two-coordinate marginal is obtained by setting every other variable
to 1: those coordinates' monomials then contribute a factor 1 and
their probabilities are summed. Repeated real specialization of a
real stable G is stable or zero. A probability marginal has value
1 at (1,1), so it is not zero. If the marginal were exactly our law,
its generator would be g, contradicting the negative difference.
This argument requires exact marginal matching and does not exclude
different coordinate constructions or arbitrary correlated laws.

This is a conventional specialization of known negative-dependence
criteria, not progress beyond those criteria. No identity expressing
P_d as a matrix average has been proved or assumed. Matrix/coefficient
matching, a sufficient signed comparison, degree-uniform transfer,
initial and edge regimes, and shifted/mixed signs remain open.

## Mathlib

Full matching coverage has not been checked. Availability in Mathlib
of the multiaffine Rayleigh characterization, projection closure and
this theta specialization is unknown. No formal verification is claimed;
the finite probability and differentiation calculations are written
out above, and the stability implications are precise source imports.
