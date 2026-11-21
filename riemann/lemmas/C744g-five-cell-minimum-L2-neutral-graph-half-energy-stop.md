# C744g: Exact minimum-L2 neutral correction exists, but its fixed half-energy bound fails

## Hypotheses

Use L744 (6)'s complete energy, with ell=log(3)/2, a=5ell/2,
L=2a, all nine active prime powers, the pole and the entire response
family. Use C744b's physical ten-output complex-linear moment map C
and its even orthonormal basis on (0,a):

    e_0=a^(-1/2), e_q=(2/a)^(1/2)cos(q*pi*x/a), q>=1.

The centered full-interval representative is f(x)=v(|x|)/sqrt(2).
Write V0=span(e_0,...,e_63), V1=span(e_64,...,e_83).
Let C0 and C1 denote the restrictions of the ORIGINAL ten-output map
to these spaces. Let E mean the semibounded zero-extension smooth
form closure, not the generator quadratic form on an asserted larger
operator domain. Put H[x]=E[x]+256||C0 x||^2 on V0. C744e's accepted
complete core matrix is an input; no sign on an84-mode space is assumed.

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-11-11-five-cell-neutral-middle-correction-471.md`.
This is a known-method specialization/REPRODUCTION. The analytic identity
and finite-form closure are imported from C744b/c/e, with their precise
source scope: Hongmin Li, *Cutoff-free positivity of localized Weil forms
through the (log11)/2 threshold*, displayed v2, 9 November2026,
[paper45](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma3.1 and (2.1)-(2.5). Only its arbitrary-a smooth identity is used;
its numerical sign and inaccessible supplement are not inputs.

Supporting scalar identities are [DLMF5.7.6](https://dlmf.nist.gov/5.7.E6)
for the digamma difference and [DLMF5.4.19](https://dlmf.nist.gov/5.4.E19)
at p=1,q=4 for psi(1/4). The enclosure uses C744b's audited70-digit
directed implementation under the [Python Decimal arithmetic
contract](https://docs.python.org/3/library/decimal.html), including
correctly rounded exp/ln/sqrt widened by adjacent numbers and its
Machin/Taylor trigonometric bounds. These unchanged inputs are reused,
not reproved as new mathematics.

The linear algebra import is R. Penrose, *A generalized inverse for
matrices*, Proc. Cambridge Philos. Soc.51 (1955),406-413,
[DOI](https://doi.org/10.1017/S0305004100030401), Theorems1-2 and
Lemma2-1, together with *On best approximate solutions of linear matrix
equations*, ibid.52 (1956),17-19,
[DOI](https://doi.org/10.1017/S0305004100030929), unnumbered theorem
p17 and proof p18. These cover complex rectangular matrices and the
unique minimum Euclidean norm consistent solution. No convexity of
the Weil form is assumed, and no linear algebra theorem is reproved.

## Conclusion

Every x in V0 has a unique minimum-L2-norm correction Yx in V1 with
C1(Yx)=-C0 x. The complex-linear map Y satisfies

    ||Y||_(L2->L2) < 37803.

Nevertheless, for the explicit nonzero real x below,

    2.659 < ||x||^2 < 2.660,
    E[x+Yx] - H[x]/2 in
        [-1.135514938e-37, -1.135514937e-37] < 0.             (1)

Thus the specified fixed64+20 minimum-L2 graph does NOT preserve at
least half of every core vector's complete penalized energy. The
correction exists and all ten moments vanish exactly; the failure is
the quantitative energy threshold. Both H[x] and E[x+Yx] are positive
for this witness. This is not negative neutral energy, a disproof of
RH, or an obstruction to every correction rule or energy fraction.
No parameter or threshold has been retuned. The separate conceptual
audit below (11 November2026, step475) accepts the exact map and
negative complete difference. RH remains IN_PROGRESS.

## Proof

### Exact equations and the minimum-norm map

For cell center t_j=(j-2)ell, the physical moment is

    m_(j,sigma)(f)=integral_(t_j-ell/2)^(t_j+ell/2)
                       exp(sigma*(x-t_j)/2) f(x) dx.

For any complex even f, substituting x=-z proves the EXACT identity
m_(j,sigma)(f)=m_(4-j,-sigma)(f). Select representatives
(0,+),(0,-),(1,+),(1,-),(2,+). Each of the ten rows is one of
these five or its reflection, including m_(2,-)=m_(2,+).
These identities apply to every basis vector and every complex
linear combination; interval-small differences are not used to
establish them. Write A for the five-row restriction on V1 and B
for the five-row restriction on V0, and G=AA^*. All entries are real.

The directed LDL certificate for G has pivots strictly exceeding,
in order,

    0.0003483, 2.1740e-8, 0.0003371, 1.4041e-8, 1.9314e-9.

The exact G therefore is positive definite and A is onto C^5.
In particular range(C0) is contained in range(C1): the latter is
the full five-dimensional reflection-invariant output space and
the former lies in that space. No rank assertion on C0 is needed.
Define the EXACT map

    Y=-A^* G^(-1) B.                                        (2)

Algebra gives A Y=-B and reflection gives all ten original moment
equations. Penrose's cited consistency/minimum-norm result identifies
(2) as their unique minimum-norm solution. The basis is orthonormal,
so the coefficient Euclidean norm is precisely the reservoir L2
norm; complex coefficients introduce no change of metric.

Outward LDL forward/diagonal/back substitution encloses G^(-1) and
every entry of Y. The full certificate gives

    ||G^(-1)||_2 <= max absolute row sum < 2.58e9,
    ||Y||_2 <= ||Y||_F < 37803.

The first norm inequality uses the real symmetry of the EXACT
inverse, not a supposition that rounded endpoints form an exact
inverse. The Frobenius upper bound is obtained by summing interval
upper bounds on all20*64 squared entries. The exact moment identities
follow from (2), not from the stored residual intervals.

### Complete form on the graph

Every vector x+Yx is a fixed finite cosine sum through83. The
C744c/C744e cutoff proof applies unchanged: an even smooth interior
cutoff removes collars of width epsilon; the removed Fourier
transform and cosine coefficients are respectively
O_v(min(epsilon,|xi|^(-1))) and O_v(min(epsilon,q^(-1))). Their
logarithmically weighted squared norms are O_v(epsilon log(1/epsilon)).
The bounded complete response map and finite delay, pole and moment
forms pass to the limit. Apply this to real and imaginary parts and
polarize. This proves the complete finite Hermitian form identity
on V0+V1. It makes no assertion of H1 zero-extension regularity or
an exactly neutral smooth approximating sequence.

For k_q=q*pi/a, u_q=k_q^2, n_0=a^(-1/2), n_q=(2/a)^(1/2), put
c_j=2j+1/2. The unpenalized matrix Q on labels0-83 is

    Q_rs=delta_rs h(k_r)+P_rs+p_r p_s
        +n_r n_s (-1)^(r+s) sum_(j>=0)
            c_j^2(1-exp(-2a c_j))/((c_j^2+u_r)(c_j^2+u_s)), (3)

where h(k)=Re psi(1/4+ik/2)-log pi. Here P includes exactly
n=2,3,4,5,7,8,9,11,13 with weights -2log(base prime)/sqrt(n).
C744b (9)-(10)'s integrations give their full correlations and
all ten moment rows, retaining the normalization n_q/sqrt(2).
The pole row is n_q(-1)^q c_0/(c_0^2+u_q) times
exp(a/2)(1-exp(-a)). Its parity sign is positive. The complete
response entries in (3), including mixed core/reservoir entries,
are not replaced by the old128-response truncation.

For completeness, the only new analytic specialization of C744e's
enclosure method is the frequency extension to83. Reuse its accepted
S_p=sum_(j>=512)c_j^(-p), 2<=p<=66, and gamma enclosure; their
dyadic-binomial and final integral-tail proofs already pay the full
infinite sums. Evaluate the first512 response terms directly.
Set R=u_83/c_512^2<0.03435. The rational part of each remaining
entry is expanded through total degree31. Before n_r n_s and its
sign, the absolute remainder is bounded by

    S_2 * 33 R^32/(1-R)^2,

because the degree-m absolute coefficient is at most (m+1)R^m.
The omitted exponential correction is at most
exp(-2a c_512)S_2. Both are added symmetrically. The first remainder
is <2.440e-49. For the new diagonal values, the convergent digamma
difference and a32-term geometric expansion give error at most
2u_q(u_q/c_512^2)^32 S_3, at q=83 less than2.429e-49.
Every new entry uses these full tails, not a preview or an asymptotic
truncation without remainder. All original nine arithmetic terms
and ten moments are evaluated by the audited elementary formulas.
The exact arithmetic contracts and supporting DLMF formulas are
those specified in C744b/e; no new source sign is imported.

The accepted core H enclosure is reused as is, and Q00=H-256C0^*C0.
Partition Q into00,01,10,11 blocks. Exact neutrality removes the
penalty on the graph only AFTER (2). The exact difference matrix is

    F=H/2-256C0^*C0 + Q01 Y + Y^* Q10 + Y^* Q11 Y.           (4)

This is simply [I;Y]^*Q[I;Y]-H/2. Every mixed term remains in
(4). No independent-box lower bound, conditional positivity,
energy-minimizing correction or complement estimate is substituted.

### The fixed witness and directed evaluation

Let x=sum_(q=0)^63 z_q e_q. The following are the EXACT finite-decimal
values z_0,...,z_47, in order; z_48=...=z_63=0.

```text
-1.669167757613132608868127578174267009160400219649696638770276E-3
-1.034561665999315833548388114976870747572088348797711104133684E-2
2.028030131360206165887456197514722170177411006555067405470735E-1
4.324588345830891777628061399803746713090256902581099533671329E-1
-3.750312142133733356482307324515643124007319675720388445190129E-2
-6.785276738114300907998238205849794120067780502025370634933339E-1
-2.030222832103253328629574114811888933372905783879861454411827E-1
9.150518164044877060199854975060628148199136575610050011117376E-1
1.000000000000000000000000000000000000000000000000000000000000E+0
1.395175409481317610595181331647261625679917085278395207319439E-1
-2.342771474142914333470200304026761585128461139322236401467419E-1
1.875841850059422529520815051348612772371776635667721915474825E-2
1.231251682874815300830565825462709971713897915234014039690416E-1
2.054587985159749712295375859985066663432974692863162751608617E-2
-8.117075879690754277420800992490503107226461677990230069063606E-3
8.866850264525185764587187325453209803702973276516056839582994E-3
3.269022109173499281874232673758034382485533561938136405679977E-3
-1.252318717459176173850602128740165957638843527083417056448374E-3
1.064749813311803520499035958300578320842336908043221761640720E-4
-2.976889843703908107218664648590799675388512547293303201846714E-5
-1.582546098172649140783920135807561911851428969140705047669535E-4
9.163320608080242011478436846393687453567516026421972468715064E-7
-5.366198719966306556218524096466061602931811131035966780482556E-6
-1.847435787729073876107236498634573453901225366080900499090800E-6
2.391068580310696436361601392142947570896870304434944513341290E-6
-4.361318508854577827720275605254865450859998859909247480127170E-7
1.917458805179445899628520194979910465313941827516694732287199E-8
-8.453149322278345732387634560482884138845417149551530972348068E-8
-3.978387331472621490007843729683990868796889206472430754534551E-8
5.129722675049615464748742219633738653964081614649817290550864E-9
-2.602444970553577436498255772441981412989638944414015384277243E-9
1.263589122293210579235817955860564380647404785301340896325334E-9
-6.970419333227460426767639716301628987726064656383849348633270E-10
-3.286785265548774476259177477830101114628479295147243285012819E-11
-2.610122851637363995415882779517541587529809655708389682020666E-11
2.079152656526642939995751469313683436020052133802913025423463E-11
5.467200265692006191666571097584815224798962250766657761242902E-12
-2.222153684991185870254279107666176450749527186208773230169139E-13
3.755908169005174964897054466462664474562488607056241182473844E-13
1.444095223482246338150435660228273390695325152178009371473070E-13
1.443727981017501901438978074395131808559784943665357460181653E-13
-1.886736963550387795364374993822854674658797377000407500246360E-14
-1.862847526522319632823175071825712111246948401376453822229118E-15
-2.155889992949654735165297968170269936689213490169403298962286E-15
7.786708874726594126283108745133996213445268905922624186234445E-16
-1.764376288046397637719685425051202047231022293245799288284433E-16
8.905883309814713756919347496224940774644354879581023047186166E-18
4.228519648252557985729893805655871992202944679259630595016672E-18
```

In particular z_8=1, so x is nonzero. The proposal came from a
110-digit point LDL computation, whose first nonpositive pivot is47.
Neither that pivot nor the NumPy screening sign is a certificate.
The coefficients above are fixed exact rationals; only their
subsequent directed contractions are used in the conclusion.

The independent rational contraction gives the deliberately widened
bounds

    H[x] in [4.47052368249005e-35, 4.47052368249006e-35],
    E[x+Yx] in [2.22390669187016e-35, 2.22390669187020e-35],
    ||Yx||^2 in [8.79804629643342e-36, 8.79804629643343e-36].

The difference is evaluated as a full expression BEFORE widening;
subtracting these displayed coarse bounds is not the certificate.
The directed64-mode contraction of (4) is enclosed in
[-1.135519245e-37,-1.135510630e-37]. An independent exact-rational
reassociation first computes the20 entries of Yx, then contracts
the full84-mode Q on [x;Yx] and subtracts H[x]/2. It gives

    [-1.1355149374865920e-37, -1.1355149374833774e-37],

which proves (1). All endpoint arithmetic in this check is exact
Fraction arithmetic; displayed decimal endpoints are rounded outward.
Thus this is a strictly negative upper enclosure for a specified
direction of the DIFFERENCE, not a failed lower bound or an
inconclusive factorization. In contrast E[x+Yx] itself is positive.

### Artifacts, verification and limits

Reproduction commands, relative to this notebook:

```sh
python3 scripts/five-cell-penalty/neutral-certificate-473.py
python3 scripts/five-cell-penalty/check-neutral-473.py
```

The full certificate is `scripts/five-cell-penalty/neutral-certificate-473.json`.
It retains all moment rows, restricted Gram/LDL/inverse, every map
entry, all complete84-mode entries, separate prime components, pole,
response and diagonal errors, mixed terms, witness and source/input
hashes. The independent check output is
`scripts/five-cell-penalty/neutral-checks-473.json`.
All3695 checks pass: exact-rational Gram and pivot recurrences,
all inverse/map columns, explicit norm bounds, every new complete
entry and every core assembly, immutable core, nine prime powers,
and both independently associated negative scalar contractions.
The checker does not constitute an independent conceptual audit of
the imported identities or the entire enclosure implementation.
The optional `neutral-screen-473.py` and its JSON are proposals only.
No earlier certificate or unfinished work was overwritten.

The failed target is precisely the prescribed minimum-L2 correction
and1/2 inequality; stop it without enlarging20 or changing1/2.
A bounded exact-neutral graph alone does not pay the remaining middle
directions, graph-distant couplings, odd sector, exactly neutral smooth
approximation or all-window propagation. C744f does not automatically
control these new graph tails. The original response-prefix/coarse-box
and L750 stops remain unchanged. No RH-equivalent positivity input
has been assumed, and no actual-Xi sign is claimed.

### Separate conceptual audit — 11 November2026, step475

**Verdict and source scope.** The exact minimum-L2 map, norm bound and
(1) pass this audit under the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-11-11-five-cell-neutral-graph-audit-473.md`.
This is REPRODUCTION: independent local validation of the existing
quantitative obstruction, not a new source-exceeding theorem. The
Penrose1955/1956 results and their complex hypotheses are imported as
cited above; the already accepted C744b/c/e identities and elementary
arithmetic contracts are reused. No source sign or numerical supplement
is an input. The original unaudited calculation remains recorded above.

