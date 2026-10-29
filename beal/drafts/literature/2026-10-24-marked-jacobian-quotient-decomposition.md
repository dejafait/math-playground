# Marked Jacobian quotient decomposition — source assessment

TARGET: Determine whether the existing L110 and L111 quotient maps give a Q-isogeny decomposition of L113's Jacobian, and certify the exact rank relation if they do.
CHECKED: 2026-10-24
DECISION: IMPORT
SEARCH_EVIDENCE: Compared L110–L113, the prior split-cover/model assessments and ATTEMPTS/050–052; searched double-cover Jacobian decomposition, Kani–Rosen terminology and exact coefficient variants; inspected the primary passages below.
SOURCE_EVIDENCE: Bruin arXiv:math/0408069v2 Section 2.2, Proposition 2.2 and proof, manuscript pp.4–5; Docking arXiv:2108.09564v2 Section 2/Table 1 Case II p.4, Lemma 4.1/proof p.6 and Lemma 5.3/proof p.8; Milne Abelian Varieties v2.00, Chapter I Proposition 7.1 and Theorems 7.2/16.7, printed pp.32–34/69.
COMPARISON: The split-cover Prym identification and base-Jacobian/Prym isogeny cover the structural target; L111 already supplies the exact constants, projections and elliptic origin. Their applicability and transport through L113 remain to be written canonically.
GAP: Import the cited results for the existing Q-models and maps, justify the connected unramified-cover hypotheses and actual marked twist, and record the induced rank equality; no quotient upper rank is supplied.
REASON: Essential source coverage is accessible and ready for one known-result application; no new decomposition theorem or computation is warranted.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked theorem-level coverage of the Prym isogeny and finite kernel; prior ready assessments covered curve construction only.
SCOPE: Exactly TARGET using L110, L111 and L113; L112 and L126 constrain interpretation. No rank search, complete descent, new curve or point classification.

## Gap, downstream use and discriminating test

The main gap remains exclusion of every positive primitive integer
solution, including the residual exponent signatures. The intermediate
target could replace the marked genus-three rank problem by ranks of
its existing genus-two and elliptic quotients. Actual upper ranks and
point control are independent gaps; the structural identity alone
excludes no integer solution.

Continue with one canonical import if the existing maps fit the source
theorem over Q, with finite kernel, the actual marked twist and an
ordinary Mordell–Weil rank equality. Narrow or abandon this comparison
if those checks fail. A dimension count, rank parity, an isogeny only
over an extension or a changed twist does not pass. This turn approves
coverage; it does not certify a new instance decomposition.

## Primary theorem coverage

