# L036 — A quadratic-pencil restriction on the exceptional overlap

## Hypotheses

Retain L033's complete hypotheses: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, k=8, the pinned four-omission cell, eight shifted
moments, nonzero polynomial D and all nonzero coordinate locators,
and the explicit union-six affine lift with three distinct finite
full-weight four-errors. Assume N_3=0 and N_ext=13, hence L010
sixteen-count equality. All parameters below are original finite
parameters; all error weights are the actual nonzero weights.

Assume L035's exceptional intersecting tag pair occurs. Write
\[
 Z_1=\{x,y\},\quad Z_2=\{r,s\},\quad Z_3=\{t,w\},
 \qquad U=Z_1\sqcup Z_2\sqcup Z_3,
\]
renumbering the selected parameters gamma_i accordingly. The exceptional
additional supports and their parameters are
\[
 B_1=\{x,p,a,b\}\quad(\tau_1),\qquad
 B_2=\{x,p,c,d\}\quad(\tau_2),\qquad
 K_0=\{a,b,c,d\}\quad(\tau_0).
\]
Here K_0 is the unique additional support disjoint from U,
p is in H minus (U union K_0), and all eleven labels in
U union {p,a,b,c,d} are distinct. These facts follow from L035;
they are retained explicitly. The six gamma_i,tau_i are distinct.

## Conclusion

The matrix over F_97
\[
 R=\begin{pmatrix}
 rs&r+s&1\\
 tw&t+w&1\\
 ab&a+b&1\\
 cd&c+d&1
 \end{pmatrix}                                      \tag{1}
\]
has rank exactly two. Its one-dimensional kernel has a generator
(A,B,C) in F_97^3 with AC-B^2!=0. The fractional linear transformation
\[
 \phi(z)=\frac{-Bz-C}{Az+B}                          \tag{2}
\]
is a nonidentity involution of P^1(F_97), defined at all eight paired
labels and exchanging r with s, t with w, a with b, and c with d.
Thus any labeling for which (1) has rank three cannot realize this
exceptional case, even with arbitrary extension-field weights.

More explicitly, the two union-six affine lifts differ by a codeword
whose polynomial is
\[
 h(X)(q_0(X)+Tq_1(X)),\qquad
 h(X)=\prod_{z\in H\setminus(U\cup\{x,p,a,b,c,d\})}(X-z),
 \qquad\deg q_i\le2.                               \tag{3}
\]
The polynomials q_0,q_1 are linearly independent over F. At each paired
label q_1 is nonzero, and -q_0/q_1 has equal values on each pair, namely
gamma_2, gamma_3, tau_2, tau_1 respectively.

This is a necessary moment-compatibility restriction, not a sufficient
construction, exclusion of all exceptional cases, twelve-incidence
bound, or global fifteen bound. The all-disjoint tag-pair case remains
untreated. The result awaits a separate critical audit.

## Proof

### The alternate lift and its shortened difference

L010 and L033 give sixteen-count equality before any use of L035 or
L032. The three actual errors on B_1,B_2,K_0 have union
U'={x,p,a,b,c,d}, of size six. Apply L032 to this equality triple:
there is an affine lift f'(T) supported on U', with the same syndrome
s(T) and taking the three actual error values at tau_1,tau_2,tau_0.
The omission pairs are {c,d}, {a,b}, {x,p}, respectively. Thus for
nonzero slopes d_z,
\[
 f'_a(T)=d_a(T-\tau_2),\quad f'_b(T)=d_b(T-\tau_2),
 \quad f'_c(T)=d_c(T-\tau_1),\quad f'_d(T)=d_d(T-\tau_1).
                                                               \tag{4}
\]
No values at other parameters are assumed to be sparse errors.

