# Marked-octic five-adic point image — source approval

TARGET: Determine the exact five-adic fake two-cover point image of L113's marked octic in L114's scalar quotient, retaining every factor and both infinity points.
CHECKED: 2026-10-23
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched marked-octic assessments for finite-local images, LocalImage and SquareClasses, and checked ATTEMPTS/050–052 and history/417; no duplicate instance image was found. Web queries were Bruin Stoll two cover descent hyperelliptic curves local image algorithm nonmonic bad reduction 0803.2052; "275" "2860" "6930" hyperelliptic; "Two-cover descent" "LocalImage" "errata"; "Bruin" "Stoll" "Lemma 4.4" square; and "3025" "31460" "76230" curve. Exact-coefficient queries returned irrelevant hits; no novelty conclusion follows.
SOURCE_EVIDENCE: Directly read Bruin–Stoll arXiv:0803.2052v2 (21 October 2008), Section 4 opening p.6, nonunit-leading/bad-discriminant discussion, polynomial valuation and Lemma 4.4 with complete proof p.8, SquareClasses and every explanation pp.9–10, and LocalImage and every explanation pp.10–11; rechecked Section 2 p.3 and reused assessed support coverage. The author resource index was accessible; its code link failed, and neither code nor the inaccessible alternate PDF is essential to this proof-based approval.
COMPARISON: Section 4 already gives an exact finite-local image algorithm for integral squarefree polynomials without monicity, good reduction or a Newton-polygon restriction. The remaining work is its certified instance execution and common-scalar/norm bookkeeping for L113's unchanged octic; the source does not provide that instance image or its ambient comparison.
GAP: Complete exact local algebra models and square-class labels, terminating coverage of both coordinate charts, realizations, all exceptional evaluations and the norm-admissible scalar-quotient comparison remain uncomputed; general source coverage is now sufficient.
REASON: Approve one later mathematical specialization of the inspected known method; do not reprove its general algorithm or infer a five-adic image from the support theorem.
LITERATURE_REASON: Startup REVIEW_REQUIRED named essential unread finite-local algorithm hypotheses and proof cases, outside the ready support and real-image assessments; this turn fills exactly that coverage gap.
SCOPE: Exactly TARGET for L113's smooth proper curve, L114's actual even-degree quotient, and the entire five-adic algebra; includes exact local factor/model certification, square/norm labels, exhaustive affine/reciprocal disk tests and realization certificates. No supported global class enumeration, rational-point completeness or other finite place is approved.

## Primary result and hypotheses

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. **78** (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8).
All page and algorithm references below use the inspected primary
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008, not inferred journal pagination.

Section 4 p.6 takes a complete discretely valued characteristic-zero
field k with finite residue field, integer ring O and uniformizer pi,
an integral squarefree polynomial f, and its complete irreducible
factorization over k. It works in every factor L_i=k[x]/(g_i) of
A=k[x]/(f). The discussion p.8 expressly includes a nonunit leading
coefficient, discriminant valuation greater than one, a small residue
field and residue characteristic two. These are reasons to compute,
not exclusions from the recursive method. The unit-leading and small
discriminant hypotheses of Lemma 4.3 must not be used to shortcut five.

Section 2 p.3 fixes the even-degree target

    H_k={delta in A*/(A*² k*): N(delta) in f_n k*²}.

For ordinary affine points use [x−theta]. For a rational branch a,
write f=(x−a)f_tilde and use [(a−theta)+f_tilde(theta)], an invertible
element. For square leading coefficient both distinct infinity points
have class [f_n]=[1]. These definitions are imported, not newly derived.

## Complete algorithm cases inspected

This records source coverage and the evidence a later specialization
must retain; it is not an execution or a new lemma.

- Lemma 4.4 p.8 uses the coefficient-minimum valuation on O[epsilon].
  If g is irreducible and
  ord(g(x0+epsilon*pi^e)−g(x0))>ord(g(x0)), then for
  x1 in x0+pi^(e+ord(4))O the product
  (x0−theta)(x1−theta) is a square in k[theta]. Its complete proof
  passes from g's norm expression to closeness to one in that field,
  then uses the stated square neighborhood. It permits ramified fields
  and nonintegral theta. Record these polynomial coefficient bounds,
  not sampled changes of g on residues. No optimality claim for the
  resulting sufficient disk precision is required.
- SquareClasses pp.9–10 splits each disk into all residue children.
  Steps 3–4 reject disks only when f cannot be square to the certified
  precision; step 5 retains factors not yet meeting the strict bound.
  Explanations ad 6–8 give termination and the extra ord(4) precision
  counter. At five ord(4)=0; use that odd-residue case with actual
  bounds, rather than an unsupported universal depth.
