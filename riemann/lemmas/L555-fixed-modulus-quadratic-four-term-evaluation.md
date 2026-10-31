# L555 — Fixed-modulus quadratic four-term evaluation

## Hypotheses

Let O=Z[omega], omega=exp(2pi i/3), lambda=1+2omega=i sqrt(3),
q_c=|c|^2, and

\[
 e(z)=\exp(2\pi i\operatorname{Tr}_{\mathbb Q(\omega)/\mathbb Q}(z/\lambda))
     =\exp(4\pi i\operatorname{Im}z/\sqrt3).
\]

The second expression extends e to C. Use dmu=(2/sqrt(3)) dx dy
and the bilinear Fourier kernel e(-zy), without conjugating y.
Fix a finite set S containing the prime ideals above 6. Let c=p or
c=pq, where p,q are primary generators of distinct prime ideals
outside S. Thus c is nonzero and coprime to 2. Every limiting argument
below fixes c first; constants may depend on it.

For these c define H(c)=|c|^(-1) sum_(x mod c) e(x^2/c). Separately,
for every odd u in O define the finite expression

\[
 h(u)=\frac12\sum_{y\bmod2O}e(-uy^2/4).
                                                        \tag{1}
\]

This latter definition is used at the residue-class representatives
lambda and -lambda without treating them as good prime moduli.

## Conclusion

For every c in the stated prime/product domain,

\[
 H(c)=h(c).
                                                        \tag{2}
\]

The function h descends to G=(O/4O)^*/((O/4O)^*)^2. This group has
representatives 1,-1,lambda,-lambda, with h-values 1,1,i,-i.
Writing the classes as (-1)^a lambda^b, with a,b in {0,1}, gives

\[
 R((-1)^a\lambda^b,(-1)^d\lambda^f)
  :=\frac{h((-1)^{a+d}\lambda^{b+f})}
          {h((-1)^a\lambda^b)h((-1)^d\lambda^f)}
   =(-1)^{af+bd+bf}.                                    \tag{3}
\]

Thus R is a symmetric sign-valued bicharacter on G and, for distinct
good p,q, H(pq)/(H(p)H(q))=R([p],[q]). These are exactly the
quadratic evaluations and correction needed in L554's reciprocity
step. The value of R at colliding classes is its finite definition,
not a quotient of residue symbols at shared primes.

This is a reproduction audit of a cited formula, not a new Gauss-sum
evaluation. It supplies no limit uniform in moving c, other finite
Gauss identities, theta/coefficient estimate, arithmetic-uniform
closure, or actual-Xi sign assertion.

## Proof

### Precise imports and audit scope

The evaluated claim is OpenAI, *The Quasi-Riemann Hypothesis*,
30 September 2026, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a,
[pinned TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex),
`lem:quadratic-four-term`, complete statement/proof lines 772–859;
normalizations are 557–566 and the needed prime/product application
is 899–927. The source claims a larger odd-modulus domain. Here we
verify only the requested prime/product domain and the finite table.
Importing the final claimed evaluation would bypass this retained
input audit, so we check its application of standard analytic results.

Import Schwartz Poisson summation in R^2 with the Euclidean kernel
exp(-2pi i x dot xi) from Terence Tao, *245C, Notes 2: The Fourier
transform*, 6 April 2009,
[Exercise 54](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/).
The complete periodization proof in Andrew V. Sutherland, MIT 18.785,
Lecture 17, 8 November 2021,
[Definition 17.4 and Theorem 17.8, PDF pp. 1–3](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec17.pdf),
is a supporting one-dimensional reference; Tao supplies the stated
dimension-two version. Only positive-damping Schwartz functions are
used. No undamped distributional Poisson theorem is imported.

