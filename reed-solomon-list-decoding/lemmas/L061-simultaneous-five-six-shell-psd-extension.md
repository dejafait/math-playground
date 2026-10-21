# L061 — The minimizing columns admit a simultaneous five/six-shell extension

## Hypotheses

Use L053's 1024-point ground set H, all 68-subsets, positive singleton rho
and unchanged pairs rho*p_i, in particular
p5=1/68881143660 and p6=133/9357995374380. Fix one 68-subset D.
Retain L056's complete anchored five-shell and, for every G with
|D\G|=6, the entire L060 minimizing column at its unchanged parameter s_*.
Add all indices {D,G} simultaneously. Their diagonals and entries against
{D} are rho*p6. Require one moment for each represented unordered triple,
including presentations at other eligible anchors, zero whenever any
pair has half-distance 1,...,4, and nonnegative remaining entries.
No extra scalar upper inequalities or actual-label restrictions are imposed.

Only the finite real symmetric matrix indexed by {D} and every {D,E}
with |D\E| in {5,6} is tested. Global moments, other conditioned matrices
and measures are not assumed. The fixed columns and their parameter may
not be replaced. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-14-simultaneous-five-six-shell-extension.md`.

## Conclusion

There is a rational nonnegative assignment of every remaining entry for
which this entire anchored matrix is PSD, preserving all fixed entries
and every represented unordered moment. The complete generalized-Schur
remainder has 49 representation coordinates: 20 positive and 29 zero.
These counts refer to product modes, not their full-space multiplicities.

This parks the fixed simultaneous-shell prescription as an exclusion
diagnostic. It is a finite reproduction/specialization of assessed algebra
and PSD methods, without a claim of progress beyond the checked literature.
It supplies no full SDP feasibility, uniform support cap, representing
measure, ordinary packing or common-center RS list. Arbitrary-center safety
at 67/68 agreements and the 955–957 bracket are unchanged. The separate
critical proof review below retains this conclusion.

## Proof

**Imported algebra and singular criterion.** Import Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE Trans. Inform. Theory 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
(7), Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59),
III.B (64), printed pp. 2,5–7. Foundations/04 gives the beta convention;
foundations/09 records the unequal-layer theorem and inspected proof.
The theorem applies to ordinary invariant relation matrices, without a
code or representing measure. Here the factor sizes are 68 and 956 and
the selected layers are 0,5,6, lying in the stated ranges. Principal
restriction of the complete source decomposition retains precisely the
blocks described below, including every nontrivial and singular mode.
No complement prefactor or impossible scalar orbit is used.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum (27 February 2026),
DOI 10.1007/s44146-026-00231-y,
[Section 2, Theorem 2.6 and Corollary 2.2](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For a retained PSD block C, cross block T and new block A, the conditions
are T^T ker C=0 and A-T^T C^dagger T PSD. These allow singular C.
The union-index interpretation is Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and its indicator proof, p. 2, with the
constant-weight qualification in foundations/12. Nonnegative coordinates
are explicit in Brouwer–Polak,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1), Section 2 (1), p. 2.
The general source results are not reproved. Exact entry and block
calculations are necessary because none supplies this fixed verdict.

**Complete entry dictionary.** A layer-l support is
E=(D\X) union Y, |X|=|Y|=l. The stabilizer S_68 x S_956 of D is
transitive on ordered pairs of layers l,m with prescribed
i=|X intersection U|, j=|Y intersection V|, where
G=(D\U) union V, |U|=|V|=m. The eight membership-atom sizes in mask
order 0,...,7 (bits D,E,G having weights 4,2,1) are

  (956-l-m+j, m-j, l-j, j, i, l-i, m-i, 68-l-m+i).

All are nonnegative for the ranges used here; they sum to 1024 and
reconstruct the three supports. Conversely these sizes determine an orbit:
bijections on corresponding atoms extend to a point permutation fixing D.
Thus the 36 five/five, 36 five/six and 49 six/six types exhaust the entries.
This is full-region symmetry, without actual-label averaging.

Let d5_(r,q) be L056's coefficients including d5_(0,0)=1 and forbidden
coefficients zero. Let t_(i,j) be L059's complete affine column evaluated
at L060's s_*=-B0/(2A); its fixed and forbidden values remain unchanged.
The five/five moment divided by rho is p5*d5_(5-i,5-j); the five/six
moment is p5*t_(i,j). Every t entry is rational and nonnegative by L060.

For six/six write r=6-i,q=6-j and use normalized coefficients d6_(r,q).
Set d6_(0,0)=1 and d6_(r,q)=0 when 1<=r+q<=4.
When r+q=5, reanchor at E: its five-neighbor is G and six-neighbor is D.
The column intersections at E are (q,r), so the required value is

  d6_(r,q)=(p5/p6)*t_(q,r), r+q=5.

The remaining 28 relations r+q>=6 are free nonnegative coordinates.
Each new Boolean diagonal and anchor entry is rho*p6, independently
of a distinct-triple formula.

All six support permutations of all 121 types are checked directly against
full atom representatives. The 434 prescribed presentations agree, including
the five/five versus five/six overlaps. The independently completed check
also compares all 726 presentations, including six/six values. For the free
equilateral-six types an alternative six-shell anchor has the same r,q:
the common region 62-r determines r, and r+q=6 then determines q.
For a nonequilateral six/six type its anchor is unique unless the third
distance is five, which is the fixed case above. This explains why no
extra free-coordinate equality is omitted. Canonical atom tuples minimized
over all six permutations also agree across all relation types. Nonnegative
entries and forbidden zeros are checked for the entire completed dictionary.
The recipe is equivariant under the stabilizer of D and transports under
point bijections to any D. No averaging of labeled constraints is asserted.

**Full mixed-layer reduction.** Divide the matrix by positive rho.
The anchor has entry 1 and vectors p5*1 and p6*1 against the two shells.
Eliminate this positive anchor by congruence on the entire matrix; the
shell blocks acquire the subtractions p_l*p_m*J. Do not transport a
pseudoinverse by congruence. Set S_l=binomial(68,l)binomial(956,l).
For n in {68,956}, define the source integer

  beta(n,l,m,a,t)=sum_(u=a)^(n-a) (-1)^(u-t) binomial(u,t)
    binomial(n-2a,u-a)binomial(n-a-u,l-u)binomial(n-a-u,m-u).

Only nonvanishing terms contribute, so u>=t and u<=min(l,m).
For each (a,b) in {0,...,6}^2, put
D_l(a,b)=binomial(68-2a,l-a)binomial(956-2b,l-b).
Layer 5 occurs exactly when a,b<=5; layer 6 occurs in all 49 modes.
Every surviving D_l is positive. The imported beta block after anchor
elimination is [C55,C56;C56,C66] when layer 5 occurs, and [C66] otherwise,
where

  C55=p5*sum_(r,q) beta(68,5,5,a,5-r)beta(956,5,5,b,5-q)d5_(r,q)
       -1_(a=b=0)*p5^2*S5^2,
  C56=p5*sum_(i,j=0)^5 beta(68,5,6,a,i)beta(956,5,6,b,j)t_(i,j)
       -1_(a=b=0)*p5*p6*S5*S6,
  C66=p6*sum_(r,q) beta(68,6,6,a,6-r)beta(956,6,6,b,6-q)d6_(r,q)
       -1_(a=b=0)*p6^2*S6^2.

For absent layer 5 set C55=C56=0. This padding is notation, not an
additional coordinate. The constant-mode anchor beta entries are
p5*S5,p6*S6, which explains these corrections.

The implementation verifies the diagonal normalization for every factor
and relation:

  beta(n,l,l,a,l-r)=binomial(n-2a,l-a)*E_(n,l,a)(r),
  E_(n,l,a)(r)=sum_(h=0)^r (-1)^h binomial(a,h)
                       binomial(l-a,r-h)binomial(n-l-a,r-h).

Consequently C55=p5*D5*lambda5, exactly recovering all 36 audited L056
Schur eigenvalues. At every zero lambda5, C56 is exactly zero; no numerical
tolerance or inversion of a zero mode is used. On positive modes the
required C66 lower value is C56^2/C55. On every other mode it is zero.
Sano's criterion is therefore reduced to these complete scalar remainder
inequalities, not merely their diagonal average.

The mode multiplicity is
m_(a,b)=(binomial(68,a)-binomial(68,a-1))
         *(binomial(956,b)-binomial(956,b-1)).
All are positive. Their sum over the 49 modes is S6, and over the 36
old modes is S5. The complete source decomposition, not just these
dimension identities, guarantees exhaustion of the actual spaces.
As an independent rectangular normalization check, define
eta_(a,b)=C56^2/(C55*p6*D6) for positive C55 and zero otherwise.
Then p6*m_(a,b)*eta_(a,b)/S6 equals the corresponding audited L060
one-column energy contribution in every mode; summing these and p6^2
recovers its exact E_min. All 36 comparisons and the sum agree.

**An explicitly defined rational witness.** List
R={(r,q):0<=r,q<=6,r+q>=6} in lexicographic order, numbered 0,...,27.
For R write z_(r,q)=v_(r,q)*d6_(r,q), with positive valency

  v_(r,q)=binomial(6,r)binomial(62,r)binomial(6,q)binomial(950,q).

Number the modes by h=7a+b. Define the complete rational matrix and vector

  H_h(r,q)=E_(68,6,a)(r)*E_(956,6,b)(q)/v_(r,q),
  A_hj=-H_h(R_j),
  B_h=1+sum_(r+q=5) d6_(r,q)E_(68,6,a)(r)E_(956,6,b)(q)
      -1_(a=b=0)*p6*S6-eta_(a,b).

The full condition is z>=0 and A*z<=B. These are exactly C66's
remainder divided by positive p6*D6; no new scalar condition is added.

Set z_21=z_22=0. Let J=(0,1,...,20,23,24,25,26,27) and

  I=(1,2,3,5,7,8,9,11,14,15,16,17,18,21,22,23,24,25,
     28,29,30,31,35,36,37,42).

Define the other 26 entries as the unique solution A_(I,J)*z_J=B_I.
Equivalently, each is the determinant of A_(I,J) with its column replaced
by B_I, divided by det A_(I,J). This fully specifies exact rational
numbers using the established inputs, without a numerical solver or a
choice of unspecified feasible point. The exact determinant is

  4655613325456352295608795245483821198395479150214935586177189640651936371688166814740376517239532820621441325172309098496/
  236753394070781148279192381771397427851495677624628478157064785404345658466176578544599641268768417047537275623214093954950024363901346724990322201165326987393200397491455078125,

which is positive. Full evaluated fractions of all 28 entries and all
49 slacks are in the certificates below. Exact substitution checks every
entry and every inequality: all 28 z entries are nonnegative, and B-A*z
has exactly 20 positive and 29 zero entries. For example z_0=85667/3;
the full witness, not this example, is used in verification.
It follows that every complete source block is PSD, including the
singular ones. The source block theorem and invertible anchor congruence
give PSD of the entire original finite matrix. Nonnegative d6 and full
unordered consistency were already checked for this same assignment.

**Exact evidence and qualifications.** Run from the notebook:

  `python3 scripts/finite-support/simultaneous_five_six_shell.py`

The full certificate `scripts/finite-support/simultaneous-five-six-shell-results.json`
stores source hashes, all atom presentations and prescribed values, all
49 blocks and normalizations, every LP coefficient, the full rational
witness and every slack. Decimal phase I proposes a basis in 196 pivots;
only exact Fraction reconstruction and substitution are used in the proof.
All 1668 constructor checks pass. A solver status would not suffice.

Independently run

  `python3 scripts/finite-support/verify_simultaneous_five_six_shell.py`.

This verifier imports neither the constructor nor an optimizer. It obtains
s_* from the three complete manuscript coefficients of L060, builds all
36 minimizing column entries directly from L059's affine input, and
reconstructs every completed atom presentation. It directly evaluates the
full beta blocks, verifies the 20 old singular cross zeros, computes all
49 exact generalized-Schur remainders, and compares every complete LP row,
witness entry and slack. It checks the explicit 26-by-26 determinant and
the six-shell Boolean trace sum m_(a,b)*C66/(p6*D6)=S6*(1-p6).
All 1928 independent checks pass, with no failures. Its complete blocks,
fractions, moments, determinant and check names are in
`scripts/finite-support/simultaneous-five-six-shell-verification.json`.
The complete witness fractions, failure lists and determinant were inspected;
the verifier consumes and checks every load-bearing entry, not a preview.

This arithmetic verification is distinct from the critical proof audit below. No
optimality of the six-shell witness or of a larger SDP is claimed. The
above-threshold singleton objective is unchanged. Scalar/label constraints,
global moment consistency and PSD, measures and RS realization remain
independent gaps. The earlier smaller diagnostic stops are preserved.

**Separate critical proof review — step 205, 2026-10-14.** Reuse the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-14-simultaneous-five-six-shell-critical-audit.md`.
The review retains the hypotheses and conclusion, with no changed
coefficient, source theorem or boundary claim. It verifies this local
reproduction, without claiming a result beyond the checked literature.

