# C034y: exact prime-exclusion recurrence returns unpaid source covariance

## Hypotheses

Use precisely C034r's real input \(h=-g''+g/4\), full theta kernel
\(\Phi\), \(\psi=C_\Phi h\), weighted space
\(E=L^2(\mathbb R,e^{-y/2}dy)\), and translations
\(T_rf(y)=f(y+r)\). In particular \(\psi\in E\) and
\(\|T_r\|_{E\to E}=e^{r/4}\). Inner products are linear in the
first slot, as in C034u. Write \(Q=\log2\).

Extend the same finite formula to every real \(X>0\):
\[
 u(X)=U_Xh=\sum_{X/2<n\le X}
   \mu(n)n^{-1/2}\log(X/n)T_{\log(n/X)}\psi.
 \tag{1}
\]
All indices are positive integers. Thus \(u(X)=0\) for \(X\le1\),
including \(X=1\), where the possible term has zero logarithmic weight.
For \(p=2,3\), let \(v_p(X)=V_{(p,X)}\) be (1) restricted to
\(p\mid n\), and let \(f_p(X)\) be (1) restricted to \(p\nmid n\).
Let \(f_6(X)\) be the restriction \((n,6)=1\), and \(w_6(X)\)
the restriction \(6\mid n\). These definitions also vanish for
\(X\le1\). No replacement coefficients, zero premise or RH premise
are imposed.

## Conclusion

For every real \(X>0\) and \(p=2,3\),
\[
 v_p(X)=-p^{-1/2}u(X/p)+p^{-1/2}v_p(X/p)
       =-\sum_{j\ge1}p^{-j/2}u(X/p^j).
 \tag{2}
\]
The sum is finite after its zero terms are removed. Both prime
recurrences have the same sign in front of every full-source term.
Consequently the exact target covariance is
\[
 B(X):=\langle v_2(X),v_3(X)\rangle_E
 =\sum_{j,k\ge1}2^{-j/2}3^{-k/2}
       \langle u(X/2^j),u(X/3^k)\rangle_E .
 \tag{3}
\]
This is a finite identity for the actual coefficients, not a positivity
assertion about its summands.

The common \(6\)-divisible sector is retained exactly:
\[
 \begin{split}
 w_6(X)&=6^{-1/2}f_6(X/6),\\
 v_2(X)&=-2^{-1/2}f_6(X/2)+w_6(X),\\
 v_3(X)&=-3^{-1/2}f_6(X/3)+w_6(X),\\
 u(X)&=f_6(X)-2^{-1/2}f_6(X/2)-3^{-1/2}f_6(X/3)
                         +6^{-1/2}f_6(X/6).
 \end{split}                                                    \tag{4}
\]

For any \(a\ge0\), the **additional assumption**
\(\|u(Y)\|_E\le M_aY^a\) for every \(Y\ge1\) implies only the
following displayed bound from the absolute use of (3):
\[
 |B(X)|\le
 \frac{M_a^2 X^{2a}}
 {(2^{a+1/2}-1)(3^{a+1/2}-1)}\qquad(X\ge1).
 \tag{5}
\]
Here “only” describes this inequality's exponent, not the optimal
behavior of the actual source. To obtain the nominated
\(O_{h,\varepsilon}(X^{1/2+\varepsilon})\) this way requires an
unpaid full-source bound with \(a=1/4+\varepsilon/2\), or a direct
bound for the signed cross-source sum in (3). Neither is proved.

This diagnoses the failure of the proposed recurrence-only contraction
test. It does not refute the covariance target, rule out other uses of
prime conditioning, prove a new zeta estimate, or sign the actual-Xi
algebraic mixed form. The result has not received a separate audit.

## Proof

### Source scope and purpose

