# Exact Legendre semistability — proposed critical audit

TARGET: Critically audit L081's everywhere semistability assertion for L078's unchanged E_L/G, including complete local torsion and the level-3 endpoint.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Step320 compared the whole L081 proof and the relevant L078 hypotheses/conclusion and generator argument with the ready exact-field assessment; inspected history/317–319 references and ATTEMPTS/033–034. Reopened only the cited primary criterion and torsion theorem, not broad discovery; no uncovered theorem or duplicate exact-field application was found in these scoped records.
SOURCE_EVIDENCE: Reuse Silverberg–Zarhin, Ann. Inst. Fourier 45(2) (1995), 403–420, Definition 3.1 p.405 and Theorem 3.5 p.406, https://www.numdam.org/article/AIF_1995__45_2_403_0.pdf ; reopened publisher abstract https://aif.centre-mersenne.org/item/AIF_1995__45_2_403_0/ confirming n>=3; reopened Milne, Elliptic Curves, second edition (2021), II Proposition 6.3 pp.70–71, https://www.jmilne.org/math/Books/EC2.pdf . Original SGA7 scan remains uninspected; its proposition is a reference, not additional claimed access.
COMPARISON: Existing coverage matches the audit of L081 with levels 5 and 3 on exactly L078's E_L/G. The criterion requires full geometric prime-to-residue n-torsion over an unramified extension and n>=3; no normality or extra 2-primary torsion hypothesis occurs. The remaining work is a separate applicability audit, not a new reduction theorem or reproof.
GAP: Essential source coverage is ready for the exact TARGET. The independent mathematical correctness verdict on L081, including its local geometric-torsion exhaustion argument, remains deferred to the research audit; original finite B>=A and independent initial-data/transport gaps are untouched.
REASON: The proposed audit stays within the already inspected exact-field criterion coverage. Approve reuse and route directly to the separate proof audit; this approval adds no mathematical result and needs no further literature turn.
SCOPE: Only L081 on L078's unchanged E_L/G, inheriting L073/L077 choices D,s,t,H,N and embedding; L049 is method context only.

Essential input: L078's nonsingular E_L/G, full geometric 15-torsion
and two embedded completion equalities, inheriting L073/L077's same
choices. L049 supplies source-method context only. Review L081's
whole proof against the reused primary statements, the endpoint
confirmation and exact place/torsion hypotheses. The proposed test
passes only if every finite place is covered by prime-to-residue
full torsion with no field enlargement, and all retention claims
refer to the same curve/field. Record any failure canonically rather
than assuming normality or additional torsion.

The original finite B>=A, G/Q normality and mixed radical-torsion
kernel, independent initial data, native input/action, all-image
factorization, pilot transport and essentiality remain unresolved.
No new theorem or audit is derived in this proposed assessment.

## Step320 — scope approval only

LITERATURE_REASON: The startup gate requires approval of the newly proposed critical-audit scope. Reuse the ready exact-field assessment; the brief primary-source checks resolve scope only and do not reopen discovery.

The main gap is still finite B>=A. The intermediate target is the exact
audit above; its downstream use is confidence in the same-field reduction
input before any later pointed-model or independent initial-data work.
The comparison did not expand the target or uncover new mathematics.

The published Theorem 3.5 requires a discretely valued base, full
geometric n-torsion over an unramified extension, and n prime to the
residue characteristic. Its extracted inequality is ambiguous, as already
recorded; the publisher's English and French abstracts explicitly include
the endpoint 3. This review relies on that published clarification and
does not claim a new visual reading of the scan. Definition 3.1 permits
a nonsplit torus. Milne II.6.3 states rank two over Z/mZ when m is prime
to the field characteristic; the relevant fields have characteristic zero.
No new specialization or independent proof is supplied in this turn.

The next audit must test complete local torsion at each completion,
using field characteristic zero, then level 5 at p!=5 and level 3 at
p=5, with the identity unramified extension. It must check that retention
uses the same field and curve, not normality or the original level-30
curve. Continue only if every hypothesis matches; record a failed case
rather than enlarge G. L078's inherited construction is an input, not
a request to reaudit all its ancestors in this bounded step.

ATTEMPTS/033–034 concern classification retrieval and the cyclic normality
separator, respectively, and do not block this independent audit. Their
stops remain intact. Full matching and supporting Mathlib coverage is
not checked; no absence claim is made. This is approval of reused known
coverage, not a correctness verdict or evidence beyond those sources.
The outcome is STALLED because the approval repeats existing coverage.
No lemma, mathematical script, DAG or argument overview is changed.
