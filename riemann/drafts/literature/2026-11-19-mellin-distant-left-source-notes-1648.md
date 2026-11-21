# Finite distant-left component: source comparison1648

19 November2026. Literature-only review of assessment1647's exact target.
No new inequality is established. The source's quantitative claims below
are objects for reproduction, not imported mathematical premises.

## Primary source and complete relevant cases

K. Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, Preprints.org202611.0383v1, posted4November2026,
DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The accessible
HTML redirects to the manuscript URL and identifies Version1, not peer
reviewed. Read Section5.2(28), Lemma5.1(i)(29), the complete horizontal
phase proof(31), AppendixB's parameter definitions, C_f/B_f display,
both full-mode inequalities and their proof explanation, and AppendixC's
domain and distant-tail allocation. No supplement is used or sought.

Section5.2 uses the same r=|p|, L=log r, w=W_0(2p/pi)=U+iV,
u_0=w/2, h_p, g and S(p) as C048c. Branches continue from positive
real p and conjugation treats the lower half-plane. Lemma5.1(i) claims
the whole remainder <=(17/10)L^(9/2)/r when L>=12 and
Re p>=-r/(4L); this global claim is not imported.

The horizontal phase statement(31) applies on x=Re u>=1, with
s=x-U/2, v_0=pi exp(U)cos V and phi(s)=exp(2s)-1-2s.
The proof treats sigma=Re p>=0 and sigma<0 separately through
Q(x)=(sigma x+Im(p)V/2)/(x^2+(V/2)^2), and explicitly reverses
the integration on the left. These cases were read, rather than
extending a right-side phase assertion by analogy. Real p and
lower-half-plane reflection must also be justified in reproduction.

AppendixB is expressly a FINITE-band majorant: 7.5<=L<=12.3,
r=exp L and Re p>=-r/(4L). Its eight Lambert enclosures define
u<=U<=h and W_*=(h^2+(pi/2)^2)^(1/2)>=|w|. It defines c=sin(s_*),
where s_* uses the displayed arctangent/arcsine lower-clearance formula;
cell checks require 0<s_*<pi/2, c>1/L and u>5. Then

    v=2rc/W_*,  b=2v(1+u/W_*^2),
    mathcal A=(4r/u)(1+1/u),

bound v_0 from below, Re A_0 from below and |A_0| from above.
Here u is a bound for U, NOT the integration variable. Its local
width is 7/(10L), unlike AppendixC's 1/(3L). No finite-cell enclosure,
cell positivity result or maximum F(L) is extended to unbounded L.

The source's separate far-left factors are

    C_f=55W_*[1+(pi exp(2)c)^(-5/2)],
    B_f=C_f sqrt(mathcal A/pi)
          exp(-9/2-v(1+exp(-2)))
                    /[9/2+2v(1-exp(-2))].

The adjacent text assigns s<=-1 to the tangent at -1 and this full-mode
bound. It prints the complete weighted-theta inequalities

    sum_{n>=1} n^4 exp(-(n^2-1)t)<=100(1+t^(-5/2)),  t>0,
    sum_{n>=2} n^4 exp(-(n^2-1)t)<=32exp(-3t),         t>=1.

For the first it specifies integral plus maximum of the unimodal
function x^4 exp(-t x^2); for the second it specifies consecutive-term
ratios. The first case is essential here: no lower bound t>1 or t>2
is available from C048h on the new segment. The negative-power mode1
term and n^2 terms still need their own justified domination in F.
The source does not give a separately numbered proof of C_f or
of the transition from this finite-band expression to AppendixC.
That is a quantitative verification obligation, not an inaccessible
essential source theorem. The inspected method and cases are explicit.

AppendixC, on the FULL sector L>=12, prints v_0>=1.9r/L^2,
Re A_0>=3.9r/L^2 and |A_0|<=6r/L. After the A_-/A_+/A_g
display it gives the distant horizontal left-tail bound

    sqrt(6/pi) L^(11/2) exp(-2r/L^2)/(3sqrt(r)),

and asserts that this and the extra-local-mode bound are each less
than 10^(-4)L^(9/2)/r. This supplies the concrete prospective
C_far=10^(-4). Neither the displayed intermediate bound nor this
coefficient has been verified in this literature turn. The finite
absolute observable is inferred from the s<=-1 split, x>=1 phase
domain and nonnegative majorants; it is not a separately named source
integral. In particular an integral of moduli must be checked, not
replaced with the modulus of an integral.

## Operational comparison and permitted specialization

