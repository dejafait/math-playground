# Equality map — determinant-line positivity source review

TARGET: Assess whether determinant line positivity for L097's finite common-H map yields an integral constraint on the full operator D without a universal sheaf.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched determinant line Gieseker semistable moduli ample Huybrechts Lehn 8.1.5/8.1.11 and Perego Rapagnetta 2012.10649; inspected the primary book's descent, surface positivity and GRR statements/proof cases, Abe's sign convention, and Stacks finite pullback. Local line-twist/jumping-cycle reviews and ATTEMPTS/064 do not duplicate this positive-line mechanism.
SOURCE_EVIDENCE: Huybrechts–Lehn (1997), Definitions 8.1.1/8.1.4/8.1.9, Theorem 8.1.5 and proof, Proposition 8.1.10, Theorem 8.1.11 and Remark 8.1.12(i), pp. 178–185; Section 8.3's GRR formula and Proposition 8.3.1(ii)/proof, pp. 195–197; Abe (2017), Section 10.1, pp. 151–152; Perego–Rapagnetta arXiv:2012.10649v1, Definition 1.3/Theorem 1.6, pp. 6/9; Stacks 30.17.2 (0B5V), statement and forward proof, inspected 2026-10-15. Direct sources: https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf ; https://doi.org/10.1017/nmj.2016.50 ; https://arxiv.org/pdf/2012.10649v1 ; https://stacks.math.columbia.edu/tag/0B5V .
COMPARISON: The general determinant construction descends suitable classes to the whole semistable space and supplies an ample combination on fixed-determinant surface moduli without primitivity, generic H or a universal sheaf. Its family pullback and GRR formulas are evaluable from the retained Chern data. The separate integral Mukai-isometry theorem still requires generic H and is not used.
GAP: Evaluate the two actual determinant pullbacks, retain their normalization and full divisor action, then determine whether the ample-combination condition excludes the retained D or merely repeats compatible positivity. No pullback, degree, cone constraint or exclusion is computed in this literature turn.
REASON: Essential coverage is now available for one bounded determinant-line calculation at the actual common H. Import the general theorems without reproof; approve only the explicit family specialization and compatibility test in a separate continuation assessment.
LITERATURE_REASON: The exact next target changes from the stable-gerbe pullback to descended determinant-line positivity on the whole projective moduli space, including its nonprimitive vector and common-H polarization; existing assessments do not cover those essential hypotheses.
SCOPE: L071/L093's hypothetical locally free rank-two Omega-polystable F with c_1=0 and full ch_2=-14e_1-21e_2-tau_D, identical marked K3 metrics, L096's finite possibly empty Z, L097's common H with H.k=0, and L098's finite map f:B -> M_H^{ss}(2,0,-12). L099's rank-four normalization is optional context, not a positivity hypothesis.

The main gap is universal primitive rational Hodge realization.
The intermediate target is feasibility of an integral projective
positivity test for this particular conditional equality kernel. Its
plausible downstream use is an additional necessary constraint on
the mixed operator or an obstruction to this kernel. Other correction
pairs, representatives, cycle transport and the universal target would
remain unresolved even after an exclusion.

The source-feasibility threshold is met: a named descended positive
combination and an actual-family formula are available. Whether their
specialization discriminates against this D is still untested. Continue
for one calculation; park this filter if the constraint is compatible
or depends on unavailable inputs. This is not approval of a calculation
performed in the present turn. No cross-notebook input is used.

## Inspected primary results

[Huybrechts–Lehn, *The Geometry of Moduli Spaces of Sheaves*,
Aspects of Mathematics E31 (1997), Chapter 8](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=190):
write b=[O_H] in K(S_1), c for the fibre's numerical K-class,
K_c=c-perp and K_{c,H}=c-perp intersect {1,b,b^2}-perp-perp,
using the Euler pairing. Theorem 8.1.5 gives
f_F^*lambda(u)=det Rp_2*(F tensor p_1^*u) for u in K_{c,H}.
Its proof checks stabilizers of every polystable object and descends
along a frame bundle; it does not require a universal sheaf on M.

Definition 8.1.9 uses u_i=-r b^i+chi(c b^i)[O_x] and
L_i=lambda(u_i). Theorem 8.1.11, Proposition 8.1.10 and
Remark 8.1.12(i) make L_0 tensor L_1^ell ample for ell sufficiently
large on each fixed-determinant surface moduli fibre. No primitive
vector or generic polarization is assumed.

