# L141 — A complete 11-adic image removes one further dimension

## Hypotheses

Use L138's actual smooth proper genus-two curve B, monic squarefree model
Y²=G(X), and product algebra Q[X]/G=Q×K with

    G=(X−r)H, r=9075,
    H=X⁴−67760X³+1581228000X²−15306287040000X+52615361700000000,
    K=Q(alpha), g(alpha)=0,
    g(U)=U⁴+64U³+150U²−32500U−109375,
    eta=−907500/(alpha−50), X -> (r,eta).

Use L137's prime P_1=(11,alpha+5) in the actual maximal order and its
complete support above 2,3,5,11. Let J=Jac(B) and use L139's supported
product norm kernel V with

    c=dim_F2 Cl(O_K[1/330])/2Cl(O_K[1/330])<=2,
    dim V=11+c, dim J(Q)[2]=1.

Use audited L140's real image W, its surjective real quotient restriction
on V and its exactly 39 saved supported global classes. There is no scalar
quotient in this odd-degree Jacobian map. Class groups are ordinary.
No unit basis, full Selmer computation, rank lower bound, GRH or assumption
on Sha is used.

## Conclusion

Put u=alpha+5. The algebra at 11 is Q_11×F, where
F=Q_11(u) has degree four, uniformizer u, residue field F_11 and
v_F(11)=4. In the coordinate order

    (v_11(q) mod 2, nonsquare residue of q/11^v_11(q),
     v_F(b) mod 2, nonsquare residue of b/u^v_F(b)),

the **complete** image delta_11(J(Q_11)/2J(Q_11)) is

    span_F2{(1,0,1,0)}.

The saved class (1/16,2) belongs to V, has real signature in W, and has
11-adic vector (0,0,0,1), outside that image. The 11-adic condition
therefore removes exactly one dimension from L140's real-filtered V.
The simultaneous ambient dimension and resulting rank bound are

    dim {v in V: s(v) in W, res_11(v) in im(delta_11)}=8+c,
    rank J(Q)<=7+c<=9.

The complete fixed-span calculation on all 39 saved witnesses has a
37-dimensional coefficient kernel for the real condition and local
quotient rank one on it. This asserts no independence of those 39 global
square classes. The upper bound nine misses the sufficient bound one by
eight and gives no point determination, marked lift, degree-nine/integer
recovery or Beal exclusion. This specializes known descent theory; no
originality beyond inspected sources is claimed. Arithmetic replay passes;
the separate critical proof audit below accepts this limited statement
without a mathematical correction or a stronger bound.

## Proof

### Imported results and exact scope

