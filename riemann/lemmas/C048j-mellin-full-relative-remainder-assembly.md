# Corollary C048j: the full relative theta-Mellin remainder

## Hypotheses

Use C048a's actual theta kernel and Mellin continuation:

\[
 \Phi(u)=\sum_{n\ge1}(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})
                           e^{-\pi n^2e^{2u}},\qquad
 I(p)=2\int_0^\infty u^{2p-1}\Phi(u)\,du\quad(\Re p>0),
\]

with I continued meromorphically as in C048a. Let

\[
 r=|p|,\quad L=\log r\ge12,\quad \Re p\ge-r/(4L),\quad
 w=W_0(2p/\pi)=U+iV,\quad u_0=w/2=x_0+iy,\quad d=1/(3L).
\]

All logarithms are principal. Use C048c's definitions

\[
 h_p(u)=2p\operatorname{Log}u-\pi e^{2u},\quad
 g(u)=8\pi^2e^{9u/2}/u,\quad K(s)=g(u_0+s)/g(u_0),\quad
 A_0=4p(1+w)/w^2,
\]
\[
 Q=\sqrt{\pi/A_0},\quad M=g(u_0)e^{h_p(u_0)},\quad
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
          e^{2p\operatorname{Log}(w/2)-2p/w}.
\]

Square roots are the principal ones, agreeing with continuation from
positive real p. The quantitative component conclusions of C048b-i
are reused with their exact observables. No global source error bound,
zero count, inversion or Xi-sign assertion is a premise.

## Conclusion

On this entire closed, unbounded sector, I is finite, S is nonzero and

\[
 \left|\frac{I(p)}{S(p)}-1\right|
 <\frac{8675923}{5400000}\frac{L^{9/2}}r
 <\frac{17}{10}\frac{L^{9/2}}r.                       \tag{1}
\]

