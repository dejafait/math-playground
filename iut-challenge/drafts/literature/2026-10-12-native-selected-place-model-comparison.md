# Native selected-place reduction hypothesis — completed source comparison

TARGET: Compare IUT I Definition 3.1's selected-place reduction hypothesis with the model-class condition in L050.
CHECKED: 2026-10-12
DECISION: IMPORT
SEARCH_EVIDENCE: Searched the scoped L050 assessments, ATTEMPTS/028, histories/163 and /166, foundations/02 and the packet-field-role assessment; these leave this comparison open. Targeted native-definition/model queries located the author-hosted May 2020 source, its older RIMS1756 version, the publisher and an accessible May 2020 reproduction; complete inspected passages and failed retrievals are distinguished below.
SOURCE_EVIDENCE: Mochizuki, IUT I, May 2020, 186 pages, Definition 3.1(a)–(f) printed pp.61–63 and section 0 Numbers/Curves pp.35–36, read completely for the relevant definitions through the linked reproduction; Remark 3.1.7(i) p.66 also read. Semi-graphs of Anabelioids, October 2005, section 0 Curves pp.9–10 read. Reuse inspected Dupuy–Hilado arXiv:2004.13228v1 Definition 5.3.1(4)/Remark 5.3.2 p.26 and audited L050. Author-hosted IUT I metadata/indexed critical wording agrees, but its complete PDF retrieval and byte identity remain unverified.
COMPARISON: Native Definition 3.1(b) conditions the fixed X_F at every F-place above the selected moduli places, not every F_mod-descent at the F_mod-completion. L050's additive Q_3-descent verdict therefore does not refute that native predicate; its conditional exposition verdict is preserved.
GAP: The textual predicate comparison is complete for the specified May 2020 version. Application to the unchanged curve at all places above 3, sufficient native initial data and original finite B>=A remain unresolved; no new mathematical application is approved here.
REASON: Import the native definition for this comparison, without reproving a reduction theorem or deriving a new lemma. The mismatch changes the route: park the broad-model native objection and review a distinct all-F-place prerequisite test separately.
LITERATURE_REASON: IUT I Definition 3.1 and any directly referenced definition of the selected places are essential unread sources for native applicability; additional browsing of the ready twist theorem is unnecessary.
SCOPE: Exactly TARGET; one bounded primary-source comparison, with a precise source version and page/definition references. No new twist, curve selection, field enlargement, all-place theorem or numerical comparison.

The main gap remains original finite B>=A. The intermediate target
is to determine which reduction predicate the native prerequisite
actually imposes. Its downstream use is deciding whether L050's
conditional obstruction addresses that prerequisite at all. The
exposition's model terminology is not by itself a native theorem.

Start with the full native Definition 3.1 and only its necessary
selected-place references, retaining the source version. Reuse the
existing exposition and twist coverage. Record whether the native
condition is attached to a fixed curve over F, a specified descent,
all descents, or some other precisely stated object; do not infer a
choice before reading. Distinguish multiplicative, split multiplicative
and potentially multiplicative reduction and their actual base fields.

The discriminating test is an exact predicate comparison. A mismatch
parks L050 as an exposition-only obstruction. A matching predicate
requires separately gate-approved mathematical applicability before
any native conclusion. If essential references cannot be inspected,
record SOURCE_BLOCKED rather than identify the definitions by analogy;
retain the bounded source blocker for subsequent routing. Do not
repeat the completed twist audit or treat a terminological objection
as an essential IUT flaw.

Essential local inputs: L050 with direct inputs L045,L048; L049 is
contrast only. Retain the same E_0, F=Q(zeta_60,E_0[30]), Omega,
u, H,N, fixed M>=max(M_tors,31), v_3(3)=1 and v_3(q_0)=30,
without q_0=3^30. L044–L047,L042 remain through those inputs.
The intended/native model class, other selected places and their
orders, sufficient initial data, actual inputs/actions, pilot,
essentiality and finite B>=A remain open. Preserve ATTEMPTS/022,
025,026,027,028. Full matching Mathlib coverage remains unchecked.
The proposal above records the turn-start test. The completed comparison below
supersedes its pending-source status only for TARGET.

## Completed comparison — 2026-10-12

### Version, retrieval and inspected scope

