# Lemma 388: negative logarithmic mean of the total normalized discriminant

## Hypotheses

Use the fixed actual real functions F=F_0,G and positive common
envelope A of L366, as used in the audited L370, L386 and L387.
For t≥40 let T=1+t, L=log(2+t), f=F/A, g=G/A and
q=(log A)''. Primes are ordinary real derivatives. Define

\[
\mathscr L(u)=u'^2-uu'',\quad B_*=2F'G'-FG''-F''G,
\quad D=B_*^2-4\mathscr L(F)\mathscr L(G),
\quad \Delta=\frac{D}{A^4T^4L^4}.
\]

This is exactly L370's Δ. No RH, simplicity, noncoincidence,
phase independence, physical D≤0 or common-zero count bound is assumed.
All functions are fixed as H tends to infinity through real values.

## Conclusion

With S=ζ(5)ζ(3)²/ζ(6)>0,

\[
\frac1H\int_H^{2H}\Delta(t)\,dt
   =-\frac{S}{240\pi^2}\log H+o(\log H).                 \tag{1}
\]

Consequently every sufficiently high dyadic interval contains an
interior point where Δ<0 and hence D<0. Constants and the onset
are not evaluated. This is an averaged negative-sign result, not an
eventual pointwise D≤0 theorem or a sign theorem for the pencil itself.
It supplies no total L367 margin, common-zero upper count,
actual-theta positivity, extended zero-exclusion range or RH consequence.
The separate critical audit below validates the assembly without
changing its hypotheses or conclusion.

## Proof

