# Horizontal Mellin local error: nominated reproduction audit1627

TARGET: Audit Kawano v1's finite horizontal leading-mode phase/amplitude error T_loc(p)<=A_loc L^(9/2)/r with A_loc<1.318214 on L>=12, Re(p)>=-|p|/(4L), including all auxiliary bounds and the complex Gaussian normalization specified in this assessment.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed comparison1627 and source-notes1627: exact-title/constant discovery, L798-L800 hypothesis comparison and scoped global-import, finite-index and reciprocal-kernel stops. No matching ready local inequality found in that scope; no novelty inference.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2 (28)-(31), AppendixB local Taylor/four-term cancellation and Gaussian moments, AppendixC local inequalities and A_loc; DLMF7.7.6 https://dlmf.nist.gov/7.7.E6 ; O'Sullivan PJM298(2019), Assumptions1.1/Theorem1.2 pp159-160 and Corollary5.1 pp175-176, primary comparison reused from 2026-11-05-actual-mellin-remainder-source-scope.md.
COMPARISON: Source already claims this effective local allowance using Taylor cancellation and Gaussian moments; L798-L800 use a different saddle, contour and amplitude split and supply no matching bound. General fixed-phase saddle results do not establish its moving-sector constants. Independent verification is reproduction, not a new saddle theorem.
GAP: Prove or rigorously fail the precisely defined T_loc inequality, paying every branch, denominator, Lambert, curvature, Taylor and numerical comparison used. Stronger source auxiliary bounds are obligations, not assumed inputs. Other theta terms and global errors are independent gaps.
REASON: Accessible primary formulas specify one bounded analytic test without unavailable supplements, zero certificates, inversion or an assumed sign theorem. Its relevance is one remainder component, with no claim of progress beyond the source's stated mathematics.
SCOPE: Newly nominated in1627; separate approval next turn is required before mathematical invocation. SPECIALIZE permits REPRODUCTION for exactly this finite local audit and its necessary auxiliary bounds. It does not approve full (29), other error components, or a creative central-sign mechanism. Full matching Mathlib coverage unknown.

## Exact proposed test, not an established result

The main gap is L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. A verified local allowance could contribute to a full
actual-theta Mellin remainder. Other components, zero counts,
inversion and a sufficient Mellin-to-sign implication remain open.

For p in the full closed sector

    r=|p|>=exp(12), L=log r, Re p>=-r/(4L),

use C048a's principal Lambert branch and C048b's S normalization:

    w=W_0(2p/pi)=U+iV, u_0=w/2, d=1/(3L),
    h_p(u)=2p Log u-pi exp(2u),
    g(u)=8pi^2 exp(9u/2)/u, g_0=g(u_0),
    A_0=-h_p''(u_0)/2,
    K(s)=g(u_0+s)/g_0,
    J_loc(p)=integral[-d,d] K(s)
                     exp(h_p(u_0+s)-h_p(u_0)) ds,
    G_loc(p)=integral[-d,d] exp(-A_0 s^2) ds,
    T_loc(p)=|J_loc(p)-G_loc(p)|/|sqrt(pi/A_0)|.

The integration variable s is real, the segment horizontal and
oriented from -d to d. Log is principal. The square root must agree
with the Gaussian branch continued from positive real p; justify
that it is the principal root once Re A_0>0 is established. Verify
the relation S(p)=g_0 exp(h_p(u_0))sqrt(pi/A_0), including its phase,
before asserting that this normalization pays the source budget.
That relation is an audit obligation here, not a new proved identity.

The sought bound is

    T_loc(p)<=A_loc L^(9/2)/r,
    A_loc=sqrt(6) [13/(2(39/10)^(3/2)12^2)
                   +33/(2(39/10)^(5/2)12)
                   +15/(799/300)^(7/2)] <1.318214.

This operationalizes the source's printed local cost. The numerator
subtracts the finite Gaussian; Gaussian extension is not charged here.
The leading amplitude g excludes the negative lower-power first-mode
term and n>=2 modes; their source allowances are recorded separately
in source-notes1627. Do not call T_loc a full-theta remainder.

## Inputs, proof obligations and decision test

Established local inputs available for narrow reuse are C048a's
branch/contour/kernel definitions and C048b's U>3L/4, U<L,
|w|<L+2, cos V>1/(4L), with their full-sector qualifications.
C048b's origin inequality itself is not required to prove T_loc.
L797-L800 are comparison/method references, not established premises
for this new phase. No cross-notebook input is needed.

Source-notes1627 records all printed stronger auxiliary constants:
|w|<=1.01L, cos V>=1/L, Re A_0>=3.9r/L^2,
|A_0|<=6r/L, cubic/quartic and amplitude Taylor bounds, and
b_*=(799/300)r/L^2. Prove the versions actually used, or disclose
a correction and compare the resulting constant with the exact
A_loc target. Neither the printed source claims nor a grid are
unconditional hypotheses. Check the segment lies in Re u>1 and
the theta strip, g_0 and A_0 are nonzero, both signs of Im p,
zero height, Re p<0, the radial and angular boundaries and unbounded L.

The primary method is the source's explicit four-term residual
split, cancellation of linear and cubic terms under a complex even
Gaussian, followed by absolute real Gaussian moment bounds.
DLMF7.7.6 has real endpoint and Re a>0; applying it with a=A_0
requires the proved curvature condition. If deriving Gaussian
moments by differentiation, justify domination or integration by
parts. No new general saddle theorem is required.

Continue with a uniform analytic proof paying the stated threshold.
A rigorous violating T_loc refutes this local reading, not RH.
Failure only of an auxiliary majorant is not a counterexample to
the integral: record the exact failure and save partial reasoning.
A weaker cost must be compared to A_loc and cannot be called a pass.
If unpaid, repeat only with a refined mechanism or new input.
Do not reopen supplement searches, full remainder assembly or the
completed origin audit under this target. After any proposed proof,
schedule independent conceptual review before treating it as audited.

This is established-route development, with no justified creative
central-sign claim. No mathematics has been performed or approved
in this nomination. The separate approval requirement preserves
the completed source comparison's outcome.
