# L060 — Native parametric place section and actual quotient cusp

## Hypotheses

Retain L053,L057,L058,L059 and their hypotheses and actual maps. Thus
E_0/Q is the unchanged reselected curve, F=Q(zeta_60,E_0[30]),
K_glob=F(E_0[7]), H=F_u subset N=(K_glob)_w subset Omega,
M>=max(M_tors,31), and the fixed pointed Tate isomorphism uses the
changed q_0 in Q_3 with v_3(q_0)=30 and v_3(3)=1. Full 30-torsion,
the stable log model, graph comparison and local splitting are those
already established. Neither K_glob=N nor q_0=3^30 is assumed.
Use the actual U, alpha:E -> B=E/U, psi:B -> E, V=ker(psi),
0_B,Q, and c:Z/7Z -> V. In particular Q has order seven and
c(1)=Q or -Q. Set X=E minus {0_E} and Y=B minus V.

Let F_mod be the native field named in IUT I Definition 3.1, and use
that definition's natural surjection

rho: V(K_glob) -> V(F_mod).

Here V(-) denotes the full set of places; the torsion subgroup V above
is a different object. The restriction rho(w) is defined by this
native surjection. This is conditional on the native field/place setup
as specified there, without computing F_mod or replacing it by Q.
No claim that all the other initial-data conditions hold is a premise
or a conclusion of this lemma.

## Conclusion

There exists a full section s of rho with s(rho(w))=w. Put
v_*=rho(w) and designate {v_*} as the proposed nonempty selected
bad subset for the (e)-(f) tests below. This designation does not
certify the independent admissibility conditions in (b)-(c).
Its inverse under the chosen section is exactly {w}; v_* has residue
characteristic three. The same global rank-one cover of L053 has the
required local graph type and admits the compatible local splitting
at this sole selected bad member.

The global nonzero cusp of the inversion quotient is the image of the
actual pair {Q,-Q}. It is K_glob-rational, is a scheme cusp, differs
from the origin cusp, and at w has the native sign label {1,-1}.
Consequently the section/local-type and distinguished-cusp tests of
Definition 3.1(e)–(f) pass for this singleton, conditionally on the
native field/place setup and the retained inputs. No test is asserted
at a second selected bad member.

The separate critical audit below validates this conditional
known-method specialization, with an algebraic scheme neighborhood
of the nonzero cusp made explicit.
It does not construct full initial Theta-data, compute F_mod, prove
all-F-place q-order coprimality or supply actual input/action/pilot/
essentiality or finite B>=A. It is not a candidate essential IUT flaw.

## Proof

### Source predicates and imported scope