For every one of the 121 relation types, construct actual D,E,G as
68-subsets of a 1024-set. Direct membership tests reconstruct all eight
atoms under each of the six support orders. Compare every original
presentation, all 434 prescribed values and every completed eligible
presentation, including Boolean coincidences, to the same rational
assignment. Minimize the full atom tuple over all orders to compare
unordered orbits across types. All comparisons agree. The completeness
argument is the atom-bijection argument above: within each fixed pair
of layers every i,j in its stated range occurs, and these counts exhaust
the stabilizer orbits. Swapping the two shell indices supplies the
six/five rectangle. Reanchoring is tested only when the presentation
belongs to the retained slice; no unrepresented value is assigned by
silently extending a five-shell formula.

An independent count verifies the unequal-layer normalization. Fix a
distinguished six-subset U of an n-set, n=68 or 956. On layer l=5 or 6,
the orbit i=|X intersection U| has size

  W_l(i)=binomial(6,i)binomial(n-6,l-i).

For l,m in {5,6}, the relation |X intersection Y|=t acts from functions
on layer m to functions on layer l by the exact quotient

  Q_lm^t(i,j)=sum_x binomial(i,x)binomial(6-i,j-x)
    binomial(l-i,t-x)binomial(n-6-l+i,m-j-t+x).

