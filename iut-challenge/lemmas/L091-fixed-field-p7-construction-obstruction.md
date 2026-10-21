# L091 — Finite exceptions do not repair the literal fixed-field (P7) construction

## Hypotheses

Retain audited L089's fixed c,h,d_*,e_*, original rational monic
family, closure Q-bar and domains K_infinity,K_2. Retain audited
L090's literal equations and full-coordinate division fields in that
closure. Write U=P^1_Q minus {0,1,infinity} and

    J(t)=256(t^2-t+1)^3/(t^2(t-1)^2).

The source assertion tested is the fixed-F initial-data construction
in Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020,
Corollary 2.2(ii), printed pp.41–43, proof pp.43–46 through (P7),
in the inspected [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf).
Its antecedent and fixed-field scope are those inspected in the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-20-compact-survivor-fixed-field-corollary-test.md`.
Use d=6 and epsilon_d=1. This qualification does not authenticate
the reproduction against current author or journal bytes.
The field prescription is read by its explicit `def=` and following
explanation: the first field expression denotes the stated Legendre
adjunction over F_tpd. An additional requirement that it independently
be an ordinary division field of an F_mod-model is outside this
conclusion; the audit below explains why that reading changes the test.

## Conclusion

For every finite set S subset U(Q-bar)_(<=6), there is one L089
survivor E/Q such that every one of its six ordered-root parameters
t_o lies in K_V minus S. For each such ordering the following data
meet the inspected corollary's displayed antecedent:

    T=Q(t_o)=F_tpd,  F_mod=Q,
    E_o: V^2=X(X-1)(X-t_o) over T,
    F=G_o=T(iota,E_o[15]),  iota^2=-1,
    E_F=E_o base changed to F.

Nevertheless [F^nor:F]=4, whereas (P7)'s initial data on this same
F require F/F_mod to be Galois, hence that index to be one. In
particular no choice of the one fixed finite Exc_6, or of a root
ordering, makes this literal fixed-field construction valid for all
its displayed inputs.

The separate step363 audit below validates this local construction
objection to the qualified (P7) assertion under that definitional
reading. It is not a disproof of the numerical conclusion
(C2), an exclusion of every alternative model/field construction,
or a demonstration of an essential inherent IUT flaw. No complete
solution candidate is claimed; the original finite B>=A remains open.

## Proof

### Source imports and the discriminating test

The approved target is the fixed-field (P7) test, not another source
retrieval or a reproof of occurrence and normal-closure theorems.
Use audited L089 for the domains, infinitude, degree and original
joint-image conditions, and audited L090 for the same-member native
fields and index four for all six literal equations. Their complete
proofs and cited general inputs are retained in those canonical
results. The necessary new application is finite-set avoidance and
the simultaneous antecedent check below.

Import the corollary's quantified scope from its cited statement and
proof: domains are fixed before d,epsilon_d and Exc_d; the latter
is one finite parameter set; the input lift has degree at most d;
full 15-torsion is F-rational; and the prescribed Legendre field is
retained when (P7) asserts all initial-data clauses. The displayed
antecedent has no separate Galois/initial-theta-data hypothesis.
Theorem 1.10, p.22, instead assumes initial data and is not being
refuted by failure of its antecedent.

The necessary condition used here is Mochizuki, [IUT I, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(b), pp.61–62: the initial-data field F is Galois over
F_mod (and has degree prime to the chosen ell). Only Galoisness is
tested. This is a definition, not an imported claim that the disputed
construction succeeds. Native identifications use IV Proposition
1.8(ii),(iii), pp.18–20, and the opening of Theorem 1.10, p.22,
as applied and audited in L090. No general result is reproved.

The main gap remains finite B>=A. This intermediate test could
isolate an error in a claimed initial-data construction. Continue
only if one member meets every displayed antecedent and the
necessary condition applies to its unchanged F. Abandon the claimed
contradiction upon a failed antecedent or a reading permitting a
different F. Essentiality and possible repairs are independent gaps.

### Avoidance after all domains and exceptional choices are fixed

Fix exactly L089's domains, with support {infinity,2}. They are
allowed domains in U in every required topology, and
J(K_2) subset O_(Qbar_2), so the corollary's integer bound can be
N=0. Fix d=6 and epsilon_d=1 after these domains. Let S be any
finite set as in the conclusion; in particular it may be the entire
Exc_6 furnished for these choices, including its finite enlargements.

Since S avoids the cusps, J is finite-valued on S. Thus J(S) is a
finite subset of Q-bar. L089 supplies infinitely many distinct
rational j-values of survivors of the unchanged family. At least
one lies outside J(S): otherwise that infinite set would be a subset
of the finite set J(S). Select one such survivor E, once and for all.

For each ordering o, L089 gives J(t_o)=j(E), t_o in K_V and
[Q(t_o):Q]<=6. If any t_o belonged to S, then its J-value would
belong to J(S), contradicting the choice of E. Hence all six lie
outside S simultaneously. This does not assume S is Galois stable
or closed under the six parameter transformations. In particular
the domains did not change with S, and the selected survivor is
chosen only after S. Every later field in this proof belongs to
this member; no named old witness is substituted.

### The full displayed antecedent on the same member

Fix any ordering o and take the displayed T,E_o,F,E_F. The roots
of the original cubic are distinct, so t_o differs from 0,1, and
E_o is nonsingular. L090 gives the embedded equalities
F_mod=Q and F_tpd=Q(t_o)=T for its unmarked punctured object.
The equation is a literal Legendre model over T. Its base change
E_F has that same geometric punctured object. The lift x_E=t_o is
in U(F), belongs to K_V minus S, and has degree at most six.
The degree bound concerns Q(t_o), not the possibly larger field F.

The field F is a number field: T is a number field, iota is
algebraic and the finitely many torsion coordinates are algebraic
over T. Its definition adjoins both coordinates of every geometric
15-torsion point of E_o. Under the fixed algebraic closure,
E_F[15]=E_o[15] as complete geometric point sets, since base change
does not change the multiplication-by-15 equations. All those points
are therefore F-rational. Consequently the exact generation equality
is F=F_tpd(iota,E_F[15]), with E_F understood through its specified
T-descent. No rational isomorphism between E_o and the original
Q-curve is needed, and no x-only division field is used.

Together with the already checked domains, d,epsilon_d and avoidance,
these discharge the complete displayed antecedent in the approved
source scope. The height-selected ell, cyclic subgroups, bad places,
core conditions and other initial-data choices in (P1)–(P6) are
claimed outputs of this construction. They are not additional
displayed hypotheses being silently assumed here. We assert no
independent verification of those outputs and do not use prime seven
in place of the source's chosen ell.

### The fixed-field necessary condition fails

L090 applies to this same survivor and ordering and yields
[F^nor:F]=4 over its proved native F_mod=Q. In characteristic zero
all finite extensions are separable; such an extension is Galois
exactly when it is normal, equivalently when it equals its normal
closure. Thus this F is not Galois over F_mod. The achieved index
four is strictly above the required index one.

If (P7) supplied all of I Definition 3.1(a)–(f) on this unchanged F,
clause (b) would force the opposite conclusion. No choice of ell,
cover, cusp or place can change this property of the fixed field.
The contradiction is to that fixed-field assembly for the exhibited
antecedent data. Because S was arbitrary finite and all six rows
were retained, neither a finite exceptional enlargement nor changing
the ordering removes this obstruction within the literal family.

### Qualifications and remaining gaps

The finite-avoidance/application test passes under the inspected
fixed-F reading. This is local progress by known methods; no result
beyond the checked literature is certified as original. The separate
audit below validates the combined application and makes its field
interpretation explicit. The source qualification remains part of
the statement.

There is no inference here that (C2)'s numerical estimates are false,
that another scaled/twisted descent or an enlarged field cannot work,
or that the defect is essential to IUT. Authentication/current-version
applicability, possible field repairs, independent initial-data outputs,
actual native input/action/factorization and marked pilot transport
remain open, as does original finite B>=A. ATTEMPTS/033–034 remain
intact. No mathematical script or numerical evidence is used.

### Separate critical audit — 2026-10-20, step363

**Verdict and inputs.** The combined application passes the exact
invocation-start scope in
`drafts/literature/2026-10-20-fixed-field-p7-critical-audit.md`,
with the definitional-reading qualification stated above. The full
proof was checked against audited L089 and L090, the step360 checklist
and the incorporated source clauses. The audit adds no occurrence,
normal-closure or repair theorem. Its necessary clarification is that
the antecedent check must retain both expressions in the source's
display, rather than silently omit the first one.

**Finite exceptions and the same member.** The domains and support
are exactly those in L089; that result checks every finite 2-adic
extension and all embeddings. Their integer j-bound is N=0. The
choices d=6 and epsilon_d=1 satisfy the required ranges. The unspecified
constants preceding these choices cause no extra assumption: the
argument works for every finite S, so also for a set with any additional
height bound required of the source's exceptional set.

The rational function J has no pole on U, hence its image of S is
finite. L089 supplies infinitely many distinct j-values, rather than
just infinitely many equations. Select a survivor outside J(S) after
S is fixed. Every ordered t_o of that survivor has the same J-value,
so none belongs to S, regardless of whether S is stable under any
conjugation or parameter transformation. All six t_o lie in the
unchanged domains and have degree at most six. This proves the full
quantifier order; it uses no effective bound, limit interchange or
subsequent reselection.

**The complete field display and its force.** The displayed prescription
in [IV, Corollary 2.2(ii), p.42](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf#page=42)
is, in the present plain-text notation,

    F = F_mod(sqrt(-1), E_(F_mod)[2*3*5])
      def= F_tpd(sqrt(-1), E_(F_tpd)[3*5]).

Its following explanation specifies a Legendre model over F_tpd.
Theorem 1.10, p.22, uses the same convention. Our interpretation
therefore retains the first expression as the name defined by the
second, not as a separately chosen Q-model's ordinary division field.
In this convention L090 gives T=F_tpd and the literal E_o over T;
its full-coordinate field is exactly the right-hand side. Thus both
expressions, with this definition, denote the chosen G_o.

There is a substantive alternate reading to exclude from the verdict.
Suppose instead that the first expression independently required

    F = Q(iota, E'[30])

for an elliptic curve E'/Q. That field is Galois over Q: every
Q-automorphism of the algebraic closure permutes the complete
30-torsion set of the Q-defined E' and sends iota to ±iota, so it
preserves the generated finite field; characteristic zero gives
separability. This is the finite normality criterion cited in L090
from Milne, *Fields and Galois Theory*, Theorem 3.17 and Remark 3.18.
Consequently L090's index four rules out that equality for every E',
not merely for the original survivor. Under this additional hypothesis
our example fails the antecedent and supplies no contradiction.
Proposition 1.8(iv) does not provide such an equality or such a
Q-descent: its conclusion is over the field on which both models have
the specified rational torsion. The explicit `def=` and explanatory
adjunction justify the narrower reading tested here; the audit does
not identify the two readings or infer the author's unstated intent.

**Actual descent and incorporated clauses.** Fix one of the same six
orderings. L090 identifies the unmarked punctured geometric object
and its embedded fields F_mod=Q and F_tpd=T. Its nonexceptional
j-value lies strictly between 0 and 1728, so its geometric pointed
automorphisms are precisely ±1. The T-model E_o exists by its displayed
equation, is nonsingular because t_o is neither zero nor one, and
has its origin and the three nonzero two-torsion points over T.
Thus T is perfect, two is invertible, the geometric moduli stabilizer
is all G_T and the two-torsion action is trivial. These verify the
hypotheses of Proposition 1.8(vi) for this actual T. The choice of a
Legendre twist allowed there is already made explicitly by E_o; it
need not be T-isomorphic to the original Q-curve.

F is a finite extension of T. All points in E_o[15] are F-rational,
because both coordinates of the full geometric set were adjoined.
The base change E_F has precisely that torsion set. It is already
the base change of E_o by construction, so the rational isomorphism
claimed in the corollary's parenthesis is the identity here. If one
uses Proposition 1.8(iv) to verify that parenthesis, its base is F,
which is perfect of characteristic zero, and prime 3 is invertible;
both descents have all their 3-torsion rational over F. No assertion
about rational 15-torsion on the original Q-curve is inserted.

The reduction parenthesis presents no missing hypothesis either.
For every finite place v of F the completion is a complete discrete
valuation field. When its residue characteristic is not 3, use prime
3 in Proposition 1.8(v); at residue characteristic 3 use prime 5.
The chosen prime is at least three and invertible in the valuation
ring, and the whole corresponding torsion set remains rational after
completion. Thus the cited semistability conclusion applies at every
finite place, including those above 2. No splitness, regular model
or local use of the last part of (vi) at residue characteristic 2 is
being assumed. These are applications of the cited clauses, not
independent proofs of their general assertions.

Finally x_E=t_o is the point of the lambda-line whose classified curve
base changes to this E_F itself. It belongs to U(F) and has degree
[Q(t_o):Q] at most six. There is no need for [F:Q] at most six.
The full prescribed field, lift, moduli and torsion conditions all
refer to this member and this equation.

**Fixed-field output and the exact obstruction.** The sentence before
(P7), IV p.46, retains the already given F and asserts all clauses
of I Definition 3.1(a)–(f). The reused May 2020 I source, Definition
3.1(b), pp.61–62, makes Galoisness over F_mod necessary. By L090 the
same F has normal-closure index four over its native F_mod=Q, whereas
this clause requires index one. This necessary condition fails
independently of the choice of the height-selected prime, cusp, cover
and places. Neither (P1)–(P6) nor all independent initial-data outputs
are assumed or certified. Replacing F by its normal closure would
change the tested datum; no such replacement occurs at this fixed-F
step.

The conclusion is a checked, qualified local construction objection,
not a verified resolution of the challenge. In particular the audit
does not refute (C2), rule out a repair, authenticate the reproduction,
or establish essentiality to IUT. The original finite B>=A and the
native input/action/factorization/pilot obligations remain open.
The original finite-avoidance and nonnormality evidence is preserved;
only the interpretation boundary has been made explicit. No new
direct mathematical input is added to the DAG.

## Mathlib

Full matching and supporting Mathlib coverage for this combined
application has not been checked. Unknown coverage is not absence.
The proof is an informal application of audited occurrence and
native-field results, the precisely cited source clauses and finite
set avoidance; it is not formal verification.
