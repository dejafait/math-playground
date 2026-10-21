# Equality local duality and point defects — source scope ready

TARGET: Determine the exact local duality sequence relating the higher-image and reflexive-hull defects in L108's (14,21) equality family.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched relative perfect duality, contravariant hyper-Ext, regular-local finite-length duality and self-dual complexes with reflexive-hull defects; compared corrected L108, its prior audit coverage, immediate working notes, history/304 and ATTEMPTS/066. Exact queries and inspected sources are recorded below.
SOURCE_EVIDENCE: Inspected Stacks 0B6S, 0BRT (48.15.7, including diagonal proof), 0G81, 0A9Q and the first perfect-duality calculation in 0E4L; 07AA/07A9 with its double-complex construction and 012X 12.25.1--3; 00O7; 0A7Q including its noncomplete-ring qualification, 0AWX, 08Z9 and the regular-local formula in 57.11.2 (0G23). Reuse the prior assessment's perfect-pushforward and reflexive-extension coverage.
COMPARISON: Known derived duality and hyper-Ext cover the required framework without locally free ordinary higher images. They do not state this family's hull-defect sequence or identify its edge maps with L108's actual pairing; that bounded specialization remains mathematical work. No matching ready-made numerical defect theorem was identified in the inspected sources, and no novelty is inferred.
GAP: Apply the cited duality and contravariant spectral sequence to the actual local complex, identify all surviving terms and maps against the extended Serre form, and compare with the hull-quotient sequence. No essential unread source is identified for that calculation; no relation, length or obstruction is established by this review.
REASON: The changed target now has primary source coverage for relative duality, local derived-dual cohomology and finite-length terms. Approve the unchanged target for a separate mathematical step; do not derive or approve a specialized defect relation in this literature turn.
SCOPE: Conditional L071/L095/L097/L100 family and corrected L108 on a regular local surface at the finite possibly empty split locus; algebraic derived duality, its ordinary-cohomology sequence and hull-defect comparison only. No metric extension, global semistability, reduced defect scheme, ordinary split-point base change or kernel existence.
LITERATURE_REASON: Essential relative-duality and contravariant local spectral-sequence coverage was missing for this newly saved target; the prior ready audit expressly excluded local defect calculations.

The main gap remains algebraic realization of primitive rational Hodge
classes, even on arbitrary fourfolds. The intermediate target is the
exact local sequence above. Its plausible downstream use is control of
the corrected sum w+q in c_2(N)=(800-w-q)eta, or a precise demonstration
that duality alone leaves the needed control unavailable. Common-kernel
existence and transverse transport remain independent gaps.

## Existing work and failure comparison

Essential inputs are corrected L108's actual C=Rp_*End_0(F), A_0=0,
torsion-free A_1, finite A_2, locally free E=A_1** and Q=E/A_1;
L071's hypothetical compatible F and full integral tensor; audited
L095's actual derivative; audited L097's algebraic family and finite
possibly empty Z; and audited L100's stable-open comparison. No F or
split parameter is known to exist. The lengths of A_2 and Q are unknown.

Reuse the [L108 audit source assessment](2026-10-15-equality-algebraic-defect-budget-critical-audit.md)
for perfect pushforward/derived base change (0B91), local representatives
(0BCC/0BCD), and reflexive full faithfulness/local freeness (0EBJ/0B3N).
Its historical numerical audit checklist contains the pre-audit signs;
corrected L108 and history/304 supersede those signs. This review uses
the corrected budget only. No independent computation is repeated.

Targeted searches in the two immediate algebraic-defect working notes
and history/304 found no previous local-duality sequence. ATTEMPTS/066
was read: algebraic extension is not metric extension or semistability,
and its codimension-two source obstruction remains. ATTEMPTS/063/065
are preserved; their parked metric/local-degree and determinant routes
are not reopened. Derived-fibre dimensions are not ordinary lengths.

## Inspected primary theorem scope

All Stacks references below are the live HTML versions inspected on
2026-10-15; tag identifiers, rather than potentially shifting chapter
numbers, identify the statements. General theorems should be imported
by these citations; no general reproof is warranted.