Retain exactly assessment1647's T_farleft, with s in [1-x_0,-1],
x_0=Re u_0, F from C048h and K,h_p,A_0 from C048c. C048c(3)-(10)
and L799's strip identity(4) supply the existing geometry, normalization
and normally convergent series, not a new far-left inequality. Read
C048h's definition and normalization(3)-(5) only for this comparison;
its near-left amplitude and t>2 estimates are outside the new interval.

The prospective proof must identify the full normalized integrand,
including 2/u, and the principal Gaussian root with S(p). It must
pay the saddle ratio, lower-power mode1 and EVERY remaining mode for
all positive real theta parameters. Use only x>=1 strip estimates;
an envelope integral may be extended only after its valid finite
interval has been established. Extending the envelope does not extend
the actual theta estimate or justify any origin continuation.

Reproduction must verify segment ordering, principal Log domain, both
signs of Re p, both signs of Im p, real p, L=12, both closed angular
boundaries and unbounded L. It must justify any reuse of C048h's phase
argument on x>=1 separately from that lemma's finite near-left result.
Finally it must prove the explicit 10^(-4) coefficient, or record a
rigorous obstruction to the selected sufficient majorant. The stronger
intermediate AppendixC expression is a source comparison, not a
required additional conclusion if the approved coefficient is proved
directly by the same covered effective methods.

## Reused methods, duplicates and failures

Reuse assessment1644/source-notes1644's inspected Devroye,
*Non-Uniform Random Variate Generation* (Springer1986), ChapterVII
Section2.6 pp299-300, reflected tangent envelope preceding Theorem2.6
and its proof, https://luc.devroye.org/chapter_seven.pdf . This is only
a real concave-envelope method; it imports no complex theta positivity.

Reuse the November5 far-left source and audit assessments' inspected
NIST DLMF v1.2.8 (15September2026), equation5.9.1 and its following
hypotheses, https://dlmf.nist.gov/5.9#E1 . The formula evaluates
integral_0^infinity exp(-z t^mu)t^(nu-1)dt as
Gamma(nu/mu)/(mu z^(nu/mu)), assuming Re nu>0, mu>0 and Re z>0,
with principal powers. Real Gaussian moments with positive parameter
fit this scope once those hypotheses are checked. No complex
saddle estimate is imported by this citation. Direct formula use
must cite it; no reproof of the gamma integral is justified.

The narrow duplicate search located audited L803/history533. Read
its complete hypotheses/conclusion and Gaussian-method citation
passage, not its full proof. Its saddle solves
x(pi exp(2x)-9/4)=s on a different D, the height is the outward
L802 endpoint height, its segment reaches zero, and its normalization
is sqrt(2pi/A). Its conclusion bounds a modulus AFTER integration.
None is a matching theorem for this Lambert saddle, fixed V/2,
[1,x_0-1] segment, S(p), or integral of moduli. L802 has the same
previously recorded saddle/height mismatch. These results provide
method comparisons; they are not proposed direct inequality inputs.

Searched farleft/far-left/distant-left/distant-tail/C_far/B_f in
C048 lemma files, Mellin-named local assessments/attempts, relevant
November5 far-left histories and November19 Mellin histories. No
matching canonical allowance was found in that bounded scope.
External queries were `"202611.0383" "distant" "tail"`,
`"Kawano" "Mellin" "full" "theta" "bound"`, and
`"theta" "sum" "unimodal" "Gaussian" bound`. The primary Kawano
manuscript was the relevant match; search hits about Gaussian
mixtures and unrelated theta applications supply no mathematical input.
No failed search establishes novelty. Matching Mathlib coverage is
unchecked; neither absence nor formal verification is claimed.

Read and preserve ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md.
Its missing global domination and unread derivations remain unpaid.
No repeated blocked-source access or cross-notebook input was needed.

## Decision and limits

SPECIALIZE: the primary full-mode cases and explicit distant-tail
allocation, together with already inspected effective methods, cover
a separate REPRODUCTION attempt. Citation alone cannot certify the
absolute specialization or preprint constants. The newly written ready
nomination1648 requires separate approval next turn; no mathematics is
performed or approved as proved by this source review.

Outcome EXPLORATION records new source extraction/comparison and a
concrete test, not a mathematical advance or informative counterexample.
Continue if the exact finite absolute coefficient is established; stop
the selected method on a rigorous majorant obstruction. A failure
would refute neither the integral inequality nor RH. The possible
downstream use remains a separately assessed full Mellin remainder.
Origin/global assembly, zero counts, inversion and sufficient actual-Xi
mixed signs remain independent. No specified signed inversion mechanism
emerged, so no central creative target is manufactured for scheduling.
