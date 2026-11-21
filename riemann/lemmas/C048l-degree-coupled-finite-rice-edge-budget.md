# Corollary C048l: a degree-coupled finite Rice closing budget

## Hypotheses

Use exactly C048k's actual entire interpolation and finite kernel:

\[
 E(s)=\frac{\sqrt\pi\,4^{-s}I(s+1/2)}{Z\Gamma(s+1/2)},
 \qquad B_d(s)=\frac{d!}{\prod_{k=0}^d(s-k)},\qquad Z>0.
\]

Here I, Z and the principal branches have the normalization of C048a,
C048j and C048k. In particular C048j's audited relative estimate is
available, with

\[
 S(p)=\frac{8\pi^{5/2}e^{9w/4}}{\sqrt{p(1+w)}}
       \exp\{2p\operatorname{Log}(w/2)-2p/w\},\quad
 w=W_0(2p/\pi),
\]
\[
 \left|I(p)/S(p)-1\right|
 <\frac{17}{10}\frac{(\log|p|)^{9/2}}{|p|}
 \quad\left(|p|\ge e^{12},\quad
       \Re p\ge-\frac{|p|}{4\log|p|}\right).                 \tag{1}
\]

Let d>=3 be an integer tending to infinity and put

\[
 \ell=\log d,\quad h=d/\ell,\quad D=d/\ell^2,
 \quad c=-1/4,\quad b=d+1/2,\quad F_d(s)=E(s)B_d(s).
\]

Let R_d be the positively oriented rectangle with real edges c,b
and heights +-h. Define the exact absolute closing contribution

\[
 A_d=\frac1{2\pi}\int_{\text{top, right and bottom of }R_d}
                  |F_d(s)|\,|ds|.                           \tag{2}
\]

No sign of a Jensen polynomial, Bernstein representation, zero-class
membership, RH, or infinite-contour opening is assumed.

## Conclusion

For all sufficiently large integers d,

\[
                  A_d\le e^{-D}.                            \tag{3}
\]

More precisely the proof supplies

\[
 \limsup_{d\to\infty}\frac{\log A_d}{D}
                  \le-(\pi-1/2)<-1.                         \tag{4}
\]

C048k's finite identity therefore retains an upward left segment as

\[
 \frac{J_d(-1)}{\gamma_0}
 =\frac{(-1)^{d+1}}{2\pi i}\int_{c-ih}^{c+ih}F_d(s)\,ds
       +\mathcal R_d,\qquad |\mathcal R_d|\le e^{-D}.        \tag{5}
\]

This is a REPRODUCTION specialization of the previously assessed
Rice/gamma tools and local Mellin estimate, not a claimed advance
beyond the inspected literature. It pays only this absolute closing
budget at x=-1, with an existential onset. It supplies no signed
margin for the left integral, other x, root count, C028b's H_d=o(d),
C028g's S_F=0, mixed positivity, or resolution of RH. Independent
conceptual audit1662 below accepts this bound without correction.

## Proof

### 1. Imported tools and uniform domains

Reuse the exact normalization, sample values and finite Rice identity
of C048k. Its standard input is P. Flajolet and R. Sedgewick,
*Mellin transforms and asymptotics: Finite differences and Rice's
integrals*, Theoret. Comput. Sci.144(1995),101--124,
[Section2 Lemma1/(6), pp104--105](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf).
The polynomial-growth openings of Section2/(7) and Section4 Theorem2
are not invoked. The present proof specializes the finite identity;
reproving that theorem or C048j would add no needed input.

