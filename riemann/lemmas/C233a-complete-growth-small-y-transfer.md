# Corollary 233a: fixed-height transfer of the complete growth residual

## Hypotheses

Use L018's entire real function Xi, L019's kernel K, and L020's
cosine representation. Let A_assoc and its Fourier transform have
exactly L233's actual-theta normalization, with k(u)=K(|u|).

The external identity used here is Michel Planat, *Nonlocal Cancellation
in a Theta-Kernel Decomposition of the Riemann Xi-Growth Derivative:
An Obstruction to Phase-Aligned Blockwise Positivity*, Preprints.org
202608.1692 v1, posted 25 August 2026, DOI
[10.20944/preprints202608.1692.v1](https://www.preprints.org/manuscript/202608.1692).
Import Definition 2, (28)--(29), and Theorem 3, (31), with its proof
(32)--(37); Proposition 1, (16), fixes the normalization.
For clarity, the exact quantities imported are

    Phi(u)=sum_(n>=1) (2 pi^2 n^4 exp(9u/2)
                       -3 pi n^2 exp(5u/2)) exp(-pi n^2 exp(2u)),
    D(z)=integral_0^infinity Phi(u) cos(zu) du,
    M(a,b)=Phi(a+b)Phi(a-b),  A_src(a,b)=-partial_b M(a,b),
    Q_y(a)=-integral_0^a b sinh(2yb) partial_a M(a,b) db,
    eps_x(a;y)=a sinh(2ya) integral_0^a A_src(a,b)sin(2xb) db,
    I(x,y)=integral_0^infinity [Q_y(a)sin(2xa)+eps_x(a;y)] da.

The source identity, for x>0 and y>0, is

    partial_y |D(x+iy)|^2=(2/x)I(x,y).                    (1)

No endpoint is removed from eps_x. In particular, A_src is not the
one-variable associated kernel A_assoc. L559 concerns endpoint deletion
in this same residual; it is a contrast, not a positivity input here.
The manuscript's global sign claims and asymptotic estimates are not
premises. The cited complete identity is imported; this corollary
independently checks its normalization and fixed-x Taylor transfer,
not the full manuscript.

## Conclusion

For every fixed real x>0, as real y decreases to zero,

    I(x,y)= (xy/16)[Xi'(x)^2-Xi(x)Xi''(x)] + O_x(y^3),    (2)
    lim_(y->0+) I(x,y)/(xy)=hat(A_assoc)(2x)/16.           (3)

The coefficient of y in the complete residual is therefore
x hat(A_assoc)(2x)/16. It need not be nonzero; no nonvanishing or sign
is asserted. There is no exclusion of central zeros or multiplicities.
The error statement is pointwise in x, not uniform at unbounded x.

One sufficient **unproved** signed estimate on an unbounded range is:
there exist X>0, y0>0 and a function omega:(0,y0]->[0,infinity),
with omega(y)->0, such that

    I(x,y) >= -xy omega(y)  for every x>=X and 0<y<=y0.   (4)

This would imply hat(A_assoc)(2x)>=0 for every x>=X. The bounded
range would still need a sign argument; evenness would cover negative
heights, and continuity would include zero. A uniform estimate such
as (4) is sufficient, not logically necessary: pointwise signed
liminf bounds for every x would also suffice. Neither form is proved
here or supplied by the source's fixed-y absolute estimate. These
conditions name the missing first-sign input; they are not an
independent positivity mechanism. Higher signs remain unresolved.

## Proof

Term-by-term comparison with the already convergent series in L019
gives K(u)=4Phi(u) for u>=0. L020 thus gives Xi(z)=4D(z) for all
complex z. This verifies Proposition 1 in the local normalization
without rederiving any theta transformation. In particular there is
no rescaling of x. Combining this equality with (1) gives

    I(x,y)=(x/32)partial_y |Xi(x+iy)|^2.                 (5)

Fix x>0 and define the auxiliary entire function of w

    H_x(w)=Xi(x+iw)Xi(x-iw).

It is even. By L018's conjugation symmetry, for real y it equals
|Xi(x+iy)|^2. Differentiation at w=0 yields

    H_x(0)=Xi(x)^2,   H_x'(0)=0,
    H_x''(0)=-2Xi(x)Xi''(x)+2Xi'(x)^2.

Indeed, the second derivatives of the two factors contribute
-Xi''(x)Xi(x) each, while their cross term is
2(iXi'(x))(-iXi'(x))=2Xi'(x)^2. Holomorphic Taylor expansion
of the entire odd function H_x' now gives

    H_x'(y)=2[Xi'(x)^2-Xi(x)Xi''(x)]y+O_x(y^3).

Here the Taylor remainder is bounded on a sufficiently small disc
about zero for this fixed x. We expand H_x' directly; no derivative
of an uncontrolled big-O term is taken. Substitute into (5) to obtain
(2), retaining the factor 2/32=1/16. L233 identifies the bracket
with hat(A_assoc)(2x), proving (3). This uses the complete I through
(5), without interchanging a limit with a sector, nested integral,
or infinite block sum. No division by Xi occurs, so the same proof
applies at every real zero, including multiple zeros.

For the conditional implication (4), fix any x>=X and divide (4)
by xy>0. Equation (3) and omega(y)->0 imply
hat(A_assoc)(2x)/16>=0. This fixes x before taking the limit;
it does not promote the O_x remainder to a uniform bound. L018's
evenness makes Xi'^2-Xi Xi'' even, and its continuity accounts for
the stated extensions if the remaining positive heights are signed.

The source's Lemma 7, (52)--(54), instead fixes y>0 and bounds
|I(x,y)| by c(y)x^(A(y))exp(-pi x/2) for x>=1. It has no sign
and no asserted small-y control of c(y), A(y). Dividing it by xy
does not yield a vanishing negative allowance in (4). Even a uniform
absolute O(xy) bound would only bound the coefficient's magnitude.
This is a hypothesis comparison, not a reproof or strengthening of
Lemma 7. Neither its absolute estimate nor (2) proves the first sign.

## Mathlib

The full transfer statement and the imported complete residual identity
have not been checked in Mathlib. Availability is unknown; absence is
not claimed. Holomorphic Taylor expansion is the standard analytic
input for the specialization. No formal verification is claimed.
General documentation: https://leanprover-community.github.io/mathlib4_docs/
