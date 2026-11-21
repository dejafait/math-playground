# Nominated conceptual audit of the uniform resolvent ratio

TARGET: Critically audit L716's uniform resolvent-ratio limit on the original closed bump interval, including the exact moment certificate, whole-tail domination and nonvanishing.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 182 reused the exact-target and obstruction searches in the step-180 ratio assessment and polynomial assessments; read L716, relevant L715 statements, step-180/181 histories and three preserved failures. New targeted DLMF searches located and inspected the local inversion and Cauchy derivative theorems; no new search for the unchanged quotient is claimed.
SOURCE_EVIDENCE: Reuse step-180 primary evidence (JKM v1 Theorem 2.2; DLMF 2.3/2.4; Temme Section 2.1; Nemes v2 Conditions 1.1/Theorem 1.1 and Section 2 distant-tail case), plus audited L715. Newly inspected NIST DLMF 1.10(vii), equations 1.10.12--14, and 1.9(iii), equations 1.9.30--31, online text retrieved 2026-11-03. Details and limits below.
COMPARISON: JKM supplies the polynomial logarithm and reciprocal-root law only; classical local inversion and Cauchy formulas cover the named analytic tools. Neither these nor the fixed-phase Laplace results certify the new finite certificate or growing-array whole-tail bound. Those are precisely the local claims for independent audit, not missing source hypotheses.
GAP: Audit the sign and normalization of the inverse identification, implemented moments and all exact rounding/Taylor/mesh bounds, compact derivative convergence, unbounded root tail, one uniform onset and nonvanishing. Adequate tool coverage is available; no correctness verdict for L716 is made here.
REASON: Separate source/scope comparison is complete for exactly the saved conceptual audit. EXPLORE authorizes that audit of the family-specific argument without claiming a matching general quotient theorem or originality.

LITERATURE_REASON: Required separate approval of the newly nominated L716 audit; its moment inversion and whole-tail argument were outside the earlier polynomial-only audit. Reuse adequate ratio coverage and inspect only the additional standard tools, without repeating the mathematical attempt.
SCOPE: Exactly TARGET for unchanged L714 coefficients, audited L715 and the original closed interval; approve scrutiny of L716 and its complete exact certificate, not L714 (2), signed bump rates, boundary laws or Xi transfer.

## Exact scope and reused inputs

Keep L714's coefficients and audited root argument; audited L715's
unique F and reciprocal-root probability measure; n=12q+3, U=121/64,
A=27/10, alpha=11/8, u=(3+4i)/10 and the original fixed interval
[omega-delta,omega+delta], 0<delta<1/3000. No width or endpoint is
changed. L714's inversion formula is not an input to L716 and is
not certified by this audit nomination.

