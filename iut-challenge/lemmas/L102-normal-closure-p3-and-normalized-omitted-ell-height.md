# L102 — Normal-closure P3 and normalized omitted-ell height

## Hypotheses

Fix one member and one ordering supplied by audited L101, with its
fixed family, domains, algebraic closure, d=6, epsilon_d=1 and finite
exceptions. Retain the same literal Legendre curve and fields

    E_o: V^2=X(X-1)(X-t_o),
    F=G_o=Q(t_o)(iota,E_o[15]), iota^2=-1,
    C=C_o=G_o^nor over Q.

Division fields adjoin both coordinates of every geometric torsion
point. Use exactly L101's selected prime ell>=7 and its downstairs
height

    H=(1/[F:Q]) sum_x h_x f_x log(p_x), H>25,

with GenEll integer curve heights and every actual finite F-place.
In particular h_x<sqrt(H) for every x|ell. L092 supplies the degrees
[F:Q]=276480 and [C:Q]=1105920. Neither F/Q normality nor integrality
of j(E_o) at ell is assumed.

For D=F or C, define the arithmetic contribution

    H_ell(D)=(1/[D:Q]) sum_(z|ell) h_z f_z log(ell),

where f_z is the absolute residue degree at z. Retain the April 2020
reproduction and explicit def= qualifications of L101. This definition
does not posit a native pilot or repaired initial theta-data for C.

## Conclusion

For every actual C-place w|ell,

    h_w<4sqrt(H).                                       (1)

The fully normalized contribution satisfies the stronger identity
and strict bound

    H_ell(C)=H_ell(F)<sqrt(H)log(ell).                    (2)

Consequently H_ell(C)/6<sqrt(H)log(ell)/6. This retains the inspected
source display's one-sixth coefficient as a numerical comparison;
identifying its left side with an actual native omitted term over C
is an additional obligation. In particular (1) does not assert the
original P3 bound h_w<sqrt(H) over C.

This is a reproduction/specialization of known height and
completion-degree formulas. The separate step410 critical audit
below validates it within its stated scope. It
neither excludes an ell-pole nor supplies P4–P7, a complete field
repair, an essential IUT flaw or original finite B>=A.

## Proof

