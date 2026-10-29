# All-place local-to-global group injections — completed source review

TARGET: Assess source coverage for the all-place local-to-global fundamental-group injections in IUT I Definition 3.1(e) on L113's unchanged reselected objects.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step463 checked the saved global/combined-clause assessments, L107/L113 scopes, step460/461 records and ATTEMPTS/031,035; searched local-global etale injections, completion/decomposition identifications and finite quotient-stack sequences; inspected the primary statements and proof cases below.
SOURCE_EVIDENCE: Qualified IUT I May 2020 reproduction Definition 3.1(e) pp.62–63; Landesman arXiv:2005.09690v3 Theorem 1.1 and Lemmas 2.3,2.6,2.9/Proposition 2.10 proofs; Stacks 0BTX complete proof; Milne ANT v3.08 Propositions 7.60–7.61, Corollary 7.62, section 8 opening and Proposition 8.10 proofs; Zoonekynd arXiv:math/0111071v1 Corollary 6.4 and proof pp.13–14.
COMPARISON: Known characteristic-zero invariance, geometric exact sequences, completion/decomposition and finite quotient-stack results cover the named mechanisms, including geometric theta covers and complex places. They do not themselves identify the actual maps on L113's retained objects.
GAP: A later application must construct compatible embeddings/basepoints, identify the completion map's decomposition image, transport full geometric covering subgroups and match each local square; no such application is proved in this literature turn.
REASON: Essential theorem coverage is now available for the conditional all-place application; use the named results rather than reprove invariance or assert injection solely from curve squares.
LITERATURE_REASON: First exact comparison of all-place local-to-global injection hypotheses after step461 narrowed its assembly; the existing global-clause review does not settle this changed local-completion scope.

Main gap: original finite B>=A and an essential-invalidity proof remain
open. The intermediate target is a precise applicability map for the
source's actual arrows, which could support a later limited (d)–(f)
comparison. No directed cover, full initial-data or numerical conclusion
is a consequence of this proposed review.

Essential inputs: L107,L113, with L105,L108,L110–L112 for fields,
selected completions and reselected section. Retain the same member,
ordering, E_o,C_o,K_C=C_o(E_o[ell]),ell>=7,U,alpha,psi,V, Q and s'.
No cross-notebook input is used. The former unread Landesman lead is
now inspected; its general invariance theorem is a known input.

Continuation/abandonment test: approve a later mathematical application
only if primary results cover the exact geometric and arithmetic arrows
for every required kind of place, with compatible basepoints up to the
permitted conjugacy. If not, name the uncovered case and narrow or park
the import. Do not replace it by an abstract isomorphism or assume
normality of K_C/Q. Preserve authentication/def= qualifications.

Unresolved: directed-cover (*), complete (a)–(c)/initial-data/III/P7,
exact generation/full repair, factor-four excess, actual comparison
action/factorization/pilot and essentiality. Mathlib coverage unchecked.
No mathematical application or new lemma is established here. The
separate application assessment below names the proposed next target.

## Step463: inspected primary inputs and exact scope

The source record is `drafts/2026-10-25-step463-all-place-injection-source-review.md`.
Existing source authentication and def= qualifications are retained.
The [IUT I reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=62)
is May 2020, 186 pages. Definition 3.1(e), pp.62–63, distinguishes
geometric, local arithmetic and base-curve columns; it specifies
profinite etale groups and decomposition quotients. It also uses a
place of the fixed algebraic closure above v. Remark 3.1.1's tempered
groups are a separate scope and are not approved here. The extractor
flattens bars/underlines; no screenshot image was returned. Use the
unambiguous actual objects below and L107's native dictionary, never
guess a new decorated module. This does not authenticate the reproduction.

