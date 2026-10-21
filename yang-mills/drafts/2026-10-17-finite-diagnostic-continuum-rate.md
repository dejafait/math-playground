# Quantitative diagnostic comparison — working record

STEP_ID: YM-20261017-282-finite-diagnostic-continuum-rate

The approved target is exactly the TARGET in
`drafts/literature/2026-10-17-finite-diagnostic-continuum-rate.md`
(SPECIALIZE, available before this invocation). Main gap: quantitative
cutoff control of the complete Ward response, followed by interacting
matching and construction, remains open. This step only tests
|D_(i,a)-D_i| <= C_i/N for i=3,6. Downstream, this could combine with
audited L221 to compare its selected trace to 2 gamma D_i; independent
component rates, L220's audit, interacting reflected error <=c_box/2,
continuum axioms and finite positive infrared mass remain unresolved.

Duplicate/failure check: the supplied assessment and narrowly read
L080, original diagnostic working/history records, L070 section 6,
L008 sections 1,2,4, L026 through (9), and ATTEMPTS/024–025 identify
qualitative convergence only. The stopped bulk-profile replacement and
axial-profile absolute-norm gain are not used. The exact upper curvature,
physical distance and full lower-rooted prefix, including axial zero,
stay in the diagnostic. Existing work is preserved.

Unfinished reasoning saved before proof writing: for r=|k|>=sqrt(3),
lambda_(k,a)>=r^2/16 and |lambda_(k,a)-lambda_k|<=C a^2 r^4.
Normalized smooth extensions have C^m norm <=C_m r^(m-1), and their
normalization discrepancy is <=C_m a^2 r^(m+1). First-order Taylor
bounds for actual plaquette/edge offsets, a uniform length-at-most-8
midpoint-prefix estimate, and compact-supported rectangle quadrature
should give |B_(i,a;kl)-B_(i;kl)| and |P_(kl,a)-P_(kl)|
<=C_i a (1+|k|+|l|)^4. The heat-exponent difference should be bounded
by C a^2(r^4+t^4) exp[-tau(r^2+t^2)/16]. Labels absent from the mesh
must be counted separately. No rate is established by this note alone.

Continuation/abandonment test: complete all retained-factor bounds with
one polynomial mode envelope and sum it against the full heat spectrum.
If a boundary, prefix or form term fails that test, retain that exact
uncontrolled term rather than claim the rate. Essential inputs are
L008 L026 L070 L080; L221 is downstream only. No cross-notebook input,
new source search or mathematical script is required.

Completed attempt: L222 proves the requested C_i/N bound for both
probes. Its canonical proof provides quantitative dispersion and mode
normalization bounds, both complete polarized probe-form comparisons,
the positive upper-row estimate, the full midpoint-prefix estimate,
compact spatial quadrature, a summable retained-pair error envelope,
and a separate omitted-label bound. No independent upstream audit or
numerical assertion is used. The continuation is separate critical
audit of L222 after the new REVIEW_REQUIRED coverage gate. Independent
gaps and the downstream-only role of L221 above remain unchanged.
