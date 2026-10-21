# L068 — Six full seven-torsion scalar pullbacks at conductor 389

## Hypotheses

Let E/Q be y^2+y=x^3+x^2-2x and retain audited L067's entire
Z=E[7] minus {O} and its full equivariant function algebra R. In the
short model put a=-3024, b=46224, c(X)=X^3+aX+b and use L067's
monic degree-24 polynomial f and faithful presentations

\[
B=\mathbf Q[X,Y]/(f(X),Y^2-c(X))\simeq R
 \simeq\mathbf Q[T]/(h(T)),\qquad T=Y.
\]

The ordered B-basis is (1,X,...,X^23,Y,XY,...,X^23Y), and the
ordered T-basis is (1,T,...,T^47). L067 supplies both full coordinate
maps and the mutually inverse basis matrices M,N. No residual-image,
L026, analytic-rank, rational-rank, Selmer or Sha premise is assumed.

The complete new finite evidence is
`scripts/seven-torsion/scalar-actions-243/actions.json`; every rational
coefficient is retained. Its independent replay report is
`scripts/seven-torsion/scalar-actions-243/verification.json`. Full-schema
altered-evidence copies and preservation results are in that directory's
`rejections/` and `rejection-verification.json`. The upstream certificate
has a fresh complete replay in `upstream-replay.json`, and all 38 existing
upstream files have the saved `upstream-manifest.json`.

Reproduction from the notebook directory is:

```bash
python3 scripts/seven-torsion/scalar-actions-243/build_actions.py
python3 scripts/seven-torsion/verify_certificate.py --report scripts/seven-torsion/scalar-actions-243/upstream-replay.json
python3 scripts/seven-torsion/scalar-actions-243/verify_actions.py
python3 scripts/seven-torsion/scalar-actions-243/check_action_rejections.py
```

The producer uses the old producer's exact polynomial helpers. The new
verifier uses only the old independent verifier's polynomial helpers and
its own quotient/matrix arithmetic; it imports neither producer nor any
producer arithmetic. The old verifier itself imports no producer. This
fixed construction, independent replay and separate critical audit pass.
The audit evidence is in `scripts/seven-torsion/scalar-audit-245/`.
This is known-algorithm reproduction.

## Conclusion

For each i=1,...,6, the certificate gives both short coordinates X_i,Y_i
of [i]P, both original coordinates x_i,y_i, the complete polynomial
sigma_i(T) and all entries of the 48-by-48 matrices of sigma_i on both
bases. These are the geometric **forward** pullbacks

\[
 (\sigma_i u)(P)=u([i]P)\quad(P\in Z).
\]

Every evaluated denominator has an exact inverse in the full R. The
maps obey sigma_1=id and sigma_i sigma_j=sigma_(ij mod 7) on the whole
algebra, with inverse indices (1,4,5,2,3,6) for i=(1,2,3,4,5,6).
The scalar 3 has order six, with powers 1,3,2,6,4,5,1 modulo seven.

These maps could supply the scalar part of L066's optional necessary
cohomology-image constraints if complete global power-class coordinates
were independently supplied. No such coordinates or constraint matrix
are produced here. Incidence data and descent functions, embeddings and
local identifications, complete units/classes and local-image upper
bounds remain absent. This establishes no cohomology-image equality,
Selmer upper bound, D=D_div, successful localization, rational Kummer
membership, Sha result or arbitrary-curve complex-order/rank comparison.

## Proof