**Geometric comparison.** [Aaron Landesman, arXiv:2005.09690v3,
20 January 2024](https://arxiv.org/html/2005.09690v3), Theorem 1.1:
for algebraically closed k contained in algebraically closed L, and
connected normal separated finite-type U/k with a normal compactification,
the natural numerically tame fundamental-group map is an isomorphism.
The preceding characteristic-zero observation identifies tame with full
etale groups. Read Lemma 2.3's connected-cover proof and the complete
smooth-curve case, Lemmas 2.6,2.9 and Proposition 2.10: specialization
matches boundary ramification, Abhyankar's lemma removes it, and proper
invariance descends a dominating cover. This is imported, not reproved.
Our scheme candidates are smooth punctured elliptic curves and their
geometric finite-etale theta covers. The comparison must use the actual
inclusions into algebraic closures of completions and, when needed,
their algebraically closed completions; it must not identify these fields.
At finite v the field characteristic is zero, including v above ell
and 2. No prime-to-residue-characteristic restriction on the generic
fiber's finite covers is licensed or required by this cited case.

**Arithmetic kernel.** [Stacks Lemma 58.14.3, 0BTX](https://stacks.math.columbia.edu/tag/0BTX)
requires a quasi-compact quasi-separated scheme over k with connected
base change to an algebraic closure. It gives the full short exact
geometric/arithmetic sequence. Its complete proof was read: constant
covers give surjectivity; Galois translates of sections give normality;
descent of a finite-etale cover to a finite separable extension gives
injectivity. This covers the scheme candidates, not quotient stacks
by an unmentioned extension of its hypotheses.

**Decomposition and completions.** [Milne, Algebraic Number Theory,
v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
section 8 opening/Proposition 8.1, pp.135–136, identifies embedded finite
completions; Proposition 8.10 and both proofs, p.139, identifies a finite
Galois decomposition group with the corresponding completion Galois group.
It is a finite-extension statement, not by itself the absolute assertion.
Propositions 7.60–7.61 with proofs, pp.131–132, and Corollary 7.62 with
proof, p.132, supply root/field stability and realization of each finite
Q_p-extension inside a number field. Remark 7.41's C_p example, p.124,
also describes the algebraically closed completion used here. Later work
must justify cofinality and compatibility before passing to absolute
Galois groups: use actual chosen extensions of places and inverse limits,
not a finite-level identity alone. All finite selected completions are
finite over Q_p. At infinity check the retained iota^2=-1 input: these
fields have complex completions, so a real-place case is not needed.

**Orbicurves.** [Vincent Zoonekynd, The Fundamental Group of an Algebraic
Stack, arXiv:math/0111071v1, 7 November 2001](https://arxiv.org/pdf/math/0111071v1),
Corollary 6.4 and complete proof, printed pp.13–14, gives
1 -> pi_1(T) -> pi_1([T/G]) -> G -> 1 for a connected scheme T
and a finite group G acting on it; these are profinite groups. The proof
uses the Galois object G times T in the equivariant-cover topos, including
its automorphisms and the slice identification. No free action on T or
fixed basepoint is assumed. This covers the constant group {+1,-1},
the punctured elliptic atlases and their theta analogues. Apply it over
the actual fields and algebraically closed extensions, retaining
stabilizers. Corollary 6.6 was also inspected but is not imported: its
printed hypothesis only says connected, whereas the scheme comparison
0BTX explicitly requires geometric connectedness. The application must
retain the latter condition and can use 0BTX and 6.4 throughout.

## Obligation map for the later application

Retain F=C_o, K=K_C, X_F=E_o minus O, X_0=(X_F)_K,
Y=B minus V, C_F=[X_F/{±1}], Z=(C_F)_K, A=[Y/{±1}].
Use L107's actual geometric theta covers of Y,A, not independently
chosen isomorphic covers. This is a scope map, not a new proof.

| Required map or case | Available coverage and remaining application test |
| --- | --- |
| Geometric groups over the fixed algebraic closure versus an algebraic closure/completed algebraic closure at w | Landesman on the scheme covers, then Zoonekynd 6.4 on their finite quotient stacks. Transport the full covering subgroups through the natural maps; an abstract group isomorphism is insufficient. |
| Geometric group into local arithmetic group | 0BTX on each geometrically connected scheme atlas, with 6.4 for the orbicurves. Match kernels and all chosen basepoints. |
| Y_(K_w) -> (X_F)_(F_u), A_(K_w) -> (C_F)_(F_u), u=w restricted to F | L107's global finite-etale maps, actual base change and finite-etale K_w/F_u; connectedness and subgroup correspondence must be checked with this u,w. The intermediate base-change X_0,Z is retained. |
| pi_1(T_(K_w)) -> pi_1(T) for the retained K-objects, and the analogous F-map | Geometric invariance plus arithmetic exactness and Milne's decomposition comparison. Identify the actual image over the chosen decomposition subgroup, with induced profinite topology; no K/Q normality or surjection onto G_K is assumed. |
| Cartesian squares involving scheme/quotient rows and geometric theta covers | Use actual finite-etale inverse images and connected pullbacks, L107's atlas square and the preceding natural maps. Check intersections in one ambient group, with simultaneous basepoint conjugacy. |
| Every finite w, including ell,2 and undesignated bad reduction | Generic fibers have characteristic zero. Do not import a stable integral model, local theta splitting or native bad-place label at these additional places. |
| Infinite w | Match embeddings and complex completions using the retained iota. Use characteristic-zero comparison and trivial complex absolute Galois group; no real descent or tempered assertion is included. |

This covers an ordinary known-method specialization. No source checked
purports to prove a new IUT inconsistency, and none removes directed
(*), full-data or numerical obligations. General reproofs are unnecessary;
only actual-map applicability and the indicated inverse-limit/subgroup
arguments belong to the next mathematical attempt. The earlier atlas,
authentication and decorated-module failures are not reopened. No
duplicate completed same-object all-place application was found in the
specific records checked above. Mathlib coverage remains unchecked.

Additional leads: Noohi arXiv:math/0201021v1 was opened at its introduction
and section 4 locator, and the author's publication page checked. No
Noohi theorem is imported; Zoonekynd 6.4 supplies the needed exact input.
SGA1 XIII Proposition 4.6 is a reference mentioned by Landesman, not an
independently inspected theorem here. No novelty inference follows.

The next application is separately recorded in
`drafts/literature/2026-10-25-all-place-group-injection-application.md`.
It receives its own next-turn approval under the shared continuation rule.
