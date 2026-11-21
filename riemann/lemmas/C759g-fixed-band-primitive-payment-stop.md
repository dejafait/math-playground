# C759g: The fixed bands 1,2 do not pay the first-sine correction

## Hypotheses

Use C759a's complete real closed Weil form on zero-extended functions
supported in [-1,1], with Fourier convention and correction

\[
 F_u(t)=\int_{-1}^1u(x)e^{-itx}\,dx,\quad
 m(t)=\Re\psi(1/4+it/2)-\log\pi,
\]
\[
 E(u)=2F_u(i/2)F_u(-i/2)
 -2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}C_u(\log n),
 \qquad C_u(y)=\int u(x+y)u(x)\,dx.
 \tag{1}
\]

Thus Q(u)=integral m|F_u|^2 dt/(2*pi)+E(u), with the logarithmic
Fourier form domain specified in C759a. In particular Lambda(4)=log2.
For unit odd f let Pf(x)=integral_-1^x f(u)du on [-1,1], zero outside,
and h_f=||Pf||_2^2. When h_f>0 define

\[
 R(f)=E(Pf)/h_f-E(f),\qquad
 p_1(f)=\int_{|t|\le1}|F_f(t)|^2\frac{dt}{2\pi},\quad
 p_2(f)=\int_{|t|\ge2}|F_f(t)|^2\frac{dt}{2\pi},
\]
\[
 B_{1,2}(f)=\frac{p_1(f)p_2(f)}{h_f}
             (m(2)-m(1))\frac34.                         \tag{2}
\]

