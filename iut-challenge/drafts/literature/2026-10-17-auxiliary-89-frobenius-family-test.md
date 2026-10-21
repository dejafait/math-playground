# Auxiliary p=89 family test — prepared specialization scope

TARGET: Test whether the p=89 translated y^2=x^3+1 reduction refines L046/L048's fixed-c family to realize L072's joint scalar while retaining local 210-torsion, v_3(q_aux)=30 and global mod-7 surjectivity.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step284's completed targeted review in 2026-10-17-auxiliary-frobenius-joint-scalar-review.md; its inspected primary sources cover good-reduction transport, the actual Frobenius polynomial and the fixed-level exceptional bound. No scalar or family certificate has been computed.
SOURCE_EVIDENCE: Milne (2021), https://www.jmilne.org/math/Books/EC2.pdf, II.6 Corollary 6.2 pp.70–71, IV.9 Theorem 9.4/proof p.150, V.7 Proposition 7.5/(46) p.217 and V.8 Propositions 8.1/8.3 pp.220–221; Zywina author version, https://pi.math.cornell.edu/~zywina/papers/MaximalGalois.pdf, section 1.1 pp.1–2, Definition 5.1 p.6 and Proposition 5.7/proof p.8. Direct URLs retrieved again in step285; unchanged prior assessments supply remaining proof/sieve/coordinate coverage.
COMPARISON: Only the explicit finite-field, congruence, fixing-field and two-parameter count specialization remains. No new general theorem, generic-image assertion or source reproof is required. Exact finite point counting avoids reliance on unread supersingular-classification leads.
GAP: Nonsingularity/trace, one actual joint scalar lift in G_(K_aux), nonempty full-rank auxiliary family and preservation of the original local/geometric/mod-7 requirements are unproved. No property of the already selected E_0 is thereby decided.
REASON: Primary coverage is adequate for this bounded known-method test; step285 separately approves the unchanged scope after direct-URL repair. No proposed scalar or family calculation has been performed.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in this ready assessment; step285 repairs that omission and verifies access without expanding the target or repeating blocked Galbraith retrievals.
SCOPE: Exactly TARGET, fixed c and fixed M>=max(M_tors,31), prospective E_aux with new K_aux,F_aux and induced places. No replacement of retained E_0,F,K_glob or unproved transfer of every later lemma is authorized.

## Concrete test and required evidence

Use the proposed reduction y^2=(x+c/3)^3+1 over F_89, with c
L046's fixed integer and finite-field division by 3. Verify its
discriminant and exact rational point count. Either an exhaustive
finite certificate or a fully justified elementary bijection suffices;
no general supersingular classification is needed. No p=89 value has
been verified in this literature turn.

Apply the inspected Frobenius identity on the prime-to-89 torsion,
checking one arithmetic lift's power on the entire E_aux[120]. Prove
that this power acts as -Id modulo 8 and Id modulo 15, and fixes
both zeta_60 and E_aux[2]. Show that it belongs to the actual
G_(K_aux), K_aux=Q(zeta_60,E_aux[2]), rather than constructing
an abstract CRT matrix or separate lifts. Trace/determinant may
identify the polynomial; the polynomial identity must justify the
scalar power. Arithmetic versus geometric Frobenius must be explicit.

Impose the reduction on L046's original fixed-c family via compatible
coefficient congruences, retain the original 3^M precision and monic
model, and exhibit the refined affine lattice after L046's pointed
Q-coordinate map. Prove a positive quadratic leading box count and
compare it with the imported O(R^(3/2) log R) exceptional bound at
fixed moduli. A bare density assertion or a one-parameter subfamily
is insufficient. Import all general source results without reproof;
the explicit family verification is why this is SPECIALIZE.

Reapply only the needed L044/L045/L046/L048 conclusions to the new
witness: full local 210-torsion, full coordinate kernels and embedded
H,N, split Tate reduction with v_3(q_aux)=30, and the required
mod-7 image. Old and new global division fields, places and Tate
parameters need not coincide. L071/L072 describe a possible later
application to the new witness; the retained curve's radical
memberships remain unknown throughout this proposed test.

Continue only if the exact reduction, actual joint fixing element and
positive-count preservation checks all pass. If any fails, record the
specific failure and abandon this condition. An achieved family
witness would address occurrence for that family only; native T/model,
exact generation, independent initial data, source-marked factorization,
pilot transport, essentiality and finite B>=A would remain unresolved.

Essential input IDs: L044,L045,L046,L048,L071,L072. Preserve the
retained E_0,F,K_glob,Omega,embedding,u,w,H,N and q_0 and the stops
in ATTEMPTS/027,028,031,032. The proposed research classification is
REPRODUCTION. Mathlib coverage is unchecked. This is a new ready
source scope for separate approval, not a proved lemma or a candidate
IUT resolution.

## Step285 direct-source approval — 2026-10-17

Both direct primary PDFs above were retrieved successfully. This separate
literature approval retains the exact TARGET and SPECIALIZE scope. It
does not certify any proposed finite-field or family calculation.

Rechecked Milne II.6 Corollary 6.2 and its proof (printed p.70), and
V.8 Propositions 8.1/8.3 with their reduction arguments (pp.220–221).
The hypotheses are an elliptic curve over Q, good reduction at p and
Tate prime different from p; the Frobenius convention is the residue
p-power automorphism. Proposition 8.3 compares its Tate-module action
with reduction. The finite-level test must retain all prime-power
parts and one actual lift. Corollary 6.2 supplies an endomorphism
identity, rather than a scalar conclusion from trace alone. Remaining
source coverage is reused from the completed step284 review, including
the determinant and finite-field point-count passages; no p=89 count
or scalar power was evaluated here.

Rechecked Zywina Definition 5.1 (printed p.6), Proposition 5.7 and
its full proof (p.8), and the first assertion in Lemma 2.4's proof
(p.5). These concern nonsingular integral short models, fixed level
and fixed norm over a number field; k=Q is allowed. The exceptional
condition is failure to contain SL_2. The Q-case full-image criterion
is explicit. The bound applies to the whole coefficient box and does
not assert positive density in this proposed congruence family. Its
refined positive leading count remains an applicability obligation,
with all congruence moduli fixed. Deeper sieve and coordinate coverage
is reused from `2026-10-11-mod7-surjective-local-approximation.md`.

Duplicate/failure comparison remains the one in the completed step284
review: L046 handles only the unrefined family, L072 remains conditional,
and ATTEMPTS/027,028,031,032 are not reopened. No essential unread
classification result is needed for the exact finite count. This is
a source-access/metadata repair, with no mathematical advance, new
lemma, script or changed argument. Mathlib coverage remains unchecked.
