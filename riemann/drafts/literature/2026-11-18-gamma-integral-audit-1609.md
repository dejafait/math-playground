# Gamma-integral conceptual audit1609

TARGET: Critically audit C033a's combined-integrand Fubini bound, complex-test Fourier scaling, origin value and uniform v>16 gamma-tail bound for real sigma in[1,2] and complex |w|<=2, retaining C032z's qualifications.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged exact-digamma assessment1608 and its source-notes1608 searches, duplicate checks and scoped comparison with stops1576/1581/1586. No new search or novelty claim; this is a critical audit of precisely that specialization, with no changed parameter domain or new mechanism.
SOURCE_EVIDENCE: NIST DLMF Section5.9(ii), equation5.9.16 https://dlmf.nist.gov/5.9.E16 with Re(z)>0; version1.2.8 as recorded in1608. C032z equations(2)-(4)/(10) and audit1585 supply the ordinary transform, zero mean and uniform bounds. The primary domain/formula was checked again solely for its application in1609. Existing named Fubini/Tonelli coverage applies only after product absolute integrability is established.
COMPARISON: C033a derives an ordinary Fourier-variable gamma integral and the bound4*exp(-128)<1/16 at cutoff16. This is a local specialization of known digamma/Fourier tools, not a new general archimedean formula or a refutation of the literal separate-error cost stop1586. Audit the proof rather than reproduce the sources.
GAP: Independently verify the combined-integrand L1 argument, all complex-test signs and scaling factors, the continuous origin value and the uniform fixed tail inequality. The present derivation has not yet received that separate critical audit; finite quadrature, O, coefficient amplification and the actual residual remain open.
REASON: The noncompact exchange is load-bearing for using this new gamma component in dictionary1570. An audit can validate it or isolate a repair before any expensive evaluator work. Existing coverage is sufficient for this exact check; no new theorem or enlarged domain is being approved.
SCOPE: Exactly C033a and its direct mathematical input C032z, real sigma in[1,2], complex |w|<=2 and cutoff16. Retain all actual-divisor/multiplicity/zero-ordinate/strip/counting qualifications on spectral use, and finite-zero/heat/fixed-v1 qualifications on probability use.

This newly written ready continuation requires separate supervisor
approval on the next invocation. It does not self-audit C033a or
retroactively approve uncovered mathematics. The completed1609 step
used the already approved assessment1608 and remains REPRODUCTION.
No new proof or mathematical script is part of this assessment.

Check the absolute r,t integral before cancelling the zero-frequency
term: in particular the split at |r|=2/t must not assume that an
absolute first moment of h exists. Check that taking the real part
precedes multiplying by complex h, and that the Fourier convention
matches C032z. Verify the ordinary endpoint extension and the tail
on the full closed parameter set, including w=0 and sigma=1,2.
The canonical statement and complete derivation are in
`lemmas/C033a-zero-mean-gamma-integral-and-fixed-fourier-tail.md`;
do not treat this paragraph as a substitute proof.

Pass only if the identity, endpoint and strict tail comparison all
hold with their exact factors and uniformity. If a failure appears,
preserve it and repair only within this assessed scope; new hypotheses,
cutoffs or independent claims require another assessment. No compact
quadrature, optimizer, new dictionary or claim of full-E accuracy is
included. Source lookup alone is not the audit.

An essential conceptual audit takes priority over creative nomination
here. This step has produced no independent signed-theta upper term
or all-degree mechanism; those missing inputs remain the recorded
blocker, and the old central discovery stops are not reopened. Full
matching Mathlib coverage remains unchecked and unknown.

## Separate source-scope approval1610 — 18 November2026

The separate literature-only invocation approves this unchanged TARGET
and SPECIALIZE scope for the next research turn. This supersedes the
prospective approval wording above; it does not certify C033a's proof.
No essential source coverage is missing for this exact audit.

Reused assessment1608 and source-notes1608, including their exact-query,
duplicate and failure comparisons; read C033a to identify the obligations,
and C032z's hypotheses, equations(2)-(5), ordinary Fourier proof and
critical audit1585 passages. The origin expansion, inverse-square bound,
complex-test convention and zero mean are documented inputs to audit,
not newly established results of this approval. Stop1586 still concerns
separate literal-series allowances; neither its cost ceiling nor the
parked direct contour mechanism is reopened. No broader novelty search
is warranted for a critical check of this known-tool specialization.

Primary source inspected again: NIST DLMF Section5.9(ii), the Re(z)>0
restriction preceding5.9.12 and the full equation5.9.16 (both integral
forms), https://dlmf.nist.gov/5.9.E16, accessed18 November2026. The
existing notes record version1.2.8; this lookup verifies the displayed
formula and domain, not an independently archived version identifier.
The needed substitution is exactly z=1/4+i*r/2, real r. The source gives
a pointwise digamma identity, not absolute product integrability or
permission to split endpoint terms. Named Fubini/Tonelli coverage can
therefore be reused only after the audit verifies that hypothesis.
Connes's smooth Mellin-test formula is comparison evidence already
reviewed in1608, not an input to this audit; it was not reread here.

The bounded test remains the four saved obligations: combined product
absolute integrability before cancellation; complex h and Fourier
normalization; uniform continuous origin extension; and the claimed
cutoff16 tail on the full closed parameter set. Do not report this
source approval as a pass of any of those proof checks. A failure must
be isolated with the original cutoff and domain retained. The full
matching Mathlib result remains unknown. No lemmas or mathematical
scripts were changed, and no new derivation was performed.

Outcome STALLED: this is a required approval and source-scope confirmation,
not new mathematical evidence or a changed literature conclusion.
The next turn is the already specified conceptual audit, with no further
literature gate needed while this exact scope and inputs are unchanged.
