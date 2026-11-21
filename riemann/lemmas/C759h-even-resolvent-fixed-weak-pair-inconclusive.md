# C759h: Complete even resolvent — fixed weak-pair test is inconclusive

## Hypotheses

Use precisely C759a(1),(5)-(6) and its closed-form realization on
real L2(-1,1), with zero extension, restricted to the even subspace H_e.
Let A_e be its self-adjoint form operator. All five overlapping prime
powers n=2,3,4,5,7 and both poles are retained. Set

\[
 h(s)=(\max\{1-s^2,0\})^2,\quad
 u(x)=h(40(x-1/5))+h(40(x+1/5)),\quad
 v(x)=h(40(x-4/5))+h(40(x+4/5)).
\]

The approved assessment822 permits one space
V=(1-x²)span{P_0,P_2,...,P_510}, of dimension256, at the fixed
spectral parameter -16. Here P_n are the Legendre polynomials
normalized by P_n(1)=1. No parameter, forcing or dimension sweep is used.
The exact candidate w in V is specified by the complete dyadic
coefficient list `exact_candidate/coefficients` in
`scripts/spectral-triples/even-weak-pair-823.json`:
w=(1-x²)sum_{j=0}^{255}q_j P_{2j}, where each stored numerator and
denominator specifies q_j exactly. Numerical assembly only selects w;
its accuracy is not a hypothesis of the certified statements.

The standard inverse estimate is imported from Gerald Teschl,
*Mathematical Methods in Quantum Mechanics*, GSM99, online version
12February2009, Theorem2.18, printed p77 (with the spectral-distance
estimate in Lemma2.7, p66),
[primary text](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
Only the real-resolvent norm estimate after a proved spectral floor
is used. This is a REPRODUCTION of its actual-form specialization,
not new operator theory or a claim of originality.

## Conclusion

The operator has the proved floor A_e>=-10I, and -16 is in its
resolvent set, with ||(A_e+16I)^(-1)||<=1/6. Every element of V is
in D(A_e), as are u and v. The full Friedrichs action is specified below.

For B=<v,(A_e+16I)^(-1)u> and the exact w above, the rational computation
gives

\[
 -0.00001309225721<\langle v,w\rangle<-0.00001309225720,
 \qquad \|u-(A_e+16I)w\|_2\le R<1.3555247227.
\]

The resulting rigorous enclosure is contained in

\[
             -0.045555<B<0.045529,
\]

and its unrounded rational endpoints have opposite signs. The
sufficient residual threshold for the negative-pair certificate using
the same inverse bound and norm majorant is between
0.0003896871374 and0.0003896871375; the achieved majorant R exceeds1.3555.
Thus neither sign is certified. This says nothing adverse about the
actual sign, the best possible residual bound or other trial methods.
The fixed test stops inconclusively under its approved termination rule.

The full physical residual sampled by the diagnostic has norm about
0.00114790, also larger than that sufficient threshold, but this sample
is not a lower or upper certificate. It cannot prove that a sharper
rigorous estimate must fail. No positivity-improvement failure,
ground-state sign/simplicity, parity ordering or RH statement follows.

## Proof

### 1. Spectral floor on the complete even closed form

Write c(x)=cosh(x/2). For even real f the two pole functionals are
both <c,f>, because the sinh component integrates to zero. Thus their
complete contribution is 2<c,f>²>=0, and its associated operator is
2c<c,f>. This remains true on the closed domain since c is L2.
C759a(5) gives m(t)>=m_*=-log(4pi)-4. Its Proof3 gives the full
prime-operator norm at most C, with C<3.12926<313/100 by its audited
certificate. These estimates hold on the whole form domain, so

\[
 Q(f)\ge(m_*-C)\|f\|_2^2\quad(f\in H_e\cap\mathcal V).
\]

For explicit conservative constants, pi<4 and log2<7/10 give
log(4pi)<log16=4log2<14/5. The logarithm bound follows from the
positive exponential series:
1+7/10+(7/10)²/2+(7/10)³/6+(7/10)^4/24>2.
Therefore m_*>-34/5 and m_*-C>-993/100>-10.
The representation/spectral theorem for a semibounded self-adjoint
form operator puts its spectrum in [-10,infinity). Teschl2.18 now
applies at the real point -16, giving the stated inverse bound.
Complexification and restriction to the invariant real subspace do
not change that bound. No small-window positivity theorem is used.

### 2. Actual operator domain and action

For f supported on [-1,1] write f_0 for its zero extension. From
C759a(5), ||r||_1<=log2+4, and half log(1+t²)<=|t|, we obtain

\[
 |m(t)|\le |t|+\log(2\pi)+\log2+4<|t|+7.             \tag{1}
\]

If f belongs to H1_0(-1,1), its zero extension is H1(R), so Plancherel
and (1) show that mF_f is L2 and
||m(D)f_0||_2<=||f'||_2+7||f||_2. The Fourier form pairing against
any g in the closed form domain consequently equals
<m(D)f_0,g_0> by Cauchy–Schwarz, and is a bounded L2 functional.
All prime shifts and poles are bounded L2 operators. The defining
representation theorem for the closed form thus gives f in the
operator domain, with, for even f,

\[
 (A_ef)(x)=(m(D)f_0)(x)+2c(x)\langle c,f\rangle
 -\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}
       [f_0(x+\log n)+f_0(x-\log n)],\quad |x|<1.       \tag{2}
\]

