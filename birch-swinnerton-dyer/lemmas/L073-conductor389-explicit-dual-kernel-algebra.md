# L073 — Explicit nonzero dual kernel over the full direction field

## Hypotheses

Use audited L067/L068/L070/L071/L072 for the fixed curve
E: y²+y=x³+x²−2x. Its rational short model is
𝓔: Y²=X³+aX+b, a=−3024, b=46224. Let D=Q[Z]/h be L070's
entire degree-eight direction field, on the basis 1,Z,…,Z⁷, with its
full relative kernel cubic q. L071 supplies the separable degree-seven
quotient Φ:𝓔_D→𝓔′, where 𝓔′:V²=T³+AT+B, and both coordinate
maps, with differential scalar one. L072 identifies the dual-kernel
family with affine lines missing zero, with its stated scalar and
Cartier-duality conventions. No generator of a direction, selected
embedding, residual-image or Selmer premise is imposed.

The complete inputs are `scripts/seven-torsion/quotient-254/quotient.json`
and `scripts/seven-torsion/compressed-249/direction.json`. All rational
coefficient arrays are ascending in Z, reduced modulo the full h; arrays
of free-variable polynomials are also ascending. The retained candidate
is `scripts/seven-torsion/dual-262/dual.json`; its independently replayed
copy is `scripts/seven-torsion/dual-263/dual.json`. The original failed
verifier and its failure are preserved and are not mathematical inputs.
L069 and unfinished incidence columns are excluded.

## Conclusion

Let k(T)=T³+7ZT²+κ₁(Z)T+κ₀(Z), where the following are the complete
ascending coefficient vectors of κ₀ and κ₁ in D:

```text
κ₀ = [123365276799408/2048947, -31517837620956/14342629,
      540373435782/14342629, -16414723577/24587364,
      9791934977/3614342508, -29044903/2655435312,
      81427/63730447488, 204766309/4721661393490944]
κ₁ = [-84768748344/2048947, -3414652908/2048947,
      218464421/4097894, -225367787/147524184,
      12684745/2065338576, -1809049/63730447488,
      1537/223056566208, 3103/27531553314816]
```

There is an explicit presentation of the full nonzero dual kernel:

\[
\mathcal B=D[T,V]/(k(T),\ V^2-(T^3+AT+B)).
\]

It is finite etale of rank six over D and rank 48 over Q. Its D-basis
is (1,T,T²,V,TV,T²V); its Q-basis is ZʲTⁱVᵉ for 0≤j<8,
0≤i<3, 0≤e<2. No fieldness or field-factor decomposition is asserted.

Put c′(T)=T³+AT+B and s₁=−7Z. Define

\[
\begin{aligned}
N&=(7T-2s_1)k^2-(6T^2+2A)k'k
       +4c'(T)((k')^2-kk''),\\
M&=N'k-2Nk'.
\end{aligned}
\]

The actual raw-model dual is

\[
\widehat\Phi(T,V)=
 \left(\frac{N(T)}{49k(T)^2},\frac{VM(T)}{343k(T)^3}\right).
\]

Its differential scalar is seven. Both compositions with Φ equal [7]
in both coordinates as full function-field identities over D. This
presentation retains all eight direction fibers and both signs over
each root of k. The full kernel has degree 56 over Q; removing its
identity in every fiber removes exactly eight geometric points.
Via L072, 𝓑 is the coordinate algebra of all 48 affine lines missing
zero, with inverse ordinary-functional scalar indexing and the retained
Cartier cyclotomic action. There is no identification with the original
point algebra or a choice trivializing μ₇.

This is a fixed known-algorithm reproduction. Its full independent replay
and separate fixed critical audit pass. Step 265's rejection-harness
mismatch and step 266's fresh corrected audit are documented below. It supplies no
incidence/norm, functions, complete global units/classes, local data,
Selmer bound, successful localization, rational membership, removal of
divisible Sha or arbitrary-curve complex-order/rank comparison.

