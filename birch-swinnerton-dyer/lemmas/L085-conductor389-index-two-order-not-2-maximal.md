# L085 — The entire index-two order is not 2-maximal

## Hypotheses

Use audited L067's entire degree-48 number field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive integer H=343h. Use audited L077's
nonmonic basis b, audited L078's order R with basis m, audited L080's
multiplier identification, and audited L084's complete table and all
rational transports for

\[
R^+=\bigoplus_{i=0}^{47}\mathbf Z n_i,
\qquad n_i=m_i\ (i<47),\quad n_{47}=m_{47}/2.
\]

Keep every field coordinate, the actual identity, original scale 31
and enlarged scale 62. Fix p=2. No 31-maximality transfer, selected
factor, stopped ideal-power calculation, L026 package or cross-notebook
input is used. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-index-two-order-prime-two-test.md`.

## Conclusion

For J=√(2R⁺), its full multiplier is the strict order

\[
S=(J:J)=\sum_{i=0}^{45}\mathbf Z n_i
       +\mathbf Z(n_{46}/2)+\mathbf Z(n_{47}/2),
\qquad [S:R^+]=4.
\]

Consequently R⁺ is not 2-maximal. In n-coordinates the complete global
integral preimages are

\[
J=2\mathbf Z n_0+\sum_{i=1}^{47}\mathbf Z n_i,
\qquad N=\sum_{i=0}^{45}2\mathbf Z n_i
                  +\mathbf Z n_{46}+\mathbf Z n_{47},\qquad S=N/2.
\]

The sixth Frobenius matrix has rank one and kernel span(e₁,…,e₄₇)
over F₂. The entire 2304-by-48 action on the rank-48 module J/2J has
rank 46 and kernel span(e₄₆,e₄₇). One strict witness is n₄₆/2.

Production and independent complete replay pass one combined externally
bounded stage. This is fixed known-method reproduction; its separate
critical audit passes below. No table for S, further correction, 2-maximality
of S, global maximality, field discriminant, complete units/classes,
descent/Selmer bound, rational membership or general BSD comparison is
supplied.

## Proof

**Imported theorem and applicability.** Import Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 and its following action/kernel/lifting paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
For a full order A in a number field and nonunit prime p, the full
preimage of the kernel of a Frobenius iterate on A/pA, with p^k greater
than its dimension, is √(pA). Its multiplier is p⁻¹ times the integral
preimage of the kernel of A/pA acting on √(pA)/p√(pA). Lemma 6.4
ensures integrality of this multiplier. It is an order containing A.
Proposition 9.3 supplies the equality stopping criterion; this instance
uses the strict branch. These source results are imported, not reproved.

L067 and L084 give a full order in a number field, and 2 is a nonunit
since R⁺ is finite free over Z. The source has no odd-prime or monogenic
restriction. Six iterates suffice because 2⁶=64>48. L080's old radical
and verdict are not inputs to the new kernels; only its identification
of the input order is used.

**Complete input identification.** All fresh evidence is in
`scripts/seven-torsion/index-two-order-two-325/`. Matrices act on column
coordinates. Let B₀ be L077's b-to-power matrix, M₀ L078's m-to-b matrix,
C₀ its inverse, D=diag(1,…,1,1/2), and T=D⁻¹.
The producer checks the full n-to-b matrix B=M₀D and its integer inverse
C=TC₀ against L084, both inverse products, both original-coordinate
transports and their inverses, both power transports and the actual
identity u=Ce₀. L080's entire multiplier matrix, numerator and inclusion
are checked; thus this is the input lattice R⁺ rather than R again.
The independent verifier reconstructs M₀ from L078's complete explicit
even/odd coefficient columns, B₀ from the nonmonic H formula, and all
six new transport matrices from these canonical inputs. It checks both
inverse products for every transport pair, including both L067 original
coordinates. It also verifies both L067 inverse products. Every H
coefficient agrees with 343h, with degree 48 and content one.

Put V_i(T)=62n_i(T). These are full integer polynomials: for i<47,
V_i=2(31m_i), whereas V₄₇=31m₄₇. Every scaled polynomial coefficient is
checked against the full power transport. The actual identity u, whose
first coordinate is 31, is checked in the original field and on both
sides of every basis element; e₀ is not substituted for it.

For each of all 2304 products, production multiplies V_iV_j, reduces
by the original H, converts to b-coordinates and applies C/62². Every
integer division is checked and all 110592 output slots agree with
L084's supplied table c_ijk. The independent verifier instead checks
the entire polynomial identity

\[
V_iV_j-62\sum_{k=0}^{47}c_{ijk}V_k\equiv0\pmod H.
\]

It uses full division in Q[T], checking all 95 positions after division.
An integer quotient is used only after checking its divisibility by
343; otherwise a rational quotient is used. All 218880 checked positions
vanish, with no rational fallback needed in this instance. Thus all
110592 integer slots are verified in the entire field before modular
work. No rational transport is inverted modulo two.

**Frobenius and the full radical preimage.** Production computes the
first Frobenius from the verified table and actual identity and retains
all six full compositions. Its NumPy operands are reduced to {0,1};
every bilinear contraction is bounded by 48²=2304<2⁶³. Compositions
use Python integers. Independent replay uses a different loop order
and exact Python integer multiplication, successively squaring all 48
basis images six times. It checks all 13824 saved entries and every
composition with the first matrix, as well as exponent 64 and dimension
48.

Complete reversible elimination of the sixth matrix is replayed:
every row operation is invertible, every pivot and pivot column is
checked, the entire terminal matrix agrees and every remaining row is
zero. The rank is one, with pivot zero; reconstructing all free-variable
vectors gives exactly e₁,…,e₄₇. Full matrix products verify kernel
containment as well as the elimination proof of completeness.

For any computed kernel, `lattice` forms the generator matrix G from
every kernel lift and every 2e_i. It saves an integer basis L, full
rational inverse, and integer matrices U,V with

\[
L=GU,\qquad G=LV,\qquad LL^{-1}=L^{-1}L=1.
\]

The independent verifier checks all entries of these two integer
generation identities and both inverse products, and replays the
kernel reduction. Thus they certify equality of global integral
lattices, not only matching residue dimensions. For the Frobenius
kernel the resulting basis is L=diag(2,1,…,1). The imported radical
theorem therefore gives the displayed J.

**Full integral action and its numerator.** For each n_i, production
saves the entire integer matrix A_i of its action on J in the verified
L-basis. Replay checks every coefficient of L A_i=L_i L using the
verified table, where L_i is multiplication by n_i on R⁺.
It also checks every action independently in original H. If
W_j=Σ_l L_lj V_l, then, for every i,j,

\[
V_iW_j-62\sum_k(LA_i)_{kj}V_k\equiv0\pmod H.
\]

The same checked rational division proves every coefficient vanishes.
All 110592 integer action slots, including zeros, are covered.
The action is on all of J/2J, which has rank 48 over F₂, rather than
the smaller image J/2R⁺.

Stack the action matrix with row (j,k), column i equal to (A_i)_kj
modulo two. Independent full elimination replay proves rank 46 and
complete kernel span(e₄₆,e₄₇). All pivots, terminal zero rows and
free-variable equations are checked. Across both eliminations and both
kernel-basis reductions, 1662 reversible row operations are verified.
The two-sided integral generation procedure above yields exactly
Q=diag(2,…,2,1,1) for the preimage N. The source multiplier result now
identifies S=N/2, giving its entire displayed basis.

**Inclusion, identity, index and strictness.** `decision.json` saves
the multiplier matrix M=Q/2 and integer inverse
T'=2Q⁻¹=diag(1,…,1,2,2). Replay checks both full inverse products,
the integral inclusion of R⁺ into S, and the actual identity T'u in S
with M(T'u)=u. Every upper-triangular zero is checked before using the
diagonal determinant product. The determinant is four and agrees with
2 to the complete action-kernel dimension, so [S:R⁺]=4.

The saved strict-witness numerator is e₄₆, outside 2R⁺. Its full
integer action B' is checked in all 2304 slots by A₄₆=2B'. Hence
n₄₆/2 preserves every element of J, but its half-integral n-coordinate
places it outside R⁺. The imported integrality result makes S a strict
integral overorder of 2-power index. Thus R⁺ is not 2-maximal.
A nonzero radical alone is not used to assert nonmaximality.

**Execution and preservation.** The sole execution is

```bash
python3 -B scripts/seven-torsion/index-two-order-two-325/run_once.py
```

The runner refuses an existing start marker. All new artifacts are
written exclusively. One external watchdog covers production, independent
replay, complete final count/verdict validation, final preservation and
report writing, stopping at 180 seconds or 134217728 combined new bytes.
There are no separate stage allowances or 181-second extension.

Production uses 1.590426 internal seconds and replay 1.263306. Through
watchdog writing, the combined run takes 3.332804 seconds (rounded
upward), below 180, and occupies 5483090 bytes, below 134217728.
`producer-report.json`, `verification-report.json`, `stage-report.json`
and `watchdog.json` all pass with empty failure lists. The stage checks
both reports against all required counts and checks their complete
rank/index/verdict agreement. Every one of 568 inventoried originals,
including canonical input lemmas and the prior assessment, has equal
before/after hashes in `input-hashes.json`, both stage-specific
preservation records and `preservation-stage.json`. Hashes supplement,
and do not replace, complete arithmetic replay.

This is the first verified verdict on this input. No retry, resumption,
altered-evidence fixture, correction iteration, table for S or other
prime test occurred. The finite certificate supplies local arithmetic
toward a possible complete global descent; all independent global and
BSD gaps remain. The subsequent separate critical audit is recorded below.

**Separate critical audit (2026-10-18, step 327).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-index-two-order-two-critical-audit.md`.
The full proof, producer, independent verifier and stage/watchdog were
read before the single execution. The imported Stevenhagen hypotheses
are satisfied by the entire number field and full order supplied by
audited L067/L077/L078/L080/L084. The radical contains 2R⁺, hence is a
nonzero full finite module. The residue algebra has dimension 48 and
64>48. The source concerns the entire J/2J, and imposes no odd-prime
or monogenic restriction. Its multiplier description and integrality
criterion are imported, not inferred from the dimension or index alone.

