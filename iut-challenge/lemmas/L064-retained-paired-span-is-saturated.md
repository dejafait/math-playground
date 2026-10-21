# L064 — The retained paired logarithm span is saturated

## Hypotheses

Retain L063's actual field N=Q_3(zeta_420,3^(1/7)), with degree
168, e=14 and f=12, its full admitted Kondo presentation, and its
single reciprocal identification. Retain its unchanged field inputs
L042,L045,L048, curve, places, markings and qualifications. Put
R=Z_3, O=O_N, U_1=1+m_N, J=log(O^times). Write u_i for the
reciprocal image of x_i in O^times and y_i=log(u_i), 0<=i<=168.
These are the reconstructed additive images under precisely L063's
identification, not chosen field-coordinate vectors. Keep all unit
torsion until applying log.

## Conclusion

The actual integral submodule

    W_J = sum_(i=3)^168 R y_i

is free of rank 166 and a saturated direct summand of J. More
precisely J/W_J is free of rank two. There is some z in
R y_0+R y_1 for which z,y_2,y_3,...,y_168 is an R-basis of J;
no particular z or field coordinates are prescribed.

This is a REPRODUCTION/specialization of the cited presentation,
reciprocity and PID-module method. It is local integral progress,
not a result claimed beyond the checked literature. It establishes
no subgroup irreducibility, field radius, actual native input/action,
pilot transport, sufficient initial data or original finite B>=A.
The separate critical audit of 2026-10-16 validates this specialization
with the presentation-category check expanded below.

## Proof

