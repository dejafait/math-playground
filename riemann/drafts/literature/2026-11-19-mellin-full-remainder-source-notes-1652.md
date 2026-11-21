# Full Mellin remainder: source comparison1652

19 November2026. Literature-only comparison of nomination1651. No
contour assembly, new inequality or scalar calculation is performed.

## Exact source and inspected material

K. Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, Preprints.org202611.0383v1, posted4November2026,
DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The live redirect
identifies Version1, not peer reviewed. Directly inspected Section5.1(25),
Section5.2(28)-(29), Lemma5.1's contour and both horizontal-phase cases,
AppendixB's full-mode/origin paragraphs and aggregation(A4), and
AppendixC from its domain through the sum immediately before C.1.
Reused source-notes1627/1648 for component extraction and prior methods;
no supplement access or new general saddle theorem is required.

The relevant source claim is Lemma5.1(i): for r=|p|, L=log r>=12,
Re p>=-r/(4L),

    |I(p)/S(p)-1| <= (17/10)L^(9/2)/r,
    S(p)=8pi^(5/2)exp(9w/4)/sqrt(p(1+w))
                      *exp(2p Log(w/2)-2p/w), w=W_0(2p/pi).

Branches continue from positive p; reflection covers negative imaginary
parts. AppendixC uses d=1/(3L), assigns the local, left, right and
Gaussian coefficients, and prints the budget

    A_loc+A_-+A_++A_g+2/12^3+3*10^(-4) <1.606651<1.7.

It separately bounds the lower-power first mode by 2L^(3/2)/r,
the other local modes by 112sqrt(L)exp(-5r/L^2), and allocates
10^(-4)L^(9/2)/r each to the latter, distant-left and combined-origin
terms. These are source statements, not calculations verified here.
The source also claims the final bound is less than one; that extra
conclusion is outside the nominated reproduction target.

## Comparison with canonical local statements

All components use r=|p|, L>=12, Re p>=-r/(4L). The following is an
applicability checklist for later research, not a proof of assembly.

C048a gives the fixed-height meromorphic contour identity and exact
agreement with source(25). Read its entire statement and its final
continuation/endpoint proof section. The identity must first be used at
a fixed numerical y=Im(w)/2, then evaluated at p. It does not claim
that individual moving-height summands are holomorphic in p. Its
positive-real case uses the original real integral; conjugation supplies
the downward contour. The sector avoids the possible Mellin poles.

C048b defines E_o as the continued vertical primitive PLUS the horizontal
piece 0<=x<=1. Its conclusion pays their combined relative cost below
10^(-4)L^(9/2)/r, with the same S(p). Neither piece may be omitted or
charged again among the horizontal tails. Its proved estimate uses a
different origin deformation; reproducing AppendixC's stronger
intermediate origin assertions is unnecessary for this assembly.

C048c's definitions identify h_p, g, K, u_0=w/2, d and A_0, and its
equation(3) identifies the complex phase of S(p), including the Gaussian
square root. Its T_loc is the leading positive-power first-mode
difference J_loc-G_loc, not the full theta contribution. Its constant
A_loc<1.318214 is already a local conclusion, not an estimate to
reprove. C048d pays the difference between G_loc and the completed
complex Gaussian, with A_g<0.099276. The later assembly must subtract
and add this same G_loc once. A modulus before integration cannot
replace the odd cancellation already built into C048c.

C048e pays the finite lower-power first-mode term separately by
2L^(3/2)/r; its stronger constant need not be recomputed. C048f pays
the finite n>=2 contribution, with its complete lower-power pieces,
by 112sqrt(L)exp(-5r/L^2). The inspected conclusion does NOT yet pay
this in units of 10^(-4)L^(9/2)/r. AppendixC explicitly states that
conversion; verifying it uniformly is a remaining scalar obligation,
within the known-source reproduction rather than an unread theorem.

C048g's entire right ray has s>=d. C048h's near-left interval is
[-1,-d], and C048i's distant-left interval is [1-x_0,-1], where
x_0=Re(u_0). They bound integrals of moduli of the full theta factor,
including both powers of mode1 and every higher mode. Their conclusions
respectively pay A_+<0.096514, A_-<0.091191, and less than 10^(-4),
in common units L^(9/2)/r. The distant-left intermediate expression
printed in AppendixC is stronger than C048i's reproduced claim and
is unnecessary here. Their interval definitions and C048c's geometry
are the material for a later exact partition check at x=1, s=-1,
s=-d and s=d; no fresh tail estimate is proposed.

Read C048h's normalization(3)-(5), C048g's geometry/normalization
section and C048i's statement. They retain the 2/u factor. L799's
general strip-series proof and identity(4) identify F with the full
normalized theta factor, with normal convergence on compact subsets
of |Im(u)|<pi/4. Only this general identity is relevant; L799's
different saddle/domain/amplitude conclusion is excluded. There is
no need to extend a theta estimate through the strip boundary.

Thus source coverage is adequate for a separate assembly attempt.
That attempt must still write the exact identity with oriented pieces,
justify use of the already convergent series/integrals, retain the
principal normalization, verify the C048f scalar conversion on the
entire ray L>=12, scale C048e's allowance consistently, and check one
total coefficient below 17/10. Rounded component bounds may be used
if their exact rational sum suffices; reproducing the sharper printed
1.606651 is not required. No such sum is evaluated in this review.

## Duplicates, recorded failures and decision

External queries were `"202611.0383" "17" "10"` and
`"Kawano" "Mellin" "relative" "remainder"`. The relevant match was
the primary manuscript; no search failure is evidence of novelty.
The scoped local search for 17/10, 1.606651 and full/global remainder
in C048 files, Mellin-named assessments/attempts and relevant
November19 histories found source notes and exclusions, not a canonical
full-assembly result. Reuse source-notes1627/1648's documented
L798-L804 mismatch comparison instead of rereading those proofs.

Read and preserve ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md
and ATTEMPTS/2026-11-05-mellin-endpoint-review-loop-closed.md. They reject
automatic import and repeated endpoint approvals, not a future assembly
with matching independently proved components. The now available
C048a-i are material new inputs relative to those stops. No source
blocker requires another supplement search. No cross-notebook input
was read. Matching Mathlib coverage for the full result is unchecked;
supporting complex integration results alone would not formalize it.

Decision SPECIALIZE: the exact full bound is already claimed by the
source, while the local contour/budget specialization still needs a
separate REPRODUCTION proof. Reproof is justified only to verify that
quantitative preprint claim from the existing checked components, not
to present the source's result as new mathematics. An incompatibility
or failed sufficient allocation must be recorded precisely; it would
refute neither RH nor automatically the source's inequality.

Outcome EXPLORATION: new theorem-scope comparison and an actionable
assembly test, without a mathematical advance or new obstruction.
The main gap remains L030-L032/C032a actual-Xi all-degree positivity,
with C028b's H_d=o(d), C028g's S_F=0 and a sufficient Mellin-to-sign
bridge unpaid. A checked full remainder could support later analytic
control of I; finite regions, zero counts, inversion and mixed signs
would remain separate. These absolute bounds specify no new signed
inversion mechanism, so no central creative target is manufactured.