All new evidence is in `scripts/seven-torsion/index-four-audit-327/`.
The external watchdog starts before copying or hashing. The audit hashes
all 568 inventoried inputs, all 70 original step-325 files, this lemma
before its audit addendum, and the prior assessment: 640 distinct files.
It copies 56 required files into a fresh sibling directory, including
the byte-unchanged verifier. The original upstream path semantics and
all fixed certificate bytes are preserved. `copy-manifest.json`,
`original-hashes.json` and `audit-preservation.json` retain complete
source paths and equal before/after hashes. No producer is executed.
The canonical audit addendum is written only after preservation passes.

Fresh complete replay verifies all 2304 original-H products and 110592
integer slots, all 218880 polynomial-division positions, every transport
and inverse, both actual identity actions on all basis vectors, every
one of the six Frobenius matrices and 13824 entries, all 110592 integral
action slots and their original-H identities, the entire 2304-by-48
action stack, and all 1662 reversible row operations with their pivots,
terminal rows and complete kernels. It checks both two-sided integral
preimage generation identities, all inverse products, the full multiplier
basis/inclusion, actual identity, index and strict witness. All remainders
vanish; the checked rational fallback is unnecessary in this instance.
Scale 62 and original scale 31 remain explicit throughout. Rational
transports are never inverted modulo two.

