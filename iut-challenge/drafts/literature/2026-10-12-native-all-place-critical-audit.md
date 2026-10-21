# All-place pointed reduction — critical-audit source coverage

TARGET: Critically audit L051's all-place multiplicative reduction and stable one-pointed cubic for the unchanged curve.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read full L051, scoped L045/L048 hypotheses and conclusions, the ready all-place/native-predicate assessments, histories/168–169 and ATTEMPTS/028; targeted relative Cartier-duality and ampleness queries located the primary Stacks statements and proof cases below. No duplicate completed L051 audit was found in those scoped records.
SOURCE_EVIDENCE: Stacks live tags retrieved 2026-10-12: 48.14.1–2 (0B4A/0AA4), 48.9.7 (0A9X), 48.15.1 (0A9W), 48.16.3 (0ATX), section 109.19 (0E6N), 109.19.3 (0E6R), 30.8.1 (01XT), 29.38.2/28.27.2 (01VG/01PT); reuse Milne ANT v3.08, Kedlaya Tate Theorems 1–2, Hassett math/0205009v1 section 2 and the qualified May 2020 native predicate.
COMPARISON: The inspected Cartier formula permits a nonsmooth divisor, projective-space duality is relative over the base ring, and the curve-family convention identifies the relative sheaf in degree -1. These sources cover L051's existing mechanism; its actual flat Cartier cubic, fibers, marking and divisor identity remain separate audit obligations.
GAP: Source coverage is ready for exactly TARGET; the critical mathematical audit and insertion of precise citations into canonical L051 remain separate research work. No audited verdict or full native initial data is established here.
REASON: SPECIALIZE these known results to review the existing proof, importing general duality rather than reproving it. No changed curve, field or new reduction theorem is needed.
LITERATURE_REASON: L051's new audit had essential unread source coverage for relative hypersurface duality with a possibly singular total space; unchanged completion, Tate and pointed-stability coverage is reused without fresh browsing.
SCOPE: Exactly TARGET, with the unchanged E_0,F,Omega,u,H,N and M; no new curve, field, action, covering or numerical theorem.

The main gap remains original finite B>=A. The intermediate audit tests
whether the single native reduction prerequisite above 3 has actually
been closed. Its downstream use is reliable reuse of this arithmetic
prerequisite, while preserving all independent initial-data and
comparison gaps. Source assessment is now complete; the mathematical
audit has not been performed in this literature-only turn.

Essential inputs: L051 with L045,L048; L044–L047,L042 are retained
through those inputs. L049 is background only and L050 is contrast
only. Keep F=Q(zeta_60,E_0[30]), F_u=H, D_w=N,
M>=max(M_tors,31), v_3(3)=1 and v_3(q_0)=30, without
q_0=3^30. Every t ranges over actual F-places above 3. The
native definition retains its May 2020 reproduced-source qualification.

The discriminating audit must check all load-bearing statements:
transport fixes coefficients and origin; the projective charts are
flat; the special cubic is geometrically integral with its only
singularity a split node; its arithmetic genus is one; the section
is smooth and Cartier; hypersurface adjunction applies despite any
total-space singularities; and the infinity divisor equals 3S over
the entire DVR, making omega(S) relatively ample. It must also
check that the native verdict is conditional on this moduli place's
selection and is no assertion of full stable log or covering data.

Continue with the audit under the approved coverage for these exact inputs;
if an essential hypothesis is unavailable, repair or restrict this
specific proof instead of reopening the additive-descent objection.
K-coricity, covering/cusp/selected-place data, actual input/action,
pilot, essentiality and finite B>=A remain unresolved. Preserve
ATTEMPTS/022,025,026,027,028. Full matching Mathlib coverage remains
unchecked. No mathematical audit was carried out in this literature step.

## Completed source comparison — 2026-10-12

### Relative-duality hypotheses and inspected proof cases

These are live primary Stacks tag versions retrieved on 2026-10-12,
not a claimed pinned repository revision. Complete theorem statements
were inspected before the essential proof cases.

