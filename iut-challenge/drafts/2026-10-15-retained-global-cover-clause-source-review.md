# Retained global covering clause — source comparison, step 226

This is a literature-only comparison, not an application proving clause
(d) for the retained cover. The main gap is still finite B>=A and actual
input/action/pilot/essentiality. Its intermediate target is to determine
exactly what remains to apply the global covering clause. Its downstream
use is a bounded same-object specialization, without a duplicate cover
lemma or an unnecessary global theta-descent problem.

## Inspected sources and qualifications

[Mochizuki, IUT I, May 2020 author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
186 pages, Definition 3.1(d), printed p.62, was read completely through
its [reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=62).
The adjacent (c),(e),(f), pp.62–63, were read to fix scope. Clause (d)
requires the level orbicurve of the specified type, the stated core,
and the cartesian cover/fundamental-group diagrams; its final paragraph
recalls geometric theta subgroups. The local models and sign condition
occur separately in (e),(f). The author endpoint supplied May 2020
metadata; its targeted passage retrieval failed. Byte identity and
journal-version equivalence remain unverified. No screenshot image
was delivered, so no visual inspection is claimed.

[Mochizuki, EtTh, PRIMS 45 (2009), 227–349](https://ems.press/content/serial-article-files/41069?nt=1),
section 2 opening, pp.261–262, Definition 2.1 and Remark 2.1.1,
p.262, Proposition 2.2, pp.262–264, its complete proof, and Definition
2.3, p.264, were read. The arithmetic elliptic quotient has geometric
quotient the abelianization modulo l. A rank-one quotient must remain
surjective geometrically and kill the whole original-cusp decomposition
group. Choosing an origin cusp supplies the inversion square. At odd
l, Proposition 2.2 gives the inversion eigensplitting and the geometric
subgroups; its arithmetic covering construction uses a cusp splitting.
Definition 2.5(i), p.265, was read separately: its local hypotheses and
compatible splitting are additional to Definition 2.1. Preserve IUT I
Remark 3.1.6's odd-level correction from the ready source record; the
deleted even-level remark is not an input.

[Mochizuki, CanLift, Documenta Mathematica Extra Volume (2003),
609–640](https://www.kurims.kyoto-u.ac.jp/~motizuki/Canonical%20Liftings.pdf),
section 2, Definition 2.1/Remark 2.1.1 and the finite-etale common-cover
categories on author-PDF pp.8–11, are reused from the completed
`drafts/2026-10-12-native-k-core-source-notes.md` and L052's audited
application. In particular, the defining category permits stack quotients
of finite-etale covers and uses K-morphisms throughout. Current targeted
retrieval timed out after title/34-page metadata. No fresh extraction or
new invariance theorem is claimed. This is adequate reused coverage,
not a new essential source blocker.

The [official challenge announcement](https://zen.ac.jp/news/0ul6zqed9-0),
dated 2023-07-07, was checked on 2026-10-15: its inherent-flaw target and
publication/adjudication qualifications remain the statement recorded in
`foundations/01-challenge-scope.md`. No inference about current prize
availability or mathematical correctness is made.

## Coverage map and remaining application checks

Use neutral names to distinguish the source's typographic underlines:
X_base=E_0,K minus 0, C_base=[X_base/{±1}], X_basic=Y=B minus V,
and C_basic=[Y/{±1}]. Here B,V,psi and the origin 0_B are exactly L053's
objects. These are names for the proposed comparison, not new objects.

| Predicate/input to compare | Existing evidence | What a separate mathematical application must check |
| --- | --- | --- |
| Arithmetic quotient through Pi_X^ell, with rank-one target | L053's constant V, actual degree-seven isogeny, full monodromy and trivial whole cusp-decomposition image | Explicitly relate this monodromy to EtTh's quotient by the geometric commutators and seventh powers, rather than only cite an abstract cyclic deck group. |
| Type (1,7-tors) and its inversion quotient | L053's actual pointed quotient, rational cusps and cartesian stack square; EtTh Definition 2.1 | Use the actual origin 0_B and psi. Retain stack stabilizers; the bottom cover is not asserted Galois. |
| Specified K-core of C_basic | L052 proves C_base itself is a K-core; L053 gives the finite-etale map to it | Apply the cited common-cover category definition to the actual finite-etale map. Do not silently replace coricity of the base by an uncited statement about a cover. |
| Arithmetic and geometric group diagrams | L053's cartesian covering square; EtTh section 2 opening specifies the corresponding groups | Track basepoints up to the permitted conjugacy, the extension K/F, and geometric kernels. An abstract group isomorphism alone is insufficient. |
| Final geometric theta subgroup recall | EtTh Proposition 2.2(i)–(iii), Definition 2.3, with odd l=7 | Import the geometric conclusion for this basic cover; retain the distinction from choosing an arithmetic/global cusp splitting. No new theta construction or reproof is needed. |
| Selected local predicates, outside this global application | L057 and L060, using L058,L059 and inherited inputs | Reuse only their conditional singleton result. They do not substitute for the global quotient or core check. |

This completed source comparison finds coverage for the proposed checks.
It does not carry them out here. In particular the last clause is a
geometric subgroup statement: demanding that L058's local splitting be
a prescribed global splitting would add an obligation not requested by
that clause. Conversely, identifying the basic cover with the further
theta cover would lose a distinction made by the inspected definitions.
No arithmetic/global theta descent is proved or authorized by this review.

L061 is a separate audited q-order prerequisite; it is not used to
manufacture the covering diagrams. None of this establishes the other
initial-data clauses, the native moduli-field identification or a
numerical inequality. Full matching Mathlib coverage is unchecked; the
uninspected GitHub formalization search hit is only a lead and supplies
no theorem or Mathlib evidence.

## Duplicate/failure screen and bounded continuation

Reused the native cover/cusp, rank-one and selected-cusp assessments
named in the gate record, plus the CanLift source record. Read L053's
actual puncture/monodromy/inversion proof, L052's coricity statement and
transfer argument, and L057/L060's exact scopes. The global algebraic
cover is already established; repeating its construction in another
lemma is unwarranted. The newly explicit source obligation is the
complete clause-(d) applicability bookkeeping, including its final
geometric paragraph.

ATTEMPTS/030 excludes the rank-two full multiplication cover, not L053's
retained factor. ATTEMPTS/031's marked-coordinate mechanism remains
parked and is not needed for the global clause; ATTEMPTS/027's exact
old-curve stop is unchanged. No cross-notebook source was read. Searches
used exact `Definition 3.1`, `type (1,l-tors)`, `K-core`, and global
cover/theta terminology on the specific author/source paths; broader
formalization/expository hits were not used as theorem evidence.

Continuation inputs: L052,L053,L057,L060, with inherited
L045,L048,L051,L054,L055,L056,L058,L059; L061 is separate. Retain
E_0/Q, F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega,u,w,H subset N,
M>=max(M_tors,31), full 30-torsion, the pointed Tate isomorphism,
q_0 in Q_3 with v_3(q_0)=30,v_3(3)=1, and actual U,alpha,psi,gamma,
0_B,Q,c and stable logs. Native Q subset F_mod subset F and rho remain
conditional. Do not set F_mod=Q, K_glob=N or q_0=3^30.

Continue if every check above follows for these same objects from the
cited inputs; record only the missing applicability argument in the
existing canonical result, with a minimal overview change if warranted.
Stop that assembly if arithmetic elliptic factorization, common-cover
core inheritance or an exact group diagram needs an uncovered theorem;
name that precise missing input for REVIEW_REQUIRED. No coordinate
calculation, second selected place, global theta descent or sufficient
initial-data claim is part of this continuation. No mathematical
EXPLORATION attempt was spent. No new mathematical result was derived.
