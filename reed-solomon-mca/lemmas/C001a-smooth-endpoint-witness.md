# C001a — A smooth RS endpoint witness at error 2^-128

## Hypotheses

Let \(F\) be a field of order \(q=5^{56}\), let \(H\le F^\times\) have
order \(16\), and let
\[
 C=\mathrm{RS}[F,H,1]=\{(c)_{h\in H}:c\in F\}.
\]
Use the support-event error \(E_C\) in
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md),
and put \(\varepsilon^*=2^{-128}\).

## Conclusion

These field and domain choices exist, the domain is smooth, and the code has
the specified rate \(1/16\). Moreover,
\[
 E_C(\delta)=1/q<\varepsilon^*\quad(0\le\delta<1/16),
 \qquad E_C(7/8)\ge6/q>\varepsilon^*.
\]
There is therefore no largest real \(\delta\in[0,1]\) satisfying
\(E_C(\delta)\le\varepsilon^*\). This is a counterexample to existence
of a largest safe real radius **for this frozen model**, not a reviewed
disproof of the grand challenge. Identification with ABF26's current error,
its intended endpoint convention, and its field-size hypothesis remains
unresolved. Nonemptiness of the safe set is established here; no unspecified
"sufficiently large field" condition is thereby certified.

## Proof

By the finite-field existence theorem, \(F\) exists. Since
\(5^4\equiv1\pmod {16}\) and \(4\mid56\), we have \(16\mid q-1\).
Cyclicity of \(F^\times\) gives \(H\). It is a multiplicative subgroup
of power-of-two size, hence a smooth domain. Degree less than one means
constant polynomials, so this is a one-dimensional, length-16 code and its
rate is exactly \(1/16\).

For any proper linear code \(D<F^I\), the full-support bad event has
probability at most \(1/q\) for every pair \((a,b)\). Indeed, if
\(a+s b\in D\) and \(a+t b\in D\) with \(s\ne t\), subtraction
and division by \(s-t\) give \(b\in D\), and then \(a\in D\).
In that case the required failure of an input is false for every challenge.
Thus a pair with any full-support bad challenge has at most one. Conversely,
take \(a=0\) and \(b\notin D\). Exactly \(\gamma=0\) is bad, so
the maximum is \(1/q\). For our code and \(0\le\delta<1/16\), the
size condition forces \(S=H\), proving \(E_C(\delta)=1/q\).
In particular there is a positive safe radius, for example \(1/32\);
the construction does not rely solely on defining the error at zero.

Choose \(\theta\in F\) with no nonzero polynomial relation of degree
at most two over \(\mathbb F_5\). To see that such a choice exists, there
are \(5^3-1=124\) nonzero polynomials of degree at most two; each has at
most two roots. Their root sets contain at most \(248<q\) field elements.
For four distinct coordinates \(h_1,h_2,h_3,h_4\in H\), set
\[
 (x_1,x_2,x_3,x_4)=(0,1,\theta,\theta^2),\qquad
 b(h_i)=x_i,\quad a(h_i)=x_i^2.
\]
Set both words equal to zero on the other twelve coordinates. The four
\(x_i\)'s are distinct. The six sums \(x_i+x_j\), \(i<j\), are
\[
 1,\ \theta,\ \theta^2,\ 1+\theta,\ 1+\theta^2,\
 \theta+\theta^2.
\]
They are distinct: equality between any two would be a nonzero polynomial
relation over \(\mathbb F_5\) of degree at most two, since their coefficient
vectors in \(1,X,X^2\) are distinct modulo five.

For each pair \(i<j\), take
\(\gamma_{ij}=-(x_i+x_j)\) and \(S_{ij}=\{h_i,h_j\}\).
Then
\[
 a(h_i)+\gamma_{ij}b(h_i)=-x_ix_j
 =a(h_j)+\gamma_{ij}b(h_j).
\]
The constant codeword with value \(-x_ix_j\) agrees on \(S_{ij}\).
However, \(b(h_i)\ne b(h_j)\), so no constant codeword agrees with
\(b\) on that same support. At radius \(7/8\) the required support size
is \(16(1-7/8)=2\). All six distinct \(\gamma_{ij}\)'s are bad for
this single pair \((a,b)\), proving \(E_C(7/8)\ge6/q\). Nothing is
assumed about any other bad challenges.

The error comparisons use exact integer inequalities. First,
\(5^7=78125>65536=2^{16}\), so \(q=(5^7)^8>2^{128}\).
Also \(5^8=390625<393216=6\cdot2^{16}\), giving
\[
 \frac{q}{2^{128}}<\left(\frac65\right)^8<6,
\]
where the last inequality is equivalent to
\(6^7=279936<390625=5^8\). Hence
\(1/q<2^{-128}<6/q\).

Monotonicity from L001 gives \(E_C(1)\ge E_C(7/8)>\varepsilon^*\).
Its endpoint conclusion now applies, showing that the nonempty safe set is
\([0,j/16)\) for some \(1\le j\le14\), with no largest real element.
We have neither located \(j\) nor needed to do so to demonstrate this
specification issue. No general optimal-radius formula follows.

The exact arithmetic and polynomial coefficient distinctions can be reproduced
with `python3 scripts/endpoint-audit/check.py`. This is an auxiliary check;
the algebraic argument above, not finite enumeration, proves the statement.

## Mathlib

Coverage of this complete example in Mathlib: **not checked**. No matching
library theorem or Lean verification of this example is claimed. The finite
field and polynomial facts used in the proof are standard algebra; supporting
formal theorem names for them were not looked up. The endpoint component has
the qualified ArkLib coverage recorded in L001.
