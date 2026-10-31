# Polynomial heat-energy obstruction — source-approved calculation

TARGET: Test whether a finite even polynomial heat family with positive imaginary-axis values, strip-confined zeros and zero endpoint flux can violate a locally bounded backward first-Laguerre energy comparison through a multiple real zero.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Laguerre/heat/negative-energy and polynomial searches, plus local duplicate/failure checks, are recorded in drafts/literature/2026-10-30-backward-heat-negative-energy-coverage.md. No inspected theorem supplies the requested collision-energy certificate; search failure is not novelty evidence.
SOURCE_EVIDENCE: Direct primary PDFs checked 2026-10-30: Alber Lemma 5.2/Theorem 5.3, pp. 90--92, https://www2.mathematik.tu-darmstadt.de/~alber/pde_2.pdf ; Brezis--Ponce Theorem 7.1 and proof, pp. 1234--1236, https://sites.math.rutgers.edu/~brezis/PUBlications/198journal.pdf ; Keady Theorem 1.2/Section 4, pp. 250, 256--257, https://doi.org/10.1017/S1446788700035679 . Full publisher PDF and applicability qualifications are below; no claimed RH preprint is imported.
COMPARISON: A finite polynomial test isolates the source comparison's missing interior-zero control while retaining evenness, positive imaginary-axis values and a finite strip. Fixed positive-defect endpoint collars prevent hiding production in an unspecified external flux. This is an elementary heat-collision/energy specialization, not a creative RH mechanism or known actual-Xi theorem.
GAP: Determine the exact clipped-energy behavior through a multiple real zero without dividing by H or E. No family meeting all certificate conditions and violating the comparison has yet been constructed or verified.
REASON: Separate literature approval repairs the missing direct-source URLs and confirms the previously inspected tools for the unchanged finite-polynomial collision test. EXPLORE authorizes that bounded test only; this approval establishes no new mathematical result.
SCOPE: Finite real even polynomial heat families of degree at most eight on a compact parameter interval; only the zero-flux finite-interval negative first-Laguerre energy comparison below. No actual-Xi conclusion, global bound or general positivity claim.

## Exact test

Seek a nonzero real even polynomial P of degree at most eight, h>0 and
its exact finite heat evolution

    H_lambda(x)=sum_{k=0}^{floor(deg(P)/2)}
                       (-lambda)^k P^(2k)(x)/k!,
    lambda in [-h,0], I=[-2,2],
    q_lambda=H_lambda'^2-H_lambda H_lambda'',
    E_lambda=integral_I (-q_lambda)_+ dx.

This is a proposed family definition; verifying its evolution equation
is part of the calculation. Require H_0(0)=1, H_lambda(iy)>0 for every
real y, all its complex zeros in |Im z|<=1/2, and q_lambda>0 on both
fixed collars [-2,-7/4] and [7/4,2], for every parameter. Multiple real
zeros are allowed and must not be divided out of the energy. The
conditions have not been verified for any P here.

The comparison under test is

    -partial_lambda E_lambda <= C(lambda) E_lambda

almost everywhere, with C locally bounded through lambda=0. C may
depend on the fixed polynomial family, interval and its finite compact
jet bounds. It may not become singular at a collision by invoking an
unproved positive lower bound for |H| or E. Fix the candidate diffusion
flux as the sum of outward normal derivatives of (-q)_+; the collar
condition requires it to vanish. Internal interfaces of {q<0} are not
external boundary flux and cannot be silently deleted.

Use the source truncation/trace theorems by citation with the stated
smoothness, or directly justify their elementary finite-polynomial
specialization. Any energy differentiation must keep its correct a.e.
or one-sided time qualification. A reproof is justified only for an
explicit energy calculation not supplied by the cited theorems.

Decisive evidence sought: a complete symbolic certificate of the
conditions with E_0=0 and some E_lambda>0 for lambda<0, tested against
the standard integral Gronwall comparison, or a rigorous unbounded
production/energy ratio approaching a collision. Include complete
relevant jets, interval roots/signs, all parameter inequalities, traces
and limiting behavior. Numerical previews are insufficient. If a
script is useful, save its certificate and print only the bound,
failure/decision and artifact paths; a hand proof may suffice.

