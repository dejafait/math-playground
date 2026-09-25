# L006 — Sparse affine lifting gives the sharp small-radius error

## Hypotheses

Let F be a finite field of order q, let I have cardinality n, and let
the evaluation points \(x_i\in F\), \(i\in I\), be pairwise distinct.
Let r,k be integers with
\[
 1\le r,\qquad 1\le k,\qquad 3r\le n-k,
\]
and set
\[
 C=\{(p(x_i))_{i\in I}:p\in F[X],\ \deg p<k\}.
\]
Use the error \(E_C\) from
[the pinned affine-line model](../foundations/02-pinned-affine-line-model.md).
Suppose \(r/n\le\delta<(r+1)/n\), and let \(0<\varepsilon\le1\).
No smoothness or extra field-size assumption is imposed.

## Conclusion

The error on this cell is exactly
\[
 E_C(\delta)=\frac{r+1}{q}.
\]
It is safe at budget epsilon if and only if
\(q\ge(r+1)/\varepsilon\). At the prescribed budget \(2^{-128}\),
this condition is \(q\ge(r+1)2^{128}\) for the given code's field.
In particular,
\[
 E_C(\delta)=3/q\quad\text{if}\quad
 1\le k\le n-6,\qquad 2/n\le\delta<3/n.
\]
This applies to all four listed rates on any smooth domain of length at
least 16. It does not determine later cells, the general maximal safe
radius, or the correspondence with the unread ABF26 event.

## Proof

Every nonzero codeword has weight at least
\(d=n-k+1>3r\), since a nonzero polynomial of degree less than k has
at most k-1 roots. Here weight means the number of nonzero coordinates;
the polynomial root bound follows by division by each distinct root.
The radius hypothesis gives
\(n-r-1<n(1-\delta)\le n-r\). Thus the admissible supports are
exactly all subsets S of size at least n-r, including the full support.

Fix a,b. On any support where \((a+\gamma b)|_S\in C|_S\), failure
of either input is equivalent to \(b|_S\notin C|_S\). Indeed, if b
were a code restriction then subtracting \(\gamma b|_S\) would show
the same for a. The reverse implication is part of the disjunction.
Let \(\Gamma\subseteq F\) be the bad challenge set for this pair.
If it has at most one member, the desired upper bound is immediate.

Otherwise choose distinct \(\gamma_0,\gamma_1\in\Gamma\). For
every \(\gamma\in\Gamma\), choose one witnessing support \(S_\gamma\)
and codeword \(c_\gamma\) agreeing with \(a+\gamma b\) there. Write
\[
 e_\gamma=a+\gamma b-c_\gamma.
\]
The support of \(e_\gamma\) lies in \(I\setminus S_\gamma\), so its
weight is at most r. Define vectors
\[
 v=\frac{e_{\gamma_1}-e_{\gamma_0}}{\gamma_1-\gamma_0},
 \qquad u=e_{\gamma_0}-\gamma_0v,
 \qquad e(\gamma)=u+\gamma v.
\]
Subtracting the equations at the two chosen parameters shows
\(b-v\in C\), and then \(a-u\in C\). Hence replacing a,b by u,v
preserves the original event on every support: each input and every
combination changes by a codeword.

For every bad gamma, the vector
\[
 e_\gamma-e(\gamma)
   =(a-u)+\gamma(b-v)-c_\gamma
\]
belongs to C. Its support is contained in the union of the supports of
\(e_\gamma,e_{\gamma_0},e_{\gamma_1}\), of total size at most 3r.
The weight bound forces this codeword to vanish. Consequently
\[
 e_\gamma=e(\gamma)\quad\text{for every }\gamma\in\Gamma.       \tag{1}
\]
This is the compatibility between challenges that certificate counting alone
does not supply. It allows the chosen codewords and supports to depend on
gamma; no common codeword was assumed.

Let
\[
 J=\{i\in I:(u_i,v_i)\ne(0,0)\},\qquad t=|J|.
\]
Both u and v are supported on the union of the two initial error supports,
so t<=2r. For i in J, the scalar affine polynomial
\(u_i+Xv_i\) is nonzero and has at most one root in F. This includes
nonzero constant coordinates, which have no root.

If t>r, equation (1) and the weight bound on \(e_\gamma\) imply
that each bad gamma is a root of at least t-r of these t scalar polynomials.
Counting pairs \((\gamma,i)\) with \(\gamma\in\Gamma\), \(i\in J\),
and \(u_i+\gamma v_i=0\), gives
\[
 |\Gamma|(t-r)\le t,
 \qquad
 |\Gamma|\le\left\lfloor\frac{t}{t-r}\right\rfloor\le r+1.
\]
The last inequality follows from
\(t/(t-r)=1+r/(t-r)\) and the positive integer t-r>=1.