The distinct `audit.py` supplement imports no producer or verifier
routines and uses no saved elimination operations. For the sixth
Frobenius matrix F it chooses a nonzero column c and a nonzero entry
c_r=1, and checks every entry of F=cd, where d is row r of F. The
computed d=e₀ᵀ and c₀=1 prove rank exactly one. Therefore its complete
kernel is span(e₁,…,e₄₇). `frobenius-independent-rank.json` retains
the whole matrix, both factors, the nonzero entry and all kernel vectors.

For the full action stack A, let C consist of its first 46 columns.
A separate reverse-pivot binary elimination selects 46 independent rows
of C. If P selects those rows, exact binary inversion of PC constructs
L=(PC)⁻¹P. Both inverse products of PC and every entry of LC=I₄₆
are checked. Set D=LA; every one of the 110592 coefficients of CD=A
is then checked on the full stack. These identities prove rank A=46:
LC=I gives the lower bound and A=CD gives the upper bound. The full
computed D is [I₄₆ | 0 | 0]. Since C is injective, ker A=ker D is
exactly span(e₄₆,e₄₇). The entire kernel containment is checked as
well. `action-independent-rank.json` retains A,C,L,D, the selected
rows and inverse, and the complete kernel. Selected rows alone are
not used to certify the full factorization.