The four factors choose Y in X intersection U, U outside X, X outside U,
and the complement of X union U. Thus the count retains all points,
including impossible occupancies through zero binomials. Its row sum is
binomial(l,t)binomial(n-l,m-t). Weighted Gram–Schmidt on 1,i,...,i^l
gives monic vectors h_l,a with positive squared norms N_l,a. Exact
coordinate checks for every relation verify
Q_lm^t h_m,a=gamma_lm,a(t) h_l,a for a<=min(l,m), and zero when a>l.
For l=m, gamma_ll,a(t)=E_(n,l,a)(l-t), identifying the modes using
the imported Johnson theorem, not merely an unclassified quotient basis.
Every mixed relation satisfies

  N_5,a gamma_56,a(t)=N_6,a gamma_65,a(t),
  gamma_56,a(t)gamma_65,a(t)
    =beta(n,5,6,a,t)^2/[binomial(n-2a,5-a)binomial(n-2a,6-a)].

For all nonzero beta values the ratio gamma_56,a(t)/beta(n,5,6,a,t)
is one common positive rational number for each n,a; both actions
vanish when beta does. Checking this signed ratio prevents the squared
identity from concealing inconsistent signs when relations are summed.

Tensor the two factor actions and sum the actual entry coefficients.
After the anchor subtraction, their off-diagonal actions g56,g65 obey
g56*g65=C56^2/(D5*D6) and N5*g56=N6*g65, where Nl is the product
of the two actual polynomial norms. The constant corrections in these
actions are respectively p5*p6*S6 and p5*p6*S5. The diagonal actions
are C55/D5 and C66/D6. Hence the actual symmetric bilinear form on this
two-vector basis has entries N5*C55/D5, N5*g56, N6*C66/D6. Its Schur
remainder is exactly N6*(C66-C56^2/C55)/D6 when C55>0; when C55=0
both cross actions vanish and the remainder is N6*C66/D6. The audit
checks every one of these identities and signs. New-only modes retain
C66/D6>=0. These quotient checks independently verify the normalization;
Schrijver's complete source decomposition supplies the full-space
exhaustion, with positive multiplicities, rather than inferring it from
a dimension sum or quotient positivity alone.