Import Michael Stoll, *Implementing 2-descent for Jacobians of
hyperelliptic curves*, Acta Arith. **98** (2001), 245–277,
DOI 10.4064/aa98-3-4,
[Lemmas 4.1, 4.3(2)–(3), 4.4(1)–(2), pp.250–251](https://www.impan.pl/shop/en/publication/transaction/download/product/83397).
For a monic integral squarefree odd model the Kummer map is a natural
injection into the product norm kernel. A rational branch at r has value
(H(r),r−eta). At an odd local prime with m irreducible factors the
Jacobian image has dimension m−1 and the full norm kernel dimension
2(m−1). These statements include bad odd primes. Infinity has value one
(Section 6, pp.267–268). No general image theorem is reproved here.

Import the Eisenstein DVR statement from Pete L. Clark,
*Algebraic Number Theory II: Valuations, Local Fields and Adeles*,
[161-page author-hosted version, Proposition 2.9/Corollary 2.10, p.65](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf)
(accessed 2026-10-26, revision date unidentified). A root of a monic
Eisenstein polynomial over Z_11 is a uniformizer of the degree-four
extension; its integer ring is Z_11[u] and residue field F_11. Use the
odd-residue Hensel square criterion: an element is a square precisely
when its normalized valuation is even and its unit residue is a square.
Clark Proposition 2.20, p.72 and Theorem 2.24/proof, p.73 supply the
valuation/unit and Hensel inputs; Exercise 2.11 is not treated as a proved
theorem. These are the primary inputs inspected in the prior SPECIALIZE
assessment `drafts/literature/2026-10-26-pair-eleven-adic-filter.md`.
The instance arithmetic below is needed because these sources do not
evaluate this curve's branch class or saved global classes.

### The local field and the full factorization

Exact coefficient substitution gives

    g(U−5)=U⁴+44U³−660U²−29700U+49500.                 (1)

All four nonleading coefficients are divisible by 11 and
49500=11*4500 is not divisible by 121. Thus (1) is Eisenstein at 11.
It is irreducible over Q_11, so F has degree four, integer ring Z_11[u],
residue field F_11 and v_F(11)=4. Its residue alpha=−5 identifies the
prime with L137's P_1. The coefficient test, rather than the repeated
mod-11 factor alone, proves irreducibility.

L138's exact maps remain valid over Q_11. Here alpha−50=u−55 is
nonzero, and eta is nonzero with inverse alpha=50−907500/eta. Consequently
Q_11(eta)=F. The verified identity H(eta)=0 therefore makes H irreducible
of degree four over Q_11. Also

    H(r)=73990352390625=3⁵*5⁶*11⁷ != 0.               (2)

The coefficient identity G=(X−r)H now gives all irreducible local factors,
with m=2. L138 supplies monicity, integrality and squarefreeness; extension
of the base field preserves squarefreeness. Stoll's hypotheses hold, and
the complete local image has dimension one. The local norm kernel has
dimension two. No good-reduction assumption is used at 11.

Dividing (1) at u by 11 and reducing modulo u gives

    u⁴/11 ≡ −4500 ≡ 10 (mod u),
    rho:=11/u⁴ ≡ 10 (mod u).                         (3)

Both residues are nonzero and inverse to one another.

### One actual branch generator reaches the completeness dimension

The divisor D=[(r,0)−infinity] is rational. Stoll's branch-factor formula
with factors X−r and H evaluates to (H(r),r−eta). Its norm is H(r)²,
so its square class lies in the norm kernel. In the rational factor (2)
gives valuation seven and unit residue

    H(r)/11⁷=3796875 ≡ 5 (mod 11).

For the quartic factor use the exact identity

    r−eta=9075*(u+45)/(u−55), 9075=75*11².            (4)

Here v_F(9075)=8, v_F(u+45)=0 and v_F(u−55)=1.
Thus v_F(r−eta)=7. Dividing (4) by u⁷ and applying (3) gives residue

    75*rho²*(u+45)*u/(u−55) ≡ 75*10²*1*1 ≡ 9.

The nonzero squares in F_11 are exactly {1,3,4,5,9}. Both unit residues
5 and 9 are squares, and both valuations are odd. The branch image is
therefore (1,0,1,0), which is nonzero. Its span attains the theorem's
one-dimensional image. This proves **completeness**, including every
divisor class and infinity, without enumerating curve points or assuming
that rational two-torsion remains nonzero modulo twice the local group.

### A real-compatible supported class outside the complete image

The class b=2 is one of L140's five explicitly appended rational
witnesses. Since [K:Q]=4, its signed norm is 16, and L139's supported
norm-kernel identification gives v=([1/16],[2]). Every valuation outside
the primes above 2 is zero, so v belongs to V. All five real coordinates
are positive; its sign vector is zero, hence in W.

At 11 the rational coordinate has valuation zero and residue
1/16 ≡ 9, a square. The quartic coordinate is a unit of residue 2, a
nonsquare. Its local vector is (0,0,0,1), outside {0,(1,0,1,0)}.
This is an actual product-coordinate class, retaining its signed inverse
norm. It is not a scalar-quotient computation or a sampled local absence.

Let V_R=s^−1(W). L140 proves dim V_R=9+c. Naturality gives a linear map

    V_R -> H_11 / delta_11(J(Q_11)),

where H_11 is the full local product norm kernel. Its codomain has
dimension 2−1=1. The class v just exhibited maps nontrivially, so this
map has rank exactly one. Rank-nullity gives simultaneous dimension 8+c.
The rational Jacobian Kummer image lies in this kernel by naturality at
both places and L138's support containment. Its global injection and
L139's dim J(Q)[2]=1 give rank J(Q)+1<=8+c, as claimed. No equality with
a Selmer group or finiteness of Sha is inferred.

### Complete fixed-domain arithmetic and independent replay

Producer: `python3 scripts/pair-genus-two/eleven_adic_filter.py`.
Replay: `python3 scripts/pair-genus-two/verify_eleven_adic_filter.py`.
The full producer certificate is
`scripts/pair-genus-two/eleven-adic-filter-certificate.json`;
the full replay is
`scripts/pair-genus-two/eleven-adic-filter-verification.json`.
Both are exact integer/Fraction computations. The replay imports no
producer implementation and passes 12335 checks, with no failures.

Bindings check all accepted L140 source hashes, including its real audit,
the actual model, basis, prime records and unchanged source certificates.
All 39 complete saved witness records are consumed. Each signed norm is
recomputed, as are its inverse-norm coordinate and local square class.
No upstream box, unit search, backend or point detector is rerun.

For an exact element a=sum_i c_i u^i the producer obtains

    v_F(a)=min_{c_i!=0}(4v_11(c_i)+i).

The nonzero terms have distinct valuations modulo four, so the minimum
is unique and no cancellation is possible. If it occurs at i and
k=v_11(c_i), the normalized residue is
(c_i/11^k)*rho^k modulo 11. The producer also constructs the exact field
element a/u^v_F(a), verifies integral coefficients and checks its nonzero
constant residue. Rational coordinates retain both valuation and unit bits.

The replay instead substitutes by polynomial Horner steps, scales to
integral u coefficients and repeatedly divides by u until the constant
residue is nonzero. Each quotient's integrality is checked. It also
reconstructs the complete normalized field vector. Norms use alpha
companion-Horner multiplication and Gaussian determinants, instead of
the producer's u-basis convolution and permutation determinants. Thus
both normalized residues, not merely valuation parities, are checked
independently for the branch and every saved witness and product.

In L140's real-root order the quotient is
phi(s)=(s_0,s_1+s_2). Its 39 columns have rank two and a 37-dimensional
coefficient kernel. The full elimination trace and kernel basis are saved.
Replay verifies every coefficient identity and independently checks rank,
kernel independence and completeness with low-bit pivots. Every one of
the 37 kernel combinations is reconstructed as an actual product in K,
including its signed norm, inverse rational coordinate, real signs,
normalized local coordinates and multiplicativity. Their local quotient
has rank one. The coefficient vector for rational-2 alone is
34359738368=2^35; its recomputed product is precisely (1/16,2).
These coefficient ranks do not assert global independence or saturation.

Actual/cap values: four field coordinates/four, 39 global columns/39,
one branch/one, 37 coefficient-kernel vectors/39, matrices at most
39 by 39/39 by 39; maximum absolute normalized valuation 7/128 in both
executions. Producer field operations are 491/100000, replay 947/100000;
maximum observed rational numerator/denominator bits are 70/4096 and
69/4096 respectively. No cap was exceeded. A field operation here counts
each explicit vector addition, scaling, multiplication or division helper
call (nested helpers count separately); determinants, rational arithmetic,
serialization and binary elimination are not charged as field operations.
Rational intermediates in those computations have separate bit checks.
This metric is not a scalar-operation, bit-complexity or runtime guarantee.
Both implementations share Python exact arithmetic; they are not formal
verification and do not themselves constitute the separate audit below.

The branch gate succeeds and the fixed-span target is met. The real and
11-adic quotient losses are now both fully detected, so further witnesses
cannot improve these same two ambient restrictions. Other finite places,
full descent, points and all recovery/signature obligations remain open.
Prior ATTEMPTS/045,050,052,059–061 and unfinished L108 remain untouched.

### Separate critical mathematical audit — 2026-10-26

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-26-pair-eleven-adic-audit.md`. This audit accepts
the complete local image, the additional codimension one and the bound
7+c<=9, with no mathematical correction or new dependency. It is a
REPRODUCTION audit of known-theorem specialization, not a stronger rank
bound or a Beal candidate. The primary coverage above is reused, including
Stoll's Lemma 4.4 at bad odd primes. No general theorem is reproved.

**Field and theorem hypotheses.** L138's actual G,H,alpha/eta maps and
maximal-order transport agree with the saved inputs. The shift (1) is
monic Eisenstein over the complete DVR Z_11. Its field is a finite
extension of Q_11 and hence complete and Henselian. Clark's DVR result
therefore identifies its full integer ring as Z_11[u], with residue F_11
and uniformizer u; the ramification degree is four. The residue alpha=−5
identifies the same prime P_1 as L137. The denominators alpha−50 and eta
in L138's inverse field maps are nonzero. Thus eta generates this degree-four
local field; the exact H(eta)=0 establishes H's local irreducibility,
not merely its global irreducibility or repeated reduction. The nonzero
H(r) separates the linear factor, so m=2 is the full local factor count.
L138 supplies monicity, integrality and squarefreeness of degree-five G.
These are all the hypotheses needed for the cited local dimensions.

**Branch sign, residue and completeness.** In Stoll's signed factor-divisor
formula the factor X−r has degree one. Its other coordinate is therefore
−(eta−r)=r−eta; changing this sign would change the nonsquare residue at
11. The rational coordinate is H(r), and the odd infinity has value one.
Equation (2) gives the rational valuation seven and residue five.
In (4), u−55 has valuation one because v_F(u)=1 and v_F(55)=4;
u+45 is a unit of residue one. Also u/(u−55) reduces to one, since
55/u has positive valuation three. These facts justify every normalized
factor, giving quartic valuation seven and residue nine. Both residues
are squares, so the full vector is exactly (1,0,1,0). Its nonzero
valuation bits prove nonvanishing in the local quotient directly.
This avoids assuming that a global two-torsion point survives modulo
twice the local Jacobian. The imported exact image dimension is one,
so this actual divisor image spans every local divisor class. There is
no rational-point generation assumption or omitted branch/infinity case.

**Complete arithmetic evidence.** Both implementations were read in full.
Every one of the 39 full source records is bound to the accepted L140
certificate, including its supported ideal data, real signs, basis
coordinates and signed inverse norm. The underlying correctness of
those inputs is the previously audited result, not a consequence of
hash equality. No outside-support parity claim is inferred merely from
a norm. All producer input hashes still match their complete files.

The producer's distinct weighted term valuations are justified by
v_F(c_i u^i)=4v_11(c_i)+i: different i have different residues modulo
four, so the minimum is unique. The leading-term residue formula uses
rho=11/u^4, including negative powers when necessary. The replay's
integral scaling writes a=11^d a_0. Its repeated exact division by u
stops at a unit, so if j divisions are used then v_F(a)=4d+j and the
normalized residue is rho^d times that unit's residue. Every quotient
is integral and the full normalized four-coordinate vector is checked
by a second reconstruction. This verifies full square classes rather
than valuation parity alone. The companion-Horner multiplication and
Gaussian norm determinant are independent of the producer's convolution
and permutation determinant; every signed norm and rational coordinate
is checked, including all 37 reconstructed products.

The real elimination has rank two on 39 coefficient columns. Replay
checks every row addition and original-input combination, and its
independent low-pivot calculation gives 37 independent kernel vectors.
Each is in the kernel and dimension 39−2 proves completeness. Every
coefficient basis vector is rebuilt as an actual product, with all
norms, real signs and local masks verified multiplicatively. The second
elimination has rank one. None of these coefficient ranks is used as
independence or generation of global square classes.

One complete replay again passes all 12335 checks, with no failure.
Its entire output is identical to the preserved
`scripts/pair-genus-two/eleven-adic-filter-preaudit-verification.json`.
The supplement `python3 scripts/pair-genus-two/audit_eleven_adic_filter.py`
passes 47 comparisons and saves its full evidence in
`scripts/pair-genus-two/eleven-adic-filter-audit.json`. It checks all
source bindings and witness/product orders, the printed scalar/residue
values and rational-2 record, all 16 local square-class vectors and
all three c cases. The complete branch and obstruction records were
also inspected directly. No source record or failing product was skipped.

**The actual quotient and rank consequence.** The odd-residue square
criterion identifies F*/F*² with basis [u],[2]: 2 is a nonsquare in F_11.
The exact norms N(u)=49500=11*4500 and N(2)=16 have rational square-class
bits (1,0) and (0,0). Hence in the stated four-coordinate order the
product norm sends (a,b,c,d) to (a+c,b). Its full kernel consists of
masks 0,5,8,13, agreeing with Stoll's dimension two. Restricting the
last bit to this kernel is a linear quotient with kernel {0,5}, exactly
the complete local image. This checks that the certificate's membership
test represents a linear quotient on all possible norm classes, not
just on the tested products.

For rational-2 the actual pair is (1/16,2), supported only over 2 and
positive in every real embedding. It belongs to V_R and has mask 8,
so the map from V_R to that one-dimensional local quotient is onto.
No generation of V_R by the saved witnesses is required. Naturality
puts every rational Jacobian Kummer class in its kernel, with the
support supplied by L138. Thus the exact simultaneous ambient dimension
is (9+c)−1=8+c. Global injectivity and rational two-torsion dimension
one then give rank+1<=8+c. For c=0,1,2 the bounds are respectively
7,8,9, exceeding the sufficient bound one by 6,7,8. There is no Selmer
equality, rank lower bound, assumed unit basis, narrow class replacement
or assumption on Sha.

Producer/replay actual caps remain respectively 491/947 field-helper
operations out of 100000, 70/69 observed rational bits out of 4096,
and maximum absolute valuation 7 out of 128. The full domain is 39
witnesses, one branch and 37 kernel products, with matrices at most
39 by 39. The supplement exhausts 16/16 local square-class vectors
and 3/3 class-dimension cases. Exceptions in either original program
are saved and produce nonzero exit status; no cap was hit. The stated
operation/bit metrics retain their qualifications above and are not
runtime or formal-verification guarantees. Further witnesses at these
same two places cannot improve the saturated ambient restrictions.
Other local conditions, point control, all lifting/recovery obligations
and other exponent signatures remain open. Direct inputs are unchanged.

## Mathlib

Full matching coverage of this local Jacobian Kummer-image theorem,
combined supported rank restriction and exact instance has not been checked
in Mathlib. No absence claim is made. Exact scripts are arithmetic
certificates, not Lean proofs or a substitute for theorem hypotheses.
