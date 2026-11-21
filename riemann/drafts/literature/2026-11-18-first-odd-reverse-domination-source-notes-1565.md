# Reverse all-Borel comparison: source review1565

18 November 2026. Literature only; no actual-law inequality is proved.

## Target, relevance and scope

Reviewed exactly assessment1564's saved target: positivity of the unique
mass-one widths1,2 law with its first odd coefficient cancelled, via
nu_2<=k*nu_1, k=p_2(0)/p_1(0). Calculation1564 fixes k>1 and the
coefficient orientation. The main gap remains actual-Xi all-degree
positivity in L030-L032/C032a. This finite building block could inform
C032q's feasibility problem; full continuum cancellation and realization
remain independent. A source must give the actual constant on all Borel
sets or a valid obstruction. A criterion or unspecified constant does
not pass that test.

Read C032j, C032m's definitions/regularity statement, C032q's full
hypotheses/conclusion and cited construction interface, C032s, C032u,
calculation1564, notes1562 and finite-Levy assessment1551. Checked the
specific ATTEMPTS1302/1534/1536 (including1538 audit)/1546/1551/1564.
Their scopes are retained. No one-jump threshold test was located in
the narrowly searched first-odd/finite-Levy notes and C032u. This is
not an archive-wide absence or originality claim.

## Inspected primary statements and applicable coverage