**Imported structural inputs.** Use Kondo, *Anabelian aspects of the
outer automorphism groups of the absolute Galois groups of
mixed-characteristic local fields*, arXiv:2512.09231v2, 12 December
2025, section 1, [Theorem 1.1(1–4)](https://arxiv.org/html/2512.09231v2#S1).
It supplies L063's full presentation, wild normal topological
generation, and the admitted word x'_0 supported on tau,x_0. Odd
p=3 and even degree 168 satisfy its hypotheses. The relation is
exactly L063's; no parameters from another presentation are used.
The pro-p wild-normal-subgroup condition is part of this input:
Jannsen–Wingberg, *Die Struktur der absoluten Galoisgruppe
p-adischer Zahlkorper*, Invent. Math. 70 (1982), 71–98,
[section 1.2, pp.74–75; Theorem 2, p.75; section 1.4(a), p.76](https://epub.uni-regensburg.de/26689/1/jannsen17.pdf).

Use Hoshi, *Introduction to Mono-anabelian Geometry*, PMB (2021),
5–44, DOI 10.5802/pmb.42,
[Lemma 1.2(i,ii,iv,v), p.11; Lemma 1.5(ii), pp.13–14;
Lemma 1.7(i), p.15; Definition 3.10 and Proposition 3.11(i,iv),
pp.21–22](https://www.numdam.org/item/10.5802/pmb.42.pdf).
These give unit structure, local reciprocity, the tame inertia
quotient and the reconstructed logarithm identification. In
particular log has exactly the full unit torsion as kernel. L063
already checks the common reciprocal normalization and identifies
J as a full free rank-168 R-lattice, with its usual scalar structure.
The integral-generation argument in Hoshi–Nishio, revised June
2022 RIMS1931, [Lemma 1.3 and proof, PDF p.5](https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1931revised.pdf),
is a method precedent; its differently parametrized relator and
its rational basis do not supply an integral basis here. Only the
remaining integral specialization is proved below. The ordinary
structure theorem for finitely generated modules over the PID R is used.

**Full closed abelian pro-3 relation module.** Let A be the maximal
abelian pro-3 quotient of G_N. Use additive symbols S,T,X_0,...,X_168
for the admitted generators. The tame relation gives
(3^12-1)T=0, so T=0 since 3^12-1 is an R-unit. Abelianizing the
fixed defining word x'_0 gives aT+bX_0 for some a,b in R: its
support is confined to the admitted tau,x_0 word. These coefficients
are obtained from that presenting word in the free abelian pro-3
module, before imposing the relators; an arbitrary expression for
an element of the already presented group is not substituted.
Commutators vanish and conjugation contributes no S term. Thus,
with c=1-tb,

    A = (R S direct-sum direct-sum_(i=0)^168 R X_i)
        / R(cX_0-3^s X_1).                              (1)

Here and below these identifications send the symbols to the
actual generator images. The relation span is closed because it
is the image of compact R; it has not been saturated. To check
that (1) has no extra relations, take any finite abelian 3-group D.
Any assignment of S,X_0,...,X_168 into D satisfying
cX_0=3^sX_1, with T=0, satisfies both defining relators. The
required wild normal image is a subgroup of the finite 3-group D,
so satisfies the pro-3 condition as well. The full admitted
presentation supplies a continuous homomorphism G_N -> D with
those images. Conversely every such homomorphism obeys these
conditions. Finite abelian 3-quotients separate points in the
compact R-module in (1), so its natural surjection to A is
injective. This also checks the presentation's pro-3 condition;
one is not treating an arbitrary relator-preserving assignment as
a Galois automorphism.

More explicitly, the free construction of Jannsen–Wingberg section
1.2 starts with the free profinite product of the free profinite
group on the x_i and the tame group. The specified S and T=0 define a map from
the tame group to D: sigma is unrestricted and its tame relation
holds. The free product therefore maps continuously to D. Its
wild normal subgroup maps to a 3-group, so the kernel of its
maximal pro-3 quotient is killed. The remaining defining relator
maps to zero by cX_0=3^sX_1. Hence the map descends through both
quotients. This uses the construction itself, not a requirement
that D retain an embedded copy of the tame group in the fixed-base
category. To make separation explicit, denote the right side of
(1) by C. For each n>=1, C/3^n C is a finite abelian 3-group,
and the resulting map A -> C/3^n C composed with C -> A is the
canonical projection, since it agrees on every generator. The
finitely generated R-module C has intersection_n 3^n C=0 by
the PID structure theorem. Thus the kernel of C -> A is zero.

Set E=R X_0 direct-sum R X_1, v=cX_0-3^sX_1,
and W=direct-sum_(i=3)^168 R X_i. Then (1) is the actual
direct decomposition

    A = R S direct-sum B,
    B = (E/Rv) direct-sum R X_2 direct-sum W.            (2)

The subgroup B is the closed span of all X_i, 0<=i<=168.
All sums here are finite sums of compact R-modules.

**Identify B with the actual principal units, before log.** The
standard unit decomposition and reciprocity identify

    A = (N^times)^(pro-3) = R direct-sum U_1.

For this statement choose any uniformizer. The valuation factor
completes to R; residue units lift to the roots of unity of order
3^12-1 and die in pro-3 completion. U_1 is compact pro-3 and
embeds unchanged. Its principal-unit filtration has finite
3-group quotients and trivial intersection. This decomposition
does not identify S with any chosen uniformizer.

Let P be wild inertia, I_N inertia, and V its reciprocal image
from P in O^times. The reciprocity image of I_N is O^times.
Compactness makes V closed, and its pro-3 property places it in
U_1. The quotient O^times/V is a continuous quotient of I_N/P,
which has only prime-to-3 finite quotients by the cited tame
inertia description. The image of U_1 in O^times/V is pro-3
and must therefore be trivial. Indeed its image in each finite
quotient of the ambient profinite group has order both a power
of 3 and prime to 3, hence is trivial; those quotients separate
points of the ambient group. Hence
V=U_1, including all its 3-primary torsion.

Normal topological generation of P by x_0,...,x_168 becomes
topological generation of its abelian image by the u_i, because
conjugates have identical images in A. Thus B in (2) is exactly
the embedded U_1 in A. There is no loss of unit torsion on
passing to A: reciprocity's projection from the profinite completion
of N^times to its pro-3 part is injective on U_1, as the displayed
unit decomposition shows. This compares the same generator images
in the full abelian group and in A, rather than two abstractly
isomorphic modules. Ordinary R-generation equals closed generation:
the coefficient map from R^169 is continuous with compact,
hence closed, image containing the dense integer sums. In
particular (2) describes the genuine U_1, not a rationalized
or sampled unit subgroup.

**Take precisely the genuine torsion quotient.** Since s>=1,
v is nonzero. Put

    k=min(v_3(c),s),     v_3(0)=infinity,
    v_0=3^(-k)v in E.

At least one coordinate of v_0 is a unit. Thus v_0 extends to
an R-basis v_0,z_0 of E. Consequently

    E/Rv = (R v_0 / 3^k R v_0) direct-sum R z_0.

In particular its torsion submodule is exactly Rv_0/Rv;
the other summands of B have none. Under B=U_1 this is the
entire torsion subgroup mu(N) intersect U_1, with no assumption
on its exact order. In fact k>=1: L063's retained primitive
third root lies in U_1 and gives nonzero torsion. Thus c is
not a unit, demonstrating why the old torsion-free elimination
cannot be used. No value of k is needed for saturation.

Every residue-unit direction is accounted for by the
prime-to-3 roots of unity. They have logarithm zero, so
log(U_1)=log(O^times)=J. Its kernel on U_1 is exactly the
torsion just determined. Using L063's continuity and scalar
compatibility gives an actual R-module isomorphism

    J = B / Tor_R(B)
      = (E/Rv_0) direct-sum R X_2 direct-sum W,          (3)

where each X_i maps to the actual y_i. The appearance of the
primitive relation in (3) is justified only now, after removing
the actual torsion; it was not imposed in (1).

The last summand in (3) maps injectively to W_J, making the
166 stated y_i independent. The quotient is
(E/Rv_0) direct-sum R X_2, free of rank two. This proves
saturation (the quotient has no R-torsion) and the direct-summand
claim. Taking z to be the logarithmic image of z_0 proves the
asserted basis. Compactness also makes W_J closed in J.

No full trace-kernel claim follows: the statement concerns only
the paired span, and it leaves its complementary field coordinates
unidentified. It neither transfers L024/L032's bases nor assumes
that an abstract integral action is an actual native permitted
action. Original finite B>=A and the independent bridges listed
in the conclusion remain open.

**Critical-audit verdict (2026-10-16).** The independent check passes
the full finite-quotient test, closed unsaturated relation span,
absence of an S-coordinate, embedded wild-unit equality, ordinary
integral generation and exact logarithm kernel. In the PID step,
v is nonzero even if c=0, since s is finite; primitive v_0 has a
free rank-one quotient in E. Thus torsion is confined to E/Rv
and cannot impose a further relation on X_2 or W after log.
There are 168-3+1=166 paired generators, leaving quotient rank
1+1=2. No conclusion is withdrawn and no torsion order, field
coordinate or trace-kernel identification is added. The audit
validates a known-method local input, not progress beyond the
sources checked or a complete candidate for the challenge.

## Mathlib

Full matching coverage for this presentation-defined saturated
submodule: **not checked**. Supporting coverage for the local-field
reciprocity/logarithm identification and for the PID torsion/direct
summand structure: **not checked**. These are not assertions of
absence. The primary structural theorems above are imported;
the displayed integral specialization is supplied in full.
