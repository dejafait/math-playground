# L095 — L094's frozen witness fails its complementary modes

## Hypotheses

Use L094's ordinary union-moment model at n=1024,d=10,w=68, divided
by L053's positive rho. Retain L021's original pairs, L073's included-
anchor five/six/seven base, L075's complete dictionary and seven-column
RREF/completion, L076's original column family, and precisely L086's
columns with t78=L083's s. In particular

    p8=16792471/1181138102168120460>0.

Freeze the complete 45-vectors `witness/z` and `witness/raw_moments` in
`scripts/finite-support/two-mixed-row-results.json`, as retained by L094's
separate conditional audit. Index z lexicographically by
0<=r,q<=8,r+q>=8, and put

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq.

Keep all 85 domain rows,90 original/weighted kernel equations,500 full
types/3000 presentations,36 forced entries,28 selected equalities,
43 entrywise-zero-old-block rows,rows23=(2,5) and 31=(3,4),45 signs,
full anchor and whole singular ranges. Ancestral PSD,uniqueness,
whole-kernel and coherent-normalization contracts from foundations/04,
09,10,12 remain conditional imports. This calculation does not
recursively audit those contracts or infer a representing measure.

## Conclusion

At this unchanged complete witness, exactly 14 of the 28 complementary
nonzero-old-block modes have strictly negative remainder; the other 14
are strictly positive. None is zero. In the convention i=9a+b the
negative indices are

    {5,7,14,16,24,32,34,40,42,50,52,58,60,68}.

The minimum normalized complementary remainder occurs at i=5,mode(0,5):

    -1055859074499109/10^6 <= b_5-A_5*z
                          < -1055859074499108/10^6 < 0.

The required lower bound is zero. A complete rational four-by-four
offending block and exact negative vector are saved under
`offending_block` in
`scripts/finite-support/l094-complementary-modes-results.json`.
The independent certificate below reconstructs that block and explicitly
transports a negative vector to the actual weighted mode block.

All 28 selected original/raw equalities remain zero. All 45 retained
mode inequalities pass, with 14 positive and 31 zero; row23 is exactly
zero and row31 has normalized remainder in [153320960,153320961).
The 43 zero-old-block rows have 13 positive and 30 zero remainders.
All 45 moments remain nonnegative, with 33 positive and 12 zero.
All frozen domain,kernel,dictionary and range controls pass.

This rejects precisely L094's complete assignment under the imported
contracts and preserves its necessary-subsystem pass. Other moment
completions at these columns,other columns/base/pairs,scalar upper rows,
other anchors,global moment consistency,representing measures and RS
realization remain unresolved. Arbitrary-center safety at 67/68 agreements
and the 955–957 bracket are unchanged. This is RESEARCH / REPRODUCTION
using assessed methods, an informative negative for the fixed assignment,
with no progress beyond the sources checked claimed. The separate conditional critical
review below retains this rejection.

## Proof