Let f be L033's original affine lift. By L010's moment-kernel identity,
both coefficient vectors of f-f' belong to C, since
sigma(f(T)-f'(T))=0 as a polynomial identity. The evaluation map on
polynomials of degree less than eight is injective, so f-f' is the
evaluation of a unique polynomial P_0(X)+TP_1(X), deg P_i<8.
It vanishes off U union U'. Since U intersects U' in exactly {x},
this union has eleven labels and its complement has five.

Use the already assessed shortening formula of Marquez-Corbella and
Pellikaan, *A characterization of MDS codes that have an error correcting
pair*, Finite Fields and Their Applications 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript dated February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following unnumbered
GRS shortening formula, printed pp. 7–8. Exactly as specialized in
L033, shorten on these five excluded labels. At stage j=0,...,4 the
code has n=16-j,k=8-j; the next deletion meets
15-j>=8-j, and the final dimension is three. Labels are distinct and
every retained multiplier is a product of nonzero label differences.
The formula therefore gives (3), with residual degrees less than three,
over F. This is a new application to five deletions, not a reproof of
the generic theorem. It uses the same assessed hypotheses and factor
convention; no puncturing or dual-code formula is substituted.

For z in Z_2 or Z_3, f'_z=0 and h(z)!=0, so (3) gives
q_1(z)=c_z/h(z)!=0 and q_0(z)=-gamma_i q_1(z), with i=2 or 3.
For z in {a,b} or {c,d}, f_z=0. Equation (4) similarly gives
q_1(z)=-d_z/h(z)!=0 and q_0(z)=-tau_j q_1(z), with j=2 or 1.
This proves all paired-value assertions. If q_0,q_1 were dependent,
their ratio would be constant wherever q_1!=0, contradicting the
distinct values gamma_2 and gamma_3. Hence they are independent.
The shared coordinate x imposes further conditions; none is discarded
as a sufficient-construction claim here.

### A bilinear constraint and its exact field descent

Write q_i(X)=alpha_i+beta_i X+chi_i X^2. Direct expansion gives
\[
 q_0(z)q_1(v)-q_0(v)q_1(z)
 =(z-v)\bigl(Azv+B(z+v)+C\bigr),                    \tag{5}
\]
where
\[
 A=\chi_0\beta_1-\beta_0\chi_1,\quad
 B=\chi_0\alpha_1-\alpha_0\chi_1,\quad
 C=\beta_0\alpha_1-\alpha_0\beta_1.
\]
Independence means these three two-by-two minors are not all zero:
otherwise the two coefficient rows have rank at most one. Every pair
in (1) consists of distinct labels, and its equal q_0/q_1 values make
the left side of (5) zero. Thus (A,B,C) is a nonzero kernel vector
of R over F and rank_F R<=2.

All entries of R lie in F_97. Rank over F equals rank over F_97,
because a minor is zero over one field exactly when it is zero over
the other. Two rows from distinct disjoint pairs are independent:
their last entries are one, so proportionality would mean equal sums
and products, hence identical unordered root sets of their monic
quadratics. The pairs are disjoint. Consequently rank R=2 and its
kernel is one-dimensional over F_97. Choose its nonzero rational
generator, again named (A,B,C); it is proportional over F to the
vector in (5). This descent concerns the bilinear constraint only;
it assumes neither rational affine parameters nor rational weights.

Suppose AC-B^2=0. If A=0, then B=0 and C!=0, contradicting any
row equation. If A!=0, the row equation factors as
(Az+B)(Av+B)/A=0. Each of the four disjoint pairs would then contain
the same label -B/A, impossible already for the first two pairs.
Thus AC-B^2!=0.

The matrix of (2) is M=((-B,-C),(A,B)), with determinant AC-B^2.
It is invertible and M^2=(B^2-AC)I, proving phi squared is the identity
projectively. It is not a scalar matrix: if it were, A=C=0 and
-B=B; characteristic 97 is not two, forcing B=0, contrary to
invertibility. For a paired label z, Az+B cannot vanish, since its
row equation would then give Bz+C=0, contradicting AC-B^2!=0.
Solving that equation gives v=phi(z). This proves the involution
assertion with all finite-denominator cases checked.

### Nonvacuous labeling test and limitations

The condition is a genuine additional test on labels, rather than
degree balance. For example, take
\[
 \{r,s\}=\{1,8\},\quad \{t,w\}=\{64,27\},\quad
 \{a,b\}=\{22,79\},\quad \{c,d\}=\{50,12\}.
\]
These are distinct labels of H: they are the first eight powers of 8
in F_97, with 8^4=22 and 8^8=-1, so 8 has order sixteen.
The first three rows of (1) are (8,9,1),(79,91,1),(89,4,1).
Their determinant is
71*(-5)-82*81=-6997=84 modulo 97, nonzero. This labeling is
therefore excluded regardless of the other three labels or weights.
This is an algebraic test case, not a complete support family or a
finite search. Conversely the label test can pass, for example on
four disjoint opposite pairs exchanged by z -> -z. Passing it
establishes no actual pencil or thirteen-incidence completion.

All mathematical inputs have been used with equality, full weights,
finite parameters and the actual syndrome pencil retained. Neither a
projective parameter change nor removal of the original excluded [v]
is made. The four paired equations do not encode the shared-coordinate
weight condition, the remaining errors, or nonpersistent locators.
The all-disjoint alternative of L035, the full twelve bound, universal
cluster extraction, ABF26 identification and global fifteen remain
unresolved. This is local progress under the unchanged EXPLORE review;
POTENTIALLY_NEW means its coverage was not established in that bounded
comparison, not certified originality beyond the inspected sources.

## Mathlib

Coverage of this complete conditional restriction is **not checked**.
Supporting fractional linear transformations, polynomial identities,
matrix rank and scalar-extension facts have not been looked up here.
No absence or formal verification claim is made; the elementary
bilinear and involution calculations needed are written out above.
