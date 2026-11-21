# Uniform two-atom retained-cost test: ready coverage, separately approved

TARGET: Test whether the shared positive two-site Uvarov system forces B_d>=c*d^2 uniformly for affine full-theta references plus two unit atoms with a_(d-1)=0, or construct a feasible degree sequence with B_d/d^2 tending to zero.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed review1931 of nomination1930 searched the exact cost/family and stronger orthogonal-polynomial modification results, plus scoped C028/finite-atom failures; no inspected theorem decides the uniform floor and no novelty is inferred. Full search record in source-notes1931.
SOURCE_EVIDENCE: Direct primary PDFs https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf and https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf verified accessible 2026-11-20; reuse source-notes1931's precise primary citations and proof reads: Delgado et al., SIGMA12(2016),090,Theorem3.1,(3.1)-(3.14),pp8-10; Schmeisser2002,Theorem1/Corollary1,pp205-207,Lemmas1/4/5 and complete Theorem1 proof,pp211-214; supporting DLMF18.2 coverage1908/1920/1926/1694. No asymptotic lead is imported.
COMPARISON: C028p's parity-based scale floor and C028c's fixed Hermite-prefix recurrence do not cover the changed family. C028t/v supply no all-degree cost estimate. The shared two-site kernel system is available but the proposed uniform three-residual conclusion is not known from the inspected sources.
GAP: Establish the uniform retained floor or a rigorously feasible infinite-degree sequence refuting it without new unproved recurrence/compactness assumptions; lower/full costs and C028b's H_d=o(d) remain independent gaps.
REASON: One bounded new finite-rank cost mechanism is justified at the central reference-budget bottleneck, with a decisive threshold and preserved prior stops. Separate literature approval completed in recovery1932 with direct primary URLs; the exact target, hypotheses and permitted mechanism are unchanged.
SCOPE: Exactly the full-theta affine/two-unit-atom family and three retained terms below; arbitrary d-dependent parameters, d>=4 and a_(d-1)=0. One symbolic proof/countersequence attempt; no collar matching, numerical sweep, new mass parameter, source refinement or assumed theta asymptotic.

## Exact prospective target and permitted mechanism

Use C028t's probability mu_0 with density K(|x|)/(2*I_0), actual monic
P_d=R_d/gamma_0 of C028a, and integers d>=4. For real t,A<B and s>0,
all allowed to vary freely with d, set

    nu=((x->t+s*x)_*mu_0+delta_A+delta_B)/3.

Let q_j be the monic orthogonal polynomials of this measure,
h_j=integral q_j^2 dnu, and P_d=sum_(j=0)^d a_j*q_j, a_d=1.
Feasible means a_(d-1)=0, with no further presumed cancellation. Set

    B_d=(h_(d-2)*a_(d-2)^2+h_(d-3)*a_(d-3)^2
                          +h_(d-4)*a_(d-4)^2)/h_(d-1).

Seek c>0 and D>=4 such that B_d>=c*d^2 for all d>=D and every
feasible choice. Alternatively, give explicit feasible choices along
integer d_n->infinity with B_(d_n)/d_n^2->0. Exact cancellation of all
three retained terms along such a sequence would suffice to refute the
floor. No such sequence, feasibility theorem or bound is asserted here.

The proposed mechanism is to keep the shared two-site evaluation system
and positive modified norms in the imported Uvarov formulas while
extracting only the top residual coefficients. Test whether these joint
constraints force a positive normalized cost despite parameter escape,
or allow an explicit asymptotic cancellation mechanism. A rank-two
change of the moment functional must not be replaced by C028c's
particular last-two-recurrence modification. All actual coefficient
comparisons and any parameter normalization remain mathematical work.
The Uvarov/Schmeisser theorems themselves are cited, not reproved.

One coherent symbolic attempt is authorized after separate approval.
No fixed compact parameter restriction, bounded standardized sites,
exchange of site/degree limits or theta recurrence asymptotic may be
assumed. A proof must cover s tending to0/infinity, unbounded translations
or sites, and site coalescence limits as relevant to the universal claim;
every finite member still has s>0 and A<B. A countersequence must check
these finite admissibility conditions and exact a_(d-1)=0. Neither
small finite-degree costs nor a count of free parameters is sufficient.
If the argument needs an uncovered asymptotic, save its exact statement,
remaining derivation and hypotheses and stop; it requires REVIEW_REQUIRED
before dependent work. Save unfinished reasoning before lengthy work.

## Relevance, stop test and inputs

C028b's H_d=o(d) remains the main unpaid height criterion. A uniform
retained floor would rule out this reference family's Schmeisser upper
payment, leaving actual H_d undecided. A countersequence would defeat
this obstruction and could guide a changed reference shape; it would
not upper-bound the omitted terms or establish RH. No root-reality,
positive realization or small full-cost premise is introduced.

Continue only with a proved bound/sequence, informative new obstruction,
or precise useful intermediate condition. After one unresolved attempt,
retain partial reasoning and identify the missing condition; repeating
it needs a materially new input or refined mechanism. Whole-collar
matching remains parked under C028u/v; this target does not reopen it.

Essential inputs: C028a/b/c/o/p/t/v,L019/L021,source-notes1931 and reused
1908/1920/1926. C028c/o/p are scope contrasts and available finite source
interfaces, not floors for this family. The base positivity/moments and
actual coefficient convention are mathematical inputs. No finite Decimal
certificate is needed for this initial symbolic attempt; importing new
numerical moment claims would need their full contracts and evidence.
Unresolved: degree-uniform retained control, lower/full costs, H_d=o(d)
and actual-Xi all-degree positivity. No cross-notebook theorem. Full
matching Mathlib coverage unchecked. Proposed classification is
POTENTIALLY_NEW only in the limited search-assessment sense, not certified
originality; importing the source formulas alone is known mathematics.

## Separate source-gate approval, recovery1932 (2026-11-20)

The direct published PDFs above were opened successfully. Delgado et al.,
Theorem3.1, printed p9, explicitly assumes both original and modified
functionals quasi-definite and supplies the finite-site invertibility and
connection/norm formulas. Schmeisser, Corollary1, printed p206, gives the
root-height upper estimate recorded in source-notes1931. These are the
same sources and interfaces already assessed; their full proof reads and
positive-measure applicability argument are reused, not repeated. No
asymptotic estimate or uniform retained-cost lower bound is imported.

The recovery repairs the missing direct URLs in this assessment itself.
No new search-based novelty conclusion, mathematical derivation or
source-scope expansion is claimed. The EXPLORE decision is approved for
the exact TARGET and SCOPE above; the next invocation may perform its one
bounded symbolic attempt. All prior stops and independent gaps remain.
Mathlib matching coverage remains unchecked.