**Known results and applicability.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-19-l094-complementary-mode-residuals.md`.
Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47),Theorem 1 (51),III.A (52)–(59),III.B (64),printed
pp. 5–7, supplies the finite unequal-layer decomposition on ground sets
68,956 and principal restriction to layers 0,5,6,7,8. Retain both
rectangular directions,positive multiplicities and L078's coherent
positive normalization, independently retained in L091's conditional
audit. No actual-label averaging or suspect complement prefactor (61)
is used. These results supply no sign at the new witness.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2,Theorem 2.6 including both singular proof directions,
and Lemma 2.7, covers finite real symmetric blocks. Old PSD, the entire
cross vector in its range, and a nonnegative generalized-Schur remainder
are required even when the nonzero old block is singular. For any
verified B*x=c, its inverse cost is c^T*x: two solutions differ by a
kernel vector orthogonal to c. No quotient Euclidean pseudoinverse is
assumed. The concrete vector identity below exhibits a PSD violation;
it does not reprove a general theorem.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, IEEE TIT 65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),15 March 2017,
Section 1.1 (1)–(3),Proposition 1.1 and indicator proof p.2,Section 1.2 p.3,
supplies the ordinary union-moment model with constant weight retained.
There is no uniqueness,measure or common-center conclusion. These
general inputs are imported,not reproved. L093's different-witness
failure supplies only a calculation pattern; its residuals do not apply.

**Complete original/raw reconstruction.** Binomial coefficients outside
their ordinary range are zero. Use

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

Put S_l=C(68,l)C(956,l). In mode i=9a+b use the old layers l in
{5,6,7} satisfying l>=max(a,b). Reconstruct from the entire raw dictionary

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm), c_i=(T_l8), B_i*x_i=c_i.

Reconstruct the original pairs,rho,column RREF and completion,all 85
domain factors,all 90 affine original/weighted kernel equations,and
every one of 500 full keys in all six presentations,including Boolean
and forbidden cases. The 36 forced and 45 free entries are preserved.
All coefficient arrays agree with L094's complete source reconstruction;
both audited z/raw vectors agree entrywise with the frozen vectors.
The source reconstruction's old L086 residuals are regression controls,
not residuals at L094's moments.

For every mode reconstruct the entire old block,cross and affine inverse
action,including both rectangular directions. All 306 nonempty old
principal minors are nonnegative. Enumerate principal subsets by
increasing cardinality and lexicographic order; choose the last with
nonzero determinant,solve its cross restriction by Cramer's rule,and
fill zeros outside it. With the empty solution where appropriate,
direct substitution checks every coordinate of B_i*x_i=c_i and every
coefficient of the affine whole-range equations. The cost c_i^T*x_i
agrees with the saved full affine inverse action in all 81 modes.
Nonzero blocks are never assumed invertible.

Let F_i be the complete forced raw diagonal contribution,H_i the
constant-mode anchor correction,and define

    H_i=1_(i=0)*p8^2*S_8^2,
    D_i=C(68-2a,8-a)C(956-2b,8-b)>0, M_i=p8*D_i>0,
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-c_i^T*x_i)/M_i.

All forced terms,anchor terms and range-inverse costs are retained.
The entire original/raw identity at the frozen z is checked exactly:

    R_i=F_i-H_i-c_i^T*x_i
        +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)*p8*z_rq/V_rq
       =M_i*(b_i-A_i*z).

The complete rational rows,blocks,crosses,inverses,minors,costs,raw beta
coefficients and both residuals are saved under `rows` for all 81 modes.

**Partition and retained controls.** Let
I={9a+b:0<=a<=6,0<=b<=3}; determine Z by testing every entry of every
old block for zero,including empty blocks. Exactly 43 modes qualify,
including all 17 empty modes,and every whole cross vector on Z vanishes.
Let J=Z union {23,31}. Both added indices lie outside I union Z;
|I intersect Z|=20,|J|=45 and |I union J|=53. Its exact complement is

    {4,5,6,7,14,15,16,24,25,32,33,34,40,41,42,43,
     49,50,51,52,58,59,60,61,67,68,69,70}.

Every one of81 entrywise membership decisions agrees with L094.
Every retained original/raw remainder agrees with L094's complete saved
value. All equalities,signs and retained inequalities have exactly the
counts and two added-row values in Conclusion. The same frozen45-vector
is substituted in every complementary row. Exact comparison gives the
14 negative indices above and14 positive remainders; integer cross
multiplication verifies the displayed interval at the minimum i=5.

**Full negative block and actual weighted transport.** At i=5,old layers
are 5,6,7. Put d=F_5-H_5 plus the complete free raw beta sum,and form

    C=((B_5,c_5);(c_5^T,d)), v=(-x_5,1).

All 16 block entries and all four vector coordinates are saved exactly.
Since B_5*x_5=c_5, direct multiplication checks

    v^T*C*v=d-c_5^T*x_5=R_5=M_5*(b_5-A_5*z)<0.

The independent verifier also reconstructs the full diagonal from all 81
actual raw orbit values and uses the full affine inverse action rather
than the sparse principal solution. Both vectors have the same negative
quadratic value in the same full block.

For the actual weighted block use the retained monic orthogonal factors
h_(n,l,a),their squared norms nu_(n,l,a) under weights
C(8,i)C(n-8,l-i),and direct subset-transition coefficients g. All complete
norm and transition arrays are consumed from the independent audited
source. For every nonzero beta set

    sigma_(n,l,m,a)=nu_(n,l,a)*g_(n,l,m,a,k)/beta(n,l,m,a,k).

The verifier checks positivity and independence of k for every used
ratio; a zero beta has zero action. At(a,b)=(0,5),put

    N=nu_(68,8,0)*nu_(956,8,5),
    D=C(68,8)*C(946,3), alpha=N/D=76721335004160/97169059>0,
    s_l=sigma_(68,l,8,0)*sigma_(956,l,8,5)/alpha.

For l=5,6,7,8 all computed scales are exactly 1. Independently reconstruct
each full weighted entry,including both rectangular directions,as

    W_lm=nu_(68,l,0)*nu_(956,l,5)
         *sum_(j,k=0)^min(l,m)g_(68,l,m,0,j)g_(956,l,m,5,k)Y_lm(j,k).

This nonconstant mode has no anchor subtraction. Every entry satisfies

    W=alpha*diag(s_5,s_6,s_7,1)*C*diag(s_5,s_6,s_7,1)=alpha*C.

For the independently computed range vector v', the transported vector
diag(s_5,s_6,s_7,1)^(-1)*v'=v' has last coordinate1 and quadratic value
alpha*R_5<0. The product-mode multiplicity is 6550452053781>0. Thus the
retained source decomposition places a non-PSD block in the prescribed
matrix. This is an exact rational vector certificate,not a numerical
eigenvalue. Complete weighted entries,scales,vector and negative value
are under `actual_congruence` in the independent certificate.

**Independent arithmetic and scope.** The independent original-row
calculation uses

    e(n,a,r)=sum_(h=0)^r(-1)^h C(a,h)C(8-a,r-h)C(n-8-a,r-h)

and checks beta(n,8,8,a,8-r)=C(n-2a,8-a)*e(n,a,r) for every used
coefficient. It independently obtains the bounds from the full affine
inverse action,checks every original/raw identity and retained control,
and performs the complete diagonal/block/transport checks above.

Reproduce without a constructor,optimizer or pivot replay:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/l094_complementary_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_l094_complementary_modes.py

The first calculation has 1216 passing checks; the independent verifier
has 2049,with no failures. Complete certificates are respectively
`scripts/finite-support/l094-complementary-modes-results.json` and
`scripts/finite-support/l094-complementary-modes-verification.json`.
They consume complete relevant arrays and verify all exact identities;
previews and saved success flags do not establish this verdict.

No mathematical reconstruction discrepancy arose. No moment,column,
pair,base or constraint was changed. No full-row/conic solve was
restarted; all previous stops and fixed-assignment rejections remain.
This initial calculation verifies arithmetic for one frozen assignment.
The separate review below retains its conditional conclusion. Neither
calculation excludes other completions or improves the Reed–Solomon boundary.

**Separate conditional critical audit, 2026-10-19 (step 348).** The
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-19-l095-fixed-witness-rejection-critical-audit.md`
approves this exact review. The named theorems and hypotheses above
are imported without reproof. The audit consumes the complete L094
source arrays, preserving their conditional ancestral contracts; it does
not recursively audit their derivation. Hash binding and full array
comparisons retain the 85 domain rows, 90 affine kernel equations,
500 types/3000 presentations, 36 forced entries and complete frozen
45-coordinate z/raw witness. Earlier L086 residuals remain regression
controls only. The 7993 prior source checks are reused, not rerun here.

