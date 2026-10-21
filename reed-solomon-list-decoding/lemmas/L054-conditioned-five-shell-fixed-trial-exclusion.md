# L054 — The full conditioned distance-five shell excludes L053's trial

## Hypotheses

Use exactly L053's rational moment assignment on the universe V of all
68-subsets of the 1024-point domain H. In particular its singleton moment
is rho=M/binomial(1024,68)>0, M=(U+1)/2,
U=binomial(1024,64)/binomial(68,64), its pair moment at half-distance i
is rho*p_i, and lambda=p_68>0. The p_i are the unchanged values specified
in L053 from L022's pairs. Boolean repetitions retain lower-order moments.
Distinct triple moments are rho*p_i*p_j*p_h/lambda except for forbidden
half-distances 1,...,4 and the full L020 incidence, where they are zero.
Zeroing the entire incidence, including realizable cases, is this trial's
choice, not a necessary condition on all RS lists.

Fix any A in V. Put S_A={B in V: |A\B|=5}. Consider the union matrix
with indices {A} and {A,B} for all B in S_A, and entries x(I union J).
All moment matrices are real symmetric. No representing measure or
feasibility for larger matrices is assumed. For the RS interpretation
retain L053's message degree less than 64, ambient field F_(65537^28),
closed simultaneous agreement and arbitrary tuple width m>=1.

## Conclusion

This full anchored shell matrix is not PSD, for every A. Its Schur
complement has 12 negative and 24 positive product spectral coordinates,
with no zero coordinate. The negative coordinates are exactly

  (a,b) with 0<=a<=3 and 0<=b<=2.

Their complete multiplicities and exact rational values are certified
below. In particular the (0,1) mode has multiplicity 955 and is negative
already in the anchor-free shell block.

Consequently the fixed L053 trial does not extend to a feasible point of
the full order-three union-matrix program. Its audited small-principal
nonexclusion result remains valid. This excludes one trial only: it
does not bound the program with free pair/triple moments, exclude every
extension of these pairs, construct an RS list, or change 955<=t_star(m)<=957.
Both 67/68-agreement safety gaps remain unresolved. This finite diagnostic
is a reproduction of the assessed spectral methods, not a claim of new
mathematics beyond the checked sources. The separate critical proof review
below retains the fixed-trial exclusion.

## Proof

**Necessary matrix and imported tools.** Reuse L053's established
support specialization and the precise primary program in
[foundations/12](../foundations/12-global-degree-three-moment-source.md):
Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and its indicator proof, printed p. 2.
At order three, a singleton anchor permits every index {A,B}; the matrix
here is a principal restriction. L053's argument applies to selected
supports of a whole tuple list, without scalar projection, without an
exponent m, and allowing extra agreements. Thus PSD of this matrix is
necessary for the full program and for list indicators. The source's
displayed-endpoint qualification is retained in foundations/12.

Import the complete simultaneous Johnson eigenspaces, their relation
eigenvalues and multiplicities from Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2, 3
and 3.4, printed pp. 3, 10, 12; and Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Section 11.2, pp. 162–163. Import tensor eigenvectors and their complete
product spectrum from the latter's Section 1.4.7, p. 19, and the Schur
congruence from Theorem 2.7.1(i), p. 36. The exact scope and primary
cases read are recorded in
[foundations/09](../foundations/09-global-pair-johnson-source.md).
The factor parameters (68,5) and (956,5) satisfy n>=2d.
Identity relations use the identity matrix. No hierarchy or spectral
theorem is reproved; only the entries and signs for this finite trial
need specialization. The separately approved SPECIALIZE assessment is
`drafts/literature/2026-10-12-conditioned-five-shell-spectrum.md`.