Section 8.3 states GRR for the K-theoretic pushforward of any class
on the product. Proposition 8.3.1(ii) gives
c_1(lambda_F(u_1))=p_2*(Delta(F) p_1^*H)/2,
where Delta(F)=2r c_2(F)-(r-1)c_1(F)^2.
Its proof retains a possible base determinant term and cancels it
after fibre integration. These general inputs are imported, not reproved.

The scanned book's text extraction drops some minus signs. The
displayed u_i convention is also explicitly legible in [Takeshi Abe,
*Semistable sheaves with symmetric c_1 on a quadric surface*,
Nagoya Math. J. 227 (2017), 86–159, Section 10.1, pp. 151–152,
doi:10.1017/nmj.2016.50](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E99CFB15879252A08B4D71D09ACEA734/S0027763016000507a.pdf/semistable-sheaves-with-symmetric-c1-on-a-quadric-surface.pdf#page=67).
Only its transcription of the determinant convention is used;
its quadric-specific cone and symmetric-class results are not K3 inputs.
In particular this is the determinant of the alternating pushforward,
not its dual or the determinant of a single cohomology sheaf.

[Stacks, Lemma 30.17.2, 0B5V](https://stacks.math.columbia.edu/tag/0B5V),
for finite surjective maps between schemes proper over a Noetherian
ring, preserves ampleness under pullback (and gives the converse).
The forward proof uses finite implies affine and pullback by a
quasi-affine morphism. Apply this to L098's factor onto its reduced
projective image, after restricting an ample moduli line to that image.
Surjectivity onto the entire moduli space is not an assumption.

[Perego–Rapagnetta, *The second integral cohomology of moduli spaces
of sheaves on K3 and Abelian surfaces*, arXiv:2012.10649v1,
19 December 2020](https://arxiv.org/pdf/2012.10649v1#page=6),
Definition 1.3, p. 6, defines an (m,k)-triple using primitive,
v-generic H, v=mw with w primitive and w^2=2k>0, and an
additional condition in the rank-zero, higher-Picard case. Theorem
1.6(1), p. 9, supplies the integral Hodge isometry under that scope.
L097 supplies no generic H, and its chosen very ample multiple need
not be primitive. No application of this theorem is asserted. Its
full proof is unnecessary for this failed hypothesis match.

## Applicability and retained limitations

L097 already gives a smooth projective K3, a very ample integral H,
a fixed numerical class of positive rank and the actual flat family
on S_1 x B. These are the general determinant theorem's inputs.
The integral c_1=0 fixes the fibre determinant O on the K3; this
does not impose a new condition on the hypothetical family.
Descent on the whole semistable space includes Z even if it is
nonempty. Finiteness is L098's audited result. Neither L099's
normalization conclusion nor a comparison at a split metric germ
is needed for this source application.

The difference left for research is the full family-specific GRR
evaluation, including L_0, and its comparison with the actual ample
cone as H ranges over the permitted common stratum. A positive
holomorphic eigenvalue alone is not this test. Do not presume that
L_1 is ample on the whole Gieseker space; use the stated ample
combination. GRR supplies rational cohomology identities; any integral
identification must separately retain the actual line and the K3's
torsion-free H^2 and Picard injection. Do not infer all of D from
one tested divisor, or introduce a new polarization changing the
family's semistability. No new mathematical specialization is proved here.

The main-gap relevance is conditional: a failed positivity condition
could obstruct this equality kernel, while compatibility would stop
this bounded filter. F existence, other corrections/representatives,
transverse transport and universal primitive Hodge realization would
remain unresolved. The new calculation assessment is
[the separate continuation](2026-10-15-equality-determinant-pullback-test.md)
and requires the supervisor's separate approval next turn.

## Duplicates, search boundary and Mathlib

The retained line-twist assessment and jumping-cycle assessment of
2026-10-12 concern concentration and effectivity of a different
virtual complex; neither supplies these descended positive lines.
ATTEMPTS/064 stops an independently evaluated gerbe pullback, not
determinant descent. The earlier analytic and prescribed-product-jet
stops remain intact. No source claims the Hodge conjecture or
excludes this F; no novelty is inferred from the bounded search.

Queries used the theorem numbers above, determinant/Gieseker/ample
terminology, the exact Perego–Rapagnetta identifier, and finite
pullback ampleness. Primary theorem statements and the indicated
descent/positivity/GRR proof cases were read. Stacks 02UO was also
inspected: its displayed version assumes locally free higher direct
images, which must not be silently imposed here. The book's
K-theoretic GRR statement avoids that extra condition. An additional
Fulton search returned leads; no unseen Fulton theorem is used.
Shell download of the book failed at DNS; the web-accessible primary
book text supplied the inspected ranges. This is not a source blocker.
Full matching Mathlib coverage is not checked; no absence is claimed.