The anchor coordinate change on the actual full matrix is
(s,u,v) -> (s-p5*1^T*u-p6*1^T*v,u,v). It is invertible and produces
diag(1, shell remainder) with all three corrections p_l*p_m*J.
No pseudoinverse congruence identity is asserted. The 20 old zero-mode
cross entries vanish exactly; the 13 new-only modes and all 36 shared
modes are retained. This meets the singular criterion for the entire
new block, not only for each individual column.

Run `python3 scripts/finite-support/critical_audit_simultaneous_five_six_shell.py`.
It imports no notebook code or optimizer, parses the manuscript's I and
determinant, solves its 26-by-26 system afresh, fixes z_21=z_22=0 and
compares all 28 resulting fractions with both complete certificates.
The determinant agrees exactly with the displayed positive fraction.
All 49 reconstructed linear rows, right sides, source blocks and Schur
remainders agree; all 28 coordinates are nonnegative, with 20 positive
and 29 zero remainder modes. All 36 rectangular energy comparisons,
the total L060 energy, both full-space dimensions and the six-shell
Boolean trace agree. These are exact rational checks, not numerical
rank or feasibility reports.

All 3011 additional checks pass, as do the 1928 rerun substitution
checks. The complete reconstructed regions, factor quotients/bases,
weighted blocks, witness, determinant and inequalities are saved in
`scripts/finite-support/simultaneous-five-six-shell-critical-audit.json`.
The full summary, failure list and determinant were inspected; the
audit reads and compares every load-bearing original coordinate.
No mathematical repair was required. This retains only the stated
fixed diagnostic's nonexclusion. The omitted ordinary scalar and label
constraints, global PSD/moments, measures and RS realization remain
unproved; the above-threshold objective is not an unsafe-list witness.

## Mathlib

Full matching finite simultaneous-shell certificate, mixed-layer
Terwilliger reduction and prescribed singular completion: not checked.
Supporting finite-set, block PSD, pseudoinverse and exact linear-system
coverage: not checked. Unknown availability is not evidence of absence.
