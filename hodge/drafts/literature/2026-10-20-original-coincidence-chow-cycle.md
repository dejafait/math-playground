# Original opposite coincidences — completed Chow source comparison

TARGET: Assess whether Fulton's residual formula and Beauville–Voisin's K3 zero-cycle theorem force the original ordered-coincidence source cycle to be a multiple of the canonical zero-cycle.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Inspected L140 and its saved projection assessments and narrowly searched named failures; exact-statement and stronger-result searches retrieved published Beauville–Voisin and Fulton 1978, but no theorem separately controlling the original projected-residual subcycle.
SOURCE_EVIDENCE: Beauville–Voisin, J. Algebraic Geom. 13 (2004), Theorem 1, Section 2.1, Proposition 2.6(b), Proposition 3.2, Corollary 3.3 and Section 3.4; Fulton 1978 Theorem 2 and Remarks 2.1–2.5; reuse saved Intersection Theory Theorem 9.3 coverage.
COMPARISON: Beauville–Voisin covers divisor products and the tangent second Chern class; its stronger diagonal identity retains slice terms. Fulton controls the entire residual of the chosen auxiliary map, without isolating the original coincidence subcycle.
GAP: Separate Chow control of the auxiliary contribution, including possible excess length at original pairs, is missing; neither the desired original-cycle conclusion nor a counterexample is established.
REASON: Park the original-cycle inference: the inspected sources do not isolate its contribution. EXPLORE records bounded search coverage, without authorizing the missing assertion or a new lemma repackaging whole-residual control.
LITERATURE_REASON: New target changes numerical degree control to rational equivalence of the original source zero-cycle and requires the unread primary Beauville–Voisin theorem and a comparison retaining the auxiliary residual.

The initial registration below is retained; the completed comparison follows it.
No new Chow identity is derived in this literature-only step.

Retain the full hypothetical L071/L118 assumptions: identical marked
projective K3 factors and common metric, actual holomorphic locally free
Omega-polystable rank-two F with integral c_1=0 and
ch_2=-14e_1-21e_2-tau_D, with the unchanged full tensor.
The essential existing inputs are L120's normalization, L121's original
finite reduced ordered coincidence scheme, L137's fixed projective
embedding and L140's auxiliary projection and residual formula.
L141 is the completed numerical comparison, not a Chow-theoretic input.

The object to be assessed is the first-source pushforward of the
fundamental zero-cycle of the **original** R_off on B, with both orders
retained. Include the empty case. The question asks whether it lies in
the span of the canonical K3 zero-cycle in CH_0(B) with rational
coefficients. It must not be silently replaced by the source cycle of
the whole auxiliary projected residual.

The precise new idea is to inspect the cycle-valued information before
L140 takes degrees, using the K3 zero-cycle theorem for the relevant
intersection/Chern terms. The discriminating issue is the separate
auxiliary contribution. A source review must retrieve the exact primary
hypotheses and relevant proof cases, check known stronger results and
duplicates, and distinguish any established whole-residual identity
from the desired original-cycle statement. No general intersection
theory or K3 theorem needs reproof.

A constraint on the locations of actual coincidences up to rational
equivalence could provide an independent obstruction test using the
family correspondence, beyond the now-audited upper counts. That
downstream incompatibility is not known; neither collision existence nor
a lower bound nor a contradiction is assumed. Universal primitive
Hodge realization and existence of F remain separate unresolved gaps.

Continue to a separately approved mathematical specialization only if
the sources give a concrete way to control or test the auxiliary
contribution. If they constrain only the entire residual and supply no
such control, record that limitation and park this original-cycle
inference rather than treating the total as the original. Do not merely
sharpen numerical bounds again. ATTEMPTS/070,073,078 stay preserved:
minimal gluing, automatic coherent vanishing and an uncontrolled
middle-Hom Euler term are not reopened. Full matching Mathlib coverage
is not checked.

## Completed primary comparison — step 444

The main gap remains universal primitive rational Hodge realization;
existence of the fixed equality kernel F is independently unresolved.
The reviewed intermediate target is the original ordered-coincidence
source cycle, retaining both orders and the empty case. A canonical-class
constraint could support a later obstruction through the actual family
correspondence, but no downstream incompatibility is known. The stated
continuation test was separate auxiliary-contribution control. That test
is not met by the sources inspected.