For each kernel, independent binary ranks of the saved basis, the new
basis and their union check independence and both span containments.
For its new full kernel basis K, the supplement forms the integer
generator matrix G=[Kᵀ | 2I₄₈]. Reducing any integral preimage modulo
two expresses its residue in K, so these columns generate the whole
preimage, not just a sublattice. For the displayed diagonal basis B
of J or N, respectively, it independently constructs integer U,V and
checks GU=B and BV=G. It verifies both inverse products of B, both
integral containments between B and the saved basis, both generation
identities and both comparison inverse products. Complete evidence is
in `radical-independent-preimage.json` and
`numerator-independent-preimage.json`. These checks identify precisely
J=diag(2,1,…,1)Z⁴⁸ and N=diag(2,…,2,1,1)Z⁴⁸ in n-coordinates.
Together with the imported theorem, this proves that N/2 is the full
multiplier (J:J), rather than a strict suborder inside it.

`independent-multiplier.json` checks M=N/2 and its inverse inclusion
T=diag(1,…,1,2,2) in every entry. Both MT=TM=I and all off-diagonal
zeros are checked. Thus |det T|=4 is [S:R⁺], since the columns of T
express the old R⁺ basis in the new S basis. The actual identity u is
checked in original power coordinates by Σu_i V_i=62; the supplement
also checks M(Tu)=u and agreement with the saved identity. It independently
reconstructs the action of n₄₆/2 from the verified table and its own
diagonal J basis. All 2304 coefficients are integral and agree with
half of the entire replayed A₄₆. The coordinate e₄₆/2 is not integral
in the old n basis. Thus the witness preserves all of J and lies
outside R⁺, establishing the asserted strictness and non-2-maximality.

The sole execution is

```bash
python3 -B scripts/seven-torsion/index-four-audit-327/run_once.py
```

The runner refuses an existing start marker; all writes are exclusive.
One external watchdog covers initial copies/hashes, fresh replay, both
rank and lattice supplements, all final preservation and report writes.
Through watchdog writing the run takes at most 1.704403 seconds (rounded
upward), below 180, with 6272658 combined new bytes, below 134217728.
The count includes code, fixed copies, logs, full certificates and reports.
`verification-report.json`, `audit-report.json` and `watchdog.json`
all pass with empty failure lists. All 640 originals and all 56 fixed
copies remain byte-identical during the audit. No retry, malformed fixture,
successor table, further correction or new prime test occurs. This
validates a fixed known-method input; it advances no general theorem
beyond the assessed sources and resolves none of the independent BSD gaps.

## Mathlib

Full matching coverage for this explicit radical/multiplier certificate
and the imported criterion has not been checked. Supporting coverage
also remains unchecked; this is not evidence of absence. The cited
theorem and exact informal finite replay are the mathematical inputs.
