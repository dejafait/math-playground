# L096 — Remaining-prime normal-closure completions are tame

## Hypotheses

Retain an arbitrary L089 survivor E/Q with all the hypotheses and
embedded fields of audited L090. In particular, in its fixed closure,

    T=Q(E[2])=Q(t_o),
    E_o: V^2=X(X-1)(X-t_o),
    G_o=T(iota,E_o[15]), iota^2=-1,
    C_o=G_o^nor subset M=Q(E[60]).

Every torsion field contains both coordinates of every geometric
torsion point. Fix any of the six orderings o and any actual finite
places w|v|p of C_o/T/Q with p outside {2,3,5}. All local embeddings
are induced from w in one algebraic closure of Q_p. Use the absolute
valuation v_p(p)=1, also on its finite extensions. No initial theta-data
or choice of selected conductor support is assumed.

## Conclusion

The actual extension (C_o)_w/T_v is tamely ramified. If
v_p(j(E))>=0, this extension is unramified. These assertions hold
uniformly for every survivor, ordering and extending place specified
above. They impose no assertion that T_v/Q_p is unramified or tame.

This is a specialization of the previously assessed reduction,
torsion and compositum theorems. It supplies only a local input for
the pre-ell estimate; native selected support, weighted assembly and
a complete field repair remain unresolved. The separate step384
critical audit below validates this application with those limitations.

## Proof

### Imports and applicability

The invocation-start assessment is
`drafts/literature/2026-10-20-normal-closure-remaining-prime-ramification.md`,
with decision SPECIALIZE. Import the following results without
reproving their general statements:

