# L065 — The retained paired span is residually irreducible

## Hypotheses

Retain exactly L063's field N=Q_3(zeta_420,3^(1/7)), of degree
168, e=14 and f=12, its admitted full Kondo presentation, single
reciprocity choice and reference lifts, and L064's actual logarithms
y_j=log(u_j). Retain the unchanged L042/L045/L048 field and curve
data and their qualifications. Put R=Z_3, J=log(O_N^times), and

    E=W_J=sum_(j=3)^168 R y_j,
    e_i=y_(2i+1), f_i=y_(2i+2), 1<=i<=83.

By L064 these 166 vectors are an R-basis of the saturated direct
summand E of J; J/E is free of rank two. All unit torsion is kept
in L063's full pair and removed only by the genuine logarithm quotient.
Let Gamma be precisely the finite-word reference subgroup in L063,
including inverses of the paired and adjacent generators. The separate
x_2 shear and arbitrary unit-exponent twists are not included.
No field coordinates for these vectors or for a complement are assumed.

## Conclusion

Gamma preserves E in both directions and acts irreducibly on E/3E:
the only invariant F_3-subspaces are zero and all of E/3E. This
reduction has dimension 166 with the displayed reduced basis; it
also embeds in J/3J without an additional relation.

This is a REPRODUCTION of the inspected paired extraction/adjacency
method on the retained integral span, not a result claimed beyond the
checked sources. It supplies no whole-kernel irreducibility, stable-
lattice application, field radius, actual native action/input, pilot
transport, sufficient initial data, or original finite B>=A conclusion.
Its separate critical audit of 2026-10-16 validates the statement;
the source-sign qualification and verification are recorded below.

## Proof