**Primary theorem.** The published author-hosted version of
[A. Beauville and C. Voisin, On the Chow ring of a K3 surface,
J. Algebraic Geom. 13 (2004), 417–426](https://math.univ-cotedazur.fr/u/beauvill/pubs/bv.pdf)
was inspected. Theorem 1, p. 417, gives a degree-one class c_B for points
on rational curves, puts divisor products in Z c_B, and states
c_2(T_B)=24c_B. The setting is complex algebraic K3 surfaces. Section
2.1, pp. 418–419, uses rational curves and Bogomolov–Mumford; it does
not identify arbitrary point classes. The theorem imposes no Picard-rank-one
hypothesis.

Also read Proposition 2.6(b), pp. 419–420, Proposition 3.2 and Corollary
3.3, p. 420, and its proof in Section 3.4, p. 421. For a codimension-two
cycle xi on B x B, the corollary expresses Delta^*xi as i_c^*xi+j_c^*xi
plus a degree-adjusting multiple of c_B, with i_c(x)=(x,c), j_c(x)=(c,x).
The proof pushes the small-diagonal identity against xi. Both slice
restrictions remain; this is not a canonical-class assertion for every
zero-cycle.

The earlier ten-page [author manuscript](https://www.cmls.polytechnique.fr/~voisin/Articlesweb/Chowams.pdf)
was read first; numbering was checked against the published text.
[arXiv:math/0111146v1](https://arxiv.org/abs/math/0111146v1), submitted
13 November 2001, supersedes the earlier single-author preprint. The
latter is not a substitute for the proved two-author c_2 theorem.

**Residual coverage.** Reuse the saved book assessment in
`2026-10-20-opposite-projection-double-point-bound.md`: Fulton,
Intersection Theory, second edition, Theorem 9.3 and proof, pp. 165–167.
Also inspected [Fulton, Acta Math. 140 (1978), 93–101](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6234-11511_2006_Article_BF02392305.pdf),
Theorem 2, p. 94, and Remarks 2.1–2.5, pp. 95–96. For a smooth-source
map X^n -> Y^m between nonsingular varieties, its blowup residual must
have codimension m. Its first-source cycle is
f^*f_*[X]-c_(m-n)(f^*T_Y-T_X) cap [X]. The formula concerns the entire
residual of that map. Remark 2.4 distinguishes ordered triple-point
contributions from the conductor, and Remark 2.5 requires the residual
dimension check. These qualifications survive singularity of the image.

**Comparison with the actual target.** L140 checks smoothness and the
finite residual for its auxiliary map a:B -> P^4 and identifies that
residual with S_off. Its intersection and tangent-Chern terms fall within
the types of inputs covered by Theorem 1. A whole-cycle specialization
would require only applicability and substitution, without reproving
either theorem; no such new specialization is performed here.

That formula still concerns S_off. L140 proves a closed immersion of
reduced R_off into it, and only a lower estimate on the local length at
each original pair. Separate contribution control must therefore cover
both newly supported pairs and possible excess length at old support.
Theorem 1 supplies no separate statement for an effective subcycle of
this residual. Corollary 3.3 neither kills its slice terms nor localizes
the residual to R_off; no identification of R_off with a covered diagonal
restriction has been supplied. A degree estimate is not a rational-equivalence
statement. This is a limitation of the source inference, not a disproof
of the desired original-cycle statement or a counterexample to it.

**Bounded searches and local duplicates.** Queries were “Beauville
Voisin Chow ring K3 surface 2004 theorem 1 zero cycle pdf”, “Beauville
Voisin double point zero cycle immersion K3 surface projection Chow”,
“K3 surface double point cycle projection Beauville Voisin zero cycles”,
“K3 immersion self intersection points canonical zero cycle Beauville
Voisin”, and “Beauville Voisin double points residual intersection
canonical zero cycle”. Exact bibliographic searching located the
published primary text. No adequate separate-component theorem was
identified. This is no novelty or theorem-nonexistence claim. Results
on elliptic-curve singularities and constant-cycle curves remained
unread leads, not coverage for this finite family scheme.

The local check was restricted to L140, its two projection assessments,
histories 436/439, the supplied registration and targeted failure searches
in ATTEMPTS/070,073,078. L140's degree-only disclaimer is preserved.
No minimal-gluing equality, coherent vanishing or middle-Hom Euler bound
is reopened. Full matching Mathlib coverage is not checked.

**Route decision.** Park the original-cycle inference. Reopening requires
a specific theorem or independently discriminating geometric test of
the separate contribution. Do not merely derive the total residual's
canonical class or repeat numerical upper bounds. No justified dependent
mathematical continuation was found; a bounded discovery/source screen
for an independent equality-kernel obstruction is registered separately.
No lemma, mathematical script, DAG edge or PROOF.md argument is changed.