Assessment2106 and source-notes2107 already cover this exact finite
prime-exclusion diagnostic. The inspected comparisons are Bourgain,
Sarnak and Ziegler, *Disjointness of Mobius from Horocycle Flows*,
[author PDF, Theorem 2, (1.3)-(1.4)](https://publications.ias.edu/sites/default/files/disjointness%20b-s-z%20oct.pdf),
and Matomaki and Radziwill, *Multiplicative functions in short intervals*,
Annals of Mathematics **183** (2016), 1015-1056,
[Lemma 12 and its complete proof, pp. 1032-1033](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf),
DOI 10.4007/annals.2016.183.3.6. Neither theorem is invoked as a
covariance estimate: the former assumes prime-dilate correlations;
the latter retains square-prime corrections and a prime-free remainder.

The calculation below is an elementary specialization of Mobius
prime exclusion to the actual weighted finite vectors. It is written
out to verify the endpoints, absence of an extra translation, common
divisibility and recurrence signs. It is not presented as mathematics
beyond the literature checked or as a reproof of either cited theorem.

### Exact rescaling and finite termination

The defining rule for the Mobius function gives
\[
 \mu(pm)=-\mu(m)\mathbf1_{p\nmid m}.
 \tag{6}
\]
Indeed, if \(p\mid m\), the left side is zero because \(p^2\mid pm\).
If \(p\nmid m\), adjoining the distinct prime changes the sign when
\(m\) is squarefree, and both sides vanish when it is not squarefree.
Thus no complete multiplicativity is assumed.

In the sum for \(v_p(X)\), set \(n=pm\). The endpoints become
\(X/(2p)<m\le X/p\), with exactly the same strict/inclusive
convention, and
\[
 \log(X/(pm))=\log((X/p)/m),\qquad
 T_{\log(pm/X)}=T_{\log(m/(X/p))},\qquad
 (pm)^{-1/2}=p^{-1/2}m^{-1/2}.
\]
Consequently \(v_p(X)=-p^{-1/2}f_p(X/p)\).
Since \(f_p=u-v_p\) at every scale, this proves the first part of (2).
No endpoint rounding, boundary deletion or spatial translation was used.

Iterating it \(N\) times gives
\[
 v_p(X)=-\sum_{j=1}^Np^{-j/2}u(X/p^j)
                         +p^{-N/2}v_p(X/p^N).
\]
Choose \(N\) with \(X/p^N\le1\). The remainder then vanishes
identically, including the equality case. All later terms vanish too.
Expanding the inner product of the two resulting finite sums proves
(3); their two minus signs cancel. No infinite-limit interchange is
involved.

### Common divisibility and the complete square

For the \(6\)-divisible terms, \(n=6m\) gives
\(\mu(6m)=\mu(m)\mathbf1_{(m,6)=1}\), by exactly the squarefree
cases in (6). The same endpoint and weight calculation gives the first
line of (4). The terms with \(2\mid n,3\nmid n\) are
\(-2^{-1/2}f_6(X/2)\): terms with \(2\mid m\) vanish, while
\(3\mid m\) are excluded. Interchanging 2 and 3 gives the remaining
single-prime sector. These four disjoint divisibility sectors sum to
\(u(X)\), proving every line of (4).

For another check, define \((D_pf)(X)=p^{-1/2}f(X/p)\) on these
vector-valued scale functions. Equation (4) says
\(u=(I-D_2)(I-D_3)f_6\). The dilations commute, and their inverses
on functions vanishing for \(X\le1\) are pointwise finite geometric
sums. Hence
\[
 f_6(X)=\sum_{j,k\ge0}2^{-j/2}3^{-k/2}
                         u(X/(2^j3^k)).                         \tag{7}
\]
For each \(X\), only pairs with \(2^j3^k<X\) can contribute.
This verifies consistency with (2), without dropping the common sector.

In particular, with \(a_2(X)=-2^{-1/2}f_6(X/2)\) and
\(a_3(X)=-3^{-1/2}f_6(X/3)\),
\[
 B(X)=\langle a_2,a_3\rangle_E+\langle a_2,w_6\rangle_E
          +\langle w_6,a_3\rangle_E+\|w_6\|_E^2.               \tag{8}
\]
All vectors on the right are evaluated at \(X\). The two single-sector
cross terms and the common-sector square remain present. The covariance
also agrees directly with C034u section 1's finite-square formula:
\[
 B(X)=X^{-1/2}
 \sum_{\substack{X/2<n,k\le X\\2\mid n,\ 3\mid k}}
 \frac{\mu(n)\mu(k)}{(nk)^{1/4}}
 \log(X/n)\log(X/k)C_h(\log(k/n)),                             \tag{9}
\]
where \(C_h(r)=\int J\psi(y)\overline{J\psi(y+r)}\,dy\).
In particular the \(n=k,6\mid n\) terms have not been subtracted.
There is no assumed sign for the off-diagonal terms.

### The cross-energy equation is forced by an unpaid source

Set \(G(Y,Z)=\langle u(Y),u(Z)\rangle_E\) and
\(K(Y,Z)=\langle v_2(Y),v_3(Z)\rangle_E\). Applying the two
first-order identities in (2) in their respective slots gives
\[
 \begin{split}
 K(Y,Z)&-2^{-1/2}K(Y/2,Z)-3^{-1/2}K(Y,Z/3)\\
       &+6^{-1/2}K(Y/2,Z/3)
        =6^{-1/2}G(Y/2,Z/3).                                  \tag{10}
 \end{split}
\]
The diagonal \(K(X,X)=B(X)\) therefore does not obey a closed
smaller-scale recurrence in \(B\). The forcing term is the full
source cross covariance. Inverting the finite difference operators
returns exactly (3), whose coefficients are all positive. No sign
estimate on \(G\), or cancellation among its values, has been supplied
by prime exclusion.

If the additional bound preceding (5) holds, Cauchy-Schwarz gives
\(|G(Y,Z)|\le M_a^2(YZ)^a\) for \(Y,Z\ge1\); it is zero if
either scale is at most 1. Taking absolute values in the finite sum
(3), and bounding by positive geometric series, gives
\[
 |B(X)|\le M_a^2X^{2a}
 \left(\sum_{j\ge1}2^{-j(a+1/2)}\right)
 \left(\sum_{k\ge1}3^{-k(a+1/2)}\right),
\]
which is (5). If the assumed source bound is only eventual, it extends
to \(Y\ge1\) by increasing \(M_a\): (1) is uniformly bounded on
every compact scale interval by its finite-sum triangle bound.

For an explicit unconditional comparison, the elementary estimate
\(\|u(Y)\|_E\le2Q\|\psi\|_E\sqrt Y\) follows from
\(\log(Y/n)\le Q\), \(\|T_{\log(n/Y)}\|\le1\), and
\(\sum_{n\le Y}n^{-1/2}\le2\sqrt Y\).
Taking \(a=1/2\) in (5) yields
\[
 |B(X)|\le2Q^2\|\psi\|_E^2X.                                \tag{11}
\]
This displayed elementary upper misses \(X^{1/2+\varepsilon}\)
for \(0<\varepsilon<1/2\). It is not claimed to be the strongest
available zeta-based upper: C034v(26)'s stronger envelope and other
recorded analytic inputs are not invalidated. The relevant conclusion
is that (5) preserves any input power exponent rather than improving it.

Thus the approved test meets its stated stop condition: (10) leaves
full cross-source forcing unpaid, and the displayed closure (5)
requires the full-source power estimate it was meant to avoid.
This is a local negative result about this proposed mechanism, not
a lower bound contradicting the nominated actual covariance upper.
Other sectors, recombination, cumulative/subpower control, completion
transfer and actual-Xi mixed signs all remain unresolved.

## Mathlib

Full matching coverage for these exact weighted finite recurrences and
the covariance diagnostic has not been checked. Supporting ingredients
are the defining squarefree rule for the Mobius function, finite sum
reindexing, Hilbert-space Cauchy-Schwarz and a geometric series. No
formal verification or absence from Mathlib is claimed.