Reuse the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-native-moduli-parametric-section.md`.
The relevant exact predicates are in
[Mochizuki, IUT I, May 2020 author text](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
Definition 3.1(b)–(f), printed pp.61–63. The inspected text is the
[186-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
with byte identity and journal-version equivalence unverified, as in
the retained source record. Clause (e) selects a section over all
moduli places but tests local type at its selected bad members;
clause (f) tests one fixed nonzero global cusp there. Clause (b)
permits a nonempty bad subset, rather than requiring every bad place.

[Mochizuki, EtTh, PRIMS 45 (2009), 227–349](https://ems.press/content/serial-article-files/41069?nt=1),
section 2 opening and Definition 2.1, p.262, specifies the inversion
quotient with origin cusp; Definition 2.5(i), p.265, specifies the
local graph and compatible-splitting conditions. The component-label
construction preceding Corollary 2.9, pp.268–269, reduces modulo level
and sign. No orbit-bijection theorem is used to choose a new generator.
Use the odd-level correction in IUT I Remark 3.1.6 already recorded
in the source notes. The native surjection is an input from the
specified field/place setup, not a derived moduli-field theorem.

### A full section with its prescribed member

For each v in V(F_mod), rho^(-1)({v}) is nonempty by surjectivity.
For v different from v_*, choose a member t_v of this fiber, using
ordinary set-theoretic choice. Define s(v)=t_v at those places and
s(v_*)=w. For every v, rho(s(v))=v; hence s is a section on the
entire place set, including archimedean places, and is injective.
Indeed s(v)=s(v') implies v=rho(s(v))=rho(s(v'))=v'.
Thus its selected subset s(V(F_mod)) contains precisely one member
above v_*, namely w. In particular s({v_*})={w}, even if several
other K_glob-places restrict to v_*.

Restriction of the finite place w above 3 has residue characteristic
three. Explicitly its valuation is nontrivial on Q, with positive
value on 3; the restricted valuation in the native field/place setup
has the same rational residue characteristic. No identification of
v_* with a named Q-place is needed. Selecting {v_*} is nonempty and
satisfies the odd-residue-characteristic test. This says nothing by
itself about all other clauses of Definition 3.1(b)–(c).

If decomposition-group representatives require algebraic-closure
lifts, choose a lift of each selected place as permitted by the same
native convention, retaining the original lift at w. Changing a lift
conjugates a decomposition subgroup, so does not impose a second
local condition or change the retained cover at w. No compatibility
between distinct fibers is a requirement of this place section.

### Local type of the unchanged global cover

L053 supplies the one fixed global cover Y -> X, geometrically
connected of degree seven, with constant deck group V, trivial
original-cusp decomposition image, and the cartesian inversion-stack
square. Base change at the selected bad member gives exactly Y_N -> X_N;
we do not replace K_glob by N as a global field.
L057 identifies this arithmetic cover with the actual mod-seven
native graph quotient: mu=c (mod 7) beta_hat. L058 supplies the
independent compatible local splitting and its additional local theta
cover, with odd p=3,l=7 and the same N=double-dot N. Therefore the
covered local-type predicates hold at w. Since the selected bad
subset in the section is {w}, there is no remaining second-place test
for these predicates. This is an application of those results;
there is no new graph comparison or splitting proof here.
The additional theta cover used here is local data from L058;
no globally prescribed theta cover or global cusp splitting is asserted.

### The actual quotient cusp and its sign label

On the compactified puncture set of Y, inversion sends T to -T
and fixes the origin. Since Q has order seven, Q is nonzero and
Q=-Q would imply 2Q=0, which is impossible. Thus its inversion orbit
is exactly the two distinct K_glob-rational points {Q,-Q}.
Neither member is 0_B, so its quotient cusp differs from the origin.

Near this pair, the quotient has no stabilizer. More explicitly,
the two cusp germs over K_glob have disjoint formal completions,
and inversion interchanges them by an isomorphism. The quotient
of their disjoint union is isomorphic to either germ: its objects
are a torsor of the two choices together with the equivariant germ
map, and taking its quotient identifies the two branches without
an automorphism fixing one. Equivalently, invariants in the product
of the two completed local rings are pairs (a,iota(a)), which form
one completed local ring. The free pair of rational points is the
trivial two-element torsor over Spec K_glob, so its quotient is a
K_glob-rational point with trivial inertia. Thus it is a scheme cusp
of the native inversion quotient. Any convention replacing the
stacky origin boundary by a scheme cusp affects the origin only,
not this disjoint free orbit. Interior stack stabilizers are retained;
no coarse ramified quotient is substituted for the covering square.

Over N the same Q and -Q are the actual marking sections. For a in
Z/7Z, the native translation sends the origin marking to c(a).
L059 proves c(1)=epsilon Q for epsilon=1 or -1 in Z/7Z. Hence
Q=c(epsilon) and -Q=c(-epsilon). Their component labels are
respectively epsilon and -epsilon. This conclusion uses the actual
marked deck map, rather than an arbitrary isomorphism of cyclic groups.
Inversion sends the origin to itself and conjugates translation by T
to translation by -T, since -(x+T)=-x-T. It therefore identifies
these two labels precisely by sign. The image cusp of {Q,-Q} has
label {1,-1}, as required. The full section construction changes
neither c nor Q and never multiplies a generator by another unit.

Together these checks prove the limited conditional (e)–(f)
application claimed. Identification of F_mod, the all-F-place
normalized q-order, other initial-data conditions and the numerical
comparison remain independent unresolved obligations. In particular
no statement about the permitted numerical output or its hull follows.

### Separate critical audit — 2026-10-14

The unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-14-native-parametric-section-critical-audit.md`
approves exactly this audit. The section, local type and actual sign
checks pass; no extra selected place or globally prescribed theta
splitting is required by the cited (e)-(f) predicates. This verdict
is conditional on the native field inclusion/place surjection and
all retained lemma hypotheses. It does not verify the other initial
data. The designation of a bad singleton in the conclusion has been
clarified accordingly.