If t<=r, weight alone imposes no useful restriction: every e(gamma) has
weight at most r. Use the same-support failure instead. For a bad gamma,
\(v|_{S_\gamma}\notin C|_{S_\gamma}\), because \(b-v\in C\).
In particular this restriction is not zero. Choose an index
\(i\in S_\gamma\) with \(v_i\ne0\). Equation (1) and the definition
of the error give \(u_i+\gamma v_i=e_{\gamma,i}=0\).
Thus each bad gamma is a root of one of at most t nonconstant coordinate
polynomials, each with just one root. Therefore
\[
 |\Gamma|\le t\le r.
\]
This also shows why a line lying entirely within an r-coordinate error
space does not make every parameter bad. Zero quotient directions have
no bad challenges by the same failure condition; neither they nor lines
through a codeword were excluded from the argument.

The two cases prove \(|\Gamma|\le r+1\) uniformly for every a,b.

For attainment, note that \(q\ge n\ge3r+1\), so there are r+1 distinct
coordinates \(i_0,\ldots,i_r\) and r+1 distinct field elements
\(\alpha_0,\ldots,\alpha_r\). Define a,b by
\[
 a_{i_j}=-\alpha_j,\qquad b_{i_j}=1\quad(0\le j\le r),
 \qquad a_i=b_i=0\quad(i\notin\{i_0,\ldots,i_r\}).
\]
At \(\gamma=\alpha_j\), the combination is zero exactly at i_j
among these r+1 coordinates, and zero everywhere outside them. It agrees
with the zero codeword on
\[
 S_j=I\setminus\{i_h:h\ne j\},\qquad |S_j|=n-r.
\]
The direction cannot agree with a codeword on S_j. If c were such a
codeword, it would vanish outside \(\{i_0,\ldots,i_r\}\), hence have
weight at most r+1<d; but \(c_{i_j}=b_{i_j}=1\), a contradiction.
Thus each of the r+1 distinct alpha_j is bad on its stated support.
Together with the upper bound, this proves the exact error (r+1)/q.
The safety equivalence follows by multiplying by q/epsilon>0.

For r=2, the hypotheses are precisely k<=n-6. If n>=16 and k/n is
one of 1/2,1/4,1/8,1/16, then k<=n/2<=n-6, as required. The proof
also recovers the r=1 formula in L005; it does not use that result.

For comparison, L004 at length 16 and support cutoff 14 permits
\[
 \left\lfloor\frac{\binom{16}{k+1}}{\binom{13}{k}}\right\rfloor
   =8,6,7,9\quad\text{for }k=8,4,2,1,
\]
whereas the exact count here is three. For length 256 and k=128, the
present theorem determines every cell with 1<=r<=42. Its last such cell
ends at the excluded endpoint 43/256. At q=257^32 all these cells meet
the actual 2^-128 budget, but this does not extend L004's larger sufficient
interval delta<90/256. Sharp counts on early cells and a sufficient bound
on later cells answer different parts of the remaining threshold question.

The hypothesis 3r<=n-k is the sufficient condition used in the lifting
argument, not a claimed optimal condition. Without a distance restriction,
even the two-omission formula can fail: over F_7 with evaluation points
0,1,2,3,4 and k=1, take a=(0,0,1,1,1), b=(0,0,1,2,3).
At gamma=0 the last three coordinates agree with the constant 1 and their
direction values 1,2,3 are not constant. At gamma=6,3,2 respectively,
the first two coordinates and respectively coordinate 2,3,4 agree with
the constant 0, while their direction values are 0,0,1; 0,0,2; and 0,0,3.
Thus four distinct parameters are bad at cutoff three. This example has
n-k=4<6 and does not determine whether the sufficient condition can be
weakened to n-k=5.

The auxiliary command `python3 scripts/sparse-affine-lifting/check.py`
tests the original punctured-code event, including characteristic two,
attainment, small active supports, and the excluded example. The uniform
result follows from the proof above, not from the finite checks.

## Mathlib

Coverage of the full statement and of supporting sparse-lifting and finite
counting results in Mathlib: **not checked**. No matching library theorem or
Lean verification is claimed. The minimum-weight bound and affine-lifting
argument are proved here from elementary linear algebra and the polynomial
root bound.

The previously read ArkLib declarations
[`CoreDefinitions.IsMCA` and `CoreDefinitions.mcaError`](https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/Data/CodingTheory/ProximityGap/ProximityGenerators.lean#L98)
support the frozen event definition. ArkLib is separate from Mathlib; these
definitions do not match the sharp-error theorem or certify its correspondence
with the current ABF26 challenge.