## Proof

**Named inputs and specialization.** Reuse the invocation-start SPECIALIZE
assessment `drafts/literature/2026-10-16-explicit-dual-kernel-algebra.md`.
Bostan–Morain–Salvy–Schost, *Fast algorithms for computing isogenies
between elliptic curves*, Math. Comp. 77 (2008), 1755–1778,
DOI 10.1090/S0025-5718-08-02066-8,
[arXiv:cs/0609020v1](https://arxiv.org/pdf/cs/0609020v1), Theorem 2(2),
§§2.4–2.5 and 4.1–4.3, Proposition 4.1 and fastElkies′ correctness,
provides normalized reconstruction in characteristic zero. Numbering
is that of the inspected PDF dated 1 February 2008, not an independently
compared publisher version. D has characteristic zero and L071/L072
supply the isogeny and its base-field dual. Thus this is a supported
fixed reconstruction, not a new general isogeny algorithm.

Sutherland, MIT 18.783 Fall 2023,
[Lecture 5 §§5.5–5.6, Lemma 5.20 and Theorem 5.21, pp.10–14](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
supplies the division-polynomial recurrences and multiplication maps.
The source and target are nonsingular characteristic-zero short curves,
by L067/L071, so those formulas apply to their full function fields.
Sutherland, MIT 18.783 Fall 2025,
[Lecture 6, Theorem 6.7 prime-degree Case 1, pp.3–4, and Lemma 6.10, p.5](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
supplies the unique dual and its compositions. We use it to identify
the checked map, without redoing general duality. The model-scaling
convention agrees with the inspected
[Sage 10.7 baseWI definition, lines 32–40 and 158–203](https://raw.githubusercontent.com/sagemath/sage/10.7/src/sage/schemes/elliptic_curves/weierstrass_morphism.py).

**Normalization and construction.** The isomorphism
J:𝓔→𝓔″:Y″²=X″³+7⁴aX″+7⁶b is (X″,Y″)=(49X,343Y).
Substitution uses 343²=49³, 49·7⁴=343² and 7⁶=343².
Its inverse divides by 49 and 343, and J*ω″=ω/7. Consequently
J∘hat(Φ) has differential scalar one. BMSS is applied from 𝓔′ to
𝓔″, and the actual dual is recovered by J inverse; a normalized map
directly to unchanged 𝓔 would have the wrong scalar.

The producer in `dual-262/build_dual.py` constructs S to precision 52
and T(t)=S(x)/x, t=x², to precision 26, with Newton precisions 8,16,26.
It reconstructs the reversed x-map with numerator degree ≤7 and
denominator degree ≤6, takes its exact monic square root and reverses
it to obtain k. The complete series, reconstruction and constant-unit
witnesses are retained. The new independent verifier imports only
`verify_certificate` rational helpers and no producer arithmetic.
It verifies the complete 26-coefficient differential equation,
reciprocal-series and rational-reconstruction identities, exact
squaring, kernel reversal, and all 21 retained constant-unit pairs.
No reliance on formal reconstruction alone is needed: the full maps
and both compositions are independently checked below.

**Curve, differential and noncancellation identities.** The verifier
recomputes in D[T], checking monicity/degree and every coefficient of

\[
c'M^2=N^3+7^4aNk^4+7^6bk^6,\qquad M=N'k-2Nk'.
\]

Division by 343²k⁶ yields the equation of 𝓔 for the displayed map.
Differentiating its x-coordinate and dividing by twice its y-coordinate
gives 7 dT/(2V), including the sign of M. The checked degrees are
(deg k,deg N,deg M)=(3,7,9), all monic. The complete saved witnesses I,J₀
satisfy k′I=1 and c′J₀=1 modulo k. The verifier also checks the units

\[
N^{-1}=J_0I^2/4,\qquad M^{-1}=-J_0I^3/8\quad\pmod k.
\]

These follow from N=4c′(k′)² and M=−2Nk′ modulo k, and their full
products, not just these formulas, are checked. Thus neither numerator
cancels any root of k in any geometric fiber.

**Independent multiplication normalization and both compositions.** Write
r₄=ψ₄/(4V), r₆=ψ₆/V and r₈=ψ₈/V on either short curve, using its
own cubic c. The standard recurrences specialize to

\[
\begin{aligned}
\psi_5&=32c^2r_4-\psi_3^3,&
r_6&=2\psi_3(\psi_5-4r_4^2),\\
\psi_7&=\psi_5\psi_3^3-128c^2r_4^3,&
r_8&=2r_4(r_6\psi_3^2-2\psi_5^2),\\
\psi_9&=64c^2r_6r_4^3-\psi_3\psi_5^3.
\end{aligned}
\]

The original step-262 verifier had factor eight instead of two in r₈.
Its stopped files are preserved. This replay additionally implements
the original recurrences in pairs (f,g) representing f+gV with V²=c,
retaining V through every multiplication. Division by 2V is performed
by exact monic division of the even component by c, with zero remainder
required, and ordinary division of the odd component by two. It checks
all coefficients of ψ₅,…,ψ₉ against the compressed formulas in each
of the two full curve function fields. It then checks

\[
\phi_7=T\psi_7^2-cr_6r_8,\qquad
\omega_7/V=(\psi_9r_6^2-\psi_5r_8^2)/4
\]

against the pair-ring multiplication formulas. Degrees/leading
coefficients are respectively (24,7),(49,1),(72,1) for ψ₇,φ₇,ω₇/V.
The additional identity φ₇′ψ₇−2φ₇ψ₇′=7ω₇/V holds in both fields.

For a polynomial p of degree at most n write
Hₙ(p;I,D₀)=D₀ⁿp(I/D₀). For dual after quotient use
(I,D₀,K,M_in)=(N_Φ,q²,q,M_Φ), and outer polynomials (N,k,M).
For quotient after dual use (I,D₀,K,M_in)=(N,49k²,k,M), and
outer polynomials (N_Φ,q,M_Φ). The subscripts Φ denote L071's maps.
In both orders, the exact composite has x numerator
H₇(N_out;I,D₀), denominator root

\[
 d=7K H_3(k_{out};I,D_0),
\]

and y multiplier numerator M_in H₉(M_out;I,D₀), with denominators
d² and d³. In the first order the outer factors 49,343 give these
denominators; in the second order they are the inner factors. Thus
no additional scalar is omitted. The two complete composition
certificates check d=ψ₇ and equality of both numerators with φ₇ and
ω₇/V, coefficientwise modulo h. Their six residual arrays are all
zero; ψ₇ is nonzero by its checked leading coefficient. Hence
FΦ=[7] and ΦF=[7] as rational maps, where F is the displayed candidate.
Since the actual dual satisfies hat(Φ)Φ=[7] and Φ is dominant,
injectivity of its function-field pullback gives F=hat(Φ). This uses
both coordinate identities, rather than seven-torsion membership or
an unproved group-homomorphism assertion from curve substitution.

**Projective completeness in every fiber.** Fix any embedding D→Qbar.
For each root t of k, its derivative is nonzero, and c′(t) is nonzero
by the checked units. There are exactly two points (t,±sqrt(c′(t))).
At either point s=T−t is a local parameter, k has order one, and N,M,V
are units. The target chart coordinates

\[
 x/y=7Nk/(VM),\qquad 1/y=343k^3/(VM)
\]

are regular of orders one and three and vanish at the point, so it
maps to O. At source O the monic degree checks give x/T→1/49 and
y/V→1/343. The same chart coordinates have orders one and three;
O maps to O, with local parameter −x/y having leading factor seven
times −T/V. Away from these seven points the denominators are nonzero,
so the image is affine. This proves the exact kernel, including both
signs and O, with no missing exceptional point. The coprime reduced
x-map N/(49k²) has degree seven on P¹. Since the elliptic x-coordinates
have degree two, the map of elliptic curves has degree seven.
All identities were in D, so they hold simultaneously after every one
of its eight embeddings; no embedding-specific calculation is used.

**Full algebra and etaleness.** Successive monic division by k(T) and
V²−c′(T) gives the unique normal form f(T)+g(T)V with deg f,deg g<3.
Equivalently each monic quotient is free of its asserted rank, so the
six displayed elements are a basis, not merely a spanning set. This
proves rank six over D and rank 48 over Q. The full 36-entry product
table is retained in `dual-263/algebra.json`, using c′ modulo k.
Import [Stacks Definition 10.144.1, tag 00UB](https://stacks.math.columbia.edu/tag/00UB)
and [Lemma 10.144.2, tag 00UC](https://stacks.math.columbia.edu/tag/00UC)
for the monic/invertible-derivative etale criterion. In D[T]/k the
witness I makes k′ a unit, so this rank-three algebra is etale.
In the quadratic quotient V is a unit because V²=c′ and c′ is a unit;
thus 2V is a unit. The next rank-two algebra is etale. Transitivity
and the etaleness of D/Q give finite etaleness over Q. Each geometric
fiber consists precisely of the six checked nonidentity kernel points.
L072 identifies their union with affine lines missing zero, retaining
the ordinary inverse scalar labels and Cartier μ₇ action. Its identity
section over D has eight Q-geometric points, all excluded here. We
compose schemes over D to Q; we do not use Weil restriction or a
matching dimension as a substitute for the kernel identification.

**Finite evidence, bounds and qualifications.** One repaired independent
replay was executed, with no new producer run or extension of a stopped
stage:

```bash
python3 -B scripts/seven-torsion/dual-263/run_stage.py verify_dual
```

Internal time is 9.586825000005774 seconds against 180; external time
is 9.670649584033526 seconds against 181, with no watchdog firing.
The watchdog records 599923 bytes before its report against 134217728.
The original production had already completed within its cap in step 262.
Every replay check, zero failure list, six composition residuals, both
complete recurrence residual records, curve/differential residuals,
etaleness-unit residuals and preservation record was inspected in full.
All 21 original stopped files and both complete upstream input files
retain their original hashes. The bounded wrong-normalization, lost-sign
and changed-late-coefficient fixtures are rejected at
`actual_dual_normalization` and `actual_dual_differential_seven` (the latter
for both coefficient fixtures). These test the displayed preliminary
coordinate conditions; they are not falsely described as full fresh
replays of every malformed certificate.

The computation establishes an explicit fixed input already covered
in general by known algorithms, not a new theorem beyond the sources
checked. Full replay and the projective argument were completed at the
construction stage; its then-pending separate audit is completed below. No descent
arithmetic or BSD conclusion is inferred.

**Partial separate audit and stopped harness (2026-10-16, step 265).**
The unchanged SPECIALIZE assessment
`drafts/literature/2026-10-16-explicit-dual-kernel-critical-audit.md`
authorizes this fixed RESEARCH / REPRODUCTION audit. Audited upstream
inputs are accepted, not reaudited. All new evidence is under
`scripts/seven-torsion/dual-audit-265/`. The single stage stopped at a
rejection-expectation mismatch; its aggregate `passed` value is false.
No second stage, modified expectation or rerun occurred this turn.

The fresh complete replay passes in 9.662294708075933 seconds. It also
checks the displayed full N formula, all retained Newton prefixes
(8,16,26) against the final series and original records, the reconstruction
kernel/bounds and constant-unit correspondence. `complete-evidence.json`
records full recursive equality with eleven original data files, including
both entire composition certificates, both recurrence records and the
whole 36-entry multiplication table. All six composition residuals, ten
pair-ring recurrence residual pairs, curve/differential residuals and
both etaleness-unit residuals are zero. This is a complete replay, not
a check of saved success flags.

The distinct check `group_law.py` imports no notebook arithmetic or
division recurrence. It works with integer polynomial pairs in
R=Q[X,Y]/(Y²−(X³−3024X+46224)), preserving both coefficients of 1,Y.
The standard elliptic chord-and-tangent group law is used in homogeneous
coordinates (u,v,w), with affine coordinates (u/w²,v/w³). This verifies
the fixed multiplication instance covered by the cited Sutherland theorem,
not a new group-law theorem or a reproof of general duality. For doubling
put s=4uv² and m=3u²+aw⁴; the actual formulas are

\[
u_2=m^2-2s,\qquad v_2=m(s-u_2)-8v^4,\qquad w_2=2vw.
\]

For addition put U₁=u₁w₂², U₂=u₂w₁², S₁=v₁w₂³, S₂=v₂w₁³,
H=U₂−U₁ and r=S₂−S₁; then

\[
u_3=r^2-H^3-2U_1H^2,\quad
v_3=r(U_1H^2-u_3)-S_1H^3,\quad w_3=Hw_1w_2.
\]

Substitution of u/w²,v/w³ in the usual tangent and secant slopes
(3x²+a)/(2y) and (y₂−y₁)/(x₂−x₁) gives these formulas. Starting at
(X,Y,1), the check doubles to 2, adds 1 to reach 3, doubles to 6 and
adds 1 to reach 7. Every tangent denominator, secant H and resulting w
is checked nonzero in R. Thus the formulas compute generic multiples;
they do not assert denominators nonzero at every point. The full triples
and secant witnesses are saved in `group-law.json`.

Write d,nₓ,nᵧ for the *composition* denominator root, x numerator and
y-multiplier numerator in the fresh `dual_after_quotient.json`. Every
D coefficient is examined: all nonconstant Z coefficients vanish and
constant coefficients are integers. This is equality in the whole D,
not a specialization at one root. For the output (u₇,v₇,w₇), the full
polynomial-pair residuals

\[
u_7d^2-n_xw_7^2=0,\qquad v_7d^3-Yn_yw_7^3=0
\]

vanish, with d,w₇ nonzero. Therefore FΦ=[7] independently of the
division recurrence in both coordinates over D. The other order follows
independently as well: the *audited* Φ is a homomorphism, so
(ΦF)Φ=Φ[7]=[7]Φ, and dominance gives ΦF=[7]. No homomorphism property
of F is assumed. Fresh replay also checks the other order directly in D.
No second group-law computation on a selected target fiber is asserted.
All 308 recorded distinct-check conditions pass.

Critical reading of the projective and algebra arguments above found no
omitted fiber: k′ and c′ units give simple roots with two nonzero signs
each, numerator units give the pole orders, and monic degrees control O.
T−t is a parameter at each finite point since 2V≠0. The chart x/y,1/y
is the target plane cubic's neighborhood of O. Elsewhere the image is
affine. Monic division gives uniqueness as well as spanning, and
V⁻¹=V(c′)⁻¹ makes 2V a unit. These arguments hold under every embedding
of D. Identity removal and affine-line conventions remain those of L072.

Fresh malformed normalization and sign fixtures fail at
`actual_dual_normalization` and `actual_dual_differential_seven`.
They are preliminary-condition rejections, not complete malformed replays.
The third fixture changes the last T-series coefficient. It passes both
full composition orders, then fails `complete_Newton_prefix_26`: its
unchanged saved Newton iterate no longer matches that coefficient.
The harness expected the later `full_reciprocal_series` failure and stops
with `unintended rejection late-series`. This is an expectation error
after adding a valid earlier check, not a counterexample to the original
certificate or a successful aggregate audit. The late malformed replay
does not reach reciprocal, ODE or algebra checks. Complete reports remain
under `reject-late-series/`, `reject-normalization/` and `reject-sign/`.
No aggregate fresh-rejection report was completed.

The single stage records 17.107853291905485 seconds against 180; the
external watchdog records 17.235021500033326 against 181 without firing,
and 1480379 bytes before its report against 134217728. All 178 inventoried
original/upstream files retain their hashes, including the failed original
recurrence verifier. The stage was not restarted after its first unexpected
outcome; its negative aggregate result remains authoritative. Mathematical
subchecks provide additional fixed-instance evidence, but the separate
audit remains incomplete. No incidence, arithmetic descent, BSD conclusion
or progress beyond the checked known algorithms follows.

**Completed separate critical audit (2026-10-17, step 266).** Reuse the
unchanged SPECIALIZE critical-audit assessment cited above. The complete
proof, actual producer, repaired independent verifier, stage wrappers and
distinct group-law implementation were read before the single fresh run.
Only the fresh harness's expected late-series failure and its description
were corrected: `complete_Newton_prefix_26` is the intended earlier failure.
The mathematical verifier, group-law code and seven seed input files are
unchanged copies. Step 265's stopped evidence and ATTEMPTS/035--038 remain.

Reproduction command, with all new arithmetic in one stage:

```bash
python3 -B scripts/seven-torsion/dual-audit-266/run_stage.py
```

The aggregate audit passes with no failures. Internal time is
17.311364333028905 seconds against 180; external time is
17.418279582983814 seconds against 181, with no watchdog firing.
The external record counts 1498969 bytes before its own report against
134217728. Fresh complete replay takes 9.813124750042334 seconds.
`complete-evidence.json` records complete recursive equality of all eleven
original data files, including both compositions, both recurrence records
and the entire 36-entry multiplication table. All six composition residuals,
ten recurrence residual pairs, curve/differential residuals and both
etaleness-unit residuals were inspected in full and are zero. The full check
record includes all 26 Pade, reciprocal and ODE coefficients, every retained
Newton prefix and original iterate, all 21 constant-unit witnesses and the
monic basis. Both multiplication degree/leading-coefficient records match
(24,7), (49,1), (72,1).

The distinct generic group-law chain above passes all 308 conditions with
both full polynomial-pair residuals zero. Every nonconstant D-coordinate
of the composition is checked zero before the integer comparison; this
is neither evaluation at a chosen root nor sampling. Generic tangent and
secant denominators are nonzero. Dominance and the audited quotient's
homomorphism property justify the second order independently, while full
replay checks it directly as well. The existing projective argument covers
every root of k with both signs and O: the derivative/cubic units give
local parameters and nonzero V; numerator units give the stated orders;
monic leading terms control O. These identities hold in D, hence in all
eight embeddings. Successive monic quotient bases have unique normal forms,
and k-prime and 2V are units. L072's equivariant identification and exactly
eight excluded identity points are retained, without a fieldness assertion
or root-of-unity trivialization.

All three fresh malformed cases are rejected as intended. Normalization
and sign fail at the two preliminary checks named above. The late-series
case passes both complete composition orders and fails at
`complete_Newton_prefix_26`, before reciprocal, ODE and algebra checks;
it is not a complete malformed replay. `fresh-rejections.json` records
their complete actual check prefixes and qualifications. `preservation.json`
confirms all 241 inventoried original/upstream files, including the entire
stopped step-265 audit, have unchanged hashes. No failed stage was restarted
within this turn and no cap or mathematical check was relaxed.

This completes the fixed critical audit under the unchanged hypotheses.
It makes the explicit affine-line algebra a reliable local input, without
constructing incidence pullbacks/norms or supplying any descent arithmetic,
Selmer bound, successful localization, rational membership, divisible-Sha
removal or arbitrary-curve rank comparison. No new result beyond the checked
known algorithms is claimed; the direct mathematical inputs in the DAG
remain L067/L068/L070/L071/L072.

## Mathlib

Full matching Mathlib coverage of this explicit full-field dual-kernel
presentation, both compositions and exact finite certificate has not
been checked. Unknown availability is not absence. The cited primary
theorems supply the imported mathematics; this is not a Lean proof.
