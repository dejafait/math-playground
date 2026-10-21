# L071 — The fixed degree-seven quotient over the full direction field

## Hypotheses

Use audited L067/L068/L070 for E/Q: y²+y=x³+x²−2x. In L067's
short coordinates the same curve is

\[
\mathcal E:\ Y^2=c(X)=X^3+aX+b,\qquad a=-3024,\quad b=46224.
\]

Let D=Q[Z]/h be L070's entire degree-eight direction field, with the
same ordered basis 1,Z,…,Z⁷. Let q(U)=U³+q₂U²+q₁U+q₀ in D[U]
be its full relative cubic, not a chosen root or a partial column cache.
The exact h and all four cubic coefficients are the complete `/h` and
`/cubic` values in `scripts/seven-torsion/compressed-249/direction.json`.
L070's mixed inverse identifies this presentation with the full
x-coordinate algebra, and its audited factorization is
q(U,z)=∏_{i=1}³(U−X_i), where L068 identifies X_i as the forward
short coordinate of [i]P. Thus over each geometric embedding of D the
three roots are precisely the inverse pairs of one order-seven subgroup.
No D-rational generator is assumed. L069 and all unfinished incidence
columns are excluded. No L026, rank, analytic-order or Selmer premise is used.

Full new coefficients, maps and inverses are saved in
`scripts/seven-torsion/quotient-254/quotient.json`. Polynomial arrays are
ascending in the free source X, with each coefficient an ascending
Z-array of length at most eight; trailing zero slots may be omitted.
All coefficient reductions are modulo the full h, never at one embedding.

## Conclusion

There is a D-defined separable degree-seven quotient isogeny

\[
\Phi:\mathcal E_D\longrightarrow\mathcal E',\qquad
\mathcal E':Y'^2=X'^3+a'X'+b',
\]

with kernel the indicated whole order-seven subgroup, including O.
Its complete short-coordinate maps are

\[
X'=\frac{N(X)}{q(X)^2},\qquad
Y'=Y\frac{M(X)}{q(X)^3},\qquad
\Phi^*\frac{dX'}{2Y'}=\frac{dX}{2Y}.
\]

Here put s₁=−q₂, s₂=s₁²−2q₁, s₃=s₁s₂−q₁s₁−3q₀, and define

