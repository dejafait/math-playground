# C759c: A full weighted Fourier-deficit trace pays the fixed complement

## Hypotheses

Use precisely C759a's real closed form Q on zero-extended functions
in L2(-1,1), its logarithmic Fourier form domain Vcal, and its odd
orthogonal complement

\[
 W=\{w:w(-x)=-w(x),\ \langle w,\sin(\pi jx)\rangle=0,
                       \quad 1\le j\le120\}.
\]

Thus F_f(t)=integral_{-1}^1 f(x)e^{-itx}dx, the Fourier measure is
dt/(2*pi), and m(t)=Re psi(1/4+it/2)-log pi. Retain the complete
prime cost and the projected negative odd pole cost from C759a(2):

\[
 C=\sqrt2\frac{\log2}{\sqrt2}
    +\frac{\log3}{\sqrt3}+\frac{\log2}{2}
    +\frac{\log5}{\sqrt5}+\frac{\log7}{\sqrt7},\qquad
 P_{120}=\frac{8\sinh^2(1/2)}{120\pi^2}.
 \tag{1}
\]

The bounded prime/pole lower estimate is Q(w)>=Q_m(w)-(C+P_120)||w||²
for real w in W intersect Vcal, as proved in C759a Section3. No
neutrality, positivity premise, spectral truncation or RH is assumed.
The scalar inputs are C759a(5) and L744(8):

\[
 m(t)\ge m_*=-\log(4\pi)-4\quad(t\in\mathbb R),\qquad
 m(t)\ge h(|t|):=\log\frac{|t|}{2\pi}-\frac2{t^2}
                       \quad(|t|\ge1).                    \tag{2}
\]

L744 specializes the principal-logarithm expansion and complex
remainder in [NIST DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii) on Re z=1/4. Only its
all-real scalar bounds are used, not its modulation-family hypotheses.

