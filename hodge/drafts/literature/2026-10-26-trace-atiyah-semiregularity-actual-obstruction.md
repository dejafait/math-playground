# Trace–Atiyah semiregularity and the actual obstruction — source comparison

TARGET: Assess whether the trace–Atiyah semiregularity map constrains L167's actual quadratic obstruction through L165's fixed Leray maps.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 578 inspected Buchweitz–Flenner Corollary 4.8 and its graded-centrality proof input, Lepri–Manetti's explicit two-input identity and obstruction theorem, and Bandiera–Lepri–Manetti's all-component theorem; compared the precise local failures and L171's base Atiyah/KS comparison. Exact queries and scope are recorded below; no novelty inference from searching.
SOURCE_EVIDENCE: Buchweitz–Flenner arXiv:math/9912245v1, Proposition 3.12 and Corollaries 4.3,4.8, PDF pp.24,29,32; Lepri–Manetti arXiv:2102.05016v3, Theorem 3.6 (complete C2 proof), Corollaries 3.7,4.1–4.2, pp.9–13; Bandiera–Lepri–Manetti arXiv:2111.12985v3, Section 6 and Corollaries 6.3–6.4, pp.14–16. Reuse saved actual duality and Atiyah/KS coverage.
COMPARISON: Annihilation of the actual quadratic bracket is already known, without any semiregularity injectivity hypothesis. The remaining specialization is to compare the base Atiyah component and its Serre transpose with the fixed tangent summand through j,r,a; the sources do not assert this family-specific identity. Scalar cyclicity alone did not use this Atiyah-class input.
GAP: No essential source gap remains for a bounded base-tangent comparison; a global derived lift and trace/Serre comparison with the actual maps still require mathematical verification. No vanishing of the full complement, point bracket, or F has been established.
REASON: Known graded-commutator annihilation supplies the exact quadratic input; a specific base-tangent test can now be stated rather than leaving two unrestricted components. Its new continuation assessment requires separate approval before research.
SCOPE: Same conditional L071/L116/L165 family, product metric/triple/forms and actual connection; locally free rank-two product-polystable F with integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P; finite reduced possibly empty Z, unknown s,t, actual j,r,a, full trace-free obstruction and actual Yoneda quadratic term. No cross-notebook input.

## Invocation-start proposal (retained; superseded by the comparison below)

The main gap is primitive realization, with existence of F unresolved.
The intermediate target is source coverage for the specified
semiregularity operation and its comparison with both actual obstruction
components. Its possible downstream use is a linear restriction on the
quadratic lifts in L167 which does not discard L165's complement.
This is a proposed mechanism, not a claim that the restriction is
nonzero or independent of the already retained cyclic identities.

Retrieve primary theorem hypotheses and the essential proof case for
locally free sheaves on smooth projective complex varieties. Distinguish
annihilation of the ordinary Yoneda quadratic obstruction, all higher
obstructions, and curvilinear obstructions. Check trace-free/fixed
determinant scope, volume conventions and whether real polarization
enters at all. Search stronger results and known obstructions to using
semiregularity on hyperkähler products. Reuse ready Atiyah/KS coverage
where its actual scope matches; do not derive a new map identity here.

Essential inputs are L071,L116,L165,L166,L167, retaining
L108/L109/L111/L115 through their hypotheses. L168 is optional only if
its actual quotient-adjoint comparison is needed. The relevant local
lead is `2026-10-25-adjoint-complementary-yoneda-component.md`, final
paragraph; the failure boundaries are ATTEMPTS/004,/009,/068,/093,/094
and /095. No other notebook result is proposed.

Continue only if the inspected theorem applies to the actual quadratic
operation and supplies a specific evaluable restriction or a bounded
independence test. Park if it merely reexpresses an already known
cyclic identity or leaves both components wholly uncontrolled. A
nonzero obstruction cannot be inferred from a nonzero target space,
and an obstruction-annihilation theorem cannot be treated as
injectivity. Keep Z empty and t=0 cases and all actual maps.

If a new central mechanism survives the source comparison, nominate
one bounded proof_attempt/creative with a precise critical claim and
decisive test. At present no such attempt is ready: theorem scope,
independence and actual-map evaluability are missing. Full matching
Mathlib coverage is not checked.

## Completed comparison — step 578, 2026-10-26

This is a literature-only EXPLORATION / REPRODUCTION. It fills source
coverage and identifies a bounded specialization; it proves no new
family-specific map identity. No lemma, mathematical script, DAG edge,
or argument in PROOF.md is changed.

### Primary results and inspected proof cases

