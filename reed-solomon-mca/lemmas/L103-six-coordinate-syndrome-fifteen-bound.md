# L103 — Six-coordinate syndrome pencils have at most fifteen bad parameters

## Hypotheses

Let F=F_(97^20), let H be the order-sixteen subgroup of F_97^*, and
let C=RS[F,H,8] be the evaluations of polynomials of degree less than
eight. Use the pinned same-support event at 1/4<=delta<5/16. For
a,b in F^H write
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^j\quad(1\le j\le8),\qquad
 s(T)=\sigma(a)+T\sigma(b).
\]
Assume L010's actual Hankel determinant D and every actual coordinate
locator are nonzero polynomials in F[T]. Let B=B(a,b) be the entire
original finite bad-parameter set.

Suppose some S subset H of size six satisfies
\[
 \sigma(a),\sigma(b)\in U_S,
 \qquad U_S=\{\sigma(z):\operatorname{supp}(z)\subseteq S\}.
\]
This is coefficient-syndrome membership, not confinement of all actual
error supports to S. The original words, weights, coefficient syndromes
and finite chart may be arbitrary over F; independence is not assumed.
Inactive coordinates and nonzero constant lift coordinates are allowed.

The imported L040 bound and L069 universal configuration bound retain
their explicit complete-finite-certificate qualifications. Their earlier
audits are reused; this proof does not rerun those certificates.

## Conclusion

The full original bad set satisfies |B(a,b)|<=15. If the unique affine
lift on S has at most five active coordinates, the stronger bound
|B(a,b)|<=11 holds.

The equality-conditioned bridge is explicit: if |B|=16 and all six
lift coordinates are active, exactly three distinct original finite
bad parameters have actual errors equal to that lift. Their zero sets
partition S into pairs, and the lift has precisely the explicit form
required by L033. L040 contradicts this hypothetical equality.

This proves the bound only for the represented class in the hypotheses.
It neither supplies such a six-set for arbitrary pencils nor improves
the global interval 11/q–16/q. Uniform triangle twelve, cyclic
feasibility and challenge-definition qualifications remain unresolved.
The separate critical audit of 2026-10-17 found no defect in this local
specialization or its full-event imports. It is not a complete challenge
candidate; the computational qualifications above remain essential.

## Proof

### Imported inputs and the unique affine lift

Use L010's kernel identity ker(sigma)=C, injectivity on any set of at
most eight coordinates, unique error representatives of weight at most
four, same-support badness and |B|<=16. In particular its equality
conclusion says that |B|=16 forces sixteen distinct actual full-weight
four-errors, with each label in exactly four of their supports. Singular
and lower-weight errors are included in its bound before equality is
assumed.

The standard distance input is J. I. Hall, *Notes on Coding Theory*,
GRS chapter, Theorem 5.1.1 and complete proof, printed pp. 63–64 of the
[undated author-hosted chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf).
Its hypotheses allow any field, distinct evaluation labels, nonzero
multipliers and 0<k<=n. Here F is a field, H has sixteen distinct
labels, every multiplier is one and k=8, so every nonzero codeword has
weight at least nine. This theorem is imported, not reproved. Its source
coverage is reused from the prior assessment, not newly retrieved.

By membership in U_S there exist u,v supported on S with
sigma(u)=sigma(a), sigma(v)=sigma(b). L010's injectivity on S makes
these representatives unique. Define
\[
 f(T)=u+Tv,\qquad \sigma(f(T))=s(T).
\]
The identity is polynomial and holds in all eight shifted moments.
No value f(T) is presumed to be a sparse actual error. Let
\[
 A=\{x\in S:f_x(T)\text{ is not the zero polynomial}\}.
\]

### Inactive-coordinate case

