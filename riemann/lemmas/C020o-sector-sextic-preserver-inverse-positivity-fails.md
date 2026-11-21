# An admissible sextic preserver need not have a positive inverse

## Hypotheses

Let V_6 be the real polynomials of degree at most six, D=d/dx, and
\[
 q(z)=1+z+\frac5{18}z^2,\qquad T=q(D):V_6\longrightarrow V_6.
\]
Real-rooted sextics below have degree exactly six, with arbitrary
nonzero real leading coefficient; roots are counted with multiplicity.

## Conclusion

The rational symbol q has q(0)=1 and nonnegative coefficients. Both
its zeros satisfy Re z<0 and |Im z|=-Re z/3. The operator T preserves
real-rootedness of every real-rooted sextic, including repeated roots.
Nevertheless its inverse on V_6 does not preserve strict positivity on
the real axis. Explicitly, put
\[
 h(x)=393x^3+1782x^2+2084x+558,\qquad F(x)=h(x)^2+1.
\]
Then F(x)>=1 for every real x, but
\[
 (T^{-1}F)(0)=-\frac{162175}{3}<0.
\]

This is a failure of the proposed sextic extension of the inverse-
positivity method in C020n, not an answer to the approved (2,4)
nonreal-root-count test. In particular F has no real zeros, so the
displayed pair cannot be that requested witness. No claim that the
requested count increase exists, or is impossible, follows here.
Independent critical audit of this local obstruction remains pending.

## Proof

**Sector and preservation.** The roots of q are exactly
\[
 -\frac95+\frac35 i,\qquad -\frac95-\frac35 i.
\]
Their sum is -18/5 and product 18/5, which, with leading coefficient
5/18, gives q; their real parts are strictly negative and their ratio
|Im z|/(-Re z) is 1/3. All coefficient restrictions are immediate.

Use Walsh's convolution theorem as stated in Thomas Craven and George
Csordas, *Location of zeros. Part I: Real polynomials and entire
functions*, Illinois J. Math. **27**(2) (1983), 244--278,
Theorem 3.3 and remarks (1),(3), printed pp.257--258,
[primary scan](https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf).
The statement, closed-half-plane case and real-rooted consequence were
inspected in the reused assessment1468/review1469; no damaged numerical
sector formula is imported. In the required normalization, for
g(x)=sum_(j=0)^n b_j x^j, the convolution is
\[
 W(f,g)=\sum_{k=0}^n (n-k)!b_{n-k}f^{(k)}.
\]
If f and g have degree n and all roots real, W(f,g) is real rooted:
apply Walsh to each of the closed upper and lower half-planes
containing the zeros of f. Each translate by a real zero of g is the
same half-plane. The two conclusions place all zeros on the real
axis. There is no simplicity hypothesis, and the leading coefficient
is n! times the product of the two leading coefficients, hence nonzero.
This is a specialization of the cited theorem, not a reproof of it.

Here n=6 and
\[
 g(x)=Tx^6=x^6+6x^5+\frac{25}{3}x^4
       =x^4\left(x^2+6x+\frac{25}{3}\right).
\]
Its four zeros at zero and its two zeros -3+sqrt(2/3) and
-3-sqrt(2/3) are all real. Indeed the quadratic discriminant is
36-100/3=8/3>0. The nonzero coefficients b_6=1, b_5=6 and
b_4=25/3 give
\[
 \frac{W(f,g)}{6!}
 =f+\frac{5!\,6}{6!}f'
    +\frac{4!\,(25/3)}{6!}f''
 =f+f'+\frac5{18}f''=Tf.
\]
Walsh therefore applies to every real-rooted sextic, including the
repeated roots of either polynomial and either sign of the leading
coefficient. Differentiation lowers degree, so T retains the original
degree and leading coefficient.

**Finite inverse and exact positive input.** On V_6 one has D^7=0.
The constant coefficient of q is one, so its positive-order part is
nilpotent and the finite geometric series gives a two-sided inverse.
Explicit multiplication modulo D^7 gives
\[
 R=T^{-1}=1-D+\frac{13}{18}D^2-\frac49D^3
       +\frac{79}{324}D^4-\frac{13}{108}D^5
       +\frac{307}{5832}D^6.
\]
There is no infinite series or limit interchange. To check the claimed
evaluation without an inference from a determinant, define
\[
 P(x)=154449x^6+473958x^5+1156683x^4+606132x^3
          +657762x^2-\frac{162175}{3}.
\]
Direct differentiation gives the following complete coefficient
identities, in ascending powers of x:
\[
\begin{split}
 TP&=(311365,2325744,6331768,7865964,4813548,1400652,154449),\\
 h^2+1&=(311365,2325744,6331768,7865964,4813548,1400652,154449).
\end{split}
\]
For example the constant coefficient of TP is
-162175/3+(5/18)(2)(657762)=311365=558^2+1;
the other coefficients follow from
[x^j]TP=P_j+(j+1)P_(j+1)+(5/18)(j+2)(j+1)P_(j+2),
with coefficients beyond degree six zero. Thus TP=F exactly and,
by invertibility, RF=P. Since F=h^2+1>=1 everywhere and P(0)<0,
strict inverse positivity fails as claimed.

**Relation to the attempted method.** The normalized inverse moments
m_k=k!r_k for R=sum r_k D^k are
\[
 (1,-1,13/9,-8/3,158/27,-130/9,3070/81).
\]
For h=sum_(i=0)^3 c_i x^i, one has
R(h^2)(0)=sum_(i,j=0)^3 c_i c_j m_(i+j), by finite differentiation.
The moment matrix has leading principal minors
\[
 1,\quad\frac49,\quad\frac{131}{729},\quad-\frac{1238}{19683}.
\]
Thus the degree-four positive matrix does not extend to a positive
degree-six matrix. The explicit vector (558,2084,1782,393) gives
R(h^2)(0)=-162178/3, and adding one gives the evaluation above.
The direct polynomial identity already proves the obstruction; these
moments explain how the failed extension led to its certificate.

**Verification and limitations.** Run
`python3 scripts/quartic-differential/sector-sextic-inverse-obstruction-1470.py`.
The full certificate is
`scripts/quartic-differential/sector-sextic-inverse-obstruction-1470.json`.
It checks the finite inverse, complete moments and matrix, determinants,
the displayed polynomials and their image identity, and all seven
monomial-basis instances of the Walsh normalization. All algebra flags
pass. The actual lower bound for F is 1; the inverse value -162175/3
fails the required positive threshold. The preservation discriminant
is 8/3 against a required nonnegative value. The complete relevant
coefficient/matrix/check fields were inspected. The script does not
replace Walsh or certify the desired (2,4) count test.

The approved EXPLORE assessment1468 permits the fixed sextic attempt.
This obstruction arose within its inverse-method test. Walsh is a known
import; the explicit finite obstruction was not supplied by the
inspected sources. No originality claim follows. C020n and C020m are
comparisons, not mathematical premises. Actual-Xi factor applicability,
exceptional-divisor bounds, unbounded degrees, signs, initialization and
overlap remain unproved. The original count target is unresolved, and
there is no RH candidate.

## Mathlib

Full matching coverage of this finite obstruction and its sector-
restricted preservation statement has not been checked. The certificate
uses rational polynomial identities and the cited Walsh theorem; it is
not a Lean proof. Unknown coverage is not evidence of absence.
