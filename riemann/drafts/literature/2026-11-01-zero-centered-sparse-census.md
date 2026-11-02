# Zero-centered sparse census — completed source comparison

TARGET: Assess whether known unconditional local zero-counting theorems supply C645h's sparse census at a hypothetical off-line zero with n=floor(log gamma), retaining all multiplicities.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched local zero density N(sigma,T+1)-N(sigma,T), explicit disk counts centered at 2+it, and off-line zero multiplicity bounds; reused the two saved vertical-Pick count/density assessments and L467's audit coverage. Primary sources inspected below; search snippets and secondary Lindelof summaries are leads only. No matching unconditional sparse census was found in this bounded search; this is not an absence or novelty theorem.
SOURCE_EVIDENCE: Bellotti--Wong arXiv:2412.15470v2 (7 July 2025), Theorem 1.1 p.1, Section 3 opening p.9, Section 5 pp.23--24 and Corollary 1.6/Section 6 pp.4--5,24--26; Ivic arXiv:1706.08268v1, (2.11) p.6, Theorem 4/Corollary 1 pp.10--12; author-hosted Vaughan Chapter 10 Section 1 Exercise 20(a) p.321. Reused Baluyot 2017 Theorem 1.2.1 p.16 and its previously inspected proof cases, without broadening their scope.
COMPARISON: Theorem 1.1 is unconditional and uniform at every ordinate with multiplicities, but counts all real parts. The inspected density input is cumulative, not a bound on every zero-centered disk; Ivic bounds one zero's multiplicity, not the disk census. The conditional small-o local-count comparison assumes Lindelof. None states the required kappa_delta bound. C645i remains a synthetic contrast, not an actual-zero counterexample.
GAP: A separate mathematical application must justify the closed-disk enclosure, source subtraction and endpoint limits, then compute the complete finite-height envelope and its leading coefficient against kappa_delta*floor(log gamma). No actual sparse census has been established or refuted.
REASON: Essential source coverage for this bounded application is now ready. SPECIALIZE permits only the count-envelope and threshold comparison under the unchanged target, not a new local density theorem or a repetition of the Hankel construction.
SCOPE: Fixed 0<delta<1/2, gamma>=e^5, n=floor(log gamma), all zeros of xi in the stated closed disk with multiplicities; apply the cited global count and the already audited endpoint method. No typical-height, simplicity, RH, Lindelof, clearance, or actual-Xi matrix-positivity hypothesis is available.
LITERATURE_REASON: The invocation-start assessment was REVIEW_REQUIRED for this exact zero-centered coefficient and quantifier comparison; existing operator and density coverage did not assess it. This turn completes that source gate without writing a lemma or mathematical script.

## Exact question for the next review

Fix 0<delta<1/2. Conditionally consider a nontrivial zero
rho=1/2+delta+i*gamma, gamma>=e^5, allowing arbitrary multiplicity.
Use the definitions already fixed in C645g/C645h:

    R = 3/2-delta/2,
    n = floor(log gamma),
    kappa_delta = delta / (16*(1+log(256*R/delta))).

Let M_rho count, with multiplicity, every xi zero w in the closed disk
|w-(2+i*gamma)|<=R. Ask whether a named unconditional theorem supplies

    M_rho <= kappa_delta*n

for every such zero above an onset depending only on delta. Compare the
exact finite-height bounds even if they do not meet this threshold.
Do not replace all zeros by distinct zeros, disregard boundary zeros,
assume simplicity, condition on typical heights, or choose gamma from
a favorable set unrelated to the hypothetical off-line zero.

The later application would still separately require fixed positive
boundary clearance, its complete pole set, the stipulated interpolation,
and a useful independent boundary upper bound. The question here does
not assume or establish any of these. It also does not address initial
heights or prove positivity of L645's actual matrices.

## Reuse, bounded test and routing

Essential local identifiers for the eventual comparison are L018, L467,
L645, C645g and C645h. C645i is the newly audited failure comparison;
C645b's envelope stop and the prior vertical-Pick favorable-height
selection difficulties remain independent obstructions. Read only the
necessary statements/source ranges, not whole earlier proof chains.
Consult the local GOAL's overlap assessment and external-input register
before relying on their newer strip claims or reopening parked estimates.

Start with the exact local-shell theorem and saved primary density
comparisons. Retrieve any missing primary hypotheses and the relevant
local-versus-averaged proof cases. A sufficient citation with the required
uniformity is a positive source finding; otherwise record the strongest
actual bound and the precise missing coefficient or quantifier. An
average density bound alone is not a local census at a zero ordinate.
Failure to find a sufficient theorem is not a disproof of the count.

