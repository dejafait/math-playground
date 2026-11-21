# Gaussian extension: primary-source extraction1630

Inspected19November2026: K. Kawano, *Logarithmic Inequalities of Arbitrary
Order for the Riemann Xi Coefficients*, Preprints.org202611.0383v1,
posted4November2026, DOI10.20944/preprints202611.0383.v1,
https://www.preprints.org/manuscript/202611.0383/v1 . The URL redirects
to a page marked Version1 and not peer reviewed. The following are
source statements and applicability comparisons, not a new tail proof.

## Exact primary cases

Section5.2(28) continues branches from positive real p and reflects to
the lower half-plane. Its proof uses horizontal s=Re u-U/2.
AppendixB bounds |A_0| by mathcal A and Re A_0 below by real b>0;
the paragraph immediately preceding its B_g display states

    integral_{|s|>d} exp(-b s^2) ds <= exp(-b d^2)/(b d),
    B_g=sqrt(mathcal A/pi) exp(-b d^2)/(b d).

Thus this allocation already includes both tails. AppendixB uses
width7/(10L) on7.5<=L<=12.3. AppendixC instead sets

    L>=12, r=exp(L), Re p>=-r/(4L), d=1/(3L),
    Re A_0>=3.9r/L^2, |A_0|<=6r/L,
    y_0=exp(12)/12^4,
    A_g=[sqrt(6/pi)/(13/10)]sqrt(y_0)exp(-(13/30)y_0)<0.099276.

Its next sentence invokes increasing y=exp(L)/L^4 and decreasing
sqrt(y)exp(-c y) over the relevant range. No finite-band certificate
or supplementary archive was needed or retrieved for this extraction.
The source's constant and monotonicity are still assertions to verify.

## Standard theorem statements inspected

Live NIST DLMF, accessed19November2026, equations7.7.6 and7.8.1-7.8.2;
no release number established. [7.7.6](https://dlmf.nist.gov/7.7.E6):

    integral_x^infinity exp(-(a t^2+2bt+c)) dt
      =(1/2)sqrt(pi/a) exp((b^2-ac)/a)
          erfc(sqrt(a)x+b/sqrt(a)), Re a>0, real x.

[7.8.1-7.8.2](https://dlmf.nist.gov/7.8.E2):

    M(x)=exp(x^2)integral_x^infinity exp(-t^2)dt,
    1/(x+sqrt(x^2+2))<M(x)<=1/(x+sqrt(x^2+4/pi)), x>=0.

DLMF cites Mills(1926), Mitrinovic(1970),p177 and Gautschi(1959b).
Those originals were not read and supply no additional premises here.
The selected real upper bound has no large-argument exception.

## Exact applicability and work reserved for reproduction

C048c's hypothesis matches the saved target, including negative Re p,
both angular boundaries, r=exp(12), real p and unbounded L.
Its equations(9)-(10) establish the two curvature bounds above, with
strict slack. Its equation(3) establishes the complex S normalization;
its definition of G_loc uses the same horizontal s and width. Those
passages were read directly. Extension is expressly excluded there.
The prospective standard Gaussian substitution is a=A_0, b=c=0,
x=d (or x=0 for completion). C048c supplies Re a>0 and the principal
root. The later proof must write out convergence and the pair-of-tails
identity; it must retain the normalization sqrt(|A_0|/pi).

For an absolute majorant, the prospective real Mills argument is
d sqrt(b)>0, with b=Re A_0, not complex d sqrt(A_0). The exact complex
identity and a positive real majorant have distinct roles. Verify the
direction of every replacement of b and |A_0|. Reserve the substitution
algebra, the c=13/30 monotonicity threshold, endpoint enclosures and
strict comparison to the rational decimal0.099276 for the next research
turn. No such derivation or numerical calculation occurs here.

The source defines no symbol T_ext: the saved observable operationalizes
its B_g charge of the omitted Gaussian pair. It is an upper-majorant
reading, not a claim that a complex integral equals its absolute integral.
Do not carry over AppendixB's different width or cell prerequisites.
The permitted domain/width are those explicitly printed in AppendixC.

## Known results, duplicates and failure limits

Reused source-notes1627 and assessment1627's fixed-phase saddle comparison;
no general saddle theorem supplies this effective moving-sector constant.
Read L800's complete proof/audit and the November5 Gaussian scope/test
assessments. L800 uses curvature |A|/2, rotated segment d=3/(16u),
normalization sqrt(2pi/A) and a different saddle/domain. Its real-tail
method is relevant but its bound cannot be imported with renamed symbols.

Read ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md.
That stop concerns whole-path domination and uniform remainders; this
isolated Gaussian assessment neither contradicts nor resolves it.
History1629 preserves the preceding local audit and changed-target gate.
No matching proof of this T_ext or counterexample to it was found in
these narrowly inspected records; no novelty follows from that search.

Discovery queries were exact Kawano/Gaussian-extension/0.099276 terms
and complex Gaussian tail/Re/erfc terms. The former returned this source;
the latter mostly probability results about complex random variables.
Those theorem texts were not inspected or used. No stronger independent
parameter-specific theorem was located in this bounded search. Primary
NIST coverage suffices for the method without repeating that search.

The comparison supports SPECIALIZE and a separate REPRODUCTION attempt
on the unchanged exact TARGET. Full matching Mathlib coverage is
unchecked, not absent. Continue only with a uniform analytic estimate
and rigorous scalar endpoint check. A failed sufficient majorant alone
does not disprove T_ext; a violating T_ext would refute this local source
allocation, not RH. Other theta modes, horizontal tails, Mellin assembly,
zero counts, inversion and sufficient mixed signs remain independent.
No central creative mechanism follows from this isolated allowance;
the all-order Mellin-to-sign bridge still needs a specific new input.
