# Full-divisor phase: primary source comparison1721

19 November 2026. Literature only; no enclosure was calculated.

## Exact scope and local screening

The reviewed target is the TARGET of assessment1720. Main gap:
L030-L032/C032a actual-Xi all-degree positivity. Intermediate target:
the phase at 1/8 lies strictly between zero and pi for every width in
[1,2]. C032n(15),(19) gives its prospective use as the nonvanishing
premise of a width-ratio test. W's sign remains unpaid independently.

Read C032j's source conventions, C032m's Gaussian bounds through (7),
and C032n's complete attempt1711, including (15)-(20) and its park.
Reused comparison1709 and stop1711; inspected the earlier finite-height
citation in L466 narrowly. The present question is neither the stopped
scalar recursion nor a repetition of its unsigned determinant bound.
No cross-notebook input was used. All preexisting work is preserved.

## Search record

Queries included: `Platt Trudgian Riemann hypothesis true up to 3 10 12
theorem 1 2021 pdf`; `Hasanalizade Shen Wong number zeroes Riemann zeta
function explicit 0.1038 theorem`; `Gaussian zero smoothing phase Sra
Riemann`; `Accurate estimation of sums over zeros Gaussian Theorem 2`;
`Sra Pσ Gaussian phase`; `Riemann Gaussian cumulative 1/8`.
Search snippets were discovery only. The comparisons below use primary
PDFs. No matching upper enclosure was found in the inspected statements;
this neither establishes absence from the literature nor novelty.

## Inspected primary inputs

Suvrit Sra, *Some positivity properties of Riemann Xi under smoothing*,
[fixed 2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1), released
11 November 2026: normalization (1.1), Section2's P=2 integral p,
Section3.1 Gaussian, Theorem3.3 (p6), and AppendixC.5 (pp23-24), all
three proof ranges. For T>=10^11 with V(T), it states P_sigma(x)>0
for x>0 and sigma>=1/(16 log T). At verified T=3*10^12 its threshold
is <0.00218. The phase convention is A=pi P, so this covers the lower
inequality by applicability, not a new estimate. AppendixA.1 (p12)
specifies multiplicities, the real anchor in (14,15), and counting;
C.5 separates the origin, middle range and unbounded range. No upper
bound P(1/8)<1 occurs there. Retain C032j's preprint qualifications;
the external computation was not rerun. This is not pointwise p>=0
at all widths or an unsmoothed conclusion. PropositionC.1 was located;
its additional proof is not needed when citing Theorem3.3 directly.

Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3 times 10^12*, Bulletin LMS53 (2021), 792-797,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1), Theorem1 and
Section2, p2: all zeros through 3,000,175,332,800 are on the line.
The sign-change count is checked against all zeros by Turing's method.
The upper endpoint is included; the theorem is stronger than the
notebook's cutoff. Section2 explicitly says high-precision ordinates
were not retained. Thus it is a completeness theorem, not a downloaded
list of coordinates. No simplicity assumption is needed here.

Chiara Bellotti and Peng-Jie Wong, *Improved estimates for the argument
and zero-counting function of the Riemann zeta-function*,
[2412.15470v2, 7 July 2025](https://arxiv.org/pdf/2412.15470v2),
Theorem1.1, p1, gives for every T>=e, with
M(T)=T/(2*pi)*log(T/(2*pi*e)),

    |N(T)-M(T)| <= 0.11200 log T +0.12567 log log T +3.77417.

Its alternative is 0.10076 log T+0.24460 log log T+8.08344.
Read the theorem, Table1 footnote1 (p2), and Section5 (pp23-24):
large-height parameter specialization and small-height completion.
Use precisely v2 constants, not a search-result variant. N counts
positive ordinates through T. At a cutoff, one-sided count limits
must retain multiplicity; no endpoint is silently removed. This
provides an explicit envelope, not a Gaussian bound by itself.

Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros
of the Riemann zeta function*, JNT235 (2022), 219-241,
[author's published PDF](https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf):
read Corollary1.2 (p221), counting/argument-principle setup (pp220,223),
and its proof (pp238-239). Its displayed 9.3675 constant is explicitly
corrected to 9.4925 by Bellotti-Wong's Table1 footnote. The continuation
will use the latter paper directly. This discrepancy matters for a
rigorous certificate; the older displayed constant is not approved.

Richard P. Brent, David J. Platt and Timothy S. Trudgian, *Accurate
estimation of sums over zeros of the Riemann zeta-function*, Math.
Comp.90 (2021), 2923-2935, DOI10.1090/mcom/3652,
[published author copy](https://maths-people.anu.edu.au/~brent/pd/rpb276-electronic.pdf).
Read ConditionA/Theorem1 (PDF pp1-2), conventions (p4), complete
Lemma3 proof (pp6-7), Lemma4 and Theorem1 proof (p8).
For 2*pi<=T0<=T, phi C2, nonnegative, decreasing, convex, and
integral_T^infinity phi(t)log(t/(2*pi))dt finite, its primed tail is
that integral/(2*pi)-phi(T)Q(T)+E2, where

    |E2| <= 2*(2.067+0.059 log T)*|phi'(T)|
            +(0.059+1/150)*phi(T)/T.

Q=N-L, L=M+7/8. Endpoints carry half mass and multiplicities are
retained. The theorem is unconditional but applies only to ordinate
weights, not complex-center Gaussian values. Any proposed positive
majorant must satisfy every hypothesis uniformly, and cutoff mass
must be reconciled with the notebook convention. No Gaussian
specialization is proved here.

## Decision and limits

SPECIALIZE: citation supplies the lower sign; explicit counting and
tail results support a bounded test of the upper bound. A count
envelope can replace a coordinate list for a deliberately coarse
enclosure, but that replacement and its numerical margin must be
proved later. No missing coordinate list is an essential source
blocker for that test. A raw finite-zero preview is never sufficient.

Continue only with a full analytic or directed-interval enclosure over
the closed width interval and a strict upper margin below pi, retaining
the cited lower sign and all source qualifications. If the coarse
bound fails, save its actual versus required bound and stop this
attempt; do not infer a negative phase or reopen W from that failure.
Independent signed W, ordered-minor signs, general signed measures,
positive output and actual-Xi transfer remain open. This is established
route development, not a creative central mechanism. Full matching
Mathlib coverage was not checked. No lemma or mathematical script
was changed; no new theorem is asserted by this source review.