The multiplier is applied on the full line before restriction. Each
polynomial in V vanishes at ±1 and has an L2 weak derivative after
zero extension. The quartic bumps u,v are C1, piecewise polynomial,
supported strictly inside (-1,1), and in H1_0 as well. All are even;
their nonnegativity where asserted is immediate from their formula.
Their disjoint supports give no premise about a resolvent sign.
This proves domain membership without identifying A_e with the
nonsymmetric causal generator considered in L741.

### 3. Whole-residual comparison and certified majorant

For any w in D(A_e), let r=u-(A_e+16I)w. The exact identity
(A_e+16I)^(-1)u-w=(A_e+16I)^(-1)r and the imported inverse estimate
give, by Cauchy–Schwarz,

\[
 |B-\langle v,w\rangle|\le\|v\|_2\|r\|_2/6.          \tag{3}
\]

The pole operator has norm 2||c||²=2(1+sinh1)<5<8, since e<3.
Combining (1),(2), C<4 and the triangle inequality yields the deliberately
conservative, but full-interval, certificate

\[
 \|r\|_2\le\|u\|_2+\|w'\|_2+35\|w\|_2.             \tag{4}
\]

It includes the entire Fourier multiplier and every arithmetic/pole
term, with no projected-residual substitution or unbounded tail omitted.
The bound loses cancellations; it is not an estimate from the sampled
residual. Direct integration gives ||u||²=||v||²=64/1575.

Here is the exact finite arithmetic underlying the artifact. Multiplying
each P_n by 1-x² uses twice the recurrence
xP_n=((n+1)P_{n+1}+nP_{n-1})/(2n+1), with the n=0 lower term absent.
This converts the stored dyadic q_j to rational coefficients a_n of w.
Orthogonality and the derivative identity
P_n'=sum_{k<n,n-k odd}(2k+1)P_k give

\[
 \|w\|_2^2=\sum_n\frac{2a_n^2}{2n+1},\quad
 \|w'\|_2^2=\sum_k2(2k+1)
                \left(\sum_{n>k,n-k\ {m odd}}a_n\right)^2.
\]

These are rational equalities, evaluated completely in the script.
For <v,w>, the same polynomial recurrence is evaluated at
x=4/5+s/40. Integrate its coefficients against (1-s²)²/40 on [-1,1]:
the moment for even k is
2[1/(k+1)-2/(k+3)+1/(k+5)]/40; odd moments vanish. Multiply by2
for the reflected bump. This is an exact rational integral, independent
of numerical quadrature.

For each nonnegative rational norm square a, the script computes the
least k/10^24 whose square is >=a by integer square root and an exact
comparison. Let W,D,U be these upper bounds for ||w||,||w'||,||u||.
The stored R=U+D+35W and error radius UR/6 are rational. In particular
W<0.01139459 and D<0.75513305. All endpoints and sufficient threshold
6|<v,w>|/U are computed as rationals. Their complete values are saved,
and exact comparisons establish the decimal brackets in the conclusion,
including that zero lies strictly inside the enclosure from (3)-(4).

### 4. Diagnostic status and reproducibility

Run `python3 scripts/spectral-triples/even-weak-pair-823.py`.
The script uses a single256-dimensional space, forms a quadrature
Galerkin system, selects a dyadic candidate, and samples (2) on a
different grid. The auxiliary physical-space singular-integral assembly
and all floating quadrature/eigenvalue outputs are explicitly diagnostic.
They have no validated quadrature or roundoff bounds and are not used
to establish (1)-(4), domain membership, the floor or the exact finite
arithmetic certificate. In particular a computed matrix inverse does
not certify B. Any exact dyadic candidate would be valid in (3)-(4).

The artifact stores all candidate coefficients, exact norms, exact
trial pairing, whole-residual majorant, rational sign enclosure, failures
and the script hash. `rational_certificate/exact_checks` contains exact
comparisons for the reported brackets and endpoint/even membership.
The present attempt stops at its zero-containing enclosure; neither
another basis size nor a sharper same-witness computation is nominated.
Reopening would need a materially improved certified residual mechanism,
not treating the sampled value or trial pairing as the answer.

## Mathlib

Full matching theorem and supporting theorem coverage were not checked.
The mathematical imports are the precisely cited standard real-resolvent
estimate and C759a's canonical complete form/domain/bounds. No Mathlib
absence, formal verification or progress beyond those sources is claimed.