\[
\begin{aligned}
t&=6s_2+6a,&w&=10s_3+6as_1+12b,\\
a'&=a-5t,&b'&=b-7w,\\
N&=(7X-2s_1)q^2-(6X^2+2a)q'q
       +4c(X)((q')^2-qq''),\\
M&=N'q-2Nq'.
\end{aligned}
\]

Every coefficient of a', b', N, M and both denominators is retained in
the certificate. Its target discriminant has an explicit inverse in D.
These are raw short models: no new minimal Neron model over D, long-model
target map, real-period comparison, dual isogeny or affine-line identification
is asserted. This is known-method reproduction; full fixed production,
independent replay and the separate critical audit below pass.

It supplies only a quotient input for a possible later descent construction.
Incidence/norm, functions, complete units/classes, local identifications and
bounds, Selmer containment, all other L026 premises, successful localization,
rational membership, divisible Sha and arbitrary-curve rank comparison
remain unresolved. It is not a BSD candidate.

## Proof

**Imported quotient theorem and formulas.** Import Vélu, *Isogénies entre
courbes elliptiques*, C. R. Acad. Sci. Paris Sér. A 273 (1971), A238–A241,
[Ghitza translation §§2–3, equations (7)–(13), Remarks 2–3, pp.2–4](https://aghitza.github.io/publications/translation-velu.pdf).
Equation (7) gives sums over all nonidentity kernel points; (8)–(11)
give the inverse-pair convention, Remark 2 gives normalized differential,
and Remark 3 gives descent for a separable conjugation-stable subgroup.
Also import Sutherland, MIT 18.783 Fall 2025,
[Lecture 5, Theorem 5.11 pp.5–6 and Theorem 5.15/Remarks 5.16–5.17 pp.7–8](https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf):
the smooth projective quotient exists for the stable subgroup, is an
isogeny with that kernel, and has the odd-order short-model formulas.
These are general theorem inputs, not rederived here. Characteristic
zero gives separability; L067 gives nonsingularity; L070 gives subgroup
stability over the entire D. Individual points need not be D-rational.

Shumow, *Isogenies of Elliptic Curves: A Computational Approach* (2009),
[§3.1 p.30 and Theorem 3.2.1 with proof pp.54–56](https://www.sagemath.org/files/thesis/shumow-thesis-2009.pdf),
provides the kernel-polynomial formulation under an existing separable
normalized isogeny. Existence is supplied by the preceding quotient
theorem. The text qualifications in the saved source comparison are
retained: the repeated exponent pattern and omitted initial X in one
proof line are not premises. The fixed maps are checked against Vélu's
full paired sums instead. No new general isogeny theorem is claimed.

**Full-field construction and independent paired replay.** Write u for
the class of U in K=D[U]/q. Its three geometric roots u_i correspond
to all three inverse pairs. The saved polynomials I,J of U-degree <3
satisfy, in the entire K,

\[
q'(u)I(u)=1,\qquad c(u)J(u)=1.
\]

The independent verifier multiplies each witness and reduces by the monic
q with all D coefficients retained. Consequently q is squarefree and
disjoint from c. Each u_i therefore has two distinct nonzero Y-values,
so none of the six kernel points is a two-torsion point. This checks
all components of K, not a selected point.

The producer uses the displayed polynomial formula for N and M. Its
independent verifier imports no producer arithmetic. It uses sparse
free-variable polynomials with coefficients in D and the old independent
rational-polynomial verifier solely for arithmetic in D. It computes
Tr_{K/D}(u^k), 0≤k≤9, as sums of the three diagonal entries of
multiplication by u^k on (1,u,u²), reducing each u^{k+j} modulo q.
Thus traces are evaluated on all three roots without a splitting field.
In particular Tr(1)=3. The independently obtained traces verify the
full saved a',b' against

\[
t=\operatorname{Tr}(6u^2+2a),\qquad
w=\operatorname{Tr}(10u^3+6au+4b).
\]

For the map check let

\[
A(X,u)=X^2+Xu+u^2+q_2(X+u)+q_1.
\]

The verifier first checks the entire free bivariate identity
(X−u)A+q(u)=q(X). In K[X], A=q(X)/(X−u). Vélu's paired x correction
for the points (u,±v), v²=c(u), is
(6u²+2a)/(X−u)+4c(u)/(X−u)². The full polynomial replay checks

\[
N=Xq^2+\operatorname{Tr}((6u^2+2a)Aq+4c(u)A^2).
\]

This is the whole three-pair sum, not a specialization of its free X.
It also checks the y sum separately. The secant addition law, summed
over both v signs and divided by Y in the function field, gives

\[
\frac{Y(P+(u,v))+Y(P-(u,v))}{Y(P)}
=-2+\frac{2(2X+u)}{X-u}
 -\frac{2c(X)+6c(u)}{(X-u)^3}.
\]

Indeed the two slopes sum to 2Y/(X−u), and their cubes sum to
2Y(c(X)+3c(u))/(X−u)³. The subtracted kernel y-coordinates cancel.
The verifier checks, as a full polynomial identity,

\[
M=q^3+\operatorname{Tr}\bigl(-2q^3+
2(2X+u)Aq^2-(2c(X)+6c(u))A^3\bigr).
\]

This fixed comparison justifies the implementation of the imported
paired formulas and retains both signs; it is not a general theorem
reproof. The two sums identify the given maps with the named projective
quotient. Their coefficients lie in D throughout, so conjugation-stable
descent applies without introducing a rational generator.

**Equation, differential and noncancellation.** Independent replay checks
every coefficient in D[X] of

\[
c(X)M^2=N^3+a'Nq^4+b'q^6,
\qquad M=N'q-2Nq',
\qquad Mq=N'q^2-N(q^2)'.
\]

The first gives the entire target curve equation in D(\mathcal E).
The latter identities give dX'/(2Y')=dX/(2Y). Cancellation of the
nonzero rational multiplier is in the function field; equality then
holds as global differentials on the smooth curves. The certificate's
δ,δ^{-1} satisfy
δ=−16(4a'³+27b'²) and δδ^{-1}=1, so the target is nonsingular.
All fourteen saved constant-unit pairs are multiplied and checked in D;
they include every nonrational leading coefficient inverted by the
producer's polynomial divisions and the target discriminant. The
explicit rational units 2,3,4,5,6,7,16 are also checked. Remaining
arithmetic is exact rational arithmetic and monic reduction; nonzero
rational numerator/denominator data have their usual Q meaning.

Reduction of the numerator at the full kernel gives

\[
N\equiv4c(q')^2\pmod q,\qquad M\equiv-2Nq'\pmod q.
\]

With the saved I,J the verifier constructs N^{-1}=JI²/4 modulo q
and M^{-1}=−N^{-1}I/2 modulo q, and checks both products equal one.
Thus gcd(N,q)=gcd(M,q)=1 over D, and also after geometric extension.
There is no lost kernel point from numerator cancellation. Complete
leading-coefficient checks give deg N=7 with leading coefficient one,
deg q²=6 with leading coefficient one, and deg M=deg q³=9 with
leading coefficients one.

**All exceptional points and degree.** Fix any embedding D→Qbar and
any root u_i of q. At each of the two points (u_i,±sqrt(c(u_i))),
s=X−u_i is a local parameter since 2Y is nonzero. Squarefreeness gives
ord_s q=1, and the checked units give ord_s N=ord_s M=0. Hence X'
and Y' have exact poles of order two and three. In the target projective
chart where the homogeneous Y'-coordinate is nonzero, the coordinates
are X'/Y'=Nq/(YM) and 1/Y'=q³/(YM). They are regular, vanish at this
point with orders one and three, and satisfy the target equation.
Each of all six points therefore extends to the target O. This is
complete algebraic local evidence, independent of an affine substitution
at a zero denominator.

At source O, X and Y have pole orders two and three. The checked monic
degrees give X'/X→1 and Y'/Y→1. Thus the same target chart has regular
coordinates of orders one and three, and O maps to O. Away from these
seven points q is nonzero, so both affine coordinates are regular and
the image is affine. The extended map has exactly the stated kernel.
It agrees with the imported isogeny on a dense open set and hence
everywhere; no group-homomorphism conclusion is inferred solely from
curve substitution.

Finally the reduced rational function N/q² has degree seven as a map
P¹→P¹, by the checked coprimality and exact degrees. Since X and X'
each have degree two on their elliptic curves,
2 deg Φ=deg(X'∘Φ)=2·7, so deg Φ=7. In characteristic zero it is
separable. This verifies degree independently of a software degree
label or a count alone. The differential scalar one concerns the stated
short differentials only. No minimal-model or Neron-normalization claim
over D follows from it.

**Bounded evidence and preservation.** Reproduction from the notebook
directory uses Python's standard library:

```bash
python3 scripts/seven-torsion/quotient-254/run_stage.py build_quotient
python3 scripts/seven-torsion/quotient-254/run_stage.py verify_quotient
```

Existing output paths deliberately refuse overwrite. For replay in the
saved directory the main mathematical function `verify` can be invoked
on the unchanged certificate with a fresh check list; a later audit
must save its reports in a fresh directory. Neither stopped column
stage is invoked. Full production, replay and preservation reports are
`production-report.json`, `complete-replay.json`, `replay-stage-report.json`
and `rejections-and-preservation.json` in the quotient directory.
All passed. The one production stage took 0.030122 seconds internally,
0.154021 seconds through its watchdog. The one replay stage, including
both altered-evidence tests and preservation checks, took 0.285326 seconds
internally, 0.359009 seconds through its watchdog. Each internal limit
was 180 seconds and each external timeout 181 seconds; neither fired.
New directory bytes before the final watchdog report were 96673 against
134217728. Including the subsequent metadata-only `summary.json`, the
final directory total is 97400 bytes, still below the same bound.

Two complete altered copies are freshly rejected: changing the constant
coefficient of N fails `full_paired_Velu_x_sum`; changing the discriminant
inverse fails `target_discriminant_unit`. No rejection is credited merely
to an input hash mismatch. The preservation inventory covers 152 files,
including every existing upstream non-cache seven-torsion artifact and
the completed production inputs/code/certificate. The pre-production
inventory is also checked after replay. Zero original files changed or
went missing, including all unfinished action/relation evidence and
earlier invalid drafts. Rejection files and complete reports are retained.
The calculation is evidence only for this fixed instance and does not
establish universal implementation correctness. These are the original
production results; the separate critical audit follows. No new mathematics
beyond the inspected general methods is claimed.

**Separate critical audit (2026-10-16, step 256).** Reuse the unchanged
SPECIALIZE assessment and the precise primary theorem statements cited
above. The imported quotient theorem applies over the characteristic-zero
field D: its geometric subgroup is stable under Gal(Qbar/D), as follows
from the entire scalar-orbit presentation in audited L070. The generator
need not be D-rational. L067 proves source nonsingularity, and the saved
target discriminant inverse proves target nonsingularity. Shumow's
existing-isogeny hypothesis is supplied by the quotient theorem, not by
assuming the desired map. Its recorded suspect text lines are not used.
No general isogeny theorem is reproved.

The signs in the paired y formula were checked directly in the secant
law: with lambda_+=(Y-v)/(X-u) and lambda_-=(Y+v)/(X-u), each translated
y-coordinate is -Y+(2X+u)lambda-lambda^3. Their sum gives exactly the
displayed formula after dividing by Y in the function field. The two
subtracted kernel y-values cancel. Division by Y here is a rational
function calculation, not a restriction excluding source two-torsion:
the resulting map Y M/q^3 is regular wherever q is nonzero, including
Y=0. The paired x sum, all three trace components, and both maps are
checked as free-variable polynomial identities, not at a chosen root.

The local extension argument covers every geometric fiber. The two units
q'(u) and c(u) imply three distinct x-roots and two distinct nonzero
y-values over each root. At either sign, X-u is a parameter, N and M
are units, and the two chart functions Nq/(YM), q^3/(YM) have orders
one and three. In this target chart the equation is
beta=alpha^3+a' alpha beta^2+b' beta^3; their values (0,0) are the
smooth target O. At source O the same orders follow from the monic
degrees and the source pole orders (2,3). This proves extension at all
seven exceptional points. Everywhere else q is nonzero and the image
is affine. Agreement with the named quotient on the dense affine open
supplies the homomorphism property. Coprimality and degree seven of
N/q^2, followed by multiplicativity of map degrees and both degree-two
x-coordinates, give degree seven of the elliptic map. Characteristic
zero supplies separability. The nonzero rational differential multiplier
can be canceled in the function field, and equality of regular
differentials then holds globally. None of this asserts minimality.

Fresh complete evidence is in `scripts/seven-torsion/quotient-audit-256/`.
`upstream.json`, `actions.json` and `direction.json` replay all the L067,
L068 and L070 certificates, including both 48-dimensional transports,
the mixed inverse and the full cubic. `quotient.json` replays every
original quotient check and is exactly equal to the original complete
report. The producer, independent verifier and stage wrapper were read;
the rational-polynomial helper uses exact convolution and monic
reduction. All fourteen saved constant-unit products and seven specified
rational constants are covered. The producer records every inverse
used in its polynomial divisions; no unrecorded field approximation or
selected embedding enters.

The distinct `crosscheck.py` imports no notebook arithmetic. It uses its
own exact eight-coordinate field operations and evaluates at all 22
distinct rational numbers -10,...,11. For the cleared curve equation,
the difference is a D[X]-polynomial of degree at most 21. Every full
eight-coordinate residual is zero at all 22 values, so the polynomial
is identically zero. The same check tests the displayed N formula
(degree at most 7), M formula (at most 9), differential identity (at most
12), and both denominators (at most 6 and 9). The exact array lengths,
monic leading coefficients and these degree bounds are checked; the
22 evaluations exceed each corresponding degree. Thus this is exact
interpolation, not numerical sampling or an unbounded-degree inference.
`crosscheck.json` retains every full field value, both curve sides and
every residual. It also independently checks all constant units and
the target discriminant. The projective justification above remains
essential and is not replaced by these polynomial identities.

`evidence.json` compares the complete original stage reports, watchdogs,
logs and summary with fresh replay and the actual file sizes. Each of the
two original altered certificates is checked to differ in precisely its
intended entry, then freshly rejected: `wrong-x.json` at
`full_paired_Velu_x_sum`, and `wrong-discriminant-inverse.json` at
`target_discriminant_unit`. Their own fresh reports retain every check
preceding failure; neither rejection is credited to a hash mismatch.
The original production-input and replay inventories (144 and 152 files)
both match exactly. The fresh pre-audit inventory covers 161 original
non-cache files, with zero changed or missing files after all stages,
including the invalid drafts and unfinished incidence columns.

Reproduce with a fresh copy/output location because existing report and
log paths deliberately refuse overwrite:

```bash
python3 -B scripts/seven-torsion/quotient-audit-256/run_audit.py
```

All five fresh stages finish in less than three seconds each against
the 180-second bound, with external 181-second watchdogs never fired.
The directory has 128521 bytes before the final audit report, below
134217728. `audit-report.json` retains the exact stage measurements and
preservation result. This separate fixed audit passes as REPRODUCTION;
it establishes a checked quotient input only. The affine-line/dual-twist
identification, incidence/norm and arithmetic descent conclusions remain
outside its hypotheses and conclusion. No BSD candidate is supplied.

## Mathlib

Full matching coverage for this quotient, its stable non-pointwise-rational
kernel, all maps, projective local witnesses and complete fixed rational
certificate was not checked. Unknown coverage is not absence. The precise
primary theorem citations above are the imported mathematical inputs;
the exact arithmetic replay is not a Lean formalization.