- Mochizuki, *IUT IV*, April 2020
  [87-page reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.8(vi),(vii), statement p.19 and relevant proof
  pp.20-21: an actual Legendre model over an odd-residue complete
  discretely valued field becomes semistable over an extension of
  degree at most two; in the potentially-good case it is good over
  the original field. For invertible level n, good reduction makes
  the full torsion representation unramified; bad multiplicative
  reduction makes its full torsion field tame, with ramification
  index dividing n. Split multiplicative reduction is unnecessary.
  The Legendre-specific proof cites Silverman VII.5.4(c); the torsion
  proof cites *Neron Models*, section 7.4, Theorems 5 and 6.
- Silverman, *The Arithmetic of Elliptic Curves*, second edition
  (2009), [VII.5.5, pp.197-199](https://studylib.net/doc/28155304/the-arithmetic-of-elliptic-curves):
  integral j is equivalent to potential good reduction over a
  complete discretely valued field with perfect residue field.
  The inspected general statement recorded in the local-two-degree
  assessment is reused, not a dyadic-only assertion.
- Conrad, [*Math 248A. Tame ramification and composite fields*](https://math.stanford.edu/~conrad/154Page/handouts/tamecomp.pdf),
  Theorem 2.1 and the tower observation immediately following it,
  p.2: finite tame extensions have tame compositum, and tameness
  is equivalent to tameness of both steps of a finite tower.
- Milne, [*Algebraic Number Theory*, v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  Theorem 7.50 and Corollaries 7.51-7.52, pp.127-129: finite
  unramified extensions form subfields of the maximal unramified
  extension; prime-to-p roots of unity belong to that extension.
  The completion construction preceding Proposition 8.1 and
  Proposition 8.2, pp.135-136, identifies completions using the
  chosen embeddings and generators. Propositions 8.10/8.13,
  pp.139/141, retain the actual places in Galois towers.

Every local field here is a finite extension of Q_p; characteristic
zero, completeness, discrete valuation and perfect finite residue
field satisfy these hypotheses. Because p is outside {2,3,5}, both
2 and 15 are units. L090 gives j(E) rational with 0<j(E)<1728,
so the geometric pointed automorphisms are precisely {+1,-1}.
Every E_o is an actual nonsingular Legendre equation with all its
two-torsion rational over T, hence over T_v. Its geometric j is
j(E), as proved by L090's pointed geometric isomorphism. Thus the
model, moduli and trivial two-torsion hypotheses of IV 1.8(vi),
including G_E=G_k in its notation, hold over each local base used
below. Potential good reduction is applied to the literal Legendre
model, not to an arbitrary quadratic twist.

### The actual completed compositum

Fix E,o,w,v,p as in the hypotheses and put K=T_v. Embed C_o into
Qbar_p compatibly with w, then take all completions inside this same
algebraic closure. L090 proves that every Q-conjugate of G_o is
one of the embedded fields G_a belonging to the six root orderings,
and that every such ordering occurs as a conjugate. The normal
closure C_o is their finite compositum. This uses the actual normal
ambient M and full coordinate fields; it does not assume normality
of G_o. Each G_a contains the same global T, since T/Q is a
splitting field and L090 identifies Q(t_a)=T for every a.

Let u_a be the restriction of w to G_a and let F_a be the embedded
completion (G_a)_(u_a). The completion construction just cited gives

    F_a=K(iota,E_a[15]).

Here each algebraic torsion point is transported by the fixed
embedding; characteristic-zero base change retains the complete
geometric 15-torsion set. In particular, these are full torsion
fields, not fields of a chosen point or of x-coordinates alone.

Inside (C_o)_w, the field F generated by the finitely many F_a
is finite over K and therefore complete and closed. It contains
the embedded G_a, hence their compositum C_o. The latter is dense
in (C_o)_w, so closedness gives F=(C_o)_w. Conversely each F_a
lies in (C_o)_w by continuity of the completion inclusion. This
verifies the completed compositum in both directions for this w;
no interchange of completion and normal closure is asserted.

### Tameness for every factor and the whole completion

For each ordering a, IV 1.8(vi) supplies an embedded extension
L_a/K of degree at most two over which the unchanged E_a is
semistable. Since p>=7, its ramification index divides a degree
prime to p, and its finite residue extension is separable.
Consequently L_a/K is tame, including the identity-extension case.

Put R_a=L_a(E_a[15]). Over L_a the curve has either good or bad
multiplicative reduction. In the first case IV 1.8(vii) makes
R_a/L_a unramified; in the second it makes R_a/L_a tame. The
theorem concerns the kernel on all E_a[15], which is exactly this
full coordinate field. The level is invertible in O_(L_a) in both
cases. The tame tower observation gives R_a/K tame. Its subfield
K(E_a[15]) is therefore tame over K as well.

The element iota has exact order four, and 4 is prime to p.
Milne 7.51-7.52 puts K(iota) in K's maximal unramified extension.
Conrad's compositum theorem now makes
F_a=K(iota,E_a[15]) tame over K. Applying the same theorem to
the finite collection of F_a and using the completed-compositum
identity proves (C_o)_w/K tame. Neither the possibly different
quadratic extensions L_a nor an equality of their ramification
indices was required.

### The integral-j case

Suppose v_p(j(E))>=0. This same rational j is the invariant of
every E_a, under the fixed embedding into K. Silverman VII.5.5
gives potential good reduction for every E_a/K. The
Legendre-specific good-reduction clause of IV 1.8(vi), with its
explicit proof case on p.21, then gives good reduction already
over K. IV 1.8(vii) makes every K(E_a[15])/K unramified.

We already know K(iota)/K is unramified. Milne 7.52 therefore
puts every F_a, and their finite compositum, inside the same
maximal unramified extension of K. By the identity above that
compositum is (C_o)_w. Thus (C_o)_w/T_v is unramified, as claimed.
The arbitrary choice of w and the shared rational j establish the
assertion for every actual place, not just one selected completion.

### Qualifications and boundary of the result

The specified continuation test passes: all actual conjugates and
their completion compositum have been identified, and both reduction
cases satisfy the imported hypotheses. The source-version
qualification remains April 2020 reproduction; authentication against
current author/journal bytes is unresolved and ATTEMPTS/035 is not
reopened. No native initial-data assertion is used as a premise.

This result identifies no native selected conductor support and
performs no normalized weighted sum or different calculation. It
does not repair the factor-four relative degree excess, establish
the exact generation prescription after normal closure, choose a
height-selected prime, or supply independent initial data, native
input/action/factorization/pilot or essentiality. Original finite
B>=A remains open. This is local progress by known methods, with
no claim of progress beyond the inspected sources or a complete
solution candidate.

### Separate critical audit — 2026-10-21, step384

The unchanged approved target passes. No conclusion, hypothesis or
direct mathematical dependency is changed; the direct input remains
audited L090, with L089 inherited. This audit checks the application
of known results, not a new general ramification theorem.

**All conjugates and actual completions.** L090's full conjugation
argument applies to every ambient automorphism, not merely those
fixing the cyclotomic field: applying sigma and its inverse to the
complete coordinate sets proves sigma(G_o)=G_(sigma o). Extension
of embeddings through the normal M exhausts every Q-conjugate;
the full mod-two image realizes every root ordering. Each field
contains the very same T. Consequently restricting the chosen w
gives embeddings over one K=T_v, even though the restricted places
on the different G_a need not have any further identification.

For each a, K(iota,E_a[15]) is finite and complete, contains G_a,
and lies in its embedded completion. Density of G_a gives equality
with that completion. Conversely its generators belong to that
completion, including K as the closure of T. The finite compositum
F of these fields inside (C_o)_w is closed and contains C_o, hence
contains its closure (C_o)_w. The reverse inclusion follows from
the individual completed embeddings. This verifies both field
identifications without a normal-closure/completion interchange.
Milne's cited completion construction and Proposition 8.2 retain
the chosen place, not just an abstract isomorphism type.

**Reduction hypotheses and both cases.** Rechecked IV 1.8(ii),(iii),
(vi),(vii), p.19, and the proof of (vi),(vii), pp.20-21, at the
linked April reproduction. For every a, the actual K-equation
provides descent, hence G_E=G_K; nonexceptional j gives the stated
automorphism group; (0,0),(1,0),(t_a,0) give trivial two-torsion
action. The distinct roots ensure nonsingularity. The local fields
are perfect and complete with finite residue fields, and 2,15 are
units. The proof of (vi) explicitly treats a given Legendre equation,
so no different twist or newly chosen descent is substituted.

The potentially delicate good-reduction clause is also supported by
the already assessed Silverman VII.5.4(c) and VII.5.5 proofs,
pp.198-199, rechecked at the linked second-edition reproduction.
Their Legendre cases give good reduction when the parameter and its
complement are units, multiplicative reduction when an integral
parameter reduces to 0 or 1, and multiplicative reduction after at
most a quadratic extension in the nonintegral case. The integral-j
proof places the literal parameter in the first case over K itself.
Its preliminary extension to obtain Legendre form is unnecessary
here. OCR in that reproduction drops negation signs; the mutually
exclusive cases and displayed discriminant must be read together.
No arbitrary potentially-good twist is being assigned good reduction.

**Towers and composita.** The quadratic semistable extension has
ramification index prime to p>=7 and separable residue extension.
The full-coordinate field is precisely the fixed field of the
torsion representation's kernel, so IV (vii) applies at n=15.
Conrad Theorem 2.1 and its following tower observation, p.2,
validate both the tower and subfield steps and the finite compositum.
Milne 7.51-7.52 place the actual fourth root of unity and, in the
good case, every torsion field in one maximal unramified extension.
There is no claim that a compositum has the same ramification index
as a factor, or that the quadratic auxiliary fields agree.

The bounded test therefore validates both conclusions at every
actual place. Source authentication, selected support, weighted
assembly and the other qualifications above remain unresolved.
No mathematical script or numerical evidence is used. This audit
supersedes the pending-audit wording in the unchanged PROOF overview;
the argument and DAG have not changed.

## Mathlib

Full matching and supporting coverage are unchecked. The proof uses
the precisely cited informal theorems above; unknown Mathlib coverage
is not evidence of absence.