The new proof asserts a limit 1/[alpha+u*z_v*F'(z_v)], lower modulus
8/47, and an existential eventual onset. Its critical claim is a
uniform integrable majorant for the entire real Laplace parameter,
derived from G(x)<4/3 for every x>=2/5. Check especially the sign
and normalization in y=-z*F', the coefficient-residue specialization,
the exact c_k recurrence, interval rounding and Taylor remainders,
all 401 cells with both series and mesh errors, the unbounded x tail,
and passage from the limiting bound to one onset uniform in v.

The original ratio assessment already inspected general Watson and
Laplace theorems and found no automatically applicable quotient
theorem. L716 uses its own array bound, not their missing hypotheses.
Its coefficient formula includes a local Cauchy-residue derivation
of the Lagrange--Bürmann specialization to make the implementation
checkable. Reuse adequate source coverage; determine in the separate
review whether any essential theorem hypothesis remains unread.
This nomination neither performs that review nor claims novelty.

The exact certificate is under scripts/one-sided-hankel/; the
separate Decimal ratio diagnostic is nonrigorous and unused in the
proof. Acceptance requires the uniform quotient limit and positive
minimum modulus with all tails paid, or a specific correction or
failed inference. Do not conflate a script replay with a proof audit.

Outer signed bump integration, other response terms, angular
persistence, complementary spatial Jensen defect, amplitude/full
charge, H/support, Xi realization and all-degree positivity remain
unresolved. An independent audit of the new load-bearing tail argument
takes priority over inventing a creative target to satisfy scheduling.

## Separate coverage review — step 182, 3 November 2026

The preceding nomination is retained as the pre-review record. This
section discharges its source gate; it does not perform the audit.
Read the complete step-180 ratio assessment, the step-178 polynomial
audit assessment, the step-176 source header and step-180/181 histories.
The primary hypotheses and essential far-tail proof case recorded in
step 180 remain adequate and are reused without reopening those sources.
Read L716 in full to delimit its claimed tools and L715's statement and
source-import section. The new exact script's first 100 lines were read
only to identify its rational/interval implementation and source needs;
no script was run, certificate verified or implementation approved.

Queries were `site.dlmf.nist.gov "Lagrange" "1.10"` and
`site.dlmf.nist.gov analytic functions uniform convergence derivatives Cauchy`.
Search results were leads, not evidence. Inspected the following named
standard theorems in the NIST reference text:

- [DLMF 1.10(vii)](https://dlmf.nist.gov/1.10.vii), equations
  (1.10.12)--(1.10.14): an analytic map at its base point with nonzero
  derivative has a unique local analytic inverse. The inverse's nth
  coefficient is 1/n times the stated residue of the reciprocal nth
  power of the shifted map; the analytic-composition version includes
  the derivative of the composing function. This is local, with no
  assertion about a global inverse or the unit-circle boundary.
- [DLMF 1.9(iii)](https://dlmf.nist.gov/1.9.iii), equations
  (1.9.30)--(1.9.31): Cauchy's function and derivative integral formulas
  require analyticity inside a simple closed contour and continuity
  on it, with the evaluation point inside. This is the relevant tool
  for L716's claimed derivative convergence on smaller compact disks;
  the contour separation and analytic hypotheses remain to be audited.

For source comparison, L716 names the map w/phi(w), its base point
zero and its claimed nonzero derivative. Its proposed moment formula
is a local residue specialization of the inspected inversion theorem.
Checking the map, sign, coefficient recurrence and contour calculation
is still mathematical audit work. The short local derivation has a
stated implementation purpose: certify precisely the coefficients fed
to the interval program. A reproof of the general inversion theorem
or JKM is unnecessary. The new source tools do not establish any of
the family-specific inequalities. No new formula is derived here.

The fixed-phase endpoint results already compared in step 180 do not
supply uniform domination for an n-dependent normalized polynomial.
L716 instead claims a compact limiting bound plus a separate finite-n
root bound on the remaining unbounded path. That distinction makes the
proposed audit independently testable without seeking a stronger
asymptotic theorem: verify every premise and quantifier of this exact
argument, rather than importing a theorem whose hypotheses are unpaid.
No essential external source remains unread for that audit. The two
unread step-180 leads remain unused and nonessential.

Read the three preserved failure records for the signed bump rate,
absolute horizontal contour and positive blend named in step 180.
The first exposes the resolvent/outer-integration gap; the others stop
different certificates or weights. None decides L716. The step-181
history records an audit nomination, not an already completed audit;
no duplicate independent verdict was located in the scoped records.
Full matching Mathlib coverage and supporting theorem names remain
not checked; no absence or formal-verification claim is made.

Proceed next with exactly TARGET. Acceptance requires the complete
uniform relative limit and positive minimum modulus on the unchanged
closed interval, with the full certificate and analytic tail paid.
Otherwise record a specific defect and repair or reject that inference;
finite ratio samples or replay alone are insufficient. Independent
outer cancellation, L714 (2), complementary defect, amplitude/full
charge, H/support, angular persistence and Xi realization stay open.
This review is EXPLORATION/NOVELTY_UNCHECKED: it supplies ready coverage,
not new mathematics or an independent confirmation of L716.