Such a certificate stops this generic bounded-C comparison only.
Failure to find one in degree eight is not evidence of a theorem;
record the tested family and remaining bulk obligation instead. A
finite-interval identity alone does not meet the threshold.

## Inputs, limits and routing

L058 supplies the actual theta heat convention and positive imaginary-axis
comparison property; L018 supplies its Xi meaning. L471 and L486 explain
the signed-negative-mass gap and the stopped positive-majorant threshold;
none supplies a polynomial realization as actual Xi. L126/L128's old
moving-supremum stop remains a contrast, not an input to this comparison.
No cross-notebook theorem is used.

The proposed test is a calculation using known heat and truncation tools.
Potentially new refers only to the unchecked exact certificate, not to
heat collisions or a novelty assertion. If approved for research, use
REPRODUCTION or POTENTIALLY_NEW as warranted by what is actually proved.
This nomination does not license a broader creative attempt. Transfer
to actual Xi, normalized large-height mass, global endpoint control,
all-height signs and all-degree positivity all remain unresolved.
Mathlib full matching coverage is not checked.


## Direct-source recovery and separate approval, 2026-10-30

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment. This turn repairs that coverage field and checks the cited hypotheses; it does not repeat discovery or expand the target.

The preceding assessment's exact searches and duplicate/failure comparison are reused unchanged. The sole additional query was `Keady persistence logconcavity positive solutions heat equation 1990 pdf`, to recover the publisher PDF after the DOI fetch timed out. No persistent essential-source blocker remains.

- **Alber**, *Nonlinear elliptic and parabolic partial differential equations (PDE 2)*, last modified 10 June 2018, [primary PDF](https://www2.mathematik.tu-darmstadt.de/~alber/pde_2.pdf), Section 5.1. The printed page labels place Lemma 5.2 on pp. 90--91 and Theorem 5.3 on p. 92 (PDF pages 90--92); the preceding review's pp. 89--91 locator was imprecise. Read both statements, the bounded approximation proof and the zero-level argument. On a bounded open set, for 1<=p<infinity, these give absolute-value/positive-part Sobolev regularity and the a.e. derivative rule, including vanishing on the zero set. Smooth finite polynomial spacetime functions satisfy the regularity requirement. Integrating in space and handling exceptional times remain calculation obligations; the theorem supplies no nonlinear energy inequality.
- **Brezis--Ponce**, *Kato's inequality up to the boundary*, Comm. Contemp. Math. 10 (2008), 1217--1241, [published author-hosted PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/198journal.pdf), Theorem 7.1 and proof, pp. 1234--1236. Rechecked W^{2,1} hypothesis, BV conclusion, Lemmas 7.1--7.2 and all boundary-value cases. The normal trace of u_+ is the trace of u when u>0, zero when u<0, and min(partial_n u,0) when u=0, a.e. on the boundary. Smooth spatial polynomial slices meet the hypothesis. The proposed collars must still be verified for a candidate; internal interfaces cannot be erased by a boundary citation.
- **Keady**, J. Austral. Math. Soc. A 48 (1990), 246--263, [direct publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/136790B75EBEC163688603A5CBF42D05/S1446788700035679a.pdf/persistence_of_logconcavity_for_positive_solutions_of_the_one_dimensional_heat_equation.pdf), DOI above. Rechecked Theorem 1.2, p. 250, and Section 4/Theorem 4.0 with its proof, pp. 256--257. Smooth positive heat solutions with nonpositive I_2 initially and in boundary neighborhoods retain logconcavity. The proof uses logarithmic quantities and bounded-coefficient maximum principles. An interior collision is outside this positivity hypothesis. This result is a comparison only, not an imported collision-energy estimate.

Approval: retain DECISION EXPLORE for the exact TARGET and SCOPE above. No essential unread theorem is being assumed to supply the energy estimate. The next calculation must establish every candidate condition, the full relevant clipped-energy behavior and the Gronwall or unbounded-ratio test itself. An elementary direct energy calculation is justified because these tools do not evaluate that functional. No lemma or mathematical script was written in this literature turn. Full matching Mathlib coverage remains unchecked. This is a source-access/process repair, not new evidence against the comparison or progress beyond the inspected sources.