**Exact map and metric.** In physical output order the reflection pairs
are (0,+)/(4,-), (0,-)/(4,+), (1,+)/(3,-), (1,-)/(3,+), and
(2,+)/(2,-). Substitution reverses the exponential sign but does not
conjugate the test. Thus the same five representatives work over C;
there is no extra reality constraint. Surjectivity of A follows from
the five strictly positive exact Gram pivots. Copying each representative
to its partner embeds C^5 as precisely the reflection-fixed output
space, so the full ten equations are equivalent to the reduced five.
For every reservoir solution, its Euclidean coefficient norm equals
its function L2 norm in the orthonormal basis. Penrose applies to the equivalent
consistent system and identifies (2) without a change of objective.
The factor two from duplicated rows affects their residual norm, not
the set of exact solutions or the norm being minimized.

All Gram/LDL recurrences, inverse columns and20*64 map coefficients
are checked in exact Fraction arithmetic, including the quoted lower
pivot bounds. Each interval denominator excludes zero. Exact symmetry
of G^(-1), rather than symmetry of an interval rounding operation,
justifies its row-sum spectral bound. The squared Frobenius bound for
Y includes every entry and is strictly below37803^2. Neither the
recorded small residuals nor the point LDL rank is used for exactness.

**Domain and physical form.** C744c's accepted bounded response map
and C744e's cutoff argument apply to every fixed cosine sum through83:
the sum and its derivative are bounded; the two removed endpoint
collars have L1 norm O(epsilon) and uniformly bounded zero-extension
variation, including jumps. The squared logarithmic Fourier norm and
the shifted cosine-diagonal norm both tend to zero as
O(epsilon log(1/epsilon)). The finite delays, pole and moment maps are
L2-continuous, as is the entire response map. Taking both form limits
and polarizing gives (3) over C. This proves membership in the smooth
form closure, not the generator domain or an exactly neutral smooth
core. No uniform estimate in an infinite frequency index is needed.