For a complex symmetric matrix with positive definite real part, use
Victor Ivrii, *Partial Differential Equations*,
[Section 5.2.A, Definition 1 and Remark 2, (5.2A.2)–(5.2A.3)](https://www.math.utoronto.ca/ivrii/PDE-textbook/Chapter5/S5.2.A.html).
In dimension two set his kappa=2pi, A=2pi M and frequency k=2pi ell.
His formula becomes

\[
 \int_{\mathbb R^2}e^{-\pi X^TMX-2\pi i\ell^TX}\,dX
   =\det(M^{-1/2})\exp(-\pi\ell^TM^{-1}\ell).           \tag{4}
\]

Matrix powers use the branch off the nonpositive real axis. We verify
that branch for our M below, rather than replace the determinant by
an absolute value for a general complex matrix. These cited analytic
theorems are imports, not reproved here.

### Bilinear lattice and measure

For z=x+it and y=u+iv the real pairing is
B(z,y)=2(xv+tu)/sqrt(3), so e(zy)=exp(2pi i B(z,y)). Its real matrix
is J=(2/sqrt(3))[[0,1],[1,0]]. The basis matrix of O is
A=[[1,-1/2],[0,sqrt(3)/2]], and

\[
 A^TJA=\begin{pmatrix}0&1\\1&-1\end{pmatrix}.
                                                        \tag{5}
\]

The integer matrix (5) is unimodular. Hence the annihilator of O
under B is O. Explicitly, if y=u+v omega with real u,v, then
B(1,y)=v and B(omega,y)=u-v; their integrality is equivalent to
u,v being integers. Also e is one on O. The Euclidean covolume
of O is sqrt(3)/2 and its dmu-covolume is one.

Write F_E for the Euclidean Fourier transform. Then
hat f(y)=(2/sqrt(3)) F_E f(Jy), and the Euclidean dual lattice
is J O. Changing basis in the imported Poisson formula therefore gives

\[
 \sum_{z\in O}f(z)=\sum_{y\in O}\widehat f(y).           \tag{6}
\]

There is no conjugated lattice here. More generally, for nonzero b
in O the B-dual of bO is b^(-1)O, since B(bz,y)=B(z,by), and
the dmu-covolume of bO is q_b. Translation by v gives

\[
 \sum_{z\in v+bO}g(z)=q_b^{-1}
       \sum_{y\in b^{-1}O}e(vy)\widehat g(y).            \tag{7}
\]

All the functions in (6)–(7) below are Schwartz, so both sums are
absolutely convergent for each positive damping parameter.

### The damped transform and its branch

Put rho=|c| and choose theta with c=rho exp(i theta). For epsilon>0,
set f_epsilon(z)=e(z^2/c) exp(-pi epsilon |z|^2). Rotate
z=exp(i theta/2)(s+it) and put y'=exp(i theta/2)y=U+iV. The rotation
has real Jacobian one. In (4) the resulting matrix and frequency are

\[
 k=\frac4{\sqrt3\rho},\quad
 M=\begin{pmatrix}\varepsilon&-ik\\-ik&\varepsilon\end{pmatrix},
 \qquad \ell=\frac2{\sqrt3}\binom{V}{U}.
                                                        \tag{8}
\]

Indeed -pi X^TMX supplies 8pi i st/(sqrt(3)rho), the exponent of
e(z^2/c), and -2pi i ell^T X is the exponent of e(-zy).
For real X, Re(X^TMX)=epsilon |X|^2>0. The real orthogonal
eigenvectors (1,1),(1,-1) have eigenvalues epsilon-ik, epsilon+ik.
Their principal square roots are conjugates with positive real part.
Consequently their product is the positive number
sqrt(epsilon^2+k^2). This determines the determinant factor in (4)
without an additional sign or fourth root of unity.

Set r_epsilon=1+3q_c epsilon^2/16 and D=epsilon^2+k^2
=16r_epsilon/(3q_c). Directly from (8),

\[
 M^{-1}=D^{-1}\begin{pmatrix}\varepsilon&ik\\ik&\varepsilon\end{pmatrix},
 \qquad
 \ell^TM^{-1}\ell=
 \frac4{3D}\{\varepsilon(U^2+V^2)+2ikUV\}.              \tag{9}
\]

The real term in (9) is epsilon q_c |y|^2/(4r_epsilon).
The imaginary exponent -pi(8ik/(3D))UV is
-2pi i rho UV/(sqrt(3)r_epsilon), exactly the exponent of
e(-cy^2/(4r_epsilon)), because cy^2=rho(y')^2.
Finally (2/sqrt(3))/sqrt(D)=rho/(2sqrt(r_epsilon)). Thus

\[
 \widehat f_\varepsilon(y)=
 \frac{\rho}{2\sqrt{r_\varepsilon}}
 \exp\left(-\frac{\pi\varepsilon q_c|y|^2}{4r_\varepsilon}\right)
 e\left(-\frac{cy^2}{4r_\varepsilon}\right).             \tag{10}
\]

Changing theta by 2pi negates both real coordinates and the frequency,
so leaves (9)–(10) unchanged. No angular branch choice affects (10).

### Coset Gaussian means

Let I_epsilon=2/(sqrt(3)epsilon). For fixed a>0 the transform of
g(z)=exp(-pi a epsilon |z|^2), in the same convention, is

\[
 \widehat g(y)=\frac{I_\varepsilon}{a}
        \exp\left(-\frac{4\pi|y|^2}{3a\varepsilon}\right).
\]

Substitute this in (7). The zero dual vector contributes 1/(a q_b)
after division by I_epsilon. For the other vectors of the fixed
lattice b^(-1)O, let d_b>0 be their minimum nonzero length. For
0<epsilon<=1, the sum of their absolute contributions is bounded by

\[
 \exp\left(-\frac{2\pi d_b^2}{3a\varepsilon}\right)
       \sum_{y\in b^{-1}O}\exp\left(-\frac{2\pi|y|^2}{3a}\right).
\]

The final Gaussian lattice sum is finite. This proves, with b,a,v
fixed, the full limit

\[
 I_\varepsilon^{-1}\sum_{z\in v+bO}
       e^{-\pi a\varepsilon|z|^2}\longrightarrow\frac1{a q_b}.
                                                        \tag{11}
\]

### Normalized boundary limit and every replacement error

For each fixed positive B and j=0,1, lattice counting gives

\[
 \sum_{y\in O}|y|^{2j}e^{-B\varepsilon|y|^2}
       =O_B(\varepsilon^{-j-1})\quad(0<\varepsilon\le1), \tag{12}
\]

where for j=0 the weight is one also at zero. To justify the bound,
place pairwise disjoint disks of radius 1/3 at lattice points. Those
with n<=|y|<n+1 lie in an annulus of area O(n+1); hence their number
is O(n+1). Summing (n+1)^(2j+1) exp(-B epsilon n^2) over n>=0,
or comparing it with its rescaled Gaussian integral, gives (12).

For sufficiently small epsilon depending on c, 1<=r_epsilon<=2
and r_epsilon-1=O_c(epsilon^2). Put A=q_c/4. Compare the sum of
(10) with

\[
 \frac\rho2\sum_{y\in O}e^{-\pi A\varepsilon|y|^2}
                              e(-cy^2/4).               \tag{13}
\]

Use a telescoping replacement of the prefactor, the damping, then
the phase. Each bound is for the complete absolute sum:

* Prefactor: |rho/(2sqrt(r_epsilon))-rho/2|=O_c(epsilon^2).
  The remaining damping is at most exp(-pi A epsilon |y|^2/2),
  so (12) bounds this error by O_c(epsilon).
* Damping: with t=pi A epsilon |y|^2, the real mean-value theorem gives
  |exp(-t/r_epsilon)-exp(-t)|<=t|1/r_epsilon-1|exp(-t/2).
  Thus the total is O_c(epsilon^3) times the j=1 sum in (12),
  namely O_c(epsilon).
* Phase: |exp(iu)-exp(iv)|<=|u-v| and |Im(cy^2)|<=rho |y|^2
  give |e(-cy^2/(4r_epsilon))-e(-cy^2/4)|
  <=(pi rho/sqrt(3))|1/r_epsilon-1||y|^2.
  Its total, with the Gaussian weight, is O_c(epsilon^2)
  times the j=1 sum, hence O_c(1).

After division by I_epsilon these errors are respectively
O_c(epsilon^2), O_c(epsilon^2), O_c(epsilon), all tending to zero.
In particular an unnormalized O_c(1) phase error causes no gap.

The phase e(z^2/c) is cO-periodic, because its exponent changes by
2zw+cw^2 in O when z is replaced by z+cw. Partitioning the left
side of (6) into its q_c residue classes and using (11) with a=1
therefore gives the limit H(c)/rho after normalization.

The phase in (13) is 2O-periodic: replacing y by y+2w changes
-cy^2/4 by -cyw-cw^2 in O. Apply (11) with b=2 and a=q_c/4;
each of its four residue classes has normalized Gaussian mass 1/q_c.
The limit of (13)/I_epsilon is consequently
(1/(2rho)) sum_(y mod 2O) e(-cy^2/4). Comparing with the left
side proves (2). All partitions here are finite, and Poisson is used
only before taking the controlled normalized limit.

### All finite classes and the correction

For u=a+b omega, e(u)=exp(2pi i b). The residues 0,1,omega,omega^2
represent O/2O, since X^2+X+1 is irreducible over F_2. Their squares
are 0,1,omega^2,omega. Multiplication gives
u omega^2=(-a+b)-a omega and u omega=-b+(a-b)omega, so

\[
 h(a+b\omega)=\frac{1+i^{-b}+i^a+i^{b-a}}2.              \tag{14}
\]

Changing u by 4v does not change any summand. For an odd v,
multiplication by v permutes O/2O, whence h(uv^2)=h(u).
There are twelve units modulo 4: all sixteen residues except the
four in 2O/4O. A square modulo 4 depends only on its lift modulo 2,
since (v+2w)^2=v^2 modulo 4. Thus the square subgroup is
{1,omega,omega^2}. The following coordinates modulo 4 display all
twelve units and show that the four asserted cosets are distinct:

| Representative | Its multiples by 1, omega, omega^2 as (a,b) | h |
| --- | --- | --- |
| 1 | (1,0), (0,1), (3,3) | 1 |
| -1 | (3,0), (0,3), (1,1) | 1 |
| lambda | (1,2), (2,3), (1,3) | i |
| -lambda | (3,2), (2,1), (3,1) | -i |

The h-column follows by substituting the representative in (14),
and square invariance covers the other two entries in each row.
Both generators have order two in G: (-1)^2=1 and
lambda^2=-3=1 modulo 4. Hence G is the product of the two order-two
groups. On its coordinates h((-1)^a lambda^b)=(-1)^(ab) i^b.
In a quotient as in (3), the sign part contributes (-1)^(af+bd);
the i-powers contribute i^((b+f mod 2)-b-f)=(-1)^(bf).
This proves (3) for all sixteen pairs, its nonvanishing, symmetry
and separate multiplicativity. For p,pq the equality (2) then gives
exactly the claimed H-quotient. No other prime or Gauss identity is
used in this argument.

The source's character, measure, prefactor, branch, limiting errors
and table therefore pass this fixed-modulus reproduction audit.
Only the stated conditional input in the L554 application is removed;
its other imports and the hypotheses of its analytic uses remain.

## Mathlib

The previously inspected
[PoissonSummation documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/PoissonSummation.html)
lists `Real.tsum_eq_tsum_fourier` with explicit summability hypotheses
and `SchwartzMap.tsum_eq_tsum_fourier`. These support standard Poisson
summation; they are not a checked full match for the bilinear Eisenstein
specialization here. Full matching coverage of (2)–(3), and coverage
of the complex-matrix Gaussian branch application, have not been
checked. No absence claim or formal verification is made.
