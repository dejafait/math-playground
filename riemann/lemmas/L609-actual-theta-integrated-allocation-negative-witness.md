# Lemma 609: a negative actual-theta integrated layer allocation

## Hypotheses

Use exactly C604b's full-line density p=k/Z, where k is L019's
even kernel, k(u)=4 Phi(u/2), and Z=integral_R k. Retain L604's
h, tau=h/p, full four-term K_x(a,b), and C604a's q=-tau', J_a,
ell=lim tau. In particular no auxiliary squared-variable density is
substituted. Define, for a>0 and real x,

\[
G_x(a)=q(a)J_a(x)^2+
2p(a)\int_0^a[\tau(b)-\tau(a)]p(b)K_x(a,b)\,db.
\]

The calculation uses the standard named Taylor theorem with bounded
real second derivative and Machin's formula for pi. For the numerical
inclusion method import Fredrik Johansson, *Numerical integration in
arbitrary-precision ball arithmetic*, arXiv:1802.07942v1, Sections
2–2.1, pp.2–3, https://arxiv.org/pdf/1802.07942v1 (enclose the entire
input interval; a real box integral needs no complex analyticity).
Explicit geometric series/derivative tails follow the method of
Johansson, *Numerical Evaluation of Elliptic Functions, Elliptic
Integrals and Modular Forms*, arXiv:1806.06725v1, Section 1.2, p.4,
Section 1.4.2, (1.18)–(1.20), pp.12–13,
https://arxiv.org/pdf/1806.06725v1. These are known numerical methods;
their exact theta/coordinate/error specialization is given below,
rather than importing a source sign assertion or redoing its algorithm.

## Conclusion

For this fixed density, the interval calculation establishes

\[
G_{11}(7/16)\in[-0.002615,-0.002543]\subset(-\infty,0).
\]

Thus the proposed fixed-a sufficient condition G_x(a)>=0 for all
a,x fails even for the actual theta density. L604 and C604a still give

\[
D(x)=\ell F(x)^2+\int_0^\infty G_x(a)\,da.
\]

A negative integrand value does not determine this integral or D.
There is no negative Xi determinant, off-line zero, higher-sign result
or RH conclusion. This is a computer-assisted local obstruction, not
a complete candidate solution. The independent implementation and
application audit below passes; proofs of imported source theorems
and the Decimal implementation itself have not been independently verified.

## Proof

**Assembly and absolute convergence.** C604b verifies the hypotheses
of C604a and L604 for this exact p. The positive part has
|J_a(x)|<=1 and integral_0^infinity q<=c. The other part is absolutely
integrable by L604's |K_x(a,b)|<=2+2|x|a, 0<=tau(b)-tau(a)<=c,
and the finite first moment of p. Adding C604a's layer representation
to L604's remainder representation proves the identity above with
the nonnegative floor ell F^2 retained. This is only an assembly of
existing absolutely convergent identities.

**Normalization cancellation before numerical division.** On u>=0 set

\[
H(u)=\int_u^\infty v k(v)\,dv,\qquad
S=\int_0^a k(b)\cos(xb)\,db.
\]

Since h=H/Z, tau=H/k and H'=-uk, differentiation gives
q(a)=a+H(a)k'(a)/k(a)^2. Also J_a=2S/Z. Exact substitution, without
any approximation, gives

