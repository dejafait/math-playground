# Source scope for auditing the actual signed remainder/residue comparison

TARGET: Assess source coverage for an independent audit of L722's actual signed remainder/residue rate gap, including its exact phase certificate and limsup qualifications.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 198 reused the completed step-174 exact-target/stronger-result search and step-184/195 tool assessments; read L722 in full, its script and four imported helper definitions, L719/L721 interfaces, step-196/197 histories and the specific signed-rate/common-phase/gamma-Rice stops. Targeted primary lookup inspected the calculus, Simpson and logarithm statements below; no repeated broad saddle search or novelty claim.
SOURCE_EVIDENCE: NIST DLMF live text inspected 2026-11-03: 1.4(v), (1.4.18); 1.4(vi), (1.4.35)--(1.4.37); 1.10(i), (1.10.1); 3.5(ii), (3.5.6)--(3.5.8); 4.6(i), (4.6.4). Inherited finite inversion and signed support-transfer coverage is reused, not reapproved here. Exact links and hypotheses follow.
COMPARISON: Standard composite Simpson gives a sharper C^4 error formula than L722's hand-derived bound, and DLMF supplies the exact logarithm series and integral Taylor tool. These cover the general tools, not this array's nonzero factors, support endpoint, phase geometry, rational enclosures or signed limsup comparison. L721 supplies only a limsup and L714 only the signed identity.
GAP: Independently audit L722 Sections 1--4 and the complete load-bearing certificate, including inherited interfaces, positivity near the actual support edge, segment Taylor bound, all exact rounding and subtraction qualifications. No essential inaccessible theorem remains for this bounded audit; none of those application checks is accepted by this source decision.
REASON: New source comparison resolves the nominated coverage gate and identifies a standard replacement for unnecessary general quadrature reproof. SPECIALIZE permits a separate audit of the existing application, not acceptance of its result or a new saddle/support theorem.
LITERATURE_REASON: The new L722 audit adds residue endpoint, rational phase and exact quadrature/logarithm obligations outside the already approved support-transfer audit; these are the changed source questions, not a reason to repeat its general source search.
SCOPE: Exactly the saved coverage target and the covered audit below, with the original L703 bump, L714 signed identity, L719 phase and L721 limsup. No changed peak/profile, endpoint law, full limit, complete-response or Xi conclusion is covered.
COVERED_TARGET: Critically audit L722's actual signed remainder/residue rate gap, including the residue endpoint argument, legal phase Taylor bound, complete exact certificate and limsup qualifications.

Essential input IDs: L714, L719, L721. L715/L716/L720 remain inherited
through those audited inputs. Original L703 chi and delta, u=(3+4i)/10,
U=121/64, A=27/10, d=5/4, c_0=1/8 and n=12q+3 remain unchanged.
The actual b=sup supp chi must not be replaced by omega+delta.

The bounded intended audit must check:

- The residue's nonzero factors, C^1 Riemann-sum bound and positive
  endpoint integral imply a full rate without endpoint positivity.
- L719's legal logarithms, exact stationary phase identity and rectangle
  imply a Taylor loss <1/3200 at s0=(73/40)(1-i), without using a
  diagnostic numerical saddle.
- The two rational squared moduli, fourth derivative bounds, composite
  quadrature constants and full logarithm tail enclose the actual
  integrals, including all rows and exact comparison values.
- L721 is used as a limsup only. The strict gap survives the signed sum
  on an infinite subsequence; zero subsequences and absence of a full
  limit are retained. No complete-response or RH inference is licensed.

The originally nominated primary/source scope was to be compared with the reused
rate assessment before approving an audit. No essential inaccessible
source has been identified. Full matching Mathlib coverage is not
checked. This file contains no newly derived mathematics and grants
no audit acceptance. The nomination's literature-only requirement is discharged
by step 198 below; the covered mathematical audit remains unperformed.

## Completed source comparison — step 198, 3 November 2026

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
target is reliability of L722's competing-rate obstruction at the unchanged
spatial peak. A favorable audit would justify abandoning the exponentially
subordinate signed-remainder certificate there; an error would reopen only the
affected comparison. Neither outcome settles complementary spatial Jensen
defect, the complete response, angular persistence, amplitude/full charge,
H/support or Xi realization. This is a literature-only step: no certificate
was replayed, no numerical bounds were accepted and no lemma was changed.

### Primary statements and exact limits of their coverage

