# L089 — L088's fixed witness fails sixteen omitted mixed modes

## Hypotheses

Retain precisely L076,L078,L082,L083,L086,L087,L088's ordinary moment
slice: n=1024,w=68, L021's pair prescription, L053's positive singleton
rho, matrices divided by rho, L073's included-anchor five/six/seven
base and L075's entire immutable dictionary. Preserve the original
seven-column RREF/completion and all ancestral PSD, uniqueness,
whole-kernel-exhaustion and coherent-normalization qualifications.
This calculation does not recursively audit those inputs.

Fix the columns to L086's exact parameters: the first four coordinates
of `witness/original` in
`scripts/finite-support/affine-sign-phase-one-results.json` are
(1,t56,t63,t69), and t78 is L083's stationary s. Fix the entire new
45-moment witness `witness/z` in
`scripts/finite-support/fixed-column-new-only-results.json` to L088's
values, not L086's different moments. Consume all rational coordinates
in full. Keep

    p8=16792471/1181138102168120460>0,
    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq.

Here C(n,k) is the binomial coefficient, zero outside 0<=k<=n. The
45 free indices are lexicographically ordered (r,q) with 0<=r,q<=8
and r+q>=8. Freeze every other datum: original pairs, 85 domain rows,
90 weighted kernel equations, 500 types/3000 presentations, all 36
forced eight/eight entries, Boolean cases, forbidden distinct distances
and full anchor. No solve, retuning, scalar upper row, other-anchor
constraint, labeled restriction or global extension is added.

Index modes by i=9a+b, 0<=a,b<=8. Let

    I={9a+b:0<=a<=6,0<=b<=3},
    J={9a+b:max(a,b)=8}, K={0,...,80}\(I union J).

The sets have sizes 28,17,36 respectively. L088 supplies the equality,
new-only and sign controls on I,J and z. This lemma evaluates K at
exactly the same witness.

## Conclusion

Sixteen of the 36 omitted mixed inequalities fail strictly; the other
20 pass strictly. The negative original indices are exactly

    6,15,23,25,31,32,34,42,49,50,52,60,64,66,67,68.

All 28 selected equalities remain zero; the 17 new-only modes retain
11 positive and six zero slacks. The moments retain 31 positive and
14 zero coordinates. All 81 original/raw identities and all singular
range equations pass, with all 306 old principal minors nonnegative.

The smallest mixed scaled remainder is in mode (7,1), index 64:

    -4587146655180994/10^6 <= sigma_64
       < -4587146655180993/10^6 < 0.

A particularly simple negative mode is (7,3), index 66: its old block
is the one-by-one zero matrix, its cross vector is zero and it has no
anchor term. Its raw remainder is the negative diagonal entry itself,
and equals

    R_66=(1782682793617737/363922042337)*sigma_66 < 0.

Thus the included-anchor matrix with exactly L088's columns AND moments
is not PSD. This rejects only this complete assignment. L088's necessary
subsystem remains feasible. Different moments at these columns, other
zero-plane points, scalar upper rows, other anchors, global consistency,
other base/pair choices and RS realization remain unresolved. There is
no uniform family bound or improvement of the 955–957 bracket.

This is a RESEARCH / REPRODUCTION specialization of known criteria,
an informative negative result for this fixed completion, without a
source-level novelty claim. The separate critical proof review below
retains this fixed rejection with its ancestral qualifications.

## Proof

**Known imports and applicability.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-new-only-witness-mixed-mode-residuals.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Ground sets 68,956 and principal layers 0,5,6,7,8 meet
the unequal-layer hypotheses. Retain L078's coherent positive
congruence, both rectangular directions and positive mode multiplicities.
The suspect complement prefactor (61) is unused. A negative diagonal in
any of these blocks contradicts PSD, including a singular old block.

