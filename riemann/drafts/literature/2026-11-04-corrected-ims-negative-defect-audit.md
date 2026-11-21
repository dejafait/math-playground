# Independent audit scope for the fixed negative corrected defect

TARGET: Audit L750's exact-neutral negative two-window defect certificate, including its signed identity, interval arithmetic, interpolation/Fourier/image bounds and every arithmetic delay.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step314 exact-target/obstruction searches; step316 searched site.nist.gov DLMF composite Simpson rule error fourth derivative 180 and inspected https://dlmf.nist.gov/3.5#ii for the previously unnamed quadrature input; no new discovery claim.
SOURCE_EVIDENCE: L744(6),(8) and L749 remain local normalization inputs; inspected NIST DLMF https://dlmf.nist.gov/5.9.E16, https://dlmf.nist.gov/5.5.E2, https://dlmf.nist.gov/5.11.E2 with https://dlmf.nist.gov/5.11#ii, and composite Simpson https://dlmf.nist.gov/3.5.E7 and https://dlmf.nist.gov/3.5.E8 on 2026-11-04; L750/certificates remain unaudited.
COMPARISON: The sources cover the full energy identity and elementary analytic estimates; they do not sign this exact defect. The independent task is to verify the exact specialization and finite certificate, including both corrected first-pass issues, rather than import a universal IMS sign or reproduce the source theorems.
GAP: Independent validation of L750's negative certificate, its exact moment definitions, interval implementation, all-frequency and interpolation controls, and complete delay enumeration remains; no RH or full-class positivity conclusion is in scope.
REASON: The source assumptions and nominated data are unchanged, so existing coverage is adequate for this narrower conceptual verification. This newly written continuation awaits the supervisor's separate approval next turn; no audit is claimed in step315.
SCOPE: Only the existing L750 witness, T=8log3, ell=6log3, nominated partition/bumps, full L744 energy and recorded certificate. No replacement vector, enlarged trial space, new propagation rule or RH-dependent input.
COVERED_TARGET: Audit L750's exact-neutral negative two-window defect certificate, including its signed identity, interval arithmetic, interpolation/Fourier/image bounds and every arithmetic delay.

## Reused evidence and intended critical review

The primary comparison in
[the existing assessment](2026-11-04-neutral-corrected-ims-defect.md)
read the applicable DLMF integral representation and the full hypotheses
of the fractional IMS and logarithmic-Laplacian comparisons. L744's
smooth identity and global symbol majorant have a separate local audit;
L749's cutoff/derivative argument also has a separate local audit. Those
facts are used within the same scope. No new literature browsing was
performed or needed during the covered step315 construction.

The result to inspect is
[L750](../../lemmas/L750-exact-neutral-two-window-localization-defect-counterexample.md).
Its output is a negative localization defect, while the three individual
complete energies are positive. An audit must not interpret it as a
negative Weil vector or global rejection of spatial propagation.

Check the two moment inverses and reflected correction before the
pole cancellation. Verify that the auxiliary linear interpolants are
not silently assigned exact neutrality. Check the signed identity,
real-line/periodic image comparison, linear-hat autocorrelation,
Nyquist convention, entire Fourier tail and interpolation energy norm.
Replay the interval program and the constant checks; scrutinize the
outward elementary functions and hypotheses of Simpson's bound.
The invalid first pass used 270 where the sufficient eta derivative
bound is 280 and is retained as invalid. A separate constant-check
first pass straddled the exact integer 352; its final check is exact
integer arithmetic. Neither failed output is supporting evidence.

Full matching Mathlib coverage remains not checked. A successful audit
would be REPRODUCTION/local verification, not a new discovery or
originality certification. It would certify only failure of the literal
rule. A materially different next mechanism needs its own source gate;
automatic enlargement or repeating this completed sign test is excluded.

The intended routing after separate approval is proof_audit /
conceptual_audit, deep_research/xhigh: periodic/full-line normalization
and machine-enclosure obligations are delicate analytic issues, beyond
a routine numerical replay.

## Direct-source recovery, step316

This literature-only recovery repairs the missing direct URLs. It does
not replay or validate L750. The exact TARGET and SPECIALIZE scope are
unchanged; the next invocation is its mathematical conceptual audit.
LITERATURE_REASON: Supervisor required direct source URLs in the ready
assessment; the composite Simpson input also lacked a precise source
identifier. No new sign-search or theorem-discovery round is needed.

Read the live NIST DLMF statements on 4 November 2026 (unversioned live
URLs, not a newly checked release number):

- [5.9.16](https://dlmf.nist.gov/5.9.E16), including the preceding
  Re(z)>0 condition in Section 5.9(ii), gives psi(z)+gamma as the
  convergent difference integral. L750's z=1/4+it/2 lies in this domain;
  exchanging that scalar integral with the Fourier integral remains a
  local proof obligation, not part of the cited formula.
- [5.5.2](https://dlmf.nist.gov/5.5.E2) gives the digamma recurrence;
  it is applied away from poles. [5.11.2](https://dlmf.nist.gov/5.11.E2)
  uses the principal logarithm and the sector |arg z|<=pi-epsilon.
  The first paragraph of [5.11(ii)](https://dlmf.nist.gov/5.11#ii)
  bounds the complex digamma remainder by the first omitted term in
  modulus times sec(arg(z)/2)^(2n+1), for truncation at k=n-1.
  The positive-real sign statement must not be applied to complex z.
  The audit must check the actual shift, truncation and constants.
- [3.5(ii), (3.5.6)-(3.5.8)](https://dlmf.nist.gov/3.5#ii) assumes
  a real C^4 integrand on [a,b]. Its composite rule uses even n,
  h=(b-a)/n, and error -(b-a)h^4 f^(4)(xi)/180. This precisely
  covers the type of real moment integrals claimed in L750, conditional
  on its derivative bounds. Check that its word “panels” means the
  subinterval count in this formula, and that interval nodes include
  uncertainty in endpoints/parameters. DLMF cites Davis and Rabinowitz
  (1984), pp.57-58; that book was not independently read here.

The elementary error theorem supplies no outward arithmetic, exact
moment inverse, FFT normalization, image sum, Fourier tail or complete
prime-power enumeration guarantee. Those remain the independent audit's
load-bearing work, including the two retained failed first passes.
Existing overlap searches and route stops are reused from step314;
none establishes a negative Weil vector or a general propagation ban.
No source reproof is justified. Full matching Mathlib coverage remains
not checked. Source coverage is ready for the unchanged fixed audit;
accept only a strict negative full defect with every error justified,
otherwise repair/retract the affected claim within the same witness.
