# C006a — A fixed-slack list certificate in large characteristic

## Hypotheses

Fix 0<gamma<1 and choose r,mu,n_0,B_gamma as in L006. Let F be a
finite field with q elements and characteristic

\[
 p>\max\{k-1,B_\gamma\}.
\]

Let n>=n_0, let x_1,...,x_n be distinct elements of F, and let
1<=k<=(1-gamma)n. Set A=k+ceil(gamma n), so A<=n. Use the
[pinned column-Hamming model](../foundations/02-pinned-list-model.md)
with interleaving width m>=1 and target constant 0<epsilon*<1.
Define

\[
 \begin{split}
 d&=k-1,& D&=\mu n,& B&=B_\gamma,\\
 N&=D+(B-1)d+1,& L&=\max(0,2d-1),\\
 E&=(D+B)(1+BL),&T&=(D+B)L+1,\\
 \Delta&=B^2N(ET)^r,&\beta&=\Delta\sum_{a=0}^r n^a.
 \end{split} \tag{1}
\]

## Conclusion

For every m-row received word, the number of codewords with at least
A simultaneous column agreements is at most beta^m. In particular,

\[
 B_m((n-A)/n)\le\beta^m,
 \qquad
 q\ge(\varepsilon^*)^{-1}\beta^m
 \ \Longrightarrow\ B_m((n-A)/n)\le\varepsilon^*q. \tag{2}
\]

The same list bound holds at real radius 1-k/n-gamma. For fixed gamma
and m, beta^m=O_gamma,m(n^(m(5r+1))), independently of q. This is a
sufficient field-size condition for one radius, not the largest safe
grid index or a resolution under only epsilon* q>=1.

## Proof

Apply L006 separately to each scalar row. It produces a nonzero Q with
order r, total Y-degree at most B, and X-degree at most D, containing
that entire scalar list. These bounds are the same for every received
row, although the polynomial Q can differ.

If d>=r, extend scalars to an algebraic closure and apply L005. Its
characteristic and order hypotheses hold, and its constants are exactly
those in (1). It gives a cover of dimension at most r and summed
cumulative degree at most Delta of every scalar list.

If d<r, the ambient coefficient space has dimension d+1=k<=r and
degree one. It itself is an admissible cover; no use of L005 with
r>d is made. The value Delta in (1) is at least one, so the same cover
bounds apply. This case also avoids specializing away higher derivative
variables of Q, which could turn Q into the zero polynomial.

L002 applies with A>=k, the common dimension bound r, and the common
degree bound Delta. It gives (2); the interleaved list injects into the
product of its row lists. For the real radius rho=1-k/n-gamma,

\[
 \lfloor n\rho\rfloor=n-k-\lceil\gamma n\rceil=n-A,
\]

so the closed ball is identical to the ball at (n-A)/n.

For completeness, all implied constants can be bounded from (1).
For n>=1 and d<=n,

\[
 N\le(\mu+B)n,\quad
 E\le(\mu+B)(1+2B)n^2,\quad
 T\le[2(\mu+B)+1]n^2.
\]

Together with sum_(a=0)^r n^a<=(r+1)n^r these give

\[
 \beta\le C_\gamma n^{5r+1},\qquad
 C_\gamma=(r+1)B^2(\mu+B)
  \bigl[(\mu+B)(1+2B)(2(\mu+B)+1)\bigr]^r. \tag{3}
\]

This yields the asserted polynomial bound, with no q-dependence hidden
in its constant. The constants can be very large; effectiveness does
not establish a useful certificate for any particular field instance.
Increasing q does not fix a violation of the characteristic hypothesis.
For prime q>=n, that hypothesis holds once n>B_gamma, since k-1<n.

## Mathlib

Full explicit certificate (1)–(3): **not checked** in Mathlib.
Supporting finite products of lists and the floor/ceiling identity:
**not checked** in this step. [TR26-169, Corollary 8.2 and Section 8.4,
printed pp. 31–32](https://eccc.weizmann.ac.il/report/2026/169/download#page=31)
state matching qualitative fixed-interleaving and characteristic
consequences. They are supporting source comparisons, not inputs in
place of the proof here or a citation for these explicit constants.