**Section and quantifiers.** A right inverse of rho is automatically
injective. Consequently

    s(V(F_mod)) intersect rho^(-1)({v_*}) = {w}.

This is the source's selected bad set, not the full fiber of rho.
The construction uses choice on all remaining fibers, including
archimedean ones, without altering the fixed embedding at w. Since
the native inclusion is over Q, restriction sends a place above 3
to a finite place above 3. Nothing here computes F_mod. Neither
this equality nor the choice of lifts proves multiplicativity or
q-order coprimality at every F-place over v_*; those are separate
conditions in (b)-(c).

**Actual local application.** The completed cover is L053's psi_N
with its origin 0_B. L057's arithmetic, not just geometric, kernel
comparison gives the native graph factorization. L058 applies its
compatible splitting to that same cover and origin over N, with
odd residue characteristic 3, odd level 7 and N=double-dot N.
These are precisely Definition 2.5(i)'s local requirements. The
quotient by origin-based inversion is the retained stack quotient.
No Galois property is assigned to the bottom quotient cover;
EtTh Remark 2.1.1 explicitly distinguishes it from the top cover.

**Algebraic neighborhood of the actual cusp.** To make clear that
completed-ring invariants alone are not being used as an algebraization
theorem, one can exhibit the free quotient algebraically. Apply the
standard Weierstrass normal-form theorem to the elliptic curve B over
k_0=K_glob, a characteristic-zero field. Write its complement of the
origin as y^2=g(x), with g a squarefree cubic and inversion
(x,y) -> (x,-y). These are coordinates on the same B, and do not
replace Q or prescribe a Tate/graph coordinate. Since Q has order
seven, it is neither the origin nor a two-torsion point. Thus y(Q)
is nonzero, and g(x(Q)) is nonzero.

Put A=k_0[x,1/g(x)] and D=A[y]/(y^2-g(x)). The open
W=Spec D of B contains Q and -Q. D is finite free of rank two
over A; both y and 2 are units, so it is etale. In D[t] the two
factors t-y and t+y of t^2-g(x) are comaximal. The Chinese
remainder isomorphism therefore gives

    D tensor_A D = D[t]/(t^2-g(x)) = D times D.

The two factors are exactly the identity and inversion graphs.
Consequently W -> Spec A is a torsor for the constant group {±1}.
The quotient-stack torsor description (Stacks Project Proposition
95.15.3, tag [04UV](https://stacks.math.columbia.edu/tag/04UV),
already imported in L053) identifies [W/{±1}] with Spec A:
a torsor equipped with an equivariant map to W is its pullback
along a unique map to Spec A, and has no extra automorphisms.
Thus the native quotient has an actual scheme neighborhood of this
boundary point. Its coordinate x(Q) belongs to k_0, and its entire
fiber is exactly {Q,-Q}; the residue field is k_0. Deleting the
puncture orbit gives the corresponding cusp in the punctured
quotient. Any other punctures in this neighborhood can be removed
without affecting this point. This proves the rational scheme-cusp
claim without replacing the full stack quotient by its coarse space.
The coordinate calculation is only the elementary free-pair check
approved for this audit, not a reproof of the native constructions.

**Retained sign and verdict.** L059's c(1)=epsilon Q, with
epsilon in {1,-1}, implies Q=c(epsilon), since epsilon^2=1.
Inversion fixes the origin and conjugates each translation to its
negative, so the quotient pair has the unordered labels {1,-1}.
This is the component-label construction before EtTh Corollary 2.9;
its orbit-bijection theorem is not invoked to choose or change a
generator. Neither the section nor the auxiliary affine coordinates
alter the actual c or Q. Base change retains the rational free pair,
so no additional cusp descent is needed at another selected place.

The audit validates the conditional input and supplies its explicit
algebraic neighborhood justification. It finds no counterexample and
makes no claim of progress beyond known methods. Original finite
B>=A, actual input/action/pilot/essentiality, explicit F_mod and
all-F-place q-order remain unresolved. No DAG input is added: the
four existing direct inputs retain all the actual maps used here.

## Mathlib

Full matching Mathlib coverage for the native place selection combined
with the IUT/EtTh quotient-cusp predicate has not been checked. Ordinary
choice and free finite-group quotients are supporting general
constructions; no presence or absence of the full matching theorem
is inferred. The native predicates are imported by the precise
citations above, and the local maps and labels by the retained results.