**Complete entry dictionary.** Every B in S_A has a unique description
B=(A\X) union Y with X a five-subset of A and Y a five-subset of H\A.
This is a bijection between S_A and the full product of the two weight-five
layers. For another C=(A\X') union Y', put
r=5-|X intersection X'| and q=5-|Y intersection Y'|. In L053's orbit
notation i=j=5, t=5-r, s=5-q and h=r+q. Its eight disjoint region sizes
are, in the order used in L053,

  5-r, r, r, 63-r, 5-q, q, q, 951-q.

All 36 r,q in {0,...,5} are possible: each factor requires at most ten
distinct points, below both available sizes. A triple has common size
61, all pair-only sizes two and all private sizes three exactly when
r=2 and q=3. Thus the (5,5,3,2) override affects just this product
relation, not all triples at distance multiset (5,5,5).

When r=q=0, B=C, and the union of the two identical {A,B} indices is
{A,B}. Its moment is rho*p_5. Otherwise A,B,C are distinct. Dividing
the shell block by rho gives the following complete coefficient table:

\[
c_{rq}=\begin{cases}
p_5,&r=q=0,\\
0,&1\le r+q\le4\text{ or }(r,q)=(2,3),\\
\alpha p_{r+q},&\text{otherwise},
\end{cases}\qquad \alpha=p_5^2/\lambda>0.
\]

The normalized anchor entry is 1 and every anchor/shell entry is p_5.
Let R_r^(n) be the relation-r matrix on five-subsets of an n-set,
including R_0^(n)=I. The complete matrix after division by rho is

\[
\begin{pmatrix}1&p_5\mathbf1^T\\p_5\mathbf1&C\end{pmatrix},
\qquad C=\sum_{r,q=0}^5 c_{rq}R_r^{(68)}\otimes R_q^{(956)}.
\]

These equalities follow from the trial's explicit recipe for every entry.
They establish symmetry under permutations of the head and tail for
this specified matrix. No labeled feasible point is averaged and no
actual-label rank exclusion is transported by that group.

**All modes and anchor.** For factor eigenspace a, relation r has eigenvalue

\[
E_a^{(n)}(r)=\sum_{h=0}^r(-1)^h\binom ah
                 \binom{5-a}{r-h}\binom{n-5-a}{r-h},
\qquad m_a^{(n)}=\binom na-\binom n{a-1}.
\]

Binomials outside their ordinary range are zero. These are the imported
source eigenvalues, with the notation translated as in foundations/09.
The two complete multiplicity arrays, indexed a=0,...,5, are

  n=68:  1, 67, 2210, 47838, 764269, 9609743;
  n=956: 1, 955, 455534, 144707330, 34440116295, 6550452053781.

They sum to binomial(68,5) and binomial(956,5). Every product eigenspace
(a,b) has positive dimension m_a^(68)*m_b^(956), and their dimensions sum to

  S=binomial(68,5)binomial(956,5)=68643272053310642688.

The shell eigenvalue divided by rho is
e_ab=sum_(r,q) c_rq E_a^(68)(r) E_b^(956)(q). The imported Schur
congruence inverts only the positive leading 1 and reduces the matrix
to 1 and C-p_5^2 J. The constant projector is J/S; hence its spectral
coordinates are

\[
\sigma_{ab}=e_{ab}-\mathbf1_{(a,b)=(0,0)}p_5^2 S.
\]

This retains singular lower blocks and changes only the constant
coordinate. Positivity of rho and alpha allows equivalent sign testing
of eta_ab=sigma_ab/alpha. The complete exact sign table is

| a \\ b | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 0 | − | − | − | + | + | + |
| 1 | − | − | − | + | + | + |
| 2 | − | − | − | + | + | + |
| 3 | − | − | − | + | + | + |
| 4 | + | + | + | + | + | + |
| 5 | + | + | + | + | + | + |

For a load-bearing nonconstant witness, the exact value is

\[
\eta_{01}=
-\frac{9407447982070183554138710330070988958007422947593808542631328728863935482584761986056607300265166515267887}
{58777218163070353667139034661145066715999641701236218891492604409567076435028516765657297701931037908560}<0.
\]

The anchor correction on this mode is exactly zero. Its dimension is
m_0^(68)*m_1^(956)=955. A nonzero real vector in that eigenspace has
negative quadratic form under C, and under the Schur complement.
It follows that both the shell block and the full anchored matrix
fail PSD. Completeness is necessary for the claimed whole sign table,
though this one negative coordinate suffices for exclusion.

**Full exact certificate and independent reconstruction.** Run from the
active notebook:

  `python3 scripts/finite-support/conditioned_five_shell.py`

then

  `python3 scripts/finite-support/audit_conditioned_five_shell.py`.

The first writes all 36 entries, all 72 factor eigenvalues, complete
multiplicities, all 36 rational shell and Schur coordinates and positive
normalizations to `scripts/finite-support/conditioned-five-shell-results.json`.
The second imports no constructor routines and writes the complete
reconstruction to
`scripts/finite-support/conditioned-five-shell-audit-results.json`.

The independent verifier uses factorial binomials, reconstructs all p_i
from L053's specified L021 input and checks its 64 defining equations,
as well as exact agreement with L022's saved pairs. It constructs actual
representative support sets for every r,q and evaluates the Boolean union
and all common/pair-only/private intersections directly, rather than
using the constructor's coefficient recipe. The entry dictionary above
proves that these representatives cover every relation, including the
repeated diagonal and the sole override.

As a second factor reconstruction it uses Schrijver's single-layer beta
coefficients from Theorem 1 (51), III.A (53)–(58), pp. 6–7 of
[the author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
with the source normalization recorded in
[foundations/04](../foundations/04-constant-weight-triple-sdp-source.md):

\[
\widetilde E_k^{(n)}(r)=\frac{1}{\binom{n-2k}{5-k}}
\sum_{u=\max(k,5-r)}^5(-1)^{u-(5-r)}\binom{u}{5-r}
\binom{n-2k}{u-k}\binom{n-k-u}{5-u}^{\!2}.
\]

Terms outside this u range vanish in the full source sum. The denominator
is positive for both factors and all k<=5. All 72 values agree exactly
with the imported Johnson eigenmatrix. The verifier checks every relation
valency, identity eigenvalue and all 72 factor trace-orthogonality equations
sum_k m_k E_k(r)E_k(s)=binomial(n,5)E_0(r) if r=s and zero otherwise.
It then independently evaluates every one of the 36 product modes and
anchor corrections, checks every saved rational value and multiplicity,
and checks the dimension sum and complete shell/Schur traces. The sign
classification follows by exact rational comparison in every mode.
All 328 arithmetic checks pass with no failures. Negative spectral
coordinates are the mathematical result, not arithmetic-check failures.
The full (0,1) witness and the empty failure list were inspected; complete
verification uses reconstruction of all relevant values, not a preview
or stored success flag. The report includes the constructor certificate's
SHA-256 hash.

**Scope of the verdict.** This rules out full conditioned PSD for the
unchanged L053 moments. Its objective still has floor(M)>=
T=floor(65537^28/2^128)+1, but is no longer a feasible lower witness
for the full program. A uniform upper bound below T is still required
for safety. No retuning or optimization is performed here. Other
triples with these pairs, general pairs, other conditioned matrices,
representing measures and RS realization remain open.

**Separate critical proof review (2026-10-12, step 175).** The approved
scope is `drafts/literature/2026-10-12-conditioned-five-shell-critical-audit.md`.
The review reused the precise primary imports above and audited L053;
it found no defect in the exclusion or its qualifications. The full
independent reconstruction was rerun: all 328 checks pass. This checks
every saved dictionary entry and every shell/Schur coordinate, not just
the negative witness or a stored summary. The code uses the same specified
pair input as L053, verifies its defining equations, and reconstructs the
entries by actual set unions. The general eight-region argument above
justifies extending these representatives to every shell entry for every
anchor; no special choice of actual field labels is assumed.

For the beta normalization, specialize the source to i=j=5 and t=5-r.
Terms u<t vanish by binomial(u,t), terms u<k by binomial(n-2k,u-k),
and terms u>5 by the two weight-layer binomials. The surviving denominator
binomial(n-2k,5-k) is positive since 0<=k<=5 and n is 68 or 956.
The source's normalized block is therefore precisely the beta expression
displayed above. Its exact equality with all Johnson factor coordinates,
identity relations and valencies is checked before taking products.
Every factor multiplicity is positive and both complete layer dimensions
are exhausted. Consequently there is neither an omitted mode nor a
zero-dimensional negative coordinate.

The normalized anchor is 1 because x({A})=rho, whereas the normalized
shell diagonal and anchor/shell entries are p_5 because their Boolean
unions have two supports. The congruence therefore subtracts p_5^2 J,
not p_5 J or a conditional orbit count. It uses only the inverse of 1;
no lower-block invertibility is assumed. The constant projector J/S
acts only on (0,0), so the (0,1) witness excludes the shell itself.

An additional check connects that witness directly to a concrete real
vector, without using beta or Johnson formulas to compute its value.
Fix a tail point z and put f_z(X,Y)=1_{z in Y}-5/956, constant in X.
This vector is nonzero and has sum zero, since exactly binomial(955,4)
tail five-sets contain z. At relation q from Y, the fraction of Y'
containing z is (5-q)/5 if z belongs to Y, and q/951 otherwise.
Writing v_q=binomial(5,q)binomial(951,q), both cases give

  (R_q f_z)(Y)=v_q*(1-956*q/(5*951))*f_z(Y).

The head constant vector has relation-r eigenvalue
binomial(5,r)binomial(63,r). Substitution of all 36 dictionary coefficients
thus computes C f_z=e_01 f_z directly. This audit-specific count verifies
the existing witness; it does not reprove the imported full spectral
theorem. The exact sum divided by alpha agrees with every digit of the
displayed negative fraction. Since J f_z=0 and rho,alpha>0, both the
shell and the anchored matrix have a negative quadratic direction.

Run `python3 scripts/finite-support/critical_audit_conditioned_five_shell.py`
after the independent reconstruction. All 52 additional checks pass,
including both point-membership cases for all six tail relations, every
manuscript sign and multiplicity, dimension exhaustion, positive scaling,
the exact displayed fraction, constant-only correction and the unchanged
objective threshold comparison. Complete rational contributions and
checks are saved in
`scripts/finite-support/conditioned-five-shell-critical-audit-results.json`,
bound by hash to the reconstruction report. Both full failure lists and
the complete displayed witness were inspected. No retuning was performed.
This completes local verification of L054, not a new bound beyond its
statement or the sources checked. Trial invariance is established by its
recipe; averaging arbitrary labeled feasible moments is not asserted.
Other triples at the same pairs, a uniform bound below T, representing
measures and common-center RS lists remain unproved.

## Mathlib

Full matching finite-shell exclusion and order-three support program:
**not checked** in Mathlib. Supporting Johnson/product eigenspaces,
Schur congruence and Boolean-union coverage are also not checked.
Unknown availability is not evidence of absence; the precise primary
imports and complete rational certificates supply this local proof.
