# Principal Rice stationary-point source review1663

19 November2026. This is a literature-only review of assessment1662's
unchanged target. It imports analytic tools and checks their domains;
it does not form or solve the stationary equation, prove localization,
differentiate I/S, or assert a signed asymptotic.

## Primary derivative inputs

NIST DLMF version1.2.8, release2026-09-15 (footer checked),
[5.11.2 and5.11(ii), first remainder paragraph](https://dlmf.nist.gov/5.11),
read19November2026. For complex z tending to infinity in a fixed
sector |arg z|<=pi-delta, delta>0, the principal-log expansion is

    psi(z)=Log z-1/(2z)
             -sum_(k=1)^(n-1) B_(2k)/(2k*z^(2k))+R_n(z),
    |R_n(z)|<=sec^(2n+1)(arg(z)/2)
                         *|B_(2n)/(2n*z^(2n))|,  n>=1.

The empty sum n=1 retains Log z-1/(2z); the first omitted term
has magnitude 1/(12|z|^2). This is the source's digamma remainder,
not the sec^(2n) log-gamma bound. Import it directly; no differentiation
of a Stirling error or new gamma theorem is necessary. The fixed-shift
ratio expansion5.11(iii) is unnecessary for growing d.

[DLMF5.5.2 and5.5.4](https://dlmf.nist.gov/5.5), inspected with their
recurrence/reflection conditions, give

    psi(z+1)=psi(z)+1/z,
    psi(z)-psi(1-z)=-pi*cot(pi*z).

Reflection excludes integers; recurrence is used away from its poles.
These are available exact identities, not permission to replace a
finite Rice kernel by an infinite-contour approximation.

[DLMF4.13.1, principal-branch paragraph and4.13.4](https://dlmf.nist.gov/4.13)
give W_0 analytic off (-infinity,-1/e], with W exp W=z and
W'=W/[z(1+W)] away from the displayed singularities. C048a already
pays the branch geometry. C048l(13), which was read, already gives
the exact S'/S expression for the present S. Reuse that formula;
the next attempt need not reconstruct its cancellation.

## Source-domain specialization, not a localization proof

Retain p=s+1/2, actual fixed Z=gamma_0, and C048j's principal S.
The proposed region requires d^(1/3)<=|s|<=d^(2/3), Im(s)>=|s|/2,
and the stated C048j conditions on p. In particular Im(s)>0, so
no integer pole of B_d or gamma pole is on this test region.

For the gamma tools the arguments p, -s and d+1-s are sufficient:
the first comes from the normalization, while the last two occur
in C048l(17)'s already established reflected kernel identity. No
new identity for the kernel or its derivative is derived here.

|arg(s)|<=5pi/6 in the upper half-plane; adding the positive shift
1/2 cannot increase its argument. Thus |arg(p)|<=5pi/6 and
|arg(-s)|<=5pi/6. Also Re(d+1-s)>=d+1-d^(2/3)>0.
Their moduli are respectively at least d^(1/3)/2, d^(1/3), and
d+1-d^(2/3). These substitutions verify a common fixed angular
clearance and growing moduli for the inspected digamma theorem.
They establish no bound for the combined logarithmic derivative,
no sign of its real part, and no stationary-point existence or absence.
The later attempt must keep full arguments and branch phases.

C048j's value error is unnecessary for the derivative of this explicit
main term. A later transfer to the actual integrand would require its
own assessed derivative/deformation argument. C048l's absolute closing
budget remains a separate checked input and does not sign a left integral.

## Rice saddle overlap: actual primary statements and proof cases

Reuse the finite Rice theorem and both closing-contour cases already
inspected in source-notes1656/1660; do not repeat their proofs.
Newly inspected: Flajolet--Sedgewick, *Mellin transforms and asymptotics:
Finite differences and Rice's integrals*, TCS144(1995),101--124,
[Section5, printed p120, paragraph “Entire functions”](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf).
Its example uses the entire coefficient function 1/Gamma(s), cites
a Laguerre-related oscillatory asymptotic, and refers to Odlyzko's
survey [25]. It states no general theorem locating stationary points
for arbitrary entire coefficient functions. The extra theta-Mellin
factor S(p) in this target is absent. Hence this paragraph supplies
method context, not a matching location theorem. Odlyzko and its
references are unread leads, not imported results or an essential
source for the bounded derivative test.

P. Flajolet and L. Vepstas, *On Differences of Zeta Values*,
[arXiv:math/0611332v2, revised11July2007](https://arxiv.org/pdf/math/0611332v2),
Section4, pp6--9, (18)--(30) and Theorem1/(34), inspected. The
observable is the Newton coefficient of zeta(s)-1/(s-1).
The transformed integrand(19) contains zeta(1+s), sin(pi*s/2),
Gamma(s+1), and the rising product s(s+1)...(s+n). Its upper-half-plane
model(23) has approximate saddles(26) at (1+i)sqrt(pi*n).
The compact first-quadrant expansion(24), slanted central segment,
vertical-tail estimate(28) and complement estimate(30) concern that
model and integrand. They neither contain this theta-Mellin S nor
locate roots of (F_d^S)'. Sharing a Rice kernel or a degree-power
annulus is insufficient for transferring the stationary equation.
No part of their oscillatory asymptotic is imported as a sign here.

K. Mazhouda, *The saddle-point method and the Li coefficients*,
[arXiv:1506.01755v1,5June2015](https://arxiv.org/pdf/1506.01755),
Sections2--4, Theorem2.2's hypothesis H, Section3's three saddle
conditions and Lemma3.1, Theorem4.1, and Proposition4.3's defining
sum/integral pp5--6 inspected. Theorem4.1 explicitly assumes GRH
for a Selberg-class function. Section3 presupposes a saddle and a
suitable contour, then requires tail, quadratic and Gaussian-completion
checks. Proposition4.3 concerns Hurwitz-zeta finite differences.
None is an unconditional location theorem for this F_d^S. Importing
the conditional Li conclusion to pay positivity would be circular.
No estimate from this paper is used; its later coefficient analysis
was not critically audited.

Kawano202611.0383v1's existing comparison1652 and finite-saddle
ledger1627 are reused. A narrowly targeted check of the live
[Version1 page](https://www.preprints.org/manuscript/202611.0383/v1)
found the same (28) and Lemma5.1 sector; text searches for “Rice”
and “stationary” returned no match. This is not an exhaustive proof
of absence. AppendixC.1's differentiation paragraph appeared as a
lead but was not assessed or imported: actual-I derivative transfer
is outside the present main-term-only target.

## Duplicate and failure checks

Read the exact definitions/conclusions in C048j, C048l and its(13),
C048k's scoped source records1656/1660, L718's full statement and
ATTEMPTS/2026-11-17-unshifted-edge-automatic-airy-import-stop-1345.md.
C048k's fixed-d infinite absolute-opening obstruction is unchanged.
L718's accumulating poles belong to a different moving-size
interpolation. The Airy stop concerns an unpaid exterior contribution
and cannot locate this phase. Neither is a global ban on the present
finite-degree, explicit-main-term test.

The scoped stationary-point/digamma search also identified
2026-11-05-direct-mellin-laguerre-interpolation-scope.md and
2026-11-18-mellin-finite-saddle-source-notes-1627.md; their inspected
target/definition passages concern respectively E at a real point
and the inner u-saddle of I. They do not duplicate the outer s-variable
Rice stationary problem. Other fixed-Mellin-floor hits were not read
or used: a digamma word match alone is not a theorem comparison.

External queries actually issued included `digamma asymptotic expansion
complex sector remainder DLMF 5.11`, `Rice integrals saddle point method
finite differences Lambert W Mellin transform`, `"Mellin" "Rice" "xi"
"stationary"`, `"Kawano" "Logarithmic Inequalities" Rice saddle`,
`"Jensen polynomials" "Rice" "saddle"`, `"Saddle-Point Method and the
Li Coefficients" theorem saddle`, `"Jensen" "Rice" "Lambert"`,
`"Rice" "saddle" "theta" Mellin gamma`, `"Riemann xi" "digamma"
"saddle"`, and `"S(s+1/2)" "B_d" Rice`. The inspected primary
comparisons above found no matching location theorem. Unrelated
statistical Lugannani--Rice hits and secondary snippets are not inputs.
The bounded search does not establish novelty.

## Coverage decision and limits

SPECIALIZE for the unchanged target: known exact branch/kernel
identities, the existing S derivative, and the direct uniform digamma
remainder cover the analytic prerequisites. The unpaid difference is
an eventual existence or exclusion proof for this combined main term
on the entire stated region. This is an ordinary analytic specialization
of established tools, provisionally REPRODUCTION, not a new gamma
theorem or a protected creative sign mechanism. No source blocker
remains for that bounded mathematical attempt. Full matching Mathlib
coverage has not been checked; it is not inferred absent.

Continue toward a signed saddle mechanism only with a rigorous
in-region existence result; then nondegeneracy, contour access,
actual-remainder transfer, a signed margin and a sufficient height
implication remain open. Eventual absence stops only this in-region
saddle prerequisite. An inconclusive result must name a specific
unpaid estimate instead of repeating numerics at larger d.
The main actual-Xi positivity gap remains unchanged. The newly
completed assessment is submitted for separate next-turn approval;
this source turn does not invoke the mathematical test.