[Section 48.14, Lemmas 48.14.1–2](https://stacks.math.columbia.edu/tag/0B4A)
and [Lemma 48.14.2](https://stacks.math.columbia.edu/tag/0AA4)
assume an effective Cartier immersion i:D -> X with normal sheaf
N=i^*O_X(D). For K in D(O_X), the formula is
RHom(O_D,K)=Li^*K tensor^L N[-1]. The complete two-term-resolution
proofs were read: the invertible ideal resolves O_D and the normal
sheaf is the cokernel in degree one. Neither X nor D must be smooth
or regular. This covers the kind of adjunction used in L051.

[Lemma 48.9.7](https://stacks.math.columbia.edu/tag/0A9X)
assumes a quasi-compact quasi-separated ambient scheme, a
pseudo-coherent closed immersion and K in D_QCoh^+. It identifies
the right adjoint of Ri_* with this derived sheaf Hom; on a
noetherian ambient scheme every closed immersion is pseudo-coherent.
Its complete uniqueness-of-adjoints proof was read. The audit must
state these qualifications for the actual projective ambient scheme.

[Lemma 48.15.1](https://stacks.math.columbia.edu/tag/0A9W)
assumes a quasi-compact quasi-separated base Y and a locally free
rank n+1 module E. The projection of P(E) has right adjoint at
O_Y equal to f^*(det E)(-n-1)[n]; for trivial E it is
O(-n-1)[n]. The entire proof, including affine-base reduction and
the generating twists, was read. It is relative over the base ring,
not merely a projective-space formula over a field.

[Lemma 48.16.3](https://stacks.math.columbia.edu/tag/0ATX)
assumes composable separated finite-type morphisms over a fixed
noetherian base and gives (g composed with f)^!=f^!g^!.
The proper-morphism/right-adjoint case at the start of its proof
was inspected; later compactification-independence diagrams are
unnecessary for the proposed proper cubic/projection application.
The section 48.16 construction and complete
[Remark 48.17.5](https://stacks.math.columbia.edu/tag/0BV2)
were also read. Its local description is supporting coverage, not
a substitute for gluing the global sheaf in L051.

[Section 109.19](https://stacks.math.columbia.edu/tag/0E6N),
Lemma 109.19.1 and Definition 109.19.2, identifies the relative
dualizing sheaf of a curve family with Cohen–Macaulay,
equidimensional one-dimensional fibers as H^(-1) of the relative
dualizing complex. In the noetherian schemes setting the discussion
identifies that complex with f^!O_S. Its full reduction proof and
[Lemma 109.19.3](https://stacks.math.columbia.edu/tag/0E6R)
were read; Gorenstein fibers give an invertible sheaf compatible with
arbitrary base change. These are family/fiber hypotheses, without
a regular-total-space requirement. Supporting Lemma 48.23.3
(0C0Z) was read but is not needed as an extra independent input.

The audit must distinguish degree-one Ext on the ambient surface
from degree-minus-one cohomology of the relative curve complex.
It must verify noetherian base, proper finite presentation, flatness,
Cartier equation and fiber dimensions before applying these sources.
This comparison covers L051's already written cancellation of the
cubic twist against O(-3); it does not derive a new formula here.

### Genus and ampleness inputs

[Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XT)
gives all twists' projective-space cohomology over an arbitrary ring.
The statement and complete Cech proof were read: all-negative,
nonnegative and mixed-weight cases, including the contracting
homotopy. It supplies a precise supporting citation for L051's
cubic-sequence arithmetic-genus check. Normalization genus is a
different quantity from the singular fiber's arithmetic genus.

[Lemma 29.38.2](https://stacks.math.columbia.edu/tag/01VG)
states that an invertible sheaf is f-ample exactly when any specified
positive tensor power is f-ample. Its cited
[Lemma 28.27.2](https://stacks.math.columbia.edu/tag/01PT)
and complete proof were read. They cover the tensor-power inference;
the audit must still check that the marking is Cartier and that Z's
divisor is exactly 3S over the whole DVR, not just equal supports
on a fiber. This review proves no new divisor identity.

### Reused coverage, stops and scope

The unchanged all-place application assessment supplies inspected
Milne ANT v3.08 Theorem 3.34's Galois proof and completion statements,
Kedlaya's finite-p-adic-field Tate criterion, and Hassett's noetherian-base
weight-one pointed-family definition. The native-predicate assessment
retains its May 2020 reproduced-source qualification: author-hosted
PDF byte identity remains unverified. No new native theorem is imported.

Scoped duplicate checking distinguishes L051's application from its
unperformed audit. L050 and ATTEMPTS/028 concern an additive descent
over Q_3 under a different exposition quantifier. The regular I_n
polygon objection distinguishes models; it supplies no objection to
Cartier duality. Neither route is reopened by this source review.

Queries included `site.stacks.math.columbia.edu relative dualizing
effective Cartier divisor Gorenstein adjunction`, `dualizing sheaf
relative hypersurface projective space`, `smooth upper shriek wedge
differentials 48.17`, and `ample invertible sheaf power ample`.
Search excerpts and the exercises page 111.50 were leads only;
the latter is not an Euler-sequence input. Direct projective-space
duality made that lead unnecessary. No novelty is inferred.

SPECIALIZE approves exactly TARGET for a separate known-method
critical audit. Allowed repairs are genuine errors or missing precise
citations in the existing proof with L051,L045,L048 and the unchanged
arithmetic choices. The audit must retain the conditional selected-place
verdict and independent gaps. General duality, Tate and completion
theorems need citation, not reproof; explicit chart/divisor checks are
necessary because a general existence theorem would not verify this
specified model. Full matching Mathlib coverage remains unchecked.
