# Signed Rice mechanism: stationary-point sector gate1662

TARGET: Test whether the principal Rice main term F_d^S(s)=sqrt(pi)*4^(-s)*S(s+1/2)*B_d(s)/(Z*Gamma(s+1/2)) has a stationary point in d^(1/3)<=|s|<=d^(2/3), Im(s)>=|s|/2, with p=s+1/2 in C048j's audited sector, for every sufficiently large integer d.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step1663 completed the scoped Mellin/Rice duplicate and failure search and primary Rice-saddle comparisons; exact queries and inspected ranges are in 2026-11-19-rice-saddle-sector-source-notes-1663.md. No matching location theorem was found in the bounded search; no novelty is inferred.
SOURCE_EVIDENCE: Direct primary URLs: DLMF5.11.2 https://dlmf.nist.gov/5.11#E2 and complex remainder https://dlmf.nist.gov/5.11#ii; recurrence/reflection https://dlmf.nist.gov/5.5#E2 and https://dlmf.nist.gov/5.5#E4; W derivative/branch https://dlmf.nist.gov/4.13#E4. Reopened and checked in recovery1664; reuse C048l(13) and notes1656/1660. Prior inspected Rice comparisons: Flajolet--Sedgewick1995 p120 https://algo.inria.fr/flajolet/Publications/FlSe95.pdf; Flajolet--Vepstas Section4 https://arxiv.org/pdf/math/0611332v2; Mazhouda Sections2--4 https://arxiv.org/pdf/1506.01755v1; exact hypotheses and limits in notes1663.
COMPARISON: Established derivative and branch tools cover the saved main-term test after the documented full-argument sector checks. The inspected Rice saddles concern different coefficient functions; the Li asymptotic assumes GRH. None decides this F_d^S stationary equation. No differentiation of I/S or generic signed saddle import is licensed.
GAP: Existence or exclusion of stationary points for the combined explicit main term in the full specified region remains unproved; actual-I derivative transfer, nondegeneracy, admissible deformation, signed margin and height transfer remain separate.
REASON: Established derivative tools cover one bounded ordinary specialization, provisionally REPRODUCTION; a citation alone does not locate this observable's stationary points. Separate recovery review1664 checked the primary URLs and approved the unchanged SPECIALIZE scope without deriving a stationary equation or mathematical result.
LITERATURE_REASON: Recovery1664 requires a direct source URL in the ready assessment itself. Add checked primary URLs to SOURCE_EVIDENCE and review the unchanged scope; reuse notes1663 rather than repeat the completed theorem search.
SCOPE: The exact TARGET and region below only, with fixed actual Z and the explicit principal S. Coverage permits a later uniform existence/exclusion test; it excludes actual-integrand derivative control, saddle expansions, contour deformation and sign/height conclusions.

## Direct-source recovery and approval1664

19 November2026. The supervisor reported that ready assessments need a
direct source URL. SOURCE_EVIDENCE now contains the primary URLs,
including the digamma expansion and its separate remainder paragraph.
Reopened DLMF5.11, 5.5 and4.13: the sector condition, complex-remainder
factor, noninteger reflection restriction and principal W branch agree
with notes1663. The prior Rice comparisons and scoped duplicate/failure
checks are reused unchanged. No broader source search or mathematical
specialization was performed. This is a metadata repair, honestly
STALLED as mathematical progress; it does not renew any exploration
budget. The separate approval requested by review1663 is completed for
the exact TARGET and SCOPE above. The next action is the saved bounded
mathematical test. No actual-I derivative or sign conclusion is covered.

## Completed review1663

The primary-source hypotheses, applicability checks, exact overlap and
unread-lead qualifications are recorded in
[source notes1663](2026-11-19-rice-saddle-sector-source-notes-1663.md).
C048l already supplies the exact S derivative; the newly inspected
digamma remainder closes the essential analytic-source gap. No
stationary-point location is accepted in this review. The next step
should perform the unchanged mathematical test after separate approval.
This is routine localization preparation; a justified creative signed
mechanism is still blocked by untested candidate phase geometry.

## Exact proposed test, not a derived result

Use S(p), its principal branches and B_d(s) exactly as in C048l,
and the actual fixed Z=gamma_0. Define the proposed main term

    F_d^S(s)=sqrt(pi)*4^(-s)*S(s+1/2)*B_d(s)
                                  /(Z*Gamma(s+1/2)).

A stationary point means (F_d^S)'(s)=0, with the derivative
in the complex variable s. It concerns this explicitly specified
main term, not the derivative of the actual I or E. The test region is

    d^(1/3)<=|s|<=d^(2/3),  Im(s)>=|s|/2,
    p=s+1/2, |p|>=exp(12), Re(p)>=-|p|/(4log|p|).

The powers specify a bounded degree-dependent annulus for the
proposed test; no claim that it contains all relevant saddles is
being made. The positive-imaginary restriction chooses one member
of a prospective conjugate pair. No stationary equation has been
solved and no asymptotic for its solutions is asserted in this
nomination. Definition of the observable is not approval to derive it.

The main gap remains actual-Xi positivity through L030-L032/C032a.
C028b's sufficient H_d=o(d) criterion and a signed bridge remain
unpaid. C048l now supplies a checked finite closing error at x=-1.
A signed saddle comparison would be a different mechanism from
absolute edge closure. Before attempting that mechanism, this test
asks whether candidate saddles can even be treated with the current
audited Mellin sector. It is a concrete prerequisite, not a claim
that another modulus estimate proves a sign or that this annulus
already gives sufficient root coverage.

After adequate source review, continue toward a signed mechanism
only if a rigorous stationary-point location stays in the stated
sector; even then nondegeneracy, accessible contour paths, control
of the actual remainder and a useful signed comparison remain open.
A rigorous eventual absence of stationary points in this region
would stop direct use of an in-sector saddle there. It would not
exclude saddles outside the annulus, other representations,
nonstationary methods or RH. An inconclusive test must name the
unpaid derivative or localization estimate, not repeatedly enlarge d.

## Original nomination contract (completed by review1663)

The nomination required a literature-only invocation. Preserve the exact proposed
stationary-point test while searching its standard Rice, Mellin and
steepest-descent terminology and stronger known localization results.
Read primary theorem hypotheses and relevant cases for any uniform
digamma or logarithmic-derivative estimate actually needed; the
previous log-Gamma error may not simply be differentiated. Reuse
the inspected finite Rice and W facts rather than reviewing them
generically. Compare the named local Mellin/Rice records first,
then only the specific further duplicates identified by that search.

The canonical inputs are C048a, C048j, C048k and C048l. L718's
noninteger-size interpolation and the Airy Cauchy-integral record1345
are contrasts, not mathematical inputs or global bans. The existing
source comparisons have not established coverage for the new
stationary equation. No unread source theorem is assumed.

In particular, a bound on |I/S-1| does not itself bound its derivative
or justify differentiating its error. A successful main-term test
still needs a separately approved transfer and deformation step.
Full matching Mathlib coverage is unchecked. Review1663 changes this
assessment to SPECIALIZE for the unchanged target; no localization
result or new mathematics is derived or approved here.
An eventual creative signed-comparison attempt must name its real
phase/cancellation obstruction and bounded test after this coverage
and feasibility gate, rather than label routine gamma specialization
creative to satisfy a scheduling target.