**Imported action and reason for the specialization.** Use Kaiji Kondo,
*Anabelian aspects of the outer automorphism groups of the absolute
Galois groups of mixed-characteristic local fields*,
[arXiv:2512.09231v2, 12 December 2025, section 1, Theorem 1.1
and the even-degree proof of Theorem 1.3, printed pp.9–11](https://arxiv.org/html/2512.09231v2#S1).
The paired/adjacent words and fixed-generator clauses apply for odd
p=3 and even d=168>=5, with (d-2)/2=83 pairs and 82 adjacencies.
L063 has already transported these actual automorphisms through one
reciprocity choice to compatible R-linear actions h on J and their
inverses. No reconstruction or presentation theorem is reproved here.
The cited rational theorem does not itself assert residual
irreducibility on this integral submodule. L033's proof and separate
audit are a method precedent on a different rank-106 quotient, not
an input identifying that quotient with E. The following argument
checks the changed module and reduction directly using L063 and L064.

**Compute the action on the actual span.** Denote the paired actions
by u_i,v_i and the adjacent action by w_i. L063's logarithm/reciprocity
compatibility makes the action of a source word the sum of its
generator logarithms with their integer exponents. The paired words
b_i -> b_i a_i and a_i -> a_i b_i^(-1) therefore give

    u_i: f_i -> f_i+e_i,
    v_i: e_i -> e_i-f_i.                              (1)

For 1<=i<=82, the three changed adjacent words have exponent sums

    a_i:     e_i-f_i+e_(i+1)+f_(i+1)-e_(i+1)
             =e_i-f_i+f_(i+1),
    b_i:     e_(i+1)-f_(i+1)-e_(i+1)+f_i
                 +e_(i+1)+f_(i+1)-e_(i+1)=f_i,
    a_(i+1): e_(i+1)-f_(i+1)-e_(i+1)+f_i+e_(i+1)
             =e_(i+1)+f_i-f_(i+1).

Consequently the adjacent action is exactly

    w_i: e_i     -> e_i-f_i+f_(i+1),
         e_(i+1) -> e_(i+1)+f_i-f_(i+1),              (2)

with all other e_j,f_j fixed. In particular f_i is fixed despite
its changed nonabelian word, and f_(i+1) is fixed by the source's
unlisted-generator clause. There is no term in y_0,y_1,y_2 in
any formula. Thus every forward generator sends E into E.

For each h in (1) or (2), put D=h-id on E. For u_i, D sends
f_i to e_i and kills every e_j and other f_j. For v_i it sends
e_i to -f_i and kills all f_j and other e_j. For w_i it sends
the two indicated e vectors to f combinations and kills every
f_j and the other e_j. Thus D^2=0 in each case. The integral
map id-D is a two-sided inverse of id+D on E. Since the actual
action on J is invertible by L063, this inverse is the restriction
of its actual inverse: for x in E, h((id-D)x)=x, so uniqueness
of h^(-1)x in J gives h^(-1)x=(id-D)x in E. Hence h(E)=E,
and every finite word and inverse preserves E.

**The full reduction.** L064 gives a free R-module E with exactly
the 166 specified basis vectors, so E/3E has F_3-basis
bar(e_i),bar(f_i), 1<=i<=83. There are no relations from the
torsion block in the presentation: that issue is already resolved
by L064's actual direct sum after the genuine logarithm quotient.
For completeness, if x in E lies in 3J, write x=3j. Its class
in J/E has 3[j]=0. That quotient is free by L064, so [j]=0
and j is in E. Hence E intersect 3J=3E, proving the asserted
embedding E/3E -> J/3J. Reducing (1) and (2) is therefore the
whole induced action on E/3E, not an action on sampled generators.

**All nonzero invariant subspaces.** Let S be a nonzero
Gamma-invariant F_3-subspace of E/3E. Choose a nonzero vector

    z=sum_(i=1)^83 (A_i bar(e_i)+B_i bar(f_i)) in S.

For each generator h and z in S, h(z)-z belongs to S by
invariance and linearity. If some B_i is nonzero, (1) yields

    (u_i-id)z=B_i bar(e_i) in S.

Dividing by the nonzero element B_i of F_3 gives bar(e_i) in
S; applying v_i-id then gives -bar(f_i) in S. If all B_i
are zero, some A_i is nonzero, and

    (v_i-id)z=-A_i bar(f_i) in S.

Dividing by -A_i gives bar(f_i) in S, and u_i-id applied to
it gives bar(e_i) in S. Thus in every case S contains a full
pair bar(e_i),bar(f_i). This includes mixed coefficient vectors
and vectors supported in any number of pairs.

If an available pair has index i<83, (2) gives

    (w_i-id)bar(e_i)=-bar(f_i)+bar(f_(i+1)) in S.

Adding bar(f_i) gives bar(f_(i+1)); applying u_(i+1)-id gives
bar(e_(i+1)). This propagates one step right. If an available
pair has index i>1, the second formula in (2), with adjacency
index i-1, gives

    (w_(i-1)-id)bar(e_i)=bar(f_(i-1))-bar(f_i) in S.

Adding bar(f_i) gives bar(f_(i-1)); applying u_(i-1)-id gives
bar(e_(i-1)). This propagates one step left. From any extracted
pair, successive right steps reach pair 83 and successive left
steps reach pair 1. Only adjacency indices 1 through 82 are
used; neither w_0 nor w_83 is needed. All 166 basis vectors
therefore belong to S, so S=E/3E.

All extracted coefficients are nonzero elements of F_3, and every
propagation coefficient is 1 or -1. No division by 3 or assumption
of characteristic at least 5 occurs. Neither a larger symplectic
image nor Kondo's additional x_2 shear enters the proof.

**Scope.** Both continuation tests pass for this exact span: it is
preserved with inverses, and there is no nonzero proper invariant
residual subspace. This is a local subgroup input only. In particular
ATTEMPTS/020's coordinate obstruction and ATTEMPTS/024's different
whole-kernel fixed-line obstruction are unchanged. A later stable-
lattice or numerical test requires its own assessed hypotheses and
cannot infer actual native permitted-action or input membership
from this result. Independent initial-data, marked pilot transport,
essentiality and original finite B>=A remain unresolved. This is
neither a complete candidate nor a counterexample to IUT.

**Independent critical audit (2026-10-16).** The statement passes
without changing its hypotheses, argument or direct inputs L063,L064.
The versioned primary display cited above was checked against all
five changed words and the unchanged-generator clauses. In an adjacent
four-vector block ordered as (e_i,f_i,e_(i+1),f_(i+1)), the columns
of w_i-id are respectively

    (0,-1,0,1), 0, (0,1,0,-1), 0.

In particular its value on a general vector in this block is
(A_(i+1)-A_i)(f_i-f_(i+1)). The changed b_i word has exponent
sum f_i, while b_(i+1) is explicitly among the fixed b generators.
There is no complement contribution. The two paired differences
and this adjacent difference have image in their respective kernels;
their square-zero inverse formulas are integral and coincide with
the actual inverses on J by uniqueness. This verifies restrictions
in both directions, without assuming that an injective integral
endomorphism is surjective.

The use of L064 is exactly its actual free summand after removing
genuine unit torsion. The equation 3[j]=0 in the free quotient J/E
forces j in E, so the reduction is all of E/3E with no hidden
relation from J. The audit separately checks both coefficient cases:
a nonzero B_i isolates e_i regardless of all other coefficients;
if every B_i vanishes, a nonzero A_i isolates f_i. The other paired
generator then supplies the missing vector. Propagation acts on
that isolated e vector, not on the original z, so possible equality
of adjacent A coefficients cannot cancel the required step. Repeated
right and left steps cover every pair, including starting at either
endpoint; only w_1,...,w_82 occur. All inversions of coefficients
are in F_3^times. No characteristic-at-least-five theorem is used.

There is a source-sign qualification in Kondo's proof of Theorem 1.3,
even-degree case (d), the display immediately before its final
application of (a) (versioned HTML line 426). Written in our symbols,
that display asserts f_i=-w_i(e_(i+1))+e_(i+1)+f_(i+1).
The displayed generator word instead gives its right side as
-f_i+2f_(i+1). The correct identity is

    f_i=w_i(e_(i+1))-e_(i+1)+f_(i+1).

This is precisely the identity already used in L065's leftward
propagation. Since the isolated e_(i+1), f_(i+1) and its image
belong to the invariant subspace, the corrected identity still
proves the source's desired membership. Thus the audit does not
import that erroneous displayed equality, and it finds no failure
of the source automorphism input or of L065. This local sign issue
is neither an essential IUT flaw nor a reason to withdraw the
intermediate subgroup conclusion.

The audit is a REPRODUCTION check of existing local mathematics,
not a new irreducibility theorem or an advance beyond checked
sources. No stable-lattice, container, numerical or native-action
conclusion has been added. The proof requires no numerical script.

## Mathlib

Full matching coverage for the retained presentation-defined span and
its residual reference action: **not checked**. Supporting results for
free-module reduction, square-zero inverses and invariant subspaces:
**not checked**. Unknown coverage is not evidence of absence; no
formal verification is claimed. The primary construction is imported,
and the complete elementary specialization above is the local proof.