If |A|<=5, choose any five-set A' with A subseteq A' subset H.
Both coefficient syndromes lie in U_(A'), since u,v are supported on
A. The field, H, dimension, pinned event and actual nonzero D/locator
polynomials are unchanged. These are exactly L015's hypotheses, giving
\[
 |B|\le5+M(A')\le11.
\]
The last inequality imports only L069's universal conclusion M(A')<=6
for every five-set; its conditional triangle theorem and subtraction of
three base events are not used. L015 includes dependent coefficient
syndromes (with bound at most one) and all original cancellation and
singular parameters. Its hypotheses already exclude a lift on at most
four coordinates; no such lift is silently assumed nonpersistent.
L069's complete census and independent replay, including their shared
compiler and residue-field qualification, remain part of this input.

### Distance forces three equal-vector errors at equality

It remains to treat A=S. Each of the six coordinate polynomials f_x
is now nonzero of degree at most one; nonzero constants are retained.
Suppose for contradiction that |B|=16. By L010, every T in B has a
unique full-weight error e_T with sigma(e_T)=s(T). Put
\[
 E=\{T\in B:e_T=f(T)\},\qquad t=|E|.
\]
For T in B minus E, the vector f(T)-e_T is a nonzero codeword because
its syndrome is zero. Writing m_T=|S intersect supp(e_T)|, distance
nine gives
\[
 9\le\operatorname{wt}(f(T)-e_T)
   \le|S\cup\operatorname{supp}(e_T)|=10-m_T,
 \qquad m_T\le1.                                      \tag{1}
\]
The support upper bound uses the fixed six-set S, not supp(f(T)).
Vanishing lift coordinates, overlapping errors at such coordinates and
any cancellation in the difference can only decrease its support.
The equal-vector exception is explicitly excluded from (1).

For T in E the four nonzero error coordinates lie in S, so m_T=4.
L010's equality balance on the six labels of S therefore yields
\[
 24=\sum_{T\in B}m_T
       \le4t+(16-t)=16+3t.
\]
Since t is an integer, t>=3. This proves the existence of three actual
finite equal-vector errors without first selecting any actual error
inside S or assuming confinement of the remaining errors.

### All cancellations and the precise paired-root form

For each T in E, f(T)=e_T has weight exactly four on the six-set S.
Consequently
\[
 Z_T=\{x\in S:f_x(T)=0\}
\]
has size exactly two. If T,T' are distinct elements of E, their zero
sets are disjoint: a nonzero affine polynomial cannot have two distinct
finite roots. This includes nonzero constant coordinates, which have
no roots. Hence 2t<=6, so t<=3. Combined with the incidence inequality,
t=3. Write E={gamma_1,gamma_2,gamma_3} and Z_i=Z_(gamma_i).
The three pairwise disjoint two-sets Z_i exhaust S.

Every x in S therefore belongs to exactly one Z_i. Its nonzero affine
polynomial has the finite root gamma_i, so it cannot be constant and
has the form
\[
 f_x(T)=c_x(T-\gamma_i)\quad(x\in Z_i),\qquad c_x\in F^*.
                                                               \tag{2}
\]
Off S the lift is identically zero. At gamma_i the four coordinates
in S minus Z_i are nonzero, because the three gamma_i are distinct
and all c_x are nonzero. Thus the three actual full-error supports
are S minus Z_i, and their union is exactly S.

Independence required for L033 follows here, rather than being assumed:
for x in Z_1 and y in Z_2, the coefficient columns of u,v are
(-c_x gamma_1,c_x) and (-c_y gamma_2,c_y), with determinant
c_x c_y(gamma_2-gamma_1)!=0. The vectors u,v are independent, and
injectivity of sigma on S makes their syndromes independent too.
Thus dependent starting syndromes cannot escape this equality argument.

### Full-event bound and qualifications

Equations (2), the partition S=Z_1 disjoint union Z_2 disjoint union Z_3,
and sigma(f(T))=s(T) verify L033's alternative explicit-triple hypotheses.
The gamma_i are distinct finite parameters in the unchanged original
chart; their errors are actual, full and unique. The field, subgroup,
code, radius cell and actual polynomial nonpersistence assumptions are
precisely those of L033/L040. No projective change, rational chart,
prime-field weight descent, L032 classification or triangle recovery
assumption is needed.

Import L040's audited conclusion for this explicit L033 pencil. It bounds
the entire original set B by fifteen: with N_3=0 its complete paired-ratio
and matching-completion certificates give N_ext<=12 and
|B|=3+N_ext<=15; if N_3>0, its separate L010/L033 lower-weight case
already gives |B|<=15. In the present hypothetical equality N_3=0 by
L010, so the first case applies and contradicts |B|=16. L010's integer
upper bound then gives |B|<=15 without an equality hypothesis. The
initial reduction to equality has not discarded any singular, zero-
weight or lower-weight event.

The shortening input inherited through L033/L040 is I. Marquez-Corbella
and R. Pellikaan, *A characterization of MDS codes that have an error
correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript dated February 29, 2016](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and the following unnumbered
GRS shortening formula, printed pp. 7–8. L033 has already checked the
distinct labels, changed nonzero retained multipliers, positive shortened
dimensions and all eight moments. This unchanged application imports
that reduction and L040's audited finite obstruction, without a new
shortening proof or new finite enumeration.

The gate assessment saved before this invocation is
`drafts/literature/2026-10-17-general-six-coordinate-bound-review.md`.
The missing-premise change from L070/L082 is that the present argument
starts from coefficient-syndrome membership only. It adapts their
fixed-set distance/equal-vector mechanism and L032's affine zero
accounting to extract the triple. None of those earlier statements is
applied outside its scope. This is a REPRODUCTION specialization of the
assessed tools, with no originality claim or assertion of progress
beyond unread sources. No mathematical scripts or cross-notebook input
are used. The separate audit of this assembly is recorded below.

### Separate critical audit, 2026-10-17

Step 2026-10-17-mca-287-general-six-coordinate-critical-audit checks this
assembly under the unchanged SPECIALIZE assessment. It found no
mathematical defect. This is local verification of a reproduced class
bound, not a new theorem beyond the checked sources or a fresh finite
census. The proof and its mathematical inputs are unchanged.

The audit read L010 and L015 in full, L033's explicit hypotheses and
full-event accounting, and L040's hypotheses, conclusion, equality
entry and relevant earlier audit. It checked L069's universal census
argument and separate audit rather than apply its conditional triangle
conclusion. The complete L040 and L069 certificate audits are reused;
their programs and certificates were not rerun in this step.

First, the eight shifted moments and code are exactly L010's. On the
six-set, injectivity gives coefficient vectors u,v individually, not
only a parameter-dependent choice of lift. Consequently f(T)-e_T has
zero syndrome for every actual error. L010 identifies the entire
original bad set with weight-at-most-four representatives, proves
uniqueness, and gives sixteen as an upper bound before fullness or
balance is invoked. Its multiplicity proof includes every singular
parameter. Hall's cited Theorem 5.1.1 applies over the stated extension
field with sixteen distinct labels and unit multipliers, giving distance
n-k+1=9. No fresh distance theorem or source retrieval is claimed.

Second, the inactive-coordinate branch supplies precisely the membership
hypothesis of L015 on a five-set containing the active coordinates.
Its nonpersistence and field assumptions are inherited unchanged.
L069's M<=6 is universal over all five-sets and has its own complete
census proof; that statement does not require L069's triangle or pair
hypotheses. Hence 5+M<=11 bounds the entire original set B. The stronger
dependent-syndrome clause of L015 is consistent with this bound. An
active set of size at most four is excluded by the assumed polynomial
nonpersistence, as L015 proves, rather than being a missing case.

Third, at hypothetical equality, every error has exactly four nonzero
coordinates. For T outside E the codeword f(T)-e_T is nonzero; its
support is contained in S union supp(e_T), of size 10-m_T. Thus m_T<=1
even if a lift coordinate vanishes or a difference cancels. For T in E,
the actual error is supported on S and has m_T=4. Coordinate balance
counts exactly 6*4=24 incidences with this fixed S, giving
24<=4t+(16-t) and the integral bound t>=3. The distance inequality was
never applied to a zero codeword or to an unproved full error.

Fourth, the six active coordinate polynomials are nonzero and affine.
At each equal-vector parameter exactly two vanish, and no coordinate
can vanish at two distinct finite parameters. Hence 2t<=6, so t=3;
the zero pairs exhaust S. A nonzero constant has no root and therefore
cannot remain in this exhausted set. All six slopes are nonzero, and
the distinct roots give exactly (2). Each extracted error has support
S minus its pair; every label occurs in two of these three supports.
The displayed two-coordinate determinant has sign and value
c_x*c_y*(gamma_2-gamma_1), so independence of u,v and their syndromes
follows without a prior independence assumption.

Finally, these are three actual bad parameters in the original finite
chart, not just compatible projective directions. Equation (2) verifies
L033's explicit alternative to entering through L032. No additional
classification premise is required. At hypothetical equality L010 gives
N_3=0, so the exact L040 hypotheses hold, with N_ext=16-3=13 by L033.
L040 gives N_ext<=12, the required contradiction. Independently its
N_3>0 clause still bounds the full event by fifteen; no lower-weight
or singular case is removed from the unconditional conclusion. All
scalars and the excluded original direction remain arbitrary over F.

L040's complete paired-ratio and matching-completion certificates and
L069's full two-method census remain essential imported evidence, with
the qualifications recorded there. No additional DAG edge is needed:
the exact explicit L033 entry avoids treating L032, L070 or L082 as
unstated inputs. The historical failures in ATTEMPTS/006,007,017,027
concern smaller generators or incidence-only extraction; none refutes
this additional syndrome-space hypothesis. The separate audit validates
the class bound fifteen (eleven in the smaller class), not universal
six-set representation or a change to the global 11/q–16/q interval.

## Mathlib

Full matching six-coordinate bound and equality-conditioned extraction:
**not checked**. Supporting affine-polynomial root, finite-field,
Vandermonde, coding-distance and incidence coverage: **not checked**.
Unknown coverage is not absence. L040/L069 remain computational inputs,
not Lean-certified results. The pinned ArkLib event is separate from
Mathlib and is not identified with the unread July ABF26 statement.