This is REPRODUCTION of K. Kawano, *Logarithmic Inequalities of
Arbitrary Order for the Riemann Xi Coefficients*,
[Preprints.org 202611.0383v1, posted 4 November 2026,
DOI 10.20944/preprints202611.0383.v1](https://www.preprints.org/manuscript/202611.0383/v1),
Section5.1(25), Section5.2(28)-(29), Lemma5.1(i), and AppendixC's
final aggregation before C.1. The preprint is not peer reviewed.
Its precise claim and allocation were compared in source-notes1652;
assessment1652 approved this assembly before the present step1653.
The proof verifies the claimed estimate from existing components,
rather than importing the quantitative preprint assertion as a theorem.
The coarser rational coefficient in (1) is not the source's printed
1.606651 and is not asserted to improve its result.

Independent conceptual audit1655 below validates this assembly without
a mathematical correction, reusing the audited component conclusions.
It does not assert the source's additional less-than-one conclusion,
finite-region estimates, zero counts, inversion, or sufficient
actual-Xi mixed signs. L030-L032/C032a, C028b's H_d=o(d), C028g's
S_F=0 and the Mellin-to-sign bridge remain open. No RH candidate is
claimed. The downstream use is quantitative analytic control of I.

## Proof

### 1. Normalization, convergence and the combined origin

C048c gives

\[
 x_0>9/2,\quad |y|<\pi/4,\quad 0<d\le1/36,\quad
 \Re A_0>0,\qquad MQ=S(p)\ne0.                       \tag{2}
\]

The equality in (2) retains the complex phase, not just its modulus.
For completeness, the branch calculation in C048c gives
\(\sqrt{p(1+w)}=w\sqrt{A_0}/2\) and
\(Q=\sqrt\pi/\sqrt{A_0}\), which imply it on the whole sector.
C048a also excludes every possible Mellin pole there.

Define the full theta factor

\[
 F(u)=1+b(u)+R(u),\quad b(u)=-\frac3{2\pi e^{2u}},\quad
 R(u)=\sum_{n\ge2}\left(n^4-\frac{3n^2}{2\pi e^{2u}}\right)
                         e^{-\pi(n^2-1)e^{2u}}.        \tag{3}
\]

L799's general strip-convergence argument and identity(4) apply to
this factor on |Im u|<pi/4, independently of that lemma's different
saddle estimates. On each compact subset the series is normally
convergent, and division by the nonvanishing leading theta mode gives
exactly

\[
 2u^{2p-1}\Phi(u)=g(u)e^{h_p(u)}F(u)\quad(\Re u>0,
                                                |\Im u|<\pi/4).
                                                               \tag{4}
\]

In particular the factor 2/u is present in g. All the contour pieces
below with x>=1 lie inside this domain. Their finite integrands are
continuous. C048g supplies absolute convergence on the infinite right
ray, so ordinary additive splitting of that integral is legitimate.
We do not integrate the mode series term by term on an infinite ray.

First suppose Im p>0. Fix the numerical height y=Im(w)/2 for this
p. C048a's meromorphic fixed-height identity, evaluated at p only
after that identity is established, and C048b's definition of E_o,
give

\[
 I(p)=E_o(p)+2\int_1^\infty(x+iy)^{2p-1}\Phi(x+iy)\,dx.          \tag{5}
\]

Here, writing \(\Phi(z)=\sum_{n\ge0}c_nz^{2n}\) near zero and
\(a_y=\min(y,1/4)\), the complete combined-origin expression is

\[
 E_o(p)=\sum_{n\ge0}\frac{c_n(ia_y)^{2p+2n}}{p+n}
       +2\int_{ia_y}^{iy}z^{2p-1}\Phi(z)\,dz
       +2\int_0^1(x+iy)^{2p-1}\Phi(x+iy)\,dx.          \tag{6}
\]

The vertical segment is upward; the horizontal segment is to the
right. C048b pays their combined contribution, including the series,
once. There is no assumption that separate moving-height terms are
holomorphic in p.

### 2. Exact oriented partition and Gaussian subtraction

Set \(B(s)=K(s)e^{h_p(u_0+s)-h_p(u_0)}\). Changing variables
x=x_0+s in (5) has dx=ds and preserves orientation. By (2),

\[
 1-x_0<-1<-d<d,
\]

so the whole horizontal interval x>=1 partitions into the following
four pieces, with shared endpoints of zero integration measure:

\[
 J_f=\int_{1-x_0}^{-1}B(s)F(u_0+s)\,ds,\quad
 J_n=\int_{-1}^{-d}B(s)F(u_0+s)\,ds,\quad
 J_r=\int_d^\infty B(s)F(u_0+s)\,ds,
\]
\[
 J_{\rm loc}=\int_{-d}^d B(s)\,ds,\quad
 J_{\rm low}=\int_{-d}^d B(s)b(u_0+s)\,ds,\quad
 J_{\rm modes}=\int_{-d}^d B(s)R(u_0+s)\,ds.           \tag{7}
\]

Only the middle interval is split into modes. Normal convergence from
(3) and C048f justifies its continuous summed integrand; linearity
applied to F=1+b+R gives its exact three-term split. Equations (4)-(7)
therefore give

\[
 I=E_o+M(J_f+J_n+J_{\rm loc}+J_{\rm low}+J_{\rm modes}+J_r).
                                                               \tag{8}
\]

Let \(G_{\rm loc}=\int_{-d}^d e^{-A_0s^2}\,ds\). C048d gives
\(\int_{\mathbb R}e^{-A_0s^2}\,ds=Q\), with both tails absolutely
convergent. The underlying standard formula is
[NIST DLMF7.7.6](https://dlmf.nist.gov/7.7.E6), with a=A_0,
b=c=x=0 and Re A_0>0; evenness gives the full-line integral and
C048c fixes its principal square root. Thus (8) and S=MQ imply the
exact identity

\[
 \frac I S-1=\frac{E_o}S+
 \frac{J_f+J_n+J_r+(J_{\rm loc}-G_{\rm loc})
              +J_{\rm low}+J_{\rm modes}-(Q-G_{\rm loc})}{Q}.
                                                               \tag{9}
\]

The Gaussian completion enters with a minus sign and is charged once.
It is not part of any full-theta tail. Neither the origin interval
nor any theta mode has been omitted or counted twice.

### 3. Uniform higher-mode conversion

Put q(L)=e^L/L^2. For L>=12,
\(q'(L)=q(L)(1-2/L)>0\). The exponential series gives e>2, hence

\[
 q(L)\ge q(12)>\frac{2^{12}}{144}>28
 \quad\text{since }4096>28\cdot144=4032.              \tag{10}
\]

The function q exp(-5q) has derivative exp(-5q)(1-5q)<0 for q>=28.
Consequently C048f's allowance divided by the common scale obeys

\[
 \frac{112\sqrt L\,e^{-5r/L^2}}{L^{9/2}/r}
 =\frac{112}{L^2}q e^{-5q}
 <\frac79\,28e^{-140}
 <\frac{196}{9\cdot2^{20}}
 <\frac1{10000}.                                    \tag{11}
\]

For the middle strict inequality, e^140>2^140>2^20. The last one
is the exact integer comparison
\(1960000<9\cdot1048576=9437184\). Thus (11) holds for the
whole unbounded L-ray, not just its endpoint or a numerical sample.
It converts precisely the C048f bound, without a stronger mode claim.

### 4. One total error budget

Write \(\mathcal E=L^{9/2}/r>0\). Divide the absolute value of
(9) by this scale and use the triangle inequality. C048b contributes
less than 1/10000. C048i, C048h and C048g bound respectively
\(|J_f|/|Q|\), \(|J_n|/|Q|\), \(|J_r|/|Q|\) by their integrals
of absolute values, giving coefficients less than 1/10000,
0.091191 and 0.096514. Their moduli are inside the integrals;
no signed cancellation in a theta tail is being assumed.

C048c bounds \(|J_{\rm loc}-G_{\rm loc}|/|Q|\) with coefficient
less than 1.318214, retaining its already proved local cancellation.
C048d bounds \(|Q-G_{\rm loc}|/|Q|\) with coefficient less than
0.099276; that constant includes both Gaussian tails. C048e gives

\[
 \frac{|J_{\rm low}|}{|Q|}<\frac{2L^{3/2}}r
 =\frac2{L^3}\mathcal E\le\frac1{864}\mathcal E.      \tag{12}
\]

C048f together with (11) contributes less than 1/10000. All component
inequalities have identical p, d, K, A_0 and S normalization. The
four finite decimals below denote exact rational upper bounds from
the cited component conclusions. Their complete sum is

\[
 \begin{split}
 \frac{|I/S-1|}{\mathcal E}
 &<\frac{1318214+99276+96514+91191}{1000000}
       +\frac3{10000}+\frac1{864}\\
 &=\frac{8675923}{5400000}<\frac{17}{10},
 \qquad
 \frac{17}{10}-\frac{8675923}{5400000}
       =\frac{504077}{5400000}>0.                    \tag{13}
 \end{split}
\]

No source sum or source higher-mode allocation is an assumed premise.
Equations (11)-(13) are exact arithmetic and analytic monotonicity
checks; the independent rational replay is
`python3 scripts/mellin-horizontal-local/c048j-assembly-rational-1653.py`,
with its complete finite evidence in
`scripts/mellin-horizontal-local/c048j-assembly-rational-1653.json`.
That replay checks the displayed arithmetic only; the contour and
uniform-in-L arguments are the proof above.

### 5. Real points, reflection and boundaries

When Im p=0 the sector forces p>0. C048b defines
\(E_o=2\int_0^1x^{2p-1}\Phi(x)\,dx\); splitting the original
real Mellin integral immediately gives (5) with y=0. No singular
limit of (6) is needed. Every subsequent identity and component
bound applies at y=0. For Im p<0 use C048a's conjugate downward
formula. The real coefficients of Phi and the principal branches give
conjugate I, w, M, Q and S; the downward vertical orientation and
rightward horizontal orientation are preserved by conjugating the
integrals. Thus the same identities, or their conjugates, and their
absolute bounds apply.

All geometric and component conclusions used above include both
closed angular boundaries and L=12. The intervals remain strictly
inside the theta strip even at those boundaries. The scalar argument
(10)-(13) covers every L>=12 without an upper cutoff. This proves
(1) in all stated cases. It supplies no positivity or zero-count
implication beyond this relative analytic error estimate.

### Independent conceptual audit1655 — 19 November2026

The exact claim (1) was reviewed under assessment1653, separately
approved in step1654. Read the entire assembly and C048a's fixed-height
proof; checked C048b-i's exact hypotheses, observables and conclusions,
the necessary normalization/convergence junctions, and L799's general
strip proof. The component inequalities retain their existing proofs
and audits; this step checks their application and the new assembly,
not a fresh audit of every component's scalar certificate. No
mathematical correction or stronger conclusion is required.

**Contour and continuation.** For each fixed upper-half-plane p in
the sector, C048a first supplies its identity for the fixed numerical
height y=Im(w)/2. Its primitive has the same coefficients, exponent
2p+2n and denominator p+n as (6). Its horizontal tail is entire in p
at fixed y by local compact domination. Adding the finite interval
0<=x<=1 to the primitive is exactly C048b's E_o, so (5) follows by
additivity. All possible poles lie at nonpositive integers, while the
sector excludes that real ray: a negative real p would require
1<=1/(4L). Thus evaluation involves no pole or finite-part limit.
Neither separate moving-height holomorphy nor uniform convergence as
y tends to zero is used.

**Full factor and partition.** In L799's strip notation P=Phi and
H=4pi^2 exp(9u/2-pi exp(2u)), so F=P/H. On compact strip subsets,
the positive minimum of Re(pi exp(2u)) gives a summable majorant
C(n^4+n^2)exp(-delta n^2). Division by the nonzero H gives precisely
(3), independently of L799's different saddle hypotheses. Multiplying
by 2 exp(2p Log u)/u proves (4) with the stated g. On the horizontal
path x>=1 this logarithm is unambiguous. The substitution s=x-x_0
has Jacobian +1 and gives the ordered endpoints
1-x_0<-1<-d<d. The far-left, near-left, local and right pieces
exhaust x>=1, with endpoints irrelevant to integration. Only the
finite local piece is expanded as 1+b+R; all outer pieces retain F.
C048g proves the right integral absolutely convergent, so this finite
partition involves no unsupported infinite interchange. In particular
the combined origin is included once, and both powers of every higher
theta mode are present.

**Complex Gaussian and sign.** C048c gives Re A_0>0 and
|arg w|<pi/4. The principal sqrt(A_0) has argument of absolute value
less than pi/4. Hence w sqrt(A_0)/2 has positive real part and square
p(1+w), proving it is the principal sqrt(p(1+w)). Substitution of
g(u_0)=16pi^2 exp(9w/4)/w and pi exp(w)=2p/w then gives MQ=S
as a complex identity. DLMF7.7.6, with a=A_0 and b=c=x=0, has its
required Re a>0; doubling the half-line integral is legitimate by
evenness and absolute convergence. Thus its full Gaussian is exactly
Q, not merely a number of modulus |Q|. After dividing (8) by MQ,
subtracting 1 subtracts Q in the numerator. Writing
J_loc-Q=(J_loc-G_loc)-(Q-G_loc) verifies the minus sign in (9).
C048d pays that entire Gaussian pair once. The local cancellation
already proved in C048c is retained before taking the modulus.

**Uniform conversion and exact budget.** Since q=e^L/L^2 has
q'/q=1-2/L>0, q>4096/144>28 throughout L>=12. For q>=28,
(q exp(-5q))'=exp(-5q)(1-5q)<0. Dividing C048f's allowance by
L^(9/2)/r gives 112q exp(-5q)/L^2, including the necessary L^-2.
Using L^2>=144, then q>28, then exp(140)>2^20 gives the cap
196/(9*2^20)=49/2359296<1/10000; its last comparison is exactly
1960000<9437184. C048e's ratio is 2/L^3<=1/864. Neither
conversion is a finite grid test.

C048i/h/g bound the integrals of the moduli of the integrands defining
J_f/J_n/J_r, divided by |Q|. The integral triangle inequality therefore
bounds the required normalized signed integrals. C048b, c, d, e and f
bound the moduli of exactly E_o/S, (J_loc-G_loc)/Q, (Q-G_loc)/Q,
J_low/Q and J_modes/Q, respectively.
All use the same p, w, d, K and principal root on the same closed
domain. No component requires a narrower sector, a finite upper
cutoff for L, or an extra positivity assumption. The four decimal
numerators sum to 1605195. After adding the three 1/10000 allowances
this is 321099/200000; adding 1/864 gives 8675923/5400000.
Subtracting it from 17/10 gives 504077/5400000>0. The strict
component-to-rational comparisons justify the strict inequality (1).

Read every mathematical field of certificate1653 in full using
`../scripts/loop/inspect_json.py` at `/budget`, `/scalar`, `/checks`
and `/failures`. Replayed the stated producer once: seven checks
passed, zero failures. Its saved certificate was unchanged byte for
byte, SHA256
`1a94a399abe5caaf6ca8101cc1af438c57a9ac6c7dccb0ecebb2173808edaac4`.
This replay validates finite arithmetic only; the preceding analytic
checks supply the contour and all-L justification.

**Remaining cases and scope.** For real sector points p>0, C048b's
real E_o and the original real Mellin integral give (5) directly.
Conjugation sends the upper vertical segment to the downward segment
and the horizontal path to a rightward lower path, with the same
real parametrization. Real coefficients and the branches just checked
conjugate I, w, M, Q and S. All component bounds include both closed
angular boundaries and L=12, with |y|<pi/4 still strict. Consequently
the audit covers every claimed parameter, not just the open sector.

This establishes C048j as a checked reproduction of the cited
quantitative preprint claim, with its stated coarser constant. It
neither validates the source's stronger printed decimal nor supplies
less-than-one, zero counts, inversion or actual-Xi signs. The
November5 automatic-import and endpoint-review-loop stops are not
reopened: this assembly uses the later proved components. The direct
mathematical inputs in the existing DAG row remain unchanged.

## Mathlib

Full matching coverage for this sector-specific quantitative Mellin
assembly has not been checked and is unknown. No absence or formal
verification is asserted. The standard analytic input used through
C048a and C048d is the meromorphic contour identity and the complex
Gaussian formula with Re A_0>0; supporting integration results alone
would not provide the sector geometry or quantitative components.
No particular Mathlib declaration is claimed to cover (1).