The trace inputs are Jan Hamhalter, *Classes of Operators on Hilbert
Spaces*, extended notes dated10 April2008, printed pp18-19,
Definitions5.1/5.5 and Proposition5.2
([author PDF](https://math.fel.cvut.cz/en/people/hamhalte/malta07.pdf)),
and Jordan Bell, *Trace class operators and Hilbert-Schmidt operators*,
18 April2016, Section8 and Theorems19/26
([full author notes](https://jordanbell.info/LaTeX/mathematics/traceclass/)).
These give the basis-independent nonnegative diagonal trace of a
bounded positive operator, the finite-trace criterion and operator
norm bounded by trace for positive trace-class operators. Their
hypotheses are checked below. No rectangular integral-kernel theorem
or source numerical positivity certificate is imported.

## Conclusion

Put kappa(t)=(4-m(t))_+ and s_j(x)=sin(pi*j*x), of norm1. The bounded
positive compression of this multiplier to the complexification of W
is trace class, with trace

\[
 T_4=\sum_{j=121}^{\infty}\int_{\mathbb R}
             \kappa(t)|F_{s_j}(t)|^2\frac{dt}{2\pi}.
 \tag{3}
\]

The complete upper certificate proves

\[
 0\le T_4\le B<0.529<0.8139<4-C-P_{120}-\frac{11}{200},
 \qquad
 B\in(0.52800039426954205,0.52800039426954207).
 \tag{4}
\]

Here B is a majorant, not a computed trace value. For every real
w in W intersect Vcal,

\[
 Q(w)\ge(4-B-C-P_{120})\|w\|_2^2
                   \ge0.3409\|w\|_2^2,
 \tag{5}
\]
\[
 Q(w)-\frac{11}{200}\|w\|_2^2
                   \ge0.2859\|w\|_2^2.                    \tag{6}
\]

The exact coefficient in(6) exceeds0.28591312897062012. This supplies
the fixed shifted complementary prerequisite that C759a's different
two-region estimate did not pay. It does not invalidate that scoped
stop or C759b's arithmetic obstruction. No form-dual coupling bound,
finite Schur sign, actual parity comparison, even simplicity/sign,
Xi realization with multiplicities or global mixed positivity is
established. This is a local REPRODUCTION of assessed standard trace
machinery and scalar bounds, not a claim of a discovery beyond the
sources checked. The separate conceptual and complete arithmetic audit
in Section5 accepts this local bound under the stated hypotheses.

## Proof

### 1. Explicit support and the positive compression

The function m is continuous and real even: the digamma function has
no poles on Re z=1/4 and respects conjugation. The derivative
h'(t)=1/t+4/t^3 is positive for t>=1. The outward certificate below
verifies h(350)>4 and 350<121*pi. Therefore(2) implies kappa(t)=0
for |t|>=350. Globally 0<=kappa<=4-m_*, so kappa is measurable,
bounded and integrable. No asymptotic estimate is applied at t=0.

Let W_C be the closed complex odd subspace orthogonal to s_1,...,s_120.
Let U:W_C -> L2(R,dt/(2*pi)) send a zero-extended function to its
Fourier transform. Plancherel makes U an isometry. Multiplication
M_kappa is bounded and positive, so A=U* M_kappa U is a bounded
positive operator on W_C. This constructs the compression without
assuming that the Fourier image is the entire target L2 space.

The s_j, j>=121, form an orthonormal basis of W_C. Thus the extended
positive diagonal trace of A is exactly(3). It remains to show this
sum is finite before invoking trace-norm domination. This computation
does not presume that A preserves the original real subspace; its
quadratic inequality can simply be restricted to real w afterward.

### 2. Every omitted sine mode

For |t|<=350<121*pi the direct transform in C759a(7) gives

\[
 |F_{s_j}(t)|^2
 =\frac{4\sin^2t}{\pi^2 j^2(1-(t/(j\pi))^2)^2},\qquad j\ge121.
\]

Every denominator in this use is nonzero. Since sin²t<=1,
j>=121 and sum_{j>120} j^(-2)<=integral_120^infinity x^(-2)dx=1/120,

\[
 S(t):=\sum_{j=121}^{\infty}|F_{s_j}(t)|^2
 \le M(|t|):=\frac4{120\pi^2(1-(t/(121\pi))^2)^2}.
 \tag{7}
\]

The right side is increasing on[0,350]. Tonelli applies to the
nonnegative functions in(3), hence, using evenness,

\[
 T_4=\frac1\pi\int_0^{350}\kappa(t)S(t)dt.
 \tag{8}
\]

The Fourier formula is needed only on this support; apparent
removable singularities at omitted frequencies lie outside it.
No sine cutoff replaces the infinite sum in(7) or(8).

On[0,1], kappa<=4-m_* and S<=M(1). On every[k,k+1],
k=1,...,349, monotonicity of h and M gives

\[
 \kappa(t)S(t)\le(4-h(k))_+ M(k+1).
\]

Consequently the explicit finite majorant is

\[
 B:=\frac{(4-m_*)M(1)}\pi
       +\frac1\pi\sum_{k=1}^{349}(4-h(k))_+M(k+1),\qquad T_4\le B.
 \tag{9}
\]

These are upper rectangles for proved majorants, not sampled values
of the weighted integrand. Their widths are exactly1. There is no
omitted quadrature error, signed interchange, or unevaluated tail.
In particular(9) establishes finite trace. The cited positive-trace
criterion makes A trace class; Bell Theorem26 now gives
||A||<=Tr(A)=T_4. Thus for all w in W_C,

\[
 \int\kappa(t)|F_w(t)|^2\frac{dt}{2\pi}
       =\langle Aw,w\rangle\le T_4\|w\|_2^2\le B\|w\|_2^2.
 \tag{10}
\]

### 3. Complete scalar certificate

Run from the notebook:

    python3 scripts/spectral-triples/weighted-fourier-deficit-802.py

The full certificate is
`scripts/spectral-triples/weighted-fourier-deficit-802.json`.
It contains the actual source hash, pi and m_* enclosures, support
checks, the origin term, all349 rectangle factors/contributions,
all five prime-power weights and the original pole cost. It reports

\[
 \begin{split}
 B&\in(0.52800039426954205,0.52800039426954207),\\
 4-C-P_{120}-11/200&\in(0.81391352324016218,0.81391352324016219),\\
 4-B-C-P_{120}-11/200
   &\in(0.28591312897062012,0.28591312897062013).
 \end{split}
 \tag{11}
\]

All comparisons in(4)-(6) use outward endpoints, not these shortened
decimal displays. Decimal intervals have60 significant digits, with
floor/ceiling contexts for basic arithmetic and adjacent representable
endpoints for the correctly rounded ln,exp,sqrt operations. This reuses
the scalar-enclosure convention already assessed and audited for
C759a Section5-6, based on the
[Python Decimal reference](https://docs.python.org/3/library/decimal.html).
All inputs are integers or exact decimal strings. Division excludes0;
in particular 1-(t/(121*pi))² is certified positive at every use.
Positive-part endpoints are taken monotonically. Negation uses
copy_negate rather than ambient-precision unary rounding.

Pi is enclosed by Machin's identity
pi=16 atan(1/5)-4 atan(1/239). Each arctangent uses its first60
alternating terms and a symmetric radius equal to an outward upper
bound for its next term z^121/121. The recurrence maintains an interval
for every power. Thus all constant, logarithm, pole and rectangular
errors enter B and the strict comparison. No digamma evaluation,
Euler gamma value or numerical integration is required. Interpreter
and Decimal correctness remain software trust assumptions; this is
not a formal arithmetic certificate in a proof assistant.

### 4. The closed-form consequence

Pointwise m(t)>=4-kappa(t). For w in C759a's supported logarithmic
form domain, the m integral is well defined, and the kappa integral
is bounded already on L2. Plancherel and(10) therefore imply

\[
 Q_m(w)=\int m(t)|F_w(t)|^2\frac{dt}{2\pi}
        \ge4\|w\|_2^2-\langle Aw,w\rangle
        \ge(4-B)\|w\|_2^2.
\]

Restricting to real W intersect Vcal and applying C759a's complete
bounded prime and projected odd pole estimate proves(5). Subtracting
11/200 times the squared norm and using(11) proves(6). This argument
holds on the full closed domain; it uses neither convergence of a
finite sine matrix nor an extension from unproved finite signs.
It establishes only a complementary floor. The separate coupling
and Schur requirements cannot be dropped on account of this bound.

### 5. Independent conceptual and arithmetic audit — 13 November2026, step804

The separately approved SPECIALIZE assessment
`drafts/literature/2026-11-13-weighted-fourier-deficit-audit-802.md`
covers this exact audit. Equations(3)-(6) survive without a mathematical
correction. This verifies a previously provisional local input; it is
not a new general trace theorem or progress beyond the checked sources.
The original step802 script and certificate are preserved unchanged.

**Compression, support and trace.** The two scalar estimates are used
in their proper regimes. In L744's right-half-plane specialization,
the total error coefficient is at most1/8+1/2+2sqrt(2)/3<2;
C759a's global lower bound handles the origin independently. Since
h'(t)=1/t+4/t^3>0, the verified h(350)>4 excludes the whole exterior,
not just the cutoff point. The verified350<121*pi keeps every
denominator in the infinite sine sum positive on the full support.

Zero extension followed by the Fourier transform is an isometry from
the complex odd complement into L2(R,dt/(2*pi)); surjectivity is not
needed to form U* M_kappa U. The closed odd subspace has the complete
orthonormal sine basis, with norm1 for every sine on(-1,1). Bounded
positivity follows before any trace assertion from0<=kappa<=4-m_*.
The cited Hamhalter/Bell diagonal criterion therefore applies.
Tonelli is justified by nonnegativity; real-even kappa and the even
squared sine transforms give exactly the factor1/pi in(8). Replacing
sin²t by1 and summing j^-2<=1/120 are upper bounds over every omitted
mode. Finite trace follows from the finite majorant(9) before Bell's
operator-norm domination is invoked. No finite-rank approximation of
the complement or assumed sign of Q enters this reasoning.

**Whole intervals and whole domain.** On[k,k+1], monotonicity gives
(4-m(t))_+<=(4-h(k))_+ and M(t)<=M(k+1), both nonnegative.
Thus the product is an upper bound even on the interval containing
the crossing of h=4. The independent intervals certify positive left
deficits for k=1,...,343 and zero left deficits for k=344,...,349;
[343,344] is included with its positive left-end bound. The origin
rectangle covers all of[0,1]; endpoints shared by rectangles have
measure zero. The arithmetic test is consequently not a quadrature
of sampled values of m or a claim of integrand monotonicity.

C759a's supported logarithmic domain makes the m integral absolutely
integrable: m differs from one half log(1+t²) by a bounded function.
The kappa quadratic form is already bounded on the entire L2
complement. Combining(10) with the pointwise inequality m>=4-kappa
gives the lower inequality for Q_m directly on this domain, without
assuming sine-polynomial convergence in form norm. The complete
arithmetic cost is C, with chain norms sqrt2 for log2 and1 for the
four other overlapping prime powers. The audit rechecks the delay
inequalities log7<2<log8, 2log2<2<3log2 and log3>1. There is no
missing factor2: the prime operator is the sum of each shift and its
adjoint. For real odd w the pole product is -2|<w,sinh(x/2)>|²;
projection and the entire inverse-square sine tail bound this below
by-P_120||w||². Subtracting these bounded costs on the same domain
proves the claimed full-form floor, including the unfavorable pole.

**Complete independent arithmetic.** Reproduce with

    python3 scripts/spectral-triples/weighted-fourier-deficit-audit-804.py

The full certificate is
`scripts/spectral-triples/weighted-fourier-deficit-audit-804.json`.
All2147 checks pass. Every saved constant, origin term, all349
rectangle factors and contributions, all five prime weights and chain
norms, pole cost, sum and final bound is checked by containment in
the original outward interval. Every majorant denominator is positive;
every positive-part branch is resolved. The original source hash and
a byte-identical replay at ambient Decimal precision7 are also checked,
with the replay isolated under `scripts/spectral-triples/audit-804/`.
Replay is supplemental, not the independent arithmetic argument.

Independent basic operations use exact Fraction endpoints. After each
operation a lower endpoint a is replaced by floor(10^90 a)/10^90
and an upper endpoint b by ceil(10^90 b)/10^90. This explicit outward
rational rounding controls denominator growth. The60-term Machin sums
and next-term radii are evaluated as exact rationals. For monotone
ln, exp and sqrt, rational arguments are first converted outward at
110 significant decimal digits, their correctly rounded evaluations
are expanded to adjacent representable endpoints, then enclosed on
the rational grid. This is the same assessed Decimal convention with
tighter precision, not reliance on the step802 implementation's basic
interval arithmetic. The complete independent intervals imply

\[
 B<0.528000394269542058<0.813913523240162181
       <4-C-P_{120}-11/200,
\]
\[
 4-B-C-P_{120}-11/200>0.285913128970620124>0.2859.
\]

The certified number B remains a majorant, not a trace evaluation.
Python integer/Fraction arithmetic and Decimal correctness remain
software trust assumptions; this is not a proof-assistant replay.
No form-dual coupling, finite Schur positivity, actual parity gap,
even simplicity/sign or Xi realization with multiplicities has been
verified. C759a/C759b/L743's differently scoped stops remain intact.

## Mathlib

Full matching coverage of this fixed Fourier-deficit compression,
all-mode enclosure and numerical threshold has not been checked.
Plancherel, positive-operator trace domination, sine completeness and
the digamma asymptotic remainder are supporting named results used
with the precise sources and qualifications above. No Mathlib absence
or formal verification is inferred from the unchecked status.