**Named inputs and specialization.** Import Sutherland, MIT 18.783,
Fall 2023, [Lecture 5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
Sections 5.5--5.6, printed pp. 10--14, Lemma 5.20, Theorem 5.21 and
Lemma 5.24: the division-polynomial recurrences, multiplication
coordinates and no-cancellation assertion. Q has characteristic neither
two nor three. L067 identifies the nonsingular short model by the
origin-preserving change X=36x+12, Y=216y+108; hence these group-law
formulas transport to the exact original E. The six indices are prime
to seven, so [i]P never equals O for P in Z. The exact inverses below
also verify domain validity directly on every one of the 48 points.
We import the general multiplication theorem, rather than reprove it.
The instance coefficient and domain checks are necessary because that
theorem does not supply this certificate's rational arithmetic.

For the convention import Schaefer--Stoll, *How to do a p-descent on an
elliptic curve*, Trans. AMS 356 (2004), 1209--1231,
[author long version dated 13 June 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 7, Lemma 7.2, Corollary 7.3 and its following convention,
printed pp. 13--14. The explicit source convention is
(sigma_g phi)(P)=phi(gP). It is used here without any assertion that
scalar constraints suffice for cohomology. The additional incidence
condition of Corollary 7.9 and Proposition 7.10, pp. 18--19, is not
constructed or assumed. No point-stabilizer hypothesis is needed to
construct the pullbacks themselves; the source's hypotheses remain
necessary for any later application of its cohomological conclusions.

**Complete symbolic construction before evaluation.** Work first in
C=Q[X,Y]/(Y^2-c(X)), with unique representatives A(X)+B(X)Y, without
reducing modulo f. The certificate retains psi_-1=-1, psi_0=0,
psi_1=1, psi_2=2Y, and the standard bases

\[
\begin{split}
\psi_3&=3X^4+6aX^2+12bX-a^2,\\
\psi_4&=4Y(X^6+5aX^4+20bX^3-5a^2X^2-4abX-8b^2-a^3).
\end{split}
\]

The only further division-polynomial recurrences used are

\[
\begin{split}
\psi_5&=\psi_4\psi_2^3-\psi_3^3,\\
2Y\psi_6&=\psi_3(\psi_5\psi_2^2-\psi_1\psi_4^2),\\
\psi_7&=\psi_5\psi_3^3-\psi_2\psi_4^3,\\
2Y\psi_8&=\psi_4(\psi_6\psi_3^2-\psi_2\psi_5^2).
\end{split}
\]

For every i=1,...,6 form

\[
\phi_i=X\psi_i^2-\psi_{i+1}\psi_{i-1},\qquad
4Y\omega_i=\psi_{i+2}\psi_{i-1}^2-\psi_{i-2}\psi_{i+1}^2.
\]

The producer divides a numerator A+BY by kY by polynomial division of
A by c, giving B/k+(A/c)Y/k; it requires the entire polynomial remainder
to be zero. It saves both full numerator and quotient for psi_6,
psi_8 and all six omega_i. The independent verifier reconstructs the
base cases and every numerator using bivariate multiplication followed
by Y^2=c, and checks (kY)(saved quotient)=reconstructed numerator as a
complete identity in C, before any reduction by f. These identities
certify all eight polynomial divisions, rather than cancellation only
at torsion points. Multiplication by Y is injective in C: in its two
components Y(A+BY)=Bc+AY, and c is a nonzero polynomial over Q.
Thus each checked quotient is the required unique quotient. Every
coefficient of all ten psi polynomials and all twelve phi/omega
polynomials agrees with the independently reconstructed expressions.
In particular omega_1=Y, retaining the negative base case psi_-1=-1.

**Full-domain denominator and coordinate witnesses.** Now reduce in
B. The certificate contains the following exact 24 unit witnesses:
constants 2,4,36,216; elements 2Y,4Y; and, for i=1,...,6, each of
psi_i, psi_i^2, psi_i^3. A witness consists of the complete pair of
polynomials for its value and its inverse. The verifier independently
reconstructs the required set, verifies the values and checks every
product with its inverse equals one in B. Missing witnesses are
rejected, including the intermediate symbolic denominators. Rational
constants appearing in the original-model transport are explicitly
covered. No numerical roots or single embeddings are used.

The producer obtains an inverse of A+BY by using
(A-BY)/(A^2-cB^2) and a rational-polynomial Bezout identity modulo f;
the verifier needs none of that inverse construction and instead checks
the full product identity directly. The actual map values satisfy

\[
\psi_i^2 X_i=\phi_i,\qquad \psi_i^3Y_i=\omega_i,\qquad
x_i=(X_i-12)/36,\quad y_i=(Y_i-108)/216
\]

in the whole B. These equations, together with the checked unit
witnesses and the imported multiplication theorem, identify both
coordinates as those of [i]P simultaneously for every P in Z. L067's
etaleness identifies B tensor Qbar with the product of all 48 point
coordinates, so a unit identity excludes a zero denominator at any
point. It also makes every exact B-identity a whole-domain identity.
Checking only h(sigma_i(T))=0 would not give this geometric identification.

The verifier additionally checks both transported curve equations,
f(X_i)=0 and h(Y_i)=0 by full quotient Horner reduction. Thus
substitution gives a Q-algebra endomorphism of B and retains the
nonzero torsion domain. These checks use the complete f and h from
audited L067 with the upstream byte hash verified. Fresh complete
upstream replay passes all 4852 checks before the new result is used.

**Faithful actions, composition and inverses.** For every i the B-action
matrix has, in order, the columns X_i^j and X_i^jY_i, 0<=j<24. The
independent verifier reconstructs all 48 columns by quotient
multiplication. The saved T-action has column j equal to the T-basis
coordinates of Y_i^j, 0<=j<48. For every column the verifier multiplies
by L067's complete M and checks equality with the independently
constructed B-coordinate vector. Since M is invertible, this identifies
all 48 T-basis images. The saved sigma_i(T) is also checked against
column one and the geometric Y_i. Both original coordinate functions
are tested under the full action. These are 576 basis-image checks,
not just generator images or a dimension declaration.

For every ordered pair (i,j), with k the nonzero residue ij modulo
seven, the verifier tests sigma_i(X_j)=X_k, sigma_i(Y_j)=Y_k and both
original-coordinate identities. It then checks both complete matrix
products B_i B_j=B_k and T_i T_j=T_k, at all 2304 entries each.
This gives 144 coordinate identities and 165888 scalar matrix-entry
identities. The matrices are scaled by exact common denominators and
the equalities are checked as integer equations, without rounding.
All expected entries, including zeros, are tested. The identity matrices
at i=1 and the pairs (1,1),(2,4),(3,5),(4,2),(5,3),(6,6) give both
inverse products. Together with the polynomial-domain checks this
proves faithful whole-algebra automorphisms with the required forward
convention. The seven explicitly checked residues of powers of 3 show
that 3 has order exactly six; no global power-class action is inferred.

**Evidence and limits.** The complete replay reports 166964 passing
checks, zero failures, all six maps on dimension 48, all eight symbolic
divisions, 24 denominator witnesses, 576 basis images and all 165888
required composition entries. Five full-schema altered copies change a
short X-coordinate, an inverse, a T-action entry, a B-action entry, or
remove 2Y's unit witness. The verifier rejects these respectively at
`geometric_X_2`, `denominator_inverse_psi3`, `full_T_basis_3_1`,
`full_B_even_4_1` and `complete_required_denominators`. All five intended
rejections pass. Before/after hashes preserve all 38 upstream files
and the five new production/code/replay files tested. L067's invalid
degree-47 draft and initial failed audit-harness report are included
in the preserved upstream manifest. Nothing replaces those failures
with passing evidence.

The separate critical audit below validates this finite assembly. It
supplies only the stated fixed scalar maps; universal software correctness,
incidence and full descent are not asserted. The limitations in the
conclusion and ATTEMPTS/021/032/033/034 remain unchanged. No progress
beyond the imported multiplication algorithm is claimed.

**Separate critical audit (2026-10-16, step 245).** The saved audit
assessment was SPECIALIZE before this invocation. Its inspected primary
theorem statements and essential cases are reused, including Sutherland's
negative-index convention and Schaefer--Stoll's forward convention; no
new general multiplication result is asserted. The audit read this entire
proof, L067's full algebra justification and both action implementations,
including all polynomial helpers imported by the independent verifier.
No additional arithmetic or residual-image hypothesis is needed.

The model change is L067's projective isomorphism preserving O, so it
preserves the elliptic group law. Every nonzero seven-torsion point has
order exactly seven; each of the six indices is invertible modulo seven.
The entire etale algebra, not merely its field label, is required here.
The fresh L067 replay verifies both inverse basis products, both coordinate
models, all defining equations and the finite-field evidence in 4852
checks. It supplies the full-domain identification used below.

The eight pre-reduction identities in C are checked coefficient by
coefficient. In particular, at i=1 the numerator for omega_1 is
psi_3 psi_0^2 - psi_-1 psi_2^2 = 4Y^2 = 4c(X); the saved numerator is
184896 - 12096X + 4X^3 and the quotient is Y. Injectivity of multiplication
by Y in C proves uniqueness, without assuming it is a unit there.
Only after these polynomial identities are checked do we reduce modulo f.
All 24 required evaluated unit witnesses are present: four constants,
2Y and 4Y, and three powers of each of the six psi_i. The constants
36 and 216 cover both transports; the reciprocal constants in the
source formulas are rational and nonzero. Thus neither coordinate has
an unverified denominator at any point. The imported theorem now
identifies both coordinates on all of Z. The defining-relation checks
then justify the algebra substitutions, independently of any mere root
or convention label.

The matrix orientation was checked explicitly: M sends T-basis columns
to B-basis columns, and N=M^{-1} sends them back. Therefore each of the
48 column equalities per basis identifies the indicated substitution on
the full vector space. There are 6*2*48=576 such images. For a function
u, the composite sigma_i(sigma_j(u)) evaluates as u([j][i]P), which is
u([ij]P). All 36 ordered products are checked in both bases at every
entry, giving 36*2*48^2=165888 identities. The ordered list includes
both products for every inverse pair, not just one order. Identity is
checked on the whole algebra. The power sequence of 3 has six distinct
nonzero residues before returning to one. Because all P in Z have order
seven and the algebra separates them, those six geometric maps really
are distinct; hence this scalar action is faithful and sigma_3 has order
six. A composition table alone would not distinguish forward from inverse
indexing; the preceding geometric coordinate equations do.

A distinct exact cross-check is implemented in
`scripts/seven-torsion/scalar-audit-245/audit_actions.py`. It imports no
arithmetic from either producer or verifier. In Q[T]/(h), it multiplies by
integer convolution after clearing rational denominators and then performs
monic rational long reduction. For every denominator value and inverse
and every X_i,Y_i,x_i,y_i, it transports the complete B-vector v by N,
and independently evaluates A(X(T))+B(X(T))T using these univariate
operations. All 72 transport equalities hold. Powers through X^54 cover
every coefficient of the unreduced phi_i and omega_i used in this check.
It verifies all 24 full unit products and, for every i, the equalities

\[
 \psi_i^2 X_i=\phi_i,\qquad \psi_i^3Y_i=\omega_i,\qquad
 36x_i+12=X_i,\qquad216y_i+108=Y_i
\]

in Q[T]/(h), as well as all six sigma_i(T)=Y_i identities. Here all
symbols mean their transported univariate representatives. In total,
72+24+12+12+6=126 exact equalities pass. The full rational left and right
sides and zero residuals are saved in `univariate-crosscheck.json` in
that audit directory. This is a complete alternate representation check,
not selected embeddings, modular samples or numerical evaluation. Its
use of N and h is justified by the independent full L067 replay and
L067's already audited determinant cross-check; it supplements rather
than replaces the pre-reduction and full-action evidence.

Fresh action replay passes all 166964 checks, including all eight
divisions, 24 denominator units and the required basis/composition counts.
The five original full-schema rejection fixtures are replayed to fresh
reports with their original intended labels. Two additional full-schema
copies retain the convention label. Changing psi_-1 from -1 to +1 is
rejected at `psi_-1_all_coefficients`, a mathematical base-case check.
Swapping the complete scalar-2 and scalar-4 maps is rejected at
`geometric_X_2`, before the basis or composition checks. Thus the inverse
index test fails geometrically, not merely on a schema or label mismatch.
All seven intended rejections pass; none is evidence against the actual
scalar maps. Complete evidence inspection also checks all 126 saved
rational equalities and the entire ordered composition report.

The final report is `scripts/seven-torsion/scalar-audit-245/audit-report.json`;
full replays, rejection fixtures/reports, `complete-evidence-inspection.json`
and before/after preservation manifests are in that directory. All 61
original files retain their bytes, and the previous 38-file upstream
manifest still matches. This includes the invalid degree-47 draft and
the failed earlier audit-harness report. The audit commands, from the
notebook directory, are:

```bash
python3 scripts/seven-torsion/verify_certificate.py --report scripts/seven-torsion/scalar-audit-245/upstream-replay.json
python3 scripts/seven-torsion/scalar-actions-243/verify_actions.py --report scripts/seven-torsion/scalar-audit-245/action-replay.json
python3 scripts/seven-torsion/scalar-audit-245/audit_actions.py
```

This separate fixed audit passes. It validates the known scalar algorithm
on this exact full algebra; it neither extends the general source theorem
nor constructs incidence, functions, complete global classes, local bounds
or any Selmer certificate. The independent gaps in the conclusion remain.

## Mathlib

Full matching coverage for these fixed full-torsion scalar certificates,
forward pullbacks and the descent interface was not checked; no absence
claim is made. The primary multiplication theorem is the mathematical
input, and exact certificates plus independent replay verify this
instance. This is an informal proof, not a Lean formalization.