The [author's paper list](https://www.kurims.kyoto-u.ac.jp/~motizuki/papers-english.html)
dates IUT I 2020-05-18. The author-hosted endpoint returned 186-page
metadata and an indexed passage containing the critical clause of Definition
3.1(b), but subsequent text requests timed out. A direct curl failed DNS
resolution. The [publisher page](https://ems.press/journals/prims/articles/201525)
identifies the separate 2021 journal publication, PRIMS 57(1/2), pp.3–207,
DOI 10.4171/PRIMS/57-1-1; its PDF link requires a subscription and did not
supply the definition. No purchase or authentication was attempted.

The accessible [reproduction of IUT I](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf#page=61)
is headed May 2020, has 186 pages, and supplies the same critical wording
as the indexed author source. Its title/version and full Definition
3.1(a)–(f), printed pp.61–63, were actually inspected, including the
continuation of (b) across pp.61–62. Section 0 Numbers/Curves,
pp.35–36, fixes the valuation and curve conventions. These are primary
mathematical text reproduced on another host; byte identity with the
currently hosted author PDF was not checked. No claim is made that
the 2021 journal pagination or an unread later revision was inspected.
The August 2012 RIMS1756 PDF yielded metadata/indexed excerpts only;
it is not a substitute input for this May 2020 comparison.

Queries included `Mochizuki IUT I Definition 3.1 multiplicative model`,
the exact every-model terminology, native stable-reduction/odd-residue
wording, the author version date and a targeted search for the known
reproduction host. Search excerpts initially suggested the discrepancy;
approval relies on the complete reproduced definition, not those excerpts.

### Predicate and quantifiers

Write X_F for the specified once-punctured elliptic curve and F_mod for
its field of moduli. The reduction clause is:

For every v in V_mod^bad and every t in V(F) lying over v, X_F has
multiplicative reduction at t.

Thus the base completion for this test is F_t. The index v belongs to
the moduli field; it does not move the curve or reduction test to that
field. The clause concerns one fixed F-curve, not a class of its descents.
It says multiplicative, without adding splitness or replacing it by
potential multiplicativity. Definition 3.1(e)'s chosen K-places are
a separate section of the place map, not a restriction of this all-F-place
quantifier to one retained completion. The stable-reduction requirement
is likewise on X_F over F.

The contrasting exposition clause is precisely Dupuy–Hilado v1,
Definition 5.3.1(4), printed p.26, as inspected in the reused
`2026-10-11-selected-model-quantifier-at-three.md` assessment. It
quantifies over models over Q(j_E) and tests reduction at that field's
place. L050 retains an explicit broad-model interpretation and also
records the narrower isomorphic-equation interpretation. Neither is
a universal descent quantifier supplied by native Definition 3.1(b).

This is an object/base-field/quantifier mismatch. L050's conclusion
concerns E_0^(3) over Q_3. The native clause instead concerns the given
X_F over completions F_t. There is consequently no source-supported
step replacing the latter predicate by the former. This is a textual
applicability verdict, not a derived assertion that the unchanged curve
satisfies the native clause. In particular, neither one-place split
reduction from L048 nor semistability from L049 is silently substituted
for all selected native data.

### Defining references and remaining scope

[Semi-graphs of Anabelioids](https://www.kurims.kyoto-u.ac.jp/~motizuki/Semi-graphs%20of%20Anabelioids.pdf#page=9),
October 2005, section 0 Curves, pp.9–10, was read for the curve/log-curve
conventions cited by IUT I section 0. It specifies pointed stable-curve
moduli and stable log curves via pullback of the tautological log curve.
This supplies terminology, not a newly proved bridge from elliptic
semistability to the pointed stable model required by a future application.

IUT I Remark 3.1.7(i), p.66, distinguishes the unique orbicurve model
C_Fmod under the K-core hypothesis from the elliptic curve's descents.
It supplies no replacement reduction quantifier. Its assertion is not
applied to the retained packet: K-coricity is still unestablished.
The directly cited AbsTopIII Definition 5.1(ii) remains an incompletely
retrieved lead (November 2015 author PDF metadata/indexed start only).
No new field-of-moduli theorem or reconstruction input is imported from
it. Naming F_mod as in Definition 3.1 suffices for the comparison;
the L050 field identification is reused with its existing qualifications.
The EtTh/CanLift references in (d)–(f) are not needed to decide this
reduction quantifier and have not been approved for a new construction.

The stop test returns a mismatch. Preserve L050 and ATTEMPTS/028 as
conditional exposition results, but park their native application. A
distinct test at every F-place above 3 may use L045,L048,L049 after
separate coverage approval. Its obligations include the all-place
transfer and the pointed-curve reduction meaning; no such test was
performed this turn. All other native data, actual inputs/actions,
pilot transport, essentiality and finite B>=A remain unresolved.

No new lemma, theorem proof, mathematical script or Mathlib absence
claim is supplied. Full matching Mathlib coverage is not checked.