For the complete mixed-mode check retain Takashi Sano, *Moore-Penrose
inverse, generalized Schur complement and inertia*, version of record
27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. Finite real
symmetric PSD old blocks, including singular/empty blocks, satisfy its
hypotheses when the checked cross vectors lie in their ranges. No
Euclidean quotient pseudoinverse, Slater or attainment assumption is used.
Retain Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Sections 1.1 (1)–(3), Proposition 1.1 and its complete
indicator proof p.2, Section 1.2 p.3, for ordinary union moments. Its
proof gives the constant-weight statement despite its final displayed
notation. No actual-label restriction is averaged. Foundations/04,09,
10,12's qualifications remain. General results are imported without
reproof; none evaluates this particular rational witness.

**Exact formulas.** Put S_l=C(68,l)C(956,l) and

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

For mode i=9a+b retain old layers l in {5,6,7} with l>=max(a,b).
After eliminating the positive anchor, its source entries are

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m.

Let B_i=(T_lm) on the old layers, c_i=(T_l8), and solve B_i*x_i=c_i.
Retain all equations, including zero rows. Set

    D_i=C(68-2a,8-a)C(956-2b,8-b)>0,
    H_i=1_(i=0)*p8*S8,
    F_i=sum_(forced j,k) beta(68,8,8,a,j)beta(956,8,8,b,k)Y_88(j,k)/(p8*D_i),
    b_i=F_i-H_i-c_i^T*x_i/(p8*D_i),
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    sigma_i=b_i-A_i*z.

The unnormalized raw remainder, retaining all forced terms and the
full constant-mode anchor, is

    R_i=sum_(forced j,k) beta(68,8,8,a,j)beta(956,8,8,b,k)Y_88(j,k)
        +sum_(free r,q) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)Y_88(8-r,8-q)
        -1_(i=0)*p8^2*S8^2-c_i^T*x_i
       =p8*D_i*sigma_i.

All scales are positive. With the qualified old PSD base and checked
ranges, each required mixed Schur inequality is sigma_i>=0. For the
load-bearing index 66, B_66=[0], c_66=[0], H_66=0 and the cost is zero;
therefore R_66 is also the source diagonal. Its strict negativity alone
rejects this assignment, without choosing an inverse of a nonzero block.

**Frozen reconstruction and controls.** Consume the complete step-318
witness, reconstruction and verification, and step-320 critical source,
verification and audit certificates. Check their input hashes, full
coordinate arrays and relevant original data, rather than success labels
or previews. Rebuild the 85-factor family from L076's original RREF
with nonpivots 56,63,69,78. Every factor is nonnegative. Rebuild all
150 affine column coordinates and both sets of 90 equations, retaining
actual orbit weights and anchor. Every coefficient residual is zero.

Reconstruct all types using atoms
(956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i) and all six bit-permuted
presentations. Boolean repetitions, forbidden cases and reanchorings
outside retained layers agree with the full immutable dictionary.
Exactly 36 eight/eight entries are forced and 45 distinct keys are free.
All reconstructed records and kernel arrays agree in full with steps
318 and 320. The seven-completion uniqueness and underlying normalization
remain imported qualified inputs, not newly proved by this comparison.

Rebuild all 81 source matrices, affine crosses, forced terms, anchors,
raw beta coefficients and original rows. Check every affine inverse
residual. Fresh Cramer solves on largest nonsingular principal subsystems
verify every fixed-point equation and agree in energy with the saved
affine inverse. Recompute all 306 nonempty old principal minors; each
is nonnegative. Every original bound agrees with its complete saved
quadratic, and every coefficient/bound agrees with both step-318 and
step-320 evidence. No old L086 residual is used as a new L088 residual.

Only then substitute the unchanged full L088 z and raw arrays. The sets
I,J,K partition all 81 indices exactly. On I, all original/raw residuals
are zero. On J the 11-positive/six-zero pattern is unchanged, as are all
45 signs. On K, the 16 negative indices above and 20 positive indices
exhaust the set, with no zeros. Check R_i=p8*D_i*sigma_i separately in
all 81 modes. All exact failing original AND raw reduced fractions are
saved in `failing_remainders` and `rows/i` of
`scripts/finite-support/new-only-witness-mixed-modes-results.json`.
No failure is discarded or replaced by a rounded value.