A fresh run of the independent verifier agrees with every complete
current saved row, sign list, diagonal term, block, vector and weighted
certificate. Additional arithmetic reconstructs all old blocks and both
cross directions from the raw dictionary, all original row coefficients,
all full affine range equations, all 306 old principal minors, fresh
principal range solutions and their costs. For each of 81 modes it sums
all 81 raw diagonal terms and all 81 direct-transition weighted terms,
retaining the constant anchor correction, and verifies

    raw remainder = p8*D_i*(b_i-A_i*z),
    weighted remainder = p8*N_i*(b_i-A_i*z).

Here D_i,N_i are strictly positive as defined above. Every entrywise
membership decision, the 53/28 partition, every selected equality and
every retained original/raw control agrees. All 28 complementary signs,
the exact negative-index set and the minimum interval in Conclusion
are retained. The 45 moment signs and both added rows retain their
stated counts and values. No moments were retuned.

For mode (0,5), the old three-by-three block is nonzero and rank one:
all its two-by-two minors vanish, while an entry is nonzero. Thus it is
singular. Both the sparse principal solution and the full affine inverse
solve every range coordinate. Each corresponding full four-vector has
quadratic value R_5<0 in the same reconstructed four-by-four block.
Every direct-transition weighted entry, including both rectangular
directions, agrees with alpha times the raw block; all four scales are
one, alpha=76721335004160/97169059>0, and multiplicity is
6550452053781>0. Both transported vectors give alpha*R_5<0. These full
identities, rather than a nonsingular-block shortcut or saved success
flag, retain the fixed-assignment rejection.

The audit command was

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_l095.py

All 2049 fresh independent verifier checks and 1565 additional audit
checks pass, with no failures. Complete exact evidence is saved in
`scripts/finite-support/l095-critical-verification.json` and
`scripts/finite-support/l095-critical-audit.json`, with the run log in
`scripts/finite-support/l095-critical-run.log`. The latter certificate
contains every current raw/weighted diagonal term, row residual, full
negative block, both vectors, complete weighted block, scales and
quadratic values. The script refuses to overwrite an existing main
audit certificate; reproductions should select a fresh output path.
No mathematical discrepancy arose. This is a conditional critical
verification of an existing finite input, not progress beyond the cited
methods, a uniform exclusion at these columns, or a change to the RS
boundary. The proof's direct mathematical inputs are unchanged.

## Mathlib

Full matching fixed-witness rejection:not checked. Supporting singular
Schur,unequal-layer decomposition and exact rational arithmetic coverage:
not checked here. Unknown availability is not absence. General results
are imported by precise citations without a novelty claim.