These definitions are the fixed candidate payment test of assessment817,
not an assumed covariance inequality. Its source motivation is Fabio
Zucca, *An inequality for correlated measurable functions*,
[author-hosted manuscript](https://zucca.faculty.polimi.it/papers/inequality/inequality.pdf),
Lemma3.3/(3.6), p5, and the separated-region estimate in the proof of
Theorem3.1, pp5-6, in the probability-measure case. We do not specialize
that theorem to the full odd form domain here. Its factor/product
integrability and signed domination remain separate obligations.

The input is exactly s(x)=sin(pi*x). C759d(2) certifies
||s||=1 and Q(s)<0.00364123566126519<1/250, so it belongs to the
prescribed unit cap. C759f supplies its actual primitive and domain.
No RH, neutrality, parity ordering or zero-free-region estimate is assumed.

## Conclusion

At this eligible input, the complete-error interval certificate gives

\[
\begin{array}{c|rr}
 R(s)&1.2337657779&1.2337657780\\
 p_1(s)&0.0397677932&0.0397681981\\
 p_2(s)&0.7475910562&0.7475942943\\
 m(1)&-2.025298776&-2.025024115\\
 m(2)&-1.161709680&-1.161435013\\
 B_{1,2}(s)&0.0633292503&0.0633704662
\end{array}                                                   \tag{3}
\]

where both columns are strict outward bounds. In particular

\[
 1.17039531<R(s)-B_{1,2}(s)<1.17043653.                    \tag{4}
\]

The proposed sufficient estimate R(f)<=B_(1,2)(f) on the full capped
odd domain is therefore false. Stop this fixed-band sufficient estimate;
no band/mode/cap variation is tested. This does not refute normalized
primitive lowering: C759f's strict comparison on the two-sine slice
remains intact. Full covariance can exceed a single rectangle resource.
Even ground-state sign/simplicity, parity infima, other windows, Xi
realization and L030-L032/C032a actual-Xi mixed positivity remain open.

This is a local negative certificate obtained by REPRODUCTION of the
assessed standard methods, with no claim of a new general theorem or
originality beyond the sources checked. The separate independent audit
in Section5 accepts this scoped stop. The qualification is numerical software trust, not a missing
infinite tail: every analytic remainder used below is bounded.

## Proof

### 1. Actual primitive and complete signed correction

By C759f(3) put g(x)=-1-cos(pi*x), so Ps=g/pi,
||g||^2=3 and h_s=3/pi^2>0. The continuous zero extensions of s and g
are in H1(R), hence in the stated form domain. Since E is quadratic,

\[
 R(s)=E(g)/3-E(s).                                       \tag{5}
\]

C759f(8),(10), or their elementary integrations, specialize as follows.
Writing alpha=2*pi*sinh(1/2)/(pi^2+1/4), the four pole values are

\[
 F_s(i/2)=\alpha,\quad F_s(-i/2)=-\alpha,
 \qquad F_g(i/2)=F_g(-i/2)=-2\pi\alpha.
\]

Thus the pole contribution to (5) is
2*alpha^2*(1+4*pi^2/3)>0. Both poles and the odd negative pole
product have been retained. For 0<=y<=2 the correlations are

\[
 C_s(y)=(1-y/2)\cos(\pi y)+\frac{\sin(\pi y)}{2\pi},
\]
\[
 C_g(y)=(2-y)(1+\tfrac12\cos(\pi y))
                         +\frac{3\sin(\pi y)}{2\pi}.
\]

For clarity, the latter integrates 1, the two individual cosines, and
their product on [-1,1-y]: these contribute respectively 2-y,
2*sin(pi*y)/pi, and (2-y)*cos(pi*y)/2-sin(pi*y)/(2*pi).
Hence C_g(y)/3-C_s(y)=(2-y)(1-cos(pi*y))/3, and exactly

\[
 R(s)=2\alpha^2(1+4\pi^2/3)
 -\frac23\sum_{n\in\{2,3,4,5,7\}}
 \frac{\Lambda(n)}{\sqrt n}(2-\log n)(1-\cos(\pi\log n)). \tag{6}
\]

The signed prime part is about -1.73068373684512; the pole part is
about 2.96444951480281. These orientation decimals do not enter the
proof: the certificate encloses (5) from the unsimplified correlations
and also checks enclosure overlap with each term of (6). Their equality
is the preceding algebra, not an inference from numerical overlap.
There are exactly five overlapping prime powers because log7<2<log8;
6 is not a prime power. No absolute-value replacement is made.

### 2. Digamma evaluation and complete series tails

Import [NIST DLMF5.7.6](https://dlmf.nist.gov/5.7.E6): for z away
from the nonpositive integers,

\[
 \psi(z)=-\gamma-\frac1z+
         \sum_{k=1}^{\infty}\left(\frac1k-\frac1{k+z}\right).
\]

For z=a+ib, a=1/4 and b=t/2, t=1,2, there are no excluded poles.
Its real part has terms

\[
 d_k=\frac1k-\frac{k+a}{(k+a)^2+b^2}
 =\frac{a(k+a)+b^2}{k((k+a)^2+b^2)},\qquad
 0<d_k\le\frac a{k^2}+\frac{b^2}{k^3}.
\]

This proves absolute convergence and, by decreasing-integrand comparison,
the complete bound after k=N=8192:

\[
 0\le\sum_{k>N}d_k\le a/N+b^2/(2N^2).                  \tag{7}
\]

For gamma use its defining limit gamma=lim(H_M-log M).
The identity
H_N-log N-gamma=sum_(k=N)^infinity[log(1+1/k)-1/(k+1)]
follows by telescoping finite sums and taking that limit. Each summand
lies between 0 and 1/k-1/(k+1), by integrating 1/x over [k,k+1].
Thus

\[
 H_N-\log N-1/N\le\gamma\le H_N-\log N,\quad N=4096.     \tag{8}
\]

Finite outward sums with (7)-(8), the term -a/(a^2+b^2) and
-log(pi) give the two m intervals in (3). DLMF5.15.1, assessed as
supporting coverage, is not needed here. No monotonicity or derivative
series is assumed, and no gamma-energy integral is recomputed.

### 3. Compact Fourier integrals and their complete errors

C759d(4) gives, on |t|<=2<pi,

\[
 q(t):=|F_s(t)|^2=
          \frac{4\pi^2\sin^2t}{(\pi^2-t^2)^2}.           \tag{9}
\]

All its denominators are strictly positive before squaring. Real s
makes q even. The defining Fourier integral is twice continuously
differentiable by compact support and dominated differentiation. From
||s||_2=1 and Cauchy--Schwarz,
|F_s^(j)(t)|<=sqrt(2/(2j+1)) for j=0,1,2. Therefore

\[
 |q''(t)|\le2|F_s'(t)|^2+2|F_s''(t)||F_s(t)|
       \le\frac43+\frac4{\sqrt5}<4                     \tag{10}
\]

on the whole real line. For L=1,2 use N=512 equal cells in [0,L]
with midpoints t_j=L*(2j+1)/(2N). Taylor expansion about each midpoint
with second derivative bounded by4, integrated over the symmetric
cell of width Delta=L/N, gives error at most 4*Delta^3/24; the linear
term integrates to zero. Summing gives the complete midpoint estimate

\[
 \left|\int_0^Lq(t)dt-
          \frac LN\sum_{j=0}^{N-1}q(t_j)\right|
       \le\frac{4L^3}{24N^2}.                            \tag{11}
\]

Divide the resulting interval by pi to obtain the entire mass on
|t|<=L. Plancherel for the stated dt/(2*pi) convention gives total
mass ||s||^2=1. Thus p1 is the L=1 mass and p2=1-(L=2 mass);
endpoints have zero measure. This pays the entire infinite complement
without a tail approximation. The possible inverse-frequency covariance
singularity at zero is not used in (9)-(11), nor assumed integrable
for other inputs. These are finite integrals of the smooth q itself.

### 4. Arithmetic, certificate and scope

Run from the notebook:

    python3 scripts/spectral-triples/fixed-band-payment-819.py

The full certificate is `scripts/spectral-triples/fixed-band-payment-819.json`.
It retains all 4096 harmonic terms, both sets of 8192 digamma terms,
all 512 midpoint records for each compact interval, analytic remainder
intervals, both signed pole energies and all five signed prime terms,
constants, actual norm, result intervals, threshold0, checks and failures.
All12 checks pass. Its exact interval for R-B has lower endpoint
1.17039531185096879944858096040279375622365249981076659756748
and upper endpoint
1.17043652760178537701479079496090920050455252445824202218568.
These imply (3)-(4), directly using the full intervals rather than
rounded table entries. Multiplication is valid without covariance
assumptions; the certificate also verifies p1,p2 in(0,1), h>0 and
m(2)-m(1)>0.

Arithmetic definitions are extracted from the AST prefix of the audited
`scripts/spectral-triples/two-sine-primitive-814.py`, ending before
class Z. No matrix computation or previous numerical certificate is
executed. The new certificate records hashes of its generating script and
that arithmetic source. C759f Section4 documents its 60-digit outward
Decimal operations; negation is context independent, division excludes
zero, and ln/exp/sqrt endpoints are expanded by adjacent representable
values. Correct rounding of those primitives is documented in the
[Python Decimal specification](https://docs.python.org/3/library/decimal.html).
Pi uses Machin's identity with60 alternating arctangent terms and
next-term error. Sine/cosine use60 Taylor terms after reducing by an
integer multiple of2*pi; each reduced argument is checked below4.
Twice the absolute next term bounds the entire remaining series since
subsequent term ratios are below1/2. This includes trig error at every
prime delay and every midpoint, as well as finite arithmetic rounding.
Python/Decimal and the elementary identities are software/mathematical
trust assumptions; this is not a formal verification claim.

The strict positive lower endpoint is a counterexample to precisely
R<=B_(1,2) on this cap. We have not identified the full archimedean
decrease with this small rectangle, assumed a general covariance
specialization, or inferred a positive actual normalized-Q defect.
It is consistent with C759f's negative actual defect. The present
calculation supplies a stopping decision for the sufficient estimate,
not a counterexample to parity, to primitive lowering, or to RH.

### 5. Separate independent audit — 13 November2026, step821

The invocation-start SPECIALIZE assessment819, separately approved in820,
covers this exact audit, classified REPRODUCTION. The complete proof,
generator, inherited814 arithmetic and relevant C759a/d/f inputs were
inspected. Reuse the primary-source statements and domains in that
assessment; neither an additional source claim nor a broader inequality
is imported. No mathematical correction was needed.

**Hypotheses, signs and complete analytic errors.** Direct integration
gives Ps=(-1-cos(pi*x))/pi and its squared norm3/pi². Both s and g
vanish at the support endpoints, so their zero extensions are H1 and
belong to the logarithmic form domain. C759d's already audited cap is
the eligibility input; a comparison with0.004 alone does not establish
Q(s)'s value. At the positive imaginary pole, direct real integration
gives Fs=2pi*S/d and Fg=-4S+S/d, where S=sinh(1/2), d=pi²+1/4.
At the negative pole the odd value reverses sign and the even value
agrees. Thus the odd pole energy is negative, the even pole energy
positive, and their normalized difference is precisely(6)'s pole term.
Product-to-sum integration on[-1,1-y] gives both displayed correlations
and Cg/3-Cs=(2-y)(1-cos(pi*y))/3. All five prime-power corrections are
retained with their signs; Lambda4=log2 and log7<2<log8 exclude any
unpaid overlap. Enclosure overlap is an arithmetic check, not the proof
of the correlation identity.

For the DLMF partial fractions, a>0 makes the displayed d_k positive;
its rational expression is bounded by a/k²+b²/k³. Integrating these
decreasing majorants from N to infinity bounds the entire tail(7).
In(8), finite telescoping followed by the defining gamma limit gives
the stated remainder starting at k=N. The inequalities
1/(k+1)<=log(1+1/k)<=1/k pay every summand and telescope its upper
majorant to1/N. No asymptotic remainder sign is assumed.

Compact support permits two dominated Fourier differentiations.
Cauchy--Schwarz gives the three stated derivative bounds, hence
|q''|<=4/3+4/sqrt5<4. The midpoint linear term integrates to zero;
integrating the quadratic remainder on each whole cell gives(11).
Evenness supplies the factor1/pi. Plancherel supplies the entire
complement p2=1-mass(|t|<=2), including all unbounded frequencies.
No inverse-frequency covariance integral or zero-frequency limiting
argument is used. Thus every infinite series or integral omitted from
the finite calculation has a complete analytic bound.

**Complete independent arithmetic.** Run from the notebook:

    python3 scripts/spectral-triples/fixed-band-payment-audit-821.py

The full evidence is `scripts/spectral-triples/fixed-band-payment-audit-821.json`.
Original819 and814 artifacts are preserved. Exact-byte copies replay
under ambient Decimal precision7 in `scripts/spectral-triples/audit-821/`.
Every parsed field agrees except the explicitly checked relative path
of the copied arithmetic source, which changes with its directory.
Generator and arithmetic hashes agree. The actual runtime is
Python3.15.2/libmpdec4.0.1. Both explicit60-digit contexts have the
specified directed rounding and Emin=-999999,Emax=999999, with no
InvalidOperation, DivisionByZero, Overflow, Underflow, Subnormal or
Clamped flags. Expected Rounded/Inexact flags do not indicate failure.

Reviewing the complete814 prefix confirms directed basic operations,
context-independent copy_negate, nonzero reciprocal denominators,
repeated-multiplication integer powers, and adjacent-representable
enlargement of monotone ln/exp/sqrt endpoints. Machin's alternating
series pays the pi error. Each integer trig shift preserves periodicity;
the actual reduced interval, not just its center, has modulus below4.
After60 terms the successive sine/cosine tail ratios are below1/2,
so twice the absolute next term pays the whole tail. These checks
include the AST loading boundary before class Z; no814 matrix is run.

The independent computation reuses only the reviewed Fraction endpoint
definitions from audit816, loaded by AST without executing that audit.
It rounds rational operations outwards by integer division on a decimal
grid with at least100 significant digits. Only monotone transcendental
endpoints use120-digit Decimal with adjacent-representable enlargement.
Pi uses80 exact rational Machin terms with next-term errors. Trig uses
unreduced arguments of modulus below13 and120 terms; subsequent ratios
are below169/(240*241)<1/2, paying both tails by twice the next term.
This does not share the original argument-reduction calculation.

Every harmonic term is checked as an exact rational; the harmonic sum
is independently accumulated exactly before rounding. Each digamma
term uses its positive rational expression rather than subtraction;
their sum is outward rational arithmetic. Poles use the direct real
formulas above; correlations use product-to-sum expressions. Every
midpoint value and reduced-argument enclosure is checked. All complete
tails, errors, masses, signed corrections and result intervals are
then recomputed, including the derivative bound and every published
coarse bound in(3)-(4).

All24678 stored numerical intervals have independently computed
enclosures inside them, with no missing or extra intervals. All27823
checks pass with no failures. In particular the independent residual
lies strictly between1.17039531185096879944858 and
1.17043652760178537701480, sustaining(4) at required threshold0.
The full unrounded rational/decimal enclosures and check details are
retained in the audit certificate; these printed coarsenings are not
substituted for its comparisons.

The accepted conclusion is only the fixed sufficient-estimate stop.
Independent verification adds local confidence, not a new general
theorem beyond the checked methods. It does not refute C759f or
primitive lowering, prove a full-domain covariance bound, or settle
parity, even ground-state signs/simplicity, other windows or Xi
realization. Python integer/Fraction/Decimal correctness remains a
software trust assumption; no formal verification is claimed.

## Mathlib

Full matching coverage of this finite signed residual and its certified
inequality is not checked. DLMF supplies the digamma partial-fraction
input; Plancherel, dominated Fourier differentiation and elementary
quadrature bounds supply supporting mathematics. Supporting Fourier or
special-function results do not constitute a matching theorem for (4).