Nils Bruin, *The arithmetic of Prym varieties in genus 3*, Compositio
Math. **144** (2008), 317–338, DOI 10.1112/S0010437X07003314;
inspected [arXiv:math/0408069v2](https://arxiv.org/pdf/math/0408069v2),
31 May 2006, **Section 2.2, manuscript pp.4–5, Proposition 2.2 and
its complete proof**. For squarefree f=f1*f2 over K with even-degree
factors, the construction gives an unramified double cover

    y1²=f1(x), y2²=f2(x) → y²=f(x), y=y1*y2.

The factor-curve pullbacks identify their product of Jacobians with
the Prym. The proof checks vanishing cross norm and multiplication
by two after norm/pullback before its stronger isomorphism conclusion.
Only the abelian-variety identification is needed here; no claim about
the restriction of a principal polarization is imported.

Jordan Docking, *2-infinity-Selmer rank parities via the Prym
construction*, J. Number Theory **265** (2024), 208–225, DOI
10.1016/j.jnt.2024.06.009; inspected
[arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2),
24 July 2023, **Section 2/Table 1 Case II, manuscript p.4**.
For a connected unramified double cover pi:D→C over a number field,
with base genus two or three, it supplies the K-isogeny and comparison

    phi: Jac(C) × P → Jac(D), (x,y) ↦ pi^*x+y,
    psi: Jac(D) → Jac(C) × P, z ↦ (pi_*z,z−iota_*z),
    psi phi=[2], phi psi=[2], P=Prym(D/C).

The extra rational-point assumption concerns base genus three.
Case II gives the quadratic–quartic case, retaining twist ambiguity.
**Lemmas 4.1 and 5.3 with proofs, pp.6/8**, describe geometric
two-torsion and the finite kernel. Geometric kernel size is not its
number of Q-points. No parity theorem or finiteness of Sha is used.

J.S. Milne, *Abelian Varieties*, **v2.00, 16 March 2008**,
[author notes](https://www.jmilne.org/math/CourseNotes/AV.pdf),
**Chapter I Proposition 7.1/proof, printed p.32, Theorem 7.2/proof,
pp.33–34, and Theorem 16.7, p.69**. These give the finite-kernel
isogeny criterion, multiplication-by-n isogenies of degree n^(2 dim A),
and Mordell–Weil finite generation. The last statement refers to Serre
for its proof. They cover the ordinary-rank interpretation: apply the
comparison after tensoring rational-point groups with Q. Only this
necessary applicability argument is called for, not a general reproof
or a numerical rank calculation.

## Existing instance data and the approved application

In Bruin's notation take base C=B from L110 and cover D from L111;
L113 identifies this same D with its marked hyperelliptic model.
L111 already records and audits these assignments:

    a(T)=−3(T²−4), b(T)=−33Q4(T),
    Q4(T)=7+52T−6T²−64T³−25T⁴,
    y1=h, y2=R/3, f1=a, f2=b/9, y=W=hR/3.

These are quoted existing identities, not a factorization derived in
this turn. L111 proves simple disjoint branch sets, geometric
integrality and the degree-four compositum; L110 supplies the
squarefree sextic. Those are the relevant hypotheses of the connected
split-cover construction. Its unramified product projection must be
identified with the existing D→B, rather than confused with D→E.

The genus-zero factor h²=a has the recorded point (T,h)=(2,0).
The quartic factor is E under the existing Q-rescaling R↔R/3, with
recorded origin (2,165) in the R-coordinate. No square root of −3 is
adjoined. The import must explicitly use the two projections

    pi_B:(T,h,R)↦(T,hR/3), pi_E:(T,h,R)↦(T,R),

and transport them through L113's established smooth-proper Q-isomorphism

    T=2(t²−3)/(t²+3), h=−12t/(t²+3),
    R=3Y/(t²+3)².

No base point on B or descent of the original scalar s to E is needed
for Jacobians. Retain proper extensions rather than inferring maps
only on an affine open.

The requested canonical output is the imported sum-of-pullbacks
isogeny through these two projections and the target relation

    rank Jac(L113)(Q) = rank Jac(B)(Q) + rank E(Q).

This is the relation to certify in the research turn, not an instance
assertion proved in this assessment. Justify finite kernel using the
imported comparison; degree and complete kernel enumeration are not
required. Explain why the integral rational-point groups need not be
isomorphic. A new differential calculation or script would duplicate
the available theorem application. No independent Prym reproof is
warranted; write only the exact applicability argument canonically.

## Duplicates, failures and remaining obligations

The inspected L110–L113 statements and their quotient/model assessments
supply curve maps, but no canonical decomposition/rank assertion.
The new coverage is the explicit base/Prym isogeny and finite-kernel
comparison alongside the reused split-cover identification. This is
known coverage, not an originality claim.

ATTEMPTS/050 stops its fixed bounded genus-two detector, not all rank
methods. ATTEMPTS/051 and audited L112 rule out elliptic rank zero
without determining its exact rank. ATTEMPTS/052 preserves the
persistent S-class backend blocker. This target repeats none of those
searches or availability probes. L126's audited trivial rational
two-torsion gives no upper-rank bound and must not be confused with
geometric two-torsion. Unfinished L108 and all stop evidence are preserved.

Full supported arithmetic, quotient upper ranks, descent/Kummer
comparison and rational points remain open. Degree-nine recovery,
remaining factors, both L095 integer systems, minus-eleven and other
residual signatures are further obligations even if point control
succeeds. There is no complete Beal candidate.

## Search, primary statement and Mathlib

Queries included `"genus 3" "genus 2" "Jacobian" "isogenous"
"double cover" elliptic`, `"Kani Rosen" "V_4" Jacobian decomposition
hyperelliptic`, `"Jacobian" "825" "2112" "1716"`,
`"Prym" "275" "2860" "6930"`, and
`"Jacobian" "isogeny" "rank" "Mordell-Weil" Milne`.
No exact-instance match was identified among inspected results; failed
searches imply no novelty. Other hits on tangential covers, modular
curves and non-simple abelian varieties were not read as theorem inputs.
No Kani–Rosen theorem is used; the directly matching Prym sources suffice.

On 2026-10-24 the opening assertion of
[Mauldin's primary statement](https://sites.math.unt.edu/~mauldin/beal.html)
again specifies positive integer bases/exponents, exponents greater
than two and a common prime of all bases, matching the local target.
The nominated [AMS page](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize)
again returned HTTP 403; its current contents and prize rules were
not read. This does not block the unchanged geometric target.

Mathlib coverage of the complete Prym/decomposition result was not
checked; no absence or formal-verification claim is made. This
LITERATURE turn changes source readiness only, with no lemma,
mathematical script, DAG edge or main-argument change. The next turn
is the bounded known-result application under this IMPORT assessment.