This is a materially different, independently assessable input question,
not a rerun of one-sided support or its counterfamily. The nomination
above records the original question; the completed review below now
supersedes its pending-source language. Full matching Mathlib coverage
is not checked.

## Primary evidence and comparison completed on 2026-11-01

Bellotti--Wong, [versioned PDF](https://arxiv.org/pdf/2412.15470v2),
Theorem 1.1: for H>=e, |N(H)-F(H)|<=E_i(H), i=1,2, where

    F(H)=H/(2*pi)*log(H/(2*pi*e)),
    E_1(H)=0.10076*log(H)+0.24460*log(log(H))+8.08344,
    E_2(H)=0.11200*log(H)+0.12567*log(log(H))+3.77417.

Section 3 uses the argument principle, hence counts orders. Section 5
combines Table 2's large-height case with a computed argument bound at
compact heights. These are cited inputs, not independently verified
computations. Corollary 1.6 counts unit/two-unit ordinate intervals,
without horizontal restriction. Section 6 uses differences of S; it
does not make zero ordinates favorable centers. Its proof displays a
2.00001 factor before conclusions displaying 2; this review does not
resolve that discrepancy. Use Theorem 1.1 directly, not that corollary,
for the pending finite-height application.

Theorem 1.1 supplies the sharpest asymptotic global-count error
coefficient among the explicit total-count inputs inspected here.
This does not assert that its induced disk estimate is optimal among
all known horizontal local-count methods. Neither L467's coarser shell
constant nor a count of distinct poles can replace residue multiplicity.
The size of an error envelope is not a lower bound on the actual census.

The [saved density assessment](2026-11-01-vertical-pick-density-weighted-annulus.md)
already inspected Baluyot's thesis Theorem 1.2.1 and the integrated,
near-line and dyadic proof cases. For fixed 0<theta<4/7 its bound is
N(sigma,H)<<_theta H^[1+theta*(1-2*sigma)] log H, uniformly sigma>=1/2,
with strict beta>sigma. It is a cumulative count. Subtracting two upper
bounds would not bound their difference; using one cumulative upper
bound would retain its height power. No pointwise logarithmic census
at each exceptional zero ordinate is supplied. An inclusive horizontal
cutoff needs a strict lower threshold before using this source.

Ivic, [1706.08268v1](https://arxiv.org/pdf/1706.08268), (2.11),
records the unconditional m(beta+i*gamma)<<log gamma for beta>=1/2.
Theorem 4 and Corollary 1 require 5/6<=beta<1 and large gamma;
the latter gives m<=4 log log gamma+20(1-beta)^(3/2) log gamma.
The Section 5 proof uses a rectangle and a Vinogradov--Korobov bound
at real part 3*beta-2, explaining the beta restriction. These estimates
count one zero's order, not all distinct zeros and orders in our disk;
they cannot be summed without an additional count input. No such input
is imported here. Their full source proofs have not been independently
audited.

Vaughan's [author-hosted Chapter 10](https://personal.science.psu.edu/rcv4/568s20/568chapter10.pdf),
Section 1 Exercise 20(a), p.321, explicitly assumes Lindelof before
asking for an o(log T) count in a fixed rectangle strictly to the right
of 1/2. It is a conditional comparison, not an unconditional theorem
available here. Titchmarsh--Heath-Brown Theorem 13.5 was located as an
equivalence lead, but its relevant pages were not successfully retrieved;
no assertion from that unread theorem is used. This is not an essential
source blocker for the unconditional total-count specialization.

The local baseline register was read. Its fixed half-plane statements
do not give a census in the remaining strip; displacement values they
exclude make the hypothetical anchor vacuous. No new half-plane theorem,
or quantitative consequence of its proof, is claimed or needed here.

## Ready mathematical continuation and stopping test

Keep the exact TARGET; only its source gate has been completed. Apply
Theorem 1.1 directly to a closed ordinate enclosure of the disk. Retain
lower-endpoint zeros by the one-sided limit already justified in L467;
check gamma>=e^5 is sufficient for every source argument. Obtain the
full finite-height envelope, including constants and n=floor(log gamma),
before comparing leading coefficients. This application has not been
proved in this literature-only turn and is the one next mathematical
attempt. A reproof of the analytic count theorem is unnecessary.

Continue this count-envelope mechanism only if it certifies the exact
sparse threshold, or identifies a concrete refinement that could do so.
If its coefficient is too large, record that precise deficit and park
this envelope as a source of the census; do not conclude the census is
false. Independent horizontal localization would then need a genuinely
different test and separate coverage. Selection, clearance, complete
pole accounting, interpolation, a smaller boundary upper bound, initial
heights and all-degree signs remain unresolved even after a sufficient
census. No actual-Xi or RH conclusion is approved.