- Explanation ad 8 p.10 separates both terminal cases. With no unresolved
  factor, all points in the disk have the recorded component classes
  and the surviving square test supplies an actual point at the center.
  With one unresolved linear factor, every feasible point has the
  already inserted branch class. Explanation ad 11 requires refinement
  otherwise and explains termination. Thus the source gives containment
  and realization. Unclosed disks cannot certify an exact image.
- LocalImage pp.10–11 initializes every rational branch image, runs the
  integral chart on O, then the reciprocal chart on pi O. For even
  degree it uses the reversed polynomial and the map
  q -> q(1−q theta) modulo squares, with q=1/x. Steps 10–11 insert the
  infinity identity and add an auxiliary q factor to prevent evaluating
  that affine expression at q=0. Explanation ad 12 establishes complete
  coverage by these two charts and the exceptional rows.
- LocalImage explanation ad 2 p.10 computes first in A*/A*²; the actual
  even-degree image is its projection modulo one common k* scalar.
  Retain quotient collisions. There is no permission to quotient factors
  by independent scalars or assume subgroup closure of the point image.

The primary proof and algorithm explanations suffice; their earlier
implementation reference is not an essential unread input. The
[author's resource index](https://www.cecm.sfu.ca/~nbruin/twocovdesc/)
lists Magma code, but its code link failed retrieval. An alternate
author PDF also failed retrieval, and a shell PDF download failed DNS
(curl exit 6). These do not block the arXiv text actually inspected.
No implementation execution or software correctness is imported.
Searches did not identify an erratum; that does not certify its absence.

## Applicability and bounded research contract

The main gap remains global rational/integer point control sufficient
for residual Beal exclusions. The intermediate target is the exact
five-adic fake point image. Its plausible downstream use is a membership
test on later supported representatives, alongside L118's audited real
filter; independent global gaps need not be solved first.

Use precisely L113's model

    G(t)=3025t^8−31460t^6+76230t^4−39204t^2+2673.

L113 supplies squarefreeness and smooth proper charts; L114 fixes the
map, norm fiber, discriminant and two infinity rows. These inputs meet
the integral squarefree characteristic-zero hypotheses with k=Q5.
Its nonunit leading coefficient and bad polynomial reduction are
expressly within Section 4's scope. Do not replace the curve by Y²=G/11.
L115's rational irreducibility does not identify the five-adic algebra
as one field. If used, L116's maximal ring and L117's complete five-prime
data must be transported to actual local models with certified
factorization and the same theta in every evaluation; residue degrees
alone are not local field models or square-class maps. Those existing
data may be independently rechecked as needed.

Retain every local field factor and scalar embedding. Certify complete
square-class equality tests and norm labels before comparing sets in
L114's quotient. Execute or rigorously compress both source chart
searches, recording each rejected disk's obstruction, each terminating
disk's sufficient precision and realization, any rational branch points,
both separate infinity rows and all quotient collisions. Exact Hensel
realizations and cited constant-class bounds must replace precision
guesses. An equivalent disk organization requires explicit exhaustive
coverage and justified bounds; citing pseudocode is not its execution.

Compare the exact image with the complete norm-admissible ambient set
in that same scalar quotient. Strictness supports this local filter;
ambient equality stops extra pruning at five. Missing factors,
unrealized labels, unclosed disks or a computation cap leave the image
unresolved. Neither an ambient size nor an image size is asserted here.

## Reuse, limits and decision

Reuse the support and real-image assessments within their scopes;
neither supplies this finite image. Scoped searches found no duplicate
marked-octic finite-image result. Failed coefficient searches do not
establish novelty; the general method is already known. SPECIALIZE
authorizes REPRODUCTION of an instance, not a new general theorem.

ATTEMPTS/052 parks global class-backend execution, independently of this
finite residue/disk target. Do not repeat backend probes. Preserve
ATTEMPTS/050–051 and unfinished L108. Supported units, ordinary S-class
two-torsion, other finite images, points on surviving covers, degree-nine
root recovery, remaining factors, both L095 systems and minus-eleven
remain unresolved. Known rational infinity points preclude an empty
fake-Selmer-set shortcut. No global class is shown removed here.
Mathlib coverage of the full finite-local algorithm is not checked;
no absence claim is made. No cross-notebook input is used.

This literature-only step derives no new instance result and changes
no lemma, mathematical script, argument assembly or DAG. The unchanged
TARGET is ready for a separate mathematical invocation.
