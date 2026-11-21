# Near-left horizontal allowance: source comparison1644

19 November2026. Literature-only review of assessment1643's exact target.
No new inequality or mathematical script is established.

## Primary statement and essential cases

K. Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, Preprints.org202611.0383v1, posted4November2026,
DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The live redirect
identifies Version1, not peer reviewed. Inspected Section5.2(28),
Lemma5.1(i), complete left-side proof(31), AppendixB's C_n/B_-/B_f
and full-mode inequalities/proof sentence, and AppendixC's domain,
width, A_- and monotonicity. No unread supplement is used.

The source uses r=|p|, L=log r>=12, Re p>=-r/(4L), w=W_0(2p/pi),
u_0=w/2, branches continued from positive p, and reflection below the
real axis. Its h_p,g,A_0,S match C048c. Lemma5.1(i)(29) asserts a
complete relative remainder <=(17/10)L^(9/2)/r; it is not imported.
AppendixC uses d=1/(3L) and separately prints

    y_0=exp(12)/12^4,
    A_-=[(3/2)sqrt(6/pi)/(133/54)]
                       sqrt(y_0)exp(-(1007/2430)y_0)<0.091191.

Section5.2(31) asserts the phase bound on x=Re u>=1, s=x-U/2,
with v_0=pi exp(U)cos V and phi(s)=exp(2s)-1-2s. For upper-half-plane
p=sigma+i tau, y=V/2, the proof defines
Q(x)=(sigma x+tau y)/(x^2+y^2), Q(U/2)=v_0.
For sigma>=0 it uses the numerator of Q'; for sigma<0 it uses
Q'=(sigma-2xQ)/(x^2+y^2) on Q>0 and the decreasing numerator of Q.
It concludes Q(x)>=v_0 on 1<=x<=U/2 and explicitly reverses
integration on the left. These are inspected source proof cases,
not independently established inequalities in this literature turn.

AppendixB defines

    C_n=(1+3W_*exp(2)/(4r))
                     (1+32exp(-3v exp(-2)))/(1-2/u),
    B_-=C_n sqrt(mathcal A/pi)
               exp(-9d/2-v phi(-d))/(9/2+2v(1-exp(-2d))).

Here u bounds U below, W_* bounds |w| above, v bounds v_0 below,
and mathcal A bounds |A_0| above. The proof uses the tangent to phi
at -d and integrates a positive envelope; s<=-1 receives a separate
tangent at -1 and C_f/B_f. It supplies theta-series bounds for real
t>0 and t>=1, with the latter justified by consecutive-term ratios.
The near-mode majorant uses the t>=1 case, a hypothesis to verify.
AppendixB's finite band and width7/(10L) do not match AppendixC;
cell constants cannot be substituted on all L>=12. AppendixC asserts
uniformity using increasing exp(L)/L^4 and decreasing sqrt(y)exp(-cy).
Its A_- coefficient and monotonicity remain verification obligations.

## Segment and operational absolute observable

The split at s=-1 and C_n's exp(2),1-2/u factors identify the near-left
component as -1<=s<=-d, followed farther left by s<=-1 on x>=1.
This is an inference from the displayed majorant and split, not a
separately printed author-defined integral. A_- does not pay the whole
horizontal path down to x=0 or an origin continuation. Define

    F(z)=1-3/(2pi exp(2z))
          +sum_{n>=2}(n^4-3n^2/(2pi exp(2z)))
                            exp(-pi(n^2-1)exp(2z)),
    T_nearleft(p)=integral_{-1}^{-d}
       |K(s)F(u_0+s)exp(h_p(u_0+s)-h_p(u_0))| ds
                                       / |sqrt(pi/A_0)|.

Use exactly C048c's K,h_p,u_0,A_0 and principal square root.
F is L799(4)'s general strip factor 1+rho, also used in C048g.
The source's nonnegative full-mode envelope supports assessing this
integral of moduli; a modulus after integration cannot replace it.
Reproduction must verify its equality with the normalized full Mellin
integrand, including the factor 2/u and S(p). No frequency-cell
perturbation is included. The target is T_nearleft<=A_- L^(9/2)/r.

Future obligations: prove the whole segment ordered and within x>=1,
the theta strip and principal Log domain; control the complete F;
verify the left phase for sigma>=0, sigma<0, real p and reflection;
check tangent direction and positive decay rate; pay normalization and
exact A_- uniformly at L=12, both angular boundaries and unbounded L.
Extending the scalar envelope integral to -infinity does not extend
the actual theta or phase estimates there. A finite local-disc or
right-ray estimate is insufficient. No obligation was proved here.

## Existing coverage, duplicates and failures

Reuse the completed 2026-11-05-mellin-left-horizontal-segment-scope.md
and audit assessment: Luc Devroye, *Non-Uniform Random Variate Generation*
(Springer-Verlag1986), ChapterVII Section2.6 pp299-300, envelope before
Theorem2.6 and reflected-case reduction/first integral in its proof,
https://luc.devroye.org/chapter_seven.pdf . This covers the real
differentiable concave tangent method, not probability normalization
or complex theta log-concavity. Ready coverage was not reread.

Compared L802's full statement and November5 history529: its audited
bound uses x(pi exp(2x)-9/4)=s, outward height Im(x-da), interval
[u/2,Re(x-da)], sqrt(2pi/A) normalization and modulus after integration.
These differ from this Lambert saddle, fixed height, [-1,-d] relative
interval and integral of moduli. L802 remains an audited method example,
not an input inequality. No detailed L802 proof was needed. Read L799's
general strip convergence/identity(4); its diameter bound is not extended.
C048g's right phase/amplitude are not assumed on the left.

Near-left/A_-/B_-/T_left/T_near searches in Mellin-named local literature,
histories and attempts found nominations, exclusions and L802 records,
not a matching canonical allowance. External queries:
`"202611.0383" "left"`, `"Kawano" "Mellin" "B_-" "tail"`,
`"Logarithmic Inequalities of Arbitrary Order" "horizontal"`.
Kawano was the relevant primary match; unrelated hits supplied no input.
No failed search establishes novelty. Matching Mathlib coverage is
unchecked; no theorem is claimed absent.

Read ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md:
automatic whole-contour import remains stopped. This independent finite
component assumes no continued origin, global deformation or unread
supplement. No blocked supplement search or cross-notebook read occurred.

## Decision and bounded continuation

SPECIALIZE: accessible primary cases and reusable effective-envelope
coverage support a separate REPRODUCTION attempt. Citation alone cannot
certify this quantitative preprint claim or absolute specialization.
The ready nomination1644 requires separate next-turn approval. This
review reports EXPLORATION, not an inequality or mathematical discovery.

Continue only with a uniform proof and rigorous constant evidence, or
retain an informative obstruction to the selected sufficient majorant.
A failed method does not refute T_nearleft or RH; repetition requires
materially new input. L030-L032/C032a actual-Xi all-degree positivity
remains the main gap. This finite component could complement C048c-g
in a later remainder. Distant-left/origin, assembly, zero counts,
inversion and sufficient mixed signs remain independent. No tested
central Mellin-to-sign mechanism emerged to justify creative routing.