**Mixture proportions.** Gilles Blanchard, Gyemin Lee and Clayton Scott,
*Semi-Supervised Novelty Detection*, JMLR11 (2010), 2973-3009,
[Proposition5 p2984 and complete AppendixA.2 p3001](https://www.jmlr.org/papers/volume11/blanchard10a/blanchard10a.pdf).
Reused notes1562 and directly read these ranges. The greatest removable
coefficient is the essential infimum of the absolutely continuous
Radon-Nikodym component, relative to the reference probability. The
proof retains the singular component, constructs the endpoint residual,
and uses positive-reference-mass sets avoiding the singular part.
For the present order take P_X=nu_1 and P_0=nu_2. The question is
whether the removable coefficient is at least 1/k. Neither that value
nor an actual minimizing set is supplied. The equal-law case is covered.
No density with respect to Lebesgue measure is needed. Reversing these
roles would answer a different question. This is applicability of the
cited criterion, not a new theorem or a computed coefficient.

**Subordinator density estimates.** Tomasz Grzywny, Lukasz Lezaj and
Bartosz Trojan, *Transition densities of subordinators of positive
order*, J. Inst. Math. Jussieu22 (2023), 1119-1179,
[doi:10.1017/S1474748021000360](https://doi.org/10.1017/S1474748021000360),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D5F2B35C637219171CD84A4C465654E8/S1474748021000360a.pdf/transition-densities-of-subordinators-of-positive-order.pdf).
Inspected Theorem3.3 pp1131-1132, Theorem4.17 p1161 and its complete
proof pp1162-1164. The former requires weak lower scaling of -phi''
with index alpha-2, alpha>0, and gives absolute continuity and a
restricted saddle approximation. The latter requires zero drift,
weak lower/upper scaling of phi with 0<alpha<=beta<1, and an almost
monotone Levy density. Its two-sided estimates hold for specified
space/time ranges, globally in space when the scaling cutoff is zero.
The proof joins saddle, intermediate and large-space estimates through
comparison constants. These are not the exact paired constant k.
No application is imported: required scaling/regularity and constants
for B_1,B_2 are unproved here; the full proof of Theorem3.3 was not
audited. Density existence alone would also leave the paired ratio
bound unpaid. This excludes an immediate invocation, not future use
after additional estimates. No new density assertion is made.

**Finite activity and bounded transforms.** Reuse the ready primary
coverage in notes1552, C032u and notes1562. Jean Bertoin,
*Subordinators, Levy processes with no negative jumps, and branching
processes*, Maphysto2000, [Theorem1.2 pp7-8 and finite-activity case
p9](https://www.maphysto.dk/oldpages/events/LevyBranch2000/notes/bertoin.pdf);
Steven P. Lalley, *Levy processes, stable processes, and subordinators*,
[Definition5.1, (5.2)-(5.4), p12](https://galton.uchicago.edu/~lalley/Courses/385/LevyProcesses.pdf).
They provide the positive compound-Poisson series for a finite positive
jump measure. C032u already identifies this series for Pi(dt)=D(t)dt,
with total mass M, zero-jump weight exp(-M), and nu_2=nu_1*pi.
Its resulting domination is a lower bound for nu_2. No sharp upper
bound is contained in that construction.

Ante Mimica, *Laplace transform*, Dresden2015,
[Proposition1.4(i),(iv), pp6-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf),
provides positive-parameter derivatives and the positive convolution
transform. Directly revisited the statement and first-derivative proof;
complete relevant coverage is reused from1562/1563 and1552. For a
positive finite residual, integrating any bounded nonnegative test
must give a nonnegative value. C032q's bounded Borel integration
identity supplies the existing actual-law interface. These inputs
suffice for a prospective one-jump necessary test without density or
endpoint moment assumptions. No first moment or new inequality is
computed here.

The fixed-v1 smoothing source was opened narrowly at Section3.1 and
Theorem4.1/A.7. Its time-change and heavy-Levy-tail results give no
paired probability-law upper comparison. A statement about the
Gaussian mixture law mu_sigma on R is not a density theorem for
nu_sigma on [0,infinity). No new source-wide audit or finite-zero
verification was performed. The inherited inputs remain qualified.

## Search record and decision

Queries included: subordinator transition densities ratio upper bound
Levy measures convolution domination likelihood ratio compound Poisson;
infinitely divisible distributions bounded likelihood ratio Levy
measures domination densities; subordinator likelihood ratio densities;
convolution bounded density ratio heavy tailed; subordinators domination
densities upper; compound Poisson domination density ratio; subordinator
Harnack density ratio; and the exact smoothing-source identifier.
Search results concerning stochastic order, inverse subordinators,
Harnack estimates and path likelihoods were leads only; no theorem
from them is imported. The density-paper publisher HTML timed out on
a follow-up; its publisher PDF supplied the inspected statements and
proof. No persistent essential access blocker remains. Generic failed
searches establish no novelty or impossibility.

New source-scope evidence: the inspected density theorem does not
supply the desired constant, even before its missing hypotheses are
checked. Park automatic generic-density import. The mixture criterion
remains a characterization, and C032u remains a lower comparison.
This is NEGATIVE for those immediate imports, not for output positivity.

## One prospective bounded mechanism

Prepare exactly the COVERED_TARGET in assessment1564: test the proposed
one-jump majorant with constant M+log(k), and check whether positive
convolution iteration would make it sufficient. It is deliberately a
stronger intermediate proposal, not an asserted equivalent criterion.
Neither the estimate nor its sufficiency has been proved in this turn.
Use only bounded Laplace differences and the existing entire lifts;
retain mass terms and avoid subtracting divergent moments. This is
independent of assuming a Lebesgue density, asymptotic smoothness,
global scaling or a numerical inverse transform.

A failed majorant stops that sufficient mechanism only. A favorable
necessary transform test leaves the all-Borel estimate unresolved.
Stop after one attempt if those existing inputs do not decide it;
no automatic extra jumps, widths or derivative orders. This is a
concrete applicability test using classical tools, not a central
creative mechanism. The continuum witness or controlled approximation
needed for a justified creative target is still missing.

Retain actual divisor/multiplicity, zero-ordinate exclusion, strip and
counting, verification through100, first-zero/tail, heat and fixed-v1
qualifications. No RH, profile positivity, density, exponential moments,
full J_eta=0 or unsmoothed Xi realization is assumed. Full matching
Mathlib coverage remains unchecked and unknown. No lemma, DAG, PROOF
or mathematical-script change is justified by this source review.