[Remark 48.12.5, 0B6S](https://stacks.math.columbia.edu/tag/0B6S)
defines the relative dualizing complex and trace for a proper flat
finitely presented morphism between quasi-compact quasi-separated
schemes, and records their derived base-change compatibility. Read the
complete remark. The product projection here meets those hypotheses.
This is derived base change, not ordinary-image base change.

[Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT)
identifies the right adjoint's value on the structure sheaf with
wedge^d Omega_{X/S}[d] for a smooth proper relative-dimension-d map over
a Noetherian base. Read its complete proof: the regular diagonal,
adjoint compatibility, normal determinant and conormal identification
fix the positive shift. Here the relative dimension is two and the
chosen K3 two-form trivializes the relative canonical line. Section
48.15 explicitly does not claim all canonical compatibility assertions
for this identification; no numerical Serre-trace normalization should
be inferred from this statement alone.

[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
says that a coefficient pairing K tensor^L M -> omega^bullet inducing
K ~= RHom(M,omega^bullet), with M pseudo-coherent, produces a perfect
pushforward pairing by relative cup and trace. Read the complete remark
and its map comparison. For the proposed application, V=End_0(F) is
locally free and has the trace self-duality checked in L108. The later
step must insert the relative-canonical shift and match the induced
ordinary pairing on U with L108's chosen form; multiplying by its fixed
nonzero normalization constant does not change perfectness. No ordinary
higher-image freeness at Z is a hypothesis of this theorem.

[Lemma 48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q)
initially gives the adjunction isomorphism after the quasi-coherator;
its proof uses pullback/tensor adjunction and the projection formula.
The bounded perfect setting is covered directly by 0G81 and the first
paragraph of [48.12.7, 0E4L](https://stacks.math.columbia.edu/tag/0E4L),
which explicitly identifies the pushforward of a perfect derived dual
with the dual of the perfect pushforward. Read those passages, rather
than silently dropping 0A9Q's qualification. L108's perfectness is the
reused applicability input.

[Example 21.32.1, 07AA](https://stacks.math.columbia.edu/tag/07AA)
provides, for bounded-above K and a module M on a ringed site,

\[
 E_2^{i,j}=\operatorname{Ext}^i(H^{-j}(K),M)
 \ \Longrightarrow\ \operatorname{Ext}^{i+j}(K,M).
\]

Read the full example and its injective-resolution double-complex
construction, and [12.25.1--3, 012X](https://stacks.math.columbia.edu/tag/012X)
for the two filtrations, total-complex signs and finite-diagonal
convergence. This covers the module category over each R=O_{B,z}.
The differentials and resulting filtration must be retained in the
later application. Section 15.69 (0AVG), also inspected, instead derives
in the second argument and is not the required replacement for 07AA.
No collapse or family-specific exact sequence is asserted here.

[Proposition 10.110.1, 00O7](https://stacks.math.columbia.edu/tag/00O7)
gives a finite free resolution of length d-e for a finite module of
depth e over a regular local ring of dimension d, and global dimension
at most d. Read the statement and complete short proof. The local
rings here are regular of dimension two. The later step must check the
middle module's depth from L108's torsion-freeness before invoking the
sharper resolution length; it may not treat A_1 as free.

[Lemma 47.16.4, 0A7Q](https://stacks.math.columbia.edu/tag/0A7Q)
identifies RHom of a finite-length module into a normalized dualizing
complex with its Matlis dual in degree zero. Read its complete proof
and the explicit finite-length passage to completion in the comments.
[Lemma 57.11.2, in 0G23](https://stacks.math.columbia.edu/tag/0G23)
explicitly records RHom_R(T,R)=T'[-d] for a finite-length T over a
regular local ring of dimension d. Read that local proof paragraph;
[47.21.3, 0AWX](https://stacks.math.columbia.edu/tag/0AWX) supplies the
regular/Gorenstein input. These statements cover noncomplete R here;
no completion of the whole geometric family is being assumed.

[Matlis duality, Proposition 47.7.8, 08Z9](https://stacks.math.columbia.edu/tag/08Z9)
is stated for complete local Noetherian rings and gives an exact
contravariant equivalence with double dual identity. Read the theorem,
proof and finite-length qualification in the comments. Only its
finite-length scope is needed here; the later length bookkeeping must
keep the dual modules, not replace them by the original modules or by
derived residue-field dimensions.

## Discovery searches and limits

Queries included `site:stacks.math.columbia.edu "Relative duality"
"perfect"`, `site:stacks.math.columbia.edu "Spectral sequences for Ext"`,
`site:stacks.math.columbia.edu "finite length" "Ext" "Gorenstein"`,
`"self-dual" "perfect complex" "reflexive hull"`, `"relative duality"
"torsion-free" "surface" "Ext"`, and `"self-dual complex" "finite
length" "cohomology"`, followed by regular-local resolution and Matlis
queries. Primary statements and relevant proof cases above were read.
Broader results returned on Fourier--Mukai transforms, determinantal
complexes and threefold singularities are unread leads, not imported
results or evidence for this surface sequence. The search supplies no
claim of novelty and no blanket exclusion of stronger literature.

## Separate mathematical continuation

The exact TARGET remains unchanged and is now SPECIALIZE. A later
research turn may apply the cited framework to the actual C at each
z, list all Ext terms with their shifts, compute the relevant edge and
connecting maps, and compare with 0 -> A_1 -> E -> Q -> 0 using the
actual extended pairing. It must justify every identification on the
puncture and at the stalk; abstract self-duality alone is not a named
ordinary-sheaf map. Check Z empty directly. Do not infer reducedness,
ordinary split-point base change or local lengths from fibre dimensions.

Continue this mechanism only if the verified sequence supplies defect
control useful for the corrected budget or a concrete further local
map test. If it merely permits compatible uncontrolled defects, record
that limit and park this duality-only numerical route rather than
claiming an obstruction. No specialized sequence, relation between w
and q, metric conclusion or new lemma is approved as true here.
Full matching Mathlib coverage is not checked. This literature-only
turn changes no lemma, mathematical script, DAG or proof overview.