The full-interval factor is n_q/sqrt(2) for moments and prime
correlations; the half-interval response factor is n_q. The even pole
is positive. The nine powers are precisely those below
exp(2a)=9sqrt(3) in (15,16), with the base-prime logarithm at powers.
The q=0 moment/prime formulas have positive denominators or their
explicit S_d(0) values. The geometric response expansion uses
u_83/c_512^2<0.03435<1 and all inverse powers through S_66.
Its remainder follows from the absolutely convergent double series:
sum_(m>=32)(m+1)R^m=R^32(33-32R)/(1-R)^2. The exponential correction
has magnitude at most exp(-2ac_512)S_2. The diagonal remainder uses
1+u/c_j^2>=1. These arguments include zero and repeated frequencies
and all mixed entries; no tail is inferred from a finite preview.

**Independent physical scalar evaluation.** The audit also avoids
the saved difference matrix entirely. It checks all48 printed witness
coefficients and all16 exact zeros, then recomputes the ten moment rows
at110 digits by integrating about each cell center. For beta=sigma/2,
h=ell/2 and t=t_j, set

    U=2[beta*sinh(beta h)*cos(kh)+k*cosh(beta h)*sin(kh)]/(beta^2+k^2),
    V=2[beta*cosh(beta h)*sin(kh)-k*sinh(beta h)*cos(kh)]/(beta^2+k^2).