**Independent check and full negative certificate.** The separate verifier
uses L078's eigen formula

    E_(n,a)(r)=sum_(h=0)^r (-1)^h C(a,h)C(8-a,r-h)C(n-8-a,r-h),
    A_(i,rq)=-E_(68,a)(r)E_(956,b)(q)/V_rq.

It checks every beta/eigen coefficient identity, reconstructs original
bounds from the ancestral cross/inverse/forced arrays, retains the full
anchor and checks every inverse row. All 81 original/raw remainders and
the complete mixed sign partition agree. For index 66 it also directly
sums all 81 source diagonal terms from the full forced/free dictionary,
without using its saved forced term or inverse cost. This exact sum is
R_66<0; all terms are saved as `load_bearing_81_terms` in the verification
certificate. In particular p8*D_66=1782682793617737/363922042337>0.

The full reduced rational sigma_66=N/Q is below. N<0,Q>0, and the
verifier checks every digit against the independent exact substitution.
The raw value is the positive multiple above. The full rational values
for every other failure are retained without truncation in the results
and verification certificates.

```text
N=-280625918632517636963295232492956838512670903462740274613558657834795119118968523065554771870092833003661422546819540143468562265235369088795435482825264293547480704362255439932472003463276573845576735208450001625880357838658100538044520045020127054743848135174912013920112881906903269172534123144811790520905247882076711106332901259454169128980666158101596158288589880471828477174753863899810899514740397549409704512328352385143400782268239008559710242366130299653537714850288628026777013737227047777637884527762721667867484925578339808431951
Q=1304899245113497606859386518765422668691186098501338679062237811317679307409621474194571015635677438030992470301117696029061474194261109459615866753923543222682544332914286396382871372323670215801658278880539728146078722454740746223544922739607082153521500841178758548875643737103006498122114147941404965670001895130709926474165726973982086883942007472246720835341768133448065401910726231716475162001882279498762636863684000853552227589917896442812449819485977272302476734302796480836365978290810490586434273679246661953800737164600687500
```

Reproduce from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/new_only_witness_mixed_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_new_only_witness_mixed_modes.py

The first certificate passes 1083 checks with no failures. The independent
verifier passes 509 checks with no failures; its result is recorded in
`scripts/finite-support/new-only-witness-mixed-modes-verification.json`;
it invokes neither constructor nor optimizer. Its additional direct
diagonal and full-manuscript checks do not replace a later dedicated
critical proof review. There is no new solve, scan, retuning, separator
or revival of the capped full-row/conic attempts.