1. [NIST DLMF 1.4(v), (1.4.18)](https://dlmf.nist.gov/1.4#E18)
   gives Riemann-sum convergence as the mesh tends to zero; continuous
   functions on a compact interval qualify.
   [1.4(vi), (1.4.35)--(1.4.37)](https://dlmf.nist.gov/1.4#E37)
   assumes C^(n+1) on the closed interval and supplies Taylor's integral
   remainder. For a complex-valued real-path function use the integral
   identity componentwise, not a common-point Lagrange remainder.
   These are the needed standard tools; the C^1 cell estimate, endpoint
   positivity interval and actual bounds remain application checks.
   No endpoint asymptotic theorem is necessary for the written argument.

2. [DLMF 1.10(i), (1.10.1)](https://dlmf.nist.gov/1.10#E1)
   gives a Taylor expansion on an analytic disk. It does not itself
   grant L722's numerical remainder constant. The segment must lie in
   the legal branch domain; the real-path integral remainder above is
   the appropriate tool for that bound. L719's audited phase identity
   and rectangle are inherited inputs, not newly checked conclusions.

3. [DLMF 3.5(ii), (3.5.6)--(3.5.8)](https://dlmf.nist.gov/3.5.ii)
   gives elementary and composite Simpson rules for real C^4 data on
   [a,b]. The composite rule uses even N, h=(b-a)/N, and error
   -(b-a)*h^4*f''''(xi)/180 for an interior xi. This is a stronger
   standard bound than the general K/(45*N^4) bound written in L722
   on [0,1]. A general quadrature reproof is therefore unnecessary.
   Import the standard rule; still check the actual two real log-modulus
   integrands, fourth-derivative bounds, weights, factor 1/2, grid and
   outward node errors. Reading the sharper theorem does not certify
   any recorded node or final comparison. The DLMF reference to Davis
   and Rabinowitz (1984), pp.57--58, was identified, not separately read.

4. [DLMF 4.6(i), (4.6.4)](https://dlmf.nist.gov/4.6#E4)
   states the odd-power logarithm expansion with variable
   (z-1)/(z+1), for the principal logarithm on Re(z)>=0, z!=0.
   The helper uses positive rationals reduced to [1,2], strictly
   within the convergence domain. The displayed infinite identity
   does not certify the helper's finite tail, its fixed-point rounding,
   reciprocal sign reversal or repeated log(2) additions. Those are
   finite implementation checks, including the stated conservative
   tail and all uses of the shared globals SCALE and TERMS. No general
   validated-arithmetic package theorem is invoked by this script.

All DLMF references are live statements read on CHECKED; no release number
is inferred. The linked equations and surrounding hypotheses were inspected;
their book proofs were not separately opened. The general results should
be cited, not presented as discoveries or reproved to expand the notebook.
The elementary endpoint sandwich and limsup arithmetic are already written
in L722; checking their actual hypotheses needs no new general theorem.
Full matching Mathlib coverage remains unchecked; these sources provide
supporting tools, not formal coverage of the claimed rate comparison.

### Reuse, duplicates, failures and bounded audit test

The unchanged `2026-11-03-signed-bump-remainder-rate.md` supplies the bounded
exact-target and stronger-result searches, analytic/Gevrey comparisons and
their limitations. The finite inversion assessment and the support-transfer
audit assessment supply the inherited source interfaces. They do not assert
L722's strict separation. No new generic support, gamma or saddle search is
needed. The step-175 reduction, common-phase stop and gamma/Rice domain
failure were read directly: none supplies the actual signed comparison,
and none is an additional premise. L721 is the distinct accepted input
that changed the old cancellation bottleneck. L713's envelope and L717/L718
remain excluded. No new claim of originality follows from this reuse.

The script and its four extracted helper definitions were read only to
identify tool requirements. It reads the preserved step-166 source and
extracts ceildiv/fixed/log_unit/logq; matching globals and helper content
must be checked on replay. The existing JSON was not loaded or treated as
verified evidence in this source turn. The separate audit must inspect the
complete load-bearing evidence, including both sets of 65 rows, exact
errors, hashes and comparisons; bounded previews alone are insufficient.
Use the scoped JSON inspector for selected full values and compare them
with an independent mathematical check of what the script encloses.

Accept only if the residue has the claimed full rate without assuming
chi(b)>0; the exact saddle identity and legal segment imply the stated
phase loss; the entire rational certificate represents the actual two
integrals; and the signed sum preserves only the claimed limsup and ratio
limsup. Zero subsequences must remain allowed. If an essential inference
fails, record it canonically and stop that comparison; do not repair it by
changing the bump, assuming an endpoint law or promoting a preview to a
proof. No source blocker remains for this bounded test, but this assessment
does not predict its verdict. A newly ready covered audit receives separate
continuation approval next turn. The essential audit takes priority over
creative discovery; no independently prepared central mechanism was found
within this narrowly scoped source task.