The moment is (n_q/sqrt(2))[cos(kt)U-sin(kt)V]. These are the
integrals of exp(beta s)cos(ks) and exp(beta s)sin(ks) on (-h,h),
as verified by the antiderivative in C744b(10). This regrouping includes
q=0 and both signs. Every one of the840 refined intervals is contained
in its original interval. A fresh five-row Gram solve, contracting
the frozen x before solving, encloses the exact20 correction
coefficients inside the earlier rational map-contraction intervals.

For either real coefficient vector w=[x;0] or w=[x;Yx], put
d_q=n_q(-1)^q w_q and D_m=sum_q d_q u_q^m. The new scalar path forms
each signed response sum before squaring:

    sum_(j<512)(1-exp(-2ac_j)) [sum_q d_q c_j/(c_j^2+u_q)]^2.

The complete remaining rational tail is enclosed by

    sum_(m=0)^31 (-1)^m S_(2m+2) sum_(t=0)^m D_t D_(m-t),

with a symmetric error at most
(sum_q |d_q|)^2 [33 S_2 R^32/(1-R)^2+exp(-2ac_512)S_2].
Indeed expanding both denominators in the finite q,r sum gives the
displayed coefficient D_t D_(m-t); summing the absolute remainders
gives this bound. The finite coefficients are real here. The graph's
explicit scalar-tail remainder bound is <5.796e-48; roundoff and S_p
uncertainty are carried separately by directed operations. The accepted
S_p and gamma enclosures retain their independently audited infinite tails.

