# Lemma 772: a positive entire infinitely log-concave sequence with a negative order-five minor

## Hypotheses

Set b_n=0 for every integer n<0. Define the positive rational prefix

\[
 (b_0,\ldots,b_8)=
 (10^{-12},10^{-6},10^{-2},3/5,1,3/5,10^{-2},10^{-6},10^{-12})
                                                               \tag{1}
\]

and for every integer k>=0 define its compatible extension by

\[
 b_{8+k}=10^{-12}(10^{-6})^k4^{-k(k+1)/2}.                       \tag{2}
\]

For a one-sided sequence x extended by zero at negative indices, put
\(\mathcal L(x)_n=x_n^2-x_{n-1}x_{n+1}\) for n>=0, and continue to
extend every iterate by zero at negative indices. Write
\(r_0=(3+\sqrt5)/2\).

## Conclusion

Every b_n for n>=0 is strictly positive, the ordinary generating
function B(z)=sum_(n>=0) b_n z^n is entire, and

\[
 b_n^2\ge\frac{11}{4}b_{n-1}b_{n+1}\qquad(n\ge1).               \tag{3}
\]

For every integer m>=0, all entries of \(\mathcal L^m(b)\) at
nonnegative indices are strictly positive. Every such sequence is
r_0-factor log-concave and hence strictly log-concave, including the
zero-extended boundary at index0. Nevertheless,

\[
 D_{5,4}(b):=\det[b_{4+j-i}]_{i,j=0}^4
 =-\frac{351560678441474525317585871}{10^{28}}<0.                 \tag{4}
\]

Thus positivity of every iterated Turan transform, even strengthened
by the global 11/4 ratio bound and entire convergence, does not imply
this exceptional Toeplitz sign in the class of positive coefficient
sequences. No actual-theta moment representation, actual-Xi
realization, smoothing premise, or RH consequence is asserted.

## Proof

### Source specialization and its scope