This is a **REPRODUCTION** under the prior SPECIALIZE assessment
`drafts/literature/2026-10-10-total-discriminant-assembly.md`.
It assembles already audited canonical inputs; no new shifted-moment
theorem or originality beyond the checked sources is claimed.
The analytic moment input underlying L386 and L387 is imported from
M. P. Young, *A short proof of Levinson's theorem*, Arch. Math.
**95** (2010), 539–548, DOI 10.1007/s00013-010-0199-9,
Lemmas 4–5, (4.1)–(4.5), pp. 542–543, and the Cauchy paragraph
following (3.4), p. 541, in the
[published PDF](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Its hypotheses and complete actual-family applications are in L386
and L387. Here the same fixed pair, ordinary jets, sharp [H,2H]
interval and denominator are used, so only their conclusions are
needed. Reproving the theorem would supply no additional coverage.
The full curvature estimate is imported from L370 (6), including
its rational envelope part and sector-qualified polygamma bound from
[DLMF 5.15.8](https://dlmf.nist.gov/5.15.E8).

Put w=fg'−f'g, w'=fg''−f''g and k=f'g''−f''g'.
L370 (4), valid also at zeros of F,G or w, gives exactly

\[
\Delta=\frac{w'^2}{T^4L^4}
       +\frac{-4wk}{T^4L^4}+E_q,
\qquad E_q=\frac{4qw^2}{T^4L^4}.                       \tag{2}
\]

In particular g is G/A, not G/(AT²); there is no differentiation
of normalized jets or an averaged formula. L386 (1) and L387 (1)
assert, for this same H and pair,

\[
\frac1H\int_H^{2H}\frac{-4wk}{T^4L^4}\,dt
   =-\frac{S}{192\pi^2}\log H+r_R(H),
\quad r_R(H)=o(\log H),
\]
\[
\frac1H\int_H^{2H}\frac{w'^2}{T^4L^4}\,dt
   =\frac{S}{960\pi^2}\log H+r_Q(H),
\quad r_Q(H)=o(\log H).                              \tag{3}
\]

Both little-o statements hold for all sufficiently large H, not
separate subsequences. Their audited errors include complete real
projections, lower jets, moving divisors, all right-line derivative
tails and signed sharp endpoints. Their limit order (height first
at fixed head and smoothing width, then smoothing removal, then head
removal) has already produced the fixed-function remainders in (3).
Adding them requires no simultaneous growing-head limit or interchange.

L370 (6) supplies fixed finite K_q,M with
|E_q(t)|≤4K_qM²/((1+t)log²(2+t)) for every t≥40. Hence for H≥40,

\[
\left|\frac1H\int_H^{2H}E_q(t)\,dt\right|
 \le\frac{4K_qM^2}{(1+H)\log^2(2+H)}
 =O\!\left(\frac1{H\log^2 H}\right)=o(\log H).         \tag{4}
\]

This controls the entire correction absolutely; no relative margin
against either arithmetic term is assumed. Equations (2)–(4) give
a complete summed remainder r_R+r_Q+r_E=o(log H). The coefficient is

\[
\frac{S}{\pi^2}\left(-\frac1{192}+\frac1{960}\right)
 =\frac{S}{\pi^2}\frac{-5+1}{960}
 =-\frac{S}{240\pi^2},
\]

proving (1). Positivity of S follows from the positive convergent
real Dirichlet series for ζ at 3,5,6. If c=S/(240π²), then the
remainder has absolute value at most (c/2)log H for all sufficiently
large H. Thus the average is at most −(c/2)log H<0. Continuity of
Δ implies a negative value in (H,2H): otherwise its integral would
be nonnegative (endpoints have measure zero). The divisor A⁴T⁴L⁴
is strictly positive, so D has the same sign at that point.

This existential conclusion is compatible with eventual D≤0 and
does not establish it. A negative discriminant alone also does not
determine the sign of the quadratic pencil's leading coefficient or
its total value. No use is made of the blocked direct sharp-Hardy
source, common-zero hypotheses, or the stopped grid/phase routes. ∎

### Separate critical audit — 2026-10-10

The prior SPECIALIZE assessment
`drafts/literature/2026-10-10-total-discriminant-mean-audit.md`
approves exactly this REPRODUCTION audit. The component conclusions and
their completed audits are reused; their precisely cited Young input
above needs neither a new application nor a reproof here.

**Physical normalization and fixed functions.** Independently checking
L370 (1), its squared linear coefficient has divisor A⁴T⁴L⁴, and
the product of its constant and quadratic coefficients has divisor
(A²L²)(A²T⁴L²)=A⁴T⁴L⁴. Thus its Δ is exactly the physical D
here divided by that positive quantity. L366 gives
A=(t²+1/4)|Γ(1/4+it/2)|π^(−1/4)>0: the gamma argument is not a
pole and Γ has no zeros. Both component hypotheses use precisely
L366's F_0,G, with the same envelope as L368/L380. On this positive
ray their T,L agree with L370's absolute-height definitions. L380's
opposite Wronskian convention is not substituted into either component;
both explicitly use w=fg′−f′g.

In particular g=G/A in all three inputs. The derivatives in w′ and
k are ordinary derivatives, with no rescaled jet differentiated as
though its normalization were constant. To check the curvature sign,
put a=A′/A. L370's product identities give W=A²w,
W′=A²(w′+2aw), and K=A²[k+aw′+(a²−q)w]. Therefore
(W′²−4WK)/A⁴=w′²−4wk+4qw², checking the sign and factor in (2).
These polynomial identities remain valid at zeros of either function
and at w=0, without simplicity or noncoincidence.

**Full curvature and all-height error.** Here q is the curvature of A,
not of A|b| or of the gamma factor alone. L370 uses the exact expression
q=2/p−4t²/p²−Re Ψ′(1/4+it/2)/4, p=t²+1/4,
including both rational terms. Its audit supplies a finite K_q valid
on the entire ray and M=E_0D_1+E_1D_0. Thus C_q=4K_qM² is fixed,
independent of H. Both 1+t and log(2+t) are positive and increasing
on [H,2H]. Integration over this length-H interval and division by H
give exactly (4). Its ratio to log H is bounded by
C_q/[(1+H)log²(2+H)log H], tending to zero. There is no extra H
factor, gamma-only substitution or relative estimate.

L386 (1) and L387 (1) have the identical measure dt/H, sharp interval,
divisor T⁴L⁴ and constant S. Their audited sequential limits yield
remainders for the full fixed functions for every sufficiently large
real H, not separately chosen subsequences. For any η>0 choose each
component threshold and the curvature threshold so that its remainder
divided by log H is at most η/3 in absolute value. Their maximum is
a single threshold for the sum. This checks the full little-o assertion
without a new exchange of head, endpoint or height limits. The rational
coefficient is −1/192+1/960=(−5+1)/960=−1/240; the independent
errors cannot alter this leading coefficient.

**Interior sign and verdict.** S is strictly positive since the zeta
values at 3,5,6 are finite positive real Dirichlet sums. For
c=S/(240π²)>0 the summed error is eventually at most (c/2)log H
in absolute value. The average is then strictly negative. Δ is
continuous on the closed interval and its divisor never vanishes.
If Δ were nonnegative throughout (H,2H), its integral would be
nonnegative, irrespective of endpoint values, contradicting the mean.
Thus a negative interior point exists and the physical D is negative
there too. Constants and the threshold remain existential.

Conclusion (1) and its existential consequence pass unchanged. The
three direct mathematical inputs remain L370, L386 and L387. This
audit establishes no new bound, eventual pointwise sign, total pencil
margin, common-zero upper count or RH consequence. A negative average
allows both negative and positive pointwise values; no control of the
positive part is obtained.

## Mathlib

Full matching coverage of this actual-family asymptotic is **not
checked**. The essential analytic inputs are the cited external moment
theorem and its canonical applications, plus L370's curvature bound.
Formal addition of limits alone would not cover those inputs. Unknown
coverage is not evidence of absence.