**Separate critical proof review — step 324, 2026-10-18.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-new-only-witness-mixed-mode-critical-audit.md`.
The review retains the complete fixed-assignment rejection, with the
precise Schrijver, Sano and Polak imports and qualifications above.
It establishes a reviewed local input, not mathematics beyond those
sources or a recursive audit of ancestral PSD, uniqueness, whole-kernel
exhaustion or source decomposition. Reproduce without a constructor,
optimizer, candidate change or new separator:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_new_only_witness_mixed_modes.py

The inspected L087 audit reconstructs the unchanged source into
`scripts/finite-support/new-only-witness-mixed-modes-critical-source.json`.
All 7993 checks pass. It rebuilds the original pair equations, positive
rho and p8, seven-column RREF/completion, the entire immutable dictionary,
all 85 domain factors, 150 column coordinates, 90 weighted and original
kernel equations, 500 types and 3000 actual-support presentations.
Both rectangular directions of all 220 subset transitions are checked
against freshly generated monic orthogonal bases. Every positive
normalization ratio and reference-layer triangle identity is retained.
The source audit evaluates L086's OLD moments as a regression control;
its 19 failures are not the verdict at L088's different moments.

For every mode, the source reconstruction verifies the entire affine
range equation, all old principal minors and a fresh Cramer solution
on a largest nonsingular principal subsystem. Reverse weighted
elimination keeps zero-pivot rows and cross coordinates. The 81 old
blocks have sizes three, two, one and zero with counts 36,13,15,17;
all 306 nonempty old principal minors are nonnegative. Both the source
and weighted energies agree under one coherent positive congruence,
with the full constant-mode anchor. Whole-space source exhaustion and
its positive multiplicities stay the stated qualified imports.

The original/raw verifier is rerun into
`scripts/finite-support/new-only-witness-mixed-modes-critical-verification.json`;
all 509 checks pass. Every full row, sign partition, 81-term load-bearing
sum and complete manuscript rational agrees with step 322. The
additional dedicated audit passes 8124 checks with no failures; its
complete evidence is
`scripts/finite-support/new-only-witness-mixed-modes-critical-audit.json`.
Complete step-318/320 witness, coefficient, range, presentation and
kernel arrays are consumed and compared, not inferred from hashes or
success counts. The entire 45-coordinate z and raw vector agree with
L088's critically reviewed witness. Its algorithmic provenance remains
that of L088; no saved pivot sequence is optimized again.

For a further independent diagonal reconstruction, use the cited Johnson
relation eigenvalues E_(n,a)(r) displayed above. For each of all 81 modes,
sum all 81 actual moments, with the forced Boolean, forbidden and
reanchored values included:

    d_i=sum_(r,q=0)^8 E_(68,a)(r)E_(956,b)(q)Y_88(8-r,8-q).

The raw source diagonal before anchor subtraction is D_i*d_i. The
independently reconstructed subset-action coefficients give precisely
the same E-products in every one of these 6561 terms. If N_i is the
product of the two positive squared basis norms on layer eight, the
weighted diagonal is N_i*d_i. Its constant-mode anchor correction is
N_i*p8^2*S8, whereas the source correction is p8^2*S8^2;
D_0=S8 makes these the same coherent congruence. The checked weighted
energy divided by p8*N_i equals the source energy divided by p8*D_i.
Thus the direct original substitution, full raw diagonal-minus-anchor-
minus-energy sum, and weighted remainder agree in all 81 modes.
Complete sums, fractions and all sixteen failures are saved; none is
replaced by a rounded sign test.

All 28 selected equalities remain exactly zero, all 17 new-only modes
retain eleven positive and six zero values, and all 45 moments retain
31 positive and 14 zero values. The remaining 36 modes have exactly
the sixteen negative indices in the conclusion and twenty positive
values. The minimum remains index 64 with its stated strict rational
interval. For index 66, direct reconstruction gives old layer [7],
B_66=[0], c_66=[0], and zero anchor and energy. Reversing the full
source-intersection order matches all 81 terms of the step-322 raw
sum individually. Its positive scale is exactly
1782682793617737/363922042337. The reduced numerator and denominator
agree digit-for-digit with N,Q above, and

    -215055621867655644/10^12 <= sigma_66
        < -215055621867655643/10^12 < 0.

Hence the negative diagonal itself contradicts PSD. This conclusion
requires neither a choice of inverse for that zero block nor a sign
assumption on a different completion. The complete sixteen-failure verdict
retains the checked singular-Schur hypotheses; no uniform exclusion of
other moments or columns follows.

An initial additional-wrapper run stopped before its verdict because
step 318 calls its scale `positive_raw_normalization`, while step 320
calls it `norm`. The preserved partial checkpoint is
`scripts/finite-support/new-only-witness-mixed-modes-critical-initial.json`.
Correcting that schema mapping changed no input or mathematical value.
The completed wrapper used `--reuse-reconstruction` to consume the
already successful fresh source/verifier artifacts without repeating
their work. The unflagged command above performs the whole reconstruction.
No failed mathematical comparison was suppressed. L088's feasible
necessary subsystem, the prior full-row/conic stops and all unresolved
scalar, other-anchor, global-consistency and RS questions remain intact.
The 955–957 bracket is unchanged.

## Mathlib

Full matching fixed-witness rejection: not checked. Supporting rational
elimination, singular Schur and invariant unequal-layer results: not
checked here. Unknown availability is not absence. The known criteria
are imported by precise citation; no claim of source-level novelty is made.