Olga M. Katkova and Anna M. Vishnyakova, *On sufficient conditions
for the total positivity and for the multiple positivity of matrices*,
[arXiv:math/0504183v1](https://arxiv.org/pdf/math/0504183v1),
Theorem4(i), printed p.3, and the complete Toeplitz construction in
Section3, printed p.12, supply sharpness below
c_k=4 cos^2(pi/(k+1)). At k=5 the threshold is 3. Their positive
Toeplitz matrices obey adjacent inequalities in the TP_2(c) sense;
small positive outer diagonals perturb a tridiagonal model while
retaining a negative determinant. That known construction motivates
(1). We do not reprove sharpness. An explicit prefix, a one-sided
positive entire extension and its junction are needed here and are
not furnished by the finite theorem; those specialization obligations
are proved directly below. There is no claim of originality.

### All ratios and entire convergence

Positivity follows immediately from (1)-(2). Direct rational
arithmetic gives, for n=1,...,7 respectively,

\[
 \frac{b_n^2}{b_{n-1}b_{n+1}}
 =100,\ 500/3,\ 36,\ 25/9,\ 36,\ 500/3,\ 100.                 \tag{5}
\]

The smallest of these is 25/9>11/4, since their difference is 1/36.
At the junction, b_9=10^(-18)/4, so
b_8^2/(b_7 b_9)=4. For n>=9, the quadratic exponent in (2) gives
the same ratio 4. This proves (3) at every required index, with no
unverified tail or junction. At index0 the factor inequality is
also true because b_(-1)=0.

For n>=8,

\[
 \frac{b_{n+1}}{b_n}=10^{-6}4^{-(n-7)}\longrightarrow0.         \tag{6}
\]

For any fixed R>0 the successive ratios of b_n R^n therefore tend
to zero. The ratio test gives sum b_n R^n<infinity. Since R is
arbitrary, the power series converges absolutely and uniformly on
each closed disk and defines an entire function.

### Every iterate, including strictness and the boundary

Peter R. W. McNamara and Bruce E. Sagan, *Infinite log-concavity:
developments and conjectures*,
[arXiv:0808.1065v2](https://arxiv.org/pdf/0808.1065v2), Section2,
printed pp.3-4, Lemma2.1 (and its preceding proof), states that
r_0-factor log-concavity of a nonnegative sequence is preserved by
\(\mathcal L\), and consequently implies infinite log-concavity.
Here r_0-factor means x_n^2>=r_0 x_(n-1)x_(n+1), with zeros
outside the index set. This preservation theorem is imported, not
reproved. It is a local sequence statement and requires neither a
finite support assumption nor an interchange of infinite sums.

The strict bound r_0<11/4 follows from sqrt(5)<5/2. Thus (3) and
the zero extension meet the lemma's hypotheses. Every iterate is
nonnegative and r_0-factor log-concave by repeated application.
To establish strictness, suppose x=\(\mathcal L^m(b)\) is positive
at all n>=0, as it is at m=0. For n>=1 its preserved factor bound
implies

\[
 \mathcal L(x)_n\ge(1-1/r_0)x_n^2>0.
\]

At n=0, \(\mathcal L(x)_0=x_0^2>0\), because x_(-1)=0.
Induction proves positivity at every iterate and index. Since
r_0>1, its factor inequality is strict ordinary log-concavity at
n>=1; the index0 inequality is strict as well. This is an all-order
theorem application, not a finite iterate test.

### Exact negative determinant

Put a=3/5, d=1/100, e=1/10^6 and f=1/10^12. The matrix in (4) is

\[
 M=\begin{pmatrix}
 1&a&d&e&f\\a&1&a&d&e\\d&a&1&a&d\\e&d&a&1&a\\f&e&d&a&1
 \end{pmatrix}.                                                \tag{7}
\]

It commutes with coordinate reversal. Its invariant odd subspace
has vectors (x,y,0,-y,-x), and its invariant even subspace has
vectors (x,y,z,y,x). Their direct sum is all of R^5. The corresponding
coordinate matrices are

\[
 M_-=\begin{pmatrix}1-f&a-e\\a-e&1-d\end{pmatrix},\qquad
 M_+=\begin{pmatrix}1+f&a+e&d\\a+e&1+d&a\\2d&2a&1\end{pmatrix}.
\]

Consequently det M=det M_- det M_+, without a change-of-basis
determinant factor. Explicitly,

\[
\begin{aligned}
 \det M_-&=(1-f)(1-d)-(a-e)^2
       =\frac{63000119999801}{10^{14}}>0,\\
 \det M_+&=(1+f)(1+d-2a^2)-(a+e)^2
                +4ad(a+e)-2d^2(1+d)
       =-\frac{5580317600071}{10^{14}}<0.
\end{aligned}
\]

Their product is (4). All entries in (7) use only the prefix; the
tail cannot alter this determinant. The reference tridiagonal matrix
with d=e=f=0 has determinant 1-4a^2+3a^4=-32/625, explaining the
source construction's use here, but the actual sign has been checked
exactly rather than inferred from unspecified perturbation size.

Reproduce the finite checks with
`python3 scripts/coefficient-countermodel/strong-log-order-five-408.py`.
The script uses exact fractions and all 120 determinant permutation
terms, and independently checks the reversal-block product. It writes
the complete finite certificate to
`scripts/coefficient-countermodel/strong-log-order-five-408.json` and
prints the actual determinant, required and actual ratio bounds,
failures and certificate path. The universal tail, entire convergence
and all-iterate arguments are the proofs above; the finite script does
not replace them. In particular this countermodel does not certify
any claim including additional actual-theta moment constraints.

### Independent audit — 4 November 2026, step410

The separate audit used the unchanged SPECIALIZE gate and imported
the same McNamara–Sagan statement, without redoing source discovery.
Run `python3 scripts/coefficient-countermodel/positive-entire-audit-410.py`.
Its complete finite report is
`scripts/coefficient-countermodel/positive-entire-audit-410.json`;
the original step408 certificate is preserved and identified by SHA256.

Every one of the 120 recorded permutations was checked for validity
and uniqueness, its sign recomputed from cycle parity, and its rational
product recomputed from (1). Their sum agrees with fraction-free
integer elimination of 10^12 M, divided by 10^60. This yields exactly
(4). The audit also checks M O=O M_- and M E=E M_+, where O and E
have the odd and even basis vectors displayed above as columns.
The combined basis is invertible. Independent elimination gives the
two displayed block determinants and their product; no orthonormality
or extra determinant factor is assumed. All prefix entries, all seven
prefix ratios, b_9, the junction, the reference determinant and the
comparison with r_0 were checked exactly. All fourteen reported checks
pass, with no failures. This checks the complete relevant finite
evidence, rather than relying on the generator's success flags.

For the universal claims the audit checks the proof, not a finite
sample. In (2), the exponent difference from k to k+1 is -(k+1),
giving (6); its second difference gives ratio 4 at n>=9. The separate
n=8 calculation and (5) exhaust n>=1. On each disk |z|<=R the summable
majorant b_n R^n gives uniform convergence, so the entire claim follows.
The factor r_0 is preserved at each iterate by the cited theorem for
nonnegative sequences; the strict lower bound and the n=0 identity
then give positivity at every index by induction on the iterate.
Zero extension at negative indices is preserved, including n=-1.
There is no hidden finite-support or uniform-in-iterate limit claim.

The audited result remains only a larger-coefficient-class obstruction.
Neither a representation by the actual theta kernel nor even a
factorial-restored positive-measure moment representation is proved
for this b. L766 and any claimed actual-Xi all-iterate theorem are
unused. The audit confirms the local known-result specialization;
it supplies no actual-Xi sign and no result beyond the sources'
generic sharpness mechanism is claimed.

## Mathlib

Coverage of Katkova-Vishnyakova Theorem4(i), McNamara-Sagan Lemma2.1,
and this positive-entire specialization has not been checked in
Mathlib; availability remains unknown. No matching formal theorem
is claimed. The rational certificate is an informal arithmetic check,
not a Lean proof or a proof of any Xi sign.
