# Positive ideal cohomology: restriction test

The saved target and its prior SPECIALIZE assessment are unchanged:
determine whether H^1(X,I_C(rH)) is nonzero in some positive degree for
the original fixed ample L, with H=L external tensor L. Its numerical
class has not been specified. Any conclusion must keep that class as
a parameter; choosing a different polarization is not an answer.

The downstream use is L018's possible failure to recover a line summand
when 0<m<n. Nonzero cohomology would only remove a sufficient recovery
argument. A transverse union lift, higher-order compatibility and
algebraization would remain unresolved. The attained span is still 21,
and the stopped supports allow three of four RM directions.

## Working checkpoint

The ideal sequence and positive ambient vanishing identify the desired
group with the cokernel of H^0(S,L^r) tensor H^0(S,L^r) ->
H^0(C,O_C(rH)). L019 controls the target through the normalization and
all three descent conditions, but does not compute this map. Total
section dimensions alone need not detect its failure.

The rank-four divisor calculation in L019 suggests checking the two
pullbacks of each visible divisor F,O,E,P individually. A common
pullback description would need a proof, including the resolved fibres;
it is not assumed here. On a general complete elliptic fibre the two
projections identify the same elliptic curve. The multiplication map
for the restricted polarization is therefore a possible test of the
actual ambient image. A global cokernel still requires a section on C
whose restriction lies outside that fibrewise image, with all three
normalization gluing conditions retained.

The degree L.F is a parameter. Very high powers of an ample bundle
eventually have zero ideal cohomology in every positive degree by the
already reviewed Serre theorem, so a uniform positive answer for all
ample polarizations cannot be assumed. A degree-dependent result must
be stated as such. No cohomology value or new lifting claim has yet
been established at this checkpoint.

The continuation test is a proved nonzero cokernel for the given
numerical class, or a proved all-positive-degree vanishing statement.
An incomplete calculation must name the uncomputed class range or map.
The existing m>n>0 exclusion and unfinished earlier work are preserved.

## Parameter range with an explicit calculation

The fibre-degree-two range now has a proposed exact answer. The
determinant -7 in L019 is squarefree, so its full-rank divisor lattice
is saturated. An ample L with L.F=2 meets both type-III components
once. Translation by a multiple of P, simultaneously on both factors,
preserves C and transforms L into O+P+bF with b>=3. This transports
the original restriction map by an isomorphism; it does not replace L
by an unrelated polarization. Its square is 4b-4.

On the Laurent chart put z=(y+y_0)/(x-x_0) and
w=2x+x_0-z^2. The degree-two elliptic quotient identifies z as the
invariant coordinate and w as anti-invariant. Their poles are bounded
by O+P+2F and 2O+2P+4F respectively. For rL the candidate complete
basis consists of z^i times polynomials in t of degree at most rb-2i
(0<=i<=r), together with w z^(i-2) times such polynomials (2<=i<=r).
Kodaira vanishing and Riemann--Roch match the count. On W use the same
functions and Laurent coefficients of exponents between
-(2rb-2i) and 2rb-2i, with i running to 2r. The two pullback divisors
agree here because O, P and the two fibres over infinity are preserved.

For positive A,B, products of degree-A polynomials in t=v+a/v and
degree-B polynomials in s=zeta v+a/(zeta v) form a codimension-one
subspace of Laurent polynomials of degree at most A+B. Its single
condition relates the two extreme coefficients by
c_-=a^(A+B) zeta^(-2B) c_+. Adjacent allocations of an exponent i
give distinct such hyperplanes. This calculates the actual two-factor
restriction image, without assuming ordinary normal generation.

For r=1 the image has only the invariant functions, with total
dimension 12b-11. L019 gives h^0(C,H|_C)=16b-19 after all three
gluing conditions, suggesting h^1(I_C(H))=4b-8=L^2-4. For r>=2,
the invariant and mixed invariant/anti-invariant products already
span a subspace of codimension exactly three on W. All are ambient
restrictions and hence descend; the three-condition dimension count
would make them all sections on C. This would give vanishing for
every r>=2 in this parameter range.

Remaining checks are the section poles on both resolved components,
the translation reduction, and the endpoint coefficient ranks. No
answer for L.F>=3 or transverse lifting assertion is included.

## Completion of this parameter range

[L020](../lemmas/L020-fibre-degree-two-positive-ideal-cohomology.md)
completes the checks and proves the proposed formula for every original
ample L with L.F=2. Translation by a section is imported from
[Schuett--Shioda, arXiv:0907.0298v3, section 7.6, pp. 33--34](https://arxiv.org/pdf/0907.0298v3#page=33),
read on 2026-09-27; its compatibility with this C is checked explicitly.
The full-rank determinant -7 proves saturation, and positive intersection
with all negative curves verifies that the numerical range is nonempty.
The pole bounds apply on both resolved components, and section counts
prove that the exhibited systems on S and W are complete. The Laurent
hyperplane calculation treats the actual two projections. Ambient
products automatically descend, and comparison with the three-condition
dimension from L019 proves their exact image, including every degree.

The result is h^1(I_C(H))=L^2-4 and H^1(I_C(rH))=0 for r>=2 in
this range. It is a partial mathematical advance on the saved target,
not a uniform answer for its unspecified original L. The remaining
range is L.F>=3. The cohomological issue in reversed-degree recovery
is now real, but no particular inclusion obstruction or transverse
union lift has been computed. The new function-space calculation was
not matched by the prior assessment; the supporting translation and
vanishing tools are known. The seven finite-field coefficient checks
passed, while the proof supplies the all-parameter assertion.
