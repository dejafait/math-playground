# Opposite coincidence scheme — bounded continuation proposal

TARGET: Test whether the off-diagonal coincidence scheme of L118's opposite map is finite and reduced using local total geodesy and L120's degree-one normalization.
CHECKED: 2026-10-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed opposite point-separation comparison, its searches for trianalytic self-intersections and double points, and the earlier equality two-branch assessment; no matching theorem for this exact scheme was identified in the inspected sources.
SOURCE_EVIDENCE: Audited L118's actual natural quaternionic immersion and parametrized geodesy, audited L120's finite unramified birational image map; Verbitsky alg-geom/9703016v1, Propositions 3.9--3.10 and Theorems 4.7/6.2; Stacks Lemma 29.36.13 (02GE), full statement/proof, and Lemma 37.44.1 (02LS), full statement/proof; standard named Picard--Lindelof uniqueness and inverse function theorem.
COMPARISON: Existing sources control individual branches and smooth normalization. They do not evaluate this actual off-diagonal scheme. The proposed difference is to test branch intersections and scheme tangent spaces, retaining possible isolated collisions rather than proving separation or forcing all branch tangents equal.
GAP: Establish or refute finiteness and reducedness for the entire actual coincidence scheme, including equal-tangent branch pairs and possible accumulation toward the diagonal; no conclusion is claimed here.
REASON: One bounded specialization of ready local-geodesy and birationality tools is independently testable after the direct global-injectivity inference is parked. This newly written assessment requires separate supervisor approval before a research invocation.
SCOPE: Only L071/L118/L120's conditional F with integral c_1=0, rank two and ch_2=-14e_1-21e_2-tau_D, at the identical marked metrics/triples; B=S_1 and Y=S_2. No F existence, image normality, ambient completion, collision emptiness, reconstruction or transport.

## Exact test and intended use

Write f=f^- and R=B x_M B, using the actual algebraic map to
M=M_H^s(2,0,-19). The proposed object is the open subscheme
R_off=R minus Delta_B. The threshold is that R_off is a finite reduced
C-scheme, with the empty case permitted. This is a target, not an
established property. Its cardinality and emptiness remain separate.

The main gap remains universal primitive Hodge realization. A finite
collision reduction could support a later family-specific separation
invariant, while leaving F existence and transport independent. It
improves no cycle-class span by itself.

Use the actual smooth connection-moduli charts of audited L118 at a
putative common value. Test equal and unequal quaternionic tangent
images separately. For equal images, test local geodesic uniqueness
against the actual generic degree one, without postulating a global
source isometry. For unequal images, compute the scheme tangent of
the actual fibre product, not just a set-theoretic branch intersection.
Then address the diagonal and global finiteness. This is an outline of
questions to prove, not a derivation or a precomputed answer.

The relevant general scheme tools are
[Stacks, Lemma 29.36.13](https://stacks.math.columbia.edu/tag/02GE),
which makes the diagonal of an unramified morphism an open immersion,
and [Lemma 37.44.1](https://stacks.math.columbia.edu/tag/02LS), which
equates finiteness with properness and local quasi-finiteness. Their full
statements and proofs were inspected. Apply them only after verifying
the hypotheses for the chosen schemes. The inverse function theorem
and Picard--Lindelof uniqueness concern local smooth geodesic charts;
they give no global distance preservation or ambient completeness.
L118 already supplies the actual connection identity to which such
local uniqueness would be applied. The elementary specialization is
needed to avoid assuming an intrinsic singular-image structure and
to retain scheme multiplicities; no broad desingularization theorem
is being reproved.

The primary hypercomplex normalization theorem and its branchwise proof
are recorded precisely in the
[completed source comparison](2026-10-17-opposite-image-point-separation.md).
They describe multiple components rather than a ready singleton-fibre
criterion. The older equality tangent-coincidence stop is preserved:
this test does not try to force all tangent lines equal. It also does
not repeat ATTEMPTS/046's Hom Euler/first-order computation, the normal
index stop, or the compactification search.

Continue only with a complete argument controlling both tangent cases,
the actual fibre-product local rings and the diagonal. A finite reduced
answer is partial progress, not injectivity. Abandon this test if it
requires unproved image normality, extension of a local source isometry,
a compact ambient metric, or deleting a nonreduced contribution without
calculation. Preserve any surviving collision alternative explicitly.
Full matching Mathlib coverage is not checked. No new mathematics,
lemma or mathematical script is written in this literature turn.