All84 digamma values are independently accumulated from the convergent
difference and its paid remainder. All nine arithmetic correlations
are evaluated on the full coefficient vector, retaining cross terms.
The pole is computed directly as the square of
exp(a/2)(1-exp(-a)) sum_q d_q(1/2)/(1/4+u_q), without the earlier
square-root grouping. For H[x], all ten original physical moment
squares are added with coefficient256; the graph uses unpenalized E.
Thus this scalar path evaluates exactly E[x+Yx]-H[x]/2, independently
of (4)'s stored matrix and its point proposal.

The refined elementary library uses the same directed contracts at
110 digits, Machin alternating sums through index159 with remainder
1/(321 n^321), and sine/cosine polynomials through degrees179/178
with error4^180/180! after reduction to |argument|<4. These bounds
follow from the same alternating-series and Taylor proofs as the
accepted library; precision alone is not an error estimate. The code
does not use floating special functions or regenerate the witness.

The independent scalar enclosures, rounded outward here, are

    H[x] in [4.47052368248947e-35,4.47052368249064e-35],
    E[x+Yx] in [2.22390669186959e-35,2.22390669187076e-35],
    E[x+Yx]-H[x]/2 in
      [-1.135514937572e-37,-1.135514937398e-37] < 0.

They overlap the earlier exact matrix contractions, and the full
independent difference interval lies within (1). This pays the
cancellation-sensitive sign through a different association of the
physical expression, not just replay of a floating eigenvalue.

Reproduction command:

```sh
python3 scripts/five-cell-penalty/audit-neutral-475.py
```

Full evidence is `scripts/five-cell-penalty/replay-475/audit.json`,
`core-scalar.json`, `graph-scalar.json`, and `neutral-checks-473.json`
in that directory. All979 new checks and all3695 original rational
checks pass; the latter report replays byte for byte. The accepted
core, inverse sums, gamma and library hashes match the step466 audit.
All eight pre-existing input artifacts remain unchanged. This is an
independent physical regrouping under the same elementary contracts,
not a second implementation of exp/ln/sqrt or a formal proof.

No mathematical repair was required. The fixed half-energy target is
now an audited stop. Both energies remain positive; unrestricted
middle directions, graph-distant couplings, odd signs, exactly neutral
smooth transfer and all-window positivity remain unpaid. In particular
neither L030-L032/C032a nor RH is resolved.

## Mathlib

Full matching formal coverage of this fixed physical restriction,
complete form, minimum-norm graph and scalar certificate has not
been checked. Standard finite-dimensional adjoints, positivity and
generalized inverses would be supporting machinery only. Unknown
availability is not evidence of absence; no matching theorem name
or formal verification is claimed.
