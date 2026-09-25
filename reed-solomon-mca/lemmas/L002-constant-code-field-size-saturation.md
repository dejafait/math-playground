# L002 — Constant-code error saturates below the budget over large fields

## Hypotheses

Let \(F\) be a finite field of order \(q\), let \(I\) have cardinality
\(n\ge2\), and let \(C=\{(c)_{i\in I}:c\in F\}\). Use the exact
support-event error \(E_C\) from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
Let \(0<\varepsilon\le1\).

## Conclusion

For every \(\delta\in[0,1]\),
\[
 E_C(\delta)\le \min\left\{1,\frac{\binom n2}{q}\right\}.
\]
In particular, if \(q\ge\binom n2/\varepsilon\), every radius is safe
and the largest safe real radius is \(1\).

More precisely, fix \(a,b\in F^I\). For each unordered pair \(\{i,j\}\)
with \(b_i\ne b_j\), put
\[
 \gamma_{ij}=\frac{a_j-a_i}{b_i-b_j},\qquad
 B(a,b)=\{\gamma_{ij}:\{i,j\}\subseteq I,\ b_i\ne b_j\}.
\]
The value is independent of the ordering of \(i,j\). Every bad challenge
for this pair \((a,b)\) belongs to \(B(a,b)\); for
\(1-2/n\le\delta\le1\), the bad-challenge set is exactly \(B(a,b)\).

For the listed rate \(1/16\), there is a smooth length-16 RS code of
dimension one over the field of order \(5^{60}\) for which all real radii
are safe at error \(2^{-128}\). More generally, every length-16 constant
code over any field of order \(q\ge120\cdot2^{128}\) has this property.
These are assertions about the frozen event, not an identification with the
unread current ABF26 definition or its field-size hypothesis.

## Proof

Suppose \(\gamma\) is bad for \((a,b)\), witnessed by \(S\subseteq I\).
The restriction \((a+\gamma b)|_S\) is constant, while at least one of
\(a|_S,b|_S\) is not constant. In fact \(b|_S\) cannot be constant:
if it were, subtracting \(\gamma b|_S\) from the constant combination
would make \(a|_S\) constant as well. Thus there are distinct \(i,j\in S\)
with \(b_i\ne b_j\). Equality of the combination at these coordinates
gives
\[
 a_i+\gamma b_i=a_j+\gamma b_j,
 \qquad \gamma=\frac{a_j-a_i}{b_i-b_j}.
\]
Consequently every bad challenge lies in \(B(a,b)\). There are at most
\(\binom n2\) unordered pairs, each supplying one value. The bad-challenge
count is therefore at most \(\min\{q,\binom n2\}\). Dividing by \(q\)
and maximizing over all \(a,b\) proves the bound. The support may depend
on \(\gamma\); the containment was proved after an arbitrary witness was
chosen and does not interchange those quantifiers.

Conversely, let \(\gamma=\gamma_{ij}\in B(a,b)\). On \(S=\{i,j\}\)
the combination is constant, while \(b|_S\) is not. If
\(\delta\ge1-2/n\), then \(|S|=2\ge n(1-\delta)\), so this pair
is an admissible bad support. This proves the exact terminal-radius event.
It does not assert that all \(\binom n2\) pair values are distinct or
that the upper bound is attained.

Under \(q\ge\binom n2/\varepsilon\), the bound gives
\(E_C(\delta)\le\varepsilon\) at every \(\delta\in[0,1]\), including
\(1\). Hence the safe set is all of \([0,1]\) and has largest member
\(1\). No radius-cell theorem is needed for this conclusion.

For the explicit smooth example, the finite-field existence theorem supplies
\(F\) with \(q=5^{60}\). As \(5^4\equiv1\pmod {16}\) and
\(4\mid60\), cyclicity of \(F^\times\) gives a subgroup \(H\) of
order 16. Thus \(\mathrm{RS}[F,H,1]\) is the length-16 constant code,
with a smooth domain and rate \(1/16\). Finally,
\[
 5^7=78125>65536=2^{16},\qquad
 5^{60}=625(5^7)^8>625\cdot2^{128}>120\cdot2^{128}.
\]
Since \(\binom{16}{2}=120\), the preceding bound proves
\(E_C(\delta)<2^{-128}\) for every radius.

This is a sufficient field-size bound. It neither locates the first unsafe
grid index at smaller fields nor gives the sharp threshold for general RS
dimension. In particular, a failure of maximum attainment at one smaller
field cannot contradict an eventual assertion for fixed length as the field
size grows. Reproduction of the integer comparisons is included in
`python3 scripts/endpoint-audit/check.py`; the proof does not rely on a
finite enumeration of fields, words, or supports.

## Mathlib

Full result and supporting counting theorems in Mathlib: **not checked**.
No matching formal theorem or Lean verification is claimed. The finite-field
existence and cyclic multiplicative-group facts are the standard algebra
inputs stated in the model foundation. The separate ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
were checked as sources for the event definitions, not as coverage of this
bound or certification of the current ABF26 challenge.