R.-O. Buchweitz and H. Flenner, *A Semiregularity Map for Modules and
Applications to Deformations*, Compositio Math. **137** (2003), 135–210,
[arXiv:math/9912245v1](https://arxiv.org/pdf/math/9912245v1), is the
primary source for the needed quadratic statement. Page numbers here
are the preprint's printed pages, not the journal's numbering. Section
4 defines, for a perfect complex, the maps

    sigma_q(c) = Tr((−At(F))^q c)/q!
       in H^{q+2}(X,Omega_X^q).

Read Proposition 3.12 and its proof, p.24: the power At^q is graded
central with sign (−1)^{iq} against Ext degree i, by naturality and
shift compatibility. Corollary 4.8, p.32, states that the entire
semiregularity family vanishes on the graded commutator subspace of
the Yoneda algebra. The preceding proof explanation uses that
centrality and graded trace, and the following paragraph explicitly
identifies second-order obstructions as lying in [Ext^1,Ext^1]. This
already covers the bracket needed in L167; it is not necessary to
upgrade a curvilinear theorem to an all-obstruction theorem for this
target. F is locally free on a smooth projective X, hence perfect;
the source does not require stability or simplicity for Corollary 4.8.
No reproof of graded centrality or the semiregularity construction is
justified. Corollary 4.3, p.29, and its preceding trace/derivation
calculation compare contracted Atiyah classes with contractions of
the Chern character. They do not make sigma injective or determine
the actual Leray projections.

E. Lepri and M. Manetti, *Connections and L-infinity liftings of
semiregularity maps*, J. Geom. Phys. **168** (2021), 104303,
[arXiv:2102.05016v3, 22 May 2021](https://arxiv.org/pdf/2102.05016v3),
provides an explicit check of the same operation. Read Theorem 3.6,
pp.9–11, its complete C2 calculation on pp.9–10, Corollary 3.7,
p.12, and Corollaries 4.1–4.2 with proof, p.13. For a finite locally
free complex and a (1,0) connection, the trace cyclic form is compatible
with the connection (Example 3.3). The linear term is −Tr(u f), with
u an Atiyah cocycle; the binary term involves the connection applied
to the inputs. Their C2 identity states that g1 of a bracket differs
from the target differential of g2 by terms involving the input
differentials. This is the essential two-closed-input proof case,
not a claim that a harmonic product is its harmonic representative.
The target is the abelian truncated de Rham complex. Corollary 4.2
annihilates every sheaf obstruction in its hypercohomology; E1
degeneration makes the inclusion of H^3(Omega^1) injective and gives
the stated sigma_1 theorem. Smooth projectivity supplies degeneration,
and a vector bundle itself is a finite locally free resolution.
Remark 3.8's elliptic-curve example warns that the higher lifting
depends on the connection; the cohomological semiregularity map must
not be confused with an arbitrary higher component of a lifting.

R. Bandiera, E. Lepri and M. Manetti, *L-infinity liftings of
semiregularity maps via Chern–Simons classes*, Adv. Math. **435**
(2023), 109358, DOI [10.1016/j.aim.2023.109358](https://doi.org/10.1016/j.aim.2023.109358),
[arXiv:2111.12985v3, 6 September 2023](https://arxiv.org/pdf/2111.12985v3),
gives stronger coverage. Read Section 6's connection/curvature and
Dolbeault identification on pp.14–16, and Corollaries 6.3–6.4 with
proof on p.16. Each component Tr(At(F)^q c)/q! annihilates all sheaf
obstructions on a complex projective manifold. The proof first maps
to an abelian truncated de Rham complex via an L-infinity lift, then
uses E1 degeneration to inject the individual Hodge-cohomology
target. The introductory (−1)^q convention and Corollary 6.4's
positive convention differ by a nonzero component scalar for kernel
questions; any actual-map comparison must fix one convention rather
than transfer a numerical sign silently. The stronger theorem is
available but unnecessary for the strictly quadratic target.

In dimension four the possible targets are q=0,1,2; higher q have
coherent cohomology degree greater than four. The q=0 map is the
ordinary trace, already retained for L167's trace-free bracket. The
q=1 map is the proposed additional operation. The q=2 map is also
covered by the cited all-component statement; no evaluation or
vanishing of its restriction on End_0(F) is claimed here. In
particular c_1(F)=0 is not a license to erase the full Atiyah class.
All these theorems are stated for End(F). Use the actual inclusion
End_0(F) into End(F); they supply no injectivity assertion for that
restriction, no fixed-determinant smoothness conclusion, and no
integrability of section directions. No real polarization or choice
of a holomorphic volume is needed to define sigma. Comparing with
L165's Q does require its fixed volume and common scalar.

### Actual-map comparison boundary and independence test

Reuse the inspected source scope in
`2026-10-26-split-ks-extended-tangent-comparison.md`: Huybrechts–Lehn
10.1.5,10.1.7–9 and Kuhn's derived Atiyah naturality and extension
comparison cover the base family Atiyah/KS construction even at
nonsimple split fibres. L171's canonical proof gives the degree-one
map to L108's specific inclusion T_B -> M and compares the derived
maps locally. It does not state the global cohomological transpose
needed here. Do not promote its local derived equality to a global
one without an argument; use the actual truncation triangle as a
possible test. Reuse L165's Stacks 0G81/0FVU trace/Serre compatibility,
including its fixed shifts, and L116's actual j,a,r. These sources
cover the tools, not the desired conclusion.

The concrete candidate test is whether the base component of sigma_1,
paired against base tangent cohomology under Serre duality, detects
precisely the H^1(B,T_B) projection of R[x,x]. This is a question for
the next mathematical turn. A successful comparison could restrict
L166's complementary operation to H^1(B,N), instead of the entire
H^1(B,M). L116 already records h^1(N)=704−s+2t; at its formal endpoint
this space is zero. Thus the requested test has a discriminating
threshold and a plausible use in L167's quartic-lifting condition.
Neither the restriction nor an improved square bound is proved here.
The full point quotient, the normal part, and actual section quadrics
must remain; injectivity of sigma is not needed for this proposed
partial detection and must not be assumed.

This adds Atiyah-class information absent from L166's unweighted
triple cyclic trace. It may still collapse after the actual comparison.
Park if only an uncomputed cancellation between point and complementary
terms survives, or if no positive-rank tangent detector is identified.
Even a zero normal obstruction space would not by itself prove a
nonzero point bracket, exclude F, or realize a primitive Hodge class.

### Searches, duplicates, stronger leads and qualifications

Queries actually run: `Buchweitz Flenner semiregularity map obstructions
Atiyah class vector bundles theorem`; `Iacono Manetti semiregularity
map annihilates obstructions coherent sheaves Atiyah class`;
`site.arxiv.org semiregularity map coherent sheaves Iacono Manetti
Chern Simons`; `site.arxiv.org Buchweitz Flenner semiregularity
9912245`; `site.arxiv.org semiregularity maps annihilate obstructions
Atiyah class 2021`; `"semiregularity" "K3" "product" Atiyah
obstructions`; `"semiregularity" "symplectic" "Atiyah" kernel`;
`"semiregularity" "Serre dual" "Atiyah" map`.

Also inspected Kuznetsov–Markushevich, *Symplectic structures on moduli
spaces of sheaves via the Atiyah class*, J. Geom. Phys. **59** (2009),
843–860, [author-hosted published PDF](https://homepage.mi-ras.ru/~akuznet/publications/SymplecticStructuresOnModuliSpacesOfSheavesViaTheAtyiahClass.pdf),
Lemma 2.1, formula (11), and Theorem 2.2 with its family KS/Atiyah
proof, pp.849–850. The theorem concerns closed 2-forms on the smooth
locus of a moduli space of stable or simple sheaves. It cannot supply
unassumed smoothness, simplicity of each split restriction, or a
nondegenerate form on this fourfold's obstruction space. Later
Lie-algebroid generalizations and joint-deformation papers surfaced
as leads but were not inspected and are not required inputs. Search
hits asserting Hodge resolutions were not used as evidence.

The local duplicate check searched only the named complementary,
quadratic and base-KS assessments and L116/L165–L167/L171 passages.
The former complementary assessment explicitly left semiregularity
unread. ATTEMPTS/004 requires smooth/lci support which failed for
that different support; ATTEMPTS/009 concerns the specified negative
syzygy presentation, not this hypothetical locally free F.
ATTEMPTS/068,/092–095 retain the failures of numerical section
constraints, unevaluated brackets, scalar isotropy, cyclicity-only
vanishing and metric-star compatibility respectively. None evaluates
this base trace–Atiyah operation. No search certifies originality.

No primary source access blocker remains. Full matching Mathlib
coverage for semiregularity and this actual-map specialization is not
checked; absence is not claimed. The new bounded continuation is in
`2026-10-26-semiregularity-base-tangent-detector.md` and must receive
its separate approval before invocation. This is established-route
development, not a justified creative attempt: whether the detector
survives the fixed maps must first be settled.