Import sectorial Stirling with its complex remainder from NIST DLMF,
version1.2.8, [5.11.1 and 5.11(ii), first remainder paragraph](https://dlmf.nist.gov/5.11).
For Re(z)>0, choose the analytic gamma logarithm real on z>0 and set

\[
 H(z)=(z-1/2)\operatorname{Log}z-z+\tfrac12\log(2\pi).
\]

Truncating before the first Bernoulli term gives

\[
 |\log\Gamma(z)-H(z)|
 \le \frac{\sec^2(\arg z/2)}{12|z|}
 \le\frac1{6|z|},\qquad
 \log|\Gamma(z)|=\Re H(z)+O(1/|z|).                         \tag{6}
\]

The last bound is uniform throughout this right half-plane. The gamma
logarithm need not be the principal logarithm of its value; taking
its real part always gives log|Gamma(z)|. Also import gamma
recurrence/reflection from [DLMF5.5.1/5.5.3](https://dlmf.nist.gov/5.5),
and nonvanishing from [DLMF5.2(i)](https://dlmf.nist.gov/5.2).
The hypotheses, remainder and distinction from bounded-real-part or
fixed-shift asymptotics were inspected in source-notes1660. No
fixed-shift gamma equivalent with a growing shift is used here.

On the top and bottom, p=s+1/2 has Re(p)>=1/4 and |p|>=h.
On the right it has Re(p)=d+1 and |p|>=d+1. On all three pieces
|p|<=2d eventually. Thus (1) applies everywhere for large d, with
the common error bound

\[
 \epsilon_d=\frac{17}{10}\frac{(\log(2d))^{9/2}}h\to0.       \tag{7}
\]

In particular I and S are nonzero there once epsilon_d<1/2, and
their logarithmic moduli differ by at most 2 epsilon_d. This is
a uniform comparison over every point of all three edges.

We will repeatedly use the following uniform consequence of C048a's
principal-branch result. For the right-half-plane p used here, write
w=U+iV. Then U>0, |V|<pi/2, V has the sign of Im(p), and

\[
 U+\log|w|=\log(2|p|/\pi),\qquad
 |w|\le2\ell,\quad U=O(\ell),\quad |1+w|\ge1              \tag{8}
\]

for all sufficiently large d, uniformly on the three edges.
To justify the uniform large-d assertion, U<1 would imply
|w|e^U<e(1+pi/2), contradicting |p|>=h tending to infinity.
Once U>=1, |w|>=1, so U<=log(4d/pi) and
|w|<=U+|V|<=log(4d/pi)+pi/2<=2 ell eventually. The same argument
handles the positive real points, where V=0. These statements use
the actual W equation, not an unproved growing-argument expansion.

### 2. Whole horizontal edges via a decreasing main term

Work first on s=x+ih, c<=x<=b. Put

\[
 p=s+1/2,\quad z=s+1,\quad q=d+1-s.
\]

All three arguments have positive real part and modulus at least h.
Reflection and recurrence give the exact identity on this edge

\[
 B_d(s)=\frac{(-1)^d\pi\Gamma(d+1)}
                 {\sin(\pi s)\Gamma(z)\Gamma(q)}.            \tag{9}
\]

Indeed B_d=d! Gamma(s-d)/Gamma(s+1), and reflection at s-d
has sin(pi(s-d))=(-1)^d sin(pi s). No integer s lies on this
edge; all uses of reflection and every denominator in (9) are valid.
Moreover

\[
 \log|\sin(\pi(x+ih))|=\pi h-\log2+O(e^{-2\pi h})            \tag{10}
\]

uniformly in x: factor its modulus as
(e^(pi h)/2)|1-e^(-2pi h+2pi i x)|.

Define the following exact real main-term function (including S):

\[
 G_d(x)=\log\frac{2\pi\sqrt\pi\,\Gamma(d+1)}Z
       -x\log4+\log|S(p)|-\pi h
       -\Re\{H(z)+H(p)+H(q)\}.                             \tag{11}
\]

Equations (1), (6), (9), (10) imply

\[
 \log|F_d(x+ih)|=G_d(x)+O(\epsilon_d+1/h+e^{-2\pi h}),       \tag{12}
\]

with a constant independent of d,x. We differentiate only the
explicit main term G_d, never an asymptotic remainder.

Differentiating w e^w=2p/pi gives w'=w/(p(1+w)). Direct
logarithmic differentiation of the displayed exact S yields

\[
 \frac{S'(p)}{S(p)}
 =2\operatorname{Log}(w/2)+\frac94 w'
       -\frac1{2p}-\frac{w'}{2(1+w)}.                       \tag{13}
\]

For the exponent, the two differentiated w terms cancel because
2p w'(1+w)/w^2=2/w. Since U>0,
|w/(1+w)|<=1; hence |w'|<=1/|p|<=1/h. Using (8), (13)
therefore gives

\[
 \frac{d}{dx}\log|S(p)|
       \le2\log\ell+\frac{13}{4h}.                         \tag{14}
\]

This is valid even when log|w/2| is negative, since
2 log(|w|/2)<=2 log ell. The chosen branch of S is nonzero;
the real derivative is Re(S'/S), independent of any logarithm of
the value S itself.

Since H'(v)=Log(v)-1/(2v), q'=-1, and
|q|<=2d, |z|,|p|>=h on the whole top, (11)--(14) imply

\[
 \begin{split}
 G_d'(x)
 &\le-\log4+2\log\ell+\log|q|-\log|z|-\log|p|
                                      +\frac{19}{4h}\\
 &\le-\log d+4\log\ell-\log2+\frac{19}{4h}
 \le-\tfrac12\ell
 \end{split}                                                \tag{15}
\]

eventually, uniformly in x. The 19/(4h) includes the three
1/(2v) corrections in the H derivatives. Thus G_d(x)<=G_d(c).
Together with the uniform error in (12), this proves

\[
 \sup_{c\le x\le b}\log|F_d(x+ih)|
                  \le\log|F_d(c+ih)|+o(1).                 \tag{16}
\]

In particular no unexamined intermediate part of the horizontal
edge can exceed the left-corner scale by a fixed exponential loss.

### 3. Left-corner scale and its positive margin

There is a second exact recurrence identity

\[
 B_d(s)=(-1)^{d+1}\frac{\Gamma(d+1)\Gamma(-s)}
                                  {\Gamma(d+1-s)}.          \tag{17}
\]

At s=c+ih, p=1/4+ih and -s=conjugate(p), so
|Gamma(-s)|=|Gamma(p)|. Equation (17) and the exact E
normalization consequently give, without a gamma approximation,

\[
 |F_d(c+ih)|=\frac{\sqrt\pi\,4^{1/4}}Z
       |I(1/4+ih)|\frac{\Gamma(d+1)}{|\Gamma(d+5/4-ih)|}.
                                                               \tag{18}
\]

Reuse the audited conclusion of C048k Section4/(11), proved there
from (1) and the principal W equation:

\[
 \log|I(1/4+ih)|=-(\pi+o(1))\frac h{\log h}.
                                                               \tag{19}
\]

This is a limit for every sufficiently large real h, not a fixed-d
claim about B_d. Substitution h=d/ell into this I-only statement is
legitimate. Since log h=ell-log ell, h/log h=(1+o(1))D.

For clarity the simultaneous gamma-quotient estimate in (18) is
proved from the uniform full-argument formula (6). Put n=d+1 and
u=1/4-ih. Along the segment n+theta u, 0<=theta<=1,
|n+theta u|>=n and

\[
 H'(n)=\log n-1/(2n),\quad H''(n)=1/n+1/(2n^2),\quad
 H'''(v)=-1/v^2-1/v^3.
\]

Taylor's formula along that complex segment therefore has remainder
O(|u|^3/n^2), with an absolute constant. Taking real parts and
using Re(u)=1/4, Re(u^2)=1/16-h^2, then (6), gives

\[
 \log\Gamma(n)-\log|\Gamma(n+u)|
 =-\tfrac14\log n+\frac{h^2}{2n}
       +O(1/n+h^2/n^2+(1+h)^3/n^2)
 =(\tfrac12+o(1))D.                                        \tag{20}
\]

Here log n=o(D), h^2/n=(1+o(1))D and
(1+h)^3/n^2=O(d/ell^3)=o(D). Thus this expansion uses a
small relative displacement u/n, not a fixed shift. Equations
(18)--(20) establish

\[
 \log|F_d(c+ih)|=-(\pi-1/2+o(1))D.                          \tag{21}
\]

Equations (16), (21) bound the complete top edge at this scale.
C048k's conjugation symmetry gives F_d(conjugate(s))=
conjugate(F_d(s)), so the identical uniform bound holds on the
complete bottom edge, with no extra hypothesis or omitted corner.

### 4. Complete right edge, including its middle

Let s=b+it, |t|<=h, and p=a+it with a=d+1. The original finite
product immediately gives the uniform estimate

\[
 |B_d(b+it)|\le\frac{d!}{\prod_{j=0}^d(j+1/2)}\le2,         \tag{22}
\]

because the first factor is 1/2 and j+1/2>=j for j>=1.
Thus no large-argument estimate for q=1/2-it is required,
including at t=0 or on any compact part of this edge.

For w=U+iV corresponding to p, (8) holds; t and V have the
same sign. Consequently t arg(w)>=0 and
Re(p/w)=(aU+tV)/|w|^2>0. Taking the real part of the exact
formula for S and dropping these nonpositive contributions gives

\[
 \begin{split}
 \log|S(p)|={}&\log(8\pi^{5/2})+\tfrac94U
   -\tfrac12\log|p|-\tfrac12\log|1+w|
   +2a\log(|w|/2)-2t\arg w-2\Re(p/w)\\
 &\le 2a\log\ell+O(\ell),
 \end{split}                                                \tag{23}
\]

uniformly for |t|<=h. This also holds at t=0, where w>0.
For gamma, (6) and |atan(t/a)|<=|t|/a give

\[
 \log|\Gamma(a+it)|
 \ge(a-1/2)\log a-a-t^2/a+\tfrac12\log(2\pi)-O(1/a).
                                                               \tag{24}
\]

Indeed Re H(p)=(a-1/2)log|p|-t arg(p)-a+log(2pi)/2,
|p|>=a, and 0<=t arg(p)<=t^2/a. Using (1), (7),
(23), (24) and the factor 4^(-b) in E gives uniformly

\[
 \log|E(b+it)|
 \le-d\log d+2d\log\ell+O(d)
 \le-\tfrac12d\log d                                      \tag{25}
\]

eventually. The term t^2/a is at most O(d/ell^2) and is included
in the displayed O(d). Equations (22), (25) bound every point
of the right edge by 2 exp(-d log(d)/2). In particular the
bounded reflected gamma argument at its midpoint was neither
approximated nor deleted.

### 5. Integration lengths, threshold and finite remainder

The two horizontal lengths are b-c=d+3/4 each; the right length
is 2h. They are O(d), and log d=o(D). Thus (16), (21), (22),
(25) yield

\[
 A_d\le\frac1{2\pi}\left[
 2(d+3/4)\exp\{-(\pi-1/2+o(1))D\}
       +4h\exp\{-d\log d/2\}\right].                      \tag{26}
\]

The second term has logarithm divided by D tending to -infinity;
the logarithms of the lengths and fixed factors divided by D
tend to zero. This proves (4). Since pi-1/2>1, (4) implies
(3) for all sufficiently large integers d, with no effective
onset asserted. These are bounds on full edge integrals, not
numerical samples or an oversized undecisive upper envelope.

Finally C048k's positive finite rectangle traverses the left edge
downwards. Its contribution to (-1)^d/(2pi i) times the boundary
integral is the upward segment with prefactor (-1)^(d+1)/(2pi i).
The other three contributions have modulus at most A_d by the
triangle inequality. This proves (5) without an infinite-contour
limit. In particular the fixed-d absolute divergence in C048k is
preserved: its limit takes h to infinity with d fixed, whereas the
present estimate couples h=d/log d to growing d.

The remaining signed comparison and height/sign implications are
independent gaps; none follows from taking an absolute value in
(2) or from the finite identity (5).

### 6. Independent conceptual audit1662

This audit reuses the unchanged SPECIALIZE assessment1659 and its
primary-source ledger1660. It checks the whole joint-limit argument,
including C048k's I-only limit and normalization, against the audited
C048a/C048j contracts. It accepts (3)--(5) without changing their
statement, proof or inputs. This is verification of a local
REPRODUCTION specialization, not a new bound beyond Section5 or
progress beyond the literature already assessed.

**Uniform comparison and branches.** On the horizontal edges
Re(p)>=1/4 and |p|>=h, and on the right Re(p)=d+1.
The common upper bound |p|<=2d holds eventually, so (7) bounds
the error at every edge point. In particular epsilon_d is
O(ell^(11/2)/d) and tends to zero. For epsilon_d<1/2,
1-epsilon_d<=|I/S|<=1+epsilon_d and
|log|I/S||<=2epsilon_d. Thus logarithmic modulus comparison
is justified and I has no zero on these edges. No derivative
bound on I/S is being inferred. C048a gives U>0 and |V|<pi/2
with the correct sign, also on open neighborhoods. The W modulus
identity and |p|>=h force U>=1 uniformly eventually, after which
|w|<=2ell follows exactly as in (8). All powers and derivatives
of the nonzero S use that same branch.

**Horizontal normalization and monotonicity.** Reflection at s-d
gives the parity (-1)^d in (9); recurrence gives precisely one
factor each of Gamma(s+1) and Gamma(d+1-s). The third gamma
in (11) is Gamma(p) from E. For x in [c,b] these three full
arguments have positive real part and modulus at least h. The
sectorial remainder (6) is therefore O(1/h) uniformly, including
both corners. The sine factor has a uniform O(exp(-2pi h))
logarithmic error. Together with the two-sided I/S comparison,
this verifies (12) uniformly, not just pointwise in x.

The exact differentiation in (13) retains the prefactor derivative.
The exponent derivative is 2 Log(w/2): the remaining terms are
2p w'(1+w)/w^2-2/w=0. The other three terms have total modulus
at most (9/4+1/2+1/2)/h=13/(4h). The three H derivatives
add at most 3/(2h), giving 19/(4h). Also |q|<=2d uniformly;
h=d/ell then gives the second line of (15) with its stated
constant -log2. Its right side is at most -ell/2 eventually.
Only G_d has been differentiated. Writing the uniform error in
(12) as r_d(x), the precise deduction is

    log|F_d(x+ih)| <= log|F_d(c+ih)|
                         +2 sup_(c<=y<=b)|r_d(y)|.

The last term tends to zero independently of x. This validates
(16) without any analytic information about a derivative of the
Mellin or Stirling error, and without multiplying that error by
the length of the edge.

**Corner scale in the simultaneous limit.** Equation (17) follows
from recurrence with d+1 factors, so its parity is (-1)^(d+1).
At c=-1/4, -s is exactly the conjugate of p. Gamma conjugation
cancels their moduli in (18), leaving the actual I and one full
large-argument gamma quotient. Z=gamma_0 is a fixed positive
constant from C048k; it is not allowed to depend on d.

C048k Section4/(11) concerns I(1/4+it) alone as real t tends
to infinity. Its derivation uses U/log t->1, V->pi/2 and the
two-sided I/S bound, and contains no fixed-degree estimate.
It is therefore valid at t=h_d; h_d/log h_d=(1+o(1))D.
In the gamma quotient, n=d+1 and u=1/4-ih give
Re(n+theta u)>=n on the entire Taylor segment. Thus
|H'''(n+theta u)|<=1/n^2+1/n^3. Taylor's integral remainder
is bounded by (|u|^3/6)(1/n^2+1/n^3). The linear and quadratic
real parts give -log(n)/4+h^2/(2n) with precisely the smaller
terms in (20); both Stirling remainders are O(1/n).
The potentially largest discarded term, h^3/n^2, is O(D/ell),
and log n=o(D). Hence the quotient contributes +(1/2+o(1))D,
whereas I contributes -(pi+o(1))D. This verifies the sign and
strict coefficient pi-1/2 in (21). Conjugation treats the whole
bottom edge, with the identical modulus, rather than just its
left endpoint.

**The full right edge.** Re(s-k)=d+1/2-k is positive for every
k=0,...,d. Taking moduli factor by factor therefore gives (22)
for all |t|<=h; no reflected gamma argument is used here.
For p=d+1+it, t arg(w)>=0 and aU+tV>0, so dropping the two
nonpositive exponent contributions in (23) is legitimate for
either sign of t, including zero. The remaining prefactor is
O(ell) uniformly. In (24), a-1/2>0 and
0<=t arg(a+it)<=t^2/a, giving the asserted lower gamma bound.
Here |p|>=a, so the gamma remainder is uniformly O(1/a).
Consequently (25) is uniform even at the midpoint t=0. Its
dominant term -d log d is not offset by 2d log ell+O(d).

**Common onset, integration and finite identity.** Every eventual
condition above holds for all d beyond a fixed onset, with constants
independent of the edge parameter. There are finitely many such
conditions, so they have a common onset. The two horizontal lengths
are each d+3/4, and the vertical length is 2h. Since
log d/D->0 and (d log d)/D=ell^3->infinity, these lengths and
the fixed 1/(2pi) normalization yield exactly the limsup in (4).
For example choose any eta with 0<eta<pi-3/2. The limsup gives
log A_d/D<=-(pi-1/2)+eta<-1 for all sufficiently large d,
which proves the requested threshold. No effective onset is supplied.

The finite positively oriented rectangle has its left edge downward;
reversing only that edge gives the sign (-1)^(d+1) in (5).
The triangle inequality pays the other three edges by A_d. There
is no infinite-contour limit and no conflict with C048k's fixed-d
divergence. The audit uses exactly C048a, C048j and C048k as
direct local mathematical inputs; their underlying results are
reused through those established statements. The direct DAG row
requires no change. No script, numerical sample or source extension
is part of this verification. Signed cancellation, other x, and
sufficient height or positivity implications remain unproved.

## Mathlib

Full matching coverage for this actual-E joint degree/height edge
estimate has not been checked; availability is unknown. No absence
or formal verification is claimed. The imported results are the
precisely cited finite Rice theorem and gamma recurrence, reflection,
nonvanishing and sectorial Stirling remainder. The existing audited
local Mellin estimate and its fixed-real-part I-only asymptotic are
reused. Uniform optimization of their product over these finite edges
is the specialization proved here and checked in audit1662; no
mathematical script or numerical certificate is used.
