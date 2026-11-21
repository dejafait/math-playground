# Right full-theta ray: primary-source comparison1640

19 November 2026. Literature-only review of the exact target saved in
assessment1639. No tail estimate, convergence proof or new lemma is
established here; the source's estimates remain reproduction obligations.

## Primary statement and essential cases

K. Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, Preprints.org202611.0383v1, posted4 November2026,
DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 .
The live redirect identifies Version1, not peer reviewed. Read
Section5.2(28), Lemma5.1(i), proof(31) including both sigma cases;
AppendixB's phi, C_n, B_+ and theta-series displays/proof sentences;
AppendixC's domain, width, A_+ and monotonicity passage.

The source uses upper-half-plane p, reflection below, principal branches
continued from positive p, and in AppendixC L>=12, r=exp(L),
Re p>=-r/(4L), d=1/(3L). Its distinct right allocation is

    y_0=exp(12)/12^4,
    A_+=[(3/2)exp(1/8)sqrt(6/pi)/(62/25)]
             sqrt(y_0)exp(-(19/45)y_0)<0.096514.

AppendixB displays phi(s)=exp(2s)-1-2s and

    C_n=(1+3W_*exp(2)/(4r))
                  (1+32exp(-3v exp(-2)))/(1-2/u),
    B_+=C_n sqrt(mathcal A/pi)
          exp(9d/2-v phi(d))/(2v(exp(2d)-1)-9/2).

There u bounds U below, W_* bounds |w| above, v bounds v_0 below,
and mathcal A bounds |A_0| above. The source uses the tangent to phi
at d on the entire s>=d ray, and its n>=2 series estimate requires
real t>=1. Its proof(31) treats sigma>=0 and sigma<0 separately
using Q(x)=(sigma x+tau y)/(x^2+y^2): Q decreases while positive;
when sigma<0 its numerator cannot turn positive again. AppendixC
uses increasing exp(L)/L^4 and decreasing sqrt(y)exp(-cy).
These are inspected source assertions, not results proved in this review.

## Precise scope comparison

C048c supplies the exact phase, amplitude and principal-root normalization.
Its definition and equations(3)-(11) were read; no new uniform estimate
was obtained. L799's strip normal convergence and identity(4) supply
the full theta factor, with C048f fixing the notation R_modes. The
definition of T_right in assessment1639 is retained without alteration.

The source's B_+ derivation integrates a nonnegative phase envelope
after bounding the full-mode amplitude. Thus it supports an absolute
right-ray interpretation rather than merely a signed integral estimate.
This is a scope inference from the displayed majorant and the infinite
s>=d tangent argument, not an author-defined symbol T_right or an
equality between a modulus of an integral and an integral of moduli.
The later reproduction must establish that inference with the exact
L799 factorization and C048c normalization. No frequency-cell
perturbation factor is included.

A_+ is printed separately from A_- (left), A_g (Gaussian pair), distant
left, local modes and origin. It is not the combined horizontal budget.
The B_+ endpoint d and method match the proposed right ray; AppendixB's
finite L band and width7/(10L) do not themselves match AppendixC.
In particular its cell values C_n,v,W_*,u cannot be substituted as if
already certified on all L>=12. AppendixC explicitly supplies the
changed width and right coefficient, whose verification is future work.

The later attempt must check the whole ray in the theta strip and
principal Log domain, justify series/integral domination, prove or
independently verify the right-side phase inequality(31) in both real-part
cases and by reflection, bound K and the complete theta factor on the
entire ray, and prove the endpoint decay rate is strictly positive.
It must track sqrt(|A_0|/pi), prove absolute convergence without assuming
it, and verify the claimed A_+ coefficient, radial monotonicity and
strict rational-decimal comparison on the full closed sector.
Finite-segment bounds alone do not establish any of these ray bounds.
No calculation of those obligations was performed here.

## Reused coverage, duplicates and failures

Reused source-notes1636 for the finite theta series, and the already
inspected effective tangent-envelope coverage in
2026-11-05-mellin-right-horizontal-tail-scope.md: Devroye,
*Non-Uniform Random Variate Generation* (Springer-Verlag1986),
ChapterVII Section2.6 pp299-300, envelope before Theorem2.6 and its
first proof integral, https://luc.devroye.org/chapter_seven.pdf .
That real-envelope method needs a strictly negative endpoint slope;
it asserts no log-concavity of the complex theta kernel. No new
general-method search or Devroye reread was needed.

Searched right-tail, horizontal, T_right and B_right in Mellin-named
local literature, histories and attempts. Compared L801's complete
statement, not its detailed proof: its x solves
x(pi exp(2x)-9/4)=s, its endpoint is x+da and its normalization is
sqrt(2pi/A); T_R takes a modulus after integration. These differ from
the present Lambert saddle w/2, endpoint w/2+d and absolute integral.
Its final allowance is no direct mathematical input here. No matching
canonical bound of this new T_right was located; no novelty follows.

Read the preserved
ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md.
The global contour/uniform-remainder import remains unpaid. The
independent right ray does not invoke a continued origin or full-contour
identity. No blocked supplement search was repeated and no cross-notebook
result was read. Fixed-phase asymptotics remain inadequate automatic
imports; the existing scope comparison suffices.

External queries: `"202611.0383" "horizontal"`,
`"Kawano" "Mellin" "tail" "bound"`, and
`"Logarithmic Inequalities of Arbitrary Order" "tails"`.
The primary manuscript was the relevant inspected match; other search
hits supplied no theorem used here. These bounded checks do not establish
novelty. Full matching Mathlib coverage remains unchecked.

## Decision and limits

Essential source-method coverage is accessible: SPECIALIZE supports a
separate REPRODUCTION attempt at the printed right allowance, with the
operational absolute-integral qualification above. This is source
readiness, not an established mathematical input inequality or progress
beyond the source. The new research nomination1640 requires separate
next-turn approval.

Continue only if the exact normalized full absolute ray is bounded by
A_+ L^(9/2)/r uniformly, including L=12, both angular boundaries,
positive real p and unbounded L. A failed sufficient envelope is not a
counterexample to T_right or RH. Record the precise failure and require
a materially different input before repeating a failed mechanism.

Main-gap actual-Xi all-degree positivity remains L030-L032/C032a.
A successful ray estimate could complement C048c-f in a later Mellin
remainder assembly. Left tails, assembly, zero counts, inversion and a
sufficient Mellin-to-sign bridge remain independent. No specific tested
central sign mechanism emerged, so creative routing is not justified by
this routine source specialization.