\[
\begin{split}
Z^2G_x(a)={}&4\left(a+\frac{H(a)k'(a)}{k(a)^2}\right)S^2\\
&+2\int_0^a[k(a)H(b)-H(a)k(b)]K_x(a,b)\,db.       \tag{1}
\end{split}
\]

The identity eliminates divisions by k(b) throughout the integral.
The established 0<Z<infinity already gives sign equivalence.
The calculation additionally encloses Z and k(a) away from zero to
enclose the normalized G. Every numerical division is separated from
zero; neither qualitative positivity nor a floating approximation is
used to divide by an interval containing zero.

**Uniform theta and derivative inclusions.** For u in [0,8], write
v_n=pi n^2 exp(2u). L019 and the termwise derivative justification in
L016 give

\[
k^{(j)}(u)=e^{u/2}\sum_{n\ge1}e^{-v_n}P_j(v_n),\quad j=0,1,2,
\]

where exact differentiation, using v_n'=2v_n, gives

\[
\begin{split}
P_0(v)&=8v^2-12v,\\
P_1(v)&=-16v^3+60v^2-30v,\\
P_2(v)&=32v^4-224v^3+330v^2-75v.
\end{split}
\]

These are successive applications of P -> (1/2-2v)P+2vP'.
Compute terms n=1,...,5 by outward interval algebra. For omitted
n>=6, v_n>=pi n^2>108, and
|P_j(v)|<=C_j v^(j+2), with (C_0,C_1,C_2)=(20,106,661), since
v>=1 and these are the sums of absolute coefficients. For
m=j+2<=4 the function v^m exp(-v) decreases for v>=108. Hence
each omitted absolute summand is bounded by
exp(4) C_j (pi n^2)^m exp(-pi n^2). Consecutive majorants have ratio

\[
\left(\frac{n+1}{n}\right)^{2m}e^{-\pi(2n+1)}
\le(7/6)^8e^{-39}<4e^{-39}<1/2.
\]

Their first term is at most C_j exp(4)144^m exp(-108). Thus the
entire omitted tail is bounded by

\[
T_j=2C_j144^{j+2}e^{-104}.                         \tag{2}
\]

The certificate uses evaluated upper bounds for these expressions:
T_0<5.652*10^-40, T_1<4.314*10^-37, T_2<3.874*10^-34.
Add [0,T_0] for k (each omitted P_0 summand is positive), and
[-T_j,T_j] for j=1,2. This is an evaluated uniform bound, not an
unevaluated superexponential constant or first-summand approximation.

**Spatial cutoff with its actual coordinate factor.** L564's complete
envelope is Phi_R(u)<=10000 exp(-u^2). Its Phi_R is k/2 on u>=0,
so k(u)<=20000 exp(-u^2), without scaling u. Therefore

\[
0\le H(8)\le10000e^{-64},\qquad
0\le\int_8^\infty k(u)\,du\le1250e^{-64}.           \tag{3}
\]

The second bound follows by 1<=u/8 and integrating u exp(-u^2).
These upper bounds are respectively <1.604*10^-24 and
<2.005*10^-25. Evenness accounts for both sides when computing Z.

**Real finite integration.** Fix a=7/16, x=11. Divide [a,8] into
2048 equal cells of length d. For f(u)=u k(u), its second derivative
is 2k'(u)+u k''(u), enclosed on each whole cell by the series bounds
above. On a cell with midpoint m, Taylor's theorem gives

\[
\left|\int_{m-d/2}^{m+d/2}f(u)\,du-d f(m)\right|
\le d^3\sup|f''|/24.                              \tag{4}
\]

Indeed the linear term integrates to zero and the bounded quadratic
remainder integrates to that value. Apply the same rule to k using
k'' for its error, and add (3). This encloses H(a) and the mass on
[a,infinity). The summed H quadrature error is <5.263*10^-7;
the corresponding one-sided mass error is <1.463*10^-6.

Divide [0,a] into 16384 equal real cells of length e. Enclose k(b)
and b k(b) on each whole cell. Enclose sin(xb), cos(xb) using their
midpoint values and the Lipschitz radius x e/2. The two midpoint
values propagate by the exact angle-addition formulas with interval
arithmetic, from the first midpoint and step. No unrounded native
floating sine or cosine is used. The initial sine/cosine and step
enclosures use their Taylor polynomials through degrees 99/98;
all arguments have absolute value <=5, and each remainder is bounded
by 5^100/100! (view cosine as Taylor degree 99 with zero odd term).

The complete original K is evaluated using its exact equivalent

\[
K_x(a,b)=2[(\cos(xa)+xa\sin(xa))\cos(xb)
                       -xb\cos(xa)\sin(xb)].       \tag{5}
\]

This follows by the sum/difference identities and retains both
cosines and both sine terms; it is not a changed kernel. The
whole-cell box for k(b)cos(xb), multiplied by e and summed, encloses S.

For H(b), descend from the enclosure for H(a). If a cell is [l,r]
and H(r) is enclosed by [L,U], while e b k(b) on the whole cell is
enclosed by [m_-,m_+], then positivity of b k(b) gives
H(b) in [L,U+m_+] for every b in [l,r]. Update the endpoint
enclosure to [L,U]+[m_-,m_+] and continue. Use the whole-cell H(b),
k(b), and K boxes in the second integral of (1). Multiplication by
e and interval summation enclose its complete integral. There is no
nested numerical tail approximation or interchange of limits here.
This is the imported real-box inclusion method, with (4) used only
where a bounded real derivative is supplied. No complex branch,
analyticity flag or quadrature tolerance is treated as proof.

**Arithmetic and complete computed bounds.** Reproduction command:

```text
python3 scripts/theta-allocation/certify.py
```

The full result is `scripts/theta-allocation/certificate.json`.
The executable uses Python Decimal with 45-digit explicit contexts:
every endpoint addition, product and reciprocal is rounded down or
up as appropriate. Decimal's correctly rounded nearest exp at each
endpoint is widened to the adjacent representable numbers. Negation
uses exact copy_negate, including error radii, rather than a default
precision unary operation. All inputs are integers or exact decimal
strings. Machin's pi formula uses alternating arctangent sums with
120 terms and remainder <=(1/q)^241/241 for q=5,239; its enclosure
lies strictly between 3 and 4. Intermediate intervals must be finite
and ordered, and each division asserts denominator separation.

The following rational-decimal intervals are outward widenings of
the complete inspected output; their endpoints do not abbreviate
the actual values inward:

| Quantity | Lower bound | Upper bound |
|---|---:|---:|
| k(a) | 0.24157430 | 0.24157432 |
| k'(a) | -2.43400227 | -2.43400225 |
| H(a) | 0.0097806749 | 0.0097817275 |
| q(a) | 0.02952360 | 0.02956750 |
| S | 0.00846067 | 0.00871906 |
| 4 q(a) S^2 | 0.00000845355 | 0.00000899111 |
| second line of (1) | -0.002592355 | -0.002524214 |
| Z | 0.99405069 | 0.99442693 |
| Z^2 G | -0.002583901 | -0.002515223 |
| G | -0.002614923 | -0.002543494 |

For the last upper endpoint, the actual interval endpoint is
-0.00254349445073187978085041497223350674919322775, so the printed
table upper bound -0.002543494 is outward. The actual Z^2G upper
endpoint is -0.00251522327027041753433328453782206035365046735;
the required threshold is 0. The Z^2G interval radius is
<0.000034339; the normalized G interval radius is <0.000035714.
All errors in (2)–(4), arithmetic and real-box
integration are included. k(a)>0.24157430 and Z>0.99405069 certify
both divisions. The asserted broader conclusion follows.

**Bounded search and limitations.** `scripts/theta-allocation/preview.py`
evaluated only the approved grid x=1,...,64, a=j/16, j=1,...,64.
Its floating arithmetic yielded 2752 finite values; 1344 points were
skipped because k(a) underflowed to zero. It ranks the finite values
by Z^2G, and the first corrected candidate is (11,7/16). Only that
rational point was certified; the remaining two candidates were not
attempted. The grid file is explicitly NONRIGOROUS_PREVIEW_ONLY and
supplies no sign or denominator evidence, including for skipped points.
An initial preview derivative coefficient 56 was corrected to 60 by
the displayed exact differentiation before certification. The final
certificate also reran after exact-negation correction and replacing
the initially mistyped P2 coefficient -232 by the exact recurrence's
-224. The final executable generates P1/P2 by exact Fraction arithmetic
from P0, and derives C_j from their coefficients. Initial outputs are
not mathematical evidence. These corrections and the
bounded scope remain recorded rather than reporting a larger search.

This establishes a new local diagnostic relative to the assessed
sources; the search does not certify originality. No theorem claiming
G's sign was imported or reproved. Its negativity rejects the fixed-a
allocation only. The floor, all other a, integrated compensation,
independent higher signs and every RH obligation remain as before.

**Independent single-witness audit, 1 November 2026.** Reused the ready
assessment `drafts/literature/2026-11-01-l609-independent-certificate-audit.md`
and its completed companion source comparison. This checks the existing
local result (REPRODUCTION); it establishes no new sign beyond that result
or novelty beyond the sources checked. No grid was enlarged and no other
rational candidate was evaluated. The floating preview is not an input.

The arithmetic specification additionally imported here is the Python
Software Foundation, *Python Library Reference*, version-tagged
[CPython v3.15.0 decimal documentation](https://raw.githubusercontent.com/python/cpython/v3.15.0/Doc/library/decimal.rst),
named entries `Decimal`, `copy_abs`, `copy_negate`, `exp`, `next_minus`,
`next_plus`, `Context`, and Rounding modes. Exact string/integer conversion,
context-independent sign copying, correctly rounded nearest-even exp,
adjacent representable values in the selected context, and directed basic
arithmetic are used as library guarantees. This audits their use, not their
implementation. The previously assessed Johansson and Taylor inputs above
are unchanged; there is no reproof of their general numerical methods.

1. **Exact algebra and coordinates.** Substitution of p=k/Z and h=H/Z
   gives tau=H/k and q=a+Hk'/k^2 since H'=-ak. The layer factor is
   q(2S/Z)^2. In the remainder,
   Z^2 p(a)p(b)(tau(b)-tau(a))=k(a)H(b)-H(a)k(b).
   These verify every factor in (1), without numerical cancellation of
   normalizations. Expanding sin(x(a+b)) and sin(x(a-b)) gives a sin(xa)
   cos(xb) coefficient 2xa and a cos(xa) sin(xb) coefficient -2xb;
   the cosine pair is 2cos(xa)cos(xb). Thus (5) retains all four terms.
   L019's summands are exactly 4 Phi(u/2) and 2 Phi_R(u), so (3) uses
   k<=20000 exp(-u^2) in the actual u coordinate. Integration of
   u exp(-u^2), and 1<=u/8 for u>=8, give exactly the two bounds in (3).
   The full-line normalization doubles both one-sided masses. The
   assembly retains the floor and the absolutely integrable signed
   remainder; no sign is inferred by discarding either.

2. **Complete differentiated series.** Direct differentiation of
   exp(u/2-v)P(v), v'=2v, gives the stated polynomial operator. Its first
   two outputs are (0,-30,60,-16) and (0,-75,330,-224,32) in ascending
   coefficients, agreeing with the exact Fraction-generated executable.
   For v>=1 the sums of absolute coefficients give 20v^2,106v^3,661v^4.
   For n>=6, v>=pi n^2>108>4, so each v^m exp(-v) is decreasing.
   On u<=8, exp(u/2)<=exp(4). Successive n-majorants have ratio
   <=(7/6)^8 exp(-39)<4exp(-39)<1/2. Their n=6 term is bounded using
   pi*36<144 and pi*36>108, giving (2). This controls the whole infinite
   tail, with nonnegative sign only for order zero. The computed tails
   include their own outward exp and arithmetic errors. L016 justifies
   the differentiated series; no finite differentiation stencil is used.

3. **Endpoint arithmetic, including exceptional cases.** Interval sums
   use directed lower/lower and upper/upper operations; products take
   the minimum/maximum of the four directed corner products. If an
   interval misses zero, reciprocal is [down(1/hi),up(1/lo)] on either
   sign component, followed by the product rule. Negation reverses
   endpoints by exact copy_negate. The square routine separately handles
   nonnegative, nonpositive and zero-straddling intervals. Thus no sign
   case is omitted. Exp is monotone, and one adjacent number on each
   side of a correctly rounded endpoint exp encloses the exact value.
   Exact Decimal constructors do not round integers or decimal strings;
   comparisons, copy_abs and copy_negate do not invoke the default
   precision. All other endpoint numerical operations use explicit
   contexts. Python integer/Fraction calculations are exact.

   The replay below uses CPython 3.15.0, the C `_decimal` backend,
   decimal specification version 1.70 and libmpdec 4.0.1. All three
   contexts have precision 45, Emin=-999999999, Emax=999999999, clamp=0,
   with rounding FLOOR, CEILING and HALF_EVEN respectively. Their sticky
   flags, including the module-level pi/tail calculations, show only
   Inexact and Rounded. InvalidOperation, FloatOperation, DivisionByZero,
   Overflow, Underflow, Subnormal and Clamped are false in every context.
   During main's replay every constructed endpoint is finite and ordered;
   nonzero adjusted exponents range from -303099977 to 157. Exp input
   lies between -697913488.255362660138543923210874727652360159 and 16.
   Thus the very small high-u terms do not trigger numerical underflow.
   Every one of 26935 division calls has a denominator separated from
   zero; the smallest observed denominator magnitude is greater than
   0.0583581473194319893953050183665117204599052410.

4. **Pi, trigonometry and the complete real cells.** The arctangent
   loop includes powers through t^239, with 0<t<1. Its updated term
   encloses t^241 and its remainder radius is rounded upward after
   division by 241. Machin's exact identity then gives an interval
   strictly inside (3,4). The sin/cos loops sum degrees 99 and 98;
   both are their degree-99 Taylor polynomials (the cosine degree-99
   coefficient is zero). The uniform degree-99 remainder on |t|<=5
   is bounded by 5^100/100!. Every direct call meets that argument
   restriction. Angle addition uses simultaneous updates from the two
   old intervals, and so inductively encloses every actual midpoint
   angle, including accumulated rounding error. The global derivative
   bounds |sin'|,|cos'|<=1 justify adding radius 11db/2 on every box;
   periodicity is not used to reset accumulated intervals.

   Both meshes are exact dyadics: dt=121/32768 and db=7/262144.
   Their endpoints and midpoints fit exactly within precision 45.
   Consequently their cells cover [a,8] and [0,a] without a rounded
   mesh gap or an unaccounted endpoint displacement. Kernel evaluation
   on a cell encloses every real u in it. Differentiating u k gives
   (uk)''=2k'+uk'', exactly the midpoint bound used; k'' supplies the
   mass error. The integral of the Taylor quadratic bound is d^3/24,
   while the linear term vanishes. The replay checks all 2048 derivative
   cells, not a sample. The 16384 head boxes bound S and the head mass
   directly, without substituting midpoint integrals for boxes.

   Finally, if H(r) is enclosed, positivity of u k(u) gives the lower
   bound H(b)>=H(r) on [l,r] and the upper increment <=db*(b k(b))_hi.
   These are exactly the descending whole-cell bound and endpoint update.
   Interval products of that H box, the complete K box and kernel boxes
   enclose the full signed integrand, even when boxes straddle zero.
   Shared-variable dependencies only widen these enclosures. This proves
   the induction over all head boxes, including b=0 and b=a, rather than
   assuming a nested numerical approximation is accurate.

5. **Full replay and inspected error budget.** Reproduction command:

   ```text
   python3 scripts/theta-allocation/audit.py
   ```

   The wrapper preserves `scripts/theta-allocation/certificate-before-independent-audit.json`
   and writes complete runtime/context/exception telemetry plus the entire
   regenerated certificate to `scripts/theta-allocation/independent-audit.json`.
   It instruments arithmetic and kernel calls but does not replace the
   integration algorithm or claim a second independent numerical method.
   Every value of the preserved and replayed complete certificates matches
   exactly. Their bytes differ only in the order of three top-level JSON
   keys, as checked by a complete diff; both SHA256 values are recorded.
   The original executable is unchanged. Its historical three-generation
   counter is reproduced verbatim, not incremented as a live run count;
   this audit adds one separately recorded replay.
   All complete enclosures, arithmetic/tails, quadrature and test objects,
   and the complete audit runtime/telemetry, were inspected using the
   shared JSON inspector. Counts are 18432 order-zero, one order-one and
   2048 order-two kernel evaluations, consistent with the entire mesh.

   The H midpoint radius allowance is
   5.26271068968315206113842802306021402251577617e-7;
   the one-sided mass allowance is
   1.46224352287185355946367440829151087517742697e-6.
   Spatial allowances are respectively
   1.60381089054863785297608703414233538099836385e-24 and
   2.00476361318579731622010879267791922624795482e-25.
   Theta tails are the complete values bounded above in (2), and head-box,
   trigonometric propagation and arithmetic widths are already included
   in the displayed enclosures. No additional tolerance is left unpaid.
   In particular the negative remainder upper endpoint plus positive
   layer upper endpoint is the stated Z^2G upper endpoint, still <0.
   Both k(a)>0.24157430 and Z>0.99405069 hold; division gives the same
   G upper endpoint -0.00254349445073187978085041497223350674919322775.
   The normalized interval radius is
   0.00003571393379345010223607846256358698663545356.
   The earlier unqualified radius referred to Z^2G; this is clarified
   above. No bound, sign, mesh, derivative or executable needed repair.

This passes the bounded audit of the local computer-assisted witness.
Library and cited source proofs remain imported, not independently
machine-verified. The fixed-a sufficient condition is stopped; integrated
compensation, other allocations and independent higher signs are open.

## Mathlib

Full matching-result and supporting interval/Taylor/Decimal coverage
not checked. L016 retains its supporting theta-series references;
these are not a formalization of this numerical witness. No absence
claim or proof-assistant verification is made. The certificate and
implementation passed the bounded audit above, with the stated imported
library/source-proof qualifications and without formal verification.
