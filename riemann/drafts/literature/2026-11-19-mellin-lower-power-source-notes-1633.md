# Lower-power first-mode allowance: source comparison1633

Inspected19November2026: K. Kawano, *Logarithmic Inequalities of Arbitrary
Order for the Riemann Xi Coefficients*, Preprints.org202611.0383v1,
posted4November2026, DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The URL redirects
to the manuscript page, marked Version1 and not peer reviewed.
These are source claims and scope evidence; their effective
specialization is reserved for a later mathematical turn.

## Primary hypotheses and essential proof cases

Section5.2(28), Lemma5.1(i) and its proof fix p=sigma+i tau,
r=|p|, L=log r, w=W_0(2p/pi)=U+iV, u_0=w/2, L>=12,
sigma>=-r/(4L). Branches continue from positive real p; reflection
supplies tau<0. The horizontal coordinate is real s=Re u-U/2.
The phase/amplitude are C048c's h_p,g, and the normalization is
S=g(u_0)exp(h_p(u_0))sqrt(pi/A_0), A_0=-h_p''(u_0)/2.

Read AppendixA.2(A3)'s entire displayed normalized mode factor. Its
n=1 factor separates into1 and -3/(2pi exp(2u)). The additional
exp(2z Log(u/u_*)) there belongs to that appendix's frequency-cell
perturbation variable z; do not append it to the saved h_p integral.
A3 identifies the correction; its finite-frequency-cell hypotheses
are not the infinite-region estimate.

Read AppendixB from its domain/local definitions through B_low/B_modes.
It treats7.5<=L<=12.3, width d=7/(10L), with enclosing symbols
u<=U<=h, |w|<=W_*, v<=pi exp(U)cos V, b<=Re A_0,
|A_0|<=mathcal A. Its local data include

    M=exp(9d/2)/(1-2d/u), Y=B_3+E_4 d, b_*=b-Yd>0,
    u/2-d>1, |K|<=M,
    h_p(u_0+s)-h_p(u_0)=-A_0 s^2+Z(s), |Z(s)|<=Y|s|^3.

These hold for real |s|<=d. Following its Gaussian integration and
modulus-normalization discussion, the display immediately after B_g gives

    B_low=M [3W_*/(4r)] exp(2d) sqrt(mathcal A/b_*).

The source gives no separately numbered theorem or step-by-step
derivation of B_low. Our scope inference is that this is a local
absolute allowance: horizontal
tails receive B_-/B_+/B_f, Gaussian extension B_g, and other local
modes B_modes. Thus we infer that its intended scope matches the finite local
correction, rather than cancellation with omitted path pieces.
The later reproduction must prove the finite-integral majorization;
a larger signed-integral bound would not justify restriction.

Read AppendixC's opening domain/width, complete local estimates,
absorbed curvature and the paragraph between A_-/A_+/A_g and the
origin cases. On L>=12 and sigma>=-r/(4L), for d=1/(3L), it supplies

    U>=3L/4, |w|<=1.01L, cos V>=1/L,
    |A_0|<=6r/L, |K|<=1.16, Re A_0>=3.9r/L^2,
    -Re A_0 s^2+|Z(s)|<=-[(799/300)r/L^2]s^2.

It assigns the first-mode lower-power contribution2L^(3/2)/r,
between its distant horizontal left-tail and remaining local-mode
allowances. Its final aggregate includes2/12^3. No supplement or
finite-band cell certificate is invoked for this individual allowance.
AppendixB supplies the proof structure; AppendixC supplies the saved
domain/width and effective claim. Its coefficient2 remains to verify.
No bound, specialization or scalar comparison was calculated here.

## Applicability and work reserved for reproduction

Read C048c's hypotheses and equations(3)-(19) with their proofs:
exact S normalization, branch/reflection geometry, segment containment,
amplitude bound and absorbed curvature. They have exactly the saved
p,w,h_p,g,K,A_0,width. In particular C048c(19) verifies the absorbed
curvature on the full sector; it is not an unproved source premise.
C048c expressly excludes this lower-power correction. C048d's
Gaussian-pair result also does not pay it or require a repeat audit.

The later reproduction must identify the correction using
pi exp(w)=2p/w, bound it on the finite interval, retain
sqrt(|A_0|/pi), and extend only a nonnegative real Gaussian majorant.
Check the coefficient2 uniformly at L=12, unbounded L, real p,
both angular boundaries and reflection. These are unperformed tests.
Do not transfer AppendixB's width or its finite-band cell prerequisites.

Reuse DLMF7.7.6, https://dlmf.nist.gov/7.7.E6 , already inspected in
source-notes1630 and applied in C048c's Gaussian paragraph: its
coefficient a satisfies Re a>0, its integration endpoint is real,
and its square root is principal. The zero-moment real specialization
needs positive real coefficient, as supplied by C048c(19) for the
prospective majorant. No reread is needed for this unchanged coverage.
Full matching Mathlib coverage remains unchecked, not absent.

## Duplicates, failures and bounded searches

Read L799's hypotheses, conclusion and normalization proof through its
amplitude estimates. Its full theta correction rho includes the
negative first-mode factor but uses the different saddle
x(pi exp(2x)-9/4)=s, rotated diameter x+exp(-i Arg(A)/2)v,
width3/(16Re x), and normalization sqrt(2pi/A). Its bound cannot
transfer to the saved integral. Reuse source-notes1627's L798-L800
comparison and source-notes1630's failure comparison. The scoped
lower-power/T_low search in Mellin literature/history/attempt paths
found the nomination and prior exclusions, not a matching proved bound.

Read ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md:
whole-path domination, uniformity and endpoint requirements block the
automatic global import. This finite test neither contradicts that
stop nor imports the source's full(29), zero counts, inversion or signs.

Web queries: exact title with first/saddle and with low-order;
Kawano/Mellin/lower/202611.0383; 202611.0383/B_low;
Kawano/lower-power/theta/Mellin. The relevant primary hit was the
manuscript; unrelated hits were not theorem evidence. No independent
stronger theorem was located in this bounded search, with no novelty
inference. The known Gaussian method is covered, while the moving-sector
constant needs reproduction because the preprint claim is being tested.

The scope test passes with a qualification: T_low is the notebook's
operational definition of the source's local absolute allowance, not
a printed source symbol or a full-path theorem. Prove that application
explicitly later. A failed sufficient majorant alone refutes neither
T_low nor RH. Higher modes, horizontal tails, remainder assembly and a
sufficient all-degree sign bridge remain independent. This component
supplies no specific new central Mellin-to-sign mechanism for creative
routing; historical stops are not global bans.