### Imports, relevance and bounded test

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-normal-closure-p3-and-omitted-ell-height.md`.
Its inspected general sources are reused; no general theorem is
reproved:

- Mochizuki, *Arithmetic Elliptic Curves in General Position*,
  Math. J. Okayama Univ. 52 (2010),
  [Definition 3.3/Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf#page=17):
  integer curve height downstairs, computed by dividing a splitting
  extension's Tate order by its ramification index. L100's audited
  semistability and local-height calculation specializes this to
  h_z=max(0,-ord_z(j(E_o))) at every actual completion of F and C,
  including nonsplit reduction and residue characteristic ell.
- Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
  [Theorem 3.34, pp.59–60; Corollary 7.42/Remark 7.43, p.124;
  Exercise 4-2/solution, pp.83,155](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
  for a number-field extension C/F and a fixed F-place x,
  sum_(w|x) e(w/x)f(w/x)=[C:F]; the corresponding local degree is
  e(w/x)f(w/x). Integer valuations restrict by e(w/x), and residue
  degrees multiply. These identities do not require F/Q normal,
  tame ramification or residue characteristic different from ell.
- Mochizuki, *IUT IV*, April 2020,
  [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=47),
  Corollary 2.2(ii), proof pp.44–47: the height is normalized before
  adjoining ell-torsion, P3 is on p.45, and the first omitted-ell
  display on p.47 retains a coefficient 1/6 on both sides. This is
  the qualified text comparison recorded in the assessment, not an
  authenticated current author/journal version or a definition over C.

The main gap remains original finite B>=A. The intermediate target
is precisely (1)–(2); it could support the numerical omitted-ell
part of a normal-closure repair without first proving ell-integrality.
L092 gives degree data but no height transfer, L100 gives the height
formula and P2 transfer, and L101 gives only downstairs P3. Thus
this quantitative assembly is not already one of their conclusions.
The local test passes only with actual relative completion degrees;
the normalized test requires all extending places and residue weights.
A failure of either hypothesis or normalization would stop this test.
ATTEMPTS/035's authentication route stays parked.

### Actual tower and local bound

Set m=[C:F]. The actual inclusion F subset C and L092 give

    m=1105920/276480=4.

Fix any x|ell in F and any actual w|x in C. Write r_w=e(w/x),
s_w=f(w/x). The imported completion decomposition, at this fixed x,
gives

    sum_(w|x) r_w s_w=m=4.                              (3)

All terms are positive integers. Hence r_w<=r_w s_w<=4 for every
w. This is a bound on the actual local extension C_w/F_x; equality
of different local indices over the possibly nonnormal F is not used.

Put j=j(E_o). L100's height formula applies to these same fields and
curve: full 15-torsion gives semistability at every completion, using
level five at ell>=7. Its nonsplit height normalization is already
included. Restriction of integer valuations therefore yields

    h_w=max(0,-ord_w(j))
       =max(0,-r_w ord_x(j))=r_w h_x.                  (4)

If h_x=0, then h_w=0<4sqrt(H) since H>25. If h_x>0, the same
prime's strict downstairs P3 and r_w<=4 give
h_w=r_w h_x<=4h_x<4sqrt(H). This proves (1) for every w|ell.
No splitting extension or ell-division field replaces C_w or F_x.

### All-place regrouping and strict normalized bound

Absolute residue degrees satisfy f_w=s_w f_x. Finite regrouping
over every actual x|ell, followed by (3)–(4), gives

    H_ell(C)
      = log(ell)/[C:Q] sum_(x|ell) sum_(w|x) r_w h_x s_w f_x
      = log(ell)/(4[F:Q]) sum_(x|ell) h_x f_x * 4
      = H_ell(F).                                      (5)

Thus the relative ramification growth cancels exactly with the
relative residue-degree sum and global normalization. A pointwise
factor-four upper estimate alone would not give (5).

There is a nonempty finite set of F-places above ell. Every f_x is
positive, every h_x<sqrt(H), and sqrt(H)>0. Consequently

    sum_(x|ell) h_x f_x < sqrt(H) sum_(x|ell) f_x.

This is strict also if all heights vanish. Applying prime
decomposition to F/Q gives

    sum_(x|ell) e(F_x/Q_ell) f_x=[F:Q].

Each absolute ramification index is at least one, so sum f_x<=
[F:Q]. Division by [F:Q] and multiplication by the positive
log(ell) prove the strict bound in (2). Division by six preserves
strictness and the source's coefficient; it does not construct a
native pilot or justify a repaired application of Theorem 1.10.

The test passes with actual local multiplier at most four and
normalized multiplier exactly one. Native selected support and
ell-integrality, L092's relative factor-four excess, exact generation,
P4–P7/full selected-theta data, complete repair, source authentication,
native input/action/factorization/pilot, essentiality and finite B>=A
remain unresolved. No complete-solution candidate is asserted.

### Separate critical audit — 2026-10-23, step410

**Scope and input compatibility.** The invocation-start SPECIALIZE
assessment is `drafts/literature/2026-10-23-normal-closure-p3-transfer-critical-audit.md`.
The proof passes without correction. L101 supplies one fixed member,
ordering, curve, literal F and prime; its proof and step406 audit give
H>xi^2 with xi>=5, so the strict H>25 used here is available.
Its P3 holds at every actual F-place above that same ell. L092's
degree calculation concerns exactly these full-coordinate fields in
the same closure, and C contains F. Thus [C:F]=1105920/276480=4.
Neither an old auxiliary witness nor a field obtained by adjoining
ell-torsion is substituted. The direct inputs remain L092,L100,L101.

**Local theorem hypotheses and all reduction cases.** Both fields are
number fields; C/F is finite separable. For each nonarchimedean
F-place x, the cited Milne decomposition theorem applies to the
entire fiber over x. Each completion C_w/F_x is a finite extension
of local fields, with degree r_w s_w. Hence its positive integer
degree is at most their complete sum four, and r_w<=4. This uses no
equality between different local indices, no normality of F/Q and
no tame hypothesis. The proof needs this bound, not the numerical
value of each individual completion degree.

L100's semistability and height calculation precedes and does not
use its conditional P2 inference. Full geometric 15-torsion is
rational over both fields and stays rational under each completion;
level five is invertible at ell>=7. Its audited local argument
therefore supplies h_x=max(0,-ord_x(j)) and the corresponding
formula at w. For good reduction both heights are zero. For split
multiplicative reduction the full integral Tate-series remainder
gives height -ord(j). For nonsplit multiplicative reduction GenEll
divides the splitting-field Tate order by the ramification index,
not the extension degree, yielding the same formula downstairs.
These are precisely the cases justified in L100, not an assumption
that every multiplicative place is split. Valuation restriction
ord_w(j)=r_w ord_x(j) and r_w>0 now verify (4). The two cases
h_x=0 and h_x>0 give strict (1) with the original H and prime.

**Full weighted identity and strictness.** For each fixed x, absolute
residue degrees multiply as f_w=s_w f_x. Thus its entire contribution
to the numerator upstairs is

    sum_(w|x) h_w f_w = h_x f_x sum_(w|x) r_w s_w
                      = 4 h_x f_x.

Every w over ell lies over exactly one such x; both fibers are finite.
Dividing by [C:Q]=4[F:Q] proves (5) without exchanging any infinite
sums. In particular there is no residual factor four in H_ell(C).
The strict inequality downstairs has positive margin

    sqrt(H) sum_(x|ell) f_x - sum_(x|ell) h_x f_x
      = sum_(x|ell) (sqrt(H)-h_x) f_x > 0:

the fiber is nonempty and every summand is positive. This explicitly
covers the all-zero-height case. The separate absolute decomposition
sum e_x f_x=[F:Q] gives sum f_x<=[F:Q]; following the strict
inequality by this weak one preserves strictness. Both division by
[F:Q] and multiplication by log(ell) use positive numbers. This
checks all weights and endpoints in (2), without equal-e,f reasoning
over the nonnormal field F.

**Source normalization and verdict.** The step407/409 inspected April
reproduction passage, Corollary 2.2(ii) proof p.47, has the factor
1/6 on each side of its omitted-ell comparison. The cited height on
p.44 is the pre-ell-division-field height. Accordingly dividing (2)
by the positive six gives exactly the asserted numerical comparison
H_ell(C)/6<sqrt(H)log(ell)/6. L102 does not equate its left side
with the source's difference of pilot log quantities, whose sign,
selected support and native-data prerequisites require their own
identification. No such equality is needed for the present conclusion.
The original P3 constant one upstairs is also not asserted.

The result is a verified known-method numerical transfer, not progress
beyond the inspected sources or an essential IUT flaw. Ell-integrality,
native support/omitted-term identification, the relative factor-four
degree excess, P4–P7/full selected-theta data, exact generation and
complete repair, reproduction authentication/def= qualifications,
native input/action/factorization/pilot and essentiality remain open.
Original finite B>=A is unchanged. The argument and direct inputs
are unchanged, so PROOF.md and DAG.md are unchanged; this canonical
audit supersedes the overview's pending wording for L102 only.

## Mathlib

Full matching and supporting Mathlib coverage for this same-member
specialization have not been checked. Unknown coverage is not absence.
The proof imports the cited classical theorems and verifies only the
finite-tower specialization and full weighted normalization. It claims
no mathematical progress beyond the inspected sources.
The separate step410 audit is an informal verification, not a
formalization or a numerical certificate.
