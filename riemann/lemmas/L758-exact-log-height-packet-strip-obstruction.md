# L758 — Exact log-height Gaussian has no full-strip extension

## Hypotheses

Fix finite real numbers a>0 and h>0. On the right half-plane define

\[
W_{a,h}(z)=\exp\left(-\frac{(\operatorname{Log}z-\log a)^2}{2h^2}\right),
\]

where Log is the principal logarithm. Let epsilon>0 and
S={z in C: |Im z|<1/2+epsilon}. Exact agreement means agreement on a
real open interval I containing a and contained in (0,infinity).

## Conclusion

There is no function F holomorphic on S with F(x)=W_{a,h}(x) for
every x in I. This holds for every fixed a,h>0 and every epsilon>0.
Thus this exact packet cannot meet the analytic-strip requirement of
the cited Guinand--Weil formula. This is an obstruction to this
implementation only; it gives no restriction on approximate or changed
packets, no sign estimate, and no conclusion about RH.

## Proof

Import the principal-logarithm convention and analyticity from
[DLMF 4.2(i), equations 4.2.1--4.2.6](https://dlmf.nist.gov/4.2.i).
Import finite-order factorization, infinite-order vanishing and the
identity theorem from Peter Topping, *MA3B8 Complex Analysis*, version
29 July 2024, Theorems 7.3--7.5, printed pp.67--69
([primary text](https://warwick.ac.uk/fac/sci/maths/people/staff/peter_topping/teaching/ma3b8_cplxanal_24_07_29.pdf)).
These standard results are used by citation, not reproved here.

Suppose such an F exists. The domain D=S intersect {Re z>0} is open,
nonempty and convex, hence connected. Both F and W are holomorphic
on D. Their agreement on I has the interior accumulation point a
in D, so the identity theorem gives F=W throughout D. In particular,
F(x)=W(x) for every real x>0, and F(a)=1.

For each integer m>=0 put t=-log x, so x approaches zero through
positive values exactly when t tends to infinity. Then

\[
\frac{W_{a,h}(x)}{x^m}
=\exp\left(-\frac{(t+\log a)^2}{2h^2}+mt\right)
=\exp\left(-\frac{t^2}{2h^2}
 +\left(m-\frac{\log a}{h^2}\right)t
 -\frac{(\log a)^2}{2h^2}\right)\longrightarrow0.
\]

The coefficient of t^2 is strictly negative for every permitted h;
all remaining coefficients are fixed finite constants. This proves
the limit for every m without exceptional a or h or a parameter limit.
For m=0, continuity of F at the interior point 0 of S gives F(0)=0.

If this zero has finite order m>=1, Theorem 7.3 gives, on a neighborhood
of 0, F(z)=z^m G(z), with G holomorphic and G(0) nonzero. Along positive
x the displayed limit gives G(0)=lim F(x)/x^m=0, a contradiction.
If instead the zero has infinite order, Theorem 7.4 applies on the
connected open strip S and makes F identically zero on S, contradicting
F(a)=1. These cases exhaust holomorphic zeros, and an initially
identically-zero F is already excluded by F(a)=1. This proves the claim.

The application scope is [Carneiro--Milinovich, arXiv:2403.17803v1,
Section 2.2, Lemma 4, printed p.5](https://arxiv.org/html/2403.17803v1#S2.SS2),
26 March 2024: its test must be analytic throughout the full closed
strip of half-width 1/2+epsilon and have power decay of order 1+delta,
with epsilon,delta>0. Its analytic requirement implies the open-strip
holomorphy excluded above. The explicit formula itself and its decay
hypothesis are not used in the contradiction. No assumptions on Xi,
zero spacing, multiplicity, or off-line zeros enter the proof.

## Mathlib

Full matching coverage and supporting theorem names have not been
checked. Unknown availability is not evidence of absence. The proof
uses the cited classical identity and zero-order theorems and the
displayed elementary asymptotic specialization.
